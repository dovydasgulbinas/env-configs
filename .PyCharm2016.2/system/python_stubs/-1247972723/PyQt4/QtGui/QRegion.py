# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QRegion(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QRegion()
    QRegion(int, int, int, int, QRegion.RegionType type=QRegion.Rectangle)
    QRegion(QRect, QRegion.RegionType type=QRegion.Rectangle)
    QRegion(QPolygon, Qt.FillRule fillRule=Qt.OddEvenFill)
    QRegion(QBitmap)
    QRegion(QRegion)
    QRegion(QVariant)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QRegion.boundingRect() -> QRect """
        pass

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRegion.contains(QPoint) -> bool
        QRegion.contains(QRect) -> bool
        """
        return False

    def eor(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.eor(QRegion) -> QRegion """
        return QRegion

    def intersect(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.intersect(QRegion) -> QRegion """
        return QRegion

    def intersected(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRegion.intersected(QRegion) -> QRegion
        QRegion.intersected(QRect) -> QRegion
        """
        return QRegion

    def intersects(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRegion.intersects(QRegion) -> bool
        QRegion.intersects(QRect) -> bool
        """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QRegion.isEmpty() -> bool """
        return False

    def numRects(self): # real signature unknown; restored from __doc__
        """ QRegion.numRects() -> int """
        return 0

    def rectCount(self): # real signature unknown; restored from __doc__
        """ QRegion.rectCount() -> int """
        return 0

    def rects(self): # real signature unknown; restored from __doc__
        """ QRegion.rects() -> list-of-QRect """
        pass

    def subtract(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.subtract(QRegion) -> QRegion """
        return QRegion

    def subtracted(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.subtracted(QRegion) -> QRegion """
        return QRegion

    def swap(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.swap(QRegion) """
        pass

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRegion.translate(int, int)
        QRegion.translate(QPoint)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRegion.translated(int, int) -> QRegion
        QRegion.translated(QPoint) -> QRegion
        """
        return QRegion

    def unite(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.unite(QRegion) -> QRegion """
        return QRegion

    def united(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRegion.united(QRegion) -> QRegion
        QRegion.united(QRect) -> QRegion
        """
        return QRegion

    def xored(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.xored(QRegion) -> QRegion """
        return QRegion

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, y): # real signature unknown; restored from __doc__
        """ x.__and__(y) <==> x&y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
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

    def __ixor__(self, y): # real signature unknown; restored from __doc__
        """ x.__ixor__(y) <==> x^=y """
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

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
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

    def __rxor__(self, y): # real signature unknown; restored from __doc__
        """ x.__rxor__(y) <==> y^x """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __xor__(self, y): # real signature unknown; restored from __doc__
        """ x.__xor__(y) <==> x^y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Ellipse = 1
    Rectangle = 0


