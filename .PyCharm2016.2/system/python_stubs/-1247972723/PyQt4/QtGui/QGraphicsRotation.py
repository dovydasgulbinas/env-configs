# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QGraphicsTransform import QGraphicsTransform

class QGraphicsRotation(QGraphicsTransform):
    """ QGraphicsRotation(QObject parent=None) """
    def angle(self): # real signature unknown; restored from __doc__
        """ QGraphicsRotation.angle() -> float """
        return 0.0

    def angleChanged(self, *args, **kwargs): # real signature unknown
        """ QGraphicsRotation.angleChanged [signal] """
        pass

    def applyTo(self, QMatrix4x4): # real signature unknown; restored from __doc__
        """ QGraphicsRotation.applyTo(QMatrix4x4) """
        pass

    def axis(self): # real signature unknown; restored from __doc__
        """ QGraphicsRotation.axis() -> QVector3D """
        return QVector3D

    def axisChanged(self, *args, **kwargs): # real signature unknown
        """ QGraphicsRotation.axisChanged [signal] """
        pass

    def origin(self): # real signature unknown; restored from __doc__
        """ QGraphicsRotation.origin() -> QVector3D """
        return QVector3D

    def originChanged(self, *args, **kwargs): # real signature unknown
        """ QGraphicsRotation.originChanged [signal] """
        pass

    def setAngle(self, p_float): # real signature unknown; restored from __doc__
        """ QGraphicsRotation.setAngle(float) """
        pass

    def setAxis(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsRotation.setAxis(QVector3D)
        QGraphicsRotation.setAxis(Qt.Axis)
        """
        pass

    def setOrigin(self, QVector3D): # real signature unknown; restored from __doc__
        """ QGraphicsRotation.setOrigin(QVector3D) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


