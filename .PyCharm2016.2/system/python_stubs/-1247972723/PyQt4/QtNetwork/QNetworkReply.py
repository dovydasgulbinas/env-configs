# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkReply(__PyQt4_QtCore.QIODevice):
    """ QNetworkReply(QObject parent=None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.abort() """
        pass

    def attribute(self, QNetworkRequest_Attribute): # real signature unknown; restored from __doc__
        """ QNetworkReply.attribute(QNetworkRequest.Attribute) -> QVariant """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.close() """
        pass

    def downloadProgress(self, *args, **kwargs): # real signature unknown
        """ QNetworkReply.downloadProgress[int, int] [signal] """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """
        QNetworkReply.error() -> QNetworkReply.NetworkError
        QNetworkReply.error[QNetworkReply.NetworkError] [signal]
        """
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        """ QNetworkReply.finished [signal] """
        pass

    def hasRawHeader(self, QByteArray): # real signature unknown; restored from __doc__
        """ QNetworkReply.hasRawHeader(QByteArray) -> bool """
        return False

    def header(self, QNetworkRequest_KnownHeaders): # real signature unknown; restored from __doc__
        """ QNetworkReply.header(QNetworkRequest.KnownHeaders) -> QVariant """
        pass

    def ignoreSslErrors(self, list_of_QSslError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QNetworkReply.ignoreSslErrors()
        QNetworkReply.ignoreSslErrors(list-of-QSslError)
        """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.isFinished() -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.isRunning() -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.isSequential() -> bool """
        return False

    def manager(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.manager() -> QNetworkAccessManager """
        return QNetworkAccessManager

    def metaDataChanged(self, *args, **kwargs): # real signature unknown
        """ QNetworkReply.metaDataChanged [signal] """
        pass

    def operation(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.operation() -> QNetworkAccessManager.Operation """
        pass

    def rawHeader(self, QByteArray): # real signature unknown; restored from __doc__
        """ QNetworkReply.rawHeader(QByteArray) -> QByteArray """
        pass

    def rawHeaderList(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.rawHeaderList() -> list-of-QByteArray """
        pass

    def rawHeaderPairs(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.rawHeaderPairs() -> list-of-tuple-of-QByteArray-QByteArray """
        pass

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.readBufferSize() -> int """
        return 0

    def request(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.request() -> QNetworkRequest """
        return QNetworkRequest

    def setAttribute(self, QNetworkRequest_Attribute, QVariant): # real signature unknown; restored from __doc__
        """ QNetworkReply.setAttribute(QNetworkRequest.Attribute, QVariant) """
        pass

    def setError(self, QNetworkReply_NetworkError, QString): # real signature unknown; restored from __doc__
        """ QNetworkReply.setError(QNetworkReply.NetworkError, QString) """
        pass

    def setFinished(self, bool): # real signature unknown; restored from __doc__
        """ QNetworkReply.setFinished(bool) """
        pass

    def setHeader(self, QNetworkRequest_KnownHeaders, QVariant): # real signature unknown; restored from __doc__
        """ QNetworkReply.setHeader(QNetworkRequest.KnownHeaders, QVariant) """
        pass

    def setOperation(self, QNetworkAccessManager_Operation): # real signature unknown; restored from __doc__
        """ QNetworkReply.setOperation(QNetworkAccessManager.Operation) """
        pass

    def setRawHeader(self, QByteArray, QByteArray_1): # real signature unknown; restored from __doc__
        """ QNetworkReply.setRawHeader(QByteArray, QByteArray) """
        pass

    def setReadBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QNetworkReply.setReadBufferSize(int) """
        pass

    def setRequest(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ QNetworkReply.setRequest(QNetworkRequest) """
        pass

    def setSslConfiguration(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ QNetworkReply.setSslConfiguration(QSslConfiguration) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QNetworkReply.setUrl(QUrl) """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.sslConfiguration() -> QSslConfiguration """
        return QSslConfiguration

    def sslErrors(self, *args, **kwargs): # real signature unknown
        """ QNetworkReply.sslErrors[list-of-QSslError] [signal] """
        pass

    def uploadProgress(self, *args, **kwargs): # real signature unknown
        """ QNetworkReply.uploadProgress[int, int] [signal] """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ QNetworkReply.url() -> QUrl """
        pass

    def writeData(self, p_str): # real signature unknown; restored from __doc__
        """ QNetworkReply.writeData(str) -> int """
        return 0

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    AuthenticationRequiredError = 204
    ConnectionRefusedError = 1
    ContentAccessDenied = 201
    ContentNotFoundError = 203
    ContentOperationNotPermittedError = 202
    ContentReSendError = 205
    HostNotFoundError = 3
    NoError = 0
    OperationCanceledError = 5
    ProtocolFailure = 399
    ProtocolInvalidOperationError = 302
    ProtocolUnknownError = 301
    ProxyAuthenticationRequiredError = 105
    ProxyConnectionClosedError = 102
    ProxyConnectionRefusedError = 101
    ProxyNotFoundError = 103
    ProxyTimeoutError = 104
    RemoteHostClosedError = 2
    SslHandshakeFailedError = 6
    TemporaryNetworkFailureError = 7
    TimeoutError = 4
    UnknownContentError = 299
    UnknownNetworkError = 99
    UnknownProxyError = 199


