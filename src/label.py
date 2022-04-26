#https://pythonspot.com/pyqt5-buttons/
import sys
import PyQt5
import PyQt5.QtWidgets


class App(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 500
        self.top = 100
        self.width = 1000
        self.height = 800
        self.initUI()
    
    def slide_right(self):
        self.label.move(self.left+100,0)
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence('Ctrl+Q'),self).activated.connect(self.close)
        PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence('Space'),self).activated.connect(self.slide_right)
        self.label = PyQt5.QtWidgets.QLabel(self)
        self.label.setText('Welcome to QLabel')
        self.show()
        

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
