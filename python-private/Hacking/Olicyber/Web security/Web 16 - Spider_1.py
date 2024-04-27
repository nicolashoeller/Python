import requests
from bs4 import BeautifulSoup
import re

def crawl(url, max_depth=4, depth=0):
    if depth > max_depth:
        return

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Crawling:", url)

    links = soup.find_all('a', href=True)
    for link in links:
        next_url = link['href']
        if not next_url.startswith('http'):
            next_url = url + next_url
        
        response = requests.get(next_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for h_tag in ['h1']:
            tags = soup.find_all(h_tag)
            for tag in tags:
                match = re.search(r'flag\{.*?\}', tag.text)
                if match:
                    print("Flag:", match.group())

        crawl(next_url, max_depth, depth + 1)

start_url = 'http://web-16.challs.olicyber.it/'

if start_url.endswith('/'):
    start_url = start_url.rstrip('/')

crawl(start_url)