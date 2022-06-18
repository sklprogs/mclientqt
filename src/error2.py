#!/usr/bin/python3

import PyQt5
import PyQt5.QtWidgets
import sys
from skl_shared_qt.localize import _


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    msg = PyQt5.QtWidgets.QMessageBox()
    msg.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
    msg.setWindowTitle('Error')
    msg.setText('[MClient] plugins.multitrancom.utils.subjects.extract.MiddlePage.get_first')
    mes = _('An unknown mode "{}"!\n\nThe following modes are supported: "{}".')
    mes = mes.format('hello','1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30.')
    msg.setInformativeText(mes)
    msg.exec_()
