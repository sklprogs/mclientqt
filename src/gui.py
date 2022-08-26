#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import PyQt5
import PyQt5.QtWidgets

from skl_shared_qt.localize import _
import skl_shared_qt.shared as sh


class CustomDelegate(PyQt5.QtWidgets.QStyledItemDelegate):
    # akej74, https://stackoverflow.com/questions/35397943/how-to-make-a-fast-qtableview-with-html-formatted-and-clickable-cells
    def paint(self,painter,option,index):
        options = PyQt5.QtWidgets.QStyleOptionViewItem(option)
        self.initStyleOption(options,index)
    
        if options.widget:
            style = options.widget.style()
        else:
            style = PyQt5.QtWidgets.QApplication.style()
    
        doc = PyQt5.QtGui.QTextDocument()
        doc.setHtml(options.text)
        options.text = ''
    
        style.drawControl(PyQt5.QtWidgets.QStyle.CE_ItemViewItem,options,painter)
        ctx = PyQt5.QtGui.QAbstractTextDocumentLayout.PaintContext()
    
        textRect = style.subElementRect(PyQt5.QtWidgets.QStyle.SE_ItemViewItemText,options)
    
        painter.save()
    
        painter.translate(textRect.topLeft())
        painter.setClipRect(textRect.translated(-textRect.topLeft()))
        painter.translate(0,0.5*(options.rect.height() - doc.size().height()))
        doc.documentLayout().draw(painter,ctx)
    
        painter.restore()



class Table(PyQt5.QtWidgets.QTableWidget):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.trigger_hover = None
        self.set_gui()
    
    def fill_cell(self,cell,code):
        cell.setText(code)
    
    def create_cell(self,text):
        return PyQt5.QtWidgets.QTableWidgetItem(text)
    
    def set_cell_bg(self,cell,bg):
        # 'cell' is QTableWidgetItem
        cell.setBackground(PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(bg)))
    
    def get_cell_by_index(self,rowno,colno):
        return self.item(rowno,colno)
    
    def get_cell_by_cursor(self,cursor):
        return self.itemAt(cursor)
    
    def get_cursor(self,event):
        return event.pos()
    
    def enter_cell(self,action):
        self.cellEntered.connect(action)
    
    def set_col_width(self,no,width):
        self.setColumnWidth(no,width)
    
    def set_row_width(self,no,width):
        self.setRowWidth(no,width)
    
    def set_row_num(self,num):
        self.setRowCount(num)
    
    def set_col_num(self,num):
        self.setColumnCount(num)
    
    def show_grid(self,Show=True):
        self.setShowGrid(Show)
    
    def set_max_row_height(self,height):
        self.vheader.setMaximumSectionSize(height)
    
    def resize_fixed(self):
        # A temporary solution
        self.vheader.setSectionResizeMode(PyQt5.QtWidgets.QHeaderView.ResizeToContents)
    
    def hide_x_header(self):
        self.hheader.hide()
    
    def hide_y_header(self):
        self.vheader.hide()
    
    def set_gui(self):
        self.setItemDelegate(CustomDelegate())
        #self.hheader = self.horizontalHeader()
        self.vheader = self.verticalHeader()
        # This is required to activate mouse hovering
        self.setMouseTracking(True)
        #self.xscroll = PyQt5.QtWidgets.QScrollBar(self)
        #self.setHorizontalScrollBar(self.xscroll)
    
    def clear(self,event=None):
        self.clear()
    
    def set_cell(self,cell,rowno,colno):
        self.setItem(rowno,colno,cell)
    
    def add_layout(self):
        self.layout.addWidget(self,0,0)
        #self.layout.addWidget(self.xscroll)



class Cell:
    
    def __init__(self):
        self.widget = PyQt5.QtWidgets.QLabel()
    
    def set_text(self,text):
        self.widget.setText(text)
    
    def align_top(self,icell):
        #TODO: del
        icell.setTextAlignment(PyQt5.QtCore.Qt.AlignTop)



