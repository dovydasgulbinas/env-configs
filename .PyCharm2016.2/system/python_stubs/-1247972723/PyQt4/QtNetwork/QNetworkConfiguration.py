# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkConfiguration(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QNetworkConfiguration()
    QNetworkConfiguration(QNetworkConfiguration)
    """
    def bearerName(self): # real signature unknown; restored from __doc__
        """ QNetworkConfiguration.bearerName() -> QString """
        pass

    def bearerType(self): # real signature unknown; restored from __doc__
        """ QNetworkConfiguration.bearerType() -> QNetworkConfiguration.BearerType """
        pass

    def bearerTypeName(self): # real signature unknown; restored from __doc__
        """ QNetworkConfiguration.bearerTypeName() -> QString """
        pass

    def children(self): # real signature unknown; restored from __doc__
        """ QNetworkConfiguration.children() -> list-of-QNetworkConfiguration """
        pass

    def identifier(self): # real signature unknown; restored from __doc__
        """ QNetworkConfiguration.identifier() -> QString """
        pass

    def isRoamingAvailable(self): # real signature unknown; restored from __doc__
        """ QNetworkConfiguration.isRoamingAvailable() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QNetworkConfiguration.isValid() -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ QNetworkConfiguration.name() -> QString """
        pass

    def purpose(self): # real signature unknown; restored from __doc__
        """ QNetworkConfiguration.purpose() -> QNetworkConfiguration.Purpose """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QNetworkConfiguration.state() -> QNetworkConfiguration.StateFlags """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QNetworkConfiguration.type() -> QNetworkConfiguration.Type """
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

    def __init__(self, QNetworkConfiguration=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    Active = 14
    Bearer2G = 3
    BearerBluetooth = 7
    BearerCDMA2000 = 4
    BearerEthernet = 1
    BearerHSPA = 6
    BearerUnknown = 0
    BearerWCDMA = 5
    BearerWiMAX = 8
    BearerWLAN = 2
    Defined = 2
    Discovered = 6
    InternetAccessPoint = 0
    Invalid = 3
    PrivatePurpose = 2
    PublicPurpose = 1
    ServiceNetwork = 1
    ServiceSpecificPurpose = 3
    Undefined = 1
    UnknownPurpose = 0
    UserChoice = 2


