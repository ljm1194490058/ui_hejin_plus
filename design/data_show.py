# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_show.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1349, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(20, 10, -1, 10)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton_openfile = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_openfile.setMinimumSize(QtCore.QSize(0, 3))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.toolButton_openfile.setFont(font)
        self.toolButton_openfile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_openfile.setStyleSheet("border-radius: 10px;\n"
"font: 11pt \"Agency FB\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 255);\n"
"padding: 5px;\n"
"background-repeat: no-repeat;")
        self.toolButton_openfile.setIconSize(QtCore.QSize(20, 16))
        self.toolButton_openfile.setObjectName("toolButton_openfile")
        self.gridLayout.addWidget(self.toolButton_openfile, 0, 0, 1, 1)
        self.textBrowser_open = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_open.sizePolicy().hasHeightForWidth())
        self.textBrowser_open.setSizePolicy(sizePolicy)
        self.textBrowser_open.setMinimumSize(QtCore.QSize(90, 30))
        self.textBrowser_open.setMaximumSize(QtCore.QSize(90, 30))
        self.textBrowser_open.setPlaceholderText("")
        self.textBrowser_open.setObjectName("textBrowser_open")
        self.gridLayout.addWidget(self.textBrowser_open, 0, 1, 1, 1)
        self.toolButton_xuanqu = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_xuanqu.setMinimumSize(QtCore.QSize(0, 3))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.toolButton_xuanqu.setFont(font)
        self.toolButton_xuanqu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_xuanqu.setStyleSheet("border-radius: 10px;\n"
"font: 11pt \"Agency FB\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 255);\n"
"padding: 5px;\n"
"background-repeat: no-repeat;")
        self.toolButton_xuanqu.setIconSize(QtCore.QSize(20, 16))
        self.toolButton_xuanqu.setObjectName("toolButton_xuanqu")
        self.gridLayout.addWidget(self.toolButton_xuanqu, 1, 0, 1, 1)
        self.spinBox_xuanqu = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_xuanqu.setMinimumSize(QtCore.QSize(91, 31))
        self.spinBox_xuanqu.setMaximum(5000)
        self.spinBox_xuanqu.setObjectName("spinBox_xuanqu")
        self.gridLayout.addWidget(self.spinBox_xuanqu, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(1255, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.groupBox_dataset = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_dataset.setObjectName("groupBox_dataset")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_dataset)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_dataset)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_dataset, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton_openfile.setText(_translate("MainWindow", "打开文件"))
        self.toolButton_xuanqu.setText(_translate("MainWindow", "选取该行"))
        self.groupBox_dataset.setTitle(_translate("MainWindow", "数据"))
