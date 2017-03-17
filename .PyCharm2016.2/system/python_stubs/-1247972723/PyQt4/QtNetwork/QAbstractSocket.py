# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QAbstractSocket(__PyQt4_QtCore.QIODevice):
    """ QAbstractSocket(QAbstractSocket.SocketType, QObject) """
    def abort(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.abort() """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.atEnd() -> bool """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.bytesAvailable() -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.bytesToWrite() -> int """
        return 0

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.canReadLine() -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.close() """
        pass

    def connected(self, *args, **kwargs): # real signature unknown
        """ QAbstractSocket.connected [signal] """
        pass

    def connectToHost(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAbstractSocket.connectToHost(QString, int, QIODevice.OpenMode mode=QIODevice.ReadWrite)
        QAbstractSocket.connectToHost(QHostAddress, int, QIODevice.OpenMode mode=QIODevice.ReadWrite)
        """
        pass

    def connectToHostImplementation(self, QString, p_int, QIODevice_OpenMode_mode=None): # real signature unknown; restored from __doc__
        """ QAbstractSocket.connectToHostImplementation(QString, int, QIODevice.OpenMode mode=QIODevice.ReadWrite) """
        pass

    def disconnected(self, *args, **kwargs): # real signature unknown
        """ QAbstractSocket.disconnected [signal] """
        pass

    def disconnectFromHost(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.disconnectFromHost() """
        pass

    def disconnectFromHostImplementation(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.disconnectFromHostImplementation() """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """
        QAbstractSocket.error() -> QAbstractSocket.SocketError
        QAbstractSocket.error[QAbstractSocket.SocketError] [signal]
        """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.flush() -> bool """
        return False

    def hostFound(self, *args, **kwargs): # real signature unknown
        """ QAbstractSocket.hostFound [signal] """
        pass

    def isSequential(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.isSequential() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.isValid() -> bool """
        return False

    def localAddress(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.localAddress() -> QHostAddress """
        return QHostAddress

    def localPort(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.localPort() -> int """
        return 0

    def peerAddress(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.peerAddress() -> QHostAddress """
        return QHostAddress

    def peerName(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.peerName() -> QString """
        pass

    def peerPort(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.peerPort() -> int """
        return 0

    def proxy(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.proxy() -> QNetworkProxy """
        return QNetworkProxy

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        """ QAbstractSocket.proxyAuthenticationRequired[QNetworkProxy, QAuthenticator] [signal] """
        pass

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.readBufferSize() -> int """
        return 0

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractSocket.readData(int) -> str """
        return ""

    def readLineData(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractSocket.readLineData(int) -> str """
        return ""

    def setLocalAddress(self, QHostAddress): # real signature unknown; restored from __doc__
        """ QAbstractSocket.setLocalAddress(QHostAddress) """
        pass

    def setLocalPort(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractSocket.setLocalPort(int) """
        pass

    def setPeerAddress(self, QHostAddress): # real signature unknown; restored from __doc__
        """ QAbstractSocket.setPeerAddress(QHostAddress) """
        pass

    def setPeerName(self, QString): # real signature unknown; restored from __doc__
        """ QAbstractSocket.setPeerName(QString) """
        pass

    def setPeerPort(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractSocket.setPeerPort(int) """
        pass

    def setProxy(self, QNetworkProxy): # real signature unknown; restored from __doc__
        """ QAbstractSocket.setProxy(QNetworkProxy) """
        pass

    def setReadBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractSocket.setReadBufferSize(int) """
        pass

    def setSocketDescriptor(self, p_int, QAbstractSocket_SocketState_state=None, QIODevice_OpenMode_mode=None): # real signature unknown; restored from __doc__
        """ QAbstractSocket.setSocketDescriptor(int, QAbstractSocket.SocketState state=QAbstractSocket.ConnectedState, QIODevice.OpenMode mode=QIODevice.ReadWrite) -> bool """
        return False

    def setSocketError(self, QAbstractSocket_SocketError): # real signature unknown; restored from __doc__
        """ QAbstractSocket.setSocketError(QAbstractSocket.SocketError) """
        pass

    def setSocketOption(self, QAbstractSocket_SocketOption, QVariant): # real signature unknown; restored from __doc__
        """ QAbstractSocket.setSocketOption(QAbstractSocket.SocketOption, QVariant) """
        pass

    def setSocketState(self, QAbstractSocket_SocketState): # real signature unknown; restored from __doc__
        """ QAbstractSocket.setSocketState(QAbstractSocket.SocketState) """
        pass

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.socketDescriptor() -> int """
        return 0

    def socketOption(self, QAbstractSocket_SocketOption): # real signature unknown; restored from __doc__
        """ QAbstractSocket.socketOption(QAbstractSocket.SocketOption) -> QVariant """
        pass

    def socketType(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.socketType() -> QAbstractSocket.SocketType """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QAbstractSocket.state() -> QAbstractSocket.SocketState """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractSocket.stateChanged[QAbstractSocket.SocketState] [signal] """
        pass

    def waitForBytesWritten(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QAbstractSocket.waitForBytesWritten(int msecs=30000) -> bool """
        return False

    def waitForConnected(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QAbstractSocket.waitForConnected(int msecs=30000) -> bool """
        return False

    def waitForDisconnected(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QAbstractSocket.waitForDisconnected(int msecs=30000) -> bool """
        return False

    def waitForReadyRead(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QAbstractSocket.waitForReadyRead(int msecs=30000) -> bool """
        return False

    def writeData(self, p_str): # real signature unknown; restored from __doc__
        """ QAbstractSocket.writeData(str) -> int """
        return 0

    def __init__(self, QAbstractSocket_SocketType, QObject): # real signature unknown; restored from __doc__
        pass

    AddressInUseError = 8
    BoundState = 4
    ClosingState = 6
    ConnectedState = 3
    ConnectingState = 2
    ConnectionRefusedError = 0
    DatagramTooLargeError = 6
    HostLookupState = 1
    HostNotFoundError = 2
    IPv4Protocol = 0
    IPv6Protocol = 1
    KeepAliveOption = 1
    ListeningState = 5
    LowDelayOption = 0
    MulticastLoopbackOption = 3
    MulticastTtlOption = 2
    NetworkError = 7
    ProxyAuthenticationRequiredError = 12
    ProxyConnectionClosedError = 15
    ProxyConnectionRefusedError = 14
    ProxyConnectionTimeoutError = 16
    ProxyNotFoundError = 17
    ProxyProtocolError = 18
    RemoteHostClosedError = 1
    SocketAccessError = 3
    SocketAddressNotAvailableError = 9
    SocketResourceError = 4
    SocketTimeoutError = 5
    SslHandshakeFailedError = 13
    TcpSocket = 0
    UdpSocket = 1
    UnconnectedState = 0
    UnfinishedSocketOperationError = 11
    UnknownNetworkLayerProtocol = -1
    UnknownSocketError = -1
    UnknownSocketType = -1
    UnsupportedSocketOperationError = 10


