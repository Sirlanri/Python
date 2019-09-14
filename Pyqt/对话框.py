import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor,QIcon

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


#选择字体
class Font(QWidget):

    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(self):
        vbox=QVBoxLayout()
        bt1=QPushButton('打开窗口',self)
        bt1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)

        bt1.move(20,20)
        vbox.addWidget(bt1)
        bt1.clicked.connect(self.showDia)

        self.lbl=QLabel('你们要努力提高自己的姿势水平',self)
        self.lbl.move(130,20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300,300,250,200)
        self.setWindowTitle('选择字体')
        self.show()

    def showDia(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)
def doFont():
    app=QApplication(sys.argv)
    ex=Font()
    sys.exit(app.exec_())


#选择文件目录的
class File(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(sell):
        self.textEdit=QTextEdit()
        self.setCentralWiget(self.textEdit)
        self.statusBar()

        openfile=QAction(QIcon('open.png'),'打开',self)
        openfile.setShortcut('Ctrl+O')
        openfile.setStatusTip('打开新文件')
        openfile.triggered.connect(self.showDio)

        menubar=self.menuBar()
        fileMenu=menubar.addMenu('&file')
        fileMenu.addAction(openfile)
        
        self.setGeometry(300,300,400,300)
        self.setWindowTitle('读取文件')
        self.show()

    def showDio(self):
        
        fname=QFileDialog.getOpenFileName(self,'打开文件夹~','/home')

        if fname[0]:
            f=open(fname[0],'r')

            with f:
                data=f.read()
                self.textEdit.setText(data)
def doFile():
    app=QApplication(sys.argv)
    ex=File()
    sys.exit(app.exec_())