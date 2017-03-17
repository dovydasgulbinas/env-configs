# encoding: utf-8
# module PyQt4.QtDBus
# from /usr/lib/python2.7/dist-packages/PyQt4/QtDBus.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


# no functions
# classes

class QDBus(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AutoDetect = 3
    Block = 1
    BlockWithGui = 2
    NoBlock = 0


class QDBusAbstractAdaptor(__PyQt4_QtCore.QObject):
    """ QDBusAbstractAdaptor(QObject) """
    def autoRelaySignals(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractAdaptor.autoRelaySignals() -> bool """
        return False

    def setAutoRelaySignals(self, bool): # real signature unknown; restored from __doc__
        """ QDBusAbstractAdaptor.setAutoRelaySignals(bool) """
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


class QDBusAbstractInterface(__PyQt4_QtCore.QObject):
    """ QDBusAbstractInterface(QString, QString, str, QDBusConnection, QObject) """
    def asyncCall(self, QString, QVariant_arg1=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDBusAbstractInterface.asyncCall(QString, QVariant arg1=QVariant(), QVariant arg2=QVariant(), QVariant arg3=QVariant(), QVariant arg4=QVariant(), QVariant arg5=QVariant(), QVariant arg6=QVariant(), QVariant arg7=QVariant(), QVariant arg8=QVariant()) -> QDBusPendingCall """
        pass

    def asyncCallWithArgumentList(self, QString, list_of_QVariant): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.asyncCallWithArgumentList(QString, list-of-QVariant) -> QDBusPendingCall """
        return QDBusPendingCall

    def call(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusAbstractInterface.call(QString, QVariant arg1=QVariant(), QVariant arg2=QVariant(), QVariant arg3=QVariant(), QVariant arg4=QVariant(), QVariant arg5=QVariant(), QVariant arg6=QVariant(), QVariant arg7=QVariant(), QVariant arg8=QVariant()) -> QDBusMessage
        QDBusAbstractInterface.call(QDBus.CallMode, QString, QVariant arg1=QVariant(), QVariant arg2=QVariant(), QVariant arg3=QVariant(), QVariant arg4=QVariant(), QVariant arg5=QVariant(), QVariant arg6=QVariant(), QVariant arg7=QVariant(), QVariant arg8=QVariant()) -> QDBusMessage
        """
        pass

    def callWithArgumentList(self, QDBus_CallMode, QString, list_of_QVariant): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.callWithArgumentList(QDBus.CallMode, QString, list-of-QVariant) -> QDBusMessage """
        return QDBusMessage

    def callWithCallback(self, QString, list_of_QVariant, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusAbstractInterface.callWithCallback(QString, list-of-QVariant, QObject, SLOT(), SLOT()) -> bool
        QDBusAbstractInterface.callWithCallback(QString, list-of-QVariant, callable, callable) -> object
        QDBusAbstractInterface.callWithCallback(QString, list-of-QVariant, QObject, SLOT()) -> bool
        QDBusAbstractInterface.callWithCallback(QString, list-of-QVariant, callable) -> object
        """
        return object()

    def connection(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.connection() -> QDBusConnection """
        return QDBusConnection

    def connectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDBusAbstractInterface.connectNotify(SIGNAL()) """
        pass

    def disconnectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDBusAbstractInterface.disconnectNotify(SIGNAL()) """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.interface() -> QString """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.isValid() -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.lastError() -> QDBusError """
        return QDBusError

    def path(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.path() -> QString """
        pass

    def service(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.service() -> QString """
        pass

    def setTimeout(self, p_int): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.setTimeout(int) """
        pass

    def timeout(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.timeout() -> int """
        return 0

    def __init__(self, QString, QString_1, p_str, QDBusConnection, QObject): # real signature unknown; restored from __doc__
        pass


class QDBusArgument(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDBusArgument()
    QDBusArgument(QDBusArgument)
    QDBusArgument(object, int id=QMetaType.Int)
    """
    def add(self, p_object, int_id=None): # real signature unknown; restored from __doc__
        """ QDBusArgument.add(object, int id=QMetaType.Int) """
        pass

    def beginArray(self, p_int): # real signature unknown; restored from __doc__
        """ QDBusArgument.beginArray(int) """
        pass

    def beginMap(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QDBusArgument.beginMap(int, int) """
        pass

    def beginMapEntry(self): # real signature unknown; restored from __doc__
        """ QDBusArgument.beginMapEntry() """
        pass

    def beginStructure(self): # real signature unknown; restored from __doc__
        """ QDBusArgument.beginStructure() """
        pass

    def endArray(self): # real signature unknown; restored from __doc__
        """ QDBusArgument.endArray() """
        pass

    def endMap(self): # real signature unknown; restored from __doc__
        """ QDBusArgument.endMap() """
        pass

    def endMapEntry(self): # real signature unknown; restored from __doc__
        """ QDBusArgument.endMapEntry() """
        pass

    def endStructure(self): # real signature unknown; restored from __doc__
        """ QDBusArgument.endStructure() """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusConnection(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDBusConnection(QString)
    QDBusConnection(QDBusConnection)
    """
    def asyncCall(self, QDBusMessage, int_timeout=-1): # real signature unknown; restored from __doc__
        """ QDBusConnection.asyncCall(QDBusMessage, int timeout=-1) -> QDBusPendingCall """
        return QDBusPendingCall

    def baseService(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.baseService() -> QString """
        pass

    def call(self, QDBusMessage, QDBus_CallMode_mode=None, int_timeout=-1): # real signature unknown; restored from __doc__
        """ QDBusConnection.call(QDBusMessage, QDBus.CallMode mode=QDBus.Block, int timeout=-1) -> QDBusMessage """
        return QDBusMessage

    def callWithCallback(self, QDBusMessage, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusConnection.callWithCallback(QDBusMessage, QObject, SLOT(), SLOT(), int timeout=-1) -> bool
        QDBusConnection.callWithCallback(QDBusMessage, callable, callable, int timeout=-1) -> object
        QDBusConnection.callWithCallback(QDBusMessage, QObject, SLOT(), int timeout=-1) -> bool
        QDBusConnection.callWithCallback(QDBusMessage, callable, int timeout=-1) -> object
        """
        return object()

    def connect(self, QString, QString_1, QString_2, QString_3, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusConnection.connect(QString, QString, QString, QString, QObject, SLOT()) -> bool
        QDBusConnection.connect(QString, QString, QString, QString, callable) -> object
        QDBusConnection.connect(QString, QString, QString, QString, QString, QObject, SLOT()) -> bool
        QDBusConnection.connect(QString, QString, QString, QString, QString, callable) -> object
        QDBusConnection.connect(QString, QString, QString, QString, QStringList, QString, QObject, SLOT()) -> bool
        QDBusConnection.connect(QString, QString, QString, QString, QStringList, QString, callable) -> object
        """
        return object()

    def connectionCapabilities(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.connectionCapabilities() -> QDBusConnection.ConnectionCapabilities """
        pass

    def connectToBus(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusConnection.connectToBus(QDBusConnection.BusType, QString) -> QDBusConnection
        QDBusConnection.connectToBus(QString, QString) -> QDBusConnection
        """
        return QDBusConnection

    def connectToPeer(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDBusConnection.connectToPeer(QString, QString) -> QDBusConnection """
        return QDBusConnection

    def disconnect(self, QString, QString_1, QString_2, QString_3, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusConnection.disconnect(QString, QString, QString, QString, QObject, SLOT()) -> bool
        QDBusConnection.disconnect(QString, QString, QString, QString, callable) -> object
        QDBusConnection.disconnect(QString, QString, QString, QString, QString, QObject, SLOT()) -> bool
        QDBusConnection.disconnect(QString, QString, QString, QString, QString, callable) -> object
        QDBusConnection.disconnect(QString, QString, QString, QString, QStringList, QString, QObject, SLOT()) -> bool
        QDBusConnection.disconnect(QString, QString, QString, QString, QStringList, QString, callable) -> object
        """
        return object()

    def disconnectFromBus(self, QString): # real signature unknown; restored from __doc__
        """ QDBusConnection.disconnectFromBus(QString) """
        pass

    def disconnectFromPeer(self, QString): # real signature unknown; restored from __doc__
        """ QDBusConnection.disconnectFromPeer(QString) """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.interface() -> QDBusConnectionInterface """
        return QDBusConnectionInterface

    def isConnected(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.isConnected() -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.lastError() -> QDBusError """
        return QDBusError

    def localMachineId(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.localMachineId() -> QByteArray """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.name() -> QString """
        pass

    def objectRegisteredAt(self, QString): # real signature unknown; restored from __doc__
        """ QDBusConnection.objectRegisteredAt(QString) -> QObject """
        pass

    def registerObject(self, QString, QObject, QDBusConnection_RegisterOptions_options=None): # real signature unknown; restored from __doc__
        """ QDBusConnection.registerObject(QString, QObject, QDBusConnection.RegisterOptions options=QDBusConnection.ExportAdaptors) -> bool """
        return False

    def registerService(self, QString): # real signature unknown; restored from __doc__
        """ QDBusConnection.registerService(QString) -> bool """
        return False

    def send(self, QDBusMessage): # real signature unknown; restored from __doc__
        """ QDBusConnection.send(QDBusMessage) -> bool """
        return False

    def sender(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.sender() -> QDBusConnection """
        return QDBusConnection

    def sessionBus(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.sessionBus() -> QDBusConnection """
        return QDBusConnection

    def systemBus(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.systemBus() -> QDBusConnection """
        return QDBusConnection

    def unregisterObject(self, QString, QDBusConnection_UnregisterMode_mode=None): # real signature unknown; restored from __doc__
        """ QDBusConnection.unregisterObject(QString, QDBusConnection.UnregisterMode mode=QDBusConnection.UnregisterNode) """
        pass

    def unregisterService(self, QString): # real signature unknown; restored from __doc__
        """ QDBusConnection.unregisterService(QString) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ActivationBus = 2
    ExportAdaptors = 1
    ExportAllContents = 4080
    ExportAllInvokables = 2176
    ExportAllProperties = 1088
    ExportAllSignal = 544
    ExportAllSignals = 544
    ExportAllSlots = 272
    ExportChildObjects = 4096
    ExportNonScriptableContents = 3840
    ExportNonScriptableInvokables = 2048
    ExportNonScriptableProperties = 1024
    ExportNonScriptableSignals = 512
    ExportNonScriptableSlots = 256
    ExportScriptableContents = 240
    ExportScriptableInvokables = 128
    ExportScriptableProperties = 64
    ExportScriptableSignals = 32
    ExportScriptableSlots = 16
    SessionBus = 0
    SystemBus = 1
    UnixFileDescriptorPassing = 1
    UnregisterNode = 0
    UnregisterTree = 1


class QDBusConnectionInterface(QDBusAbstractInterface):
    # no doc
    def callWithCallbackFailed(self, *args, **kwargs): # real signature unknown
        """ QDBusConnectionInterface.callWithCallbackFailed[QDBusError, QDBusMessage] [signal] """
        pass

    def connectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDBusConnectionInterface.connectNotify(SIGNAL()) """
        pass

    def disconnectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDBusConnectionInterface.disconnectNotify(SIGNAL()) """
        pass

    def isServiceRegistered(self, QString): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.isServiceRegistered(QString) -> QDBusReply """
        return QDBusReply

    def registeredServiceNames(self): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.registeredServiceNames() -> QDBusReply """
        return QDBusReply

    def registerService(self, QString, QDBusConnectionInterface_ServiceQueueOptions_qoption=None, QDBusConnectionInterface_ServiceReplacementOptions_roption=None): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.registerService(QString, QDBusConnectionInterface.ServiceQueueOptions qoption=QDBusConnectionInterface.DontQueueService, QDBusConnectionInterface.ServiceReplacementOptions roption=QDBusConnectionInterface.DontAllowReplacement) -> QDBusReply """
        return QDBusReply

    def serviceOwner(self, QString): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.serviceOwner(QString) -> QDBusReply """
        return QDBusReply

    def serviceOwnerChanged(self, *args, **kwargs): # real signature unknown
        """ QDBusConnectionInterface.serviceOwnerChanged[QString, QString, QString] [signal] """
        pass

    def servicePid(self, QString): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.servicePid(QString) -> QDBusReply """
        return QDBusReply

    def serviceRegistered(self, *args, **kwargs): # real signature unknown
        """ QDBusConnectionInterface.serviceRegistered[QString] [signal] """
        pass

    def serviceUid(self, QString): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.serviceUid(QString) -> QDBusReply """
        return QDBusReply

    def serviceUnregistered(self, *args, **kwargs): # real signature unknown
        """ QDBusConnectionInterface.serviceUnregistered[QString] [signal] """
        pass

    def startService(self, QString): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.startService(QString) -> QDBusReply """
        return QDBusReply

    def unregisterService(self, QString): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.unregisterService(QString) -> QDBusReply """
        return QDBusReply

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AllowReplacement = 1
    DontAllowReplacement = 0
    DontQueueService = 0
    QueueService = 1
    ReplaceExistingService = 2
    ServiceNotRegistered = 0
    ServiceQueued = 2
    ServiceRegistered = 1


class QDBusError(): # skipped bases: <type 'sip.simplewrapper'>
    """ QDBusError(QDBusError) """
    def errorString(self, QDBusError_ErrorType): # real signature unknown; restored from __doc__
        """ QDBusError.errorString(QDBusError.ErrorType) -> QString """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDBusError.isValid() -> bool """
        return False

    def message(self): # real signature unknown; restored from __doc__
        """ QDBusError.message() -> QString """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ QDBusError.name() -> QString """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QDBusError.type() -> QDBusError.ErrorType """
        pass

    def __init__(self, QDBusError): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccessDenied = 9
    AddressInUse = 13
    BadAddress = 6
    Disconnected = 14
    Failed = 2
    InternalError = 20
    InvalidArgs = 15
    InvalidInterface = 24
    InvalidMember = 25
    InvalidObjectPath = 23
    InvalidService = 22
    InvalidSignature = 18
    LimitsExceeded = 8
    NoError = 0
    NoMemory = 3
    NoNetwork = 12
    NoReply = 5
    NoServer = 10
    NotSupported = 7
    Other = 1
    ServiceUnknown = 4
    TimedOut = 17
    Timeout = 11
    UnknownInterface = 19
    UnknownMethod = 16
    UnknownObject = 21


class QDBusInterface(QDBusAbstractInterface):
    """ QDBusInterface(QString, QString, QString interface=QString(), QDBusConnection connection=QDBusConnection.sessionBus(), QObject parent=None) """
    def __init__(self, QString, QString_1, QString_interface=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QDBusMessage(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDBusMessage()
    QDBusMessage(QDBusMessage)
    """
    def arguments(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.arguments() -> list-of-QVariant """
        pass

    def autoStartService(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.autoStartService() -> bool """
        return False

    def createError(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusMessage.createError(QString, QString) -> QDBusMessage
        QDBusMessage.createError(QDBusError) -> QDBusMessage
        QDBusMessage.createError(QDBusError.ErrorType, QString) -> QDBusMessage
        """
        return QDBusMessage

    def createErrorReply(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusMessage.createErrorReply(QString, QString) -> QDBusMessage
        QDBusMessage.createErrorReply(QDBusError) -> QDBusMessage
        QDBusMessage.createErrorReply(QDBusError.ErrorType, QString) -> QDBusMessage
        """
        return QDBusMessage

    def createMethodCall(self, QString, QString_1, QString_2, QString_3): # real signature unknown; restored from __doc__
        """ QDBusMessage.createMethodCall(QString, QString, QString, QString) -> QDBusMessage """
        return QDBusMessage

    def createReply(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusMessage.createReply(list-of-QVariant arguments=QList&lt;QVariant&gt;()) -> QDBusMessage
        QDBusMessage.createReply(QVariant) -> QDBusMessage
        """
        return QDBusMessage

    def createSignal(self, QString, QString_1, QString_2): # real signature unknown; restored from __doc__
        """ QDBusMessage.createSignal(QString, QString, QString) -> QDBusMessage """
        return QDBusMessage

    def errorMessage(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.errorMessage() -> QString """
        pass

    def errorName(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.errorName() -> QString """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.interface() -> QString """
        pass

    def isDelayedReply(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.isDelayedReply() -> bool """
        return False

    def isReplyRequired(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.isReplyRequired() -> bool """
        return False

    def member(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.member() -> QString """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.path() -> QString """
        pass

    def service(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.service() -> QString """
        pass

    def setArguments(self, list_of_QVariant): # real signature unknown; restored from __doc__
        """ QDBusMessage.setArguments(list-of-QVariant) """
        pass

    def setAutoStartService(self, bool): # real signature unknown; restored from __doc__
        """ QDBusMessage.setAutoStartService(bool) """
        pass

    def setDelayedReply(self, bool): # real signature unknown; restored from __doc__
        """ QDBusMessage.setDelayedReply(bool) """
        pass

    def signature(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.signature() -> QString """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.type() -> QDBusMessage.MessageType """
        pass

    def __init__(self, QDBusMessage=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __lshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__lshift__(y) <==> x<<y """
        pass

    def __rlshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rlshift__(y) <==> y<<x """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ErrorMessage = 3
    InvalidMessage = 0
    MethodCallMessage = 1
    ReplyMessage = 2
    SignalMessage = 4


class QDBusObjectPath(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDBusObjectPath()
    QDBusObjectPath(QString)
    QDBusObjectPath(QDBusObjectPath)
    """
    def path(self): # real signature unknown; restored from __doc__
        """ QDBusObjectPath.path() -> QString """
        pass

    def setPath(self, QString): # real signature unknown; restored from __doc__
        """ QDBusObjectPath.setPath(QString) """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
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



class QDBusPendingCall(): # skipped bases: <type 'sip.simplewrapper'>
    """ QDBusPendingCall(QDBusPendingCall) """
    def fromCompletedCall(self, QDBusMessage): # real signature unknown; restored from __doc__
        """ QDBusPendingCall.fromCompletedCall(QDBusMessage) -> QDBusPendingCall """
        return QDBusPendingCall

    def fromError(self, QDBusError): # real signature unknown; restored from __doc__
        """ QDBusPendingCall.fromError(QDBusError) -> QDBusPendingCall """
        return QDBusPendingCall

    def __init__(self, QDBusPendingCall): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusPendingCallWatcher(__PyQt4_QtCore.QObject, QDBusPendingCall):
    """ QDBusPendingCallWatcher(QDBusPendingCall, QObject parent=None) """
    def finished(self, *args, **kwargs): # real signature unknown
        """ QDBusPendingCallWatcher.finished[QDBusPendingCallWatcher] [signal] """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ QDBusPendingCallWatcher.isFinished() -> bool """
        return False

    def waitForFinished(self): # real signature unknown; restored from __doc__
        """ QDBusPendingCallWatcher.waitForFinished() """
        pass

    def __init__(self, QDBusPendingCall, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QDBusPendingReply(QDBusPendingCall):
    """
    QDBusPendingReply()
    QDBusPendingReply(QDBusPendingReply)
    QDBusPendingReply(QDBusPendingCall)
    QDBusPendingReply(QDBusMessage)
    """
    def argumentAt(self, p_int): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.argumentAt(int) -> QVariant """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.error() -> QDBusError """
        return QDBusError

    def isError(self): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.isError() -> bool """
        return False

    def isFinished(self): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.isFinished() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.isValid() -> bool """
        return False

    def reply(self): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.reply() -> QDBusMessage """
        return QDBusMessage

    def value(self, object_type=None): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.value(object type=None) -> object """
        return object()

    def waitForFinished(self): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.waitForFinished() """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QDBusReply(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDBusReply(QDBusMessage)
    QDBusReply(QDBusPendingCall)
    QDBusReply(QDBusError)
    QDBusReply(QDBusReply)
    """
    def error(self): # real signature unknown; restored from __doc__
        """ QDBusReply.error() -> QDBusError """
        return QDBusError

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDBusReply.isValid() -> bool """
        return False

    def value(self, object_type=None): # real signature unknown; restored from __doc__
        """ QDBusReply.value(object type=None) -> object """
        return object()

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusServiceWatcher(__PyQt4_QtCore.QObject):
    """
    QDBusServiceWatcher(QObject parent=None)
    QDBusServiceWatcher(QString, QDBusConnection, QDBusServiceWatcher.WatchMode watchMode=QDBusServiceWatcher.WatchForOwnerChange, QObject parent=None)
    """
    def addWatchedService(self, QString): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.addWatchedService(QString) """
        pass

    def connection(self): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.connection() -> QDBusConnection """
        return QDBusConnection

    def removeWatchedService(self, QString): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.removeWatchedService(QString) -> bool """
        return False

    def serviceOwnerChanged(self, *args, **kwargs): # real signature unknown
        """ QDBusServiceWatcher.serviceOwnerChanged[QString, QString, QString] [signal] """
        pass

    def serviceRegistered(self, *args, **kwargs): # real signature unknown
        """ QDBusServiceWatcher.serviceRegistered[QString] [signal] """
        pass

    def serviceUnregistered(self, *args, **kwargs): # real signature unknown
        """ QDBusServiceWatcher.serviceUnregistered[QString] [signal] """
        pass

    def setConnection(self, QDBusConnection): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.setConnection(QDBusConnection) """
        pass

    def setWatchedServices(self, QStringList): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.setWatchedServices(QStringList) """
        pass

    def setWatchMode(self, QDBusServiceWatcher_WatchMode): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.setWatchMode(QDBusServiceWatcher.WatchMode) """
        pass

    def watchedServices(self): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.watchedServices() -> QStringList """
        pass

    def watchMode(self): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.watchMode() -> QDBusServiceWatcher.WatchMode """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    WatchForOwnerChange = 3
    WatchForRegistration = 1
    WatchForUnregistration = 2


class QDBusSignature(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDBusSignature()
    QDBusSignature(QString)
    QDBusSignature(QDBusSignature)
    """
    def setSignature(self, QString): # real signature unknown; restored from __doc__
        """ QDBusSignature.setSignature(QString) """
        pass

    def signature(self): # real signature unknown; restored from __doc__
        """ QDBusSignature.signature() -> QString """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
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



class QDBusUnixFileDescriptor(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDBusUnixFileDescriptor()
    QDBusUnixFileDescriptor(int)
    QDBusUnixFileDescriptor(QDBusUnixFileDescriptor)
    """
    def fileDescriptor(self): # real signature unknown; restored from __doc__
        """ QDBusUnixFileDescriptor.fileDescriptor() -> int """
        return 0

    def isSupported(self): # real signature unknown; restored from __doc__
        """ QDBusUnixFileDescriptor.isSupported() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDBusUnixFileDescriptor.isValid() -> bool """
        return False

    def setFileDescriptor(self, p_int): # real signature unknown; restored from __doc__
        """ QDBusUnixFileDescriptor.setFileDescriptor(int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusVariant(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDBusVariant()
    QDBusVariant(QVariant)
    QDBusVariant(QDBusVariant)
    """
    def setVariant(self, QVariant): # real signature unknown; restored from __doc__
        """ QDBusVariant.setVariant(QVariant) """
        pass

    def variant(self): # real signature unknown; restored from __doc__
        """ QDBusVariant.variant() -> QVariant """
        pass

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



