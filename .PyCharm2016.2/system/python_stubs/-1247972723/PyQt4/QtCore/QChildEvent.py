# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QEvent import QEvent

class QChildEvent(QEvent):
    """
    QChildEvent(QEvent.Type, QObject)
    QChildEvent(QChildEvent)
    """
    def added(self): # real signature unknown; restored from __doc__
        """ QChildEvent.added() -> bool """
        return False

    def child(self): # real signature unknown; restored from __doc__
        """ QChildEvent.child() -> QObject """
        return QObject

    def polished(self): # real signature unknown; restored from __doc__
        """ QChildEvent.polished() -> bool """
        return False

    def removed(self): # real signature unknown; restored from __doc__
        """ QChildEvent.removed() -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


