from urllib.request import urlopen
from bs4 import BeautifulSoup
import FileStuff
from Picture_Download_Und_Save import DownloadUndSavePictures_
from Picture_Download_Und_Save import DownloadUndSavePictures
import re
import time
base_page = 'https://konachan.net'
Num = 1


def getName(url):
    url = url[url.rfind('/'):]
    url = url[url.find('Spielen_Konachan_net.com%20')+19:]
    url = url[:url.find('%20')]
    return url


def DownloadPictures_(url):
    global Num
    time.sleep(0.01)
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    LinkList = bs.find_all('a', {'class': 'directlink largeimg', 'href': re.compile('(jpg|png)$')})
    for link in LinkList:
        link = link.attrs['href']
        if link:
            Name = getName(link)
            if FileStuff.CheckForUrl(Name):
                return Num - 1
            DownloadUndSavePictures_(link, Name, Num)
            Num += 1
        else:
            continue
        if Num == 2:
            FileStuff.LatestBackUp(Name, link)
    next_link = bs.find('a', {'class': 'next_page'})
    if next_link:
        next_link = base_page + next_link.attrs['href']
        return DownloadPictures_(next_link)
    else:
        return Num - 1


def DownloadPictures(url, num):
    global Num
    time.sleep(0.01)
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    LinkList = bs.find_all('a', {'class': 'directlink largeimg', 'href': re.compile('(jpg|png)$')})
    for link in LinkList:
        link = link.attrs['href']
        if link:
            Name = getName(link)
            DownloadUndSavePictures(link, Name, Num, num)
            Num += 1
        else:
            continue
        if Num == 2:
            FileStuff.LatestBackUp(Name, link)
        if Num > num:
            return Num - 1
    next_link = bs.find('a', {'class': 'next_page'})
    if next_link:
        next_link = base_page + next_link.attrs['href']
        return DownloadPictures(next_link, num)
    else:
        return Num - 1
