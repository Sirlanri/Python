import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor,QPixmap

#复选框
class TwoChoose(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(self):
        cb=QCheckBox('显示标题',self)
        cb.move(30,30)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300,300,250,200)
        self.setWindowTitle('复选框')
        self.show()

    def changeTitle(self,state):
        if state==Qt.Checked:
            self.setWindowTitle('检查盒')
        else:
            self.setWindowTitle('啥都没发生')
def dotwo():
    app = QApplication(sys.argv)
    ex = TwoChoose()
    sys.exit(app.exec_())


#开关按钮
class Switch(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.UI()
    
    def UI(self):
        self.col=QColor(0,0,0)

        redb=QPushButton('红色',self)
        redb.setCheckable(True)
        redb.move(10,10)
        redb.clicked[bool].connect(self.setColor)

        greenb=QPushButton('爱你的颜色',self)
        greenb.setCheckable(True)
        greenb.move(10,100)
        greenb.clicked[bool].connect(self.setColor)

        blueb=QPushButton('深邃',self)
        blueb.setCheckable(True)
        blueb.move(10,190)
        blueb.clicked[bool].connect(self.setColor)

        self.square=QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())
        #self.square.setStyleSheet('背景颜色是{}'.format(self.col.name()))

        self.setGeometry(300,300,300,500)
        self.setWindowTitle('开关按钮')
        self.show()

    def setColor(self,pressed):
        source=self.sender()

        if pressed:
            val=255
        else:
            val=0

        #更改RGB的三个数值
        if source.text()=='红色':
            self.col.setRed(val)
        if source.text()=='爱你的颜色':
            self.col.setGreen(val)
        if source.text()=='深邃':
            self.col.setBlue(val)
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())
def doSwich():
    app = QApplication(sys.argv)
    ex = Switch()
    sys.exit(app.exec_())


#滑动条
class Huadong(QWidget):

    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):

        sld=QSlider(Qt.Horizontal,self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30,40,100,30)
        sld.valueChanged[int].connect(self.changValue)

        #滑块
        self.lable=QLabel(self)
        self.lable.setPixmap(QPixmap('audio.ico'))
        self.lable.setGeometry(160,40,80,80)

        self.setGeometry(300,300,200,300)
        self.setWindowTitle('滑动条')
        self.show()

    def changValue(self,value):
        if value==0:
            self.lable.setPixmap(QPixmap('audio.ico'))
        if value>0 and value<=30:
            self.lable.setPixmap(QPixmap('min.ico'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('med.ico'))
        else:
            self.label.setPixmap(QPixmap('max.ico'))
def dohuadong():
    app=QApplication(sys.argv)
    ex=Huadong()
    sys.exit(app.exec_())


#学习进度太慢了，不再这么详细了


#进度条
class Jindu(QWidget):

    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
 
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
 
        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
 
        self.timer = QBasicTimer()
        self.step = 0
 
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()
 
    def timerEvent(self, e):
 
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
 
        self.step = self.step + 1
        self.pbar.setValue(self.step)
 
    def doAction(self):
 
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


#日历表
class Calender(QWidget):

    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)
 
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)
 
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()
 
    def showDate(self, date):
        self.lbl.setText(date.toString())


#文本框
class TextKuang(QWidget):
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)
 
        qle.move(60, 100)
        self.lbl.move(60, 40)
 
        qle.textChanged[str].connect(self.onChanged)
 
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()
 
    #文字框改变的时候，会调用这个方法
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


#控制各个部件尺寸
class CtrlBig(QWidget):
    
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        hbox = QHBoxLayout(self)
 
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
 
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
 
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
 
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
 
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
 
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
 
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()
 
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()