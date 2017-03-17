# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkInterface(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QNetworkInterface()
    QNetworkInterface(QNetworkInterface)
    """
    def addressEntries(self): # real signature unknown; restored from __doc__
        """ QNetworkInterface.addressEntries() -> list-of-QNetworkAddressEntry """
        pass

    def allAddresses(self): # real signature unknown; restored from __doc__
        """ QNetworkInterface.allAddresses() -> list-of-QHostAddress """
        pass

    def allInterfaces(self): # real signature unknown; restored from __doc__
        """ QNetworkInterface.allInterfaces() -> list-of-QNetworkInterface """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ QNetworkInterface.flags() -> QNetworkInterface.InterfaceFlags """
        pass

    def hardwareAddress(self): # real signature unknown; restored from __doc__
        """ QNetworkInterface.hardwareAddress() -> QString """
        pass

    def humanReadableName(self): # real signature unknown; restored from __doc__
        """ QNetworkInterface.humanReadableName() -> QString """
        pass

    def index(self): # real signature unknown; restored from __doc__
        """ QNetworkInterface.index() -> int """
        return 0

    def interfaceFromIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QNetworkInterface.interfaceFromIndex(int) -> QNetworkInterface """
        return QNetworkInterface

    def interfaceFromName(self, QString): # real signature unknown; restored from __doc__
        """ QNetworkInterface.interfaceFromName(QString) -> QNetworkInterface """
        return QNetworkInterface

    def isValid(self): # real signature unknown; restored from __doc__
        """ QNetworkInterface.isValid() -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ QNetworkInterface.name() -> QString """
        pass

    def __init__(self, QNetworkInterface=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CanBroadcast = 4
    CanMulticast = 32
    IsLoopBack = 8
    IsPointToPoint = 16
    IsRunning = 2
    IsUp = 1


