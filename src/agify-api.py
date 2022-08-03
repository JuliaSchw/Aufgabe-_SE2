import requests

url = 'https://api.agify.io'
params = {'country_id': 'DE', 'name': 'julia'}

response = requests.post(url, params)

print('response code: ', response.status_code)
print('response json: ', response.json())

print(response)
