# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QVariant(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QVariant()
    QVariant(Type)
    QVariant(int, sip.voidptr)
    QVariant(QVariant)
    QVariant(object)
    """
    def canConvert(self, Type): # real signature unknown; restored from __doc__
        """ QVariant.canConvert(Type) -> bool """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ QVariant.clear() """
        pass

    def convert(self, Type): # real signature unknown; restored from __doc__
        """ QVariant.convert(Type) -> bool """
        return False

    def data(self): # real signature unknown; restored from __doc__
        """ QVariant.data() -> sip.voidptr """
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """ QVariant.detach() """
        pass

    def fromList(self, list_of_QVariant): # real signature unknown; restored from __doc__
        """ QVariant.fromList(list-of-QVariant) -> QVariant """
        return QVariant

    def fromMap(self, dict_of_QString_QVariant): # real signature unknown; restored from __doc__
        """ QVariant.fromMap(dict-of-QString-QVariant) -> QVariant """
        return QVariant

    def isDetached(self): # real signature unknown; restored from __doc__
        """ QVariant.isDetached() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QVariant.isNull() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QVariant.isValid() -> bool """
        return False

    def load(self, QDataStream): # real signature unknown; restored from __doc__
        """ QVariant.load(QDataStream) """
        pass

    def nameToType(self, p_str): # real signature unknown; restored from __doc__
        """ QVariant.nameToType(str) -> Type """
        pass

    def save(self, QDataStream): # real signature unknown; restored from __doc__
        """ QVariant.save(QDataStream) """
        pass

    def swap(self, QVariant): # real signature unknown; restored from __doc__
        """ QVariant.swap(QVariant) """
        pass

    def toBitArray(self): # real signature unknown; restored from __doc__
        """ QVariant.toBitArray() -> QBitArray """
        return QBitArray

    def toBool(self): # real signature unknown; restored from __doc__
        """ QVariant.toBool() -> bool """
        return False

    def toByteArray(self): # real signature unknown; restored from __doc__
        """ QVariant.toByteArray() -> QByteArray """
        return QByteArray

    def toChar(self): # real signature unknown; restored from __doc__
        """ QVariant.toChar() -> QChar """
        return QChar

    def toDate(self): # real signature unknown; restored from __doc__
        """ QVariant.toDate() -> QDate """
        return QDate

    def toDateTime(self): # real signature unknown; restored from __doc__
        """ QVariant.toDateTime() -> QDateTime """
        return QDateTime

    def toDouble(self): # real signature unknown; restored from __doc__
        """ QVariant.toDouble() -> (float, bool) """
        pass

    def toEasingCurve(self): # real signature unknown; restored from __doc__
        """ QVariant.toEasingCurve() -> QEasingCurve """
        return QEasingCurve

    def toFloat(self): # real signature unknown; restored from __doc__
        """ QVariant.toFloat() -> (float, bool) """
        pass

    def toHash(self): # real signature unknown; restored from __doc__
        """ QVariant.toHash() -> dict-of-QString-QVariant """
        pass

    def toInt(self): # real signature unknown; restored from __doc__
        """ QVariant.toInt() -> (int, bool) """
        pass

    def toLine(self): # real signature unknown; restored from __doc__
        """ QVariant.toLine() -> QLine """
        return QLine

    def toLineF(self): # real signature unknown; restored from __doc__
        """ QVariant.toLineF() -> QLineF """
        return QLineF

    def toList(self): # real signature unknown; restored from __doc__
        """ QVariant.toList() -> list-of-QVariant """
        pass

    def toLocale(self): # real signature unknown; restored from __doc__
        """ QVariant.toLocale() -> QLocale """
        return QLocale

    def toLongLong(self): # real signature unknown; restored from __doc__
        """ QVariant.toLongLong() -> (int, bool) """
        pass

    def toMap(self): # real signature unknown; restored from __doc__
        """ QVariant.toMap() -> dict-of-QString-QVariant """
        pass

    def toPoint(self): # real signature unknown; restored from __doc__
        """ QVariant.toPoint() -> QPoint """
        return QPoint

    def toPointF(self): # real signature unknown; restored from __doc__
        """ QVariant.toPointF() -> QPointF """
        return QPointF

    def toPyObject(self): # real signature unknown; restored from __doc__
        """ QVariant.toPyObject() -> object """
        return object()

    def toReal(self): # real signature unknown; restored from __doc__
        """ QVariant.toReal() -> (float, bool) """
        pass

    def toRect(self): # real signature unknown; restored from __doc__
        """ QVariant.toRect() -> QRect """
        return QRect

    def toRectF(self): # real signature unknown; restored from __doc__
        """ QVariant.toRectF() -> QRectF """
        return QRectF

    def toRegExp(self): # real signature unknown; restored from __doc__
        """ QVariant.toRegExp() -> QRegExp """
        return QRegExp

    def toSize(self): # real signature unknown; restored from __doc__
        """ QVariant.toSize() -> QSize """
        return QSize

    def toSizeF(self): # real signature unknown; restored from __doc__
        """ QVariant.toSizeF() -> QSizeF """
        return QSizeF

    def toString(self): # real signature unknown; restored from __doc__
        """ QVariant.toString() -> QString """
        return QString

    def toStringList(self): # real signature unknown; restored from __doc__
        """ QVariant.toStringList() -> QStringList """
        return QStringList

    def toTime(self): # real signature unknown; restored from __doc__
        """ QVariant.toTime() -> QTime """
        return QTime

    def toUInt(self): # real signature unknown; restored from __doc__
        """ QVariant.toUInt() -> (int, bool) """
        pass

    def toULongLong(self): # real signature unknown; restored from __doc__
        """ QVariant.toULongLong() -> (int, bool) """
        pass

    def toUrl(self): # real signature unknown; restored from __doc__
        """ QVariant.toUrl() -> QUrl """
        return QUrl

    def type(self): # real signature unknown; restored from __doc__
        """ QVariant.type() -> Type """
        pass

    def typeName(self): # real signature unknown; restored from __doc__
        """ QVariant.typeName() -> str """
        return ""

    def typeToName(self, Type): # real signature unknown; restored from __doc__
        """ QVariant.typeToName(Type) -> str """
        return ""

    def userType(self): # real signature unknown; restored from __doc__
        """ QVariant.userType() -> int """
        return 0

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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BitArray = 13
    Bitmap = 73
    Bool = 1
    Brush = 66
    ByteArray = 12
    Char = 7
    Color = 67
    Cursor = 74
    Date = 14
    DateTime = 16
    Double = 6
    EasingCurve = 29
    Font = 64
    Hash = 28
    Icon = 69
    Image = 70
    Int = 2
    Invalid = 0
    KeySequence = 76
    Line = 23
    LineF = 24
    List = 9
    Locale = 18
    LongLong = 4
    Map = 8
    Matrix = 80
    Matrix4x4 = 82
    Palette = 68
    Pen = 77
    Pixmap = 65
    Point = 25
    PointF = 26
    Polygon = 71
    Quaternion = 86
    Rect = 19
    RectF = 20
    RegExp = 27
    Region = 72
    Size = 21
    SizeF = 22
    SizePolicy = 75
    String = 10
    StringList = 11
    TextFormat = 79
    TextLength = 78
    Time = 15
    Transform = 81
    UInt = 3
    ULongLong = 5
    Url = 17
    UserType = 127
    Vector2D = 83
    Vector3D = 84
    Vector4D = 85


