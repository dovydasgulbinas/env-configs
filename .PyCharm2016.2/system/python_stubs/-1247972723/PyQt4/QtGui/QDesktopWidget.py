# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QDesktopWidget(QWidget):
    """ QDesktopWidget() """
    def availableGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDesktopWidget.availableGeometry(int screen=-1) -> QRect
        QDesktopWidget.availableGeometry(QWidget) -> QRect
        QDesktopWidget.availableGeometry(QPoint) -> QRect
        """
        pass

    def isVirtualDesktop(self): # real signature unknown; restored from __doc__
        """ QDesktopWidget.isVirtualDesktop() -> bool """
        return False

    def numScreens(self): # real signature unknown; restored from __doc__
        """ QDesktopWidget.numScreens() -> int """
        return 0

    def primaryScreen(self): # real signature unknown; restored from __doc__
        """ QDesktopWidget.primaryScreen() -> int """
        return 0

    def resized(self, *args, **kwargs): # real signature unknown
        """ QDesktopWidget.resized[int] [signal] """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QDesktopWidget.resizeEvent(QResizeEvent) """
        pass

    def screen(self, int_screen=-1): # real signature unknown; restored from __doc__
        """ QDesktopWidget.screen(int screen=-1) -> QWidget """
        return QWidget

    def screenCount(self): # real signature unknown; restored from __doc__
        """ QDesktopWidget.screenCount() -> int """
        return 0

    def screenCountChanged(self, *args, **kwargs): # real signature unknown
        """ QDesktopWidget.screenCountChanged[int] [signal] """
        pass

    def screenGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDesktopWidget.screenGeometry(int screen=-1) -> QRect
        QDesktopWidget.screenGeometry(QWidget) -> QRect
        QDesktopWidget.screenGeometry(QPoint) -> QRect
        """
        pass

    def screenNumber(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDesktopWidget.screenNumber(QWidget widget=None) -> int
        QDesktopWidget.screenNumber(QPoint) -> int
        """
        return 0

    def workAreaResized(self, *args, **kwargs): # real signature unknown
        """ QDesktopWidget.workAreaResized[int] [signal] """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


