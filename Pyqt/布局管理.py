import sys
from PyQt5.QtWidgets import *


#绝对定位
class Absolute(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        lbl1=QLabel('喵喵喵？',self)
        lbl1.move(15,10)

        lbl2=QLabel('汪汪汪？',self)
        lbl2.move(35,40)

        lbl3=QLabel('光复艾尔！',self)#干，我也不知道教程那玩意儿啥意思，我就随便写写名字吧
        lbl3.move(55,70)

        self.setGeometry(400,300,250,150)
        self.setWindowTitle('绝对领域')#？？？？hentai!
        self.show()
def juedui():
    qApp=QApplication(sys.argv)
    ex=Absolute()
    sys.exit(qApp.exec_())
juedui()