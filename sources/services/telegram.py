import requests
requests.urllib3.disable_warnings()
from color import color

def telegram_check(nickname, service_list):
    print (color('cyan')+'------------------TELEGRAM---------------------'+color('end'))
    url = "https://t.me/"+nickname
    headers = {}
    response = requests.get(url, headers=headers).text
    resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end')}
    if '<meta name="robots" content="noindex, nofollow">' in response:
        print(resp_dict.get('1'), 'Service: Telegram')
        service_list.append('Telegram')
    else:
        print(resp_dict.get('0'), 'Service: Telegram')