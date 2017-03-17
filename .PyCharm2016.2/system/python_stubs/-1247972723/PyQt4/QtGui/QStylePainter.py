# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QPainter import QPainter

class QStylePainter(QPainter):
    """
    QStylePainter()
    QStylePainter(QWidget)
    QStylePainter(QPaintDevice, QWidget)
    """
    def begin(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStylePainter.begin(QWidget) -> bool
        QStylePainter.begin(QPaintDevice, QWidget) -> bool
        """
        return False

    def drawComplexControl(self, QStyle_ComplexControl, QStyleOptionComplex): # real signature unknown; restored from __doc__
        """ QStylePainter.drawComplexControl(QStyle.ComplexControl, QStyleOptionComplex) """
        pass

    def drawControl(self, QStyle_ControlElement, QStyleOption): # real signature unknown; restored from __doc__
        """ QStylePainter.drawControl(QStyle.ControlElement, QStyleOption) """
        pass

    def drawItemPixmap(self, QRect, p_int, QPixmap): # real signature unknown; restored from __doc__
        """ QStylePainter.drawItemPixmap(QRect, int, QPixmap) """
        pass

    def drawItemText(self, QRect, p_int, QPalette, bool, QString, QPalette_ColorRole_textRole=None): # real signature unknown; restored from __doc__
        """ QStylePainter.drawItemText(QRect, int, QPalette, bool, QString, QPalette.ColorRole textRole=QPalette.NoRole) """
        pass

    def drawPrimitive(self, QStyle_PrimitiveElement, QStyleOption): # real signature unknown; restored from __doc__
        """ QStylePainter.drawPrimitive(QStyle.PrimitiveElement, QStyleOption) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ QStylePainter.style() -> QStyle """
        return QStyle

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


