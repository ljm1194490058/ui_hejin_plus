# qt
from PyQt5.QtGui import QPixmap, QGuiApplication
from PyQt5.QtWidgets import QMainWindow,QLabel, QLineEdit,QMessageBox, QCheckBox, QFileDialog, qApp, QTableWidgetItem, QApplication
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, Qt

# design_UI
from login import Ui_login_MainWindow
from main_windows import Ui_MainWindow
from youhua import Ui_youhua_MainWindow
from data_show import Ui_xuanqu_MainWindow

# other packages
import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import tensorflow as tf
from sko.GA import GA

# 让界面在不同显示器上显示大小相同
QGuiApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

# 保存文件信息
cur_select_file = [""]

# 推荐结果
result_yuansu = ""

# 选取的元素各个数值  先设置初始值都是0   防止优化界面接收错误list
list_yuan = [0] * 13

# 登录界面
class login_Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_login_MainWindow()
        self.ui.setupUi(self)
        # 设置一下最上方的标题
        self.setWindowTitle("登录界面")

        # self.ui.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_password.setEchoMode(QLineEdit.Password)

        # self.main_window = Main_Window(self)

    @pyqtSlot()
    def on_login_clicked(self):
        if self.ui.lineEdit__login.text() == "jdliu" and self.ui.lineEdit_password.text() == "601jdliu":
            # 登录成功，隐藏登录界面，显示主页面
            self.hide()
            main_window.show()
        else:
            # 登录失败，弹出错误提示
            msgBox = QMessageBox()
            msgBox.setStyleSheet("background-color: white; color:white")
            QMessageBox.warning(self, "提示", "用户名或密码错误！",
                                QMessageBox.Yes)
            self.ui.lineEdit__login.clear()
            self.ui.lineEdit_password.clear()

# 选取元素界面
class data_show(QMainWindow):
    # 向主窗口传选取的元素列表
    signal_1 = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_xuanqu_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("样本选择界面")
        self.ui.toolButton_xuanqu.clicked.connect(self.on_toolButton_xuanqu_clicked)

    # 打开文件
    @pyqtSlot()
    def on_toolButton_openfile_clicked(self):
        fname = QFileDialog.getOpenFileName(self, "打开文件", './', '(*.csv)')
        if fname[0]:
            # TODO 用于传给子窗体，使用遍历保存
            cur_select_file[0] = fname[0]
            print("cur_select_file[0]：",cur_select_file[0])

            self.ui.textBrowser_open.setText(fname[0].split('/')[-1])
            # 显示数据
            self.display_dataset(fname[0])
            # self.signal_filename.emit(fname[0].split('/')[-1])

    # 显示数据集
    def display_dataset(self, filename):

            table = pd.read_csv(filename, encoding='gbk')

            rows = table.shape[0]
            columns = table.shape[1]
            headers = table.columns.values.tolist()

            # 保存表头，给显示单行数据表格使用
            self.headers = headers

            # 设置行、列、表头
            self.ui.tableWidget.setColumnCount(columns)
            self.ui.tableWidget.setRowCount(rows)
            self.ui.tableWidget.setHorizontalHeaderLabels(headers)

            # 遍历每个元素填充TableWidget
            for i in range(rows):
                rows_values = table.iloc[[i]]
                rows_list = np.array(rows_values).tolist()[0]
                for j in range(columns):
                    items_list = rows_list[j]

                    table_items = str(items_list)
                    newItem = QTableWidgetItem(table_items)
                    newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.ui.tableWidget.setItem(i, j, newItem)
                    self.ui.tableWidget.item(i, j).text()

    # 选取指定行的数据
    @pyqtSlot()
    def on_toolButton_xuanqu_clicked(self):
        hangshu = self.ui.spinBox_xuanqu.value()
        hangshu = int(hangshu)
        if cur_select_file[0]:
            data = pd.read_csv(cur_select_file[0], encoding='gbk')
            hang_val = data.iloc[hangshu - 1, :]
            hang_val_list = hang_val.tolist()
            self.signal_1.emit(hang_val_list)
            message = "选取数据成功！"
        else:
            message = "未选择文件！"
        QMessageBox.warning(self, "提示！", message, QMessageBox.Yes)
        self.close()
        # print("hang_)val", hang_val)


