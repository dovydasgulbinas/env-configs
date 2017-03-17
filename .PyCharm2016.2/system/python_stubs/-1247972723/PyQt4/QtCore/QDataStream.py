# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QDataStream(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDataStream()
    QDataStream(QIODevice)
    QDataStream(QByteArray, QIODevice.OpenMode)
    QDataStream(QByteArray)
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ QDataStream.atEnd() -> bool """
        return False

    def byteOrder(self): # real signature unknown; restored from __doc__
        """ QDataStream.byteOrder() -> QDataStream.ByteOrder """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ QDataStream.device() -> QIODevice """
        return QIODevice

    def floatingPointPrecision(self): # real signature unknown; restored from __doc__
        """ QDataStream.floatingPointPrecision() -> QDataStream.FloatingPointPrecision """
        pass

    def readBool(self): # real signature unknown; restored from __doc__
        """ QDataStream.readBool() -> bool """
        return False

    def readBytes(self): # real signature unknown; restored from __doc__
        """ QDataStream.readBytes() -> str """
        return ""

    def readDouble(self): # real signature unknown; restored from __doc__
        """ QDataStream.readDouble() -> float """
        return 0.0

    def readFloat(self): # real signature unknown; restored from __doc__
        """ QDataStream.readFloat() -> float """
        return 0.0

    def readInt(self): # real signature unknown; restored from __doc__
        """ QDataStream.readInt() -> int """
        return 0

    def readInt16(self): # real signature unknown; restored from __doc__
        """ QDataStream.readInt16() -> int """
        return 0

    def readInt32(self): # real signature unknown; restored from __doc__
        """ QDataStream.readInt32() -> int """
        return 0

    def readInt64(self): # real signature unknown; restored from __doc__
        """ QDataStream.readInt64() -> int """
        return 0

    def readInt8(self): # real signature unknown; restored from __doc__
        """ QDataStream.readInt8() -> str """
        return ""

    def readQString(self): # real signature unknown; restored from __doc__
        """ QDataStream.readQString() -> QString """
        return QString

    def readQStringList(self): # real signature unknown; restored from __doc__
        """ QDataStream.readQStringList() -> QStringList """
        return QStringList

    def readQVariant(self): # real signature unknown; restored from __doc__
        """ QDataStream.readQVariant() -> QVariant """
        return QVariant

    def readQVariantHash(self): # real signature unknown; restored from __doc__
        """ QDataStream.readQVariantHash() -> dict-of-QString-QVariant """
        pass

    def readQVariantList(self): # real signature unknown; restored from __doc__
        """ QDataStream.readQVariantList() -> list-of-QVariant """
        pass

    def readQVariantMap(self): # real signature unknown; restored from __doc__
        """ QDataStream.readQVariantMap() -> dict-of-QString-QVariant """
        pass

    def readRawData(self, p_int): # real signature unknown; restored from __doc__
        """ QDataStream.readRawData(int) -> str """
        return ""

    def readString(self): # real signature unknown; restored from __doc__
        """ QDataStream.readString() -> str """
        return ""

    def readUInt16(self): # real signature unknown; restored from __doc__
        """ QDataStream.readUInt16() -> int """
        return 0

    def readUInt32(self): # real signature unknown; restored from __doc__
        """ QDataStream.readUInt32() -> int """
        return 0

    def readUInt64(self): # real signature unknown; restored from __doc__
        """ QDataStream.readUInt64() -> int """
        return 0

    def readUInt8(self): # real signature unknown; restored from __doc__
        """ QDataStream.readUInt8() -> str """
        return ""

    def resetStatus(self): # real signature unknown; restored from __doc__
        """ QDataStream.resetStatus() """
        pass

    def setByteOrder(self, QDataStream_ByteOrder): # real signature unknown; restored from __doc__
        """ QDataStream.setByteOrder(QDataStream.ByteOrder) """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ QDataStream.setDevice(QIODevice) """
        pass

    def setFloatingPointPrecision(self, QDataStream_FloatingPointPrecision): # real signature unknown; restored from __doc__
        """ QDataStream.setFloatingPointPrecision(QDataStream.FloatingPointPrecision) """
        pass

    def setStatus(self, QDataStream_Status): # real signature unknown; restored from __doc__
        """ QDataStream.setStatus(QDataStream.Status) """
        pass

    def setVersion(self, p_int): # real signature unknown; restored from __doc__
        """ QDataStream.setVersion(int) """
        pass

    def skipRawData(self, p_int): # real signature unknown; restored from __doc__
        """ QDataStream.skipRawData(int) -> int """
        return 0

    def status(self): # real signature unknown; restored from __doc__
        """ QDataStream.status() -> QDataStream.Status """
        pass

    def unsetDevice(self): # real signature unknown; restored from __doc__
        """ QDataStream.unsetDevice() """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ QDataStream.version() -> int """
        return 0

    def writeBool(self, bool): # real signature unknown; restored from __doc__
        """ QDataStream.writeBool(bool) """
        pass

    def writeBytes(self, p_str): # real signature unknown; restored from __doc__
        """ QDataStream.writeBytes(str) -> QDataStream """
        return QDataStream

    def writeDouble(self, p_float): # real signature unknown; restored from __doc__
        """ QDataStream.writeDouble(float) """
        pass

    def writeFloat(self, p_float): # real signature unknown; restored from __doc__
        """ QDataStream.writeFloat(float) """
        pass

    def writeInt(self, p_int): # real signature unknown; restored from __doc__
        """ QDataStream.writeInt(int) """
        pass

    def writeInt16(self, p_int): # real signature unknown; restored from __doc__
        """ QDataStream.writeInt16(int) """
        pass

    def writeInt32(self, p_int): # real signature unknown; restored from __doc__
        """ QDataStream.writeInt32(int) """
        pass

    def writeInt64(self, p_int): # real signature unknown; restored from __doc__
        """ QDataStream.writeInt64(int) """
        pass

    def writeInt8(self, p_str): # real signature unknown; restored from __doc__
        """ QDataStream.writeInt8(str) """
        pass

    def writeQString(self, QString): # real signature unknown; restored from __doc__
        """ QDataStream.writeQString(QString) """
        pass

    def writeQStringList(self, QStringList): # real signature unknown; restored from __doc__
        """ QDataStream.writeQStringList(QStringList) """
        pass

    def writeQVariant(self, QVariant): # real signature unknown; restored from __doc__
        """ QDataStream.writeQVariant(QVariant) """
        pass

    def writeQVariantHash(self, dict_of_QString_QVariant): # real signature unknown; restored from __doc__
        """ QDataStream.writeQVariantHash(dict-of-QString-QVariant) """
        pass

    def writeQVariantList(self, list_of_QVariant): # real signature unknown; restored from __doc__
        """ QDataStream.writeQVariantList(list-of-QVariant) """
        pass

    def writeQVariantMap(self, dict_of_QString_QVariant): # real signature unknown; restored from __doc__
        """ QDataStream.writeQVariantMap(dict-of-QString-QVariant) """
        pass

    def writeRawData(self, p_str): # real signature unknown; restored from __doc__
        """ QDataStream.writeRawData(str) -> int """
        return 0

    def writeString(self, p_str): # real signature unknown; restored from __doc__
        """ QDataStream.writeString(str) """
        pass

    def writeUInt16(self, p_int): # real signature unknown; restored from __doc__
        """ QDataStream.writeUInt16(int) """
        pass

    def writeUInt32(self, p_int): # real signature unknown; restored from __doc__
        """ QDataStream.writeUInt32(int) """
        pass

    def writeUInt64(self, p_int): # real signature unknown; restored from __doc__
        """ QDataStream.writeUInt64(int) """
        pass

    def writeUInt8(self, p_str): # real signature unknown; restored from __doc__
        """ QDataStream.writeUInt8(str) """
        pass

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


    BigEndian = 0
    DoublePrecision = 1
    LittleEndian = 1
    Ok = 0
    Qt_1_0 = 1
    Qt_2_0 = 2
    Qt_2_1 = 3
    Qt_3_0 = 4
    Qt_3_1 = 5
    Qt_3_3 = 6
    Qt_4_0 = 7
    Qt_4_1 = 7
    Qt_4_2 = 8
    Qt_4_3 = 9
    Qt_4_4 = 10
    Qt_4_5 = 11
    Qt_4_6 = 12
    Qt_4_7 = 12
    Qt_4_8 = 12
    ReadCorruptData = 2
    ReadPastEnd = 1
    SinglePrecision = 0
    WriteFailed = 3


