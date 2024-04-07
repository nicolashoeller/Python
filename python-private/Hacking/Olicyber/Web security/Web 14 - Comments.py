import requests
import re
from bs4 import BeautifulSoup

url = 'http://web-14.challs.olicyber.it/'

response = requests.get(url)

print(response.text)

html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

flag = soup.find_all(string=re.compile("flag"))

print(flag)