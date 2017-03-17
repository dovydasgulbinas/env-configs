# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QHostAddress(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QHostAddress()
    QHostAddress(QHostAddress.SpecialAddress)
    QHostAddress(int)
    QHostAddress(QString)
    QHostAddress(16-tuple-of-int)
    QHostAddress(QHostAddress)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ QHostAddress.clear() """
        pass

    def isInSubnet(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHostAddress.isInSubnet(QHostAddress, int) -> bool
        QHostAddress.isInSubnet(tuple-of-QHostAddress-int) -> bool
        """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QHostAddress.isNull() -> bool """
        return False

    def parseSubnet(self, QString): # real signature unknown; restored from __doc__
        """ QHostAddress.parseSubnet(QString) -> tuple-of-QHostAddress-int """
        pass

    def protocol(self): # real signature unknown; restored from __doc__
        """ QHostAddress.protocol() -> QAbstractSocket.NetworkLayerProtocol """
        pass

    def scopeId(self): # real signature unknown; restored from __doc__
        """ QHostAddress.scopeId() -> QString """
        pass

    def setAddress(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHostAddress.setAddress(int)
        QHostAddress.setAddress(QString) -> bool
        QHostAddress.setAddress(16-tuple-of-int)
        """
        return False

    def setScopeId(self, QString): # real signature unknown; restored from __doc__
        """ QHostAddress.setScopeId(QString) """
        pass

    def toIPv4Address(self): # real signature unknown; restored from __doc__
        """ QHostAddress.toIPv4Address() -> int """
        return 0

    def toIPv6Address(self): # real signature unknown; restored from __doc__
        """ QHostAddress.toIPv6Address() -> 16-tuple-of-int """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ QHostAddress.toString() -> QString """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Any = 4
    AnyIPv6 = 5
    Broadcast = 1
    LocalHost = 2
    LocalHostIPv6 = 3
    Null = 0


