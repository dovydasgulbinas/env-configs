# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QUrlInfo(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QUrlInfo()
    QUrlInfo(QUrlInfo)
    QUrlInfo(QString, int, QString, QString, int, QDateTime, QDateTime, bool, bool, bool, bool, bool, bool)
    QUrlInfo(QUrl, int, QString, QString, int, QDateTime, QDateTime, bool, bool, bool, bool, bool, bool)
    """
    def equal(self, QUrlInfo, QUrlInfo_1, p_int): # real signature unknown; restored from __doc__
        """ QUrlInfo.equal(QUrlInfo, QUrlInfo, int) -> bool """
        return False

    def greaterThan(self, QUrlInfo, QUrlInfo_1, p_int): # real signature unknown; restored from __doc__
        """ QUrlInfo.greaterThan(QUrlInfo, QUrlInfo, int) -> bool """
        return False

    def group(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.group() -> QString """
        pass

    def isDir(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isDir() -> bool """
        return False

    def isExecutable(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isExecutable() -> bool """
        return False

    def isFile(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isFile() -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isReadable() -> bool """
        return False

    def isSymLink(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isSymLink() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isValid() -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isWritable() -> bool """
        return False

    def lastModified(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.lastModified() -> QDateTime """
        pass

    def lastRead(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.lastRead() -> QDateTime """
        pass

    def lessThan(self, QUrlInfo, QUrlInfo_1, p_int): # real signature unknown; restored from __doc__
        """ QUrlInfo.lessThan(QUrlInfo, QUrlInfo, int) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.name() -> QString """
        pass

    def owner(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.owner() -> QString """
        pass

    def permissions(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.permissions() -> int """
        return 0

    def setDir(self, bool): # real signature unknown; restored from __doc__
        """ QUrlInfo.setDir(bool) """
        pass

    def setFile(self, bool): # real signature unknown; restored from __doc__
        """ QUrlInfo.setFile(bool) """
        pass

    def setGroup(self, QString): # real signature unknown; restored from __doc__
        """ QUrlInfo.setGroup(QString) """
        pass

    def setLastModified(self, QDateTime): # real signature unknown; restored from __doc__
        """ QUrlInfo.setLastModified(QDateTime) """
        pass

    def setLastRead(self, QDateTime): # real signature unknown; restored from __doc__
        """ QUrlInfo.setLastRead(QDateTime) """
        pass

    def setName(self, QString): # real signature unknown; restored from __doc__
        """ QUrlInfo.setName(QString) """
        pass

    def setOwner(self, QString): # real signature unknown; restored from __doc__
        """ QUrlInfo.setOwner(QString) """
        pass

    def setPermissions(self, p_int): # real signature unknown; restored from __doc__
        """ QUrlInfo.setPermissions(int) """
        pass

    def setReadable(self, bool): # real signature unknown; restored from __doc__
        """ QUrlInfo.setReadable(bool) """
        pass

    def setSize(self, p_int): # real signature unknown; restored from __doc__
        """ QUrlInfo.setSize(int) """
        pass

    def setSymLink(self, bool): # real signature unknown; restored from __doc__
        """ QUrlInfo.setSymLink(bool) """
        pass

    def setWritable(self, bool): # real signature unknown; restored from __doc__
        """ QUrlInfo.setWritable(bool) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.size() -> int """
        return 0

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


    ExeGroup = 8
    ExeOther = 1
    ExeOwner = 64
    ReadGroup = 32
    ReadOther = 4
    ReadOwner = 256
    WriteGroup = 16
    WriteOther = 2
    WriteOwner = 128