class App(PyQt5.QtWidgets.QMainWindow):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
    def minimize(self):
        self.showMinimized()
    
    def show(self):
        self.showMaximized()
    
    def set_title(self,title):
        self.setWindowTitle(title)
    
    def create_layout(self):
        self.parent = PyQt5.QtWidgets.QWidget()
        self.layout = PyQt5.QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
    
    def set_layout(self):
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.panel,1)
        self.parent.setLayout(self.layout)
    
    def set_gui(self,table=None,panel=None):
        self.create_layout()
        if table:
            self.table = table
        else:
            self.table = Table()
        if panel:
            self.panel = panel
        else:
            self.panel = Panel()
        self.set_layout()
        self.setCentralWidget(self.parent)
    
    def bind(self,hotkey,action):
        PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence(hotkey),self).activated.connect(action)



class Panel(PyQt5.QtWidgets.QWidget):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_values()
        self.set_gui()
    
    def set_values(self):
        self.delta = 0
        self.offset = 10
        self.pos = 0
        self.icn_al0 = sh.objs.get_pdir().add ('..','resources'
                                              ,'buttons'
                                              ,'alphabet_off.png'
                                              )
        self.icn_al1 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'alphabet_on.png'
                                        )
        self.icn_bl0 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'block_off.png'
                                        )
        self.icn_bl1 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'block_on.png'
                                        )
        self.icn_clr = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'clear_search_field.png'
                                        )
        self.icn_def = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'define.png'
                                        )
        self.icn_bk0 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'go_back_off.png'
                                        )
        self.icn_bk1 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'go_back.png'
                                        )
        self.icn_fw0 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'go_forward_off.png'
                                        )
        self.icn_fw1 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'go_forward.png'
                                        )
        self.icn_ret = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'go_search.png'
                                        )
        self.icn_brw = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'open_in_browser.png'
                                        )
        self.icn_ins = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'paste.png'
                                        )
        self.icn_prn = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'print.png'
                                        )
        self.icn_pr0 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'priority_off.png'
                                        )
        self.icn_pr1 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'priority_on.png'
                                        )
        self.icn_qit = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'quit_now.png'
                                        )
        self.icn_rld = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'reload.png'
                                        )
        self.icn_rp0 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'repeat_sign_off.png'
                                        )
        self.icn_rp1 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'repeat_sign.png'
                                        )
        self.icn_r20 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'repeat_sign2_off.png'
                                        )
        self.icn_r21 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'repeat_sign2.png'
                                        )
        self.icn_sav = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'save_article.png'
                                        )
        self.icn_src = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'search_article.png'
                                        )
        self.icn_set = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'settings.png'
                                        )
        self.icn_abt = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'show_about.png'
                                        )
        self.icn_sym = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'spec_symbol.png'
                                        )
        self.icn_hst = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'toggle_history.png'
                                        )
        self.icn_hor = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'toggle_view_hor.png'
                                        )
        self.icn_ver = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'toggle_view_ver.png'
                                        )
        self.icn_cp0 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'watch_clipboard_off.png'
                                        )
        self.icn_cp1 = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'watch_clipboard_on.png'
                                        )
        self.icn_swp = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'swap_langs.png'
                                        )
    
    def set_delta(self):
        ''' Set a delta value between a label size and a main widget
            size. This should be called only after the widget is drawn,
            otherwise, Qt will return bogus geometry of 640x480.
            #TODO (?): do not update each time on hovering, update only
            when the window size is changed.
        '''
        self.delta = self.width() - self.panel.width()
    
    def slide_left(self):
        if self.panel.x() - self.offset >= self.delta:
            self.pos -= self.offset
            self.panel.move(self.pos,0)
    
    def slide_right(self):
        if self.panel.x() + self.offset <= 0:
            self.pos += self.offset
            self.panel.move(self.pos,0)
    
    def trigger_hover(self,event):
        ''' We shouldn't use event.x since this returns x relative to
            the widget that caused the event, and this is widget will be
            any we have mouse over.
        '''
        self.set_delta()
        geom = self.geometry()
        x = PyQt5.QtGui.QCursor().pos().x() - geom.left()
        width = geom.width()
        if 0 <= x <= 30:
            self.slide_right()
        elif width - 30 <= x <= width:
            self.slide_left()
    
    def eventFilter(self,source,event):
        if event.type() == PyQt5.QtCore.QEvent.MouseMove:
            self.trigger_hover(event)
        return super().eventFilter(source,event)
    
    def set_hint_bg(self):
        self.setStyleSheet('QPushButton:hover {background-color: white} QToolTip {background-color: #ffffe0}')
    
    def set_widgets(self):
        self.setMaximumHeight(44)
        self.panel = PyQt5.QtWidgets.QWidget(self)
        self.layout = PyQt5.QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(4,4,4,4)
        self.ent_src = sh.Entry()
        self.ent_src.set_min_width(105)
        # A button for newbies, substitutes Enter in search_field
        self.btn_trn = sh.Button (hint = _('Translate')
                                 ,inactive = self.icn_ret
                                 ,active = self.icn_ret
                                 )
        # A button to clear the search field
        self.btn_clr = sh.Button (hint = _('Clear search field')
                                 ,inactive = self.icn_clr
                                 ,active = self.icn_clr
                                 )
        # A button to insert text into the search field
        self.btn_ins = sh.Button (hint = _('Paste text from clipboard')
                                 ,inactive = self.icn_ins
                                 ,active = self.icn_ins
                                 )
        # A button to insert a current search
        self.btn_rp1 = sh.Button (hint = _('Paste current request')
                                 ,inactive = self.icn_rp0
                                 ,active = self.icn_rp1
                                 )
        # A button to insert a previous search
        self.btn_rp2 = sh.Button (hint = _('Paste previous request')
                                 ,inactive = self.icn_r20
                                 ,active = self.icn_r21
                                 )
        # A button to insert special symbols
        self.btn_sym = sh.Button (hint = _('Paste a special symbol')
                                 ,inactive = self.icn_sym
                                 ,active = self.icn_sym
                                 )
        # Drop-down list with dictionary sources
        self.opt_src = sh.OptionMenu()
        # Drop-down lists with languages
        self.opt_lg1 = sh.OptionMenu()
        self.btn_swp = sh.Button (hint = _('Swap source and target languages')
                                 ,inactive = self.icn_swp
                                 ,active = self.icn_swp
                                 )
        self.opt_lg2 = sh.OptionMenu()
        self.opt_col = sh.OptionMenu()
        # A settings button
        self.btn_set = sh.Button (hint = _('Tune up view settings')
                                 ,inactive = self.icn_set
                                 ,active = self.icn_set
                                 )
        # A button to toggle subject blocking
        self.btn_blk = sh.Button (hint = _('Configure blacklisting')
                                 ,inactive = self.icn_bl0
                                 ,active = self.icn_bl1
                                 )
        # A button to toggle subject prioritization
        self.btn_pri = sh.Button (hint = _('Configure prioritization')
                                 ,inactive = self.icn_pr0
                                 ,active = self.icn_pr1
                                 )
        # A button to toggle subject alphabetization
        self.btn_alp = sh.Button (hint = _('Toggle alphabetizing')
                                 ,inactive = self.icn_al0
                                 ,active = self.icn_al1
                                 )
        # A button to change the article view
        self.btn_viw = sh.Button (hint = _('Toggle the article view mode')
                                 ,inactive = self.icn_ver
                                 ,active = self.icn_hor
                                 )
        # A button to move to the previous article
        self.btn_prv = sh.Button (hint = _('Go to the preceding article')
                                 ,inactive = self.icn_bk0
                                 ,active = self.icn_bk1
                                 )
        # A button to move to the next article
        self.btn_nxt = sh.Button (hint = _('Go to the following article')
                                 ,inactive = self.icn_fw0
                                 ,active = self.icn_fw1
                                 )
        # A button to toggle and clear history
        self.btn_hst = sh.Button (hint = _('Toggle history')
                                 ,inactive = self.icn_hst
                                 ,active = self.icn_hst
                                 )
        # A button to reload the article
        self.btn_rld = sh.Button (hint = _('Reload the article')
                                 ,inactive = self.icn_rld
                                 ,active = self.icn_rld
                                 )
        # A button to search within the article
        self.btn_ser = sh.Button (hint = _('Find in the current article')
                                 ,inactive = self.icn_src
                                 ,active = self.icn_src
                                 )
        # A button to save the article
        self.btn_sav = sh.Button (hint = _('Save the current article')
                                 ,inactive = self.icn_sav
                                 ,active = self.icn_sav
                                 )
        # A button to open the current article in a browser
        self.btn_brw = sh.Button (hint = _('Open the current article in a browser')
                                 ,inactive = self.icn_brw
                                 ,active = self.icn_brw
                                 )
        # A button to print the article
        self.btn_prn = sh.Button (hint = _('Create a print-ready preview')
                                 ,inactive = self.icn_prn
                                 ,active = self.icn_prn
                                 )
        # A button to define a term
        self.btn_def = sh.Button (hint = _('Define the current term')
                                 ,inactive = self.icn_def
                                 ,active = self.icn_def
                                 )
        # A button to toggle capturing Ctrl-c-c and Ctrl-Ins-Ins
        self.btn_cap = sh.Button (hint = _('Capture Ctrl-c-c and Ctrl-Ins-Ins')
                                 ,inactive = self.icn_cp0
                                 ,active = self.icn_cp1
                                 )
        # A button to show info about the program
        self.btn_abt = sh.Button (hint = _('View About')
                                 ,inactive = self.icn_abt
                                 ,active = self.icn_abt
                                 )
        # A button to quit the program
        self.btn_qit = sh.Button (hint = _('Quit the program')
                                 ,action = self.close
                                 ,inactive = self.icn_qit
                                 ,active = self.icn_qit
                                 )
        self.layout.addWidget(self.ent_src.widget)
        self.layout.addWidget(self.btn_trn.widget)
        self.layout.addWidget(self.btn_clr.widget)
        self.layout.addWidget(self.btn_ins.widget)
        self.layout.addWidget(self.btn_rp1.widget)
        self.layout.addWidget(self.btn_rp2.widget)
        self.layout.addWidget(self.btn_sym.widget)
        self.layout.addWidget(self.opt_src.widget)
        self.layout.addWidget(self.opt_lg1.widget)
        self.layout.addWidget(self.btn_swp.widget)
        self.layout.addWidget(self.opt_lg2.widget)
        self.layout.addWidget(self.opt_col.widget)
        self.layout.addWidget(self.btn_set.widget)
        self.layout.addWidget(self.btn_blk.widget)
        self.layout.addWidget(self.btn_pri.widget)
        self.layout.addWidget(self.btn_alp.widget)
        self.layout.addWidget(self.btn_viw.widget)
        self.layout.addWidget(self.btn_prv.widget)
        self.layout.addWidget(self.btn_nxt.widget)
        self.layout.addWidget(self.btn_hst.widget)
        self.layout.addWidget(self.btn_rld.widget)
        self.layout.addWidget(self.btn_ser.widget)
        self.layout.addWidget(self.btn_sav.widget)
        self.layout.addWidget(self.btn_brw.widget)
        self.layout.addWidget(self.btn_prn.widget)
        self.layout.addWidget(self.btn_def.widget)
        self.layout.addWidget(self.btn_cap.widget)
        self.layout.addWidget(self.btn_abt.widget)
        self.layout.addWidget(self.btn_qit.widget)
        self.panel.setLayout(self.layout)
    
    def set_gui(self):
        self.set_widgets()
        self.set_hint_bg()
        self.show()

    @PyQt5.QtCore.pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')



