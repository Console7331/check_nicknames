import requests
requests.urllib3.disable_warnings()
from color import color

def vk_check(nickname, service_list):
    print (color('cyan')+'------------------VK.COM---------------------'+color('end'))
    url = "https://vk.com/"+nickname
    headers = {}
    response = requests.get(url, headers=headers).text
    resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end')}
    if '<title>404 Not Found</title>' in response:
        print(resp_dict.get('1'), 'Service: vk.com')
        service_list.append('vk.com')
    else:
        print(resp_dict.get('0'), 'Service: vk.com')