#!/usr/bin/python3

import PyQt5
import PyQt5.QtWidgets
import sys


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    msg = PyQt5.QtWidgets.QMessageBox()
    msg.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
    msg.setText('Error')
    msg.setInformativeText('More information')
    msg.setWindowTitle('Error')
    msg.exec_()
