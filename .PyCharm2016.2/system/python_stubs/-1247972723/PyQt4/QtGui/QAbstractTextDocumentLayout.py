# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QAbstractTextDocumentLayout(__PyQt4_QtCore.QObject):
    """ QAbstractTextDocumentLayout(QTextDocument) """
    def anchorAt(self, QPointF): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.anchorAt(QPointF) -> QString """
        pass

    def blockBoundingRect(self, QTextBlock): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.blockBoundingRect(QTextBlock) -> QRectF """
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.document() -> QTextDocument """
        return QTextDocument

    def documentChanged(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.documentChanged(int, int, int) """
        pass

    def documentSize(self): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.documentSize() -> QSizeF """
        pass

    def documentSizeChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractTextDocumentLayout.documentSizeChanged[QSizeF] [signal] """
        pass

    def draw(self, QPainter, QAbstractTextDocumentLayout_PaintContext): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.draw(QPainter, QAbstractTextDocumentLayout.PaintContext) """
        pass

    def drawInlineObject(self, QPainter, QRectF, QTextInlineObject, p_int, QTextFormat): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.drawInlineObject(QPainter, QRectF, QTextInlineObject, int, QTextFormat) """
        pass

    def format(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.format(int) -> QTextCharFormat """
        return QTextCharFormat

    def frameBoundingRect(self, QTextFrame): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.frameBoundingRect(QTextFrame) -> QRectF """
        pass

    def handlerForObject(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.handlerForObject(int) -> QTextObjectInterface """
        return QTextObjectInterface

    def hitTest(self, QPointF, Qt_HitTestAccuracy): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.hitTest(QPointF, Qt.HitTestAccuracy) -> int """
        return 0

    def pageCount(self): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.pageCount() -> int """
        return 0

    def pageCountChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractTextDocumentLayout.pageCountChanged[int] [signal] """
        pass

    def paintDevice(self): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.paintDevice() -> QPaintDevice """
        return QPaintDevice

    def positionInlineObject(self, QTextInlineObject, p_int, QTextFormat): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.positionInlineObject(QTextInlineObject, int, QTextFormat) """
        pass

    def registerHandler(self, p_int, QObject): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.registerHandler(int, QObject) """
        pass

    def resizeInlineObject(self, QTextInlineObject, p_int, QTextFormat): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.resizeInlineObject(QTextInlineObject, int, QTextFormat) """
        pass

    def setPaintDevice(self, QPaintDevice): # real signature unknown; restored from __doc__
        """ QAbstractTextDocumentLayout.setPaintDevice(QPaintDevice) """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """
        QAbstractTextDocumentLayout.update[QRectF] [signal]
        QAbstractTextDocumentLayout.update [signal]
        """
        pass

    def updateBlock(self, *args, **kwargs): # real signature unknown
        """ QAbstractTextDocumentLayout.updateBlock[QTextBlock] [signal] """
        pass

    def __init__(self, QTextDocument): # real signature unknown; restored from __doc__
        pass



