# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\代码\云端同步\Python\Pyqt\UI\socket客户端.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(120, 70, 561, 241))
        self.text.setObjectName("text")
        self.fasong = QtWidgets.QPushButton(self.centralwidget)
        self.fasong.setGeometry(QtCore.QRect(460, 440, 91, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(False)
        self.fasong.setFont(font)
        self.fasong.setObjectName("fasong")
        self.guanbi = QtWidgets.QPushButton(self.centralwidget)
        self.guanbi.setGeometry(QtCore.QRect(620, 440, 91, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.guanbi.setFont(font)
        self.guanbi.setObjectName("guanbi")
        self.qingkong = QtWidgets.QPushButton(self.centralwidget)
        self.qingkong.setGeometry(QtCore.QRect(130, 320, 81, 31))
        self.qingkong.setObjectName("qingkong")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 500, 281, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.zhuangtai = QtWidgets.QLineEdit(self.frame)
        self.zhuangtai.setGeometry(QtCore.QRect(100, 20, 171, 20))
        self.zhuangtai.setObjectName("zhuangtai")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(270, 320, 331, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(240, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.qingkong.clicked.connect(self.text.clear)
        self.guanbi.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.fasong.clicked.connect(self.net)
        self.test()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "客户端（发送消息）"))
        self.fasong.setText(_translate("MainWindow", "发送"))
        self.guanbi.setText(_translate("MainWindow", "关闭"))
        self.qingkong.setText(_translate("MainWindow", "清空消息"))
        self.label_2.setText(_translate("MainWindow", "状态栏"))
        self.label_3.setText(_translate("MainWindow", "服务器IP："))
        self.lineEdit.setText(_translate("MainWindow", "127.0.0.1"))
        self.pushButton.setText(_translate("MainWindow", "连接"))

    def test(self):
        self.text.appendPlainText('啊 加个文字')
        self.zhuangtai.setText('测试开始~')
        self.lineEdit.setText('127.0.0.1')

    def net(self):
        sk=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip=self.lineEdit.text()
        sk.connect((ip,1082))
        self.zhuangtai.setText('连接服务器')

        try:
            information=self.text.toPlainText()
            print('获得文字')
            sk.sendall(information.encode())
            print('发送消息')
            reply=sk.recv(1024).decode()
            print('接收反馈')
            self.zhuangtai.setText(reply)
        except:
            print('net2出错')
        sk.close()




def do():
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
do()