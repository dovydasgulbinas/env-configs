# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QFileInfo(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QFileInfo()
    QFileInfo(QString)
    QFileInfo(QFile)
    QFileInfo(QDir, QString)
    QFileInfo(QFileInfo)
    """
    def absoluteDir(self): # real signature unknown; restored from __doc__
        """ QFileInfo.absoluteDir() -> QDir """
        return QDir

    def absoluteFilePath(self): # real signature unknown; restored from __doc__
        """ QFileInfo.absoluteFilePath() -> QString """
        return QString

    def absolutePath(self): # real signature unknown; restored from __doc__
        """ QFileInfo.absolutePath() -> QString """
        return QString

    def baseName(self): # real signature unknown; restored from __doc__
        """ QFileInfo.baseName() -> QString """
        return QString

    def bundleName(self): # real signature unknown; restored from __doc__
        """ QFileInfo.bundleName() -> QString """
        return QString

    def caching(self): # real signature unknown; restored from __doc__
        """ QFileInfo.caching() -> bool """
        return False

    def canonicalFilePath(self): # real signature unknown; restored from __doc__
        """ QFileInfo.canonicalFilePath() -> QString """
        return QString

    def canonicalPath(self): # real signature unknown; restored from __doc__
        """ QFileInfo.canonicalPath() -> QString """
        return QString

    def completeBaseName(self): # real signature unknown; restored from __doc__
        """ QFileInfo.completeBaseName() -> QString """
        return QString

    def completeSuffix(self): # real signature unknown; restored from __doc__
        """ QFileInfo.completeSuffix() -> QString """
        return QString

    def created(self): # real signature unknown; restored from __doc__
        """ QFileInfo.created() -> QDateTime """
        return QDateTime

    def dir(self): # real signature unknown; restored from __doc__
        """ QFileInfo.dir() -> QDir """
        return QDir

    def exists(self): # real signature unknown; restored from __doc__
        """ QFileInfo.exists() -> bool """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ QFileInfo.fileName() -> QString """
        return QString

    def filePath(self): # real signature unknown; restored from __doc__
        """ QFileInfo.filePath() -> QString """
        return QString

    def group(self): # real signature unknown; restored from __doc__
        """ QFileInfo.group() -> QString """
        return QString

    def groupId(self): # real signature unknown; restored from __doc__
        """ QFileInfo.groupId() -> int """
        return 0

    def isAbsolute(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isAbsolute() -> bool """
        return False

    def isBundle(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isBundle() -> bool """
        return False

    def isDir(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isDir() -> bool """
        return False

    def isExecutable(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isExecutable() -> bool """
        return False

    def isFile(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isFile() -> bool """
        return False

    def isHidden(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isHidden() -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isReadable() -> bool """
        return False

    def isRelative(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isRelative() -> bool """
        return False

    def isRoot(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isRoot() -> bool """
        return False

    def isSymLink(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isSymLink() -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isWritable() -> bool """
        return False

    def lastModified(self): # real signature unknown; restored from __doc__
        """ QFileInfo.lastModified() -> QDateTime """
        return QDateTime

    def lastRead(self): # real signature unknown; restored from __doc__
        """ QFileInfo.lastRead() -> QDateTime """
        return QDateTime

    def makeAbsolute(self): # real signature unknown; restored from __doc__
        """ QFileInfo.makeAbsolute() -> bool """
        return False

    def owner(self): # real signature unknown; restored from __doc__
        """ QFileInfo.owner() -> QString """
        return QString

    def ownerId(self): # real signature unknown; restored from __doc__
        """ QFileInfo.ownerId() -> int """
        return 0

    def path(self): # real signature unknown; restored from __doc__
        """ QFileInfo.path() -> QString """
        return QString

    def permission(self, QFile_Permissions): # real signature unknown; restored from __doc__
        """ QFileInfo.permission(QFile.Permissions) -> bool """
        return False

    def permissions(self): # real signature unknown; restored from __doc__
        """ QFileInfo.permissions() -> QFile.Permissions """
        pass

    def readLink(self): # real signature unknown; restored from __doc__
        """ QFileInfo.readLink() -> QString """
        return QString

    def refresh(self): # real signature unknown; restored from __doc__
        """ QFileInfo.refresh() """
        pass

    def setCaching(self, bool): # real signature unknown; restored from __doc__
        """ QFileInfo.setCaching(bool) """
        pass

    def setFile(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileInfo.setFile(QString)
        QFileInfo.setFile(QFile)
        QFileInfo.setFile(QDir, QString)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QFileInfo.size() -> int """
        return 0

    def suffix(self): # real signature unknown; restored from __doc__
        """ QFileInfo.suffix() -> QString """
        return QString

    def symLinkTarget(self): # real signature unknown; restored from __doc__
        """ QFileInfo.symLinkTarget() -> QString """
        return QString

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



