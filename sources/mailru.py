import requests
requests.urllib3.disable_warnings()
import json
from color import color

def mailru_check(mailru_domain, email, email_list):
	if mailru_domain == 'mail.ru':
		print (color('cyan')+'--------------------MAIL.RU----------------------'+color('end'))
	check_url = 'https://account.mail.ru/api/v1/user/exists'
	payload = 'email='+email+'@'+mailru_domain
	req = requests.get(check_url, timeout = 3, stream = False, verify = False, params = payload)
	resp_json = json.loads(req.content)
	status_bool = str(resp_json.get('body').get('exists'))
	resp_dict = {'True': color('red')+'[-] Email is already use!'+color('end'), 'False': color('green')+'[+] Email is available!'+color('end')}
	status = resp_dict.get(status_bool)
	print(u"{0} Domain: {1}".format(status,mailru_domain))
	if status_bool == 'False': 
		email_list.append(email+'@'+mailru_domain)