class Commands:
    
    def debug_memory(self,data):
        f = 'controller.Commands.debug_memory'
        if not data:
            sh.com.rep_empty(f)
            return
        #TYPE,TEXT,ROWNO,COLNO,CELLNO
        headers = (_('TYPE'),_('TEXT'),_('ROW #'),_('COLUMN #')
                  ,_('CELL #')
                  )
        mes = sh.FastTable (headers = headers
                           ,iterable = data
                           ,maxrows = 1000
                           ,maxrow = 40
                           ,Transpose = 1
                           ).run()
        sh.com.run_fast_debug(f,mes)



class Objects:
    
    def __init__(self):
        self.term_font = None
    
    def get_term_font(self):
        f = 'get_term_font'
        if self.term_font is None:
            self.term_font = PyQt5.QtGui.QFont()
            self.term_font.setFamily('Serif')
            self.term_font.setPixelSize(16)
        return self.term_font


com = Commands()
objs = Objects()


if __name__ == '__main__':
    import sys
    exe = PyQt5.QtWidgets.QApplication(sys.argv)
    app = App()
    app.set_gui()
    app.table.set_row_num(5)
    app.table.set_col_num(5)
    rowno = 0
    while rowno < 5:
        colno = 0
        while colno < 5:
            code = '<b>{}</b>:{}'.format(rowno+1,colno+1)
            cell = app.table.create_cell(code)
            app.table.set_cell(cell,rowno,colno)
            colno += 1
        rowno += 1
    app.show()
    sys.exit(exe.exec_())
