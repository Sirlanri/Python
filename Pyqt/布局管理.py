import sys
from PyQt5.QtWidgets import *


#绝对定位
class Absolute(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        #添加文字
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


#框布局
class Box(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #尝试自己写一点点,加个文字吧
        word1=QLabel('不知道写点什么...',self)
        word2=QLabel('随便写的吧',self)
        word1.move(10,20)
        word2.move(10,40)

        OKB=QPushButton('确定')
        CB=QPushButton('取消')
        hbox=QHBoxLayout()

        hbox.addStretch(1)
        hbox.addWidget(OKB)
        hbox.addWidget(CB)

        vbox=QVBoxLayout()
        vbox.addStretch(1)#允许伸展
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('框布局')
        self.show()
def kuang():
    qApp=QApplication(sys.argv)
    ex=Box()
    sys.exit(qApp.exec_())


#表格布局
class Excel(QWidget):#表格的英文是啥？干脆就叫Excel吧
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        grid=QGridLayout()
        self.setLayout(grid)

        #懒得敲了，直接copy吧
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        
        positions=[(i,j) for i in range(5) 
        for j in range(4)]

        for position,name in zip(positions,names):
            if name=='':
                continue
            button1=QPushButton(name)
            grid.addWidget(button1,*position)#这是...指针？？？
        
        self.move(300,150)
        self.setWindowTitle('网格布局')
        self.show()
def biaoge():
    app=QApplication(sys.argv)
    ex=Excel()
    sys.exit(app.exec_())


#跨越多个行列的网格
class Nduo(QWidget):
    
    def __init__(self):
        super().__init__()
        initUI()
    
    def initUI(self):
        title=QLabel('标题')
        author=QLabel('作者')
        review=QLabel('预览')

        titleEdit=QLineEdit()
        authorEdit=QLineEdit()
        reviewEdit=QTextEdit()

        grid=QGridLayout()
        grid.setSpacing(10)#间距
        
        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)
        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)

        self.setLayout(grid)

        self.setGeometry(300,300,350,400)
        self.setWindowTitle('网格')
        self.show()
def wangge():
    app=QApplication(sys.argv)
    ex=Nduo()
    sys.exit(app.exec_())

