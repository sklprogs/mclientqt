#https://pythonspot.com/pyqt5-buttons/
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#ICON = '/home/pete/bin/mclient/resources/buttons/icon_36x36_bottom.gif'
ICON = '/home/pete/downloads/Actions-address-book-new-icon.png'


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # 'PyQt5 button'
        button = QPushButton('', self)
        button.setToolTip('This is an example button')
        #button.setGeometry(0, 0, 64, 64)
        #button.move(100,70)
        button.resize(36,36)
        #button.resize(50,50)
        #button.setIcon(PyQt5.QtGui.QIcon(ICON))
        button.setStyleSheet("border-image : url({});".format(ICON))
        button.clicked.connect(self.on_click)
        
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
