import requests
from bs4 import BeautifulSoup

url = 'http://web-13.challs.olicyber.it/'

response = requests.get(url)

print(response.text)

html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

tags = soup.find_all('span')

for tag in tags:
    print(tag.text)