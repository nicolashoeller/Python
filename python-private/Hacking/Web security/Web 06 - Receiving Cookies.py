import requests

session = requests.Session()

url1 = 'http://web-06.challs.olicyber.it/token'
url2 = 'http://web-06.challs.olicyber.it/flag'

session.get(url1)

r = session.get(url2)

print(r.text);