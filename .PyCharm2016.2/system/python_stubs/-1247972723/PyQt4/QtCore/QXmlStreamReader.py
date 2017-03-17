# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QXmlStreamReader(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QXmlStreamReader()
    QXmlStreamReader(QIODevice)
    QXmlStreamReader(QByteArray)
    QXmlStreamReader(QString)
    """
    def addData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamReader.addData(QByteArray)
        QXmlStreamReader.addData(QString)
        """
        pass

    def addExtraNamespaceDeclaration(self, QXmlStreamNamespaceDeclaration): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.addExtraNamespaceDeclaration(QXmlStreamNamespaceDeclaration) """
        pass

    def addExtraNamespaceDeclarations(self, list_of_QXmlStreamNamespaceDeclaration): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.addExtraNamespaceDeclarations(list-of-QXmlStreamNamespaceDeclaration) """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.atEnd() -> bool """
        return False

    def attributes(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.attributes() -> QXmlStreamAttributes """
        return QXmlStreamAttributes

    def characterOffset(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.characterOffset() -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.clear() """
        pass

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.columnNumber() -> int """
        return 0

    def device(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.device() -> QIODevice """
        return QIODevice

    def documentEncoding(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.documentEncoding() -> QStringRef """
        return QStringRef

    def documentVersion(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.documentVersion() -> QStringRef """
        return QStringRef

    def dtdName(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.dtdName() -> QStringRef """
        return QStringRef

    def dtdPublicId(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.dtdPublicId() -> QStringRef """
        return QStringRef

    def dtdSystemId(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.dtdSystemId() -> QStringRef """
        return QStringRef

    def entityDeclarations(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.entityDeclarations() -> list-of-QXmlStreamEntityDeclaration """
        pass

    def entityResolver(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.entityResolver() -> QXmlStreamEntityResolver """
        return QXmlStreamEntityResolver

    def error(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.error() -> QXmlStreamReader.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.errorString() -> QString """
        return QString

    def hasError(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.hasError() -> bool """
        return False

    def isCDATA(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.isCDATA() -> bool """
        return False

    def isCharacters(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.isCharacters() -> bool """
        return False

    def isComment(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.isComment() -> bool """
        return False

    def isDTD(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.isDTD() -> bool """
        return False

    def isEndDocument(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.isEndDocument() -> bool """
        return False

    def isEndElement(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.isEndElement() -> bool """
        return False

    def isEntityReference(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.isEntityReference() -> bool """
        return False

    def isProcessingInstruction(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.isProcessingInstruction() -> bool """
        return False

    def isStandaloneDocument(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.isStandaloneDocument() -> bool """
        return False

    def isStartDocument(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.isStartDocument() -> bool """
        return False

    def isStartElement(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.isStartElement() -> bool """
        return False

    def isWhitespace(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.isWhitespace() -> bool """
        return False

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.lineNumber() -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.name() -> QStringRef """
        return QStringRef

    def namespaceDeclarations(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.namespaceDeclarations() -> list-of-QXmlStreamNamespaceDeclaration """
        pass

    def namespaceProcessing(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.namespaceProcessing() -> bool """
        return False

    def namespaceUri(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.namespaceUri() -> QStringRef """
        return QStringRef

    def notationDeclarations(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.notationDeclarations() -> list-of-QXmlStreamNotationDeclaration """
        pass

    def prefix(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.prefix() -> QStringRef """
        return QStringRef

    def processingInstructionData(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.processingInstructionData() -> QStringRef """
        return QStringRef

    def processingInstructionTarget(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.processingInstructionTarget() -> QStringRef """
        return QStringRef

    def qualifiedName(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.qualifiedName() -> QStringRef """
        return QStringRef

    def raiseError(self, QString_message=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QXmlStreamReader.raiseError(QString message=QString()) """
        pass

    def readElementText(self, QXmlStreamReader_ReadElementTextBehaviour=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamReader.readElementText() -> QString
        QXmlStreamReader.readElementText(QXmlStreamReader.ReadElementTextBehaviour) -> QString
        """
        return QString

    def readNext(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.readNext() -> QXmlStreamReader.TokenType """
        pass

    def readNextStartElement(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.readNextStartElement() -> bool """
        return False

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.setDevice(QIODevice) """
        pass

    def setEntityResolver(self, QXmlStreamEntityResolver): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.setEntityResolver(QXmlStreamEntityResolver) """
        pass

    def setNamespaceProcessing(self, bool): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.setNamespaceProcessing(bool) """
        pass

    def skipCurrentElement(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.skipCurrentElement() """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.text() -> QStringRef """
        return QStringRef

    def tokenString(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.tokenString() -> QString """
        return QString

    def tokenType(self): # real signature unknown; restored from __doc__
        """ QXmlStreamReader.tokenType() -> QXmlStreamReader.TokenType """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Characters = 6
    Comment = 7
    CustomError = 2
    DTD = 8
    EndDocument = 3
    EndElement = 5
    EntityReference = 9
    ErrorOnUnexpectedElement = 0
    IncludeChildElements = 1
    Invalid = 1
    NoError = 0
    NoToken = 0
    NotWellFormedError = 3
    PrematureEndOfDocumentError = 4
    ProcessingInstruction = 10
    SkipChildElements = 2
    StartDocument = 2
    StartElement = 4
    UnexpectedElementError = 1


