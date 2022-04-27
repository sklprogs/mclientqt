#https://pythonspot.com/pyqt5-buttons/
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

ICON = '/home/pete/bin/mclient/resources/buttons/icon_36x36_bottom.gif'
#ICON = '/home/pete/downloads/Actions-address-book-new-icon.png'


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 800
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.setStyleSheet('QPushButton:hover {background-color: white;}')
        
        # 'PyQt5 button'
        button = QPushButton('',self)
        button.setToolTip('This is an example button')
        #button.resize(36,36)
        button.setGeometry(0,0,36,36)
        button.move(400,400)
        #button.resize(50,50)
        #button.setIcon(PyQt5.QtGui.QIcon(ICON))
        #button.setStyleSheet("border-image : url({});".format(ICON))
        #iicon = QIcon(ICON)
        #isize = PyQt5.QtCore.QSize(36,36)
        #button.setIcon(iicon)
        #button.setIconSize(isize)
        button.setStyleSheet('image: url({}); border: 0px'.format(ICON))
        button.clicked.connect(self.on_click)
        
        self.show()
        print(button.isVisible())

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
