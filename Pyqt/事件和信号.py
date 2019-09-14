import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#使用信号槽
class Singles(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(self):
        lcd=QLCDNumber(self)
        sld=QSlider(Qt.Horizontal,self)

        vbox=QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        #将滑块的参数改动发送到数字
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('信号')
        self.show()
def doSingles():
    app=QApplication(sys.argv)
    ex=Singles()
    sys.exit(app.exec_())


#重新定义事件处理器
class ReSingle(QWidget):

    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setGeometry(600,300,500,200)
        self.setWindowTitle('重写事件处理器')
        self.show()

    #按下Esc退出程序
    def keyPressEvent(self, e):
        if e.key()==Qt.Key_Escape:
            print('操作执行成功')
            self.close()        
def doResingle():
    app=QApplication(sys.argv)
    ex=ReSingle()
    sys.exit(app.exec_())


#事件发送者
class Sender(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()
    def UI(self):
        bt1=QPushButton('按钮一号',self)
        bt1.move(30,50)
        bt2=QPushButton('第二个',self)
        bt2.move(150,50)
        bt1.clicked.connect(self.buttonClicked)
        bt2.clicked.connect(self.buttonClicked)

        self.statusBar()
        self.setGeometry(500,300,250,500)
        self.setWindowTitle('事件发送者')
        self.show()
    
    def buttonClicked(self):
        #判断信号源
        sender=self.sender()
        #更改状态栏文字
        self.setStatusBar().showMessage(sender.text()+'已经处理')
def doSender():
    app=QApplication(sys.argv)
    ex=Sender()
    sys.exit(app.exec_())


#发出自定义信号
class Communicate(QObject):
    closeApp=pyqtSignal()

class Custom(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(self):
        self.c=Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('自定义信号')
        self.show()
    
    def mousePressEvent(self,cls):
        self.c.closeApp.emit()
        return super().mousePressEvent()
def doCustom():
    app=QApplication(sys.argv)
    ex=Custom()
    sys.exit(app.exec_())
