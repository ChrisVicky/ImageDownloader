import cv2
import sys
import os.path
from PIL import Image


def detect(filename, cascade_file="lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image2 = Image.open(File_Name)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    cv2.imshow("Original.jpg", image)
    cv2.waitKey(0)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Gray.jpg", gray)
    cv2.waitKey(0)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(24, 24))
    i = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        image2.crop((x, y, x+w, y+h)).save('Face'+str(i)+'.png')
        i += 1

    cv2.imshow("AnimeFaceDetect", image)
    cv2.waitKey(0)
    cv2.imwrite("out_Rectangled.png", image)
    print("Def detect End")


# if len(sys.argv) != 2:
# if sys.argv[1] != 0:
#     print("Something went wrong")
#     sys.stderr.write("usage: detect.py <filename>\n")
#     sys.exit(-1)

print("请将您想要测试的图片拖入到该程序界面内")
print("如果不行\n请输入您想要测试的图片的绝对地址")
File_Name = input()
detect(File_Name)
