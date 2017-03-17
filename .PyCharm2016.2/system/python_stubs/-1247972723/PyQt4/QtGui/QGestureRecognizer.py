# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QGestureRecognizer(): # skipped bases: <type 'sip.wrapper'>
    """
    QGestureRecognizer()
    QGestureRecognizer(QGestureRecognizer)
    """
    def create(self, QObject): # real signature unknown; restored from __doc__
        """ QGestureRecognizer.create(QObject) -> QGesture """
        return QGesture

    def recognize(self, QGesture, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QGestureRecognizer.recognize(QGesture, QObject, QEvent) -> QGestureRecognizer.Result """
        pass

    def registerRecognizer(self, QGestureRecognizer): # real signature unknown; restored from __doc__
        """ QGestureRecognizer.registerRecognizer(QGestureRecognizer) -> Qt.GestureType """
        pass

    def reset(self, QGesture): # real signature unknown; restored from __doc__
        """ QGestureRecognizer.reset(QGesture) """
        pass

    def unregisterRecognizer(self, Qt_GestureType): # real signature unknown; restored from __doc__
        """ QGestureRecognizer.unregisterRecognizer(Qt.GestureType) """
        pass

    def __init__(self, QGestureRecognizer=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CancelGesture = 16
    ConsumeEventHint = 256
    FinishGesture = 8
    Ignore = 1
    MayBeGesture = 2
    TriggerGesture = 4


