from _Download_.FindKeyWords import findPerson
import requests
import re
import time
import os


def inputInteger(Message):
    Num = input(Message)
    while Num == "":
        Num = input(Message)
    return int(Num)


def Introduction():
    print("欢迎使用本程序")
    print("[copyright]天津大学 20级 工科班 刘锦帆")
    print("[爬虫网站]https://konachan.net")
    print("[动漫人脸识别open-CV]https://github.com/nagadomi/lbpcascade_animeface")


def GetRequirement(RD):
    Name = None
    print("请问您希望以何种形式进行图片的下载呢？")
    print("    1.从k站的推荐中下载图片")
    print("    2.输入动漫人物名称进行检索并下载")
    print("    3.检索并下载动漫人物[雪之下雪乃]的图片")
    print("    4.从k站的推荐中下载图片，并可以在下次使用本程序时更新您的图片库")
    Status = inputInteger('（请输入1~4的阿拉伯数字）\n')
    if Status == 1:
        url = 'https://konachan.net/post'
        FolderName = 'konachan.net'
    elif Status == 2:
        print("请问您想下载哪位动漫人物的图片呢？\n（支持中文、日文或英文输入）\n（例如：雪之下雪乃/雪之下/ゆきのした ゆきの/Yukinoshita Yukino）")
        Name = input()
        Tag = findPerson(Name)
        if Tag == Exception:
            return Exception
        if re.match('[a~z]*', Tag) is None:
            print("[未检索到您要的人物，接下来将为您从k站的推荐中下载图片]")
            url = 'https://konachan.net/post'
            FolderName = 'konachan.net'
            Status = 1
        else:
            url = 'https://konachan.net/post?tags=' + Tag
            FolderName = Tag
    elif Status == 3:
        Name = '雪之下雪乃'
        Tag = 'yukinoshita_yukino'
        url = 'https://konachan.net/post?tags=' + Tag
        FolderName = Tag
    elif Status == 4:
        url = 'https://konachan.net/post'
        FolderName = RD.Folder
    else:
        return ValueError
    response = requests.get(url)
    if response.status_code == 200:
        if Status == 1 or Status == 4:
            print("将从网站[%s]下载图片" % url)
        elif Status == 2 or Status == 3:
            print("将从网站[%s]下载[%s]的图片" % (url, Name))
    else:
        print("网络连接异常")
        return ConnectionError
    print("请问您想下载最多多少张图片呢？")
    TotalNum = inputInteger('（请输入一个阿拉伯数字）\n')
    print("好的，现在准备从[%s]下载[%d]张图片" % (url, TotalNum))
    return {'url': url, 'TotalNum': TotalNum, 'FolderName': FolderName, 'Status': Status}


def InternetConnectionCheck():
    print("\n[检查网络连接中......]")
    try:
        InternetStatus = os.system('ping www.baidu.com')
        if InternetStatus:
            print('\n[您的网络连接好像不太正常，请检查网络设置]\n')
            exit(ConnectionError)
        print('\n[您的网络连接正常]\n')
    except Exception as e:
        exit(e)


def FeedBack(RD):
    Back_Get = GetRequirement(RD)
    return Back_Get


def Preparation():
    Introduction()
    #InternetConnectionCheck()
