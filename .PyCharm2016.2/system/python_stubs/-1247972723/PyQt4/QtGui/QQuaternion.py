# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QQuaternion(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QQuaternion()
    QQuaternion(float, float, float, float)
    QQuaternion(float, QVector3D)
    QQuaternion(QVector4D)
    QQuaternion(QQuaternion)
    """
    def conjugate(self): # real signature unknown; restored from __doc__
        """ QQuaternion.conjugate() -> QQuaternion """
        return QQuaternion

    def fromAxisAndAngle(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QQuaternion.fromAxisAndAngle(QVector3D, float) -> QQuaternion
        QQuaternion.fromAxisAndAngle(float, float, float, float) -> QQuaternion
        """
        return QQuaternion

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ QQuaternion.isIdentity() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QQuaternion.isNull() -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ QQuaternion.length() -> float """
        return 0.0

    def lengthSquared(self): # real signature unknown; restored from __doc__
        """ QQuaternion.lengthSquared() -> float """
        return 0.0

    def nlerp(self, QQuaternion, QQuaternion_1, p_float): # real signature unknown; restored from __doc__
        """ QQuaternion.nlerp(QQuaternion, QQuaternion, float) -> QQuaternion """
        return QQuaternion

    def normalize(self): # real signature unknown; restored from __doc__
        """ QQuaternion.normalize() """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ QQuaternion.normalized() -> QQuaternion """
        return QQuaternion

    def rotatedVector(self, QVector3D): # real signature unknown; restored from __doc__
        """ QQuaternion.rotatedVector(QVector3D) -> QVector3D """
        return QVector3D

    def scalar(self): # real signature unknown; restored from __doc__
        """ QQuaternion.scalar() -> float """
        return 0.0

    def setScalar(self, p_float): # real signature unknown; restored from __doc__
        """ QQuaternion.setScalar(float) """
        pass

    def setVector(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QQuaternion.setVector(QVector3D)
        QQuaternion.setVector(float, float, float)
        """
        pass

    def setX(self, p_float): # real signature unknown; restored from __doc__
        """ QQuaternion.setX(float) """
        pass

    def setY(self, p_float): # real signature unknown; restored from __doc__
        """ QQuaternion.setY(float) """
        pass

    def setZ(self, p_float): # real signature unknown; restored from __doc__
        """ QQuaternion.setZ(float) """
        pass

    def slerp(self, QQuaternion, QQuaternion_1, p_float): # real signature unknown; restored from __doc__
        """ QQuaternion.slerp(QQuaternion, QQuaternion, float) -> QQuaternion """
        return QQuaternion

    def toVector4D(self): # real signature unknown; restored from __doc__
        """ QQuaternion.toVector4D() -> QVector4D """
        return QVector4D

    def vector(self): # real signature unknown; restored from __doc__
        """ QQuaternion.vector() -> QVector3D """
        return QVector3D

    def x(self): # real signature unknown; restored from __doc__
        """ QQuaternion.x() -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ QQuaternion.y() -> float """
        return 0.0

    def z(self): # real signature unknown; restored from __doc__
        """ QQuaternion.z() -> float """
        return 0.0

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, y): # real signature unknown; restored from __doc__
        """ x.__div__(y) <==> x/y """
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

    def __idiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__idiv__(y) <==> x/=y """
        pass

    def __imul__(self, y): # real signature unknown; restored from __doc__
        """ x.__imul__(y) <==> x*=y """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __isub__(self, y): # real signature unknown; restored from __doc__
        """ x.__isub__(y) <==> x-=y """
        pass

    def __itruediv__(self, y): # real signature unknown; restored from __doc__
        """ x.__itruediv__(y) <==> x/=y """
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

    def __neg__(self): # real signature unknown; restored from __doc__
        """ x.__neg__() <==> -x """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rdiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmul__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmul__(y) <==> y*x """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __rtruediv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rtruediv__(y) <==> y/x """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, y): # real signature unknown; restored from __doc__
        """ x.__truediv__(y) <==> x/y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



