# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QDialog(QWidget):
    """ QDialog(QWidget parent=None, Qt.WindowFlags flags=0) """
    def accept(self): # real signature unknown; restored from __doc__
        """ QDialog.accept() """
        pass

    def accepted(self, *args, **kwargs): # real signature unknown
        """ QDialog.accepted [signal] """
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ QDialog.closeEvent(QCloseEvent) """
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ QDialog.contextMenuEvent(QContextMenuEvent) """
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ QDialog.done(int) """
        pass

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QDialog.eventFilter(QObject, QEvent) -> bool """
        return False

    def exec_(self): # real signature unknown; restored from __doc__
        """ QDialog.exec_() -> int """
        return 0

    def extension(self): # real signature unknown; restored from __doc__
        """ QDialog.extension() -> QWidget """
        return QWidget

    def finished(self, *args, **kwargs): # real signature unknown
        """ QDialog.finished[int] [signal] """
        pass

    def isSizeGripEnabled(self): # real signature unknown; restored from __doc__
        """ QDialog.isSizeGripEnabled() -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QDialog.keyPressEvent(QKeyEvent) """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QDialog.minimumSizeHint() -> QSize """
        pass

    def open(self): # real signature unknown; restored from __doc__
        """ QDialog.open() """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ QDialog.orientation() -> Qt.Orientation """
        pass

    def reject(self): # real signature unknown; restored from __doc__
        """ QDialog.reject() """
        pass

    def rejected(self, *args, **kwargs): # real signature unknown
        """ QDialog.rejected [signal] """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QDialog.resizeEvent(QResizeEvent) """
        pass

    def result(self): # real signature unknown; restored from __doc__
        """ QDialog.result() -> int """
        return 0

    def setExtension(self, QWidget): # real signature unknown; restored from __doc__
        """ QDialog.setExtension(QWidget) """
        pass

    def setModal(self, bool): # real signature unknown; restored from __doc__
        """ QDialog.setModal(bool) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QDialog.setOrientation(Qt.Orientation) """
        pass

    def setResult(self, p_int): # real signature unknown; restored from __doc__
        """ QDialog.setResult(int) """
        pass

    def setSizeGripEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QDialog.setSizeGripEnabled(bool) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QDialog.setVisible(bool) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QDialog.showEvent(QShowEvent) """
        pass

    def showExtension(self, bool): # real signature unknown; restored from __doc__
        """ QDialog.showExtension(bool) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QDialog.sizeHint() -> QSize """
        pass

    def __init__(self, QWidget_parent=None, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass

    Accepted = 1
    Rejected = 0


