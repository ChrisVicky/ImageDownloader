import os


def StartUp():
    path = os.getcwd() + '\\_Logistic_' + '\\Started.txt'
    if os.path.exists(path):
        return
    print("In order to use the application with full function and avoid sudden break out,\n"
          " We plan to download some necessary Python Modules before the main programme started.")
    print("为了更好的运行所有的功能，需要提前下载一些python的模块库。")
    input("Press 'Enter' to start.\n点击“回车”开始。\n")
    try:
        print("pip install bs4")
        os.system("pip install bs4")  # bs4
        print("pip install requests")
        os.system("pip install requests")  # requests
        print("pip install PIL")
        os.system("pip install PIL")  # PIL
        print("pip install urllib")
        os.system("pip install urllib")  # urllib
        print("pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple/")
        os.system("pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple/")  # opencv-python
        print("pip install pillow")
        os.system("pip install pillow")  # pillow
        print("pip install time")
        os.system("pip install time")  # time
        print("pip install re")
        os.system("pip install re")  # re
        print("pip install lxml")
        os.system("pip install lxml")  # lxml - for bs
        with open(path, 'w') as file:
            file.write("StartUpOK")
    except Exception as e:
        raise e
