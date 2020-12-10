import cv2
import os.path
from PIL import Image
import time

def FaceProcess(number, TotalNumber, PictureName, filename, cascade_file="_Face_\DetectFace.xml"):
    FileSaveName = os.getcwd() + '\Results' + '\Face'
    print("[处理 %s 中][第 %d 张 / 共 %d 张]" %(PictureName, number, TotalNumber))
    if not os.path.exists(FileSaveName):
        os.makedirs(FileSaveName)
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)
    cascade = cv2.CascadeClassifier(cascade_file)
    image_original = Image.open(filename)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(100, 100),
                                     # minSize = (24, 24)
                                     )
    i = 1
    NUM = 100
    for k in range(1,NUM+1):
        print('\r' + '[正在处理 %s 中]:%s %d%%' % (PictureName, '#' * int(50 * k / NUM), int(100 * float(k) / float(NUM))),
              end='')
        time.sleep(0.001)
    print()
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        Face_Path = FileSaveName + '\\' + PictureName[:PictureName.rfind('.jpg')] + '_Face_'+str(i)+'.jpg'
        image_original.crop((x, y, x+w, y+h)).save(Face_Path)
        i += 1
    return "[%s处理完成，检测到到%d张脸]\n" % (PictureName, i-1)


def Processing(subFile, Num):
    Path = os.getcwd() + '\Results' + subFile
    Picture_List = os.listdir(Path)
    i = 0
    for pictre_name in Picture_List:
        if 'jpg' not in pictre_name:
            continue
        path = Path + '\\' + pictre_name
        i += 1
        if i > Num:
            return
        try:
            print(FaceProcess(i, Num, pictre_name, path))
        except Exception as e:
            exit(e)
