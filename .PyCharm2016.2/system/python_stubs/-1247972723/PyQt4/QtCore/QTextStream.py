# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QTextStream(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QTextStream()
    QTextStream(QIODevice)
    QTextStream(QString, QIODevice.OpenMode mode=QIODevice.ReadWrite)
    QTextStream(QByteArray, QIODevice.OpenMode mode=QIODevice.ReadWrite)
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ QTextStream.atEnd() -> bool """
        return False

    def autoDetectUnicode(self): # real signature unknown; restored from __doc__
        """ QTextStream.autoDetectUnicode() -> bool """
        return False

    def codec(self): # real signature unknown; restored from __doc__
        """ QTextStream.codec() -> QTextCodec """
        return QTextCodec

    def device(self): # real signature unknown; restored from __doc__
        """ QTextStream.device() -> QIODevice """
        return QIODevice

    def fieldAlignment(self): # real signature unknown; restored from __doc__
        """ QTextStream.fieldAlignment() -> QTextStream.FieldAlignment """
        pass

    def fieldWidth(self): # real signature unknown; restored from __doc__
        """ QTextStream.fieldWidth() -> int """
        return 0

    def flush(self): # real signature unknown; restored from __doc__
        """ QTextStream.flush() """
        pass

    def generateByteOrderMark(self): # real signature unknown; restored from __doc__
        """ QTextStream.generateByteOrderMark() -> bool """
        return False

    def integerBase(self): # real signature unknown; restored from __doc__
        """ QTextStream.integerBase() -> int """
        return 0

    def locale(self): # real signature unknown; restored from __doc__
        """ QTextStream.locale() -> QLocale """
        return QLocale

    def numberFlags(self): # real signature unknown; restored from __doc__
        """ QTextStream.numberFlags() -> QTextStream.NumberFlags """
        pass

    def padChar(self): # real signature unknown; restored from __doc__
        """ QTextStream.padChar() -> QChar """
        return QChar

    def pos(self): # real signature unknown; restored from __doc__
        """ QTextStream.pos() -> int """
        return 0

    def read(self, p_int): # real signature unknown; restored from __doc__
        """ QTextStream.read(int) -> QString """
        return QString

    def readAll(self): # real signature unknown; restored from __doc__
        """ QTextStream.readAll() -> QString """
        return QString

    def readLine(self, int_maxLength=0): # real signature unknown; restored from __doc__
        """ QTextStream.readLine(int maxLength=0) -> QString """
        return QString

    def realNumberNotation(self): # real signature unknown; restored from __doc__
        """ QTextStream.realNumberNotation() -> QTextStream.RealNumberNotation """
        pass

    def realNumberPrecision(self): # real signature unknown; restored from __doc__
        """ QTextStream.realNumberPrecision() -> int """
        return 0

    def reset(self): # real signature unknown; restored from __doc__
        """ QTextStream.reset() """
        pass

    def resetStatus(self): # real signature unknown; restored from __doc__
        """ QTextStream.resetStatus() """
        pass

    def seek(self, p_int): # real signature unknown; restored from __doc__
        """ QTextStream.seek(int) -> bool """
        return False

    def setAutoDetectUnicode(self, bool): # real signature unknown; restored from __doc__
        """ QTextStream.setAutoDetectUnicode(bool) """
        pass

    def setCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextStream.setCodec(QTextCodec)
        QTextStream.setCodec(str)
        """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ QTextStream.setDevice(QIODevice) """
        pass

    def setFieldAlignment(self, QTextStream_FieldAlignment): # real signature unknown; restored from __doc__
        """ QTextStream.setFieldAlignment(QTextStream.FieldAlignment) """
        pass

    def setFieldWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QTextStream.setFieldWidth(int) """
        pass

    def setGenerateByteOrderMark(self, bool): # real signature unknown; restored from __doc__
        """ QTextStream.setGenerateByteOrderMark(bool) """
        pass

    def setIntegerBase(self, p_int): # real signature unknown; restored from __doc__
        """ QTextStream.setIntegerBase(int) """
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ QTextStream.setLocale(QLocale) """
        pass

    def setNumberFlags(self, QTextStream_NumberFlags): # real signature unknown; restored from __doc__
        """ QTextStream.setNumberFlags(QTextStream.NumberFlags) """
        pass

    def setPadChar(self, QChar): # real signature unknown; restored from __doc__
        """ QTextStream.setPadChar(QChar) """
        pass

    def setRealNumberNotation(self, QTextStream_RealNumberNotation): # real signature unknown; restored from __doc__
        """ QTextStream.setRealNumberNotation(QTextStream.RealNumberNotation) """
        pass

    def setRealNumberPrecision(self, p_int): # real signature unknown; restored from __doc__
        """ QTextStream.setRealNumberPrecision(int) """
        pass

    def setStatus(self, QTextStream_Status): # real signature unknown; restored from __doc__
        """ QTextStream.setStatus(QTextStream.Status) """
        pass

    def setString(self, QString, QIODevice_OpenMode_mode=None): # real signature unknown; restored from __doc__
        """ QTextStream.setString(QString, QIODevice.OpenMode mode=QIODevice.ReadWrite) """
        pass

    def skipWhiteSpace(self): # real signature unknown; restored from __doc__
        """ QTextStream.skipWhiteSpace() """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ QTextStream.status() -> QTextStream.Status """
        pass

    def string(self): # real signature unknown; restored from __doc__
        """ QTextStream.string() -> QString """
        return QString

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __lshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__lshift__(y) <==> x<<y """
        pass

    def __rlshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rlshift__(y) <==> y<<x """
        pass

    def __rrshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rrshift__(y) <==> y>>x """
        pass

    def __rshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rshift__(y) <==> x>>y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AlignAccountingStyle = 3
    AlignCenter = 2
    AlignLeft = 0
    AlignRight = 1
    FixedNotation = 1
    ForcePoint = 2
    ForceSign = 4
    Ok = 0
    ReadCorruptData = 2
    ReadPastEnd = 1
    ScientificNotation = 2
    ShowBase = 1
    SmartNotation = 0
    UppercaseBase = 8
    UppercaseDigits = 16
    WriteFailed = 3


