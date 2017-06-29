from bs4 import BeautifulSoup
import urllib.request

while True:
    url = urllib.request.urlopen('https://www.fizikist.com')
    soup = BeautifulSoup(url,'html.parser')
for tag in soup.find_all('a'):
    link = print(tag.get('href'))
    link = url
