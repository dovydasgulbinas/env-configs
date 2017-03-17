# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QIODevice(QObject):
    """
    QIODevice()
    QIODevice(QObject)
    """
    def aboutToClose(self, *args, **kwargs): # real signature unknown
        """ QIODevice.aboutToClose [signal] """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ QIODevice.atEnd() -> bool """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ QIODevice.bytesAvailable() -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ QIODevice.bytesToWrite() -> int """
        return 0

    def bytesWritten(self, *args, **kwargs): # real signature unknown
        """ QIODevice.bytesWritten[int] [signal] """
        pass

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ QIODevice.canReadLine() -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ QIODevice.close() """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QIODevice.errorString() -> QString """
        return QString

    def getChar(self): # real signature unknown; restored from __doc__
        """ QIODevice.getChar() -> (bool, str) """
        pass

    def isOpen(self): # real signature unknown; restored from __doc__
        """ QIODevice.isOpen() -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ QIODevice.isReadable() -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ QIODevice.isSequential() -> bool """
        return False

    def isTextModeEnabled(self): # real signature unknown; restored from __doc__
        """ QIODevice.isTextModeEnabled() -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ QIODevice.isWritable() -> bool """
        return False

    def open(self, QIODevice_OpenMode): # real signature unknown; restored from __doc__
        """ QIODevice.open(QIODevice.OpenMode) -> bool """
        return False

    def openMode(self): # real signature unknown; restored from __doc__
        """ QIODevice.openMode() -> QIODevice.OpenMode """
        pass

    def peek(self, p_int): # real signature unknown; restored from __doc__
        """ QIODevice.peek(int) -> QByteArray """
        return QByteArray

    def pos(self): # real signature unknown; restored from __doc__
        """ QIODevice.pos() -> int """
        return 0

    def putChar(self, p_str): # real signature unknown; restored from __doc__
        """ QIODevice.putChar(str) -> bool """
        return False

    def read(self, p_int): # real signature unknown; restored from __doc__
        """ QIODevice.read(int) -> str """
        return ""

    def readAll(self): # real signature unknown; restored from __doc__
        """ QIODevice.readAll() -> QByteArray """
        return QByteArray

    def readChannelFinished(self, *args, **kwargs): # real signature unknown
        """ QIODevice.readChannelFinished [signal] """
        pass

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ QIODevice.readData(int) -> str """
        return ""

    def readLine(self, int_maxlen=0): # real signature unknown; restored from __doc__
        """ QIODevice.readLine(int maxlen=0) -> str """
        return ""

    def readLineData(self, p_int): # real signature unknown; restored from __doc__
        """ QIODevice.readLineData(int) -> str """
        return ""

    def readyRead(self, *args, **kwargs): # real signature unknown
        """ QIODevice.readyRead [signal] """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QIODevice.reset() -> bool """
        return False

    def seek(self, p_int): # real signature unknown; restored from __doc__
        """ QIODevice.seek(int) -> bool """
        return False

    def setErrorString(self, QString): # real signature unknown; restored from __doc__
        """ QIODevice.setErrorString(QString) """
        pass

    def setOpenMode(self, QIODevice_OpenMode): # real signature unknown; restored from __doc__
        """ QIODevice.setOpenMode(QIODevice.OpenMode) """
        pass

    def setTextModeEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QIODevice.setTextModeEnabled(bool) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QIODevice.size() -> int """
        return 0

    def ungetChar(self, p_str): # real signature unknown; restored from __doc__
        """ QIODevice.ungetChar(str) """
        pass

    def waitForBytesWritten(self, p_int): # real signature unknown; restored from __doc__
        """ QIODevice.waitForBytesWritten(int) -> bool """
        return False

    def waitForReadyRead(self, p_int): # real signature unknown; restored from __doc__
        """ QIODevice.waitForReadyRead(int) -> bool """
        return False

    def write(self, QByteArray): # real signature unknown; restored from __doc__
        """ QIODevice.write(QByteArray) -> int """
        return 0

    def writeData(self, p_str): # real signature unknown; restored from __doc__
        """ QIODevice.writeData(str) -> int """
        return 0

    def __init__(self, QObject=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Append = 4
    NotOpen = 0
    ReadOnly = 1
    ReadWrite = 3
    Text = 16
    Truncate = 8
    Unbuffered = 32
    WriteOnly = 2


