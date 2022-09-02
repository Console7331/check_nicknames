import requests
from color import color

def habr_check(nickname, service_list):
    print (color('cyan')+'------------------HABR.COM---------------------'+color('end'))
    url = "https://habr.com/ru/users/"+nickname
    payload={}
    headers = {}
    response = requests.get(url, headers=headers, data=payload).text
    resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end')}
    if '<h1 class="tm-error-message__title">' in response:
        print(resp_dict.get('1'), 'Service: Habr')
        service_list.append('Habr')
    else:
        print(resp_dict.get('0'), 'Service: Habr')
