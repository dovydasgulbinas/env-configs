# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QSslError(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QSslError()
    QSslError(QSslError.SslError)
    QSslError(QSslError.SslError, QSslCertificate)
    QSslError(QSslError)
    """
    def certificate(self): # real signature unknown; restored from __doc__
        """ QSslError.certificate() -> QSslCertificate """
        return QSslCertificate

    def error(self): # real signature unknown; restored from __doc__
        """ QSslError.error() -> QSslError.SslError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QSslError.errorString() -> QString """
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


    AuthorityIssuerSerialNumberMismatch = 20
    CertificateBlacklisted = 24
    CertificateExpired = 6
    CertificateNotYetValid = 5
    CertificateRejected = 18
    CertificateRevoked = 13
    CertificateSignatureFailed = 4
    CertificateUntrusted = 17
    HostNameMismatch = 22
    InvalidCaCertificate = 14
    InvalidNotAfterField = 8
    InvalidNotBeforeField = 7
    InvalidPurpose = 16
    NoError = 0
    NoPeerCertificate = 21
    NoSslSupport = 23
    PathLengthExceeded = 15
    SelfSignedCertificate = 9
    SelfSignedCertificateInChain = 10
    SubjectIssuerMismatch = 19
    UnableToDecodeIssuerPublicKey = 3
    UnableToDecryptCertificateSignature = 2
    UnableToGetIssuerCertificate = 1
    UnableToGetLocalIssuerCertificate = 11
    UnableToVerifyFirstCertificate = 12
    UnspecifiedError = -1


