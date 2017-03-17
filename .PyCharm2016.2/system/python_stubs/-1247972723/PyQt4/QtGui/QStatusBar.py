# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QStatusBar(QWidget):
    """ QStatusBar(QWidget parent=None) """
    def addPermanentWidget(self, QWidget, int_stretch=0): # real signature unknown; restored from __doc__
        """ QStatusBar.addPermanentWidget(QWidget, int stretch=0) """
        pass

    def addWidget(self, QWidget, int_stretch=0): # real signature unknown; restored from __doc__
        """ QStatusBar.addWidget(QWidget, int stretch=0) """
        pass

    def clearMessage(self): # real signature unknown; restored from __doc__
        """ QStatusBar.clearMessage() """
        pass

    def currentMessage(self): # real signature unknown; restored from __doc__
        """ QStatusBar.currentMessage() -> QString """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QStatusBar.event(QEvent) -> bool """
        return False

    def hideOrShow(self): # real signature unknown; restored from __doc__
        """ QStatusBar.hideOrShow() """
        pass

    def insertPermanentWidget(self, p_int, QWidget, int_stretch=0): # real signature unknown; restored from __doc__
        """ QStatusBar.insertPermanentWidget(int, QWidget, int stretch=0) -> int """
        return 0

    def insertWidget(self, p_int, QWidget, int_stretch=0): # real signature unknown; restored from __doc__
        """ QStatusBar.insertWidget(int, QWidget, int stretch=0) -> int """
        return 0

    def isSizeGripEnabled(self): # real signature unknown; restored from __doc__
        """ QStatusBar.isSizeGripEnabled() -> bool """
        return False

    def messageChanged(self, *args, **kwargs): # real signature unknown
        """ QStatusBar.messageChanged[QString] [signal] """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QStatusBar.paintEvent(QPaintEvent) """
        pass

    def reformat(self): # real signature unknown; restored from __doc__
        """ QStatusBar.reformat() """
        pass

    def removeWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QStatusBar.removeWidget(QWidget) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QStatusBar.resizeEvent(QResizeEvent) """
        pass

    def setSizeGripEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QStatusBar.setSizeGripEnabled(bool) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QStatusBar.showEvent(QShowEvent) """
        pass

    def showMessage(self, QString, int_msecs=0): # real signature unknown; restored from __doc__
        """ QStatusBar.showMessage(QString, int msecs=0) """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


