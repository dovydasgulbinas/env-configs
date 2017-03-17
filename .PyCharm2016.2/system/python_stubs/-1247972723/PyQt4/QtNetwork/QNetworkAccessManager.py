# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkAccessManager(__PyQt4_QtCore.QObject):
    """ QNetworkAccessManager(QObject parent=None) """
    def activeConfiguration(self): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.activeConfiguration() -> QNetworkConfiguration """
        return QNetworkConfiguration

    def authenticationRequired(self, *args, **kwargs): # real signature unknown
        """ QNetworkAccessManager.authenticationRequired[QNetworkReply, QAuthenticator] [signal] """
        pass

    def cache(self): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.cache() -> QAbstractNetworkCache """
        return QAbstractNetworkCache

    def configuration(self): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.configuration() -> QNetworkConfiguration """
        return QNetworkConfiguration

    def cookieJar(self): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.cookieJar() -> QNetworkCookieJar """
        return QNetworkCookieJar

    def createRequest(self, QNetworkAccessManager_Operation, QNetworkRequest, QIODevice_device=None): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.createRequest(QNetworkAccessManager.Operation, QNetworkRequest, QIODevice device=None) -> QNetworkReply """
        return QNetworkReply

    def deleteResource(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.deleteResource(QNetworkRequest) -> QNetworkReply """
        return QNetworkReply

    def finished(self, *args, **kwargs): # real signature unknown
        """ QNetworkAccessManager.finished[QNetworkReply] [signal] """
        pass

    def get(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.get(QNetworkRequest) -> QNetworkReply """
        return QNetworkReply

    def head(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.head(QNetworkRequest) -> QNetworkReply """
        return QNetworkReply

    def networkAccessible(self): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.networkAccessible() -> QNetworkAccessManager.NetworkAccessibility """
        pass

    def networkAccessibleChanged(self, *args, **kwargs): # real signature unknown
        """ QNetworkAccessManager.networkAccessibleChanged[QNetworkAccessManager.NetworkAccessibility] [signal] """
        pass

    def post(self, QNetworkRequest, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QNetworkAccessManager.post(QNetworkRequest, QIODevice) -> QNetworkReply
        QNetworkAccessManager.post(QNetworkRequest, QByteArray) -> QNetworkReply
        QNetworkAccessManager.post(QNetworkRequest, QHttpMultiPart) -> QNetworkReply
        """
        return QNetworkReply

    def proxy(self): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.proxy() -> QNetworkProxy """
        return QNetworkProxy

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        """ QNetworkAccessManager.proxyAuthenticationRequired[QNetworkProxy, QAuthenticator] [signal] """
        pass

    def proxyFactory(self): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.proxyFactory() -> QNetworkProxyFactory """
        return QNetworkProxyFactory

    def put(self, QNetworkRequest, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QNetworkAccessManager.put(QNetworkRequest, QIODevice) -> QNetworkReply
        QNetworkAccessManager.put(QNetworkRequest, QByteArray) -> QNetworkReply
        QNetworkAccessManager.put(QNetworkRequest, QHttpMultiPart) -> QNetworkReply
        """
        return QNetworkReply

    def sendCustomRequest(self, QNetworkRequest, QByteArray, QIODevice_data=None): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.sendCustomRequest(QNetworkRequest, QByteArray, QIODevice data=None) -> QNetworkReply """
        return QNetworkReply

    def setCache(self, QAbstractNetworkCache): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.setCache(QAbstractNetworkCache) """
        pass

    def setConfiguration(self, QNetworkConfiguration): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.setConfiguration(QNetworkConfiguration) """
        pass

    def setCookieJar(self, QNetworkCookieJar): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.setCookieJar(QNetworkCookieJar) """
        pass

    def setNetworkAccessible(self, QNetworkAccessManager_NetworkAccessibility): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.setNetworkAccessible(QNetworkAccessManager.NetworkAccessibility) """
        pass

    def setProxy(self, QNetworkProxy): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.setProxy(QNetworkProxy) """
        pass

    def setProxyFactory(self, QNetworkProxyFactory): # real signature unknown; restored from __doc__
        """ QNetworkAccessManager.setProxyFactory(QNetworkProxyFactory) """
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        """ QNetworkAccessManager.sslErrors[QNetworkReply, list-of-QSslError] [signal] """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Accessible = 1
    CustomOperation = 6
    DeleteOperation = 5
    GetOperation = 2
    HeadOperation = 1
    NotAccessible = 0
    PostOperation = 4
    PutOperation = 3
    UnknownAccessibility = -1


