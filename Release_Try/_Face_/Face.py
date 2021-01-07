import cv2
import os.path
from PIL import Image


def ScaleFace(img, H):
    w = float(img.size[0])
    h = float(img.size[1])
    H = float(H)
    percent = H/h
    W = int(w * percent)
    H = int(H)
    img = img.resize((W, H), Image.ANTIALIAS)
    return img


def FaceProcess(number, TotalNumber, PictureName, ImageFile, cascade_file="_Face_\DetectFace.xml"):
    FileSaveName = os.getcwd() + '\Results' + '\Face'
    print("[处理 %s 中][第 %d 张 / 共 %d 张]" % (PictureName, number, TotalNumber))
    if not os.path.exists(FileSaveName):
        os.makedirs(FileSaveName)
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)
    cascade = cv2.CascadeClassifier(cascade_file)
    image_original = Image.open(ImageFile)
    image = cv2.imread(ImageFile, cv2.IMREAD_COLOR)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.equalizeHist(gray_image)
    faces = cascade.detectMultiScale(gray_image, scaleFactor=1.1,
                                     minNeighbors=3, minSize=(100, 100),)
    i = 1
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        Face_Path = FileSaveName + '\\' + PictureName[:PictureName.rfind('.jpg')] + '_Face_'+str(i)+'.jpg'
        Face = image_original.crop((x, y, x+w, y+h))
        Face = ScaleFace(Face, 600)
        Face.save(Face_Path)
        i += 1
    print("[%s处理完成，检测到到%d张脸]\n" % (PictureName, len(faces)))


def Processing(subFile, Num):
    Path = os.getcwd() + '\Results' + subFile
    Picture_List = os.listdir(Path)
    i = 0
    for picture_name in Picture_List:
        if 'jpg' not in picture_name:
            continue
        path = Path + '\\' + picture_name
        i += 1
        if i > Num:
            return
        try:
            FaceProcess(i, Num, picture_name, path)
        except Exception as e:
            exit(e)
