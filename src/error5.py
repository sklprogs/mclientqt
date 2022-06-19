#!/usr/bin/python3

import PyQt5
import PyQt5.QtWidgets
import sys
from skl_shared_qt.localize import _
import skl_shared_qt.shared as sh





if __name__ == '__main__':
    f = 'error5.__main__'
    sh.com.start()
    f2 = '[MClient] utils.subjects.extract.MiddlePage.get_first'
    mes = _('An unknown mode "{}"!\n\nThe following modes are supported: "{}".')
    mes = mes.format('hello','1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30.')
    sh.Message(f2,mes).show_question()
    sh.com.end()
