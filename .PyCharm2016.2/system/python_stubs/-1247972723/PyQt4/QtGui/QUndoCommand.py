# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QUndoCommand(): # skipped bases: <type 'sip.wrapper'>
    """
    QUndoCommand(QUndoCommand parent=None)
    QUndoCommand(QString, QUndoCommand parent=None)
    """
    def actionText(self): # real signature unknown; restored from __doc__
        """ QUndoCommand.actionText() -> QString """
        pass

    def child(self, p_int): # real signature unknown; restored from __doc__
        """ QUndoCommand.child(int) -> QUndoCommand """
        return QUndoCommand

    def childCount(self): # real signature unknown; restored from __doc__
        """ QUndoCommand.childCount() -> int """
        return 0

    def id(self): # real signature unknown; restored from __doc__
        """ QUndoCommand.id() -> int """
        return 0

    def mergeWith(self, QUndoCommand): # real signature unknown; restored from __doc__
        """ QUndoCommand.mergeWith(QUndoCommand) -> bool """
        return False

    def redo(self): # real signature unknown; restored from __doc__
        """ QUndoCommand.redo() """
        pass

    def setText(self, QString): # real signature unknown; restored from __doc__
        """ QUndoCommand.setText(QString) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QUndoCommand.text() -> QString """
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ QUndoCommand.undo() """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



