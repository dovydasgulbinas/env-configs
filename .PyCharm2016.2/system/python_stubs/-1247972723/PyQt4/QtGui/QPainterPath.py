# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QPainterPath(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QPainterPath()
    QPainterPath(QPointF)
    QPainterPath(QPainterPath)
    """
    def addEllipse(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.addEllipse(QRectF)
        QPainterPath.addEllipse(float, float, float, float)
        QPainterPath.addEllipse(QPointF, float, float)
        """
        pass

    def addPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.addPath(QPainterPath) """
        pass

    def addPolygon(self, QPolygonF): # real signature unknown; restored from __doc__
        """ QPainterPath.addPolygon(QPolygonF) """
        pass

    def addRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.addRect(QRectF)
        QPainterPath.addRect(float, float, float, float)
        """
        pass

    def addRegion(self, QRegion): # real signature unknown; restored from __doc__
        """ QPainterPath.addRegion(QRegion) """
        pass

    def addRoundedRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.addRoundedRect(QRectF, float, float, Qt.SizeMode mode=Qt.AbsoluteSize)
        QPainterPath.addRoundedRect(float, float, float, float, float, float, Qt.SizeMode mode=Qt.AbsoluteSize)
        """
        pass

    def addRoundRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.addRoundRect(QRectF, int, int)
        QPainterPath.addRoundRect(float, float, float, float, int, int)
        QPainterPath.addRoundRect(QRectF, int)
        QPainterPath.addRoundRect(float, float, float, float, int)
        """
        pass

    def addText(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.addText(QPointF, QFont, QString)
        QPainterPath.addText(float, float, QFont, QString)
        """
        pass

    def angleAtPercent(self, p_float): # real signature unknown; restored from __doc__
        """ QPainterPath.angleAtPercent(float) -> float """
        return 0.0

    def arcMoveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.arcMoveTo(QRectF, float)
        QPainterPath.arcMoveTo(float, float, float, float, float)
        """
        pass

    def arcTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.arcTo(QRectF, float, float)
        QPainterPath.arcTo(float, float, float, float, float, float)
        """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QPainterPath.boundingRect() -> QRectF """
        pass

    def closeSubpath(self): # real signature unknown; restored from __doc__
        """ QPainterPath.closeSubpath() """
        pass

    def connectPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.connectPath(QPainterPath) """
        pass

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.contains(QPointF) -> bool
        QPainterPath.contains(QRectF) -> bool
        QPainterPath.contains(QPainterPath) -> bool
        """
        return False

    def controlPointRect(self): # real signature unknown; restored from __doc__
        """ QPainterPath.controlPointRect() -> QRectF """
        pass

    def cubicTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.cubicTo(QPointF, QPointF, QPointF)
        QPainterPath.cubicTo(float, float, float, float, float, float)
        """
        pass

    def currentPosition(self): # real signature unknown; restored from __doc__
        """ QPainterPath.currentPosition() -> QPointF """
        pass

    def elementAt(self, p_int): # real signature unknown; restored from __doc__
        """ QPainterPath.elementAt(int) -> QPainterPath.Element """
        pass

    def elementCount(self): # real signature unknown; restored from __doc__
        """ QPainterPath.elementCount() -> int """
        return 0

    def fillRule(self): # real signature unknown; restored from __doc__
        """ QPainterPath.fillRule() -> Qt.FillRule """
        pass

    def intersected(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.intersected(QPainterPath) -> QPainterPath """
        return QPainterPath

    def intersects(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.intersects(QRectF) -> bool
        QPainterPath.intersects(QPainterPath) -> bool
        """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QPainterPath.isEmpty() -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ QPainterPath.length() -> float """
        return 0.0

    def lineTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.lineTo(QPointF)
        QPainterPath.lineTo(float, float)
        """
        pass

    def moveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.moveTo(QPointF)
        QPainterPath.moveTo(float, float)
        """
        pass

    def percentAtLength(self, p_float): # real signature unknown; restored from __doc__
        """ QPainterPath.percentAtLength(float) -> float """
        return 0.0

    def pointAtPercent(self, p_float): # real signature unknown; restored from __doc__
        """ QPainterPath.pointAtPercent(float) -> QPointF """
        pass

    def quadTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.quadTo(QPointF, QPointF)
        QPainterPath.quadTo(float, float, float, float)
        """
        pass

    def setElementPositionAt(self, p_int, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QPainterPath.setElementPositionAt(int, float, float) """
        pass

    def setFillRule(self, Qt_FillRule): # real signature unknown; restored from __doc__
        """ QPainterPath.setFillRule(Qt.FillRule) """
        pass

    def simplified(self): # real signature unknown; restored from __doc__
        """ QPainterPath.simplified() -> QPainterPath """
        return QPainterPath

    def slopeAtPercent(self, p_float): # real signature unknown; restored from __doc__
        """ QPainterPath.slopeAtPercent(float) -> float """
        return 0.0

    def subtracted(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.subtracted(QPainterPath) -> QPainterPath """
        return QPainterPath

    def subtractedInverted(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.subtractedInverted(QPainterPath) -> QPainterPath """
        return QPainterPath

    def swap(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.swap(QPainterPath) """
        pass

    def toFillPolygon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.toFillPolygon(QMatrix matrix=QMatrix()) -> QPolygonF
        QPainterPath.toFillPolygon(QTransform) -> QPolygonF
        """
        return QPolygonF

    def toFillPolygons(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.toFillPolygons(QMatrix matrix=QMatrix()) -> list-of-QPolygonF
        QPainterPath.toFillPolygons(QTransform) -> list-of-QPolygonF
        """
        pass

    def toReversed(self): # real signature unknown; restored from __doc__
        """ QPainterPath.toReversed() -> QPainterPath """
        return QPainterPath

    def toSubpathPolygons(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.toSubpathPolygons(QMatrix matrix=QMatrix()) -> list-of-QPolygonF
        QPainterPath.toSubpathPolygons(QTransform) -> list-of-QPolygonF
        """
        pass

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.translate(float, float)
        QPainterPath.translate(QPointF)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.translated(float, float) -> QPainterPath
        QPainterPath.translated(QPointF) -> QPainterPath
        """
        return QPainterPath

    def united(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.united(QPainterPath) -> QPainterPath """
        return QPainterPath

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, y): # real signature unknown; restored from __doc__
        """ x.__and__(y) <==> x&y """
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

    def __iadd__(self, y): # real signature unknown; restored from __doc__
        """ x.__iadd__(y) <==> x+=y """
        pass

    def __iand__(self, y): # real signature unknown; restored from __doc__
        """ x.__iand__(y) <==> x&=y """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __ior__(self, y): # real signature unknown; restored from __doc__
        """ x.__ior__(y) <==> x|=y """
        pass

    def __isub__(self, y): # real signature unknown; restored from __doc__
        """ x.__isub__(y) <==> x-=y """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mul__(self, y): # real signature unknown; restored from __doc__
        """ x.__mul__(y) <==> x*y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __or__(self, y): # real signature unknown; restored from __doc__
        """ x.__or__(y) <==> x|y """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rand__(self, y): # real signature unknown; restored from __doc__
        """ x.__rand__(y) <==> y&x """
        pass

    def __rmul__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmul__(y) <==> y*x """
        pass

    def __ror__(self, y): # real signature unknown; restored from __doc__
        """ x.__ror__(y) <==> y|x """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CurveToDataElement = 3
    CurveToElement = 2
    LineToElement = 1
    MoveToElement = 0


