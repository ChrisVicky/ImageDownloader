from urllib.request import urlopen
from bs4 import BeautifulSoup
from _Download_.DownloadPictures import DownloadIt
import re
from _Tags_.Tags import Tag_legal
base_page = 'https://konachan.net'
Num = 1


def getName(url):
    url = url[url.rfind('/'):]
    url = url[url.find('Konachan.com%20')+19:]
    url = url[:url.find('%20')]
    return url


def Download(url, FolderName, TotalNum=None, FinalName=None, RD=None):
    global Num
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    LinkList = bs.find_all('a', {'class': 'directlink largeimg', 'href': re.compile('(jpg|png)$')})
    for link in LinkList:
        link = link.attrs['href']
        if link:
            Name = getName(link)
            if FinalName is None:
                if Num > TotalNum:
                    return Num - 1
            if Tag_legal(link):
                if RD is not None:
                    RD.WriteBackUp(Name)
                    RD = None
                if FinalName is not None:
                    if int(Name) <= int(FinalName):
                        return Num - 1
                if TotalNum is not None:
                    print("[查找图片中]")
                    DownloadIt(url=link, name=Name, subFile=FolderName, Num=Num, TotalNum=TotalNum)
                else:
                    print("[查找图片中]")
                    DownloadIt(url=link, name=Name, subFile=FolderName, Num=Num, FinalNum=FinalName)
            else:
                print("[被限制图片的地址]:%s\n" % link)
                continue
        Num += 1
    next_link = bs.find('a', {'class': 'next_page'})
    if next_link:
        next_link = base_page + next_link.attrs['href']
        return Download(url=next_link, TotalNum=TotalNum, FolderName=FolderName, FinalName=FinalName, RD=RD)
    else:
        return Num - 1
