import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor

class Duihua(QWidget):
    '''QInputDialog提供了一种简单方便的对话框从用户得到一个值。'''
    def __init__(self):
        super().__init__()
        self.UI()
    def UI(self):
        bt1=QPushButton('开启对话',self)
        bt1.move(20,20)
        bt1.clicked.connect(self.showdiolog)#这里竟然不用加括号，好奇怪
        self.le=QLineEdit(self)
        self.le.move(130,25)

        self.setGeometry(500,500,300,150)
        self.setWindowTitle('对话框1')
        self.show()

    def showdiolog(self):
        #弹出一个新窗口，输入名字
        text,ok=QInputDialog.getText(self,
            '输入内容','你的名字是？')
        if ok:
            self.le.setText(str(text))
def doDuihua():
    app=QApplication(sys.argv)
    ex=Duihua()
    sys.exit(app.exec_())
doDuihua()


#选择颜色的对话框
class Color(QWidget):

    def __init__(self):
        super().__init__()
        UI()
    
    def UI(self):
        col=QColor(0,0,0)
        bt1=QPushButton('打开颜色',self)
        bt1.move(30,25)
        bt1.clicked.connect(self.showDio)

        self.frm=QFrame(self)
        self.frm.setStyleSheet('QWidget{背景颜色是：%s}'.format(col.name()))
        self.frm.setGeometry(300,400,500,100)

        self.setGeometry(500,400,300,200)
        self.setWindowTitle('颜色选择',self)
        self.show()
    
    def showDio(self):
        col=QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet('Qwinget{背景颜色%s}'.format(clo.name()))
def docllor():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
