# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QX11EmbedWidget(QWidget):
    """ QX11EmbedWidget(QWidget parent=None) """
    def containerClosed(self, *args, **kwargs): # real signature unknown
        """ QX11EmbedWidget.containerClosed [signal] """
        pass

    def containerWinId(self): # real signature unknown; restored from __doc__
        """ QX11EmbedWidget.containerWinId() -> int """
        return 0

    def embedded(self, *args, **kwargs): # real signature unknown
        """ QX11EmbedWidget.embedded [signal] """
        pass

    def embedInto(self, p_int): # real signature unknown; restored from __doc__
        """ QX11EmbedWidget.embedInto(int) """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """
        QX11EmbedWidget.error() -> QX11EmbedWidget.Error
        QX11EmbedWidget.error[QX11EmbedWidget.Error] [signal]
        """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QX11EmbedWidget.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QX11EmbedWidget.eventFilter(QObject, QEvent) -> bool """
        return False

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QX11EmbedWidget.resizeEvent(QResizeEvent) """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    Internal = 1
    InvalidWindowID = 2
    Unknown = 0


