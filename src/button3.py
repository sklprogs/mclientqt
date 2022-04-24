#https://pythonspot.com/pyqt5-buttons/
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

icon1 = '/home/pete/bin/mclient/resources/buttons/icon_36x36_bottom.gif'
icon2 = '/home/pete/bin/mclient/resources/buttons/icon_36x36_priority_on.gif'
icon3 = '/home/pete/bin/mclient/resources/buttons/icon_36x36_settings.gif'
icon4 = '/home/pete/bin/mclient/resources/buttons/icon_36x36_toggle_history.gif'
icon5 = '/home/pete/bin/mclient/resources/buttons/icon_36x36_top.gif'


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 500
        self.top = 500
        self.width = 320
        self.height = 44
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.setStyleSheet('QPushButton:hover {background-color: white;}')
        
        button = QPushButton('',self)
        button.setToolTip('This is an example button')
        button.resize(36,36)
        button.move(4,4)
        button.setStyleSheet("border-image : url({});".format(icon1))
        button.clicked.connect(self.on_click)
        
        button2 = QPushButton('', self)
        button2.setToolTip('This is an example button')
        button2.resize(36,36)
        button2.move(43,4)
        button2.setStyleSheet("border-image : url({});".format(icon2))
        button2.clicked.connect(self.on_click)
        
        button3 = QPushButton('', self)
        button3.setToolTip('This is an example button')
        button3.resize(36,36)
        button3.move(82,4)
        button3.setStyleSheet("border-image : url({});".format(icon3))
        button3.clicked.connect(self.on_click)
        
        button4 = QPushButton('', self)
        button4.setToolTip('This is an example button')
        button4.resize(36,36)
        button4.move(121,4)
        button4.setStyleSheet("border-image : url({});".format(icon4))
        button4.clicked.connect(self.on_click)
        
        button5 = QPushButton('', self)
        button5.setToolTip('This is an example button')
        button5.resize(36,36)
        button5.move(160,4)
        button5.setStyleSheet("border-image : url({});".format(icon5))
        button5.clicked.connect(self.on_click)
        
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
