from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

MoeGirlLink = 'https://zh.moegirl.org.cn'
SearchPageBase = 'https://zh.moegirl.org.cn/index.php?'
BaiduSearchBase = 'https://baike.baidu.com/search/none?word='
BaiduWikiBase = 'https://baike.baidu.com'


def makeSearchedPage(search):
    ReturnUrl = SearchPageBase + 'search=' + str(search) + '&title=Special'
    return ReturnUrl


def repairName(Name):
    EncodeName = str(Name.encode())
    if '\\' not in EncodeName:
        Name = Name.replace(' ', '+')
    else:
        Name = quote(Name, encoding='utf-8', errors='replace')
    return Name


def getResult(Name):
    name = repairName(Name)
    url = BaiduSearchBase + name
    html = urlopen(url)
    print("[SearchURL]:%s" % url)
    bs = BeautifulSoup(html, 'lxml')
    Link = bs.find('div', {'class': 'spell-correct'})
    if Link:
        return BaiduWikiBase + Link.find('a').attrs['href']
    status = bs.find('dl', {'class': 'search-list'})
    if status is None:
        if len(Name) >= 1:  # 递归查找，避免用户输入时多输入或输错了最后几个字，增加了容错性
            return getResult(Name[:len(Name) - 1])
        print("We have not find any Results.\nPlease Try again.")
        return None
    link = status.find('dd').find('a').attrs['href']
    if 'https://' not in link:
        link = BaiduWikiBase + link
    return link


def Distinguish_Tag(Temp):
    name = ''
    Flag = False
    for i in Temp:
        if re.match(re.compile('[a-z]', flags=re.I), i) or (re.match(' ', i) and Flag is True):
            Flag = True
            name += i
    print("[Final Match]%s" % name)
    return name


def findTag(url):
    print("[WikiURL]:%s" % url)
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    Temp = bs.find('dt', {'class': 'basicInfo-item name'}, text='外文名')
    if Temp is None:
        return None
    else:
        Temp = Temp.nextSibling.nextSibling
        Temp = str(Temp.text)
        Name = Distinguish_Tag(Temp=Temp)
    Tag = Name.replace(' ', '_')
    if '\n' in Tag:
        Tag = Tag[:Tag.rfind('\n')]
    Tag = Tag.upper()
    Tag = Tag.swapcase()
    print("[Tag]:%s" % Tag)
    return Tag


def findPerson(name):
    try:
        return findTag(getResult(name))
    except Exception as e:
        exit(e)
