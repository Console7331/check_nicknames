import requests
requests.urllib3.disable_warnings()
from color import color

def instagram_check(nickname, service_list):
    url = "https://t.me/"+nickname
    headers = {}
    response = requests.get(url, headers=headers).text
    resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end')}
    if '<meta name="robots" content="noindex, nofollow">' in response:
        print(resp_dict.get('1'), 'Service: Instagram')
        service_list.append('Instagram')
    else:
        print(resp_dict.get('0'), 'Service: Instagram')