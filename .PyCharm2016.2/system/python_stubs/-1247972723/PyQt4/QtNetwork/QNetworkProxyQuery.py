# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkProxyQuery(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QNetworkProxyQuery()
    QNetworkProxyQuery(QUrl, QNetworkProxyQuery.QueryType type=QNetworkProxyQuery.UrlRequest)
    QNetworkProxyQuery(QString, int, QString protocolTag=QString(), QNetworkProxyQuery.QueryType type=QNetworkProxyQuery.TcpSocket)
    QNetworkProxyQuery(int, QString protocolTag=QString(), QNetworkProxyQuery.QueryType type=QNetworkProxyQuery.TcpServer)
    QNetworkProxyQuery(QNetworkConfiguration, QUrl, QNetworkProxyQuery.QueryType queryType=QNetworkProxyQuery.UrlRequest)
    QNetworkProxyQuery(QNetworkConfiguration, QString, int, QString protocolTag=QString(), QNetworkProxyQuery.QueryType type=QNetworkProxyQuery.TcpSocket)
    QNetworkProxyQuery(QNetworkConfiguration, int, QString protocolTag=QString(), QNetworkProxyQuery.QueryType type=QNetworkProxyQuery.TcpServer)
    QNetworkProxyQuery(QNetworkProxyQuery)
    """
    def localPort(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.localPort() -> int """
        return 0

    def networkConfiguration(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.networkConfiguration() -> QNetworkConfiguration """
        return QNetworkConfiguration

    def peerHostName(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.peerHostName() -> QString """
        pass

    def peerPort(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.peerPort() -> int """
        return 0

    def protocolTag(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.protocolTag() -> QString """
        pass

    def queryType(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.queryType() -> QNetworkProxyQuery.QueryType """
        pass

    def setLocalPort(self, p_int): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setLocalPort(int) """
        pass

    def setNetworkConfiguration(self, QNetworkConfiguration): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setNetworkConfiguration(QNetworkConfiguration) """
        pass

    def setPeerHostName(self, QString): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setPeerHostName(QString) """
        pass

    def setPeerPort(self, p_int): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setPeerPort(int) """
        pass

    def setProtocolTag(self, QString): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setProtocolTag(QString) """
        pass

    def setQueryType(self, QNetworkProxyQuery_QueryType): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setQueryType(QNetworkProxyQuery.QueryType) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setUrl(QUrl) """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.url() -> QUrl """
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


    TcpServer = 100
    TcpSocket = 0
    UdpSocket = 1
    UrlRequest = 101


