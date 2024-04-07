import requests
import json

session = requests.Session()

url1 = 'http://web-11.challs.olicyber.it/login'
url2 = 'http://web-11.challs.olicyber.it/flag_piece'

payload = {'username': 'admin', 'password': 'admin'}

for i in range(0, 4):
    params = {'index': i}
    request = session.post(url1, json=payload)
    token = request.json().get('csrf')
    print("Token:", token)
    get_request = session.get(url2, params=params, headers={'X-CSRF-Token': token})
    print(get_request.text)