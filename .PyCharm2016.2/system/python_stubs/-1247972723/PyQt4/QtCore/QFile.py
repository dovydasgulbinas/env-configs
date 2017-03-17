# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QIODevice import QIODevice

class QFile(QIODevice):
    """
    QFile()
    QFile(QString)
    QFile(QObject)
    QFile(QString, QObject)
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ QFile.atEnd() -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ QFile.close() """
        pass

    def copy(self, QString, QString_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFile.copy(QString) -> bool
        QFile.copy(QString, QString) -> bool
        """
        return False

    def decodeName(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFile.decodeName(QByteArray) -> QString
        QFile.decodeName(str) -> QString
        """
        return QString

    def encodeName(self, QString): # real signature unknown; restored from __doc__
        """ QFile.encodeName(QString) -> QByteArray """
        return QByteArray

    def error(self): # real signature unknown; restored from __doc__
        """ QFile.error() -> QFile.FileError """
        pass

    def exists(self, QString=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFile.exists() -> bool
        QFile.exists(QString) -> bool
        """
        return False

    def fileEngine(self): # real signature unknown; restored from __doc__
        """ QFile.fileEngine() -> QAbstractFileEngine """
        return QAbstractFileEngine

    def fileName(self): # real signature unknown; restored from __doc__
        """ QFile.fileName() -> QString """
        return QString

    def flush(self): # real signature unknown; restored from __doc__
        """ QFile.flush() -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ QFile.handle() -> int """
        return 0

    def isSequential(self): # real signature unknown; restored from __doc__
        """ QFile.isSequential() -> bool """
        return False

    def link(self, QString, QString_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFile.link(QString) -> bool
        QFile.link(QString, QString) -> bool
        """
        return False

    def map(self, p_int, p_int_1, QFile_MemoryMapFlags_flags=None): # real signature unknown; restored from __doc__
        """ QFile.map(int, int, QFile.MemoryMapFlags flags=QFile.NoOptions) -> sip.voidptr """
        pass

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFile.open(QIODevice.OpenMode) -> bool
        QFile.open(int, QIODevice.OpenMode) -> bool
        QFile.open(int, QIODevice.OpenMode, QFile.FileHandleFlags) -> bool
        """
        return False

    def permissions(self, QString=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFile.permissions() -> QFile.Permissions
        QFile.permissions(QString) -> QFile.Permissions
        """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ QFile.pos() -> int """
        return 0

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ QFile.readData(int) -> str """
        return ""

    def readLineData(self, p_int): # real signature unknown; restored from __doc__
        """ QFile.readLineData(int) -> str """
        return ""

    def readLink(self, QString=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFile.readLink() -> QString
        QFile.readLink(QString) -> QString
        """
        return QString

    def remove(self, QString=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFile.remove() -> bool
        QFile.remove(QString) -> bool
        """
        return False

    def rename(self, QString, QString_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFile.rename(QString) -> bool
        QFile.rename(QString, QString) -> bool
        """
        return False

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFile.resize(int) -> bool
        QFile.resize(QString, int) -> bool
        """
        return False

    def seek(self, p_int): # real signature unknown; restored from __doc__
        """ QFile.seek(int) -> bool """
        return False

    def setFileName(self, QString): # real signature unknown; restored from __doc__
        """ QFile.setFileName(QString) """
        pass

    def setPermissions(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFile.setPermissions(QFile.Permissions) -> bool
        QFile.setPermissions(QString, QFile.Permissions) -> bool
        """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ QFile.size() -> int """
        return 0

    def symLinkTarget(self, QString=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFile.symLinkTarget() -> QString
        QFile.symLinkTarget(QString) -> QString
        """
        return QString

    def unmap(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ QFile.unmap(sip.voidptr) -> bool """
        return False

    def unsetError(self): # real signature unknown; restored from __doc__
        """ QFile.unsetError() """
        pass

    def writeData(self, p_str): # real signature unknown; restored from __doc__
        """ QFile.writeData(str) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AbortError = 6
    AutoCloseHandle = 1
    CopyError = 14
    DontCloseHandle = 0
    ExeGroup = 16
    ExeOther = 1
    ExeOwner = 4096
    ExeUser = 256
    FatalError = 3
    NoError = 0
    NoOptions = 0
    OpenError = 5
    PermissionsError = 13
    PositionError = 11
    ReadError = 1
    ReadGroup = 64
    ReadOther = 4
    ReadOwner = 16384
    ReadUser = 1024
    RemoveError = 9
    RenameError = 10
    ResizeError = 12
    ResourceError = 4
    TimeOutError = 7
    UnspecifiedError = 8
    WriteError = 2
    WriteGroup = 32
    WriteOther = 2
    WriteOwner = 8192
    WriteUser = 512


