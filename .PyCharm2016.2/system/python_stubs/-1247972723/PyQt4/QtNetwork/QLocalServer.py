# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QLocalServer(__PyQt4_QtCore.QObject):
    """ QLocalServer(QObject parent=None) """
    def close(self): # real signature unknown; restored from __doc__
        """ QLocalServer.close() """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QLocalServer.errorString() -> QString """
        pass

    def fullServerName(self): # real signature unknown; restored from __doc__
        """ QLocalServer.fullServerName() -> QString """
        pass

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ QLocalServer.hasPendingConnections() -> bool """
        return False

    def incomingConnection(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ QLocalServer.incomingConnection(sip.voidptr) """
        pass

    def isListening(self): # real signature unknown; restored from __doc__
        """ QLocalServer.isListening() -> bool """
        return False

    def listen(self, QString): # real signature unknown; restored from __doc__
        """ QLocalServer.listen(QString) -> bool """
        return False

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ QLocalServer.maxPendingConnections() -> int """
        return 0

    def newConnection(self, *args, **kwargs): # real signature unknown
        """ QLocalServer.newConnection [signal] """
        pass

    def nextPendingConnection(self): # real signature unknown; restored from __doc__
        """ QLocalServer.nextPendingConnection() -> QLocalSocket """
        return QLocalSocket

    def removeServer(self, QString): # real signature unknown; restored from __doc__
        """ QLocalServer.removeServer(QString) -> bool """
        return False

    def serverError(self): # real signature unknown; restored from __doc__
        """ QLocalServer.serverError() -> QAbstractSocket.SocketError """
        pass

    def serverName(self): # real signature unknown; restored from __doc__
        """ QLocalServer.serverName() -> QString """
        pass

    def setMaxPendingConnections(self, p_int): # real signature unknown; restored from __doc__
        """ QLocalServer.setMaxPendingConnections(int) """
        pass

    def waitForNewConnection(self, int_msecs=0): # real signature unknown; restored from __doc__
        """ QLocalServer.waitForNewConnection(int msecs=0) -> (bool, bool) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


