# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QSystemSemaphore(): # skipped bases: <type 'sip.simplewrapper'>
    """ QSystemSemaphore(QString, int initialValue=0, QSystemSemaphore.AccessMode mode=QSystemSemaphore.Open) """
    def acquire(self): # real signature unknown; restored from __doc__
        """ QSystemSemaphore.acquire() -> bool """
        return False

    def error(self): # real signature unknown; restored from __doc__
        """ QSystemSemaphore.error() -> QSystemSemaphore.SystemSemaphoreError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QSystemSemaphore.errorString() -> QString """
        return QString

    def key(self): # real signature unknown; restored from __doc__
        """ QSystemSemaphore.key() -> QString """
        return QString

    def release(self, int_n=1): # real signature unknown; restored from __doc__
        """ QSystemSemaphore.release(int n=1) -> bool """
        return False

    def setKey(self, QString, int_initialValue=0, QSystemSemaphore_AccessMode_mode=None): # real signature unknown; restored from __doc__
        """ QSystemSemaphore.setKey(QString, int initialValue=0, QSystemSemaphore.AccessMode mode=QSystemSemaphore.Open) """
        pass

    def __init__(self, QString, int_initialValue=0, QSystemSemaphore_AccessMode_mode=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AlreadyExists = 3
    Create = 1
    KeyError = 2
    NoError = 0
    NotFound = 4
    Open = 0
    OutOfResources = 5
    PermissionDenied = 1
    UnknownError = 6


