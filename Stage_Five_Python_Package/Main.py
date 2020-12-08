import DownloadPictures
import Welcome
BasicUrl = 'https://konachan.net/post'


def main():
    FeedBack = Welcome.FeedBack()
    url = FeedBack['url']
    TotalNum = FeedBack['TotalNum']
    FolderName = FeedBack['FolderName']
    DownloadPictures.DownloadPictures(url, TotalNum, FolderName)


if __name__ == '__main__':
    main()
