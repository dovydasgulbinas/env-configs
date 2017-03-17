# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QHostInfo(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QHostInfo(int id=-1)
    QHostInfo(QHostInfo)
    """
    def abortHostLookup(self, p_int): # real signature unknown; restored from __doc__
        """ QHostInfo.abortHostLookup(int) """
        pass

    def addresses(self): # real signature unknown; restored from __doc__
        """ QHostInfo.addresses() -> list-of-QHostAddress """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QHostInfo.error() -> QHostInfo.HostInfoError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QHostInfo.errorString() -> QString """
        pass

    def fromName(self, QString): # real signature unknown; restored from __doc__
        """ QHostInfo.fromName(QString) -> QHostInfo """
        return QHostInfo

    def hostName(self): # real signature unknown; restored from __doc__
        """ QHostInfo.hostName() -> QString """
        pass

    def localDomainName(self): # real signature unknown; restored from __doc__
        """ QHostInfo.localDomainName() -> QString """
        pass

    def localHostName(self): # real signature unknown; restored from __doc__
        """ QHostInfo.localHostName() -> QString """
        pass

    def lookupHost(self, QString, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHostInfo.lookupHost(QString, QObject, SLOT()) -> int
        QHostInfo.lookupHost(QString, callable) -> int
        """
        return 0

    def lookupId(self): # real signature unknown; restored from __doc__
        """ QHostInfo.lookupId() -> int """
        return 0

    def setAddresses(self, list_of_QHostAddress): # real signature unknown; restored from __doc__
        """ QHostInfo.setAddresses(list-of-QHostAddress) """
        pass

    def setError(self, QHostInfo_HostInfoError): # real signature unknown; restored from __doc__
        """ QHostInfo.setError(QHostInfo.HostInfoError) """
        pass

    def setErrorString(self, QString): # real signature unknown; restored from __doc__
        """ QHostInfo.setErrorString(QString) """
        pass

    def setHostName(self, QString): # real signature unknown; restored from __doc__
        """ QHostInfo.setHostName(QString) """
        pass

    def setLookupId(self, p_int): # real signature unknown; restored from __doc__
        """ QHostInfo.setLookupId(int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    HostNotFound = 1
    NoError = 0
    UnknownError = 2


