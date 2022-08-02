import requests

url = "https://linktr.ee/validate/username"
name = "linktree"
payload={'username': 'console7331'}
files=[

]
headers = {
  'Cookie': 'countryCode=RU'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

resoult = []


print(response.text)
if response.text == {"result":"success"} : {
  
}