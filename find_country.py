def country():
    import requests
    import json

    global country
    request_url = 'https://geolocation-db.com/jsonp/'
    # https://ipinfo.io/json
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    country = result.get('country_code')
    # country = result.get('country')

def checkip_fullinfo():
    import requests
    import json

    request_url = 'https://geolocation-db.com/jsonp/'
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    country = result.get('country_code')

    IP=result.get('IPv4')
    city = result.get('city')
    country=result.get('country_code')
    region=result.get('country_name')
    print('Your IP detail\n ')
    print('IP : {3} \nRegion : {0} \nCountry : {1} \nCity : {2} \n'.format(region,country,city,IP))