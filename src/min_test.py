#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import PyQt5
import PyQt5.QtWidgets


class Button:
    
    def __init__ (self,parent,text='',action=None,width=36
                 ,height=36,hint='',active=''
                 ,inactive=''
                 ):
        self.Status = False
        self.parent = parent
        self.text = text
        self.action = action
        self.width = width
        self.height = height
        self.hint = hint
        self.active = active
        self.icon = self.inactive = inactive
        self.set_gui()
    
    def activate(self):
        if not self.Status:
            self.Status = True
            self.icon = self.active
            self.set_icon()

    def inactivate(self):
        if self.Status:
            self.Status = False
            self.icon = self.inactive
            self.set_icon()
    
    def set_hint(self):
        if self.hint:
            self.widget.setToolTip(self.hint)
    
    def resize(self):
        self.widget.resize(self.width,self.height)
    
    def set_icon(self):
        ''' Setting a button image with
            button.setStyleSheet('image: url({})'.format(path)) causes
            tooltip glitches.
        '''
        if self.icon:
            self.widget.setIcon(PyQt5.QtGui.QIcon(self.icon))
    
    def set_size(self):
        if self.width and self.height:
            self.widget.setIconSize(PyQt5.QtCore.QSize(self.width,self.height))
    
    def set_border(self):
        if self.icon:
            self.widget.setStyleSheet('border: 0px')
    
    def set_action(self):
        if self.action:
            self.widget.clicked.connect(self.action)
    
    def set_gui(self):
        self.widget = PyQt5.QtWidgets.QPushButton(self.text,self.parent)
        self.resize()
        self.set_icon()
        self.set_size()
        self.set_border()
        self.set_hint()
        self.set_action()



class App(PyQt5.QtWidgets.QWidget):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_gui()
    
    def show(self):
        self.showMaximized()
    
    def set_title(self,title):
        self.setWindowTitle(title)
    
    def set_gui(self):
        self.layout = PyQt5.QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.table = Table()
        self.panel = Panel()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.panel,1)
        self.setLayout(self.layout)
    
    def bind(self,hotkey,action):
        PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence(hotkey),self).activated.connect(action)



class Table(PyQt5.QtWidgets.QWidget):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_gui()
        self.fill()
    
    def set_gui(self):
        self.layout = PyQt5.QtWidgets.QGridLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        self.table = PyQt5.QtWidgets.QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(4)
        self.table.setShowGrid(False)
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        
    def fill(self):
        for row in range(4):
            for col in range(4):
                mes = 'row #{}, col #{}'.format(row,col)
                table_item = PyQt5.QtWidgets.QTableWidgetItem(mes)
                self.table.setItem(row,col,table_item)
        self.add_layout()
    
    def add_layout(self):
        self.layout.addWidget(self.table)



class Panel(PyQt5.QtWidgets.QWidget):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_values()
        self.set_gui()
    
    def set_values(self):
        self.icn_bl0 = '/home/pete/bin/mclientqt/resources/buttons/block_off.svgz'
        self.icn_bl1 = '/home/pete/bin/mclientqt/resources/buttons/block_on.svgz'
        self.icn_clr = '/home/pete/bin/mclientqt/resources/buttons/clear_search_field.svgz'
    
    def set_widgets(self):
        self.setMaximumHeight(44)
        self.panel = PyQt5.QtWidgets.QWidget(self)
        self.layout = PyQt5.QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(4,4,4,4)
        # A button to clear the search field
        self.btn_clr = Button (parent = self.panel
                              ,hint = 'Clear search field'
                              ,inactive = self.icn_clr
                              ,active = self.icn_clr
                              )
        # A button to toggle subject blocking
        self.btn_blk = Button (parent = self.panel
                              ,hint = 'Configure blacklisting'
                              ,inactive = self.icn_bl0
                              ,active = self.icn_bl1
                              )
        self.layout.addWidget(self.btn_clr.widget)
        self.layout.addWidget(self.btn_blk.widget)
        self.panel.setLayout(self.layout)
    
    def set_gui(self):
        self.set_widgets()

    @PyQt5.QtCore.pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')


if __name__ == '__main__':
    f = 'controller.__main__'
    exe = PyQt5.QtWidgets.QApplication(sys.argv)
    # Do not use directly App().show() - window will not be shown
    app = App()
    app.show()
    sys.exit(exe.exec_())
