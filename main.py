import requests
import random
from colorama import Fore, Style
from sites import urls
import json

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
	"Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)"
	"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/88.0.4298.0 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
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

working_proxies = []

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

use_proxy = input("Использовать прокси (y/n): ")

def download_proxies():
    url = "https://www.proxy-list.download/api/v1/get?type=http"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            proxy_list = response.text.strip().split('\r\n')
            print(f"[✓] Загружено {len(proxy_list)} прокси с сайта.")
            return proxy_list
        else:
            print(f"[✗] Не удалось получить прокси: {response.status_code}")
            return []
    except Exception as e:
        print(f"[✗] Ошибка при загрузке прокси: {e}")
        return []

def check_proxy(proxy_url):
    try:
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=3)
        if response.status_code == 200:
            print(f"[+] Рабочий: {proxy_url} → IP: {response.json()['origin']}")
            return True
        else:
            print(f"[-] Не работает: {proxy_url}")
            return False
    except Exception as e:
        print(f"[-] Ошибка: {proxy_url} → {e}")
        return False


def check_account(bazo_url, username):
    try:
        url = bazo_url + username
        if use_proxy == "y" and working_proxies:
            proxy_url = random.choice(working_proxies)
            proxies = {
                "http": proxy_url,
                "https": proxy_url
            }
            response = requests.get(url, headers=headers, cookies=cookies, proxies=proxies, timeout=5)
        else:
            response = requests.get(url, headers=headers, cookies=cookies, timeout=5)

        if response.status_code == 200:
            found_account.append(url)
            print(f"{Fore.GREEN}[+] Акк зареган {url} {Style.RESET_ALL}")
            return True
        elif response.status_code == 404:
            print(f"{Fore.RED}Акк не найден {url} {Style.RESET_ALL}")
            return False
        else:
            print(f'error: {response.status_code}')
            return False
    except Exception as e:
        print(f'error: {e}')

if use_proxy == "y":
    proxy_list = download_proxies()
    for proxy in proxy_list:
        if check_proxy(proxy):
            working_proxies.append(proxy)

if not working_proxies:
    print("Нету рабочих прокси")
    use_proxy = "n"

for url in urls:
    check_account(url, username)

format_file = input("В каком формате сохранить результат? (txt/json): ")

if format_file not in ["txt", "json"]:
    print("Неверный выбор формата файла")
    input("press enter to exit...")
    exit()

if format_file == "txt":
    with open(f"result.txt", "w") as f:
        for account in found_account:
            f.write(account + "\n")

elif format_file == "json":
    with open(f"result.json", "w") as f:
        json.dump(found_account, f, indent=4, ensure_ascii=False)
