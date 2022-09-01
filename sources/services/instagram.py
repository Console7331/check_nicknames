import requests
requests.urllib3.disable_warnings()
from color import color

def instagram_check(nickname, service_list):
    print (color('cyan')+'------------------INSTAGRAM.COM---------------------'+color('end'))
    headers = {'UserAgent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
    headers['x-requested-with'] = 'XMLHttpRequest'
    sess_url = 'https://www.instagram.com/'
    response_sess = requests.get(sess_url, headers = headers)
    instagram_cookie = response_sess.cookies.get_dict()
    headers['x-csrftoken'] = instagram_cookie.get('csrftoken')
    url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
    payload='username='+nickname
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'
    response = requests.post(url, headers=headers, data=payload, cookies=instagram_cookie)
    resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end')}
    if b'"code": "username_is_taken"' in response:
        print(resp_dict.get('0'), 'Service: Instagram')
    else:
        print(resp_dict.get('1'), 'Service: Instagram')
        service_list.append('Instagram')