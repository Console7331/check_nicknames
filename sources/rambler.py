import requests
requests.urllib3.disable_warnings()


def rambler_check(rambler_domain, email, email_list, headers, mail_status):
	headers['Content-Type'] = 'application/json'
	check_url = 'https://id.rambler.ru/jsonrpc'
	payload = '{"rpc":"2.0","method":"Rambler::Id::login_available","params":[{"login":"'+email+'@'+rambler_domain+'"}]}'
	req = requests.post(check_url, data = payload, timeout = 3, stream = False, verify = False, headers = headers)
	status = req.content
	if b'"strerror":"user not exist"' in status:
		print (mail_status.get('1'), 'Domain:',rambler_domain)
		email_list.append(email+'@'+rambler_domain)
	else:
		print (mail_status.get('0') , 'Domain:',rambler_domain)