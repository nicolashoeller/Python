
import requests

url = 'http://web-10.challs.olicyber.it/'

r = requests.options(url)

print(r.headers)

r = requests.patch(url)

print(r.headers)