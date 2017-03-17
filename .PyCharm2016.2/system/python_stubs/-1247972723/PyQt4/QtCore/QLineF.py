# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QLineF(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QLineF(QLine)
    QLineF()
    QLineF(QPointF, QPointF)
    QLineF(float, float, float, float)
    QLineF(QLineF)
    """
    def angle(self, QLineF=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLineF.angle(QLineF) -> float
        QLineF.angle() -> float
        """
        return 0.0

    def angleTo(self, QLineF): # real signature unknown; restored from __doc__
        """ QLineF.angleTo(QLineF) -> float """
        return 0.0

    def dx(self): # real signature unknown; restored from __doc__
        """ QLineF.dx() -> float """
        return 0.0

    def dy(self): # real signature unknown; restored from __doc__
        """ QLineF.dy() -> float """
        return 0.0

    def fromPolar(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QLineF.fromPolar(float, float) -> QLineF """
        return QLineF

    def intersect(self, QLineF, QPointF): # real signature unknown; restored from __doc__
        """ QLineF.intersect(QLineF, QPointF) -> QLineF.IntersectType """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ QLineF.isNull() -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ QLineF.length() -> float """
        return 0.0

    def normalVector(self): # real signature unknown; restored from __doc__
        """ QLineF.normalVector() -> QLineF """
        return QLineF

    def p1(self): # real signature unknown; restored from __doc__
        """ QLineF.p1() -> QPointF """
        return QPointF

    def p2(self): # real signature unknown; restored from __doc__
        """ QLineF.p2() -> QPointF """
        return QPointF

    def pointAt(self, p_float): # real signature unknown; restored from __doc__
        """ QLineF.pointAt(float) -> QPointF """
        return QPointF

    def setAngle(self, p_float): # real signature unknown; restored from __doc__
        """ QLineF.setAngle(float) """
        pass

    def setLength(self, p_float): # real signature unknown; restored from __doc__
        """ QLineF.setLength(float) """
        pass

    def setLine(self, p_float, p_float_1, p_float_2, p_float_3): # real signature unknown; restored from __doc__
        """ QLineF.setLine(float, float, float, float) """
        pass

    def setP1(self, QPointF): # real signature unknown; restored from __doc__
        """ QLineF.setP1(QPointF) """
        pass

    def setP2(self, QPointF): # real signature unknown; restored from __doc__
        """ QLineF.setP2(QPointF) """
        pass

    def setPoints(self, QPointF, QPointF_1): # real signature unknown; restored from __doc__
        """ QLineF.setPoints(QPointF, QPointF) """
        pass

    def toLine(self): # real signature unknown; restored from __doc__
        """ QLineF.toLine() -> QLine """
        return QLine

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLineF.translate(QPointF)
        QLineF.translate(float, float)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLineF.translated(QPointF) -> QLineF
        QLineF.translated(float, float) -> QLineF
        """
        return QLineF

    def unitVector(self): # real signature unknown; restored from __doc__
        """ QLineF.unitVector() -> QLineF """
        return QLineF

    def x1(self): # real signature unknown; restored from __doc__
        """ QLineF.x1() -> float """
        return 0.0

    def x2(self): # real signature unknown; restored from __doc__
        """ QLineF.x2() -> float """
        return 0.0

    def y1(self): # real signature unknown; restored from __doc__
        """ QLineF.y1() -> float """
        return 0.0

    def y2(self): # real signature unknown; restored from __doc__
        """ QLineF.y2() -> float """
        return 0.0

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BoundedIntersection = 1
    NoIntersection = 0
    UnboundedIntersection = 2


