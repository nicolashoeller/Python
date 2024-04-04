import requests
from bs4 import BeautifulSoup

url = 'http://web-12.challs.olicyber.it/'

response = requests.get(url)

print(response.text)

html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

pre = soup.find_all('pre')

print("flag: ", pre)