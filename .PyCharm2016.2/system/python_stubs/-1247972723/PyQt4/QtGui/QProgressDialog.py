# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QProgressDialog(QDialog):
    """
    QProgressDialog(QWidget parent=None, Qt.WindowFlags flags=0)
    QProgressDialog(QString, QString, int, int, QWidget parent=None, Qt.WindowFlags flags=0)
    """
    def autoClose(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.autoClose() -> bool """
        return False

    def autoReset(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.autoReset() -> bool """
        return False

    def cancel(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.cancel() """
        pass

    def canceled(self, *args, **kwargs): # real signature unknown
        """ QProgressDialog.canceled [signal] """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QProgressDialog.changeEvent(QEvent) """
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ QProgressDialog.closeEvent(QCloseEvent) """
        pass

    def forceShow(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.forceShow() """
        pass

    def labelText(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.labelText() -> QString """
        pass

    def maximum(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.maximum() -> int """
        return 0

    def minimum(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.minimum() -> int """
        return 0

    def minimumDuration(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.minimumDuration() -> int """
        return 0

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QProgressDialog.open()
        QProgressDialog.open(QObject, SLOT())
        QProgressDialog.open(callable)
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.reset() """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QProgressDialog.resizeEvent(QResizeEvent) """
        pass

    def setAutoClose(self, bool): # real signature unknown; restored from __doc__
        """ QProgressDialog.setAutoClose(bool) """
        pass

    def setAutoReset(self, bool): # real signature unknown; restored from __doc__
        """ QProgressDialog.setAutoReset(bool) """
        pass

    def setBar(self, QProgressBar): # real signature unknown; restored from __doc__
        """ QProgressDialog.setBar(QProgressBar) """
        pass

    def setCancelButton(self, QPushButton): # real signature unknown; restored from __doc__
        """ QProgressDialog.setCancelButton(QPushButton) """
        pass

    def setCancelButtonText(self, QString): # real signature unknown; restored from __doc__
        """ QProgressDialog.setCancelButtonText(QString) """
        pass

    def setLabel(self, QLabel): # real signature unknown; restored from __doc__
        """ QProgressDialog.setLabel(QLabel) """
        pass

    def setLabelText(self, QString): # real signature unknown; restored from __doc__
        """ QProgressDialog.setLabelText(QString) """
        pass

    def setMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ QProgressDialog.setMaximum(int) """
        pass

    def setMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ QProgressDialog.setMinimum(int) """
        pass

    def setMinimumDuration(self, p_int): # real signature unknown; restored from __doc__
        """ QProgressDialog.setMinimumDuration(int) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QProgressDialog.setRange(int, int) """
        pass

    def setValue(self, p_int): # real signature unknown; restored from __doc__
        """ QProgressDialog.setValue(int) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QProgressDialog.showEvent(QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.sizeHint() -> QSize """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.value() -> int """
        return 0

    def wasCanceled(self): # real signature unknown; restored from __doc__
        """ QProgressDialog.wasCanceled() -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


