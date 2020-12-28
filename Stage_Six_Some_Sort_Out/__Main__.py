from _Download_ import FindPictureUrl
from _Logistic_ import Welcome
from _Face_ import FaceProcessing
BasicUrl = 'https://konachan.net/post'


def main():
    # Nobody here but us chickens!
    FeedBack = Welcome.FeedBack()
    if FeedBack == Exception:
        raise Exception
    url = FeedBack['url']
    TotalNum = FeedBack['TotalNum']
    FolderName = FeedBack['FolderName']
    num = FindPictureUrl.FindPictureUrl(url, TotalNum, FolderName)
    print("[下载了%d张图片]" % num)
    Num = int(input("请问您希望处理多少张照片呢？\n"))
    FaceProcessing.Processing(FolderName, Num)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        exit(e)
    finally:
        print("所有的图片都保存在了该目录下的相应文件夹中。请注意查收")
        print("感谢您使用本程序\nHave a nice day!\nTschüs!")
        input()
