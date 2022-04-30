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
        self.pos = 0
        self.initUI()
    
    def create_button(self,icon,action,width=36,height=36,movex=4,movey=4,tooltip='This is an example button'):
        button = PyQt5.QtWidgets.QPushButton('',self.label)
        button.setToolTip(tooltip)
        button.resize(width,height)
        button.move(movex,movey)
        # Setting a button image with button.setStyleSheet('image: url({})'.format(path)) causes tooltip glitches
        button.setIcon(PyQt5.QtGui.QIcon(icon))
        button.setIconSize(PyQt5.QtCore.QSize(width,height))
        button.setStyleSheet('border: 0px')
        button.clicked.connect(action)
        return button
    
    def slide_left(self):
        self.pos -= 10
        self.label.move(self.pos,0)
    
    def slide_right(self):
        self.pos += 10
        self.label.move(self.pos,0)
    
    def trigger_hover(self,button):
        widget_geom = self.geometry()
        button_geom = button.geometry()
        label_geom = self.label.geometry()
        print('Widget geometry:',widget_geom)
        print('Label geometry:',label_geom)
        print('button:',button_geom)
        maxx = widget_geom.width()
        leftx = label_geom.x() + button_geom.x()
        rightx = leftx + button_geom.width()
        if leftx < 0:
            print('Left border is NOT visible')
        elif rightx > maxx:
            print('Right border is NOT visible')
        else:
            print('button is fully visible')
        print('')
        
    
    def eventFilter(self,source,event):
        if event.type() == PyQt5.QtCore.QEvent.Enter:
            self.trigger_hover(source)
        ''' *always* return a bool value (meaning that the event has
            been acted upon or not), it's common to call the base class
            implementation and then return the result of that.
        '''
        return super().eventFilter(source,event)
    
    def initUI(self):
        self.setWindowTitle(self.title)
        
        self.setStyleSheet('QPushButton:hover {background-color: white} QToolTip {background-color: #ffffe0}')
        
        self.label = PyQt5.QtWidgets.QWidget(self)
        
        PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence('A'),self.label).activated.connect(self.slide_left)
        PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence('D'),self.label).activated.connect(self.slide_right)
        
        self.button1 = self.create_button (icon = icon1
                                          ,action = self.on_click
                                          ,movex = 4
                                          ,movey = 4
                                          ,tooltip = 'This is Button 1'
                                          )
        
        self.button2 = self.create_button (icon = icon2
                                          ,action = self.on_click
                                          ,movex = 43
                                          ,movey = 4
                                          ,tooltip = 'This is Button 2'
                                          )
        
        self.button3 = self.create_button (icon = icon3
                                          ,action = self.on_click
                                          ,movex = 82
                                          ,movey = 4
                                          ,tooltip = 'This is Button 3'
                                          )

        self.button4 = self.create_button (icon = icon4
                                          ,action = self.on_click
                                          ,movex = 121
                                          ,movey = 4
                                          ,tooltip = 'This is Button 4'
                                          )
        
        self.button5 = self.create_button (icon = icon5
                                          ,action = self.on_click
                                          ,movex = 160
                                          ,movey = 4
                                          ,tooltip = 'This is Button 5'
                                          )
        
        self.button6 = self.create_button (icon = icon1
                                          ,action = self.on_click
                                          ,movex = 199
                                          ,movey = 4
                                          ,tooltip = 'This is Button 6'
                                          )
        
        self.button7 = self.create_button (icon = icon2
                                          ,action = self.on_click
                                          ,movex = 238
                                          ,movey = 4
                                          ,tooltip = 'This is Button 7'
                                          )

        self.button8 = self.create_button (icon = icon3
                                          ,action = self.on_click
                                          ,movex = 277
                                          ,movey = 4
                                          ,tooltip = 'This is Button 8'
                                          )

        self.button9 = self.create_button (icon = icon4
                                          ,action = self.on_click
                                          ,movex = 316
                                          ,movey = 4
                                          ,tooltip = 'This is Button 9'
                                          )
        self.button10 = self.create_button (icon = icon5
                                           ,action = self.on_click
                                           ,movex = 355
                                           ,movey = 4
                                           ,tooltip = 'This is Button 10'
                                           )
        
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.button1.installEventFilter(self)
        self.button2.installEventFilter(self)
        self.button3.installEventFilter(self)
        self.button4.installEventFilter(self)
        self.button5.installEventFilter(self)
        self.button6.installEventFilter(self)
        self.button7.installEventFilter(self)
        self.button8.installEventFilter(self)
        self.button9.installEventFilter(self)
        self.button10.installEventFilter(self)
        
        self.show()

    @PyQt5.QtCore.pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
