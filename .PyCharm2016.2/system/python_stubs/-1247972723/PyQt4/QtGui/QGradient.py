# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QGradient(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QGradient()
    QGradient(QGradient)
    """
    def coordinateMode(self): # real signature unknown; restored from __doc__
        """ QGradient.coordinateMode() -> QGradient.CoordinateMode """
        pass

    def setColorAt(self, p_float, QColor): # real signature unknown; restored from __doc__
        """ QGradient.setColorAt(float, QColor) """
        pass

    def setCoordinateMode(self, QGradient_CoordinateMode): # real signature unknown; restored from __doc__
        """ QGradient.setCoordinateMode(QGradient.CoordinateMode) """
        pass

    def setSpread(self, QGradient_Spread): # real signature unknown; restored from __doc__
        """ QGradient.setSpread(QGradient.Spread) """
        pass

    def setStops(self, list_of_tuple_of_float_QColor): # real signature unknown; restored from __doc__
        """ QGradient.setStops(list-of-tuple-of-float-QColor) """
        pass

    def spread(self): # real signature unknown; restored from __doc__
        """ QGradient.spread() -> QGradient.Spread """
        pass

    def stops(self): # real signature unknown; restored from __doc__
        """ QGradient.stops() -> list-of-tuple-of-float-QColor """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QGradient.type() -> QGradient.Type """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, QGradient=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ConicalGradient = 2
    LinearGradient = 0
    LogicalMode = 0
    NoGradient = 3
    ObjectBoundingMode = 2
    PadSpread = 0
    RadialGradient = 1
    ReflectSpread = 1
    RepeatSpread = 2
    StretchToDeviceMode = 1


