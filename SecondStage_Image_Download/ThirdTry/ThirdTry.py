from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import os


def isPictureUrl(URL, urlForCheck):
    url = str(URL.encode())
    if '\\x' in url:
        print("NotRight" + str(url) + "NotRight")
        return False
    if 'thumb' in url:
        return False
    if 'px' in URL and 'px' in urlForCheck:
        if URL[:URL.rfind('/')] == urlForCheck[:urlForCheck.rfind('/')]:
            return int(URL[URL.rfind('/')+1:URL.rfind('px')]) > int(urlForCheck[urlForCheck.rfind('/')+1:urlForCheck.rfind('px')])
    return True


def createFile(name):
    Path = os.getcwd() + '\\' + name
    if os.path.exists(Path):
        return
    os.mkdir(Path)


def getFilePath(name):
    return os.getcwd() + '\\' + name + '\\'


LocalPath = getFilePath('picture')
createFile('picture')


def getContent(url):
    return requests.get(url).content


def savePicture(savePicturePicture, num, PictureUrl):
    AllName = 'Picture'
    fileName = LocalPath + AllName + str(num) + '.png'
    print("Downloading " + PictureUrl)
    print(fileName)
    print("***************************** %Done")
    fp = open(fileName, 'wb')
    fp.write(savePicturePicture)
    fp.close()
    # savePicturePicture = cv2.imread(fileName)
    # cv2.imshow(url, savePicturePicture)
    # cv2.waitKey(0)


def getHtml(url):
    return urlopen(url)


def getBs(html):
    return BeautifulSoup(html, 'lxml')


HomePage = 'https://zh.moegirl.org.cn'


def getNewUrl(url):
    if 'https://' in url:
        return url
    else:
        return HomePage + url


def getPicture(UrlList, tag, div, num, rec):
    NewNum = 1
    LinkList = []
    url_Basic = HomePage
    if num == -1:
        return
    for url in UrlList:
        bs = getBs(getHtml(url))
        for Link in bs.find_all(tag, {div: rec}):
            newUrl = getNewUrl(Link.attrs[div])
            if 'File' in newUrl or newUrl in LinkList:
                continue
            if isPictureUrl(newUrl, url_Basic):
                LinkList.append(newUrl)
                pic = getContent(newUrl)
                savePicture(pic, NewNum, newUrl)
                NewNum += 1
                url_Basic = newUrl


def getPictureUrl(tag, div1, rec, bs):
    LIST = []
    List_Number = -1
    for Link in bs.find_all(tag, {div1: rec}):
        if div1 in Link.attrs:
            newUrl = getNewUrl(Link.attrs[div1])
            if newUrl in LIST:
                continue
            else:
                List_Number += 1
                LIST.append(newUrl)
    getPicture(LIST, tag, div1, List_Number, rec)


url_HomePage = 'https://zh.moegirl.org.cn/%E9%9B%AA%E4%B9%8B%E4%B8%8B%E9%9B%AA%E4%B9%83'
html1 = urlopen(url_HomePage)
bs1 = BeautifulSoup(html1, 'lxml')
getPictureUrl('a', 'href', re.compile('\.(jpg|png)'), bs1)
