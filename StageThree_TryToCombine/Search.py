from urllib.request import urlopen
from bs4 import BeautifulSoup
HomePage = 'https://zh.moegirl.org.cn'
SearchPageBase = 'https://zh.moegirl.org.cn/index.php?'


def makeSearchedPage(search):
    ReturnUrl = SearchPageBase + 'search=' + search + '&title=Special'
    return ReturnUrl


def getFirstResult(Name):
    html = urlopen(makeSearchedPage(Name))
    bs = BeautifulSoup(html, 'lxml')
    link = bs.find('a', {'data-serp-pos': '0'}).attrs['href']
    StartUrl = HomePage + link
    return StartUrl


print(getFirstResult('Yukinoshita'))
# for link in bs.body.find_all('a', {'href': ''}):
#     print(link)
#     print('url')
#     print(link.attrs['href'])
