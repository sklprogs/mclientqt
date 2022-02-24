# https://stackoverflow.com/questions/35397943/how-to-make-a-fast-qtableview-with-html-formatted-and-clickable-cells
from PyQt5 import QtCore, QtWidgets, QtGui
    
class CustomTableView(QtWidgets.QTableView):

    link_activated = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(parent)

        self.setMouseTracking(True)
        self._mousePressAnchor = ''
        self._lastHoveredAnchor = ''

    def mousePressEvent(self, event):
        anchor = self.anchorAt(event.pos())
        self._mousePressAnchor = anchor

    def mouseMoveEvent(self, event):
        anchor = self.anchorAt(event.pos())
        if self._mousePressAnchor != anchor:
            self._mousePressAnchor = ''

        if self._lastHoveredAnchor != anchor:
            self._lastHoveredAnchor = anchor
            if self._lastHoveredAnchor:
                QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            else:
                QtWidgets.QApplication.restoreOverrideCursor()

    def mouseReleaseEvent(self, event):
        if self._mousePressAnchor:
            anchor = self.anchorAt(event.pos())
            if anchor == self._mousePressAnchor:
                self.link_activated.emit(anchor)
            self._mousePressAnchor = ''

    def anchorAt(self, pos):
        index = self.indexAt(pos)
        if index.isValid():
            delegate = self.itemDelegate(index)
            if delegate:
                itemRect = self.visualRect(index)
                relativeClickPosition = pos - itemRect.topLeft()
                html = self.model().data(index, QtCore.Qt.DisplayRole)
                return delegate.anchorAt(html, relativeClickPosition)
        return ''



class CustomDelegate(QtWidgets.QStyledItemDelegate):

    def anchorAt(self, html, point):
        doc = QtGui.QTextDocument()
        doc.setHtml(html)
        textLayout = doc.documentLayout()
        return textLayout.anchorAt(point)

    def paint(self, painter, option, index):
        options = QtWidgets.QStyleOptionViewItem(option)
        self.initStyleOption(options, index)

        if options.widget:
            style = options.widget.style()
        else:
            style = QtWidgets.QApplication.style()

        doc = QtGui.QTextDocument()
        doc.setHtml(options.text)
        options.text = ''

        style.drawControl(QtWidgets.QStyle.CE_ItemViewItem, options, painter)
        ctx = QtGui.QAbstractTextDocumentLayout.PaintContext()

        textRect = style.subElementRect(QtWidgets.QStyle.SE_ItemViewItemText, options)

        painter.save()

        painter.translate(textRect.topLeft())
        painter.setClipRect(textRect.translated(-textRect.topLeft()))
        painter.translate(0, 0.5*(options.rect.height() - doc.size().height()))
        doc.documentLayout().draw(painter, ctx)

        painter.restore()

    def sizeHint(self, option, index):
        options = QtWidgets.QStyleOptionViewItem(option)
        self.initStyleOption(options, index)

        doc = QtGui.QTextDocument()
        doc.setHtml(options.text)
        doc.setTextWidth(options.rect.width())

        return QtCore.QSize(doc.idealWidth(), doc.size().height())


if __name__ == '__main__':
    delegate = CustomDelegate()
