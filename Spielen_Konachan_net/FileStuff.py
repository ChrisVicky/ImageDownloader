import os
import datetime
path = os.getcwd()
print(datetime.date.today())
FolderName = os.getcwd() + '\_SOURCE_'
BackUpPath = FolderName + '\\' + str(datetime.date.today())
BackUp_ = FolderName + '\\' + str(datetime.date.today()) + '\\BackUp.txt'
LastBackUpPath = FolderName
LastBackUp = FolderName + '\\LastBackUp.txt'
NAME = None
URL = None


def getFolderName():
    return FolderName + '\\' + str(datetime.date.today())


def CheckForDirection():
    global NAME
    global URL
    if os.path.exists(FolderName):
        FILE = open(LastBackUp, 'r')
        FILE = FILE.readlines()
        NAME = FILE[0]
        NAME = NAME[:NAME.rfind('\n')]
        print("[LAST TIME NAME]:" + NAME)
        URL = FILE[1]
        URL = URL[:URL.rfind('\n')]
        print("[LAST TIME URL]:" + URL)
        return True
    os.makedirs(LastBackUpPath)
    file = open(LastBackUp, 'a')
    os.makedirs(BackUpPath)
    file = open(BackUp_, 'a')
    return False


def BackUp(name, url):
    file = open(BackUp_, 'a')
    file.writelines('\n')
    print("[%s]\n[%s]" % (name, url), '\n', file=file)


def LatestBackUp(name, url):
    file = open(LastBackUp, 'w')
    print("%s\n%s" % (name, url), file=file)


def CheckForUrl(name):
    print("[NAME]:%s" % NAME)
    print("[name]:%s" % name)
    if str(name) == str(NAME):
        return True
    return False
