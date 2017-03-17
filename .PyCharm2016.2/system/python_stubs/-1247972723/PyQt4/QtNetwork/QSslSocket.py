# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QTcpSocket import QTcpSocket

class QSslSocket(QTcpSocket):
    """ QSslSocket(QObject parent=None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ QSslSocket.abort() """
        pass

    def addCaCertificate(self, QSslCertificate): # real signature unknown; restored from __doc__
        """ QSslSocket.addCaCertificate(QSslCertificate) """
        pass

    def addCaCertificates(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSslSocket.addCaCertificates(QString, QSsl.EncodingFormat format=QSsl.Pem, QRegExp.PatternSyntax syntax=QRegExp.FixedString) -> bool
        QSslSocket.addCaCertificates(list-of-QSslCertificate)
        """
        return False

    def addDefaultCaCertificate(self, QSslCertificate): # real signature unknown; restored from __doc__
        """ QSslSocket.addDefaultCaCertificate(QSslCertificate) """
        pass

    def addDefaultCaCertificates(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSslSocket.addDefaultCaCertificates(QString, QSsl.EncodingFormat format=QSsl.Pem, QRegExp.PatternSyntax syntax=QRegExp.FixedString) -> bool
        QSslSocket.addDefaultCaCertificates(list-of-QSslCertificate)
        """
        return False

    def atEnd(self): # real signature unknown; restored from __doc__
        """ QSslSocket.atEnd() -> bool """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ QSslSocket.bytesAvailable() -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ QSslSocket.bytesToWrite() -> int """
        return 0

    def caCertificates(self): # real signature unknown; restored from __doc__
        """ QSslSocket.caCertificates() -> list-of-QSslCertificate """
        pass

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ QSslSocket.canReadLine() -> bool """
        return False

    def ciphers(self): # real signature unknown; restored from __doc__
        """ QSslSocket.ciphers() -> list-of-QSslCipher """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ QSslSocket.close() """
        pass

    def connectToHostEncrypted(self, QString, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSslSocket.connectToHostEncrypted(QString, int, QIODevice.OpenMode mode=QIODevice.ReadWrite)
        QSslSocket.connectToHostEncrypted(QString, int, QString, QIODevice.OpenMode mode=QIODevice.ReadWrite)
        """
        pass

    def connectToHostImplementation(self, QString, p_int, QIODevice_OpenMode): # real signature unknown; restored from __doc__
        """ QSslSocket.connectToHostImplementation(QString, int, QIODevice.OpenMode) """
        pass

    def defaultCaCertificates(self): # real signature unknown; restored from __doc__
        """ QSslSocket.defaultCaCertificates() -> list-of-QSslCertificate """
        pass

    def defaultCiphers(self): # real signature unknown; restored from __doc__
        """ QSslSocket.defaultCiphers() -> list-of-QSslCipher """
        pass

    def disconnectFromHostImplementation(self): # real signature unknown; restored from __doc__
        """ QSslSocket.disconnectFromHostImplementation() """
        pass

    def encrypted(self, *args, **kwargs): # real signature unknown
        """ QSslSocket.encrypted [signal] """
        pass

    def encryptedBytesAvailable(self): # real signature unknown; restored from __doc__
        """ QSslSocket.encryptedBytesAvailable() -> int """
        return 0

    def encryptedBytesToWrite(self): # real signature unknown; restored from __doc__
        """ QSslSocket.encryptedBytesToWrite() -> int """
        return 0

    def encryptedBytesWritten(self, *args, **kwargs): # real signature unknown
        """ QSslSocket.encryptedBytesWritten[int] [signal] """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ QSslSocket.flush() -> bool """
        return False

    def ignoreSslErrors(self, list_of_QSslError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSslSocket.ignoreSslErrors()
        QSslSocket.ignoreSslErrors(list-of-QSslError)
        """
        pass

    def isEncrypted(self): # real signature unknown; restored from __doc__
        """ QSslSocket.isEncrypted() -> bool """
        return False

    def localCertificate(self): # real signature unknown; restored from __doc__
        """ QSslSocket.localCertificate() -> QSslCertificate """
        return QSslCertificate

    def mode(self): # real signature unknown; restored from __doc__
        """ QSslSocket.mode() -> QSslSocket.SslMode """
        pass

    def modeChanged(self, *args, **kwargs): # real signature unknown
        """ QSslSocket.modeChanged[QSslSocket.SslMode] [signal] """
        pass

    def peerCertificate(self): # real signature unknown; restored from __doc__
        """ QSslSocket.peerCertificate() -> QSslCertificate """
        return QSslCertificate

    def peerCertificateChain(self): # real signature unknown; restored from __doc__
        """ QSslSocket.peerCertificateChain() -> list-of-QSslCertificate """
        pass

    def peerVerifyDepth(self): # real signature unknown; restored from __doc__
        """ QSslSocket.peerVerifyDepth() -> int """
        return 0

    def peerVerifyError(self, *args, **kwargs): # real signature unknown
        """ QSslSocket.peerVerifyError[QSslError] [signal] """
        pass

    def peerVerifyMode(self): # real signature unknown; restored from __doc__
        """ QSslSocket.peerVerifyMode() -> QSslSocket.PeerVerifyMode """
        pass

    def peerVerifyName(self): # real signature unknown; restored from __doc__
        """ QSslSocket.peerVerifyName() -> QString """
        pass

    def privateKey(self): # real signature unknown; restored from __doc__
        """ QSslSocket.privateKey() -> QSslKey """
        return QSslKey

    def protocol(self): # real signature unknown; restored from __doc__
        """ QSslSocket.protocol() -> QSsl.SslProtocol """
        pass

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ QSslSocket.readData(int) -> str """
        return ""

    def sessionCipher(self): # real signature unknown; restored from __doc__
        """ QSslSocket.sessionCipher() -> QSslCipher """
        return QSslCipher

    def setCaCertificates(self, list_of_QSslCertificate): # real signature unknown; restored from __doc__
        """ QSslSocket.setCaCertificates(list-of-QSslCertificate) """
        pass

    def setCiphers(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSslSocket.setCiphers(list-of-QSslCipher)
        QSslSocket.setCiphers(QString)
        """
        pass

    def setDefaultCaCertificates(self, list_of_QSslCertificate): # real signature unknown; restored from __doc__
        """ QSslSocket.setDefaultCaCertificates(list-of-QSslCertificate) """
        pass

    def setDefaultCiphers(self, list_of_QSslCipher): # real signature unknown; restored from __doc__
        """ QSslSocket.setDefaultCiphers(list-of-QSslCipher) """
        pass

    def setLocalCertificate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSslSocket.setLocalCertificate(QSslCertificate)
        QSslSocket.setLocalCertificate(QString, QSsl.EncodingFormat format=QSsl.Pem)
        """
        pass

    def setPeerVerifyDepth(self, p_int): # real signature unknown; restored from __doc__
        """ QSslSocket.setPeerVerifyDepth(int) """
        pass

    def setPeerVerifyMode(self, QSslSocket_PeerVerifyMode): # real signature unknown; restored from __doc__
        """ QSslSocket.setPeerVerifyMode(QSslSocket.PeerVerifyMode) """
        pass

    def setPeerVerifyName(self, QString): # real signature unknown; restored from __doc__
        """ QSslSocket.setPeerVerifyName(QString) """
        pass

    def setPrivateKey(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSslSocket.setPrivateKey(QSslKey)
        QSslSocket.setPrivateKey(QString, QSsl.KeyAlgorithm algorithm=QSsl.Rsa, QSsl.EncodingFormat format=QSsl.Pem, QByteArray passPhrase=QByteArray())
        """
        pass

    def setProtocol(self, QSsl_SslProtocol): # real signature unknown; restored from __doc__
        """ QSslSocket.setProtocol(QSsl.SslProtocol) """
        pass

    def setReadBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QSslSocket.setReadBufferSize(int) """
        pass

    def setSocketDescriptor(self, p_int, QAbstractSocket_SocketState_state=None, QIODevice_OpenMode_mode=None): # real signature unknown; restored from __doc__
        """ QSslSocket.setSocketDescriptor(int, QAbstractSocket.SocketState state=QAbstractSocket.ConnectedState, QIODevice.OpenMode mode=QIODevice.ReadWrite) -> bool """
        return False

    def setSocketOption(self, QAbstractSocket_SocketOption, QVariant): # real signature unknown; restored from __doc__
        """ QSslSocket.setSocketOption(QAbstractSocket.SocketOption, QVariant) """
        pass

    def setSslConfiguration(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ QSslSocket.setSslConfiguration(QSslConfiguration) """
        pass

    def socketOption(self, QAbstractSocket_SocketOption): # real signature unknown; restored from __doc__
        """ QSslSocket.socketOption(QAbstractSocket.SocketOption) -> QVariant """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ QSslSocket.sslConfiguration() -> QSslConfiguration """
        return QSslConfiguration

    def sslErrors(self): # real signature unknown; restored from __doc__
        """
        QSslSocket.sslErrors() -> list-of-QSslError
        QSslSocket.sslErrors[list-of-QSslError] [signal]
        """
        pass

    def startClientEncryption(self): # real signature unknown; restored from __doc__
        """ QSslSocket.startClientEncryption() """
        pass

    def startServerEncryption(self): # real signature unknown; restored from __doc__
        """ QSslSocket.startServerEncryption() """
        pass

    def supportedCiphers(self): # real signature unknown; restored from __doc__
        """ QSslSocket.supportedCiphers() -> list-of-QSslCipher """
        pass

    def supportsSsl(self): # real signature unknown; restored from __doc__
        """ QSslSocket.supportsSsl() -> bool """
        return False

    def systemCaCertificates(self): # real signature unknown; restored from __doc__
        """ QSslSocket.systemCaCertificates() -> list-of-QSslCertificate """
        pass

    def waitForBytesWritten(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QSslSocket.waitForBytesWritten(int msecs=30000) -> bool """
        return False

    def waitForConnected(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QSslSocket.waitForConnected(int msecs=30000) -> bool """
        return False

    def waitForDisconnected(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QSslSocket.waitForDisconnected(int msecs=30000) -> bool """
        return False

    def waitForEncrypted(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QSslSocket.waitForEncrypted(int msecs=30000) -> bool """
        return False

    def waitForReadyRead(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QSslSocket.waitForReadyRead(int msecs=30000) -> bool """
        return False

    def writeData(self, p_str): # real signature unknown; restored from __doc__
        """ QSslSocket.writeData(str) -> int """
        return 0

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    AutoVerifyPeer = 3
    QueryPeer = 1
    SslClientMode = 1
    SslServerMode = 2
    UnencryptedMode = 0
    VerifyNone = 0
    VerifyPeer = 2


