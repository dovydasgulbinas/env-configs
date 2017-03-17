# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QFile import QFile

class QTemporaryFile(QFile):
    """
    QTemporaryFile()
    QTemporaryFile(QString)
    QTemporaryFile(QObject)
    QTemporaryFile(QString, QObject)
    """
    def autoRemove(self): # real signature unknown; restored from __doc__
        """ QTemporaryFile.autoRemove() -> bool """
        return False

    def createLocalFile(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTemporaryFile.createLocalFile(QString) -> QTemporaryFile
        QTemporaryFile.createLocalFile(QFile) -> QTemporaryFile
        """
        return QTemporaryFile

    def fileEngine(self): # real signature unknown; restored from __doc__
        """ QTemporaryFile.fileEngine() -> QAbstractFileEngine """
        return QAbstractFileEngine

    def fileName(self): # real signature unknown; restored from __doc__
        """ QTemporaryFile.fileName() -> QString """
        return QString

    def fileTemplate(self): # real signature unknown; restored from __doc__
        """ QTemporaryFile.fileTemplate() -> QString """
        return QString

    def open(self, QIODevice_OpenMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTemporaryFile.open() -> bool
        QTemporaryFile.open(QIODevice.OpenMode) -> bool
        """
        return False

    def setAutoRemove(self, bool): # real signature unknown; restored from __doc__
        """ QTemporaryFile.setAutoRemove(bool) """
        pass

    def setFileTemplate(self, QString): # real signature unknown; restored from __doc__
        """ QTemporaryFile.setFileTemplate(QString) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


