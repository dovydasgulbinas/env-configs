# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QRubberBand(QWidget):
    """ QRubberBand(QRubberBand.Shape, QWidget parent=None) """
    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QRubberBand.changeEvent(QEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QRubberBand.event(QEvent) -> bool """
        return False

    def initStyleOption(self, QStyleOptionRubberBand): # real signature unknown; restored from __doc__
        """ QRubberBand.initStyleOption(QStyleOptionRubberBand) """
        pass

    def move(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRubberBand.move(QPoint)
        QRubberBand.move(int, int)
        """
        pass

    def moveEvent(self, QMoveEvent): # real signature unknown; restored from __doc__
        """ QRubberBand.moveEvent(QMoveEvent) """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QRubberBand.paintEvent(QPaintEvent) """
        pass

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRubberBand.resize(int, int)
        QRubberBand.resize(QSize)
        """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QRubberBand.resizeEvent(QResizeEvent) """
        pass

    def setGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRubberBand.setGeometry(QRect)
        QRubberBand.setGeometry(int, int, int, int)
        """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QRubberBand.shape() -> QRubberBand.Shape """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QRubberBand.showEvent(QShowEvent) """
        pass

    def __init__(self, QRubberBand_Shape, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    Line = 0
    Rectangle = 1


