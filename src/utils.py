#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#from skl_shared_qt.localize import _
import skl_shared_qt.shared as sh
import plugins.multitrancom.utils.subjects.compile as us
#import plugins.multitrancom.utils.subjects.check as us


if __name__ == '__main__':
    f = '[MClient] utils.__main__'
    sh.com.start()
    #us.Compile(1).run()
    #us.Check().run()
    us.Missing(1).run()
    sh.com.end()
                
