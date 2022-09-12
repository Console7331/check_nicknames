import requests
from color import color

def facebook_check(nickname, service_list):
    print (color('cyan')+'------------------FACEBOOK.COM---------------------'+color('end'))
    url = "https://facebook.com/"+nickname
    payload={}
    headers = {}
    response = requests.get(url, headers=headers, data=payload).status_code
    resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end'), '2': color('red')+'[-] Nickname is invalid!'+color('end')}
    #resp_dict = {'0':'[-] Nickname is already use!', '1': '[+] Nickname is available!', '2':'[-] Nickname is invalid!'}
    if response == 404:
        print(resp_dict.get('1'), 'Service: Facebook')
        service_list.append('Facebook')
        print('Before changing nickname you need to read Facebook Page Username Requirements')
    elif response == 200:
        print(resp_dict.get('0'), 'Service: Facebook')
    else: 
        print(resp_dict.get('2'), 'Service: Facebook')

