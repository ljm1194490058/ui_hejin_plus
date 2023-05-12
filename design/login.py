# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import base64
import memory_pic as pic

def pytopic(pypic_code,pic_name):
    pic = pypic_code
    file = open(pic_name, 'wb')
    file.write(base64.b64decode(pic))
    file.close()
logo_background = pytopic(pic.logo1_png, 'logo1_png.png')
logo_head1 = pytopic(pic.head1_png, 'logo_head1.png')
logo_zuo2 = pytopic(pic.logo_zuo2_png, 'logo_zuo2.png')
logo_you1 = pytopic(pic.logo_you1_png, 'logo_you1.png')

class Ui_login_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 579)
        MainWindow.setMinimumSize(QtCore.QSize(996, 579))
        MainWindow.setMaximumSize(QtCore.QSize(996, 579))
        MainWindow.setStyleSheet("background-color: rgb(171, 192, 228);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: transparent;\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.label_background = QtWidgets.QLabel(self.centralwidget)
        self.label_background.setGeometry(QtCore.QRect(0, -30, 1001, 571))
        self.label_background.setMinimumSize(QtCore.QSize(951, 491))
        self.label_background.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.label_background.setBaseSize(QtCore.QSize(8, 0))
        self.label_background.setStyleSheet("background-color: transparent;\n"
"background-image: url(background1.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.label_background.setText("")
        self.label_background.setPixmap(QtGui.QPixmap("logo1_png.png"))
        self.label_background.setObjectName("label_background")
        self.label_head = QtWidgets.QLabel(self.centralwidget)
        self.label_head.setGeometry(QtCore.QRect(180, 180, 371, 281))
        self.label_head.setText("")
        self.label_head.setPixmap(QtGui.QPixmap("logo_head1.png"))
        self.label_head.setObjectName("label_head")
        self.label_logo1 = QtWidgets.QLabel(self.centralwidget)
        self.label_logo1.setGeometry(QtCore.QRect(20, 390, 151, 131))
        self.label_logo1.setText("")
        self.label_logo1.setPixmap(QtGui.QPixmap("logo_zuo2.png"))
        self.label_logo1.setObjectName("label_logo1")
        self.label_logo2 = QtWidgets.QLabel(self.centralwidget)
        self.label_logo2.setGeometry(QtCore.QRect(830, 460, 161, 71))
        self.label_logo2.setText("")
        self.label_logo2.setPixmap(QtGui.QPixmap("logo_you1.png"))
        self.label_logo2.setObjectName("label_logo2")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(30, 30, 941, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(87)
        font.setKerning(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: white;\n"
"font: 700 18pt \"微软雅黑\";")
        self.label_title.setObjectName("label_title")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(610, 200, 111, 51))
        self.label_login.setStyleSheet("font: 25 16pt \"微软雅黑\";")
        self.label_login.setObjectName("label_login")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(640, 270, 81, 51))
        self.label_password.setStyleSheet("font: 25 16pt \"微软雅黑\";")
        self.label_password.setObjectName("label_password")
        self.lineEdit__login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit__login.setGeometry(QtCore.QRect(730, 210, 231, 41))
        self.lineEdit__login.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit__login.setObjectName("lineEdit__login")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(730, 280, 231, 41))
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(660, 350, 231, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login.setStyleSheet("border-radius: 10px;\n"
"font: 16pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 164, 240);\n"
"padding: 5px;\n"
"background-repeat: no-repeat;")
        self.login.setObjectName("login")
        self.label_banben = QtWidgets.QLabel(self.centralwidget)
        self.label_banben.setGeometry(QtCore.QRect(350, 480, 251, 51))
        self.label_banben.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_banben.setObjectName("label_banben")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "                    镍基单晶高温合金成分智能优化设计系统\n"
"     Intelligent Optimization Composition-design System for \n"
"                    Nickel-based Single Crystal Superalloy"))
        self.label_login.setText(_translate("MainWindow", "用 户 名:"))
        self.label_password.setText(_translate("MainWindow", "密 码："))
        self.login.setText(_translate("MainWindow", " 登 录"))
        self.label_banben.setText(_translate("MainWindow", "               版本号：V1.0\n"
"版权所有：中国科学院金属研究所"))