from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
MoeGirlLink = 'https://zh.moegirl.org.cn'
SearchPageBase = 'https://zh.moegirl.org.cn/index.php?'
BaiduSearchBase = 'https://baike.baidu.com/search/none?word='
BaiduWikiBase = 'https://baike.baidu.com'


def makeSearchedPage(search):
    ReturnUrl = SearchPageBase + 'search=' + str(search) + '&title=Special'
    return ReturnUrl


def repairName(Name):
    EncodeName = str(Name.encode())
    # print("EncodeName " + EncodeName)
    if '\\' not in EncodeName:
        Name = Name.replace(' ', '+')
    else:
        Name = quote(Name, encoding='utf-8', errors='replace')
    return Name


def getResult(Name):
    name = repairName(Name)
    url = BaiduSearchBase + name
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    Link = bs.find('div', {'class': 'spell-correct'})
    if Link:
        return BaiduWikiBase + Link.find('a').attrs['href']
    status = bs.find('dl', {'class': 'search-list'})
    if status is None:
        if len(Name) >= 1:
            return getResult(Name[:len(Name)-1])
        print("We have not find any Results.\nPlease Try again.")
        return None
    link = status.find('dd').find('a').attrs['href']
    return link


def findTag(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    Name = str(bs.find('br').nextSibling)
    if Name is None:
        exit("Ops! Wrong Name!")
    Tag = Name.replace(' ', '_')
    return Tag


def FindPerson(name):
    return findTag(getResult(name))

# print(FindPerson('御坂琴'))
