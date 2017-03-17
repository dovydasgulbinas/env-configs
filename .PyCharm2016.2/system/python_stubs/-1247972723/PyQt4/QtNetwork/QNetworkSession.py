# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkSession(__PyQt4_QtCore.QObject):
    """ QNetworkSession(QNetworkConfiguration, QObject parent=None) """
    def accept(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.accept() """
        pass

    def activeTime(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.activeTime() -> int """
        return 0

    def bytesReceived(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.bytesReceived() -> int """
        return 0

    def bytesWritten(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.bytesWritten() -> int """
        return 0

    def close(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.close() """
        pass

    def closed(self, *args, **kwargs): # real signature unknown
        """ QNetworkSession.closed [signal] """
        pass

    def configuration(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.configuration() -> QNetworkConfiguration """
        return QNetworkConfiguration

    def connectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QNetworkSession.connectNotify(SIGNAL()) """
        pass

    def disconnectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QNetworkSession.disconnectNotify(SIGNAL()) """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """
        QNetworkSession.error() -> QNetworkSession.SessionError
        QNetworkSession.error[QNetworkSession.SessionError] [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.errorString() -> QString """
        pass

    def ignore(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.ignore() """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.interface() -> QNetworkInterface """
        return QNetworkInterface

    def isOpen(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.isOpen() -> bool """
        return False

    def migrate(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.migrate() """
        pass

    def newConfigurationActivated(self, *args, **kwargs): # real signature unknown
        """ QNetworkSession.newConfigurationActivated [signal] """
        pass

    def open(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.open() """
        pass

    def opened(self, *args, **kwargs): # real signature unknown
        """ QNetworkSession.opened [signal] """
        pass

    def preferredConfigurationChanged(self, *args, **kwargs): # real signature unknown
        """ QNetworkSession.preferredConfigurationChanged[QNetworkConfiguration, bool] [signal] """
        pass

    def reject(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.reject() """
        pass

    def sessionProperty(self, QString): # real signature unknown; restored from __doc__
        """ QNetworkSession.sessionProperty(QString) -> QVariant """
        pass

    def setSessionProperty(self, QString, QVariant): # real signature unknown; restored from __doc__
        """ QNetworkSession.setSessionProperty(QString, QVariant) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.state() -> QNetworkSession.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QNetworkSession.stateChanged[QNetworkSession.State] [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ QNetworkSession.stop() """
        pass

    def waitForOpened(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QNetworkSession.waitForOpened(int msecs=30000) -> bool """
        return False

    def __init__(self, QNetworkConfiguration, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Closing = 4
    Connected = 3
    Connecting = 2
    Disconnected = 5
    Invalid = 0
    InvalidConfigurationError = 4
    NotAvailable = 1
    OperationNotSupportedError = 3
    Roaming = 6
    RoamingError = 2
    SessionAbortedError = 1
    UnknownSessionError = 0


