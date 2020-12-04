from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests


HomePage = 'https://zh.moegirl.org.cn'
LINKCHECK = []


def repairLink(url):
    url = str(url)
    if 'https://' in url:
        return url
    else:
        return HomePage + url


def DownloadPage(url):
    Picture = requests.get(url).content
    print(Picture)


def isPictureUrl(URL, urlForCheck):
    url = str(URL.encode())
    if '\\x' in url:
        print("NotRight" + str(url) + "NotRight")
        return False
    if 'px' in URL and 'px' in urlForCheck:
        if URL[:URL.rfind('/')] == urlForCheck[:urlForCheck.rfind('/')]:
            return int(URL[URL.rfind('/')+1:URL.rfind('px')]) > int(urlForCheck[urlForCheck.rfind('/')+1:urlForCheck.rfind('px')])
    return True


def getLinks(URL, TAG, TagDiv, TagRe):
    # print("Finding Links in page " + URL)
    urlForCheck = URL
    print("Trying to reach " + str(URL))
    bs = BeautifulSoup(urlopen(URL), 'lxml')
    ListLink = bs.find_all(TAG, {TagDiv: TagRe})
    ReturnList = []
    for link in ListLink:
        link = repairLink(link.attrs[TagDiv])
        if link not in ReturnList and isPictureUrl(link, urlForCheck):
            if link not in LINKCHECK:
                LINKCHECK.append(link)
                ReturnList.append(link)
    return ReturnList


def dfs(URL, depth):
    global LINKCHECK
    ListLink = getLinks(URL, 'a', 'href', re.compile('(png|jpg)$'))
    if len(ListLink) == 0:
        print("Downloading " + URL)
        # DownloadPage(URL)
        return
    for link in ListLink:
        dfs(link, depth+1)
    print(depth)
    print(URL)
    for link in ListLink:
        print(link)


BaseUrl = 'https://zh.moegirl.org.cn/%E9%9B%AA%E4%B9%8B%E4%B8%8B%E9%9B%AA%E4%B9%83'
dfs(BaseUrl, 1)
