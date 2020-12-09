import FindTag
import requests
import os

def Introduction():
    print("欢迎使用本程序    copyright: 刘锦帆 20级 工科班 天津大学")
    print("本程序满足二次元爱好者收集二次元图片的需求，顺便增加了将图片制成头像的功能")
    print("首先，通过简单的 Python 爬虫 从[k站]（著名二次元图片网站） [https://konachan.net/post] 抓取并下载二次元图片")
    print("然后，利用 open-CV [https://github.com/nagadomi/lbpcascade_animeface] 里的方法识别人物面部")
    print("最后，将上述识别到的人物面部保存为图片，可作为 头像 使用")


def GetRequirement():
    url = 'https://konachan.net/post'
    FolderName = 'konachan.net'
    print("请问您希望以何种形式进行图片的下载呢？（请输入1~3的阿拉伯数字）")
    print("    1.从k站的推荐中下载图片\n    2.输入动漫人物名称进行检索并下载\n    3.检索并下载动漫人物[雪之下雪乃]的图片")
    Status = int(input())
    if Status == 2:
        print("请问您想下载哪位动漫人物的图片呢？\n（支持中文、日文或英文输入）\n（例如：雪之下雪乃/雪之下/ゆきのした ゆきの/Yukinoshita Yukino）")
        Name = input()
        Tag = FindTag.FindPerson(Name)
        if Tag == Exception:
            return Exception
        url = 'https://konachan.net/post?tags=' + Tag
        FolderName = Tag
    elif Status == 3:
        Name = '雪之下雪乃'
        Tag = 'yukinoshita_yukino'
        url = 'https://konachan.net/post?tags=' + Tag
        FolderName = Tag
    FolderName = '\\' + FolderName
    response = requests.get(url)
    if response.status_code == 200:
        if Status == 1:
            print("将从网站[%s]下载图片" % url)
        else:
            print("将从网站[%s]下载[%s]的图片" % (url, Name))
    else:
        print("网络连接异常")
    print("请问您想下载最多多少张图片呢？\n（请输入一个阿拉伯数字）")
    TotalNum = int(input())
    print("好的，现在准备从[%s]下载[%d]张图片" % (url, TotalNum))
    return {'url': url, 'TotalNum': TotalNum, 'FolderName': FolderName}


def FeedBack():
    Introduction()
    Back_Get = GetRequirement()
    return Back_Get
