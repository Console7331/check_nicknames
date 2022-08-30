import requests
requests.urllib3.disable_warnings()
from color import color

def linktree_check(nickname, service_list):
  print (color('cyan')+'------------------LINKTR.EE---------------------'+color('end'))
  url = "https://linktr.ee/validate/username"
  payload={'username': nickname}
  files=[]
  headers = {'Cookie': 'countryCode=RU'}
  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end')}
  if b'{"result":"success"}' in response._content:
    print(resp_dict.get('1'), 'Service: linktr.ee')
    service_list.append('linktr.ee')
  else:
    print(resp_dict.get('0'), 'Service: linktr.ee')