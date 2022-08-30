from color import color
import requests
requests.urllib3.disable_warnings()
from bs4 import BeautifulSoup

def gmail_session():
	global result
	sess_url = 'https://accounts.google.com/signup/v2/webcreateaccount?service=mail&flowEntry=SignUp'
	response = requests.get(sess_url, timeout = 3, stream = False, verify = False)
	soup = BeautifulSoup(response.content, "html.parser")
	parse=soup.find_all('div',{"class": "JhUD8d SQNfcc vLGJgb"})[0].get('data-initial-setup-data')
	result=parse.split(',')[13]

def gmail_check(email, headers, email_list):
	global status
	headers['Google-Accounts-Xsrf'] = '1'
	headers['Content-Type'] = 'application/x-www-form-urlencoded'
	check_url = 'https://accounts.google.com/_/signup/webusernameavailability'
	payload = 'f.req=['+result+',"","","'+email+'"]'
	req = requests.post(check_url, data = payload, timeout = 3, stream = False, verify = False, headers = headers)
	status = req.content
	check_status = status.split(b',')[1]
	resp_dict = {b'2': color('red')+'[-] Email is already use!'+color('end'), b'1': color('green')+'[+] Email is available!'+color('end')}
	status = resp_dict.get(check_status)
	if status == None:
		status = resp_dict.get(b'2')
	print (u'{0} Domain: {1}'.format(status,'gmail.com'))
	if check_status == b'1':
		email_list.append(email+'@gmail.com')