# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QDir(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDir(QDir)
    QDir(QString path=QString())
    QDir(QString, QString, QDir.SortFlags sort=QDir.Name|QDir.IgnoreCase, QDir.Filters filters=QDir.AllEntries)
    """
    def absoluteFilePath(self, QString): # real signature unknown; restored from __doc__
        """ QDir.absoluteFilePath(QString) -> QString """
        return QString

    def absolutePath(self): # real signature unknown; restored from __doc__
        """ QDir.absolutePath() -> QString """
        return QString

    def addResourceSearchPath(self, QString): # real signature unknown; restored from __doc__
        """ QDir.addResourceSearchPath(QString) """
        pass

    def addSearchPath(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDir.addSearchPath(QString, QString) """
        pass

    def canonicalPath(self): # real signature unknown; restored from __doc__
        """ QDir.canonicalPath() -> QString """
        return QString

    def cd(self, QString): # real signature unknown; restored from __doc__
        """ QDir.cd(QString) -> bool """
        return False

    def cdUp(self): # real signature unknown; restored from __doc__
        """ QDir.cdUp() -> bool """
        return False

    def cleanPath(self, QString): # real signature unknown; restored from __doc__
        """ QDir.cleanPath(QString) -> QString """
        return QString

    def convertSeparators(self, QString): # real signature unknown; restored from __doc__
        """ QDir.convertSeparators(QString) -> QString """
        return QString

    def count(self): # real signature unknown; restored from __doc__
        """ QDir.count() -> int """
        return 0

    def current(self): # real signature unknown; restored from __doc__
        """ QDir.current() -> QDir """
        return QDir

    def currentPath(self): # real signature unknown; restored from __doc__
        """ QDir.currentPath() -> QString """
        return QString

    def dirName(self): # real signature unknown; restored from __doc__
        """ QDir.dirName() -> QString """
        return QString

    def drives(self): # real signature unknown; restored from __doc__
        """ QDir.drives() -> list-of-QFileInfo """
        pass

    def entryInfoList(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDir.entryInfoList(QDir.Filters filters=QDir.NoFilter, QDir.SortFlags sort=QDir.NoSort) -> list-of-QFileInfo
        QDir.entryInfoList(QStringList, QDir.Filters filters=QDir.NoFilter, QDir.SortFlags sort=QDir.NoSort) -> list-of-QFileInfo
        """
        pass

    def entryList(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDir.entryList(QDir.Filters filters=QDir.NoFilter, QDir.SortFlags sort=QDir.NoSort) -> QStringList
        QDir.entryList(QStringList, QDir.Filters filters=QDir.NoFilter, QDir.SortFlags sort=QDir.NoSort) -> QStringList
        """
        return QStringList

    def exists(self, QString=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDir.exists() -> bool
        QDir.exists(QString) -> bool
        """
        return False

    def filePath(self, QString): # real signature unknown; restored from __doc__
        """ QDir.filePath(QString) -> QString """
        return QString

    def filter(self): # real signature unknown; restored from __doc__
        """ QDir.filter() -> QDir.Filters """
        pass

    def fromNativeSeparators(self, QString): # real signature unknown; restored from __doc__
        """ QDir.fromNativeSeparators(QString) -> QString """
        return QString

    def home(self): # real signature unknown; restored from __doc__
        """ QDir.home() -> QDir """
        return QDir

    def homePath(self): # real signature unknown; restored from __doc__
        """ QDir.homePath() -> QString """
        return QString

    def isAbsolute(self): # real signature unknown; restored from __doc__
        """ QDir.isAbsolute() -> bool """
        return False

    def isAbsolutePath(self, QString): # real signature unknown; restored from __doc__
        """ QDir.isAbsolutePath(QString) -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ QDir.isReadable() -> bool """
        return False

    def isRelative(self): # real signature unknown; restored from __doc__
        """ QDir.isRelative() -> bool """
        return False

    def isRelativePath(self, QString): # real signature unknown; restored from __doc__
        """ QDir.isRelativePath(QString) -> bool """
        return False

    def isRoot(self): # real signature unknown; restored from __doc__
        """ QDir.isRoot() -> bool """
        return False

    def makeAbsolute(self): # real signature unknown; restored from __doc__
        """ QDir.makeAbsolute() -> bool """
        return False

    def match(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDir.match(QStringList, QString) -> bool
        QDir.match(QString, QString) -> bool
        """
        return False

    def mkdir(self, QString): # real signature unknown; restored from __doc__
        """ QDir.mkdir(QString) -> bool """
        return False

    def mkpath(self, QString): # real signature unknown; restored from __doc__
        """ QDir.mkpath(QString) -> bool """
        return False

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ QDir.nameFilters() -> QStringList """
        return QStringList

    def nameFiltersFromString(self, QString): # real signature unknown; restored from __doc__
        """ QDir.nameFiltersFromString(QString) -> QStringList """
        return QStringList

    def path(self): # real signature unknown; restored from __doc__
        """ QDir.path() -> QString """
        return QString

    def refresh(self): # real signature unknown; restored from __doc__
        """ QDir.refresh() """
        pass

    def relativeFilePath(self, QString): # real signature unknown; restored from __doc__
        """ QDir.relativeFilePath(QString) -> QString """
        return QString

    def remove(self, QString): # real signature unknown; restored from __doc__
        """ QDir.remove(QString) -> bool """
        return False

    def rename(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDir.rename(QString, QString) -> bool """
        return False

    def rmdir(self, QString): # real signature unknown; restored from __doc__
        """ QDir.rmdir(QString) -> bool """
        return False

    def rmpath(self, QString): # real signature unknown; restored from __doc__
        """ QDir.rmpath(QString) -> bool """
        return False

    def root(self): # real signature unknown; restored from __doc__
        """ QDir.root() -> QDir """
        return QDir

    def rootPath(self): # real signature unknown; restored from __doc__
        """ QDir.rootPath() -> QString """
        return QString

    def searchPaths(self, QString): # real signature unknown; restored from __doc__
        """ QDir.searchPaths(QString) -> QStringList """
        return QStringList

    def separator(self): # real signature unknown; restored from __doc__
        """ QDir.separator() -> QChar """
        return QChar

    def setCurrent(self, QString): # real signature unknown; restored from __doc__
        """ QDir.setCurrent(QString) -> bool """
        return False

    def setFilter(self, QDir_Filters): # real signature unknown; restored from __doc__
        """ QDir.setFilter(QDir.Filters) """
        pass

    def setNameFilters(self, QStringList): # real signature unknown; restored from __doc__
        """ QDir.setNameFilters(QStringList) """
        pass

    def setPath(self, QString): # real signature unknown; restored from __doc__
        """ QDir.setPath(QString) """
        pass

    def setSearchPaths(self, QString, QStringList): # real signature unknown; restored from __doc__
        """ QDir.setSearchPaths(QString, QStringList) """
        pass

    def setSorting(self, QDir_SortFlags): # real signature unknown; restored from __doc__
        """ QDir.setSorting(QDir.SortFlags) """
        pass

    def sorting(self): # real signature unknown; restored from __doc__
        """ QDir.sorting() -> QDir.SortFlags """
        pass

    def temp(self): # real signature unknown; restored from __doc__
        """ QDir.temp() -> QDir """
        return QDir

    def tempPath(self): # real signature unknown; restored from __doc__
        """ QDir.tempPath() -> QString """
        return QString

    def toNativeSeparators(self, QString): # real signature unknown; restored from __doc__
        """ QDir.toNativeSeparators(QString) -> QString """
        return QString

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

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccessMask = 1008
    AllDirs = 1024
    AllEntries = 7
    CaseSensitive = 2048
    Dirs = 1
    DirsFirst = 4
    DirsLast = 32
    Drives = 4
    Executable = 64
    Files = 2
    Hidden = 256
    IgnoreCase = 16
    LocaleAware = 64
    Modified = 128
    Name = 0
    NoDot = 8192
    NoDotAndDotDot = 4096
    NoDotDot = 16384
    NoFilter = -1
    NoSort = -1
    NoSymLinks = 8
    PermissionMask = 112
    Readable = 16
    Reversed = 8
    Size = 2
    SortByMask = 3
    System = 512
    Time = 1
    Type = 128
    TypeMask = 15
    Unsorted = 3
    Writable = 32


