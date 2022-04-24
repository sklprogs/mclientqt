#!/usr/bin/python3

import PyQt5
import PyQt5.QtWidgets
import sys

cell = 'Общая лексика'


class MyTableModel(PyQt5.QtCore.QAbstractTableModel):
    
    def __init__(self,datain,parent=None,*args):
        PyQt5.QtCore.QAbstractTableModel.__init__(self,parent,*args)
        self.datain = datain
        self.painter = PyQt5.QtGui.QPainter()
        self.painter.setBrush(PyQt5.QtCore.Qt.cyan)

    def rowCount(self,parent=None,*args,**kwargs):
        return 4

    def columnCount(self,parent=None,*args,**kwargs):
        return 4
    
    def data(self,index,role=PyQt5.QtCore.Qt.DisplayRole):
        value = self.datain[index.row()][index.column()]
        print('value:',value)
        if not index.isValid():
            print('Invalid index')
            return PyQt5.QtCore.QVariant()
        if role == PyQt5.QtCore.Qt.ForegroundRole:
            print('Return 2')
            #return PyQt5.QtGui.QFont('Serif',14)
            return PyQt5.QtGui.QBrush(self.painter)
        else:
            print('role:',type(role),role)
            try:
                print('Return 3')
                return PyQt5.QtCore.QVariant(self.datain)
            except Exception as e:
                print('Return 4')
                print(str(e))
                return PyQt5.QtCore.QVariant()



class Table(PyQt5.QtWidgets.QWidget):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
    def fill(self):
        table_item = PyQt5.QtWidgets.QTableWidgetItem(cell)
        self.table.setItem(0,0,table_item)
    
    def set_gui(self):
        self.table = PyQt5.QtWidgets.QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(4)
        self.set_bindings()
        self.hheader = self.table.horizontalHeader()
        self.hheader.setSectionResizeMode(PyQt5.QtWidgets.QHeaderView.ResizeToContents)
        self.model = MyTableModel(datain=cell,parent=self.table)
        self.view = PyQt5.QtWidgets.QTableView(self.table)
        self.view.setModel(self.model)
        self.layout = PyQt5.QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.view)
        self.setLayout(self.layout)
    
    def set_bindings(self):
        PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence('Ctrl+Q'),self).activated.connect(self.close)
        PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence('Esc'),self).activated.connect(self.close)


if __name__ == '__main__':
    f = 'controller.__main__'
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    itable = Table()
    itable.set_gui()
    itable.fill()
    itable.showMaximized()
    sys.exit(app.exec())
