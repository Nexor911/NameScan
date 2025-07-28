import requests
from sites import urls

username = input("Введите юзернейм: ").strip()


def check_account(bazo_url, username):
    try:
        url = bazo_url + username
        response = requests.get(url, timeout=1)
        if response.status_code == 200:
            print(f"Акк зареган {url}")
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
