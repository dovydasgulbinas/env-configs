# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QSslCertificate(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QSslCertificate(QIODevice, QSsl.EncodingFormat format=QSsl.Pem)
    QSslCertificate(QByteArray data=QByteArray(), QSsl.EncodingFormat format=QSsl.Pem)
    QSslCertificate(QSslCertificate)
    """
    def alternateSubjectNames(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.alternateSubjectNames() -> dict-of-QSsl.AlternateNameEntryType-list-of-QString """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.clear() """
        pass

    def digest(self, QCryptographicHash_Algorithm_algorithm=None): # real signature unknown; restored from __doc__
        """ QSslCertificate.digest(QCryptographicHash.Algorithm algorithm=QCryptographicHash.Md5) -> QByteArray """
        pass

    def effectiveDate(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.effectiveDate() -> QDateTime """
        pass

    def expiryDate(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.expiryDate() -> QDateTime """
        pass

    def fromData(self, QByteArray, QSsl_EncodingFormat_format=None): # real signature unknown; restored from __doc__
        """ QSslCertificate.fromData(QByteArray, QSsl.EncodingFormat format=QSsl.Pem) -> list-of-QSslCertificate """
        pass

    def fromDevice(self, QIODevice, QSsl_EncodingFormat_format=None): # real signature unknown; restored from __doc__
        """ QSslCertificate.fromDevice(QIODevice, QSsl.EncodingFormat format=QSsl.Pem) -> list-of-QSslCertificate """
        pass

    def fromPath(self, QString, QSsl_EncodingFormat_format=None, QRegExp_PatternSyntax_syntax=None): # real signature unknown; restored from __doc__
        """ QSslCertificate.fromPath(QString, QSsl.EncodingFormat format=QSsl.Pem, QRegExp.PatternSyntax syntax=QRegExp.FixedString) -> list-of-QSslCertificate """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.handle() -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.isNull() -> bool """
        return False

    def issuerInfo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSslCertificate.issuerInfo(QSslCertificate.SubjectInfo) -> QString
        QSslCertificate.issuerInfo(QByteArray) -> QString
        """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.isValid() -> bool """
        return False

    def publicKey(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.publicKey() -> QSslKey """
        return QSslKey

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.serialNumber() -> QByteArray """
        pass

    def subjectInfo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSslCertificate.subjectInfo(QSslCertificate.SubjectInfo) -> QString
        QSslCertificate.subjectInfo(QByteArray) -> QString
        """
        pass

    def toDer(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.toDer() -> QByteArray """
        pass

    def toPem(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.toPem() -> QByteArray """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.version() -> QByteArray """
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


    CommonName = 1
    CountryName = 4
    LocalityName = 2
    Organization = 0
    OrganizationalUnitName = 3
    StateOrProvinceName = 5


