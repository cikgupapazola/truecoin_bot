import requests
import time
from colorama import Fore, Style

#ambil auth-key dari inspect-> network -> headers -> request headers -> auth-key -> copy value
auth_key = [
    '4b3a..............',
    '.............'
]

#ambil id tele dari bot https://t.me/CekIDTelegram_bot
user_id = [
    000000,
    000000
]

url_login = 'https://api.true.world/api/auth/signIn'
url_spin = 'https://api.true.world/api/game/spin'

print(Fore.GREEN + """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█▀▄▀█░▄▄▀█░██░█▀▄▄▀█▄░▄█░▄▄█░▄▀▄░██▄██░██░▄▄█
█░█▀█░▀▀▄█░▀▀░█░▀▀░██░██▄▄▀█░█▄█░██░▄█░██░▄▄█
██▄██▄█▄▄█▀▀▀▄█░█████▄██▄▄▄█▄███▄█▄▄▄█▄▄█▄▄▄█
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
*********************************************
******** BOT TRUECOIN BY CRYPTSMILE *********
*********************************************
\n""" + Style.RESET_ALL)

while True:
    for auth, user in zip(auth_key, user_id):
        headers_login = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,id;q=0.8',
            'auth-key': auth,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'downlink': '1.55',
            'origin': 'https://bot.true.world',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://bot.true.world/',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sendtime': '2024-07-12T15:42:05Z',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }

        data = {
            'lang': 'en',
            'userId': user
        }

        response_login = requests.post(url_login, headers=headers_login, json=data)

        if response_login.status_code != 200:
            print(Fore.RED + f"Login failed for user {user}: {response_login.text}" + Style.RESET_ALL)
            continue

        try:
            response_login_json = response_login.json()
        except ValueError:
            print(Fore.RED + f"Invalid JSON response for user {user}: {response_login.text}" + Style.RESET_ALL)
            continue

        if 'token' not in response_login_json:
            print(Fore.RED + f"No token in response for user {user}: {response_login_json}" + Style.RESET_ALL)
            continue

        token = response_login_json['token']

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,id;q=0.8',
            'auth-key': auth,
            'authorization': 'Bearer ' + token,
            'cache-control': 'no-cache',
            'downlink': '3.9',
            'multiply': '1',
            'origin': 'https://bot.true.world',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://bot.true.world/',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sendtime': '2024-07-12T15:57:09Z',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }

        response_spin = requests.get(url_spin, headers=headers)

        print(Fore.YELLOW + "====================================" + Style.RESET_ALL)
        print(Fore.YELLOW + 'Username        : ' + response_login_json['user']['username'] + Style.RESET_ALL)
        print(Fore.YELLOW + 'Spin Tersisa    : ', response_login_json['user']['currentSpins'], Style.RESET_ALL)
        print(Fore.YELLOW + 'Jumlah Truecoin : ', response_login_json['user']['coins'], Style.RESET_ALL)
        print(Fore.YELLOW + "====================================" + Style.RESET_ALL)

        if response_login_json['user']['currentSpins'] == 0:
            print('Spin Habis')
        else:
            try:
                result = response_spin.json()['result']
                if result['winType'] == 'coins':
                    print('Menang sebanyak : ', result['coins'], 'Coins')
                else:
                    print('No Coins')
            except (KeyError, ValueError):
                print(Fore.RED + "Error parsing spin response: " + response_spin.text + Style.RESET_ALL)

        time.sleep(1)
