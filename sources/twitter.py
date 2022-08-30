import requests
requests.urllib3.disable_warnings()
import http.client
from color import color

def  twitter_check(nickname, service_list):
    conn = http.client.HTTPSConnection("twitter.com")
    payload = ''
    headers = {
    'authorization': ' Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'cookie': 'guest_id=v1%3A166185093047040319; ct0=39247a039b8922eb2846276abc46f8bb; gt=1564542323010293761; _ga=GA1.2.1603557634.1661850932; _gid=GA1.2.783707880.1661850932',
    'x-csrf-token': ' 39247a039b8922eb2846276abc46f8bb'
    }    
    print (color('cyan')+'------------------TWITTER.COM---------------------'+color('end'))
    resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end'), '2': color('red')+'[-] Nickname is invalid!'+color('end')}
    conn.request("GET", "/i/api/i/users/username_available.json?username="+nickname, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

    if b'"reason":"taken"' in data:
        print (resp_dict.get('0'), 'Twitter.com')
    elif (b'"reason":"invalid_username"' in data) or (b'"reason":"is_banned_word"' in data):
        print (resp_dict.get('2'), 'Twitter.com')
    elif b'"reason":"available"' in data:
        print (resp_dict.get('1'), 'Twitter.com')
        service_list.append('Twitter.com')
