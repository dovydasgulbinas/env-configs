# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QLocalSocket(__PyQt4_QtCore.QIODevice):
    """ QLocalSocket(QObject parent=None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.abort() """
        pass

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.bytesAvailable() -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.bytesToWrite() -> int """
        return 0

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.canReadLine() -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.close() """
        pass

    def connected(self, *args, **kwargs): # real signature unknown
        """ QLocalSocket.connected [signal] """
        pass

    def connectToServer(self, QString, QIODevice_OpenMode_mode=None): # real signature unknown; restored from __doc__
        """ QLocalSocket.connectToServer(QString, QIODevice.OpenMode mode=QIODevice.ReadWrite) """
        pass

    def disconnected(self, *args, **kwargs): # real signature unknown
        """ QLocalSocket.disconnected [signal] """
        pass

    def disconnectFromServer(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.disconnectFromServer() """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """
        QLocalSocket.error() -> QLocalSocket.LocalSocketError
        QLocalSocket.error[QLocalSocket.LocalSocketError] [signal]
        """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.flush() -> bool """
        return False

    def fullServerName(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.fullServerName() -> QString """
        pass

    def isSequential(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.isSequential() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.isValid() -> bool """
        return False

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.readBufferSize() -> int """
        return 0

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ QLocalSocket.readData(int) -> str """
        return ""

    def serverName(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.serverName() -> QString """
        pass

    def setReadBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QLocalSocket.setReadBufferSize(int) """
        pass

    def setSocketDescriptor(self, sip_voidptr, QLocalSocket_LocalSocketState_state=None, QIODevice_OpenMode_mode=None): # real signature unknown; restored from __doc__
        """ QLocalSocket.setSocketDescriptor(sip.voidptr, QLocalSocket.LocalSocketState state=QLocalSocket.ConnectedState, QIODevice.OpenMode mode=QIODevice.ReadWrite) -> bool """
        return False

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.socketDescriptor() -> sip.voidptr """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QLocalSocket.state() -> QLocalSocket.LocalSocketState """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QLocalSocket.stateChanged[QLocalSocket.LocalSocketState] [signal] """
        pass

    def waitForBytesWritten(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QLocalSocket.waitForBytesWritten(int msecs=30000) -> bool """
        return False

    def waitForConnected(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QLocalSocket.waitForConnected(int msecs=30000) -> bool """
        return False

    def waitForDisconnected(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QLocalSocket.waitForDisconnected(int msecs=30000) -> bool """
        return False

    def waitForReadyRead(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QLocalSocket.waitForReadyRead(int msecs=30000) -> bool """
        return False

    def writeData(self, p_str): # real signature unknown; restored from __doc__
        """ QLocalSocket.writeData(str) -> int """
        return 0

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    ClosingState = 6
    ConnectedState = 3
    ConnectingState = 2
    ConnectionError = 7
    ConnectionRefusedError = 0
    DatagramTooLargeError = 6
    PeerClosedError = 1
    ServerNotFoundError = 2
    SocketAccessError = 3
    SocketResourceError = 4
    SocketTimeoutError = 5
    UnconnectedState = 0
    UnknownSocketError = -1
    UnsupportedSocketOperationError = 10


