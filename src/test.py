#!/usr/bin/python3

import PyQt5
import PyQt5.QtWidgets
from time import time
import sys

cell = 'Общая лексика'


class MyWindow(PyQt5.QtWidgets.QMainWindow):
    
    def __init__(self, *args):
        #QWidget.__init__(self, *args)
        PyQt5.QtWidgets.QMainWindow.__init__(self)

        central = PyQt5.QtWidgets.QWidget(self)
        self.setCentralWidget(central)
        self.layout = PyQt5.QtWidgets.QGridLayout()
        central.setLayout(self.layout)
        self.table = PyQt5.QtWidgets.QTableWidget(self)
        
        #self.setFixedWidth(400)
        #self.setFixedHeight(300)
        
        self.center()
        self.table.setRowCount(4)
        self.table.setColumnCount(4)
        
        #tablemodel = MyTableModel(cell,self)
        #tablemodel = MyTableModel(datain=cell,parent=self.table)
        #tableview = PyQt5.QtWidgets.QTableView(self)
        #tableview.setModel(tablemodel)
        
        self.vheader = self.table.verticalHeader()
        self.hheader = self.table.horizontalHeader()
        #self.vheader.setVisible(False)
        #tableview.horizontalHeader().setVisible(False)
        
        #layout = QGridLayout(self)
        #layout.setSpacing(1)
        
        table_item = PyQt5.QtWidgets.QTableWidgetItem(cell)
        #self.setLayout(layout)
        self.table.setItem(0,0,table_item)
        
        #self.hheader.setSectionResizeMode(PyQt5.QtWidgets.QHeaderView.ResizeToContents)
        #self.hheader.setSectionResizeMode(PyQt5.QtWidgets.QHeaderView.Stretch)
        #self.vheader.setSectionResizeMode(PyQt5.QtWidgets.QHeaderView.Stretch)
        
        self.table.setColumnWidth(0,150)
    
    def center(self):
        geom = self.frameGeometry()
        coor = PyQt5.QtWidgets.QDesktopWidget().availableGeometry().center()
        geom.moveCenter(coor)
        self.move(geom.topLeft())



class MyTableModel(PyQt5.QtCore.QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        PyQt5.QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.datain = datain

    def rowCount(self, parent):
        return 1

    def columnCount(self, parent):
        return 1

    def data(self, index, role=PyQt5.QtCore.Qt.DisplayRole):
        if not index.isValid():
            return PyQt5.QtCore.QVariant()
        if role == PyQt5.QtCore.Qt.FontRole:
            return PyQt5.QtGui.QFont('Serif',14)
        else:
            try:
                return PyQt5.QtCore.QVariant(self.datain)
            except Exception as e:
                print(str(e))
                return PyQt5.QtCore.QVariant()


if __name__ == '__main__':
    start_time = time()
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    w.show()
    w.setWindowTitle('<Article Title>')
    end_time = time()
    print('Завершено за %s с.' % (str(end_time - start_time)))
    sys.exit(app.exec_())
