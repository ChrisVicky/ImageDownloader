from _Download_.FindPictureUrl import FindPictureUrl
from _Logistic_ import Welcome
from _Face_ import FaceProcessing
from _Logistic_.RandomDownload import RDownload
BasicUrl = 'https://konachan.net/post'


def main():
    num = None
    TotalNum = None
    FolderName = None
    Welcome.Preparation()
    RD = RDownload()
    if RD.IfExits():
        print("检测到您上次下载到了%d.jpg，若需要继续下载，请直接按下Enter键，否则请输入任何信息后再按下Enter键" % RD.BackUpNum)
        Input = input()
        if Input == "":
            print("好的，将按照时间顺序下载，直到图片%d.jpg。运行期间关闭程序即可停止下载。" % RD.BackUpNum)
            FolderName = '\\' + RD.Folder
            num = FindPictureUrl(url=RD.url, FolderName=FolderName, FinalName=RD.BackUpNum, RD=RD)
    if num is None:
        FeedBack = Welcome.FeedBack(RD)
        if FeedBack == Exception:
            raise Exception
        url = FeedBack['url']
        TotalNum = FeedBack['TotalNum']
        FolderName = FeedBack['FolderName']
        Status = FeedBack['Status']
        if Status == 4:
            num = FindPictureUrl(url=url, FolderName=FolderName, TotalNum=TotalNum, RD=RD)
        else:
            num = FindPictureUrl(url=url, FolderName=FolderName, TotalNum=TotalNum)
    print("[下载了%d张图片]" % num)
    if TotalNum is not None:
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
