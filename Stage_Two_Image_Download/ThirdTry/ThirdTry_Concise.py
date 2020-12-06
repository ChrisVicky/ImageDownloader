from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import cv2
import requests
import numpy
import os
import difflib

HomePage = 'https://zh.moegirl.org.cn'
Num = 0

def createFile(name):
    Path = os.getcwd() + '\\' + name
    if os.path.exists(Path):
        return
    os.mkdir(Path)


def getFilePath(name):
    return os.getcwd() + '\\' + name + '\\'


LocalPath = getFilePath('picture')
createFile('picture')



def savePicture(savePicturePicture, num):
    AllName = 'Picture'
    fileName = LocalPath + AllName + str(num) + '.png'
    print(fileName)
    fp = open(fileName, 'wb')
    fp.write(savePicturePicture)
    # savePicturePicture = cv2.imread(fileName)
    # cv2.imshow(url, savePicturePicture)
    # cv2.waitKey(0)
    fp.close()


def getHtml(url):
    return urlopen(url)


def getBs(html):
    return BeautifulSoup(html, 'lxml')

HomePage = 'https://zh.moegirl.org.cn'
def getNewUrlChecked(b,url):
    b = HomePage
    if 'https://' in url:
        return url
    else:
        return HomePage + url


def getContent(url):
    return requests.get(url).content


def getSecondUrl(bs, tag, div1, rec):
    return bs.find_all(tag, {div1: rec})


def getPicture(UrlList, tag, div, num, rec):
    NewNum = 1
    LinkList = []
    if num == -1:
        return
    for url in UrlList:
        bs = getBs(getHtml(url))
        for Link in getSecondUrl(bs, tag, div, rec):
            newUrl = getNewUrlChecked(HomePage, Link.attrs[div])
            if 'File' in newUrl or newUrl in LinkList:
                continue
            LinkList.append(newUrl)
            print(newUrl)
            pic = getContent(newUrl)
            # print(pic)
            bs2 = getBs(getHtml(newUrl))
            # savePicture(pic, NewNum)
            NewNum += 1


def getPictureUrl(tag, div1, rec, bs):
    LIST = []
    List_Number = -1
    print(len(bs.find_all(tag,{div1: rec})))
    for Link in bs.find_all(tag, {div1: rec}):
        if div1 in Link.attrs:
            newUrl = getNewUrlChecked(HomePage, Link.attrs[div1])
            if newUrl in LIST:
                continue
            else:
                List_Number += 1
                LIST.append(newUrl)
                print(newUrl)
    getPicture(LIST, tag, div1, List_Number, rec)


Urls_Download = set()
pages = set()


def SeekForUrl(url):
    global Num
    global Urls_Download
    global pages
    if url in pages:
        return
    pages.add(url)
    print("=============================")
    print("Current Url = " + url)
    print("=============================")
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')

    Targets = bs.find_all('a', {'href': re.compile('(png|jpg)')})
    # Targets = bs.find_all('a' or 'img', {'href': re.compile('(png|jpg)')} or {'src': re.compile('(png|jpg)')})
    num = len(Targets)
    print(num)
    if num == 0:
        downloadLink = url
        pages.add(downloadLink)
        Urls_Download.update(downloadLink)
        print("SUCCESS = " + downloadLink)
        savePicture(getContent(downloadLink), Num)
        Num += 1
        return
    for tag in ['href']:
        page = list()
        for target in Targets:
            if tag in target.attrs:
                link = getNewUrlChecked(HomePage, target.attrs[tag])
                if link not in page:
                    page.append(link)
                    print(tag + " = " + link)
            # SeekForUrl(link)
        while len(page) > 1:
            SeekForUrl(page.pop())


# url_HomePage = 'https://img.moegirl.org.cn/common/thumb/4/43/%E5%A4%A7%E8%80%81%E5%B8%88_character.jpg/600px-%E5%A4%A7%E8%80%81%E5%B8%88_character.jpg'
url_HomePage = 'https://zh.moegirl.org.cn/%E9%9B%AA%E4%B9%8B%E4%B8%8B%E9%9B%AA%E4%B9%83'
html1 = urlopen(url_HomePage)
bs1 = BeautifulSoup(html1, 'lxml')
SeekForUrl(url_HomePage)
# getPictureUrl('a', 'href', re.compile('\.(jpg|png)'), bs1)

