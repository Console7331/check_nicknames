import requests
requests.urllib3.disable_warnings()
import re
from bs4 import BeautifulSoup


def yandex_session(headers):
	global track_id, yandex_cookie, csrf_token
	headers['x-requested-with'] = 'XMLHttpRequest'
	sess_url = 'https://passport.yandex.ru/registration'
	response = requests.get(sess_url, timeout = 3, stream = False, verify = False, headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	track_id = soup.find_all('input',{'name':'track_id'})[0].get('value')
	csrf_token = re.search('"csrf":"(.+?)"', str(soup)).group(1)
	yandex_cookie = response.cookies.get_dict()

def yandex_check(email, headers, email_list, mail_status):
	headers['x-requested-with'] = 'XMLHttpRequest'
	check_url = 'https://passport.yandex.ru/registration-validations/login'
	payload = 'track_id='+track_id+'&login='+email+'&csrf_token='+csrf_token
	req = requests.post(check_url, data = payload, timeout = 3, stream = False, verify = False, headers = headers, cookies = yandex_cookie)
	status = req.content
	if b'login.not_available' in status:
		print (mail_status.get('0'), 'Domain: yandex.ru')
	else:
		print (mail_status.get('1'), 'Domain: yandex.ru')
		email_list.append(email+'@yandex.ru')
		email_list.append(email+'@ya.ru')