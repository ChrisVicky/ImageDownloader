from _Download_ import FindPictureUrl
from _Logistic_ import Welcome
from _Face_ import FaceProcessing
BasicUrl = 'https://konachan.net/post'


def main():
    FeedBack = Welcome.FeedBack()
    if FeedBack == Exception:
        raise Exception
    url = FeedBack['url']
    TotalNum = FeedBack['TotalNum']
    FolderName = FeedBack['FolderName']
    num = FindPictureUrl.FindPictureUrl(url, TotalNum, FolderName)
    print("[下载了%d张图片]" % num)
    if num < TotalNum:
        print("总数好像不够多呢，可能是因为您所找的角色在网站上的图片不够多、或者是那些图片都不适合青少年")
    print("请问您希望处理多少张照片呢？")
    Num = Welcome.inputInteger("（请输入0~%d的阿拉伯数字）\n" % num)
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
