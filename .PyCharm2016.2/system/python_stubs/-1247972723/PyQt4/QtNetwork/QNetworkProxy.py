# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkProxy(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QNetworkProxy()
    QNetworkProxy(QNetworkProxy.ProxyType, QString hostName=QString(), int port=0, QString user=QString(), QString password=QString())
    QNetworkProxy(QNetworkProxy)
    """
    def applicationProxy(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.applicationProxy() -> QNetworkProxy """
        return QNetworkProxy

    def capabilities(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.capabilities() -> QNetworkProxy.Capabilities """
        pass

    def hostName(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.hostName() -> QString """
        pass

    def isCachingProxy(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.isCachingProxy() -> bool """
        return False

    def isTransparentProxy(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.isTransparentProxy() -> bool """
        return False

    def password(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.password() -> QString """
        pass

    def port(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.port() -> int """
        return 0

    def setApplicationProxy(self, QNetworkProxy): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setApplicationProxy(QNetworkProxy) """
        pass

    def setCapabilities(self, QNetworkProxy_Capabilities): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setCapabilities(QNetworkProxy.Capabilities) """
        pass

    def setHostName(self, QString): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setHostName(QString) """
        pass

    def setPassword(self, QString): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setPassword(QString) """
        pass

    def setPort(self, p_int): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setPort(int) """
        pass

    def setType(self, QNetworkProxy_ProxyType): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setType(QNetworkProxy.ProxyType) """
        pass

    def setUser(self, QString): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setUser(QString) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.type() -> QNetworkProxy.ProxyType """
        pass

    def user(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.user() -> QString """
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


    CachingCapability = 8
    DefaultProxy = 0
    FtpCachingProxy = 5
    HostNameLookupCapability = 16
    HttpCachingProxy = 4
    HttpProxy = 3
    ListeningCapability = 2
    NoProxy = 2
    Socks5Proxy = 1
    TunnelingCapability = 1
    UdpTunnelingCapability = 4


