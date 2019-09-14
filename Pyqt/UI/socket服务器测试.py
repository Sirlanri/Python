# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\代码\云端同步\Python\Pyqt\UI\socket服务器测试.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import socket

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(80, 60, 521, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.xiaoxi = QtWidgets.QPlainTextEdit(self.frame)
        self.xiaoxi.setGeometry(QtCore.QRect(0, 0, 531, 281))
        self.xiaoxi.setObjectName("xiaoxi")
        self.tou = QtWidgets.QLabel(self.centralwidget)
        self.tou.setGeometry(QtCore.QRect(20, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(13)
        self.tou.setFont(font)
        self.tou.setObjectName("tou")
        self.guanbi = QtWidgets.QPushButton(self.centralwidget)
        self.guanbi.setGeometry(QtCore.QRect(590, 482, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.guanbi.setFont(font)
        self.guanbi.setObjectName("guanbi")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 520, 311, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.zhuangtai = QtWidgets.QLineEdit(self.frame_2)
        self.zhuangtai.setGeometry(QtCore.QRect(110, 20, 191, 20))
        self.zhuangtai.setObjectName("zhuangtai")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 370, 61, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.IPlan = QtWidgets.QLineEdit(self.centralwidget)
        self.IPlan.setGeometry(QtCore.QRect(150, 370, 141, 20))
        self.IPlan.setReadOnly(False)
        self.IPlan.setObjectName("IPlan")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 370, 61, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 410, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.guanbi.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.zhuangtai.clear)
        self.pushButton.pressed.connect(self.IPlan.selectAll)
        self.pushButton.released.connect(self.IPlan.copy)
        self.IPlan.textChanged['QString'].connect(self.zhuangtai.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.test()
        self.connectNet()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.xiaoxi.setPlainText(_translate("MainWindow", "消息框"))
        self.tou.setText(_translate("MainWindow", "服务器（接收消息）"))
        self.guanbi.setText(_translate("MainWindow", "关闭"))
        self.label_2.setText(_translate("MainWindow", "状态栏："))
        self.label.setText(_translate("MainWindow", "本地IP："))
        self.pushButton.setText(_translate("MainWindow", "复制IP"))
        self.pushButton_2.setText(_translate("MainWindow", "开启服务器"))

    def test(self):
        self.zhuangtai.setText('测试')
        self.zhuangtai.setText('测试2')

        
    def connectNet(self):
        
        # 获取本机IP，用于跨电脑传输
        ip = socket.gethostbyname(socket.gethostname())
        self.lineEdit.setText(ip)
        self.zhuangtai.setText('成功获取本地IP')

        # 开启socket服务
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 1081))
        s.listen(5)
        self.zhuangtai.setText('开启本地服务器')
        conn, address = s.accept()  # 等待客户端连接
        while 1:
            client_data = conn.recv(1024).decode()
            if client_data == 'shutdown58468w':
                exit('通讯结束')

            # 将接收到的信息，放入文字框
            self.xiaoxi.appendPlainText(client_data+'\n\n')
            self.zhuangtai.setText('接收到消息')
            conn.sendall('(反馈）成功接收'.encode())
        s.close()

def do():
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
do()