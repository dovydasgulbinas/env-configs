# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QString(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QString()
    QString(int, QChar)
    QString(QString)
    QString(QByteArray)
    QString(QUuid)
    """
    def append(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.append(QString) -> QString
        QString.append(QLatin1String) -> QString
        QString.append(QByteArray) -> QString
        """
        return QString

    def arg(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.arg(int, int fieldWidth=0, int base=10, QChar fillChar=QLatin1Char(' ')) -> QString
        QString.arg(float, int fieldWidth=0, str format='g', int precision=-1, QChar fillChar=QLatin1Char(' ')) -> QString
        QString.arg(int, int fieldWidth=0, int base=10, QChar fillChar=QLatin1Char(' ')) -> QString
        QString.arg(int, int fieldWidth=0, int base=10, QChar fillChar=QLatin1Char(' ')) -> QString
        QString.arg(QString, int fieldWidth=0, QChar fillChar=QLatin1Char(' ')) -> QString
        QString.arg(QString, QString) -> QString
        QString.arg(QString, QString, QString) -> QString
        QString.arg(QString, QString, QString, QString) -> QString
        QString.arg(QString, QString, QString, QString, QString) -> QString
        QString.arg(QString, QString, QString, QString, QString, QString) -> QString
        QString.arg(QString, QString, QString, QString, QString, QString, QString) -> QString
        QString.arg(QString, QString, QString, QString, QString, QString, QString, QString) -> QString
        QString.arg(QString, QString, QString, QString, QString, QString, QString, QString, QString) -> QString
        """
        return QString

    def at(self, p_int): # real signature unknown; restored from __doc__
        """ QString.at(int) -> QChar """
        return QChar

    def capacity(self): # real signature unknown; restored from __doc__
        """ QString.capacity() -> int """
        return 0

    def chop(self, p_int): # real signature unknown; restored from __doc__
        """ QString.chop(int) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QString.clear() """
        pass

    def compare(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.compare(QString) -> int
        QString.compare(QString, Qt.CaseSensitivity) -> int
        QString.compare(QLatin1String, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        QString.compare(QStringRef, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        QString.compare(QString, QString) -> int
        QString.compare(QString, QString, Qt.CaseSensitivity) -> int
        QString.compare(QString, QLatin1String, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        QString.compare(QLatin1String, QString, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        QString.compare(QString, QStringRef, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        """
        return 0

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.contains(QString, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> bool
        QString.contains(QStringRef, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> bool
        QString.contains(QRegExp) -> bool
        """
        return False

    def count(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.count() -> int
        QString.count(QString, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        QString.count(QStringRef, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        QString.count(QRegExp) -> int
        """
        return 0

    def endsWith(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.endsWith(QString, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> bool
        QString.endsWith(QStringRef, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> bool
        QString.endsWith(QLatin1String, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> bool
        """
        return False

    def fill(self, QChar, int_size=-1): # real signature unknown; restored from __doc__
        """ QString.fill(QChar, int size=-1) -> QString """
        return QString

    def fromAscii(self, p_str, int_size=-1): # real signature unknown; restored from __doc__
        """ QString.fromAscii(str, int size=-1) -> QString """
        return QString

    def fromLatin1(self, p_str, int_size=-1): # real signature unknown; restored from __doc__
        """ QString.fromLatin1(str, int size=-1) -> QString """
        return QString

    def fromLocal8Bit(self, p_str, int_size=-1): # real signature unknown; restored from __doc__
        """ QString.fromLocal8Bit(str, int size=-1) -> QString """
        return QString

    def fromUtf8(self, p_str, int_size=-1): # real signature unknown; restored from __doc__
        """ QString.fromUtf8(str, int size=-1) -> QString """
        return QString

    def indexOf(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.indexOf(QString, int from=0, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        QString.indexOf(QStringRef, int from=0, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        QString.indexOf(QLatin1String, int from=0, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        QString.indexOf(QRegExp, int from=0) -> int
        """
        return 0

    def insert(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.insert(int, QString) -> QString
        QString.insert(int, QLatin1String) -> QString
        """
        return QString

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QString.isEmpty() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QString.isNull() -> bool """
        return False

    def isRightToLeft(self): # real signature unknown; restored from __doc__
        """ QString.isRightToLeft() -> bool """
        return False

    def isSimpleText(self): # real signature unknown; restored from __doc__
        """ QString.isSimpleText() -> bool """
        return False

    def lastIndexOf(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.lastIndexOf(QString, int from=-1, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        QString.lastIndexOf(QStringRef, int from=-1, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        QString.lastIndexOf(QLatin1String, int from=-1, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> int
        QString.lastIndexOf(QRegExp, int from=-1) -> int
        """
        return 0

    def left(self, p_int): # real signature unknown; restored from __doc__
        """ QString.left(int) -> QString """
        return QString

    def leftJustified(self, p_int, QChar_fillChar=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QString.leftJustified(int, QChar fillChar=QLatin1Char(' '), bool truncate=False) -> QString """
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ QString.length() -> int """
        return 0

    def localeAwareCompare(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.localeAwareCompare(QString) -> int
        QString.localeAwareCompare(QStringRef) -> int
        QString.localeAwareCompare(QString, QString) -> int
        QString.localeAwareCompare(QString, QStringRef) -> int
        """
        return 0

    def mid(self, p_int, int_n=-1): # real signature unknown; restored from __doc__
        """ QString.mid(int, int n=-1) -> QString """
        return QString

    def normalized(self, QString_NormalizationForm, QChar_UnicodeVersion=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.normalized(QString.NormalizationForm) -> QString
        QString.normalized(QString.NormalizationForm, QChar.UnicodeVersion) -> QString
        """
        return QString

    def number(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.number(int, int base=10) -> QString
        QString.number(float, str format='g', int precision=6) -> QString
        QString.number(int, int base=10) -> QString
        QString.number(int, int base=10) -> QString
        """
        return QString

    def prepend(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.prepend(QString) -> QString
        QString.prepend(QLatin1String) -> QString
        QString.prepend(QByteArray) -> QString
        """
        return QString

    def push_back(self, QString): # real signature unknown; restored from __doc__
        """ QString.push_back(QString) """
        pass

    def push_front(self, QString): # real signature unknown; restored from __doc__
        """ QString.push_front(QString) """
        pass

    def remove(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.remove(int, int) -> QString
        QString.remove(QString, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> QString
        QString.remove(QRegExp) -> QString
        """
        return QString

    def repeated(self, p_int): # real signature unknown; restored from __doc__
        """ QString.repeated(int) -> QString """
        return QString

    def replace(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.replace(int, int, QString) -> QString
        QString.replace(QString, QString, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> QString
        QString.replace(QRegExp, QString) -> QString
        QString.replace(QLatin1String, QLatin1String, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> QString
        QString.replace(QLatin1String, QString, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> QString
        QString.replace(QString, QLatin1String, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> QString
        """
        return QString

    def reserve(self, p_int): # real signature unknown; restored from __doc__
        """ QString.reserve(int) """
        pass

    def resize(self, p_int): # real signature unknown; restored from __doc__
        """ QString.resize(int) """
        pass

    def right(self, p_int): # real signature unknown; restored from __doc__
        """ QString.right(int) -> QString """
        return QString

    def rightJustified(self, p_int, QChar_fillChar=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QString.rightJustified(int, QChar fillChar=QLatin1Char(' '), bool truncate=False) -> QString """
        pass

    def section(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.section(QString, int, int end=-1, QString.SectionFlags flags=QString.SectionDefault) -> QString
        QString.section(QRegExp, int, int end=-1, QString.SectionFlags flags=QString.SectionDefault) -> QString
        """
        return QString

    def setNum(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.setNum(int, int base=10) -> QString
        QString.setNum(float, str format='g', int precision=6) -> QString
        QString.setNum(int, int base=10) -> QString
        QString.setNum(int, int base=10) -> QString
        """
        return QString

    def simplified(self): # real signature unknown; restored from __doc__
        """ QString.simplified() -> QString """
        return QString

    def size(self): # real signature unknown; restored from __doc__
        """ QString.size() -> int """
        return 0

    def split(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.split(QString, QString.SplitBehavior behavior=QString.KeepEmptyParts, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> QStringList
        QString.split(QRegExp, QString.SplitBehavior behavior=QString.KeepEmptyParts) -> QStringList
        """
        return QStringList

    def squeeze(self): # real signature unknown; restored from __doc__
        """ QString.squeeze() """
        pass

    def startsWith(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QString.startsWith(QString, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> bool
        QString.startsWith(QStringRef, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> bool
        QString.startsWith(QLatin1String, Qt.CaseSensitivity cs=Qt.CaseSensitive) -> bool
        """
        return False

    def swap(self, QString): # real signature unknown; restored from __doc__
        """ QString.swap(QString) """
        pass

    def toAscii(self): # real signature unknown; restored from __doc__
        """ QString.toAscii() -> QByteArray """
        return QByteArray

    def toCaseFolded(self): # real signature unknown; restored from __doc__
        """ QString.toCaseFolded() -> QString """
        return QString

    def toDouble(self): # real signature unknown; restored from __doc__
        """ QString.toDouble() -> (float, bool) """
        pass

    def toFloat(self): # real signature unknown; restored from __doc__
        """ QString.toFloat() -> (float, bool) """
        pass

    def toInt(self, int_base=10): # real signature unknown; restored from __doc__
        """ QString.toInt(int base=10) -> (int, bool) """
        pass

    def toLatin1(self): # real signature unknown; restored from __doc__
        """ QString.toLatin1() -> QByteArray """
        return QByteArray

    def toLocal8Bit(self): # real signature unknown; restored from __doc__
        """ QString.toLocal8Bit() -> QByteArray """
        return QByteArray

    def toLong(self, int_base=10): # real signature unknown; restored from __doc__
        """ QString.toLong(int base=10) -> (int, bool) """
        pass

    def toLongLong(self, int_base=10): # real signature unknown; restored from __doc__
        """ QString.toLongLong(int base=10) -> (int, bool) """
        pass

    def toLower(self): # real signature unknown; restored from __doc__
        """ QString.toLower() -> QString """
        return QString

    def toShort(self, int_base=10): # real signature unknown; restored from __doc__
        """ QString.toShort(int base=10) -> (int, bool) """
        pass

    def toUInt(self, int_base=10): # real signature unknown; restored from __doc__
        """ QString.toUInt(int base=10) -> (int, bool) """
        pass

    def toULong(self, int_base=10): # real signature unknown; restored from __doc__
        """ QString.toULong(int base=10) -> (int, bool) """
        pass

    def toULongLong(self, int_base=10): # real signature unknown; restored from __doc__
        """ QString.toULongLong(int base=10) -> (int, bool) """
        pass

    def toUpper(self): # real signature unknown; restored from __doc__
        """ QString.toUpper() -> QString """
        return QString

    def toUShort(self, int_base=10): # real signature unknown; restored from __doc__
        """ QString.toUShort(int base=10) -> (int, bool) """
        pass

    def toUtf8(self): # real signature unknown; restored from __doc__
        """ QString.toUtf8() -> QByteArray """
        return QByteArray

    def trimmed(self): # real signature unknown; restored from __doc__
        """ QString.trimmed() -> QString """
        return QString

    def truncate(self, p_int): # real signature unknown; restored from __doc__
        """ QString.truncate(int) """
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


    KeepEmptyParts = 0
    NormalizationForm_C = 1
    NormalizationForm_D = 0
    NormalizationForm_KC = 3
    NormalizationForm_KD = 2
    SectionCaseInsensitiveSeps = 8
    SectionDefault = 0
    SectionIncludeLeadingSep = 2
    SectionIncludeTrailingSep = 4
    SectionSkipEmpty = 1
    SkipEmptyParts = 1


