# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QValidator import QValidator

class QDoubleValidator(QValidator):
    """
    QDoubleValidator(QObject parent=None)
    QDoubleValidator(float, float, int, QObject parent=None)
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ QDoubleValidator.bottom() -> float """
        return 0.0

    def decimals(self): # real signature unknown; restored from __doc__
        """ QDoubleValidator.decimals() -> int """
        return 0

    def notation(self): # real signature unknown; restored from __doc__
        """ QDoubleValidator.notation() -> QDoubleValidator.Notation """
        pass

    def setBottom(self, p_float): # real signature unknown; restored from __doc__
        """ QDoubleValidator.setBottom(float) """
        pass

    def setDecimals(self, p_int): # real signature unknown; restored from __doc__
        """ QDoubleValidator.setDecimals(int) """
        pass

    def setNotation(self, QDoubleValidator_Notation): # real signature unknown; restored from __doc__
        """ QDoubleValidator.setNotation(QDoubleValidator.Notation) """
        pass

    def setRange(self, p_float, p_float_1, int_decimals=0): # real signature unknown; restored from __doc__
        """ QDoubleValidator.setRange(float, float, int decimals=0) """
        pass

    def setTop(self, p_float): # real signature unknown; restored from __doc__
        """ QDoubleValidator.setTop(float) """
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ QDoubleValidator.top() -> float """
        return 0.0

    def validate(self, QString, p_int): # real signature unknown; restored from __doc__
        """ QDoubleValidator.validate(QString, int) -> (QValidator.State, int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ScientificNotation = 1
    StandardNotation = 0


