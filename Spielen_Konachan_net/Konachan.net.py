from DownloadPictures import DownloadPictures_
from DownloadPictures import DownloadPictures
from FileStuff import CheckForDirection
import os
konachan_net_post = 'https://konachan.net/post'
try:
    InternetStatus = os.system('ping www.baidu.com')
    if InternetStatus:
        Exception
    Status = input("[Welcome]\n")
    if not CheckForDirection():
        num = int(
            input("This is your first time to use this programme. How many pictures would you like to download?\n"))
        if type(num) == int:
            num = DownloadPictures(konachan_net_post, int(num))
    else:
        print("It's me again, happy to see you!")
        num = DownloadPictures_(konachan_net_post)
except Exception as e:
    exit(e)
finally:
    print("[We've Download (%d) Pictures]" % num)
    Status = input("Thanks for using!\n")
