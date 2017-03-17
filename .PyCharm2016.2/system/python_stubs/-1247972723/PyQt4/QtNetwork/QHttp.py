# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QHttp(__PyQt4_QtCore.QObject):
    """
    QHttp(QObject parent=None)
    QHttp(QString, int port=80, QObject parent=None)
    QHttp(QString, QHttp.ConnectionMode, int port=0, QObject parent=None)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ QHttp.abort() """
        pass

    def authenticationRequired(self, *args, **kwargs): # real signature unknown
        """ QHttp.authenticationRequired[QString, int, QAuthenticator] [signal] """
        pass

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ QHttp.bytesAvailable() -> int """
        return 0

    def clearPendingRequests(self): # real signature unknown; restored from __doc__
        """ QHttp.clearPendingRequests() """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ QHttp.close() -> int """
        return 0

    def currentDestinationDevice(self): # real signature unknown; restored from __doc__
        """ QHttp.currentDestinationDevice() -> QIODevice """
        pass

    def currentId(self): # real signature unknown; restored from __doc__
        """ QHttp.currentId() -> int """
        return 0

    def currentRequest(self): # real signature unknown; restored from __doc__
        """ QHttp.currentRequest() -> QHttpRequestHeader """
        return QHttpRequestHeader

    def currentSourceDevice(self): # real signature unknown; restored from __doc__
        """ QHttp.currentSourceDevice() -> QIODevice """
        pass

    def dataReadProgress(self, *args, **kwargs): # real signature unknown
        """ QHttp.dataReadProgress[int, int] [signal] """
        pass

    def dataSendProgress(self, *args, **kwargs): # real signature unknown
        """ QHttp.dataSendProgress[int, int] [signal] """
        pass

    def done(self, *args, **kwargs): # real signature unknown
        """ QHttp.done[bool] [signal] """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QHttp.error() -> QHttp.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QHttp.errorString() -> QString """
        pass

    def get(self, QString, QIODevice_to=None): # real signature unknown; restored from __doc__
        """ QHttp.get(QString, QIODevice to=None) -> int """
        return 0

    def hasPendingRequests(self): # real signature unknown; restored from __doc__
        """ QHttp.hasPendingRequests() -> bool """
        return False

    def head(self, QString): # real signature unknown; restored from __doc__
        """ QHttp.head(QString) -> int """
        return 0

    def ignoreSslErrors(self): # real signature unknown; restored from __doc__
        """ QHttp.ignoreSslErrors() """
        pass

    def lastResponse(self): # real signature unknown; restored from __doc__
        """ QHttp.lastResponse() -> QHttpResponseHeader """
        return QHttpResponseHeader

    def post(self, QString, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHttp.post(QString, QIODevice, QIODevice to=None) -> int
        QHttp.post(QString, QByteArray, QIODevice to=None) -> int
        """
        return 0

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        """ QHttp.proxyAuthenticationRequired[QNetworkProxy, QAuthenticator] [signal] """
        pass

    def read(self, p_int): # real signature unknown; restored from __doc__
        """ QHttp.read(int) -> str """
        return ""

    def readAll(self): # real signature unknown; restored from __doc__
        """ QHttp.readAll() -> QByteArray """
        pass

    def readyRead(self, *args, **kwargs): # real signature unknown
        """ QHttp.readyRead[QHttpResponseHeader] [signal] """
        pass

    def request(self, QHttpRequestHeader, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHttp.request(QHttpRequestHeader, QIODevice data=None, QIODevice to=None) -> int
        QHttp.request(QHttpRequestHeader, QByteArray, QIODevice to=None) -> int
        """
        return 0

    def requestFinished(self, *args, **kwargs): # real signature unknown
        """ QHttp.requestFinished[int, bool] [signal] """
        pass

    def requestStarted(self, *args, **kwargs): # real signature unknown
        """ QHttp.requestStarted[int] [signal] """
        pass

    def responseHeaderReceived(self, *args, **kwargs): # real signature unknown
        """ QHttp.responseHeaderReceived[QHttpResponseHeader] [signal] """
        pass

    def setHost(self, QString, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHttp.setHost(QString, int port=80) -> int
        QHttp.setHost(QString, QHttp.ConnectionMode, int port=0) -> int
        """
        return 0

    def setProxy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHttp.setProxy(QString, int, QString user=QString(), QString password=QString()) -> int
        QHttp.setProxy(QNetworkProxy) -> int
        """
        return 0

    def setSocket(self, QTcpSocket): # real signature unknown; restored from __doc__
        """ QHttp.setSocket(QTcpSocket) -> int """
        return 0

    def setUser(self, QString, QString_password=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QHttp.setUser(QString, QString password=QString()) -> int """
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        """ QHttp.sslErrors[list-of-QSslError] [signal] """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QHttp.state() -> QHttp.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QHttp.stateChanged[int] [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Aborted = 7
    AuthenticationRequiredError = 8
    Closing = 6
    Connected = 5
    Connecting = 2
    ConnectionModeHttp = 0
    ConnectionModeHttps = 1
    ConnectionRefused = 3
    HostLookup = 1
    HostNotFound = 2
    InvalidResponseHeader = 5
    NoError = 0
    ProxyAuthenticationRequiredError = 9
    Reading = 4
    Sending = 3
    Unconnected = 0
    UnexpectedClose = 4
    UnknownError = 1
    WrongContentLength = 6


