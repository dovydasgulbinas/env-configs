# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QFileSystemWatcher(QObject):
    """
    QFileSystemWatcher(QObject parent=None)
    QFileSystemWatcher(QStringList, QObject parent=None)
    """
    def addPath(self, QString): # real signature unknown; restored from __doc__
        """ QFileSystemWatcher.addPath(QString) """
        pass

    def addPaths(self, QStringList): # real signature unknown; restored from __doc__
        """ QFileSystemWatcher.addPaths(QStringList) """
        pass

    def directories(self): # real signature unknown; restored from __doc__
        """ QFileSystemWatcher.directories() -> QStringList """
        return QStringList

    def directoryChanged(self, *args, **kwargs): # real signature unknown
        """ QFileSystemWatcher.directoryChanged[QString] [signal] """
        pass

    def fileChanged(self, *args, **kwargs): # real signature unknown
        """ QFileSystemWatcher.fileChanged[QString] [signal] """
        pass

    def files(self): # real signature unknown; restored from __doc__
        """ QFileSystemWatcher.files() -> QStringList """
        return QStringList

    def removePath(self, QString): # real signature unknown; restored from __doc__
        """ QFileSystemWatcher.removePath(QString) """
        pass

    def removePaths(self, QStringList): # real signature unknown; restored from __doc__
        """ QFileSystemWatcher.removePaths(QStringList) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


