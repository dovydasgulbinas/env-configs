# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkCookie(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QNetworkCookie(QByteArray name=QByteArray(), QByteArray value=QByteArray())
    QNetworkCookie(QNetworkCookie)
    """
    def domain(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.domain() -> QString """
        pass

    def expirationDate(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.expirationDate() -> QDateTime """
        pass

    def isHttpOnly(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.isHttpOnly() -> bool """
        return False

    def isSecure(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.isSecure() -> bool """
        return False

    def isSessionCookie(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.isSessionCookie() -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.name() -> QByteArray """
        pass

    def parseCookies(self, QByteArray): # real signature unknown; restored from __doc__
        """ QNetworkCookie.parseCookies(QByteArray) -> list-of-QNetworkCookie """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.path() -> QString """
        pass

    def setDomain(self, QString): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setDomain(QString) """
        pass

    def setExpirationDate(self, QDateTime): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setExpirationDate(QDateTime) """
        pass

    def setHttpOnly(self, bool): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setHttpOnly(bool) """
        pass

    def setName(self, QByteArray): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setName(QByteArray) """
        pass

    def setPath(self, QString): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setPath(QString) """
        pass

    def setSecure(self, bool): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setSecure(bool) """
        pass

    def setValue(self, QByteArray): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setValue(QByteArray) """
        pass

    def toRawForm(self, QNetworkCookie_RawForm_form=None): # real signature unknown; restored from __doc__
        """ QNetworkCookie.toRawForm(QNetworkCookie.RawForm form=QNetworkCookie.Full) -> QByteArray """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.value() -> QByteArray """
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


    Full = 1
    NameAndValueOnly = 0


