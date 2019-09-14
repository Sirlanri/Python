import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class Status(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.statusBar().showMessage('显示状态栏')#显示在左下角
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('状态bar')
        self.show()
def doStatue():
    app=QApplication(sys.argv)
    status=Status()
    sys.exit(app.exec_())


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        exitAction=QAction(QIcon('exit.png'),'退出',self)
        exitAction.setShortcut('Cirl+Q')
        exitAction.setStatusTip('可退出程序')
        exitAction.triggered.connet(qApp.quit())

        self.statusBar()

        #创建菜单栏
        menubar=self.menuBar()
        #添加菜单
        fileMenu=menubar.addMenu('$file')
        #添加事件
        fileMenu.addAction(exitAction)

        self.setGeometry(500,500,900,800)
        self.setWindowTitle('MenuBar')
        self.show()
def doMenu():
    app=QApplication(sys.argv)
    ex=Menu()
    sys.exit(app.exec_())


#工具栏
class Tolls(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()
    #懒得写了咕咕咕