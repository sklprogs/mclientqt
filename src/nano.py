import sys
import PyQt5
import PyQt5.QtWidgets


class App(PyQt5.QtWidgets.QWidget):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_gui()
    
    def show(self):
        self.showMaximized()
    
    def set_widgets(self):
        self.top1 = PyQt5.QtWidgets.QLabel('Top 1')
        self.top2 = PyQt5.QtWidgets.QLabel('Top 2')
        self.layout = PyQt5.QtWidgets.QVBoxLayout()
        # Add widgets to the layout
        self.layout.addWidget(self.top1)
        self.layout.addWidget(self.top2)
        # Set the layout on the application's window
        self.setLayout(self.layout)
    
    def set_gui(self):
        self.set_title('Hello, World!')
        self.set_bindings()
        self.set_widgets()
    
    def set_title(self,title):
        self.setWindowTitle(title)
    
    def set_bindings(self):
        self.bind('Ctrl-Q',self.close)
        self.bind('Escape',self.close)
    
    def bind(self,hotkey,action):
        PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence(hotkey),self).activated.connect(action)


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())
