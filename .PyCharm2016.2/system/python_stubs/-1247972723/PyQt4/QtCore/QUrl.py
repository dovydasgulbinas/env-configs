# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QUrl(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QUrl()
    QUrl(QString)
    QUrl(QString, QUrl.ParsingMode)
    QUrl(QUrl)
    """
    def addEncodedQueryItem(self, QByteArray, QByteArray_1): # real signature unknown; restored from __doc__
        """ QUrl.addEncodedQueryItem(QByteArray, QByteArray) """
        pass

    def addQueryItem(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QUrl.addQueryItem(QString, QString) """
        pass

    def allEncodedQueryItemValues(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.allEncodedQueryItemValues(QByteArray) -> list-of-QByteArray """
        pass

    def allQueryItemValues(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.allQueryItemValues(QString) -> QStringList """
        return QStringList

    def authority(self): # real signature unknown; restored from __doc__
        """ QUrl.authority() -> QString """
        return QString

    def clear(self): # real signature unknown; restored from __doc__
        """ QUrl.clear() """
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """ QUrl.detach() """
        pass

    def encodedFragment(self): # real signature unknown; restored from __doc__
        """ QUrl.encodedFragment() -> QByteArray """
        return QByteArray

    def encodedHost(self): # real signature unknown; restored from __doc__
        """ QUrl.encodedHost() -> QByteArray """
        return QByteArray

    def encodedPassword(self): # real signature unknown; restored from __doc__
        """ QUrl.encodedPassword() -> QByteArray """
        return QByteArray

    def encodedPath(self): # real signature unknown; restored from __doc__
        """ QUrl.encodedPath() -> QByteArray """
        return QByteArray

    def encodedQuery(self): # real signature unknown; restored from __doc__
        """ QUrl.encodedQuery() -> QByteArray """
        return QByteArray

    def encodedQueryItems(self): # real signature unknown; restored from __doc__
        """ QUrl.encodedQueryItems() -> list-of-tuple-of-QByteArray-QByteArray """
        pass

    def encodedQueryItemValue(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.encodedQueryItemValue(QByteArray) -> QByteArray """
        return QByteArray

    def encodedUserName(self): # real signature unknown; restored from __doc__
        """ QUrl.encodedUserName() -> QByteArray """
        return QByteArray

    def errorString(self): # real signature unknown; restored from __doc__
        """ QUrl.errorString() -> QString """
        return QString

    def fragment(self): # real signature unknown; restored from __doc__
        """ QUrl.fragment() -> QString """
        return QString

    def fromAce(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.fromAce(QByteArray) -> QString """
        return QString

    def fromEncoded(self, QByteArray, QUrl_ParsingMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QUrl.fromEncoded(QByteArray) -> QUrl
        QUrl.fromEncoded(QByteArray, QUrl.ParsingMode) -> QUrl
        """
        return QUrl

    def fromLocalFile(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.fromLocalFile(QString) -> QUrl """
        return QUrl

    def fromPercentEncoding(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.fromPercentEncoding(QByteArray) -> QString """
        return QString

    def fromPunycode(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.fromPunycode(QByteArray) -> QString """
        return QString

    def fromUserInput(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.fromUserInput(QString) -> QUrl """
        return QUrl

    def hasEncodedQueryItem(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.hasEncodedQueryItem(QByteArray) -> bool """
        return False

    def hasFragment(self): # real signature unknown; restored from __doc__
        """ QUrl.hasFragment() -> bool """
        return False

    def hasQuery(self): # real signature unknown; restored from __doc__
        """ QUrl.hasQuery() -> bool """
        return False

    def hasQueryItem(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.hasQueryItem(QString) -> bool """
        return False

    def host(self): # real signature unknown; restored from __doc__
        """ QUrl.host() -> QString """
        return QString

    def idnWhitelist(self): # real signature unknown; restored from __doc__
        """ QUrl.idnWhitelist() -> QStringList """
        return QStringList

    def isDetached(self): # real signature unknown; restored from __doc__
        """ QUrl.isDetached() -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QUrl.isEmpty() -> bool """
        return False

    def isLocalFile(self): # real signature unknown; restored from __doc__
        """ QUrl.isLocalFile() -> bool """
        return False

    def isParentOf(self, QUrl): # real signature unknown; restored from __doc__
        """ QUrl.isParentOf(QUrl) -> bool """
        return False

    def isRelative(self): # real signature unknown; restored from __doc__
        """ QUrl.isRelative() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QUrl.isValid() -> bool """
        return False

    def password(self): # real signature unknown; restored from __doc__
        """ QUrl.password() -> QString """
        return QString

    def path(self): # real signature unknown; restored from __doc__
        """ QUrl.path() -> QString """
        return QString

    def port(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QUrl.port() -> int
        QUrl.port(int) -> int
        """
        return 0

    def queryItems(self): # real signature unknown; restored from __doc__
        """ QUrl.queryItems() -> list-of-tuple-of-QString-QString """
        pass

    def queryItemValue(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.queryItemValue(QString) -> QString """
        return QString

    def queryPairDelimiter(self): # real signature unknown; restored from __doc__
        """ QUrl.queryPairDelimiter() -> str """
        return ""

    def queryValueDelimiter(self): # real signature unknown; restored from __doc__
        """ QUrl.queryValueDelimiter() -> str """
        return ""

    def removeAllEncodedQueryItems(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.removeAllEncodedQueryItems(QByteArray) """
        pass

    def removeAllQueryItems(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.removeAllQueryItems(QString) """
        pass

    def removeEncodedQueryItem(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.removeEncodedQueryItem(QByteArray) """
        pass

    def removeQueryItem(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.removeQueryItem(QString) """
        pass

    def resolved(self, QUrl): # real signature unknown; restored from __doc__
        """ QUrl.resolved(QUrl) -> QUrl """
        return QUrl

    def scheme(self): # real signature unknown; restored from __doc__
        """ QUrl.scheme() -> QString """
        return QString

    def setAuthority(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.setAuthority(QString) """
        pass

    def setEncodedFragment(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.setEncodedFragment(QByteArray) """
        pass

    def setEncodedHost(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.setEncodedHost(QByteArray) """
        pass

    def setEncodedPassword(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.setEncodedPassword(QByteArray) """
        pass

    def setEncodedPath(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.setEncodedPath(QByteArray) """
        pass

    def setEncodedQuery(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.setEncodedQuery(QByteArray) """
        pass

    def setEncodedQueryItems(self, list_of_tuple_of_QByteArray_QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.setEncodedQueryItems(list-of-tuple-of-QByteArray-QByteArray) """
        pass

    def setEncodedUrl(self, QByteArray, QUrl_ParsingMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QUrl.setEncodedUrl(QByteArray)
        QUrl.setEncodedUrl(QByteArray, QUrl.ParsingMode)
        """
        pass

    def setEncodedUserName(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUrl.setEncodedUserName(QByteArray) """
        pass

    def setFragment(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.setFragment(QString) """
        pass

    def setHost(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.setHost(QString) """
        pass

    def setIdnWhitelist(self, QStringList): # real signature unknown; restored from __doc__
        """ QUrl.setIdnWhitelist(QStringList) """
        pass

    def setPassword(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.setPassword(QString) """
        pass

    def setPath(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.setPath(QString) """
        pass

    def setPort(self, p_int): # real signature unknown; restored from __doc__
        """ QUrl.setPort(int) """
        pass

    def setQueryDelimiters(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QUrl.setQueryDelimiters(str, str) """
        pass

    def setQueryItems(self, list_of_tuple_of_QString_QString): # real signature unknown; restored from __doc__
        """ QUrl.setQueryItems(list-of-tuple-of-QString-QString) """
        pass

    def setScheme(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.setScheme(QString) """
        pass

    def setUrl(self, QString, QUrl_ParsingMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QUrl.setUrl(QString)
        QUrl.setUrl(QString, QUrl.ParsingMode)
        """
        pass

    def setUserInfo(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.setUserInfo(QString) """
        pass

    def setUserName(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.setUserName(QString) """
        pass

    def swap(self, QUrl): # real signature unknown; restored from __doc__
        """ QUrl.swap(QUrl) """
        pass

    def toAce(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.toAce(QString) -> QByteArray """
        return QByteArray

    def toEncoded(self, QUrl_FormattingOptions_options=None): # real signature unknown; restored from __doc__
        """ QUrl.toEncoded(QUrl.FormattingOptions options=QUrl.None) -> QByteArray """
        return QByteArray

    def toLocalFile(self): # real signature unknown; restored from __doc__
        """ QUrl.toLocalFile() -> QString """
        return QString

    def toPercentEncoding(self, QString, QByteArray_exclude=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QUrl.toPercentEncoding(QString, QByteArray exclude=QByteArray(), QByteArray include=QByteArray()) -> QByteArray """
        pass

    def topLevelDomain(self): # real signature unknown; restored from __doc__
        """ QUrl.topLevelDomain() -> QString """
        return QString

    def toPunycode(self, QString): # real signature unknown; restored from __doc__
        """ QUrl.toPunycode(QString) -> QByteArray """
        return QByteArray

    def toString(self, QUrl_FormattingOptions_options=None): # real signature unknown; restored from __doc__
        """ QUrl.toString(QUrl.FormattingOptions options=QUrl.None) -> QString """
        return QString

    def userInfo(self): # real signature unknown; restored from __doc__
        """ QUrl.userInfo() -> QString """
        return QString

    def userName(self): # real signature unknown; restored from __doc__
        """ QUrl.userName() -> QString """
        return QString

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

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    None = 0
    RemoveAuthority = 30
    RemoveFragment = 128
    RemovePassword = 2
    RemovePath = 32
    RemovePort = 8
    RemoveQuery = 64
    RemoveScheme = 1
    RemoveUserInfo = 6
    StrictMode = 1
    StripTrailingSlash = 65536
    TolerantMode = 0


