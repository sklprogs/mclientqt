#https://stackoverflow.com/questions/43300034/qt-itemdelegate-displaytext-with-a-qtablewidget-how-can-i-access-the-table-in

# -*- coding: utf-8 -*-
from __future__ import print_function, division, unicode_literals, absolute_import
import PyQt5
from PyQt5.QtWidgets import (QWidget, QApplication, QTableWidget, 
                             QTableWidgetItem, QVBoxLayout, QStyledItemDelegate)
from PyQt5.QtWidgets import QStyle  
from PyQt5.QtGui import QFont
import numpy as np

class ItemDelegate(QStyledItemDelegate):
    """
    The following methods are subclassed to replace display and editor of the
    QTableWidget.
    """
    def __init__(self, parent):
        """
        Pass instance `parent` of parent class (TestTable)
        """
        super(ItemDelegate, self).__init__(parent)
        self.parent = parent # instance of the parent (not the base) class

    def initStyleOption(self, option, index):
        """
        Initialize `option` with the values using the `index` index. When the 
        item (0,1) is processed, it is styled especially. All other items are 
        passed to the original `initStyleOption()` which then calls `displayText()`.
        """
        if index.row() == 0 and index.column() == 1: # a[0]: always 1
            option.text = "1!" # QString object
            option.font.setBold(True) 
            option.displayAlignment = PyQt5.QtCore.Qt.AlignRight
            #option.backgroundBrush ...
        else:
            # continue with the original `initStyleOption()`
            super(ItemDelegate, self).initStyleOption(option, index)     

    def displayText(self, text, locale):
        """
        Display `text` in the selected with the selected number
        of digits

        text:   string / QVariant from QTableWidget to be rendered
        locale: locale for the text
        """ 
        data = text # .toString() # Python 2: need to convert to "normal" string
        return "{0:>{1}}".format(data, 4)


class TestTable(QWidget):
    """ Create widget for viewing / editing / entering data """
    def __init__(self, parent):
        super(TestTable, self).__init__(parent)

        self.bfont = QFont()
        self.bfont.setBold(True)

        self.tblCoeff = QTableWidget(self)
        self.tblCoeff.setItemDelegate(ItemDelegate(self))

        layVMain = QVBoxLayout()
        layVMain.addWidget(self.tblCoeff)
        self.setLayout(layVMain)

        self.ba = np.random.randn(3,4) # test data
        self._refresh_table()

    def _refresh_table(self):
        """ (Re-)Create the displayed table from self.ba """
        num_cols = 3
        num_rows = 4

        self.tblCoeff.setRowCount(num_rows)
        self.tblCoeff.setColumnCount(num_cols)

        for col in range(num_cols):
            for row in range(num_rows):
                # set table item from self.ba 
                item = self.tblCoeff.item(row, col)
                if item: # does item exist?
                    item.setText(str(self.ba[col][row]))
                else: # no, construct it:
                    self.tblCoeff.setItem(row,col,QTableWidgetItem(
                          str(self.ba[col][row])))

        self.tblCoeff.resizeColumnsToContents()
        self.tblCoeff.resizeRowsToContents()

#------------------------------------------------------------------------------

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainw = TestTable(None)

    app.setActiveWindow(mainw)
    mainw.show()

    sys.exit(app.exec_())
