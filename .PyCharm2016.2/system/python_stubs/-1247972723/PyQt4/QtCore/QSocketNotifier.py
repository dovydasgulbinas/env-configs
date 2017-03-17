# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QSocketNotifier(QObject):
    """ QSocketNotifier(int, QSocketNotifier.Type, QObject parent=None) """
    def activated(self, *args, **kwargs): # real signature unknown
        """ QSocketNotifier.activated[int] [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QSocketNotifier.event(QEvent) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ QSocketNotifier.isEnabled() -> bool """
        return False

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QSocketNotifier.setEnabled(bool) """
        pass

    def socket(self): # real signature unknown; restored from __doc__
        """ QSocketNotifier.socket() -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ QSocketNotifier.type() -> QSocketNotifier.Type """
        pass

    def __init__(self, p_int, QSocketNotifier_Type, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Exception = 2
    Read = 0
    Write = 1


