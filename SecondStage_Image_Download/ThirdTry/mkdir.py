url = '链入页面'
print(url.encode())
url = 'https://zh.moegirl.org.cn/Special:链入页面/File:Yukino2.jpg'
print(type(url))
url = 'https://zh.moegirl.org.cn/Special:%E9%93%BE%E5%85%A5%E9%A1%B5%E9%9D%A2/File:Yukino2.jpg'
print(type(url))
url = 'https://img.moegirl.org.cn/common/thumb/3/33/%E9%9B%AA%E4%B9%8B%E4%B8%8B%E9%9B%AA%E4%B9%83%E7%94%9F%E6%97%A5%E8%B4%BA%E5%9B%BE3.jpg/600px-%E9%9B%AA%E4%B9%8B%E4%B8%8B%E9%9B%AA%E4%B9%83%E7%94%9F%E6%97%A5%E8%B4%BA%E5%9B%BE3.jpg'
if 'px' in url:
    print(url[url.rfind('/')+1:url.rfind('px')])
