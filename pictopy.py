import base64
import os
from PyQt5 import QtCore, QtGui, QtWidgets

def pictopy(picture_names, py_name):
    """
    将图像文件转换为py文件
    """
    write_data = []
    for picture_name in picture_names:
        filename = picture_name.replace('.', '_')
        open_pic = open("%s" % picture_name, 'rb')
        b64str = base64.b64encode(open_pic.read())
        open_pic.close()
        # 注意这边b64str一定要加上.decode()
        write_data.append('%s = "%s"\n' % (filename, b64str.decode()))
    # print(write_data)
    #
    f = open('%s.py' % py_name, 'a+')
    for data in write_data:
        f.write(data)
    f.close()
    return write_data

if __name__ == '__main__':
    pics = os.listdir('ui_picture')  # 列出文件夹下所有的目录与文件
    pics = ['ui_picture/' + i for i in pics]
    l = pictopy(pics, 'memory_pic')
    l1 = base64.b64decode(l[0])
    print(l1)
    # l1 = str(l1, 'utf-8')
    # print(l1)
    # pics = ["ui_picture/logo1.png", "ui_picture/model1ok.png"]
    # print("ok")


# pyinstaller -F -w app_test.py -p choose_model.py -p filteroriginui.py -p filterui.py -p main_windows.py -p memory_pic.py -p pictopy.py -p picture_show.py -p single_predict.py -p ui.py -p choose_yuansu.py -p data_show.py -p login.py --hidden-import choose_model --hidden-import filteroriginui --hidden-import filterui --hidden-import main_windows --hidden-import memory_pic --hidden-import pictopy --hidden-import picture_show --hidden-import single_predict --hidden-import ui --hidden-import choose_yuansu --hidden-import data_show --hidden-import login