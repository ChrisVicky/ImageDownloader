from urllib.request import urlopen
from bs4 import BeautifulSoup
import Picture_Download_Und_Save
import re
from _Logistic_ import Restriction_Tags
base_page = 'https://konachan.net'
Num = 1


def getName(url):
    url = url[url.rfind('/'):]
    url = url[url.find('Konachan.com%20')+19:]
    url = url[:url.find('%20')]
    return url


def DownloadPictures(url, TotalNum, FolderName):
    global Num
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    LinkList = bs.find_all('a', {'class': 'directlink largeimg', 'href': re.compile('(jpg|png)$')})
    for link in LinkList:
        link = link.attrs['href']
        if link:
            Name = getName(link)
            if Restriction_Tags.Tag_legal(link):
                Picture_Download_Und_Save.DownloadPicture(link, Name, FolderName, Num, TotalNum)
            else:
                # Picture_Download_Und_Save.DownloadPicture(link, Name, '\Save'+FolderName[FolderName.find('\\')+1:], Num, TotalNum)
                continue
            # Picture_Download_Und_Save.DownloadPicture(link, 'Picture_'+str(Num), FolderName, Num, TotalNum)
        Num += 1
        if Num > TotalNum:
            return Num - 1
    next_link = bs.find('a', {'class': 'next_page'})
    if next_link:
        next_link = base_page + next_link.attrs['href']
        return DownloadPictures(next_link, TotalNum, FolderName)
    else:
        return Num - 1

