# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QX11EmbedContainer(QWidget):
    """ QX11EmbedContainer(QWidget parent=None) """
    def clientClosed(self, *args, **kwargs): # real signature unknown
        """ QX11EmbedContainer.clientClosed [signal] """
        pass

    def clientIsEmbedded(self, *args, **kwargs): # real signature unknown
        """ QX11EmbedContainer.clientIsEmbedded [signal] """
        pass

    def clientWinId(self): # real signature unknown; restored from __doc__
        """ QX11EmbedContainer.clientWinId() -> int """
        return 0

    def discardClient(self): # real signature unknown; restored from __doc__
        """ QX11EmbedContainer.discardClient() """
        pass

    def embedClient(self, p_int): # real signature unknown; restored from __doc__
        """ QX11EmbedContainer.embedClient(int) """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """
        QX11EmbedContainer.error() -> QX11EmbedContainer.Error
        QX11EmbedContainer.error[QX11EmbedContainer.Error] [signal]
        """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QX11EmbedContainer.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QX11EmbedContainer.eventFilter(QObject, QEvent) -> bool """
        return False

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ QX11EmbedContainer.hideEvent(QHideEvent) """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QX11EmbedContainer.minimumSizeHint() -> QSize """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QX11EmbedContainer.paintEvent(QPaintEvent) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QX11EmbedContainer.resizeEvent(QResizeEvent) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QX11EmbedContainer.showEvent(QShowEvent) """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    Internal = 1
    InvalidWindowID = 2
    Unknown = 0