# 优化界面
class youhua_Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_youhua_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("多目标优化功能界面")

        # 连接鼠标点击事件处理函数
        self.mousePressEvent = self.on_mouse_pressed_youhua

    def on_mouse_pressed_youhua(self, event):
        self.activateWindow()
        self.raise_()
        # 将主页面选取的元素直接放到优化界面的对应位置上

    def getData1(self, list):  # 获取传过来的值
        self.ui.doubleSpinBox_1.setValue(float('{}'.format(list[0])))
        self.ui.doubleSpinBox_2.setValue(float('{}'.format(list[1])))
        self.ui.doubleSpinBox_3.setValue(float('{}'.format(list[2])))
        self.ui.doubleSpinBox_4.setValue(float('{}'.format(list[3])))
        self.ui.doubleSpinBox_5.setValue(float('{}'.format(list[4])))
        self.ui.doubleSpinBox_6.setValue(float('{}'.format(list[5])))
        self.ui.doubleSpinBox_7.setValue(float('{}'.format(list[6])))
        self.ui.doubleSpinBox_8.setValue(float('{}'.format(list[7])))
        self.ui.doubleSpinBox_9.setValue(float('{}'.format(list[8])))
        self.ui.doubleSpinBox_10.setValue(float('{}'.format(list[9])))
        self.ui.doubleSpinBox_11.setValue(float('{}'.format(list[10])))
        self.ui.doubleSpinBox_12.setValue(float('{}'.format(list[11])))
        self.ui.doubleSpinBox_13.setValue(float('{}'.format(list[12])))

    @pyqtSlot()
    def on_pushButton_shezhi_9_clicked(self):
        QMessageBox.warning(self, "提示！", "该功能暂未开通！", QMessageBox.Yes)


    # 点击优化后出现的效果
    @pyqtSlot()
    def on_pushButton_shezhi_8_clicked(self):
        l1 = self.ui.doubleSpinBox_1.value()
        l2 = self.ui.doubleSpinBox_2.value()
        l3 = self.ui.doubleSpinBox_3.value()
        l4 = self.ui.doubleSpinBox_4.value()
        l5 = self.ui.doubleSpinBox_5.value()
        l6 = self.ui.doubleSpinBox_6.value()
        l7 = self.ui.doubleSpinBox_7.value()
        l8 = self.ui.doubleSpinBox_8.value()
        r1 = self.ui.doubleSpinBox_9.value()
        r2 = self.ui.doubleSpinBox_10.value()
        r3 = self.ui.doubleSpinBox_11.value()
        r4 = self.ui.doubleSpinBox_12.value()
        r5 = self.ui.doubleSpinBox_13.value()
        list_1 =  [l1, l2, l3, l4, l5, l6, l7, l8, r1, r2, r3, r4, r5]
        listyuan_1 = list_yuan[:-2]
        #比较一下两个列表是否相同，如果相同说明用的还是原先训练模型的值， 如果不同也就是else说明又重新选择了值但没有训练新的数据
        if list_1 == listyuan_1:
            self.ui.textBrowser_3.setText(result_yuansu)
        else:
            QMessageBox.warning(self, "提示！", "选择的数据还未进行新一轮训练！", QMessageBox.Yes)

    @pyqtSlot()
    def on_pushButton_shezhi_5_clicked(self):
        l1 = self.ui.doubleSpinBox_1.value()
        l2 = self.ui.doubleSpinBox_2.value()
        l3 = self.ui.doubleSpinBox_3.value()
        l4 = self.ui.doubleSpinBox_4.value()
        l5 = self.ui.doubleSpinBox_5.value()
        l6 = self.ui.doubleSpinBox_6.value()
        l7 = self.ui.doubleSpinBox_7.value()
        l8 = self.ui.doubleSpinBox_8.value()
        r1 = self.ui.doubleSpinBox_9.value()
        r2 = self.ui.doubleSpinBox_10.value()
        r3 = self.ui.doubleSpinBox_11.value()
        r4 = self.ui.doubleSpinBox_12.value()
        r5 = self.ui.doubleSpinBox_13.value()
        list_1 =  [l1, l2, l3, l4, l5, l6, l7, l8, r1, r2, r3, r4, r5]
        listyuan_1 = list_yuan[:-2]
        #比较一下两个列表是否相同，如果相同说明用的还是原先训练模型的值， 如果不同也就是else说明又重新选择了值但没有训练新的数据
        if list_1 == listyuan_1:
            self.ui.textBrowser_3.setText(result_yuansu)
        else:
            QMessageBox.warning(self, "提示！", "选择的数据还未进行新一轮训练！", QMessageBox.Yes)

    @pyqtSlot()
    def on_pushButton_shezhi_4_clicked(self):
        l1 = self.ui.doubleSpinBox_1.value()
        l2 = self.ui.doubleSpinBox_2.value()
        l3 = self.ui.doubleSpinBox_3.value()
        l4 = self.ui.doubleSpinBox_4.value()
        l5 = self.ui.doubleSpinBox_5.value()
        l6 = self.ui.doubleSpinBox_6.value()
        l7 = self.ui.doubleSpinBox_7.value()
        l8 = self.ui.doubleSpinBox_8.value()
        r1 = self.ui.doubleSpinBox_9.value()
        r2 = self.ui.doubleSpinBox_10.value()
        r3 = self.ui.doubleSpinBox_11.value()
        r4 = self.ui.doubleSpinBox_12.value()
        r5 = self.ui.doubleSpinBox_13.value()
        list_1 =  [l1, l2, l3, l4, l5, l6, l7, l8, r1, r2, r3, r4, r5]
        listyuan_1 = list_yuan[:-2]
        #比较一下两个列表是否相同，如果相同说明用的还是原先训练模型的值， 如果不同也就是else说明又重新选择了值但没有训练新的数据
        if list_1 == listyuan_1:
            self.ui.textBrowser_3.setText(result_yuansu)
        else:
            QMessageBox.warning(self, "提示！", "选择的数据还未进行新一轮训练！", QMessageBox.Yes)


