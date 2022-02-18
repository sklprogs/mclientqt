#!/usr/bin/python3

from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
import PyQt5
import PyQt5.QtWidgets
from time import time
import sys

cell = 'Общая лексика'


class MyWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, *args):
        #QWidget.__init__(self, *args)
        PyQt5.QtWidgets.QMainWindow.__init__(self)

        center = PyQt5.QtWidgets.QWidget(self)
        self.setCentralWidget(center)
        self.layout = PyQt5.QtWidgets.QGridLayout()
        center.setLayout(self.layout)
        self.table = PyQt5.QtWidgets.QTableWidget(self)
        
        #tablemodel = MyTableModel(cell,self)
        tablemodel = MyTableModel(datain=cell,parent=self.table)
        tableview = QTableView(self)
        tableview.setModel(tablemodel)
        
        tableview.verticalHeader().setVisible(False)
        tableview.horizontalHeader().setVisible(False)
        
        #layout = QGridLayout(self)
        #layout.setSpacing(1)
        
        table_item = PyQt5.QtWidgets.QTableWidgetItem(cell)
        #self.setLayout(layout)
        self.table.setItem(0,0,table_item)



class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.datain = datain

    def rowCount(self, parent):
        return 1

    def columnCount(self, parent):
        return 1

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()
        if role == Qt.FontRole:
            return QFont('Serif',14)
        else:
            try:
                return QVariant(self.datain)
            except Exception as e:
                print(str(e))
                return QVariant()


if __name__ == '__main__':
    start_time = time()
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    w.setWindowTitle('<Article Title>')
    end_time = time()
    print('Завершено за %s с.' % (str(end_time - start_time)))
    sys.exit(app.exec_())
