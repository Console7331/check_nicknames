import requests
import inputfile

url = "https://account.mail.ru/api/v1/user/exists"

payload={'email': inputfile.email_input + '@mail.ru'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)