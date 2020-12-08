from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import os


File_Name = 'Default'
base_page = 'https://konachan.net'
base_page_18 = 'https://konachan.com'
Required_Number = 10
Count = 0


def savePicture(pic, path):
    fp = open(path, 'wb')
    fp.write(pic)
    fp.close()


def DownloadPicture(url):
    global Count
    Count += 1
    if Count > Required_Number:
        exit(0)
    picture = requests.get(url).content
    name_start = url.find('%20', url.find('Konachan.com%20-')+16)+3
    name_end = url.find('%20', url.find('Konachan.com%20-%20')+19)
    pic_name = url[name_start: name_end] + '.jpg'
    print("<Name> " + pic_name + " (" + str(Count)+"/"+str(Required_Number) + ")")
    print("<Source> " + url)
    global File_Name
    if File_Name == 'Default':
        File_Name = os.getcwd() + '\\' + 'Konachan.net\\'
    if not os.path.exists(File_Name):
        os.makedirs(File_Name)
    data_path = File_Name + pic_name
    savePicture(picture, data_path)
    print("<Path> " + data_path + "\n")


def BasicDfs(url, page):
    global File_Name
    File_Name = os.getcwd() + '\\' + 'Konachan.net\\'
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    LinkList = bs.find_all('a', {'class': 'directlink largeimg', 'href': re.compile('(jpg|png)$')})
    for link in LinkList:
        link = link.attrs['href']
        if link:
            DownloadPicture(link)
    next_link = bs.find('a', {'class': 'next_page'})
    next_link = base_page + next_link.attrs['href']
    BasicDfs(next_link, page+1)


def Welcome():
    global base_page
    global base_page_18
    global Required_Number
    if int(input("Pass_code\n")) == 1:
        base_page = base_page_18
    Required_Number = int(input("How many pictures do you want me to download?\n"))


def main():
    Welcome()
    BasicDfs(base_page+'/post', 1)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("***************************************")
        print("<<<<<<<  " + "ERROR:" + "    >>>>>>>")
        print("<<<<<<<  " + str(e) + "  >>>>>>>")
        print("***************************************")
    finally:
        print("\nThanks for Using this Programme.\nHave a nice day!")
