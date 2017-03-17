# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkRequest(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QNetworkRequest(QUrl url=QUrl())
    QNetworkRequest(QNetworkRequest)
    """
    def attribute(self, QNetworkRequest_Attribute, QVariant_defaultValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QNetworkRequest.attribute(QNetworkRequest.Attribute, QVariant defaultValue=QVariant()) -> QVariant """
        pass

    def hasRawHeader(self, QByteArray): # real signature unknown; restored from __doc__
        """ QNetworkRequest.hasRawHeader(QByteArray) -> bool """
        return False

    def header(self, QNetworkRequest_KnownHeaders): # real signature unknown; restored from __doc__
        """ QNetworkRequest.header(QNetworkRequest.KnownHeaders) -> QVariant """
        pass

    def originatingObject(self): # real signature unknown; restored from __doc__
        """ QNetworkRequest.originatingObject() -> QObject """
        pass

    def priority(self): # real signature unknown; restored from __doc__
        """ QNetworkRequest.priority() -> QNetworkRequest.Priority """
        pass

    def rawHeader(self, QByteArray): # real signature unknown; restored from __doc__
        """ QNetworkRequest.rawHeader(QByteArray) -> QByteArray """
        pass

    def rawHeaderList(self): # real signature unknown; restored from __doc__
        """ QNetworkRequest.rawHeaderList() -> list-of-QByteArray """
        pass

    def setAttribute(self, QNetworkRequest_Attribute, QVariant): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setAttribute(QNetworkRequest.Attribute, QVariant) """
        pass

    def setHeader(self, QNetworkRequest_KnownHeaders, QVariant): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setHeader(QNetworkRequest.KnownHeaders, QVariant) """
        pass

    def setOriginatingObject(self, QObject): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setOriginatingObject(QObject) """
        pass

    def setPriority(self, QNetworkRequest_Priority): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setPriority(QNetworkRequest.Priority) """
        pass

    def setRawHeader(self, QByteArray, QByteArray_1): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setRawHeader(QByteArray, QByteArray) """
        pass

    def setSslConfiguration(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setSslConfiguration(QSslConfiguration) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setUrl(QUrl) """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ QNetworkRequest.sslConfiguration() -> QSslConfiguration """
        return QSslConfiguration

    def url(self): # real signature unknown; restored from __doc__
        """ QNetworkRequest.url() -> QUrl """
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


    AlwaysCache = 3
    AlwaysNetwork = 0
    AuthenticationReuseAttribute = 12
    Automatic = 0
    CacheLoadControlAttribute = 4
    CacheSaveControlAttribute = 5
    ConnectionEncryptedAttribute = 3
    ContentDispositionHeader = 6
    ContentLengthHeader = 1
    ContentTypeHeader = 0
    CookieHeader = 4
    CookieLoadControlAttribute = 11
    CookieSaveControlAttribute = 13
    CustomVerbAttribute = 10
    DoNotBufferUploadDataAttribute = 7
    HighPriority = 1
    HttpPipeliningAllowedAttribute = 8
    HttpPipeliningWasUsedAttribute = 9
    HttpReasonPhraseAttribute = 1
    HttpStatusCodeAttribute = 0
    LastModifiedHeader = 3
    LocationHeader = 2
    LowPriority = 5
    Manual = 1
    NormalPriority = 3
    PreferCache = 2
    PreferNetwork = 1
    RedirectionTargetAttribute = 2
    SetCookieHeader = 5
    SourceIsFromCacheAttribute = 6
    User = 1000
    UserMax = 32767


