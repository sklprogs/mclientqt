#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import PyQt5
import PyQt5.QtWidgets


class Frame(PyQt5.QtWidgets.QMainWindow):
    
    def __init__(self):
        PyQt5.QtWidgets.QMainWindow.__init__(self)
        self.set_gui()
    
    def set_gui(self):
        self.qwidget = PyQt5.QtWidgets.QWidget(self)
        self.setCentralWidget(self.qwidget)
        self.layout = PyQt5.QtWidgets.QGridLayout()
        self.qwidget.setLayout(self.layout)
        self.frame = PyQt5.QtWidgets.QFrame(self)
        self.prm_btn = PyQt5.QtWidgets.QPushButton('button',self.frame)


app = PyQt5.QtWidgets.QApplication(sys.argv)
Frame().show()
sys.exit(app.exec())
