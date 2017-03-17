# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QTcpServer(__PyQt4_QtCore.QObject):
    """ QTcpServer(QObject parent=None) """
    def addPendingConnection(self, QTcpSocket): # real signature unknown; restored from __doc__
        """ QTcpServer.addPendingConnection(QTcpSocket) """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ QTcpServer.close() """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QTcpServer.errorString() -> QString """
        pass

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ QTcpServer.hasPendingConnections() -> bool """
        return False

    def incomingConnection(self, p_int): # real signature unknown; restored from __doc__
        """ QTcpServer.incomingConnection(int) """
        pass

    def isListening(self): # real signature unknown; restored from __doc__
        """ QTcpServer.isListening() -> bool """
        return False

    def listen(self, QHostAddress_address=None, int_port=0): # real signature unknown; restored from __doc__
        """ QTcpServer.listen(QHostAddress address=QHostAddress.Any, int port=0) -> bool """
        return False

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ QTcpServer.maxPendingConnections() -> int """
        return 0

    def newConnection(self, *args, **kwargs): # real signature unknown
        """ QTcpServer.newConnection [signal] """
        pass

    def nextPendingConnection(self): # real signature unknown; restored from __doc__
        """ QTcpServer.nextPendingConnection() -> QTcpSocket """
        return QTcpSocket

    def proxy(self): # real signature unknown; restored from __doc__
        """ QTcpServer.proxy() -> QNetworkProxy """
        return QNetworkProxy

    def serverAddress(self): # real signature unknown; restored from __doc__
        """ QTcpServer.serverAddress() -> QHostAddress """
        return QHostAddress

    def serverError(self): # real signature unknown; restored from __doc__
        """ QTcpServer.serverError() -> QAbstractSocket.SocketError """
        pass

    def serverPort(self): # real signature unknown; restored from __doc__
        """ QTcpServer.serverPort() -> int """
        return 0

    def setMaxPendingConnections(self, p_int): # real signature unknown; restored from __doc__
        """ QTcpServer.setMaxPendingConnections(int) """
        pass

    def setProxy(self, QNetworkProxy): # real signature unknown; restored from __doc__
        """ QTcpServer.setProxy(QNetworkProxy) """
        pass

    def setSocketDescriptor(self, p_int): # real signature unknown; restored from __doc__
        """ QTcpServer.setSocketDescriptor(int) -> bool """
        return False

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ QTcpServer.socketDescriptor() -> int """
        return 0

    def waitForNewConnection(self, int_msecs=0): # real signature unknown; restored from __doc__
        """ QTcpServer.waitForNewConnection(int msecs=0) -> (bool, bool) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


