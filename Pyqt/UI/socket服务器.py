# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\代码\云端同步\Python\Pyqt\UI\socket服务器.ui'
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
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(80, 60, 521, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.xiaoxi = QtWidgets.QPlainTextEdit(self.frame)
        self.xiaoxi.setGeometry(QtCore.QRect(0, 0, 531, 281))
        self.xiaoxi.setObjectName("xiaoxi")
        self.tou = QtWidgets.QLabel(self.centralwidget)
        self.tou.setGeometry(QtCore.QRect(20, 10, 201, 21))
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 360, 321, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(19, 20))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.guanbi.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.zhuangtai.clear)
        self.pushButton.pressed.connect(self.lineEdit.selectAll)
        self.pushButton.released.connect(self.lineEdit.copy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.getip()
        self.pushButton.clicked.connect(self.net)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.xiaoxi.setPlainText(_translate("MainWindow", "消息框"))
        self.tou.setText(_translate("MainWindow", "服务器（接收消息）"))
        self.guanbi.setText(_translate("MainWindow", "关闭"))
        self.label_2.setText(_translate("MainWindow", "状态栏："))
        self.label.setText(_translate("MainWindow", "本地IP："))
        self.pushButton.setText(_translate("MainWindow", "复制IP"))

    def getip(self):
        ip=socket.gethostbyname(socket.gethostname())
        self.lineEdit.setText(ip)

    def net(self):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ip_port=('127.0.0.1',1082)
        s.bind(ip_port)
        s.listen(5) #监听链接请求
        
        print('成功启动~')
        conn,address=s.accept() #等待连接

        while 1:
            client_data=conn.recv(1024).decode()
            if client_data=='exit':
                exit('接收到结束请求，结束通讯')
                break
            print('客户端消息：{}'.format(client_data))
            conn.sendall('回馈消息'.encode())
        conn.close()


def do():
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
def test_net():
    ex=Ui_MainWindow()
    ex.net()
test_net()