from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import requests
import cv2
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


def savePicture(savePicturePicture, num):
    print(savePicturePicture)
    AllName = 'Picture'
    fileName = LocalPath + AllName + str(num) + '.png'
    print(fileName)
    fp = open(fileName, 'wb')
    fp.write(savePicturePicture)
    savePicturePicture = cv2.imread(fileName)
    cv2.imshow(url, savePicturePicture)
    cv2.waitKey(0)
    fp.close()



url = 'https://img.moegirl.org.cn/common/thumb/4/43/%E5%A4%A7%E8%80%81%E5%B8%88_character.jpg/600px-%E5%A4%A7%E8%80' \
     '%81%E5%B8%88_character.jpg '
# url = 'https://zh.moegirl.org.cn/File:%E5%A4%A7%E8%80%81%E5%B8%88_character.jpg'
picture = requests.get(url).content
savePicture(picture, 1)
# print(requests.get(url).content)
html = urlopen(url)
bs = BeautifulSoup(html, 'lxml')
# print(html)
# print(bs)



