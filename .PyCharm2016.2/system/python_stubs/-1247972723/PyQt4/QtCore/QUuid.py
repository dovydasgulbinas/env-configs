# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QUuid(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QUuid()
    QUuid(int, int, int, str, str, str, str, str, str, str, str)
    QUuid(QString)
    QUuid(QByteArray)
    QUuid(QUuid)
    """
    def createUuid(self): # real signature unknown; restored from __doc__
        """ QUuid.createUuid() -> QUuid """
        return QUuid

    def fromRfc4122(self, QByteArray): # real signature unknown; restored from __doc__
        """ QUuid.fromRfc4122(QByteArray) -> QUuid """
        return QUuid

    def isNull(self): # real signature unknown; restored from __doc__
        """ QUuid.isNull() -> bool """
        return False

    def toByteArray(self): # real signature unknown; restored from __doc__
        """ QUuid.toByteArray() -> QByteArray """
        return QByteArray

    def toRfc4122(self): # real signature unknown; restored from __doc__
        """ QUuid.toRfc4122() -> QByteArray """
        return QByteArray

    def toString(self): # real signature unknown; restored from __doc__
        """ QUuid.toString() -> QString """
        return QString

    def variant(self): # real signature unknown; restored from __doc__
        """ QUuid.variant() -> QUuid.Variant """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ QUuid.version() -> QUuid.Version """
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

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DCE = 2
    EmbeddedPOSIX = 2
    Microsoft = 6
    Name = 3
    NCS = 0
    Random = 4
    Reserved = 7
    Time = 1
    VarUnknown = -1
    VerUnknown = -1


