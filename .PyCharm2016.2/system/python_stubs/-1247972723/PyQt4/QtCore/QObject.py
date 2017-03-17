# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QObject(): # skipped bases: <type 'sip.wrapper'>
    """ QObject(QObject parent=None) """
    def blockSignals(self, bool): # real signature unknown; restored from __doc__
        """ QObject.blockSignals(bool) -> bool """
        return False

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ QObject.childEvent(QChildEvent) """
        pass

    def children(self): # real signature unknown; restored from __doc__
        """ QObject.children() -> list-of-QObject """
        pass

    def connect(self, QObject, SIGNAL, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QObject.connect(QObject, SIGNAL(), QObject, SLOT(), Qt.ConnectionType=Qt.AutoConnection) -> bool
        QObject.connect(QObject, SIGNAL(), callable, Qt.ConnectionType=Qt.AutoConnection) -> bool
        QObject.connect(QObject, SIGNAL(), SLOT(), Qt.ConnectionType=Qt.AutoConnection) -> bool
        """
        pass

    def connectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QObject.connectNotify(SIGNAL()) """
        pass

    def customEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QObject.customEvent(QEvent) """
        pass

    def deleteLater(self): # real signature unknown; restored from __doc__
        """ QObject.deleteLater() """
        pass

    def destroyed(self, *args, **kwargs): # real signature unknown
        """
        QObject.destroyed[QObject] [signal]
        QObject.destroyed [signal]
        """
        pass

    def disconnect(self, QObject, SIGNAL, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QObject.disconnect(QObject, SIGNAL(), QObject, SLOT()) -> bool
        QObject.disconnect(QObject, SIGNAL(), callable) -> bool
        """
        pass

    def disconnectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QObject.disconnectNotify(SIGNAL()) """
        pass

    def dumpObjectInfo(self): # real signature unknown; restored from __doc__
        """ QObject.dumpObjectInfo() """
        pass

    def dumpObjectTree(self): # real signature unknown; restored from __doc__
        """ QObject.dumpObjectTree() """
        pass

    def dynamicPropertyNames(self): # real signature unknown; restored from __doc__
        """ QObject.dynamicPropertyNames() -> list-of-QByteArray """
        pass

    def emit(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QObject.emit(SIGNAL(), ...) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QObject.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QObject.eventFilter(QObject, QEvent) -> bool """
        return False

    def findChild(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QObject.findChild(type, QString name=QString()) -> QObject
        QObject.findChild(tuple, QString name=QString()) -> QObject
        """
        pass

    def findChildren(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QObject.findChildren(type, QString name=QString()) -> list-of-QObject
        QObject.findChildren(tuple, QString name=QString()) -> list-of-QObject
        QObject.findChildren(type, QRegExp) -> list-of-QObject
        QObject.findChildren(tuple, QRegExp) -> list-of-QObject
        """
        pass

    def inherits(self, p_str): # real signature unknown; restored from __doc__
        """ QObject.inherits(str) -> bool """
        return False

    def installEventFilter(self, QObject): # real signature unknown; restored from __doc__
        """ QObject.installEventFilter(QObject) """
        pass

    def isWidgetType(self): # real signature unknown; restored from __doc__
        """ QObject.isWidgetType() -> bool """
        return False

    def killTimer(self, p_int): # real signature unknown; restored from __doc__
        """ QObject.killTimer(int) """
        pass

    def metaObject(self): # real signature unknown; restored from __doc__
        """ QObject.metaObject() -> QMetaObject """
        return QMetaObject

    def moveToThread(self, QThread): # real signature unknown; restored from __doc__
        """ QObject.moveToThread(QThread) """
        pass

    def objectName(self): # real signature unknown; restored from __doc__
        """ QObject.objectName() -> QString """
        return QString

    def parent(self): # real signature unknown; restored from __doc__
        """ QObject.parent() -> QObject """
        return QObject

    def property(self, p_str): # real signature unknown; restored from __doc__
        """ QObject.property(str) -> QVariant """
        return QVariant

    def pyqtConfigure(self, *more): # real signature unknown; restored from __doc__
        """
        QObject.pyqtConfigure(...)
        
        Each keyword argument is either the name of a Qt property or a Qt signal.
        For properties the property is set to the given value which should be of an
        appropriate type.
        For signals the signal is connected to the given value which should be a
        callable.
        """
        pass

    def receivers(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QObject.receivers(SIGNAL()) -> int """
        pass

    def removeEventFilter(self, QObject): # real signature unknown; restored from __doc__
        """ QObject.removeEventFilter(QObject) """
        pass

    def sender(self): # real signature unknown; restored from __doc__
        """ QObject.sender() -> QObject """
        return QObject

    def senderSignalIndex(self): # real signature unknown; restored from __doc__
        """ QObject.senderSignalIndex() -> int """
        return 0

    def setObjectName(self, QString): # real signature unknown; restored from __doc__
        """ QObject.setObjectName(QString) """
        pass

    def setParent(self, QObject): # real signature unknown; restored from __doc__
        """ QObject.setParent(QObject) """
        pass

    def setProperty(self, p_str, QVariant): # real signature unknown; restored from __doc__
        """ QObject.setProperty(str, QVariant) -> bool """
        return False

    def signalsBlocked(self): # real signature unknown; restored from __doc__
        """ QObject.signalsBlocked() -> bool """
        return False

    def startTimer(self, p_int): # real signature unknown; restored from __doc__
        """ QObject.startTimer(int) -> int """
        return 0

    def thread(self): # real signature unknown; restored from __doc__
        """ QObject.thread() -> QThread """
        return QThread

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QObject.timerEvent(QTimerEvent) """
        pass

    def tr(self, p_str, str_disambiguation=None, int_n=-1): # real signature unknown; restored from __doc__
        """ QObject.tr(str, str disambiguation=None, int n=-1) -> QString """
        return QString

    def trUtf8(self, p_str, str_disambiguation=None, int_n=-1): # real signature unknown; restored from __doc__
        """ QObject.trUtf8(str, str disambiguation=None, int n=-1) -> QString """
        return QString

    def __getattr__(self, p_str): # real signature unknown; restored from __doc__
        """ QObject.__getattr__(str) -> object """
        return object()

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




