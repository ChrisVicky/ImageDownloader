import os
import datetime


class CDownload:
    def __init__(self):
        self.BackupFile = os.path.join(os.path.join(os.getcwd(), "_CasualDownload_"), "BackupR.txt")
        self.url = 'https://konachan.net/post'
        self.Folder = str(datetime.date.today())
        self.BackUpNum = None

    def setBackupFile(self):
        if not os.path.exists(self.BackupFile):
            os.makedirs(self.BackupFile)

    def IfExits(self):
        if os.path.exists(self.BackupFile):
            self.BackUpNum = self.getBackUpNum()
            return True
        else:
            return False

    def getBackUpNum(self):
        with open(self.BackupFile, 'r') as file:
            num = file.readline()
        return int(num)

    def WriteBackUp(self, num):
        with open(self.BackupFile, 'w') as file:
            print(num, file=file)
