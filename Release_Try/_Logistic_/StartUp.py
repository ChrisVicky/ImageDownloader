import os


def StartUp():
    path = os.getcwd() + '\\_Logistic_' + '\\Started.txt'
    if os.path.exists(path):
        return
    print("In order to use the application with full function and avoid sudden break out,\n"
          " We plan to download some necessary Python Modules before the main programme started.")
    print("为了更好的运行所有的功能，需要提前下载一些python的模块库。")
    input("Press 'Enter' to start.\n点击“回车”开始。\n")
    os.system("pip install bs4")
    os.system("pip install requests")
    os.system("pip install PIL")
    os.system("pip install urllib")
    os.system("pip install opencv-python")
    os.system("pip install pillow")
    with open(path, 'w') as file:
        file.write("StartUpOK")

