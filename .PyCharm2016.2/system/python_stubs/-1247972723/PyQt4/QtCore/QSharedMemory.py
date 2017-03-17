# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QSharedMemory(QObject):
    """
    QSharedMemory(QObject parent=None)
    QSharedMemory(QString, QObject parent=None)
    """
    def attach(self, QSharedMemory_AccessMode_mode=None): # real signature unknown; restored from __doc__
        """ QSharedMemory.attach(QSharedMemory.AccessMode mode=QSharedMemory.ReadWrite) -> bool """
        return False

    def constData(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.constData() -> sip.voidptr """
        pass

    def create(self, p_int, QSharedMemory_AccessMode_mode=None): # real signature unknown; restored from __doc__
        """ QSharedMemory.create(int, QSharedMemory.AccessMode mode=QSharedMemory.ReadWrite) -> bool """
        return False

    def data(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.data() -> sip.voidptr """
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.detach() -> bool """
        return False

    def error(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.error() -> QSharedMemory.SharedMemoryError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.errorString() -> QString """
        return QString

    def isAttached(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.isAttached() -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.key() -> QString """
        return QString

    def lock(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.lock() -> bool """
        return False

    def nativeKey(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.nativeKey() -> QString """
        return QString

    def setKey(self, QString): # real signature unknown; restored from __doc__
        """ QSharedMemory.setKey(QString) """
        pass

    def setNativeKey(self, QString): # real signature unknown; restored from __doc__
        """ QSharedMemory.setNativeKey(QString) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.size() -> int """
        return 0

    def unlock(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.unlock() -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AlreadyExists = 4
    InvalidSize = 2
    KeyError = 3
    LockError = 6
    NoError = 0
    NotFound = 5
    OutOfResources = 7
    PermissionDenied = 1
    ReadOnly = 0
    ReadWrite = 1
    UnknownError = 8


