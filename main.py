import requests
from sites import urls

headers = {
    "User-Agent": "Mozilla/5.0 (VenturaCounty; Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.89"
}

found_account = []

username = input("Введите юзернейм: ").strip()

if not username:
    print("никнейм отсутствует")
    input("press enter to exit...")
    exit()

def check_account(bazo_url, username):
    try:
        url = bazo_url + username
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            found_account.append(url)
            print(f"[+] Акк зареган {url}")
            return True
        elif response.status_code == 404:
            print(f"Акк не найден {url}")
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
