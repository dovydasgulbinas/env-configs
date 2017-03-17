# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QSessionManager(__PyQt4_QtCore.QObject):
    # no doc
    def allowsErrorInteraction(self): # real signature unknown; restored from __doc__
        """ QSessionManager.allowsErrorInteraction() -> bool """
        return False

    def allowsInteraction(self): # real signature unknown; restored from __doc__
        """ QSessionManager.allowsInteraction() -> bool """
        return False

    def cancel(self): # real signature unknown; restored from __doc__
        """ QSessionManager.cancel() """
        pass

    def discardCommand(self): # real signature unknown; restored from __doc__
        """ QSessionManager.discardCommand() -> QStringList """
        pass

    def isPhase2(self): # real signature unknown; restored from __doc__
        """ QSessionManager.isPhase2() -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ QSessionManager.release() """
        pass

    def requestPhase2(self): # real signature unknown; restored from __doc__
        """ QSessionManager.requestPhase2() """
        pass

    def restartCommand(self): # real signature unknown; restored from __doc__
        """ QSessionManager.restartCommand() -> QStringList """
        pass

    def restartHint(self): # real signature unknown; restored from __doc__
        """ QSessionManager.restartHint() -> QSessionManager.RestartHint """
        pass

    def sessionId(self): # real signature unknown; restored from __doc__
        """ QSessionManager.sessionId() -> QString """
        pass

    def sessionKey(self): # real signature unknown; restored from __doc__
        """ QSessionManager.sessionKey() -> QString """
        pass

    def setDiscardCommand(self, QStringList): # real signature unknown; restored from __doc__
        """ QSessionManager.setDiscardCommand(QStringList) """
        pass

    def setManagerProperty(self, QString, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSessionManager.setManagerProperty(QString, QString)
        QSessionManager.setManagerProperty(QString, QStringList)
        """
        pass

    def setRestartCommand(self, QStringList): # real signature unknown; restored from __doc__
        """ QSessionManager.setRestartCommand(QStringList) """
        pass

    def setRestartHint(self, QSessionManager_RestartHint): # real signature unknown; restored from __doc__
        """ QSessionManager.setRestartHint(QSessionManager.RestartHint) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    RestartAnyway = 1
    RestartIfRunning = 0
    RestartImmediately = 2
    RestartNever = 3


