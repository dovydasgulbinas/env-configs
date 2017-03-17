# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QClipboard(__PyQt4_QtCore.QObject):
    # no doc
    def changed(self, *args, **kwargs): # real signature unknown
        """ QClipboard.changed[QClipboard.Mode] [signal] """
        pass

    def clear(self, QClipboard_Mode_mode=None): # real signature unknown; restored from __doc__
        """ QClipboard.clear(QClipboard.Mode mode=QClipboard.Clipboard) """
        pass

    def connectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QClipboard.connectNotify(SIGNAL()) """
        pass

    def dataChanged(self, *args, **kwargs): # real signature unknown
        """ QClipboard.dataChanged [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QClipboard.event(QEvent) -> bool """
        return False

    def findBufferChanged(self, *args, **kwargs): # real signature unknown
        """ QClipboard.findBufferChanged [signal] """
        pass

    def image(self, QClipboard_Mode_mode=None): # real signature unknown; restored from __doc__
        """ QClipboard.image(QClipboard.Mode mode=QClipboard.Clipboard) -> QImage """
        return QImage

    def mimeData(self, QClipboard_Mode_mode=None): # real signature unknown; restored from __doc__
        """ QClipboard.mimeData(QClipboard.Mode mode=QClipboard.Clipboard) -> QMimeData """
        pass

    def ownsClipboard(self): # real signature unknown; restored from __doc__
        """ QClipboard.ownsClipboard() -> bool """
        return False

    def ownsFindBuffer(self): # real signature unknown; restored from __doc__
        """ QClipboard.ownsFindBuffer() -> bool """
        return False

    def ownsSelection(self): # real signature unknown; restored from __doc__
        """ QClipboard.ownsSelection() -> bool """
        return False

    def pixmap(self, QClipboard_Mode_mode=None): # real signature unknown; restored from __doc__
        """ QClipboard.pixmap(QClipboard.Mode mode=QClipboard.Clipboard) -> QPixmap """
        return QPixmap

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ QClipboard.selectionChanged [signal] """
        pass

    def setImage(self, QImage, QClipboard_Mode_mode=None): # real signature unknown; restored from __doc__
        """ QClipboard.setImage(QImage, QClipboard.Mode mode=QClipboard.Clipboard) """
        pass

    def setMimeData(self, QMimeData, QClipboard_Mode_mode=None): # real signature unknown; restored from __doc__
        """ QClipboard.setMimeData(QMimeData, QClipboard.Mode mode=QClipboard.Clipboard) """
        pass

    def setPixmap(self, QPixmap, QClipboard_Mode_mode=None): # real signature unknown; restored from __doc__
        """ QClipboard.setPixmap(QPixmap, QClipboard.Mode mode=QClipboard.Clipboard) """
        pass

    def setText(self, QString, QClipboard_Mode_mode=None): # real signature unknown; restored from __doc__
        """ QClipboard.setText(QString, QClipboard.Mode mode=QClipboard.Clipboard) """
        pass

    def supportsFindBuffer(self): # real signature unknown; restored from __doc__
        """ QClipboard.supportsFindBuffer() -> bool """
        return False

    def supportsSelection(self): # real signature unknown; restored from __doc__
        """ QClipboard.supportsSelection() -> bool """
        return False

    def text(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QClipboard.text(QClipboard.Mode mode=QClipboard.Clipboard) -> QString
        QClipboard.text(QString, QClipboard.Mode mode=QClipboard.Clipboard) -> QString
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Clipboard = 0
    FindBuffer = 2
    Selection = 1