# 主界面
class Main_Window(QMainWindow):
    signal_yuansu = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)
        self.setWindowTitle("镍基单晶高温合金成分智能优化设计系统")

        #  其他界面展示
        self.data_show = data_show(self)
        self.data_show.signal_1.connect(self.get_xuanqu)
        self.youhua = youhua_Window(self)
        self.signal_yuansu.connect(self.youhua.getData1) #用信号连接子窗口的getData1函数


    @pyqtSlot()
    def on_pushButton_wenjian_clicked(self):
        self.data_show.show()


    # # 允许等比例缩放
    #     self.setFixedSize(self.width(), self.height())

    # 选取的元素值展示在主页面
    def get_xuanqu(self, list):
        global list_yuan
        # 想吧多余的0去掉但不行
        self.ui.doubleSpinBox_1.setValue(float('{}'.format(list[0])))
        self.ui.doubleSpinBox_2.setValue(float('{}'.format(list[1])))
        self.ui.doubleSpinBox_3.setValue(float('{}'.format(list[2])))
        self.ui.doubleSpinBox_4.setValue(float('{}'.format(list[3])))
        self.ui.doubleSpinBox_5.setValue(float('{}'.format(list[4])))
        self.ui.doubleSpinBox_6.setValue(float('{}'.format(list[5])))
        self.ui.doubleSpinBox_7.setValue(float('{}'.format(list[6])))
        self.ui.doubleSpinBox_8.setValue(float('{}'.format(list[7])))
        self.ui.doubleSpinBox_9.setValue(float('{}'.format(list[8])))
        self.ui.doubleSpinBox_10.setValue(float('{}'.format(list[9])))
        self.ui.doubleSpinBox_11.setValue(float('{}'.format(list[10])))
        self.ui.doubleSpinBox_12.setValue(float('{}'.format(list[11])))
        self.ui.doubleSpinBox_13.setValue(float('{}'.format(list[12])))
        self.ui.doubleSpinBox_14.setValue(float('{}'.format(list[13])))
        self.ui.doubleSpinBox_15.setValue(float('{}'.format(list[14])))
        list_yuan = list

    @pyqtSlot()
    # 点击预测之后的效果
    def on_pushButton_shezhi_4_clicked(self):
        global list_yuan, result_yuansu
        l1 = self.ui.doubleSpinBox_1.value()
        l2 = self.ui.doubleSpinBox_2.value()
        l3 = self.ui.doubleSpinBox_3.value()
        l4 = self.ui.doubleSpinBox_4.value()
        l5 = self.ui.doubleSpinBox_5.value()
        l6 = self.ui.doubleSpinBox_6.value()
        l7 = self.ui.doubleSpinBox_7.value()
        l8 = self.ui.doubleSpinBox_8.value()
        r1 = self.ui.doubleSpinBox_9.value()
        r2 = self.ui.doubleSpinBox_10.value()
        r3 = self.ui.doubleSpinBox_11.value()
        r4 = self.ui.doubleSpinBox_12.value()
        r5 = self.ui.doubleSpinBox_13.value()
        r6 = self.ui.doubleSpinBox_14.value()
        r7 = self.ui.doubleSpinBox_15.value()

        a = int(l1)
        b = int(r7)
        if a == 0 or b == 0:
            QMessageBox.warning(self, "提示", "选择数据出现错误！请重新选择！",
                                QMessageBox.Yes)


        else:
            list_min = [5.5, 4.5, 0.61, 1.35, 5.9, 0.0, 2.8, 0.0, 0.0, 0.0, 60.745, 0.0, 0.0, 800.0, 130.0]
            list_max = [7.2, 9.6, 5.0, 6.5, 7.0, 6.6, 6.8, 0.006, 0.06, 0.96, 70.7, 0.5, 1.02, 1100.0, 750.0]

            # modelname = "./weights_h5/model.h5"
            modelname = "D:\\ui_hejin_plus\\weight_h5\\model.h5"
            model = tf.keras.models.load_model(modelname, compile=False)  # 加载模型出错
            # predict1 = model.predict(data)
            # predict1 = np.array(predict1)
            # predict1 = predict1.reshape(1, -1)

            # 将界面上展示的个个元素含量封装在这个list下
            list_yuan = [l1, l2, l3, l4, l5, l6, l7, l8, r1, r2, r3, r4, r5, r6, r7]

            # 推荐
            # 寿命
            def func0(p):
                # 拿到样本值
                yangben = [l1, l2, l3, l4, l5, l6, l7, l8, r1, r2, r3, r4, r5, r6, r7]
                # 对样本进行简单处理  归一化操作
                yangben = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                           zip(yangben, list_min, list_max)]

                yangben = np.array(yangben)
                yangben = yangben.reshape(1, 15)
                x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = p
                list1 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15]

                yangben_chuli = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                                 zip(list1, list_min, list_max)]

                yangben_pre = np.array(yangben_chuli)
                yangben_pre = yangben_pre.reshape(1, -1)
                if yangben[:, 5] == 0:
                    yangben_pre[:, 5] = 0
                if yangben[:, 7] == 0:
                    yangben_pre[:, 7] = 0
                if yangben[:, 8] == 0:
                    yangben_pre[:, 8] = 0
                if yangben[:, 9] == 0:
                    yangben_pre[:, 9] = 0
                if yangben[:, 11] == 0:
                    yangben_pre[:, 11] = 0
                if yangben[:, 12] == 0:
                    yangben_pre[:, 12] = 0
                PRE = model.predict(yangben_pre)
                PRE = np.array(PRE)
                PRE = PRE.reshape(1, -1)
                score = PRE[0, 0]
                return score

            # 塑性
            def func1(p):
                # 拿到样本值  这个yangbenlist只是用来判断哪些元素为0
                yangben = [l1, l2, l3, l4, l5, l6, l7, l8, r1, r2, r3, r4, r5, r6, r7]
                # 对样本进行简单处理  其实不用这个好像也OK，
                yangben = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                           zip(yangben, list_min, list_max)]

                yangben = np.array(yangben)
                yangben = yangben.reshape(1, 15)


                x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = p
                list1 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15]

                yangben_chuli = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                                 zip(list1, list_min, list_max)]

                yangben_pre = np.array(yangben_chuli)
                yangben_pre = yangben_pre.reshape(1, -1)
                if yangben[:, 5] == 0:
                    yangben_pre[:, 5] = 0
                if yangben[:, 7] == 0:
                    yangben_pre[:, 7] = 0
                if yangben[:, 8] == 0:
                    yangben_pre[:, 8] = 0
                if yangben[:, 9] == 0:
                    yangben_pre[:, 9] = 0
                if yangben[:, 11] == 0:
                    yangben_pre[:, 11] = 0
                if yangben[:, 12] == 0:
                    yangben_pre[:, 12] = 0
                PRE = model.predict(yangben_pre)
                PRE = np.array(PRE)
                PRE = PRE.reshape(1, -1)
                score = PRE[0, 1]
                return score

            # 综合
            def func2(p):
                # 拿到样本值
                yangben = [l1, l2, l3, l4, l5, l6, l7, l8, r1, r2, r3, r4, r5, r6, r7]
                # 对样本进行简单处理
                yangben = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                           zip(yangben, list_min, list_max)]

                yangben = np.array(yangben)
                yangben = yangben.reshape(1, 15)
                x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = p
                list1 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15]
                yangben_chuli = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                                 zip(list1, list_min, list_max)]
                yangben_pre = np.array(yangben_chuli)
                yangben_pre = yangben_pre.reshape(1, -1)
                if yangben[:, 5] == 0:
                    yangben_pre[:, 5] = 0
                if yangben[:, 7] == 0:
                    yangben_pre[:, 7] = 0
                if yangben[:, 8] == 0:
                    yangben_pre[:, 8] = 0
                if yangben[:, 9] == 0:
                    yangben_pre[:, 9] = 0
                if yangben[:, 11] == 0:
                    yangben_pre[:, 11] = 0
                if yangben[:, 12] == 0:
                    yangben_pre[:, 12] = 0
                PRE = model.predict(yangben_pre)
                PRE = np.array(PRE)
                PRE = PRE.reshape(1, -1)
                score = PRE[0, 0] + PRE[0, 1] * 5
                return score

            ga_shouming = GA(func=func0, n_dim=15, size_pop=10, max_iter=100, prob_mut=0.001,
                           lb=[l1 - 0.05 * l1, l2 - 0.05 * l2, l3 - 0.05 * l3
                               , l4 - 0.05 * l4, l5 - 0.05 * l5, 0, l7 - 0.05 * l7, 0
                               , 0, 0, r3 - 0.05 * r3, 0, 0
                               ,  r6 - 0.05 * r6, r7 - 0.05 * r7],
                             ub=[l1 + 0.05 * l1, l2 + 0.05 * l2, l3 + 0.05 * l3
                                 , l4 + 0.05 * l4, l5 + 0.05 * l5, 6.6, l7 + 0.05 * l7, 0.006
                                 , 0.06, 0.96, r3 + 0.05 * r3, 0.5, 1.02
                                 ,  r6 + 0.05 * r6, r7 + 0.05 * r7]
                             )
            ga_suxing = GA(func=func1, n_dim=15, size_pop=10, max_iter=100, prob_mut=0.001,
                           lb=[l1 - 0.05 * l1, l2 - 0.05 * l2, l3 - 0.05 * l3
                               , l4 - 0.05 * l4, l5 - 0.05 * l5, 0, l7 - 0.05 * l7, 0
                               , 0, 0, r3 - 0.05 * r3, 0, 0
                               ,  r6 - 0.05 * r6, r7 - 0.05 * r7],
                           ub=[l1 + 0.05 * l1, l2 + 0.05 * l2, l3 + 0.05 * l3
                               , l4 + 0.05 * l4, l5 + 0.05 * l5, 6.6, l7 + 0.05 * l7, 0.006
                               , 0.06, 0.96, r3 + 0.05 * r3, 0.5, 1.02
                               , r6 + 0.05 * r6, r7 + 0.05 * r7]
                           )

            ga_zonghe = GA(func=func2, n_dim=15, size_pop=10, max_iter=100, prob_mut=0.001,
                           lb=[l1 - 0.05 * l1, l2 - 0.05 * l2, l3 - 0.05 * l3
                               , l4 - 0.05 * l4, l5 - 0.05 * l5, 0, l7 - 0.05 * l7, 0
                               , 0, 0, r3 - 0.05 * r3, 0, 0
                               ,  r6 - 0.05 * r6, r7 - 0.05 * r7],
                           ub=[l1 + 0.05 * l1, l2 + 0.05 * l2, l3 + 0.05 * l3
                               , l4 + 0.05 * l4, l5 + 0.05 * l5, 6.6, l7 + 0.05 * l7, 0.006
                               , 0.06, 0.96, r3 + 0.05 * r3, 0.5, 1.02
                               , r6 + 0.05 * r6, r7 + 0.05 * r7]
                           )
            # 运行遗传算法
            best_x1, best_y1 = ga_shouming.run()
            best_x2, best_y2 = ga_suxing.run()
            best_x3, best_y3 = ga_zonghe.run()

            # 取出最好的组   得到的max_x11是narray数组形式  长度为100
            # 取出各自的序列
            max_x11_shouming = ga_shouming.generation_best_X
            max_x11_suxing = ga_suxing.generation_best_X
            max_x11_zonghe = ga_zonghe.generation_best_X
            # 组合
            max_x11 = max_x11_shouming + max_x11_suxing + max_x11_zonghe

            # 将遗传算法得到的X组合归一化后预测
            pre_list_x11 = []
            for i in range(len(max_x11)):
                list_x = max_x11[i].tolist()
                list_x_one = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                              zip(list_x, list_min, list_max)]
                np_x_one = np.array(list_x_one)
                np_x_one = np_x_one.reshape(1, -1)
                pre = model.predict(np_x_one)
                pre_list_x11.append(pre)
            print("ceshi_pre_list_x11", pre_list_x11[1][0])  # 是单个值  寿命的值

            # 获取值  挑选出最大值来  寿命和塑性最大值
            # 获取值  挑选出最大值来
            max_shouming = 0.0
            max_suxing = 0.0
            max_zonghe = 0.0
            max_shouming_list = [0.0, 0.0]
            max_suxing_list = [0.0, 0.0]
            max_zonghe_list = [0.0, 0.0]
            max_index = [0, 0, 0]
            # 这个for循环用于找到三种情况（寿命、塑性和综合情况）中各自的最佳寿命和塑性
            for i in range(len(pre_list_x11)):
                # 每个if针对一个情况   max_shouming_list会保存寿命和塑性  max_index记录索引，以便推荐各个元素具体值
                if pre_list_x11[i][0] > max_shouming:
                    max_shouming = pre_list_x11[i][0]
                    # max_shouming_list： 始终保持最大值
                    max_shouming_list[0] = max_shouming
                    max_shouming_list[1] = pre_list_x11[i][1]
                    max_index[0] = i
                if pre_list_x11[i][1] > max_suxing:
                    max_suxing = pre_list_x11[i][1]
                    max_suxing_list[0] = pre_list_x11[i][0]
                    max_suxing_list[1] = max_suxing
                    max_index[1] = i
                if (pre_list_x11[i][0] + pre_list_x11[i][1] * 5.0) > max_zonghe:
                    max_zonghe = pre_list_x11[i][0] + pre_list_x11[i][1] * 5.0
                    max_zonghe_list[0] = pre_list_x11[i][0]
                    max_zonghe_list[1] = pre_list_x11[i][1]
                    max_index[2] = i

            str_3 = ('针对二目标优化结果推荐：' + '\n' + 'Cr：' + str(round(max_x11[1][0], 3)) + '  Co：' + \
                     str(round(max_x11[max_index[2]][1], 3)) + '  Mo：' + str(
                        round(max_x11[max_index[2]][2], 3)) + '  W：' + str(round(max_x11[max_index[2]][3], 3)) + '  Ta：' + \
                     str(round(max_x11[max_index[2]][4], 3)) + '  Re：' + str(
                        round(max_x11[max_index[2]][5], 3)) + '  Al：' + str(round(max_x11[max_index[2]][6], 3)) + '  B：' + \
                     str(round(max_x11[max_index[2]][7], 3)) + '  C：' + str(
                        round(max_x11[max_index[2]][8], 3)) + '  Hf：' + str(round(max_x11[max_index[2]][9], 3)) + '  Ni：' + \
                     str(round(max_x11[max_index[2]][10], 3)) + '  Nb：' + str(
                        round(max_x11[max_index[2]][11], 3)) + '  Ti：' + str(round(max_x11[max_index[2]][12], 3)) +
                     '  温度：' + str(r6) + '  应力：' + str(r7) + '\n')
            print("str_3", str_3)
            self.ui.textBrowser_7.setText('寿命最优值:' + str(max_zonghe_list[0][0][0]))
            self.ui.textBrowser_8.setText('塑性最优值:' + str(max_zonghe_list[1][0][0]))
            result_yuansu = str_3

            print("list_yuan", list_yuan)

    def on_pushButton_shezhi_5_clicked(self):
        global list_yuan, result_yuansu
        l1 = self.ui.doubleSpinBox_1.value()
        l2 = self.ui.doubleSpinBox_2.value()
        l3 = self.ui.doubleSpinBox_3.value()
        l4 = self.ui.doubleSpinBox_4.value()
        l5 = self.ui.doubleSpinBox_5.value()
        l6 = self.ui.doubleSpinBox_6.value()
        l7 = self.ui.doubleSpinBox_7.value()
        l8 = self.ui.doubleSpinBox_8.value()
        r1 = self.ui.doubleSpinBox_9.value()
        r2 = self.ui.doubleSpinBox_10.value()
        r3 = self.ui.doubleSpinBox_11.value()
        r4 = self.ui.doubleSpinBox_12.value()
        r5 = self.ui.doubleSpinBox_13.value()
        r6 = self.ui.doubleSpinBox_14.value()
        r7 = self.ui.doubleSpinBox_15.value()

        a = int(l1)
        b = int(r7)
        if a == 0 or b == 0:
            QMessageBox.warning(self, "提示", "选择数据出现错误！请重新选择！",
                                QMessageBox.Yes)


        else:
            list_min = [5.5, 4.5, 0.61, 1.35, 5.9, 0.0, 2.8, 0.0, 0.0, 0.0, 60.745, 0.0, 0.0, 800.0, 130.0]
            list_max = [7.2, 9.6, 5.0, 6.5, 7.0, 6.6, 6.8, 0.006, 0.06, 0.96, 70.7, 0.5, 1.02, 1100.0, 750.0]

            # modelname = "./weights_h5/model.h5"
            modelname = "D:\\ui_hejin_plus\\weight_h5\\model.h5"
            model = tf.keras.models.load_model(modelname, compile=False)  # 加载模型出错
            # predict1 = model.predict(data)
            # predict1 = np.array(predict1)
            # predict1 = predict1.reshape(1, -1)

            # 将界面上展示的个个元素含量封装在这个list下
            list_yuan = [l1, l2, l3, l4, l5, l6, l7, l8, r1, r2, r3, r4, r5, r6, r7]

            # 推荐
            # 寿命
            def func0(p):
                # 拿到样本值
                yangben = [l1, l2, l3, l4, l5, l6, l7, l8, r1, r2, r3, r4, r5, r6, r7]
                # 对样本进行简单处理  归一化操作
                yangben = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                           zip(yangben, list_min, list_max)]

                yangben = np.array(yangben)
                yangben = yangben.reshape(1, 15)
                x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = p
                list1 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15]

                yangben_chuli = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                                 zip(list1, list_min, list_max)]

                yangben_pre = np.array(yangben_chuli)
                yangben_pre = yangben_pre.reshape(1, -1)
                if yangben[:, 5] == 0:
                    yangben_pre[:, 5] = 0
                if yangben[:, 7] == 0:
                    yangben_pre[:, 7] = 0
                if yangben[:, 8] == 0:
                    yangben_pre[:, 8] = 0
                if yangben[:, 9] == 0:
                    yangben_pre[:, 9] = 0
                if yangben[:, 11] == 0:
                    yangben_pre[:, 11] = 0
                if yangben[:, 12] == 0:
                    yangben_pre[:, 12] = 0
                PRE = model.predict(yangben_pre)
                PRE = np.array(PRE)
                PRE = PRE.reshape(1, -1)
                score = PRE[0, 0]
                return score

            # 塑性
            def func1(p):
                # 拿到样本值  这个yangbenlist只是用来判断哪些元素为0
                yangben = [l1, l2, l3, l4, l5, l6, l7, l8, r1, r2, r3, r4, r5, r6, r7]
                # 对样本进行简单处理  其实不用这个好像也OK，
                yangben = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                           zip(yangben, list_min, list_max)]

                yangben = np.array(yangben)
                yangben = yangben.reshape(1, 15)


                x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = p
                list1 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15]

                yangben_chuli = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                                 zip(list1, list_min, list_max)]

                yangben_pre = np.array(yangben_chuli)
                yangben_pre = yangben_pre.reshape(1, -1)
                if yangben[:, 5] == 0:
                    yangben_pre[:, 5] = 0
                if yangben[:, 7] == 0:
                    yangben_pre[:, 7] = 0
                if yangben[:, 8] == 0:
                    yangben_pre[:, 8] = 0
                if yangben[:, 9] == 0:
                    yangben_pre[:, 9] = 0
                if yangben[:, 11] == 0:
                    yangben_pre[:, 11] = 0
                if yangben[:, 12] == 0:
                    yangben_pre[:, 12] = 0
                PRE = model.predict(yangben_pre)
                PRE = np.array(PRE)
                PRE = PRE.reshape(1, -1)
                score = PRE[0, 1]
                return score

            # 综合
            def func2(p):
                # 拿到样本值
                yangben = [l1, l2, l3, l4, l5, l6, l7, l8, r1, r2, r3, r4, r5, r6, r7]
                # 对样本进行简单处理
                yangben = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                           zip(yangben, list_min, list_max)]

                yangben = np.array(yangben)
                yangben = yangben.reshape(1, 15)
                x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = p
                list1 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15]
                yangben_chuli = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                                 zip(list1, list_min, list_max)]
                yangben_pre = np.array(yangben_chuli)
                yangben_pre = yangben_pre.reshape(1, -1)
                if yangben[:, 5] == 0:
                    yangben_pre[:, 5] = 0
                if yangben[:, 7] == 0:
                    yangben_pre[:, 7] = 0
                if yangben[:, 8] == 0:
                    yangben_pre[:, 8] = 0
                if yangben[:, 9] == 0:
                    yangben_pre[:, 9] = 0
                if yangben[:, 11] == 0:
                    yangben_pre[:, 11] = 0
                if yangben[:, 12] == 0:
                    yangben_pre[:, 12] = 0
                PRE = model.predict(yangben_pre)
                PRE = np.array(PRE)
                PRE = PRE.reshape(1, -1)
                score = PRE[0, 0] + PRE[0, 1] * 5
                return score

            ga_shouming = GA(func=func0, n_dim=15, size_pop=10, max_iter=100, prob_mut=0.001,
                           lb=[l1 - 0.05 * l1, l2 - 0.05 * l2, l3 - 0.05 * l3
                               , l4 - 0.05 * l4, l5 - 0.05 * l5, 0, l7 - 0.05 * l7, 0
                               , 0, 0, r3 - 0.05 * r3, 0, 0
                               ,  r6 - 0.05 * r6, r7 - 0.05 * r7],
                             ub=[l1 + 0.05 * l1, l2 + 0.05 * l2, l3 + 0.05 * l3
                                 , l4 + 0.05 * l4, l5 + 0.05 * l5, 6.6, l7 + 0.05 * l7, 0.006
                                 , 0.06, 0.96, r3 + 0.05 * r3, 0.5, 1.02
                                 ,  r6 + 0.05 * r6, r7 + 0.05 * r7]
                             )
            ga_suxing = GA(func=func1, n_dim=15, size_pop=10, max_iter=100, prob_mut=0.001,
                           lb=[l1 - 0.05 * l1, l2 - 0.05 * l2, l3 - 0.05 * l3
                               , l4 - 0.05 * l4, l5 - 0.05 * l5, 0, l7 - 0.05 * l7, 0
                               , 0, 0, r3 - 0.05 * r3, 0, 0
                               ,  r6 - 0.05 * r6, r7 - 0.05 * r7],
                           ub=[l1 + 0.05 * l1, l2 + 0.05 * l2, l3 + 0.05 * l3
                               , l4 + 0.05 * l4, l5 + 0.05 * l5, 6.6, l7 + 0.05 * l7, 0.006
                               , 0.06, 0.96, r3 + 0.05 * r3, 0.5, 1.02
                               , r6 + 0.05 * r6, r7 + 0.05 * r7]
                           )

            ga_zonghe = GA(func=func2, n_dim=15, size_pop=10, max_iter=100, prob_mut=0.001,
                           lb=[l1 - 0.05 * l1, l2 - 0.05 * l2, l3 - 0.05 * l3
                               , l4 - 0.05 * l4, l5 - 0.05 * l5, 0, l7 - 0.05 * l7, 0
                               , 0, 0, r3 - 0.05 * r3, 0, 0
                               ,  r6 - 0.05 * r6, r7 - 0.05 * r7],
                           ub=[l1 + 0.05 * l1, l2 + 0.05 * l2, l3 + 0.05 * l3
                               , l4 + 0.05 * l4, l5 + 0.05 * l5, 6.6, l7 + 0.05 * l7, 0.006
                               , 0.06, 0.96, r3 + 0.05 * r3, 0.5, 1.02
                               , r6 + 0.05 * r6, r7 + 0.05 * r7]
                           )
            # 运行遗传算法
            best_x1, best_y1 = ga_shouming.run()
            best_x2, best_y2 = ga_suxing.run()
            best_x3, best_y3 = ga_zonghe.run()

            # 取出最好的组   得到的max_x11是narray数组形式  长度为100
            # 取出各自的序列
            max_x11_shouming = ga_shouming.generation_best_X
            max_x11_suxing = ga_suxing.generation_best_X
            max_x11_zonghe = ga_zonghe.generation_best_X
            # 组合
            max_x11 = max_x11_shouming + max_x11_suxing + max_x11_zonghe

            # 将遗传算法得到的X组合归一化后预测
            pre_list_x11 = []
            for i in range(len(max_x11)):
                list_x = max_x11[i].tolist()
                list_x_one = [(a - b) / (c - b) if (c - b) != 0 else 0 for a, b, c in
                              zip(list_x, list_min, list_max)]
                np_x_one = np.array(list_x_one)
                np_x_one = np_x_one.reshape(1, -1)
                pre = model.predict(np_x_one)
                pre_list_x11.append(pre)
            print("ceshi_pre_list_x11", pre_list_x11[1][0])  # 是单个值  寿命的值

            # 获取值  挑选出最大值来  寿命和塑性最大值
            # 获取值  挑选出最大值来
            max_shouming = 0.0
            max_suxing = 0.0
            max_zonghe = 0.0
            max_shouming_list = [0.0, 0.0]
            max_suxing_list = [0.0, 0.0]
            max_zonghe_list = [0.0, 0.0]
            max_index = [0, 0, 0]
            # 这个for循环用于找到三种情况（寿命、塑性和综合情况）中各自的最佳寿命和塑性
            for i in range(len(pre_list_x11)):
                # 每个if针对一个情况   max_shouming_list会保存寿命和塑性  max_index记录索引，以便推荐各个元素具体值
                if pre_list_x11[i][0] > max_shouming:
                    max_shouming = pre_list_x11[i][0]
                    # max_shouming_list： 始终保持最大值
                    max_shouming_list[0] = max_shouming
                    max_shouming_list[1] = pre_list_x11[i][1]
                    max_index[0] = i
                if pre_list_x11[i][1] > max_suxing:
                    max_suxing = pre_list_x11[i][1]
                    max_suxing_list[0] = pre_list_x11[i][0]
                    max_suxing_list[1] = max_suxing
                    max_index[1] = i
                if (pre_list_x11[i][0] + pre_list_x11[i][1] * 5.0) > max_zonghe:
                    max_zonghe = pre_list_x11[i][0] + pre_list_x11[i][1] * 5.0
                    max_zonghe_list[0] = pre_list_x11[i][0]
                    max_zonghe_list[1] = pre_list_x11[i][1]
                    max_index[2] = i

            str_3 = ('针对二目标优化结果推荐：' + '\n' + 'Cr：' + str(round(max_x11[1][0], 3)) + '  Co：' + \
                     str(round(max_x11[max_index[2]][1], 3)) + '  Mo：' + str(
                        round(max_x11[max_index[2]][2], 3)) + '  W：' + str(round(max_x11[max_index[2]][3], 3)) + '  Ta：' + \
                     str(round(max_x11[max_index[2]][4], 3)) + '  Re：' + str(
                        round(max_x11[max_index[2]][5], 3)) + '  Al：' + str(round(max_x11[max_index[2]][6], 3)) + '  B：' + \
                     str(round(max_x11[max_index[2]][7], 3)) + '  C：' + str(
                        round(max_x11[max_index[2]][8], 3)) + '  Hf：' + str(round(max_x11[max_index[2]][9], 3)) + '  Ni：' + \
                     str(round(max_x11[max_index[2]][10], 3)) + '  Nb：' + str(
                        round(max_x11[max_index[2]][11], 3)) + '  Ti：' + str(round(max_x11[max_index[2]][12], 3)) +
                     '  温度：' + str(r6) + '  应力：' + str(r7) + '\n')
            print("str_3", str_3)
            self.ui.textBrowser_7.setText('寿命最优值:' + str(max_zonghe_list[0][0][0]))
            self.ui.textBrowser_8.setText('塑性最优值:' + str(max_zonghe_list[1][0][0]))
            result_yuansu = str_3

            print("list_yuan", list_yuan)



    # 优化界面
    @pyqtSlot()
    def on_pushButton_youhua_clicked(self):
        self.signal_yuansu.emit(list_yuan)
        self.youhua.show()

    @pyqtSlot()
    def on_pushButton_shezhi_1_clicked(self):
        QMessageBox.warning(self, "提示！", "该功能暂未开通！", QMessageBox.Yes)

    @pyqtSlot()
    def on_pushButton_shezhi_2_clicked(self):
        QMessageBox.warning(self, "提示！", "该功能暂未开通！", QMessageBox.Yes)

    @pyqtSlot()
    def on_pushButton_shezhi_3_clicked(self):
        QMessageBox.warning(self, "提示！", "该功能暂未开通！", QMessageBox.Yes)

    @pyqtSlot()
    def on_pushButton_shezhi_6_clicked(self):
        QMessageBox.warning(self, "提示！", "该功能暂未开通！", QMessageBox.Yes)

    @pyqtSlot()
    def on_pushButton_shezhi_7_clicked(self):
        QMessageBox.warning(self, "提示！", "该功能暂未开通！", QMessageBox.Yes)



if __name__ == '__main__':
    # ====== 主程序 ======
    app = QApplication(sys.argv)
    # mw = login_Window()

    login_window = login_Window()
    main_window = Main_Window()
    login_window.show()


    sys.exit(app.exec_())

