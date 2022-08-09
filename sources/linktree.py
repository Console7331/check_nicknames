import requests

url = "https://linktr.ee/validate/username"
name = "linktree"
payload={'username': 'console7331'}
files=[

]
headers = {
  'Cookie': 'countryCode=RU'
}

response_linktree = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response_linktree.text)

if response_linktree.text == {"result":"success"} : {
  
}