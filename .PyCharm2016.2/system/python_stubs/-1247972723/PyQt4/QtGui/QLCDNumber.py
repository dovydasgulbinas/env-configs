# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QFrame import QFrame

class QLCDNumber(QFrame):
    """
    QLCDNumber(QWidget parent=None)
    QLCDNumber(int, QWidget parent=None)
    """
    def checkOverflow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLCDNumber.checkOverflow(float) -> bool
        QLCDNumber.checkOverflow(int) -> bool
        """
        return False

    def digitCount(self): # real signature unknown; restored from __doc__
        """ QLCDNumber.digitCount() -> int """
        return 0

    def display(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLCDNumber.display(QString)
        QLCDNumber.display(float)
        QLCDNumber.display(int)
        """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QLCDNumber.event(QEvent) -> bool """
        return False

    def intValue(self): # real signature unknown; restored from __doc__
        """ QLCDNumber.intValue() -> int """
        return 0

    def mode(self): # real signature unknown; restored from __doc__
        """ QLCDNumber.mode() -> QLCDNumber.Mode """
        pass

    def numDigits(self): # real signature unknown; restored from __doc__
        """ QLCDNumber.numDigits() -> int """
        return 0

    def overflow(self, *args, **kwargs): # real signature unknown
        """ QLCDNumber.overflow [signal] """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QLCDNumber.paintEvent(QPaintEvent) """
        pass

    def segmentStyle(self): # real signature unknown; restored from __doc__
        """ QLCDNumber.segmentStyle() -> QLCDNumber.SegmentStyle """
        pass

    def setBinMode(self): # real signature unknown; restored from __doc__
        """ QLCDNumber.setBinMode() """
        pass

    def setDecMode(self): # real signature unknown; restored from __doc__
        """ QLCDNumber.setDecMode() """
        pass

    def setDigitCount(self, p_int): # real signature unknown; restored from __doc__
        """ QLCDNumber.setDigitCount(int) """
        pass

    def setHexMode(self): # real signature unknown; restored from __doc__
        """ QLCDNumber.setHexMode() """
        pass

    def setMode(self, QLCDNumber_Mode): # real signature unknown; restored from __doc__
        """ QLCDNumber.setMode(QLCDNumber.Mode) """
        pass

    def setNumDigits(self, p_int): # real signature unknown; restored from __doc__
        """ QLCDNumber.setNumDigits(int) """
        pass

    def setOctMode(self): # real signature unknown; restored from __doc__
        """ QLCDNumber.setOctMode() """
        pass

    def setSegmentStyle(self, QLCDNumber_SegmentStyle): # real signature unknown; restored from __doc__
        """ QLCDNumber.setSegmentStyle(QLCDNumber.SegmentStyle) """
        pass

    def setSmallDecimalPoint(self, bool): # real signature unknown; restored from __doc__
        """ QLCDNumber.setSmallDecimalPoint(bool) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QLCDNumber.sizeHint() -> QSize """
        pass

    def smallDecimalPoint(self): # real signature unknown; restored from __doc__
        """ QLCDNumber.smallDecimalPoint() -> bool """
        return False

    def value(self): # real signature unknown; restored from __doc__
        """ QLCDNumber.value() -> float """
        return 0.0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Bin = 3
    Dec = 1
    Filled = 1
    Flat = 2
    Hex = 0
    Oct = 2
    Outline = 0


