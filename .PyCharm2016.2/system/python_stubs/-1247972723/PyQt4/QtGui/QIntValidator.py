# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QValidator import QValidator

class QIntValidator(QValidator):
    """
    QIntValidator(QObject parent=None)
    QIntValidator(int, int, QObject parent=None)
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ QIntValidator.bottom() -> int """
        return 0

    def fixup(self, QString): # real signature unknown; restored from __doc__
        """ QIntValidator.fixup(QString) """
        pass

    def setBottom(self, p_int): # real signature unknown; restored from __doc__
        """ QIntValidator.setBottom(int) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QIntValidator.setRange(int, int) """
        pass

    def setTop(self, p_int): # real signature unknown; restored from __doc__
        """ QIntValidator.setTop(int) """
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ QIntValidator.top() -> int """
        return 0

    def validate(self, QString, p_int): # real signature unknown; restored from __doc__
        """ QIntValidator.validate(QString, int) -> (QValidator.State, int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


