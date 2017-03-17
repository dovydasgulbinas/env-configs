# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QInputMethodEvent(__PyQt4_QtCore.QEvent):
    """
    QInputMethodEvent()
    QInputMethodEvent(QString, list-of-QInputMethodEvent.Attribute)
    QInputMethodEvent(QInputMethodEvent)
    """
    def attributes(self): # real signature unknown; restored from __doc__
        """ QInputMethodEvent.attributes() -> list-of-QInputMethodEvent.Attribute """
        pass

    def commitString(self): # real signature unknown; restored from __doc__
        """ QInputMethodEvent.commitString() -> QString """
        pass

    def preeditString(self): # real signature unknown; restored from __doc__
        """ QInputMethodEvent.preeditString() -> QString """
        pass

    def replacementLength(self): # real signature unknown; restored from __doc__
        """ QInputMethodEvent.replacementLength() -> int """
        return 0

    def replacementStart(self): # real signature unknown; restored from __doc__
        """ QInputMethodEvent.replacementStart() -> int """
        return 0

    def setCommitString(self, QString, int_from=0, int_length=0): # real signature unknown; restored from __doc__
        """ QInputMethodEvent.setCommitString(QString, int from=0, int length=0) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Cursor = 1
    Language = 2
    Ruby = 3
    Selection = 4
    TextFormat = 0


