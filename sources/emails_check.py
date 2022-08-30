import requests

requests.urllib3.disable_warnings()

from color import color
from sources.emails import mailru
from sources.emails import rambler
from sources.emails import yandex
from sources.emails import gmail

def check_emails(email):
	print (color('cyan')+'-------------------------------------------------'+color('end'))
	print (color('magenta')+'             EXISTENCE EMAIL CHECKER'+color('end'))
	print (color('cyan')+'-------------------------------------------------'+color('end'))
	print ('Check email: ', color('yellow')+email+color('end'))

	email_list = []
	mailru_domains = ['mail.ru','bk.ru','inbox.ru','list.ru','internet.ru']
	rambler_domains = ['rambler.ru','lenta.ru','autorambler.ru','myrambler.ru','ro.ru','rambler.ua']

	yandex.yandex_session()
	yandex.yandex_check(email, email_list)

	for domain in mailru_domains:
		mailru.mailru_check(domain, email, email_list)

	gmail.gmail_session()
	gmail.gmail_check(email, email_list)

	for domain in rambler_domains:
		rambler.rambler_check(domain, email, email_list)

	print (color('cyan')+'-------------------------------------------------'+color('end'))

	outputfile = open('output.txt', 'a')
	outputfile.write('All avaliable emails:')
	outputfile.writelines(str(email_list)+'\n')
	outputfile.close()