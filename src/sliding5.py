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
        self.offset = 10
        self.pos = 0
        self.initUI()
        self.set_delta()
    
    def set_delta(self):
        # Set a delta value between a label size and a main widget size
        self.delta = self.geometry().width() - self.label.geometry().width()
    
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
        if self.label.geometry().x() - self.offset >= self.delta:
            self.pos -= self.offset
            self.label.move(self.pos,0)
    
    def slide_right(self):
        if self.label.geometry().x() + self.offset <= 0:
            self.pos += self.offset
            self.label.move(self.pos,0)
    
    def trigger_hover(self,event):
        ''' We shouldn't use event.x since this returns x relative to
            the widget that caused the event, and this is widget will be
            any we have mouse over.
        '''
        geom = self.geometry()
        x = PyQt5.QtGui.QCursor().pos().x() - geom.left()
        width = geom.width()
        if 0 <= x <= 30:
            self.slide_right()
        elif width - 30 <= x <= width:
            self.slide_left()
    
    def eventFilter(self,source,event):
        if event.type() == PyQt5.QtCore.QEvent.MouseMove:
            self.trigger_hover(event)
        return super().eventFilter(source,event)
    
    def initUI(self):
        self.setWindowTitle(self.title)
        
        self.setStyleSheet('QPushButton:hover {background-color: white} QToolTip {background-color: #ffffe0}')
        
        self.label = PyQt5.QtWidgets.QWidget(self)
        
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
        
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

    @PyQt5.QtCore.pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = App()
    ''' We can get a constant mouse hovering response only if we install
        the filter like this.
    '''
    app.installEventFilter(ex)
    sys.exit(app.exec_())
