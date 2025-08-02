import requests
import random
from colorama import Fore, Style
from sites import urls

cookies = {
    "sessionid": "d8a7e9c8d01e4c96bb1b6c3fc7fa40c7",
    "csrftoken": "a1b2c3d4e5f6g7h8i9j0klmnopqrstuv",
    "userid": "1283746583",
    "device_id": "web-bc9a8f2e9c194812b345fd8e9a2d79b7",
    "auth_token": "e8f1a2b3c4d5e6f7g8h9i0j1k2l3m4n5",
    "visitor_id": "v_09f3a7b6c5d4e3f2g1h0i9j8k7l6m5n4",
    "logged_in": "true",
    "theme": "dark",
    "lang": "en",
    "remember_me": "true",
    "refresh_token": "rt_1234567890abcdef1234567890abcdef",
    "cart_id": "ci_abcdef1234567890abcdef1234567890",
    "checkout_token": "ct_123abc456def789ghi012jkl",
    "last_visit": "2025-07-30T20:59:00Z",
    "tracking_id": "trk_a1b2c3d4e5f67890",
    "uuid": "9c0b1a2e-3d4f-5g6h-7i8j-9k0l1m2n3o4p",
    "client_id": "ci_2025-07-30_21:00",
    "analytics_token": "anl_abc123xyz456",
    "ab_test_group": "B",
    "experiments": "exp1:active;exp2:inactive",
    "push_token": "ptkn_abcdef0123456789",
    "fingerprint": "fp_1122334455667788",
    "timezone": "Europe/Moscow",
    "is_bot": "false",
    "from_landing": "true",
}

user_agents = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1) Gecko/20061121 BonEcho/2.",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4pre) Gecko/20070410 BonEcho/2.0.0.4pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1) Gecko/20060930 BonEcho/2.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070213 BonEcho/2.0.0.2pre",
    "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.4463.1220 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-S906B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.176"
]

headers = {
    "User-Agent": random.choice(user_agents),
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1"
}

found_account = []

print(r"""
 _   _                      _____                       
| \ | |                    / ____|                      
|  \| | __ _ _ __ ___   ___| (___   ___  __ _ _ __.  
| . ` |/ _` | '_ ` _ \ / _ \\___ \ /  _\/ _` | '_  \  
| |\  | (_| | | | | | |  __/____) |  |_/ (_| | | | | 
|_| \_|\__,_|_| |_| |_|\___|_____/ \___|\__,_|_| |_| 
""")

username = input("Введите юзернейм: ").strip()

if not username:
    print("никнейм отсутствует")
    input("press enter to exit...")
    exit()

def check_account(bazo_url, username):
    try:
        url = bazo_url + username
        response = requests.get(url, headers=headers, cookies=cookies ,timeout=5)
        if response.status_code == 200:
            found_account.append(url)
            print(f"{Fore.GREEN}[+] Акк зареган {url} {Style.RESET_ALL}")
            return True
        elif response.status_code == 404:
            print(f"{Fore.RED}Акк не найден {url}")
            return False
        else:
            print(f'error: {response.status_code}')
            return False
    except Exception as e:
        print(f'error: {e}')

for url in urls:
    check_account(url, username)

with open("result.txt", "w") as f:
    for account in found_account:
        f.write(account + "\n")
