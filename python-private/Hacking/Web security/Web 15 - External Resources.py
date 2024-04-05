import requests
import re
from bs4 import BeautifulSoup

url = 'http://web-15.challs.olicyber.it/'

if url.endswith('/'):
    url = url.rstrip('/')

response = requests.get(url)
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')
links = soup.find_all('link')

print("-------------------", '\n')
print("Style files:", '\n')

for link in links:
    response = link.get('href')
    styleUrl = url + response
    print(styleUrl + '\n')
    response = requests.get(styleUrl)
    print(response.text + '\n')
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    flags = soup.find_all(string=re.compile("flag"))
    for flag in flags:
        match = re.search("flag{.*}", flag)
        if match:
            print("Flag:", match.group())
    print("-------------------", '\n')

response = requests.get(url)
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')
scripts = soup.find_all('script')

print("-------------------", '\n')
print("Src files:", '\n')

for script in scripts:
    response = script.get('src')
    srcUrl = url + response
    print(srcUrl + '\n')
    response = requests.get(srcUrl)
    print(response.text)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    flags = soup.find_all(string=re.compile("flag"))
    for flag in flags:
        match = re.search("flag{.*}", flag)
        if match:
            print("Flag:", match.group())
    print("-------------------", '\n')