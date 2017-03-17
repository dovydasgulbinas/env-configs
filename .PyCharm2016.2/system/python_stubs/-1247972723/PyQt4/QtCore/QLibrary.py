# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QLibrary(QObject):
    """
    QLibrary(QObject parent=None)
    QLibrary(QString, QObject parent=None)
    QLibrary(QString, int, QObject parent=None)
    QLibrary(QString, QString, QObject parent=None)
    """
    def errorString(self): # real signature unknown; restored from __doc__
        """ QLibrary.errorString() -> QString """
        return QString

    def fileName(self): # real signature unknown; restored from __doc__
        """ QLibrary.fileName() -> QString """
        return QString

    def isLibrary(self, QString): # real signature unknown; restored from __doc__
        """ QLibrary.isLibrary(QString) -> bool """
        return False

    def isLoaded(self): # real signature unknown; restored from __doc__
        """ QLibrary.isLoaded() -> bool """
        return False

    def load(self): # real signature unknown; restored from __doc__
        """ QLibrary.load() -> bool """
        return False

    def loadHints(self): # real signature unknown; restored from __doc__
        """ QLibrary.loadHints() -> QLibrary.LoadHints """
        pass

    def resolve(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLibrary.resolve(str) -> sip.voidptr
        QLibrary.resolve(QString, str) -> sip.voidptr
        QLibrary.resolve(QString, int, str) -> sip.voidptr
        QLibrary.resolve(QString, QString, str) -> sip.voidptr
        """
        pass

    def setFileName(self, QString): # real signature unknown; restored from __doc__
        """ QLibrary.setFileName(QString) """
        pass

    def setFileNameAndVersion(self, QString, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLibrary.setFileNameAndVersion(QString, int)
        QLibrary.setFileNameAndVersion(QString, QString)
        """
        pass

    def setLoadHints(self, QLibrary_LoadHints): # real signature unknown; restored from __doc__
        """ QLibrary.setLoadHints(QLibrary.LoadHints) """
        pass

    def unload(self): # real signature unknown; restored from __doc__
        """ QLibrary.unload() -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ExportExternalSymbolsHint = 2
    LoadArchiveMemberHint = 4
    ResolveAllSymbolsHint = 1


