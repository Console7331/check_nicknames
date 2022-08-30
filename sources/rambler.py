import requests
from color import color
requests.urllib3.disable_warnings()


def rambler_check(rambler_domain, email, email_list):
	if rambler_domain == 'rambler.ru':
		print (color('cyan')+'------------------RAMBLER.RU---------------------'+color('end'))
	headers = {'UserAgent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
	headers['Content-Type'] = 'application/json'
	check_url = 'https://id.rambler.ru/jsonrpc'
	payload = '{"rpc":"2.0","method":"Rambler::Id::login_available","params":[{"login":"'+email+'@'+rambler_domain+'"}]}'
	mail_status = {'0': color('red')+'[-] Email is already use!'+color('end'), '1': color('green')+'[+] Email is available!  '+color('end')}
	req = requests.post(check_url, data = payload, timeout = 3, stream = False, verify = False, headers = headers)
	status = req.content
	if b'"strerror":"user not exist"' in status:
		print (mail_status.get('1'), 'Domain:',rambler_domain)
		email_list.append(email+'@'+rambler_domain)
	else:
		print (mail_status.get('0') , 'Domain:',rambler_domain)