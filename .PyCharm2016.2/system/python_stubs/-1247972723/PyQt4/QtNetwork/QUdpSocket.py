# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractSocket import QAbstractSocket

class QUdpSocket(QAbstractSocket):
    """ QUdpSocket(QObject parent=None) """
    def bind(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QUdpSocket.bind(QHostAddress, int) -> bool
        QUdpSocket.bind(int port=0) -> bool
        QUdpSocket.bind(QHostAddress, int, QUdpSocket.BindMode) -> bool
        QUdpSocket.bind(int, QUdpSocket.BindMode) -> bool
        """
        return False

    def hasPendingDatagrams(self): # real signature unknown; restored from __doc__
        """ QUdpSocket.hasPendingDatagrams() -> bool """
        return False

    def joinMulticastGroup(self, QHostAddress, QNetworkInterface=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QUdpSocket.joinMulticastGroup(QHostAddress) -> bool
        QUdpSocket.joinMulticastGroup(QHostAddress, QNetworkInterface) -> bool
        """
        return False

    def leaveMulticastGroup(self, QHostAddress, QNetworkInterface=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QUdpSocket.leaveMulticastGroup(QHostAddress) -> bool
        QUdpSocket.leaveMulticastGroup(QHostAddress, QNetworkInterface) -> bool
        """
        return False

    def multicastInterface(self): # real signature unknown; restored from __doc__
        """ QUdpSocket.multicastInterface() -> QNetworkInterface """
        return QNetworkInterface

    def pendingDatagramSize(self): # real signature unknown; restored from __doc__
        """ QUdpSocket.pendingDatagramSize() -> int """
        return 0

    def readDatagram(self, p_int): # real signature unknown; restored from __doc__
        """ QUdpSocket.readDatagram(int) -> (str, QHostAddress, int) """
        pass

    def setMulticastInterface(self, QNetworkInterface): # real signature unknown; restored from __doc__
        """ QUdpSocket.setMulticastInterface(QNetworkInterface) """
        pass

    def writeDatagram(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QUdpSocket.writeDatagram(str, QHostAddress, int) -> int
        QUdpSocket.writeDatagram(QByteArray, QHostAddress, int) -> int
        """
        return 0

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    DefaultForPlatform = 0
    DontShareAddress = 2
    ReuseAddressHint = 4
    ShareAddress = 1


