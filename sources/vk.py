import requests
from color import color

def vk_check(nickname, service_list):
    url = "https://vk.com/"+nickname
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end')}
    if b'<title>404 Not Found</title>' in response._content:
        print(resp_dict.get('1'), 'Service: vk.com')
        service_list.append('vk.com')
    else:
        print(resp_dict.get('0'), 'Service: vk.com')