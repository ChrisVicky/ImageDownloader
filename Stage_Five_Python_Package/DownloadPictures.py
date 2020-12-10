from urllib.request import urlopen
from bs4 import BeautifulSoup
import Picture_Download_Und_Save
import re
from _Logistic_ import Restriction_Tags
base_page = 'https://konachan.net'
Num = 1


def getName(url):
    url = url[url.rfind('/'):]


def DownloadPictures(url, TotalNum, FolderName):
    global Num
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    LinkList = bs.find_all('a', {'class': 'directlink largeimg', 'href': re.compile('(jpg|png)$')})
    for link in LinkList:
        link = link.attrs['href']
        if link:
            if Restriction_Tags.Tag_legal(link):

                Picture_Download_Und_Save.DownloadPicture(link, 'Picture_'+str(Num), FolderName, Num, TotalNum)
            else:
                continue
            # Picture_Download_Und_Save.DownloadPicture(link, 'Picture_'+str(Num), FolderName, Num, TotalNum)
        Num += 1
        if Num > TotalNum:
            return
    next_link = bs.find('a', {'class': 'next_page'})
    next_link = base_page + next_link.attrs['href']
    DownloadPictures(next_link, TotalNum, FolderName)
