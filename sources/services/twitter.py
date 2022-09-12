import requests
requests.urllib3.disable_warnings()
import http.client
from color import color

def  twitter_check(nickname, service_list):
    conn = http.client.HTTPSConnection("twitter.com")
    payload = ''
    headers = {
    'authorization': ' Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'cookie': ' guest_id=v1%3A166143208836379265; _gid=GA1.2.602906032.1661432092; gt=1562785587244937217; external_referer=padhuUp37zhU%2Fo1ilYwCNOmtabS4UqDS|0|8e8t2xd8A2w%3D; at_check=true; eu_cn=1; des_opt_in=Y; _gcl_au=1.1.764735199.1661435924; mbox=session#3283a60cb08c49b4ad15a81d5338612f#1661437879|PC#3283a60cb08c49b4ad15a81d5338612f.34_0#1724680819; _ga_34PHSZMC42=GS1.1.1661435923.1.1.1661436091.0.0.0; _ga=GA1.2.1968826528.1661432092; _sl=1; kdt=pWawv6L6WXev3WpleA23WPJhKXfAQLr1yHJoA6Zk; auth_token=5bf81ca2e8dccf87a68ab1a31beeee4deaaf20c4; ct0=1c8126b7193168e266f261e49dd2587f7c67b63f34b6c961039bc65af09bb6628b947033a370298e4c435952dd5a9f6ccf9ee47722da216cf241f5edab9580ff88c0c4fd0dbc362a89f29f88a3272ec5; att=1-51InM5wguHL7O2ocm2gDGdvZm2zAK8l66N3tvWZl; twid=u%3D2863471385; lang=ru; _twitter_sess=BAh7CyIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoHaWQiJWJlMmQ0NWRkZGE2M2ZkODI0YmUwNDg0%250AN2Y3YmQ0MThiOg9jcmVhdGVkX2F0bCsIIQ1Y1YIBOgxjc3JmX2lkIiVkZWJm%250AZjZmYTNmNWMxZTY5MmNiNzUxYjZiNDYyNDkxNTofbGFzdF9wYXNzd29yZF9j%250Ab25maXJtYXRpb24iFTE2NjE0MzY4NjI1ODUwMDA6HnBhc3N3b3JkX2NvbmZp%250Acm1hdGlvbl91aWQiDzI4NjM0NzEzODU%253D--3d6490a4a87b21a8f750b33957afbbdf138a465b; guest_id=v1%3A166184907809452721',
    'x-csrf-token': ' 1c8126b7193168e266f261e49dd2587f7c67b63f34b6c961039bc65af09bb6628b947033a370298e4c435952dd5a9f6ccf9ee47722da216cf241f5edab9580ff88c0c4fd0dbc362a89f29f88a3272ec5'
    }    
    print (color('cyan')+'------------------TWITTER.COM---------------------'+color('end'))
    resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end'), '2': color('red')+'[-] Nickname is invalid!'+color('end')}
    conn.request("GET", "/i/api/i/users/username_available.json?username="+nickname, payload, headers)
    res = conn.getresponse()
    data = res.read()

    if b'"reason":"taken"' in data:
        print (resp_dict.get('0'), 'Twitter.com')
    elif (b'"reason":"invalid_username"' in data) or (b'"reason":"is_banned_word"' in data) or (b'"valid":false' in data):
        print (resp_dict.get('2'), 'Twitter.com')
    elif b'"reason":"available"' in data:
        print (resp_dict.get('1'), 'Twitter.com')
        service_list.append('Twitter.com')
    

    ######################################
    #Need to fix method below
    # because this method creates csrf token and cookie by yourself
    ######################################
def twitter_check_second(nickname, service_list):
    #print (color('cyan')+'------------------TWITTER.COM---------------------'+color('end'))
    headers = {'UserAgent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
    headers['x-requested-with'] = 'XMLHttpRequest'
    sess_url = 'https://www.twitter.com/'
    response_sess = requests.get(sess_url, headers = headers)
    twitter_cookie = response_sess.cookies.get_dict()
    print(twitter_cookie)
    print(response_sess.cookies)
    headers['authorization'] = twitter_cookie.get('authorization')
    headers['x-csrf-token'] = twitter_cookie.get('x-csrf-token')
    url = "https://www.twitter.com/i/api/i/users/username_available.json?username="+nickname
    payload = ''
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'
    response = requests.get(url, headers=headers, data=payload, cookies=twitter_cookie)
    #resp_dict = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!'+color('end'), '2': color('red')+'[-] Nickname is invalid!'+color('end')}
    resp_dict = {'0': '[-] Nickname is already use!', '1':'[+] Nickname is available!', '2': '[-] Nickname is invalid!'}
    if '"reason":"taken"' in response.text:
        print(resp_dict.get('0'), 'Service: Twitter')
    elif response.status_code != 200:
        print(resp_dict.get('2'), 'Service: Twitter')
    else:
        print(resp_dict.get('1'), 'Service: Twitter')
        service_list.append('Twitter')


#empty_services = []
#twitter_check_second(nickname='haxgajhxgfhj', service_list=empty_services)