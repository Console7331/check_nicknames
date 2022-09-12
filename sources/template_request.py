import requests
from color import color

def service_check(nickname, service_list):
    print (color('cyan')+'------------------________---------------------'+color('end'))
    url = "                  "+nickname
    payload={}
    headers = {}
    response = requests.get(url, headers=headers, data=payload).status_code
    resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end'), '2': color('red')+'[-] Nickname is invalid!'+color('end')}
    if response == 404:
        print(resp_dict.get('1'), 'Service: ________')
        service_list.append('________')
    elif response == 200:
        print(resp_dict.get('0'), 'Service: ________')
    else: 
        print(resp_dict.get('2'), 'Service: ________')
