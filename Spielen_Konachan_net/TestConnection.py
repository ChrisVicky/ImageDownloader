from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
url = 'https://konachan.net'
requ = requests.get(url)
print(requ)


html = urlopen(url)
bs = BeautifulSoup(html, 'lxml')
print(bs)


