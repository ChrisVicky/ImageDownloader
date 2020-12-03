from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import cv2
import requests
import numpy
import os



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
def getNewUrl(url):
    if 'https://' in url:
        return url
    else:
        return HomePage + url


def getSecondUrl(bs, tag, div1, rec):
    return bs.find_all(tag, {div1: rec})


def Exist(x):
    if x:
        return True
    return False

NumTxt=0
def writeUrlInTxt(url):
    global NumTxt
    NumTxt += 1
    fileName = LocalPath + 'text' + str(NumTxt) + '.txt'
    fp = open(fileName, 'wb')
    fp.write(url)
    fp.close()


def _getPicture(UrlList, tag, div, num, rec):
    NewNum = 1
    LinkList = []
    if num == -1:
        return
    for url in UrlList:
        bs = getBs(getHtml(url))
        for Link in getSecondUrl(bs, tag, div, rec):
            newUrl = getNewUrl(Link.attrs[div])
            if 'File' in newUrl or newUrl in LinkList :
                continue
            LinkList.append(newUrl)
            print(newUrl)
            pic = getContent(newUrl)
            bs2 = getBs(getHtml(newUrl))

            #savePicture(pic, NewNum)
            NewNum += 1


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
                print(newUrl)
    _getPicture(LIST, tag, div1, List_Number, rec)


url_HomePage = 'https://zh.moegirl.org.cn/%E9%9B%AA%E4%B9%8B%E4%B8%8B%E9%9B%AA%E4%B9%83'
html1 = urlopen(url_HomePage)
bs1 = BeautifulSoup(html1, 'lxml')
getPictureUrl('a', 'href', re.compile('\.(jpg|png)'), bs1)
# getPicture('meta', 'content', re.compile('\.(jpg|png)'), bs1, 'src')
# getPicture('a', 'href', re.compile('\.(jpg|png)'), bs1, 'src')
