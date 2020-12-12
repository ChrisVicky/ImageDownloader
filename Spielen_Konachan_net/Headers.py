import urllib.request
from bs4 import BeautifulSoup
import requests
#
url1 = 'https://konachan.net/post'
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 " \
             "Safari/537.36 "
headers = ("User-Agent", User_Agent)
opener = urllib.request.build_opener()  # 初始化创建自定义的opener
opener.addheaders = [headers]  # 设置对应的头信息，之后的open需要用opener对象的open方法
data = opener.open(url1).read()  # 使用opener对象下的open、read方法读取内容
bs = BeautifulSoup(data, 'lxml')
print(data)
# for url1 in bs.find_all('a'):
#     print(url1)
#     if 'href' in url1.attrs:
#         print("URLStart")
#         print(url1.attrs['href'])
#         print("URLEND")
#     print()



#
# url2 = "http://konachan.net/post"
# User_Agent2 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
# req = urllib.request.Request(url2)
# req.add_header('User-Agent', User_Agent2)
# html = urllib.request.urlopen(req)

