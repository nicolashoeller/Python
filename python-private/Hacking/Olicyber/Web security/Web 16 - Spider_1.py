import requests
from bs4 import BeautifulSoup

def main():
    url = 'http://web-16.challs.olicyber.it/'

    if url.endswith('/'):
        url = url.rstrip('/')
    
    soup = getRequest(url)
    tags = soup.find_all('a')
    for tag in tags:
        newUrl = getNewUrl(url, tag)
        print(newUrl)
        print("Redirecting...")
    

def getRequest(url):
    respone = requests.get(url)
    html_doc = respone.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup

def getNewUrl(url, tag):
    href = tag.get('href')
    if href:
        newUrl = url + href
        return newUrl
    

if __name__ == '__main__':
    main()