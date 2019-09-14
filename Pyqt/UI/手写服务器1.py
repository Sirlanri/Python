from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import socket

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self):
        self.setWindowTitle("服务器端")
        self.resize(800,600)