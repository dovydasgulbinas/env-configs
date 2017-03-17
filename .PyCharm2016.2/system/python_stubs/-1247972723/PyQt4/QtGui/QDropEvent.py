# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QMimeSource import QMimeSource

class QDropEvent(__PyQt4_QtCore.QEvent, QMimeSource):
    """
    QDropEvent(QPoint, Qt.DropActions, QMimeData, Qt.MouseButtons, Qt.KeyboardModifiers, QEvent.Type type=QEvent.Drop)
    QDropEvent(QDropEvent)
    """
    def acceptProposedAction(self): # real signature unknown; restored from __doc__
        """ QDropEvent.acceptProposedAction() """
        pass

    def dropAction(self): # real signature unknown; restored from __doc__
        """ QDropEvent.dropAction() -> Qt.DropAction """
        pass

    def encodedData(self, p_str): # real signature unknown; restored from __doc__
        """ QDropEvent.encodedData(str) -> QByteArray """
        pass

    def format(self, int_n=0): # real signature unknown; restored from __doc__
        """ QDropEvent.format(int n=0) -> str """
        return ""

    def keyboardModifiers(self): # real signature unknown; restored from __doc__
        """ QDropEvent.keyboardModifiers() -> Qt.KeyboardModifiers """
        pass

    def mimeData(self): # real signature unknown; restored from __doc__
        """ QDropEvent.mimeData() -> QMimeData """
        pass

    def mouseButtons(self): # real signature unknown; restored from __doc__
        """ QDropEvent.mouseButtons() -> Qt.MouseButtons """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ QDropEvent.pos() -> QPoint """
        pass

    def possibleActions(self): # real signature unknown; restored from __doc__
        """ QDropEvent.possibleActions() -> Qt.DropActions """
        pass

    def proposedAction(self): # real signature unknown; restored from __doc__
        """ QDropEvent.proposedAction() -> Qt.DropAction """
        pass

    def provides(self, p_str): # real signature unknown; restored from __doc__
        """ QDropEvent.provides(str) -> bool """
        return False

    def setDropAction(self, Qt_DropAction): # real signature unknown; restored from __doc__
        """ QDropEvent.setDropAction(Qt.DropAction) """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ QDropEvent.source() -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


