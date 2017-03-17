# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QAbstractFileEngine import QAbstractFileEngine

class QFSFileEngine(QAbstractFileEngine):
    """
    QFSFileEngine()
    QFSFileEngine(QString)
    """
    def caseSensitive(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.caseSensitive() -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.close() -> bool """
        return False

    def copy(self, QString): # real signature unknown; restored from __doc__
        """ QFSFileEngine.copy(QString) -> bool """
        return False

    def currentPath(self, QString_fileName=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFSFileEngine.currentPath(QString fileName=QString()) -> QString """
        pass

    def drives(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.drives() -> list-of-QFileInfo """
        pass

    def entryList(self, QDir_Filters, QStringList): # real signature unknown; restored from __doc__
        """ QFSFileEngine.entryList(QDir.Filters, QStringList) -> QStringList """
        return QStringList

    def fileFlags(self, QAbstractFileEngine_FileFlags): # real signature unknown; restored from __doc__
        """ QFSFileEngine.fileFlags(QAbstractFileEngine.FileFlags) -> QAbstractFileEngine.FileFlags """
        pass

    def fileName(self, QAbstractFileEngine_FileName): # real signature unknown; restored from __doc__
        """ QFSFileEngine.fileName(QAbstractFileEngine.FileName) -> QString """
        return QString

    def fileTime(self, QAbstractFileEngine_FileTime): # real signature unknown; restored from __doc__
        """ QFSFileEngine.fileTime(QAbstractFileEngine.FileTime) -> QDateTime """
        return QDateTime

    def flush(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.flush() -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.handle() -> int """
        return 0

    def homePath(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.homePath() -> QString """
        return QString

    def isRelativePath(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.isRelativePath() -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.isSequential() -> bool """
        return False

    def link(self, QString): # real signature unknown; restored from __doc__
        """ QFSFileEngine.link(QString) -> bool """
        return False

    def mkdir(self, QString, bool): # real signature unknown; restored from __doc__
        """ QFSFileEngine.mkdir(QString, bool) -> bool """
        return False

    def open(self, QIODevice_OpenMode, p_int=None, QFile_FileHandleFlags=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFSFileEngine.open(QIODevice.OpenMode) -> bool
        QFSFileEngine.open(QIODevice.OpenMode, int, QFile.FileHandleFlags) -> bool
        QFSFileEngine.open(QIODevice.OpenMode, int) -> bool
        """
        return False

    def owner(self, QAbstractFileEngine_FileOwner): # real signature unknown; restored from __doc__
        """ QFSFileEngine.owner(QAbstractFileEngine.FileOwner) -> QString """
        return QString

    def ownerId(self, QAbstractFileEngine_FileOwner): # real signature unknown; restored from __doc__
        """ QFSFileEngine.ownerId(QAbstractFileEngine.FileOwner) -> int """
        return 0

    def pos(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.pos() -> int """
        return 0

    def read(self, p_int): # real signature unknown; restored from __doc__
        """ QFSFileEngine.read(int) -> str """
        return ""

    def readLine(self, p_int): # real signature unknown; restored from __doc__
        """ QFSFileEngine.readLine(int) -> str """
        return ""

    def remove(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.remove() -> bool """
        return False

    def rename(self, QString): # real signature unknown; restored from __doc__
        """ QFSFileEngine.rename(QString) -> bool """
        return False

    def rmdir(self, QString, bool): # real signature unknown; restored from __doc__
        """ QFSFileEngine.rmdir(QString, bool) -> bool """
        return False

    def rootPath(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.rootPath() -> QString """
        return QString

    def seek(self, p_int): # real signature unknown; restored from __doc__
        """ QFSFileEngine.seek(int) -> bool """
        return False

    def setCurrentPath(self, QString): # real signature unknown; restored from __doc__
        """ QFSFileEngine.setCurrentPath(QString) -> bool """
        return False

    def setFileName(self, QString): # real signature unknown; restored from __doc__
        """ QFSFileEngine.setFileName(QString) """
        pass

    def setPermissions(self, p_int): # real signature unknown; restored from __doc__
        """ QFSFileEngine.setPermissions(int) -> bool """
        return False

    def setSize(self, p_int): # real signature unknown; restored from __doc__
        """ QFSFileEngine.setSize(int) -> bool """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.size() -> int """
        return 0

    def tempPath(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.tempPath() -> QString """
        return QString

    def write(self, p_str): # real signature unknown; restored from __doc__
        """ QFSFileEngine.write(str) -> int """
        return 0

    def __init__(self, QString=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass


