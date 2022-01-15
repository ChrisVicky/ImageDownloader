import time
import os
import requests


def SpaceCut(string):
    for i in range(1, 4):
        string = string[string.find('%20')+3:]
    return string


def BackUp(name, url, path):
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = path + '\Backup.txt'
    file = open(file_path, 'a')
    file.writelines('\n')
    print("[%s]\n[%s]" % (name, url), end='\n', file=file)


def DownloadIt(url, name, subFile, Num, TotalNum=None, FinalNum=None):
    try:
        path = os.path.join(os.getcwd(), 'Results')
        path = os.path.join(path, subFile)
        if not os.path.exists(path):
            os.makedirs(path)
        picture = requests.get(url)
        chunk_size = 1024
        size = 0
        start = time.time()
        picture_size = int(picture.headers['content-length'])
        File_Name = os.path.join(path, name+'.jpg')
        if TotalNum is not None:
            print('[ %s ][第 %d 张 / 共 %d 张][大小 %.2fM ]' % (name, Num, TotalNum, float(float(picture_size)/1024/1024)))
        elif FinalNum is not None:
            print('[下载]%d.jpg / [目标]%d.jpg [大小 %.2fM ]' % (int(name), int(FinalNum), float(float(picture_size) / 1024 / 1024)))
        print('[本地地址]:%s' % File_Name)
        print('[下载源]:%s' % url)
        with open(File_Name, 'wb') as file:
            for data in picture.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)
                print('\r'+'[正在下载]:%s %d%%' % ('#'*int(50*size/picture_size), min(int(100*size/picture_size), 100)), end='')
                # time.sleep(0.001)
        end = time.time()
        print('\n[用时]:%.2fs\n' % (end-start))
        BackUp(str(name), str(url), str(path))
    except Exception as e:
        print("<<<<<<<<<<" + str(e) + ">>>>>>>>>>")
    return
