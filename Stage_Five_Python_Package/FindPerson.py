from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
MoeGirlLink = 'https://zh.moegirl.org.cn'
SearchPageBase = 'https://zh.moegirl.org.cn/index.php?'
BaiduSearchBase = 'https://baike.baidu.com/search/none?word='


def makeSearchedPage(search):
    ReturnUrl = SearchPageBase + 'search=' + str(search) + '&title=Special'
    return ReturnUrl


def repairName(Name):
    EncodeName = str(Name.encode())
    print("EncodeName " + EncodeName)
    if '\\' not in EncodeName:
        Name = Name.replace(' ', '+')
    else:
        Name = quote(Name, encoding='GBK')
    return Name


def getFirstResult(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    status = bs.find('a', {'data-serp-pos': '0'})
    if status is None:
        print("We have not find any Results.\nPlease Try again.")
        return None
    link = status.attrs['href']
    StartUrl = MoeGirlLink + link
    return StartUrl


def ifResults(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    status = bs.find('a', {'data-serp-pos': '0'})
    if status is None:
        return False
    return True


def findTag(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    line = bs.find('span', {'itemprop': 'name'})
    if line is None:
        exit("Ops! Wrong Name!")
    line = str(line)
    Name = line[line.rfind('(')+1: line.rfind(')')]
    Tag = Name.replace(' ', '_')
    return Tag


def FindPerson(name):
    name = repairName(name)
    print("Name " + name)
    InitialUrl = makeSearchedPage(name)
    print("InitialUrl "+InitialUrl)
    if ifResults(InitialUrl):
        url = getFirstResult(InitialUrl)
    else:
        url = InitialUrl
    return findTag(url)
