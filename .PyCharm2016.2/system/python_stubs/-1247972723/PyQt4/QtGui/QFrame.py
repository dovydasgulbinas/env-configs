# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QFrame(QWidget):
    """ QFrame(QWidget parent=None, Qt.WindowFlags flags=0) """
    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QFrame.changeEvent(QEvent) """
        pass

    def drawFrame(self, QPainter): # real signature unknown; restored from __doc__
        """ QFrame.drawFrame(QPainter) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QFrame.event(QEvent) -> bool """
        return False

    def frameRect(self): # real signature unknown; restored from __doc__
        """ QFrame.frameRect() -> QRect """
        pass

    def frameShadow(self): # real signature unknown; restored from __doc__
        """ QFrame.frameShadow() -> QFrame.Shadow """
        pass

    def frameShape(self): # real signature unknown; restored from __doc__
        """ QFrame.frameShape() -> QFrame.Shape """
        pass

    def frameStyle(self): # real signature unknown; restored from __doc__
        """ QFrame.frameStyle() -> int """
        return 0

    def frameWidth(self): # real signature unknown; restored from __doc__
        """ QFrame.frameWidth() -> int """
        return 0

    def lineWidth(self): # real signature unknown; restored from __doc__
        """ QFrame.lineWidth() -> int """
        return 0

    def midLineWidth(self): # real signature unknown; restored from __doc__
        """ QFrame.midLineWidth() -> int """
        return 0

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QFrame.paintEvent(QPaintEvent) """
        pass

    def setFrameRect(self, QRect): # real signature unknown; restored from __doc__
        """ QFrame.setFrameRect(QRect) """
        pass

    def setFrameShadow(self, QFrame_Shadow): # real signature unknown; restored from __doc__
        """ QFrame.setFrameShadow(QFrame.Shadow) """
        pass

    def setFrameShape(self, QFrame_Shape): # real signature unknown; restored from __doc__
        """ QFrame.setFrameShape(QFrame.Shape) """
        pass

    def setFrameStyle(self, p_int): # real signature unknown; restored from __doc__
        """ QFrame.setFrameStyle(int) """
        pass

    def setLineWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QFrame.setLineWidth(int) """
        pass

    def setMidLineWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QFrame.setMidLineWidth(int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QFrame.sizeHint() -> QSize """
        pass

    def __init__(self, QWidget_parent=None, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass

    Box = 1
    HLine = 4
    NoFrame = 0
    Panel = 2
    Plain = 16
    Raised = 32
    Shadow_Mask = 240
    Shape_Mask = 15
    StyledPanel = 6
    Sunken = 48
    VLine = 5
    WinPanel = 3


