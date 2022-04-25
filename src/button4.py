#https://pythonspot.com/pyqt5-buttons/
import sys
import PyQt5
import PyQt5.QtWidgets

icon1 = '/home/pete/bin/mclient/resources/buttons/icon_36x36_bottom.gif'
icon2 = '/home/pete/bin/mclient/resources/buttons/icon_36x36_priority_on.gif'
icon3 = '/home/pete/bin/mclient/resources/buttons/icon_36x36_settings.gif'
icon4 = '/home/pete/bin/mclient/resources/buttons/icon_36x36_toggle_history.gif'
icon5 = '/home/pete/bin/mclient/resources/buttons/icon_36x36_top.gif'


class App(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 500
        self.top = 500
        self.width = 320
        self.height = 44
        self.initUI()
    
    def create_button(self,icon,action,width=36,height=36,movex=4,movey=4,tooltip='This is an example button'):
        button = PyQt5.QtWidgets.QPushButton('',self)
        button.setToolTip(tooltip)
        button.resize(width,height)
        button.move(movex,movey)
        # Setting a button image with button.setStyleSheet('image: url({})'.format(path)) causes tooltip glitches
        button.setIcon(PyQt5.QtGui.QIcon(icon))
        button.setIconSize(PyQt5.QtCore.QSize(width,height))
        button.setStyleSheet('border: 0px')
        button.clicked.connect(action)
        return button
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.setStyleSheet('QPushButton:hover {background-color: white} QToolTip {background-color: #ffffe0}')
        
        button = self.create_button (icon = icon1
                                    ,action = self.on_click
                                    ,movex = 4
                                    ,movey = 4
                                    ,tooltip = 'This is Button 1'
                                    )
        
        button2 = self.create_button (icon = icon2
                                     ,action = self.on_click
                                     ,movex = 43
                                     ,movey = 4
                                     ,tooltip = 'This is Button 2'
                                     )
        
        button3 = self.create_button (icon = icon3
                                     ,action = self.on_click
                                     ,movex = 82
                                     ,movey = 4
                                     ,tooltip = 'This is Button 3'
                                     )

        button4 = self.create_button (icon = icon4
                                     ,action = self.on_click
                                     ,movex = 121
                                     ,movey = 4
                                     ,tooltip = 'This is Button 4'
                                     )
        
        button5 = self.create_button (icon = icon5
                                     ,action = self.on_click
                                     ,movex = 160
                                     ,movey = 4
                                     ,tooltip = 'This is Button 5'
                                     )
        
        button6 = self.create_button (icon = icon1
                                     ,action = self.on_click
                                     ,movex = 199
                                     ,movey = 4
                                     ,tooltip = 'This is Button 6'
                                     )
        
        button7 = self.create_button (icon = icon2
                                     ,action = self.on_click
                                     ,movex = 238
                                     ,movey = 4
                                     ,tooltip = 'This is Button 7'
                                     )

        button8 = self.create_button (icon = icon3
                                     ,action = self.on_click
                                     ,movex = 277
                                     ,movey = 4
                                     ,tooltip = 'This is Button 8'
                                     )

        button9 = self.create_button (icon = icon4
                                     ,action = self.on_click
                                     ,movex = 316
                                     ,movey = 4
                                     ,tooltip = 'This is Button 9'
                                     )
        
        self.show()

    @PyQt5.QtCore.pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
