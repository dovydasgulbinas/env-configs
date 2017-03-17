# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QByteArray(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QByteArray()
    QByteArray(int, str)
    QByteArray(QByteArray)
    """
    def append(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QByteArray.append(QByteArray) -> QByteArray
        QByteArray.append(QString) -> QByteArray
        """
        return QByteArray

    def at(self, p_int): # real signature unknown; restored from __doc__
        """ QByteArray.at(int) -> str """
        return ""

    def capacity(self): # real signature unknown; restored from __doc__
        """ QByteArray.capacity() -> int """
        return 0

    def chop(self, p_int): # real signature unknown; restored from __doc__
        """ QByteArray.chop(int) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QByteArray.clear() """
        pass

    def contains(self, QByteArray): # real signature unknown; restored from __doc__
        """ QByteArray.contains(QByteArray) -> bool """
        return False

    def count(self, QByteArray=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QByteArray.count(QByteArray) -> int
        QByteArray.count() -> int
        """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ QByteArray.data() -> str """
        return ""

    def endsWith(self, QByteArray): # real signature unknown; restored from __doc__
        """ QByteArray.endsWith(QByteArray) -> bool """
        return False

    def fill(self, p_str, int_size=-1): # real signature unknown; restored from __doc__
        """ QByteArray.fill(str, int size=-1) -> QByteArray """
        return QByteArray

    def fromBase64(self, QByteArray): # real signature unknown; restored from __doc__
        """ QByteArray.fromBase64(QByteArray) -> QByteArray """
        return QByteArray

    def fromHex(self, QByteArray): # real signature unknown; restored from __doc__
        """ QByteArray.fromHex(QByteArray) -> QByteArray """
        return QByteArray

    def fromPercentEncoding(self, QByteArray, str_percent='%'): # real signature unknown; restored from __doc__
        """ QByteArray.fromPercentEncoding(QByteArray, str percent='%') -> QByteArray """
        return QByteArray

    def fromRawData(self, p_str): # real signature unknown; restored from __doc__
        """ QByteArray.fromRawData(str) -> QByteArray """
        return QByteArray

    def indexOf(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QByteArray.indexOf(QByteArray, int from=0) -> int
        QByteArray.indexOf(QString, int from=0) -> int
        """
        return 0

    def insert(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QByteArray.insert(int, QByteArray) -> QByteArray
        QByteArray.insert(int, QString) -> QByteArray
        """
        return QByteArray

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QByteArray.isEmpty() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QByteArray.isNull() -> bool """
        return False

    def lastIndexOf(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QByteArray.lastIndexOf(QByteArray, int from=-1) -> int
        QByteArray.lastIndexOf(QString, int from=-1) -> int
        """
        return 0

    def left(self, p_int): # real signature unknown; restored from __doc__
        """ QByteArray.left(int) -> QByteArray """
        return QByteArray

    def leftJustified(self, p_int, str_fill=' ', bool_truncate=False): # real signature unknown; restored from __doc__
        """ QByteArray.leftJustified(int, str fill=' ', bool truncate=False) -> QByteArray """
        return QByteArray

    def length(self): # real signature unknown; restored from __doc__
        """ QByteArray.length() -> int """
        return 0

    def mid(self, p_int, int_length=-1): # real signature unknown; restored from __doc__
        """ QByteArray.mid(int, int length=-1) -> QByteArray """
        return QByteArray

    def number(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QByteArray.number(int, int base=10) -> QByteArray
        QByteArray.number(float, str format='g', int precision=6) -> QByteArray
        QByteArray.number(int, int base=10) -> QByteArray
        QByteArray.number(int, int base=10) -> QByteArray
        """
        return QByteArray

    def prepend(self, QByteArray): # real signature unknown; restored from __doc__
        """ QByteArray.prepend(QByteArray) -> QByteArray """
        return QByteArray

    def push_back(self, QByteArray): # real signature unknown; restored from __doc__
        """ QByteArray.push_back(QByteArray) """
        pass

    def push_front(self, QByteArray): # real signature unknown; restored from __doc__
        """ QByteArray.push_front(QByteArray) """
        pass

    def remove(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QByteArray.remove(int, int) -> QByteArray """
        return QByteArray

    def repeated(self, p_int): # real signature unknown; restored from __doc__
        """ QByteArray.repeated(int) -> QByteArray """
        return QByteArray

    def replace(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QByteArray.replace(int, int, QByteArray) -> QByteArray
        QByteArray.replace(QByteArray, QByteArray) -> QByteArray
        QByteArray.replace(QString, QByteArray) -> QByteArray
        """
        return QByteArray

    def reserve(self, p_int): # real signature unknown; restored from __doc__
        """ QByteArray.reserve(int) """
        pass

    def resize(self, p_int): # real signature unknown; restored from __doc__
        """ QByteArray.resize(int) """
        pass

    def right(self, p_int): # real signature unknown; restored from __doc__
        """ QByteArray.right(int) -> QByteArray """
        return QByteArray

    def rightJustified(self, p_int, str_fill=' ', bool_truncate=False): # real signature unknown; restored from __doc__
        """ QByteArray.rightJustified(int, str fill=' ', bool truncate=False) -> QByteArray """
        return QByteArray

    def setNum(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QByteArray.setNum(int, int base=10) -> QByteArray
        QByteArray.setNum(float, str format='g', int precision=6) -> QByteArray
        QByteArray.setNum(int, int base=10) -> QByteArray
        QByteArray.setNum(int, int base=10) -> QByteArray
        """
        return QByteArray

    def simplified(self): # real signature unknown; restored from __doc__
        """ QByteArray.simplified() -> QByteArray """
        return QByteArray

    def size(self): # real signature unknown; restored from __doc__
        """ QByteArray.size() -> int """
        return 0

    def split(self, p_str): # real signature unknown; restored from __doc__
        """ QByteArray.split(str) -> list-of-QByteArray """
        pass

    def squeeze(self): # real signature unknown; restored from __doc__
        """ QByteArray.squeeze() """
        pass

    def startsWith(self, QByteArray): # real signature unknown; restored from __doc__
        """ QByteArray.startsWith(QByteArray) -> bool """
        return False

    def swap(self, QByteArray): # real signature unknown; restored from __doc__
        """ QByteArray.swap(QByteArray) """
        pass

    def toBase64(self): # real signature unknown; restored from __doc__
        """ QByteArray.toBase64() -> QByteArray """
        return QByteArray

    def toDouble(self): # real signature unknown; restored from __doc__
        """ QByteArray.toDouble() -> (float, bool) """
        pass

    def toFloat(self): # real signature unknown; restored from __doc__
        """ QByteArray.toFloat() -> (float, bool) """
        pass

    def toHex(self): # real signature unknown; restored from __doc__
        """ QByteArray.toHex() -> QByteArray """
        return QByteArray

    def toInt(self, int_base=10): # real signature unknown; restored from __doc__
        """ QByteArray.toInt(int base=10) -> (int, bool) """
        pass

    def toLong(self, int_base=10): # real signature unknown; restored from __doc__
        """ QByteArray.toLong(int base=10) -> (int, bool) """
        pass

    def toLongLong(self, int_base=10): # real signature unknown; restored from __doc__
        """ QByteArray.toLongLong(int base=10) -> (int, bool) """
        pass

    def toLower(self): # real signature unknown; restored from __doc__
        """ QByteArray.toLower() -> QByteArray """
        return QByteArray

    def toPercentEncoding(self, QByteArray_exclude=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QByteArray.toPercentEncoding(QByteArray exclude=QByteArray(), QByteArray include=QByteArray(), str percent='%') -> QByteArray """
        pass

    def toShort(self, int_base=10): # real signature unknown; restored from __doc__
        """ QByteArray.toShort(int base=10) -> (int, bool) """
        pass

    def toUInt(self, int_base=10): # real signature unknown; restored from __doc__
        """ QByteArray.toUInt(int base=10) -> (int, bool) """
        pass

    def toULong(self, int_base=10): # real signature unknown; restored from __doc__
        """ QByteArray.toULong(int base=10) -> (int, bool) """
        pass

    def toULongLong(self, int_base=10): # real signature unknown; restored from __doc__
        """ QByteArray.toULongLong(int base=10) -> (int, bool) """
        pass

    def toUpper(self): # real signature unknown; restored from __doc__
        """ QByteArray.toUpper() -> QByteArray """
        return QByteArray

    def toUShort(self, int_base=10): # real signature unknown; restored from __doc__
        """ QByteArray.toUShort(int base=10) -> (int, bool) """
        pass

    def trimmed(self): # real signature unknown; restored from __doc__
        """ QByteArray.trimmed() -> QByteArray """
        return QByteArray

    def truncate(self, p_int): # real signature unknown; restored from __doc__
        """ QByteArray.truncate(int) """
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __iadd__(self, y): # real signature unknown; restored from __doc__
        """ x.__iadd__(y) <==> x+=y """
        pass

    def __imul__(self, y): # real signature unknown; restored from __doc__
        """ x.__imul__(y) <==> x*=y """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



