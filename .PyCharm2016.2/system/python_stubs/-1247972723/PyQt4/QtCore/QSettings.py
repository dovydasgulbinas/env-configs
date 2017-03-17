# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QSettings(QObject):
    """
    QSettings(QString, QString application=QString(), QObject parent=None)
    QSettings(QSettings.Scope, QString, QString application=QString(), QObject parent=None)
    QSettings(QSettings.Format, QSettings.Scope, QString, QString application=QString(), QObject parent=None)
    QSettings(QString, QSettings.Format, QObject parent=None)
    QSettings(QObject parent=None)
    """
    def allKeys(self): # real signature unknown; restored from __doc__
        """ QSettings.allKeys() -> QStringList """
        return QStringList

    def applicationName(self): # real signature unknown; restored from __doc__
        """ QSettings.applicationName() -> QString """
        return QString

    def beginGroup(self, QString): # real signature unknown; restored from __doc__
        """ QSettings.beginGroup(QString) """
        pass

    def beginReadArray(self, QString): # real signature unknown; restored from __doc__
        """ QSettings.beginReadArray(QString) -> int """
        return 0

    def beginWriteArray(self, QString, int_size=-1): # real signature unknown; restored from __doc__
        """ QSettings.beginWriteArray(QString, int size=-1) """
        pass

    def childGroups(self): # real signature unknown; restored from __doc__
        """ QSettings.childGroups() -> QStringList """
        return QStringList

    def childKeys(self): # real signature unknown; restored from __doc__
        """ QSettings.childKeys() -> QStringList """
        return QStringList

    def clear(self): # real signature unknown; restored from __doc__
        """ QSettings.clear() """
        pass

    def contains(self, QString): # real signature unknown; restored from __doc__
        """ QSettings.contains(QString) -> bool """
        return False

    def defaultFormat(self): # real signature unknown; restored from __doc__
        """ QSettings.defaultFormat() -> QSettings.Format """
        pass

    def endArray(self): # real signature unknown; restored from __doc__
        """ QSettings.endArray() """
        pass

    def endGroup(self): # real signature unknown; restored from __doc__
        """ QSettings.endGroup() """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QSettings.event(QEvent) -> bool """
        return False

    def fallbacksEnabled(self): # real signature unknown; restored from __doc__
        """ QSettings.fallbacksEnabled() -> bool """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ QSettings.fileName() -> QString """
        return QString

    def format(self): # real signature unknown; restored from __doc__
        """ QSettings.format() -> QSettings.Format """
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ QSettings.group() -> QString """
        return QString

    def iniCodec(self): # real signature unknown; restored from __doc__
        """ QSettings.iniCodec() -> QTextCodec """
        return QTextCodec

    def isWritable(self): # real signature unknown; restored from __doc__
        """ QSettings.isWritable() -> bool """
        return False

    def organizationName(self): # real signature unknown; restored from __doc__
        """ QSettings.organizationName() -> QString """
        return QString

    def remove(self, QString): # real signature unknown; restored from __doc__
        """ QSettings.remove(QString) """
        pass

    def scope(self): # real signature unknown; restored from __doc__
        """ QSettings.scope() -> QSettings.Scope """
        pass

    def setArrayIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QSettings.setArrayIndex(int) """
        pass

    def setDefaultFormat(self, QSettings_Format): # real signature unknown; restored from __doc__
        """ QSettings.setDefaultFormat(QSettings.Format) """
        pass

    def setFallbacksEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QSettings.setFallbacksEnabled(bool) """
        pass

    def setIniCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSettings.setIniCodec(QTextCodec)
        QSettings.setIniCodec(str)
        """
        pass

    def setPath(self, QSettings_Format, QSettings_Scope, QString): # real signature unknown; restored from __doc__
        """ QSettings.setPath(QSettings.Format, QSettings.Scope, QString) """
        pass

    def setSystemIniPath(self, QString): # real signature unknown; restored from __doc__
        """ QSettings.setSystemIniPath(QString) """
        pass

    def setUserIniPath(self, QString): # real signature unknown; restored from __doc__
        """ QSettings.setUserIniPath(QString) """
        pass

    def setValue(self, QString, QVariant): # real signature unknown; restored from __doc__
        """ QSettings.setValue(QString, QVariant) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ QSettings.status() -> QSettings.Status """
        pass

    def sync(self): # real signature unknown; restored from __doc__
        """ QSettings.sync() """
        pass

    def value(self, QString, QVariant_defaultValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSettings.value(QString, QVariant defaultValue=QVariant(), object type=None) -> object """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AccessError = 1
    FormatError = 2
    IniFormat = 1
    InvalidFormat = 16
    NativeFormat = 0
    NoError = 0
    SystemScope = 1
    UserScope = 0


