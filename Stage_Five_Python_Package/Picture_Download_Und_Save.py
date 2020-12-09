import time
import os
import requests
import numpy


def SpaceCut(string):
    for i in range(1, 4):
        string = string[string.find('%20')+3:]
    return string


def BackUp(name, url, path):
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = path + '\Backup.txt'
    file = open(file_path, 'a')
    Write = name + '\n' + url + '\n'
    file.writelines('\n')
    print("[%s]\n[%s]" % (name, url), end='\n', file=file)
    # numpy.savetxt(path, Write)


def DownloadPicture(url, name, subFile, Num, TotalNum):
    try:
        path = os.getcwd() + '\Results' + subFile
        if not os.path.exists(path):
            os.makedirs(path)
        picture = requests.get(url)
        chunk_size = 1024
        size = 0
        start = time.time()
        picture_size = int(picture.headers['content-length'])
        File_Name = path + '\\' + name + '.jpg'
        print('[ %s ][第 %d 张 / 共 %d 张][大小 %.2fM ]' % (name, Num, TotalNum, float(float(picture_size)/1024/1024)))
        print('[本地地址]:%s' % File_Name)
        print('[下载源]:%s' % url)
        with open(File_Name, 'wb') as file:
            for data in picture.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)
                print('\r'+'[正在下载]:%s %d%%' % ('#'*int(50*size/picture_size), min(int(100*size/picture_size), 100)), end='')
                time.sleep(0.001)
        end = time.time()
        print('\n[用时]:%.2fs\n' % (end-start))
    except Exception as e:
        print("<<<<<<<<<<" + str(e) + ">>>>>>>>>>")
    BackUp(str(name), str(url), str(path))
    return

#
# DownloadPicture(
#     'https://konachan.net/image/b28c76f1c19606871f55bcff9050f4e5/Konachan.com%20-%20221153%20animal%20bird%20blue_eyes%20dress%20ein_eis%20hat%20long_hair%20yahari_ore_no_seishun_love_come_wa_machigatteiru.%20yukinoshita_yukino.jpg',
#     'Yukinoshita','\Yukino',1,2
# )
# DownloadPicture(
#     'https://konachan.net/image/b28c76f1c19606871f55bcff9050f4e5/Konachan.com%20-%20221153%20animal%20bird%20blue_eyes%20dress%20ein_eis%20hat%20long_hair%20yahari_ore_no_seishun_love_come_wa_machigatteiru.%20yukinoshita_yukino.jpg',
#     'Yukinoshita2','\Yukino',2,2
# )