import difflib
import re

def CheckUrl(url):
    if url[url.find('jpg'):] == 'jpg':
        return True
    return False
url1 = 'https://zh.moegirl.org.cn/File:Winner-sapphire-2015.jpg'
url2 = 'https://zh.moegirl.org.cn/File:Winner-sapphire-2016.jpg'
d = difflib.Differ()
# print(d.compare(url2, url1))
# print(list(d.compare(url1, url2)))
print(url1[url1.find('File'):])
if CheckUrl(url1):
    print("OK")
