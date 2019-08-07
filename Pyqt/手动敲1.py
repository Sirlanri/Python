import sys

# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QMessageBox
from PyQt5.QtCore import QCoreApplication


def simple():
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
    w = QWidget()
    # resize()方法调整窗口的大小。这离是250px宽150px高
    w.resize(250, 150)
    # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
    w.move(300, 300)
    # 设置窗口的标题
    w.setWindowTitle('用纯代码实现的第一个例子')
    # 显示在屏幕上
    w.show()

    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())


def tubiao():  # 带图标的
    from PyQt5.QtGui import QIcon
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('Icon')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('web.png'))

        # 显示窗口
        self.show()

class Tuichu(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        #设置一个按钮
        qbtn = QPushButton('退出！', self)
        #按钮监听关闭事件
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('可以自己关闭')    
        self.show()

def tuichu():
        app = QApplication(sys.argv)
        ex = Tuichu()
        sys.exit(app.exec_())


#弹出对话框确认关闭
class Duihuak(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__()
        self.do()
    def do(self):
        self.setGeometry(300,300,300,303)
        self.setWindowTitle('双重确认')
        self.show()
    #弹出对话框
    def closeEvent(cls, self, QCloseEvent):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()