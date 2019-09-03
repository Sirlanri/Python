# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\代码\云端同步\Python\Pyqt\UI\socket客户端.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 171, 41))
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
        self.frame.setGeometry(QtCore.QRect(20, 509, 261, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.zhuangtai = QtWidgets.QLineEdit(self.frame)
        self.zhuangtai.setGeometry(QtCore.QRect(60, 10, 171, 20))
        self.zhuangtai.setObjectName("zhuangtai")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.qingkong.clicked.connect(self.text.clear)
        self.guanbi.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "客户端（发送消息）"))
        self.fasong.setText(_translate("MainWindow", "发送"))
        self.guanbi.setText(_translate("MainWindow", "关闭"))
        self.qingkong.setText(_translate("MainWindow", "清空消息"))
        self.label_2.setText(_translate("MainWindow", "状态栏"))
