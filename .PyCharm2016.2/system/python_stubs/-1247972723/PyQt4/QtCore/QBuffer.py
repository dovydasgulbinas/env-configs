# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QIODevice import QIODevice

class QBuffer(QIODevice):
    """
    QBuffer(QObject parent=None)
    QBuffer(QByteArray, QObject parent=None)
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ QBuffer.atEnd() -> bool """
        return False

    def buffer(self): # real signature unknown; restored from __doc__
        """ QBuffer.buffer() -> QByteArray """
        return QByteArray

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ QBuffer.canReadLine() -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ QBuffer.close() """
        pass

    def connectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QBuffer.connectNotify(SIGNAL()) """
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ QBuffer.data() -> QByteArray """
        return QByteArray

    def disconnectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QBuffer.disconnectNotify(SIGNAL()) """
        pass

    def open(self, QIODevice_OpenMode): # real signature unknown; restored from __doc__
        """ QBuffer.open(QIODevice.OpenMode) -> bool """
        return False

    def pos(self): # real signature unknown; restored from __doc__
        """ QBuffer.pos() -> int """
        return 0

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ QBuffer.readData(int) -> str """
        return ""

    def seek(self, p_int): # real signature unknown; restored from __doc__
        """ QBuffer.seek(int) -> bool """
        return False

    def setBuffer(self, QByteArray): # real signature unknown; restored from __doc__
        """ QBuffer.setBuffer(QByteArray) """
        pass

    def setData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QBuffer.setData(QByteArray)
        QBuffer.setData(str)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QBuffer.size() -> int """
        return 0

    def writeData(self, p_str): # real signature unknown; restored from __doc__
        """ QBuffer.writeData(str) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


