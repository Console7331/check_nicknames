#created by p0z
#edited by Console

import os
import sys
import requests
requests.urllib3.disable_warnings()

from color import color
from sources import mailru
from sources import rambler
from sources import yandex
from sources import gmail


def check_emails(email_input):
	email = email_input

	headers = {'UserAgent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
	mail_status = {'0': color('red')+'[-] Email is already use!'+color('end'), '1': color('green')+'[+] Email is available!  '+color('end')}
	email_list = []

	print (color('cyan')+'-------------------------------------------------'+color('end'))
	print (color('magenta')+'             EXISTENCE EMAIL CHECKER'+color('end'))
	print (color('cyan')+'-------------------------------------------------'+color('end'))

	print ('Check email: ', color('yellow')+email+color('end'))

	print(color('cyan')+'-------------------YANDEX.RU---------------------'+color('end'))
	yandex.yandex_session(headers)
	yandex.yandex_check(email, headers, email_list, mail_status)

	print (color('cyan')+'--------------------MAIL.RU----------------------'+color('end'))
	mailru_domains = ['mail.ru','bk.ru','inbox.ru','list.ru','internet.ru']
	for domain in mailru_domains:
		mailru.mailru_check(domain, email, email_list)

	print (color('cyan')+'-------------------GMAIL.COM---------------------'+color('end'))
	gmail.gmail_session()
	gmail.gmail_check(email, headers, email_list)

	print (color('cyan')+'------------------RAMBLER.RU---------------------'+color('end'))
	rambler_domains = ['rambler.ru','lenta.ru','autorambler.ru','myrambler.ru','ro.ru','rambler.ua']
	for domain in rambler_domains:
		rambler.rambler_check(domain, email, email_list, headers, mail_status)

	print (color('cyan')+'-------------------------------------------------'+color('end'))

	outputfile = open('output.txt', 'w+')
	outputfile.write('All avaliable emails:')
	outputfile.writelines(str(email_list)+'\n')
	outputfile.close()