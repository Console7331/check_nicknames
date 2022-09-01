import requests
from color import color
requests.urllib3.disable_warnings()
import re
from bs4 import BeautifulSoup


def yandex_session():
	global yandex_track_id, yandex_cookie, yandex_csrf_token
	headers = {'UserAgent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
	headers['x-requested-with'] = 'XMLHttpRequest'
	sess_url = 'https://passport.yandex.ru/registration'
	response = requests.get(sess_url, timeout = 3, stream = False, verify = False, headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	yandex_track_id = soup.find_all('input',{'name':'track_id'})[0].get('value')
	yandex_csrf_token = re.search('"csrf":"(.+?)"', str(soup)).group(1)
	yandex_cookie = response.cookies.get_dict()

def yandex_check(email, email_list):
	print(color('cyan')+'-------------------YANDEX.RU---------------------'+color('end'))
	mail_status = {'0': color('red')+'[-] Email is already use!'+color('end'), '1': color('green')+'[+] Email is available!  '+color('end')}
	headers = {'UserAgent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
	headers['x-requested-with'] = 'XMLHttpRequest'
	check_url = 'https://passport.yandex.ru/registration-validations/login'
	payload = 'track_id='+yandex_track_id+'&login='+email+'&csrf_token='+yandex_csrf_token
	req = requests.post(check_url, data = payload, timeout = 3, stream = False, verify = False, headers = headers, cookies = yandex_cookie)
	status = req.content
	if b'login.not_available' in status:
		print (mail_status.get('0'), 'Domain: yandex.ru')
	else:
		print (mail_status.get('1'), 'Domain: yandex.ru')
		email_list.append(email+'@yandex.ru')
		email_list.append(email+'@ya.ru')