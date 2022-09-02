import requests
from color import color

def habr_check(nickname, service_list):
    print (color('cyan')+'------------------HABR.COM---------------------'+color('end'))
    url = "https://habr.com/ru/users/"+nickname
    payload={}
    headers = {}
    response = requests.get(url, headers=headers, data=payload).status_code
    resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end'), '2': color('red')+'[-] Nickname is invalid!'+color('end')}
    if response == '404':
        print(resp_dict.get('1'), 'Service: Habr')
        service_list.append('Habr')
    elif response == '200':
        print(resp_dict.get('0'), 'Service: Habr')
    else: 
        print(resp_dict.get('2'), 'Service: Habr')
