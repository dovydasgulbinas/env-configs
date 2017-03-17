# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QUndoStack(__PyQt4_QtCore.QObject):
    """ QUndoStack(QObject parent=None) """
    def beginMacro(self, QString): # real signature unknown; restored from __doc__
        """ QUndoStack.beginMacro(QString) """
        pass

    def canRedo(self): # real signature unknown; restored from __doc__
        """ QUndoStack.canRedo() -> bool """
        return False

    def canRedoChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoStack.canRedoChanged[bool] [signal] """
        pass

    def canUndo(self): # real signature unknown; restored from __doc__
        """ QUndoStack.canUndo() -> bool """
        return False

    def canUndoChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoStack.canUndoChanged[bool] [signal] """
        pass

    def cleanChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoStack.cleanChanged[bool] [signal] """
        pass

    def cleanIndex(self): # real signature unknown; restored from __doc__
        """ QUndoStack.cleanIndex() -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ QUndoStack.clear() """
        pass

    def command(self, p_int): # real signature unknown; restored from __doc__
        """ QUndoStack.command(int) -> QUndoCommand """
        return QUndoCommand

    def count(self): # real signature unknown; restored from __doc__
        """ QUndoStack.count() -> int """
        return 0

    def createRedoAction(self, QObject, QString_prefix=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QUndoStack.createRedoAction(QObject, QString prefix=QString()) -> QAction """
        pass

    def createUndoAction(self, QObject, QString_prefix=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QUndoStack.createUndoAction(QObject, QString prefix=QString()) -> QAction """
        pass

    def endMacro(self): # real signature unknown; restored from __doc__
        """ QUndoStack.endMacro() """
        pass

    def index(self): # real signature unknown; restored from __doc__
        """ QUndoStack.index() -> int """
        return 0

    def indexChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoStack.indexChanged[int] [signal] """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ QUndoStack.isActive() -> bool """
        return False

    def isClean(self): # real signature unknown; restored from __doc__
        """ QUndoStack.isClean() -> bool """
        return False

    def push(self, QUndoCommand): # real signature unknown; restored from __doc__
        """ QUndoStack.push(QUndoCommand) """
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ QUndoStack.redo() """
        pass

    def redoText(self): # real signature unknown; restored from __doc__
        """ QUndoStack.redoText() -> QString """
        pass

    def redoTextChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoStack.redoTextChanged[QString] [signal] """
        pass

    def setActive(self, bool_active=True): # real signature unknown; restored from __doc__
        """ QUndoStack.setActive(bool active=True) """
        pass

    def setClean(self): # real signature unknown; restored from __doc__
        """ QUndoStack.setClean() """
        pass

    def setIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QUndoStack.setIndex(int) """
        pass

    def setUndoLimit(self, p_int): # real signature unknown; restored from __doc__
        """ QUndoStack.setUndoLimit(int) """
        pass

    def text(self, p_int): # real signature unknown; restored from __doc__
        """ QUndoStack.text(int) -> QString """
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ QUndoStack.undo() """
        pass

    def undoLimit(self): # real signature unknown; restored from __doc__
        """ QUndoStack.undoLimit() -> int """
        return 0

    def undoText(self): # real signature unknown; restored from __doc__
        """ QUndoStack.undoText() -> QString """
        pass

    def undoTextChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoStack.undoTextChanged[QString] [signal] """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass


