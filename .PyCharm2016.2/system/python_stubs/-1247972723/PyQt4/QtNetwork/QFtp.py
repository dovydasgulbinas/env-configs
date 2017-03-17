# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QFtp(__PyQt4_QtCore.QObject):
    """ QFtp(QObject parent=None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ QFtp.abort() """
        pass

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ QFtp.bytesAvailable() -> int """
        return 0

    def cd(self, QString): # real signature unknown; restored from __doc__
        """ QFtp.cd(QString) -> int """
        return 0

    def clearPendingCommands(self): # real signature unknown; restored from __doc__
        """ QFtp.clearPendingCommands() """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ QFtp.close() -> int """
        return 0

    def commandFinished(self, *args, **kwargs): # real signature unknown
        """ QFtp.commandFinished[int, bool] [signal] """
        pass

    def commandStarted(self, *args, **kwargs): # real signature unknown
        """ QFtp.commandStarted[int] [signal] """
        pass

    def connectToHost(self, QString, int_port=21): # real signature unknown; restored from __doc__
        """ QFtp.connectToHost(QString, int port=21) -> int """
        return 0

    def currentCommand(self): # real signature unknown; restored from __doc__
        """ QFtp.currentCommand() -> QFtp.Command """
        pass

    def currentDevice(self): # real signature unknown; restored from __doc__
        """ QFtp.currentDevice() -> QIODevice """
        pass

    def currentId(self): # real signature unknown; restored from __doc__
        """ QFtp.currentId() -> int """
        return 0

    def dataTransferProgress(self, *args, **kwargs): # real signature unknown
        """ QFtp.dataTransferProgress[int, int] [signal] """
        pass

    def done(self, *args, **kwargs): # real signature unknown
        """ QFtp.done[bool] [signal] """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QFtp.error() -> QFtp.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QFtp.errorString() -> QString """
        pass

    def get(self, QString, QIODevice_device=None, QFtp_TransferType_type=None): # real signature unknown; restored from __doc__
        """ QFtp.get(QString, QIODevice device=None, QFtp.TransferType type=QFtp.Binary) -> int """
        return 0

    def hasPendingCommands(self): # real signature unknown; restored from __doc__
        """ QFtp.hasPendingCommands() -> bool """
        return False

    def list(self, QString_directory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFtp.list(QString directory=QString()) -> int """
        pass

    def listInfo(self, *args, **kwargs): # real signature unknown
        """ QFtp.listInfo[QUrlInfo] [signal] """
        pass

    def login(self, QString_user=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFtp.login(QString user=QString(), QString password=QString()) -> int """
        pass

    def mkdir(self, QString): # real signature unknown; restored from __doc__
        """ QFtp.mkdir(QString) -> int """
        return 0

    def put(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFtp.put(QByteArray, QString, QFtp.TransferType type=QFtp.Binary) -> int
        QFtp.put(QIODevice, QString, QFtp.TransferType type=QFtp.Binary) -> int
        """
        return 0

    def rawCommand(self, QString): # real signature unknown; restored from __doc__
        """ QFtp.rawCommand(QString) -> int """
        return 0

    def rawCommandReply(self, *args, **kwargs): # real signature unknown
        """ QFtp.rawCommandReply[int, QString] [signal] """
        pass

    def read(self, p_int): # real signature unknown; restored from __doc__
        """ QFtp.read(int) -> str """
        return ""

    def readAll(self): # real signature unknown; restored from __doc__
        """ QFtp.readAll() -> QByteArray """
        pass

    def readyRead(self, *args, **kwargs): # real signature unknown
        """ QFtp.readyRead [signal] """
        pass

    def remove(self, QString): # real signature unknown; restored from __doc__
        """ QFtp.remove(QString) -> int """
        return 0

    def rename(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QFtp.rename(QString, QString) -> int """
        return 0

    def rmdir(self, QString): # real signature unknown; restored from __doc__
        """ QFtp.rmdir(QString) -> int """
        return 0

    def setProxy(self, QString, p_int): # real signature unknown; restored from __doc__
        """ QFtp.setProxy(QString, int) -> int """
        return 0

    def setTransferMode(self, QFtp_TransferMode): # real signature unknown; restored from __doc__
        """ QFtp.setTransferMode(QFtp.TransferMode) -> int """
        return 0

    def state(self): # real signature unknown; restored from __doc__
        """ QFtp.state() -> QFtp.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QFtp.stateChanged[int] [signal] """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Active = 0
    Ascii = 1
    Binary = 0
    Cd = 7
    Close = 5
    Closing = 5
    Connected = 3
    Connecting = 2
    ConnectionRefused = 3
    ConnectToHost = 3
    Get = 8
    HostLookup = 1
    HostNotFound = 2
    List = 6
    LoggedIn = 4
    Login = 4
    Mkdir = 11
    NoError = 0
    None_ = 0
    NotConnected = 4
    Passive = 1
    Put = 9
    RawCommand = 14
    Remove = 10
    Rename = 13
    Rmdir = 12
    SetProxy = 2
    SetTransferMode = 1
    Unconnected = 0
    UnknownError = 1


