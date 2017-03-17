# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QDirIterator(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDirIterator(QDir, QDirIterator.IteratorFlags flags=QDirIterator.NoIteratorFlags)
    QDirIterator(QString, QDirIterator.IteratorFlags flags=QDirIterator.NoIteratorFlags)
    QDirIterator(QString, QDir.Filters, QDirIterator.IteratorFlags flags=QDirIterator.NoIteratorFlags)
    QDirIterator(QString, QStringList, QDir.Filters filters=QDir.NoFilter, QDirIterator.IteratorFlags flags=QDirIterator.NoIteratorFlags)
    """
    def fileInfo(self): # real signature unknown; restored from __doc__
        """ QDirIterator.fileInfo() -> QFileInfo """
        return QFileInfo

    def fileName(self): # real signature unknown; restored from __doc__
        """ QDirIterator.fileName() -> QString """
        return QString

    def filePath(self): # real signature unknown; restored from __doc__
        """ QDirIterator.filePath() -> QString """
        return QString

    def hasNext(self): # real signature unknown; restored from __doc__
        """ QDirIterator.hasNext() -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ QDirIterator.next() -> QString """
        return QString

    def path(self): # real signature unknown; restored from __doc__
        """ QDirIterator.path() -> QString """
        return QString

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FollowSymlinks = 1
    NoIteratorFlags = 0
    Subdirectories = 2


