#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from skl_shared_qt.localize import _
#import skl_shared_qt.shared as sh

import config as cf
from . import gui as gi


class Attach:
    
    def __init__(self, x1, width, y1, height):
        self.px1 = self.px2 = self.py1 = self.py2 = 0
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
    
    def set_coords(self):
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
        self.py1 = self.y1
        self.py2 = self.py1 + gi.HEIGHT
        self.px1 = self.x2
        self.px2 = self.px1 + gi.WIDTH
    
    def run(self):
        self.set_coords()
        return(self.px1, self.px2, self.py1, self.py2)



class Popup:
    
    def __init__(self):
        self.Shown = False
        self.gui = gi.Popup()
        self.set_gui()
    
    def adjust_position(self, x1, x2, y1, y2):
        px1, px2, py1, py2 = Attach(x1, x2, y1, y2).run()
        self.gui.move(px1, py1)
    
    def toggle(self):
        if self.Shown:
            self.close()
        else:
            self.show()
    
    def fill(self, text):
        self.gui.fill(text)
    
    def set_title(self, title=_('Full cell text')):
        self.gui.set_title(title)
    
    def set_gui(self):
        self.set_bindings()
        self.set_title()
    
    def show(self):
        self.Shown = True
        self.gui.show()
    
    def close(self):
        self.Shown = False
        self.gui.close()
    
    def set_bindings(self):
        self.gui.bind(('Esc',), self.close)
        self.gui.bind(cf.objs.get_config().new['actions']['toggle_popup']['hotkeys'], self.toggle)
