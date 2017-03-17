# encoding: utf-8
# module PyQt4.QtXmlPatterns
# from /usr/lib/python2.7/dist-packages/PyQt4/QtXmlPatterns.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


# no functions
# classes

class QAbstractMessageHandler(__PyQt4_QtCore.QObject):
    """ QAbstractMessageHandler(QObject parent=None) """
    def handleMessage(self, QtMsgType, QString, QUrl, QSourceLocation): # real signature unknown; restored from __doc__
        """ QAbstractMessageHandler.handleMessage(QtMsgType, QString, QUrl, QSourceLocation) """
        pass

    def message(self, QtMsgType, QString, QUrl_identifier=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractMessageHandler.message(QtMsgType, QString, QUrl identifier=QUrl(), QSourceLocation sourceLocation=QSourceLocation()) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QAbstractUriResolver(__PyQt4_QtCore.QObject):
    """ QAbstractUriResolver(QObject parent=None) """
    def resolve(self, QUrl, QUrl_1): # real signature unknown; restored from __doc__
        """ QAbstractUriResolver.resolve(QUrl, QUrl) -> QUrl """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QAbstractXmlNodeModel(): # skipped bases: <type 'sip.simplewrapper'>
    """ QAbstractXmlNodeModel() """
    def attributes(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.attributes(QXmlNodeModelIndex) -> list-of-QXmlNodeModelIndex """
        pass

    def baseUri(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.baseUri(QXmlNodeModelIndex) -> QUrl """
        pass

    def compareOrder(self, QXmlNodeModelIndex, QXmlNodeModelIndex_1): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.compareOrder(QXmlNodeModelIndex, QXmlNodeModelIndex) -> QXmlNodeModelIndex.DocumentOrder """
        pass

    def createIndex(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAbstractXmlNodeModel.createIndex(int) -> QXmlNodeModelIndex
        QAbstractXmlNodeModel.createIndex(int, int) -> QXmlNodeModelIndex
        QAbstractXmlNodeModel.createIndex(object, int additionalData=0) -> QXmlNodeModelIndex
        """
        return QXmlNodeModelIndex

    def documentUri(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.documentUri(QXmlNodeModelIndex) -> QUrl """
        pass

    def elementById(self, QXmlName): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.elementById(QXmlName) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def kind(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.kind(QXmlNodeModelIndex) -> QXmlNodeModelIndex.NodeKind """
        pass

    def name(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.name(QXmlNodeModelIndex) -> QXmlName """
        return QXmlName

    def namespaceBindings(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.namespaceBindings(QXmlNodeModelIndex) -> list-of-QXmlName """
        pass

    def nextFromSimpleAxis(self, QAbstractXmlNodeModel_SimpleAxis, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.nextFromSimpleAxis(QAbstractXmlNodeModel.SimpleAxis, QXmlNodeModelIndex) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def nodesByIdref(self, QXmlName): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.nodesByIdref(QXmlName) -> list-of-QXmlNodeModelIndex """
        pass

    def root(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.root(QXmlNodeModelIndex) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def sourceLocation(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.sourceLocation(QXmlNodeModelIndex) -> QSourceLocation """
        return QSourceLocation

    def stringValue(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.stringValue(QXmlNodeModelIndex) -> QString """
        pass

    def typedValue(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractXmlNodeModel.typedValue(QXmlNodeModelIndex) -> QVariant """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FirstChild = 1
    NextSibling = 3
    Parent = 0
    PreviousSibling = 2


class QAbstractXmlReceiver(): # skipped bases: <type 'sip.simplewrapper'>
    """ QAbstractXmlReceiver() """
    def atomicValue(self, QVariant): # real signature unknown; restored from __doc__
        """ QAbstractXmlReceiver.atomicValue(QVariant) """
        pass

    def attribute(self, QXmlName, QStringRef): # real signature unknown; restored from __doc__
        """ QAbstractXmlReceiver.attribute(QXmlName, QStringRef) """
        pass

    def characters(self, QStringRef): # real signature unknown; restored from __doc__
        """ QAbstractXmlReceiver.characters(QStringRef) """
        pass

    def comment(self, QString): # real signature unknown; restored from __doc__
        """ QAbstractXmlReceiver.comment(QString) """
        pass

    def endDocument(self): # real signature unknown; restored from __doc__
        """ QAbstractXmlReceiver.endDocument() """
        pass

    def endElement(self): # real signature unknown; restored from __doc__
        """ QAbstractXmlReceiver.endElement() """
        pass

    def endOfSequence(self): # real signature unknown; restored from __doc__
        """ QAbstractXmlReceiver.endOfSequence() """
        pass

    def namespaceBinding(self, QXmlName): # real signature unknown; restored from __doc__
        """ QAbstractXmlReceiver.namespaceBinding(QXmlName) """
        pass

    def processingInstruction(self, QXmlName, QString): # real signature unknown; restored from __doc__
        """ QAbstractXmlReceiver.processingInstruction(QXmlName, QString) """
        pass

    def startDocument(self): # real signature unknown; restored from __doc__
        """ QAbstractXmlReceiver.startDocument() """
        pass

    def startElement(self, QXmlName): # real signature unknown; restored from __doc__
        """ QAbstractXmlReceiver.startElement(QXmlName) """
        pass

    def startOfSequence(self): # real signature unknown; restored from __doc__
        """ QAbstractXmlReceiver.startOfSequence() """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSimpleXmlNodeModel(QAbstractXmlNodeModel):
    """ QSimpleXmlNodeModel(QXmlNamePool) """
    def baseUri(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QSimpleXmlNodeModel.baseUri(QXmlNodeModelIndex) -> QUrl """
        pass

    def elementById(self, QXmlName): # real signature unknown; restored from __doc__
        """ QSimpleXmlNodeModel.elementById(QXmlName) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def namePool(self): # real signature unknown; restored from __doc__
        """ QSimpleXmlNodeModel.namePool() -> QXmlNamePool """
        return QXmlNamePool

    def namespaceBindings(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QSimpleXmlNodeModel.namespaceBindings(QXmlNodeModelIndex) -> list-of-QXmlName """
        pass

    def nodesByIdref(self, QXmlName): # real signature unknown; restored from __doc__
        """ QSimpleXmlNodeModel.nodesByIdref(QXmlName) -> list-of-QXmlNodeModelIndex """
        pass

    def stringValue(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ QSimpleXmlNodeModel.stringValue(QXmlNodeModelIndex) -> QString """
        pass

    def __init__(self, QXmlNamePool): # real signature unknown; restored from __doc__
        pass


class QSourceLocation(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QSourceLocation()
    QSourceLocation(QSourceLocation)
    QSourceLocation(QUrl, int line=-1, int column=-1)
    """
    def column(self): # real signature unknown; restored from __doc__
        """ QSourceLocation.column() -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ QSourceLocation.isNull() -> bool """
        return False

    def line(self): # real signature unknown; restored from __doc__
        """ QSourceLocation.line() -> int """
        return 0

    def setColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QSourceLocation.setColumn(int) """
        pass

    def setLine(self, p_int): # real signature unknown; restored from __doc__
        """ QSourceLocation.setLine(int) """
        pass

    def setUri(self, QUrl): # real signature unknown; restored from __doc__
        """ QSourceLocation.setUri(QUrl) """
        pass

    def uri(self): # real signature unknown; restored from __doc__
        """ QSourceLocation.uri() -> QUrl """
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



class QXmlSerializer(QAbstractXmlReceiver):
    """ QXmlSerializer(QXmlQuery, QIODevice) """
    def atomicValue(self, QVariant): # real signature unknown; restored from __doc__
        """ QXmlSerializer.atomicValue(QVariant) """
        pass

    def attribute(self, QXmlName, QStringRef): # real signature unknown; restored from __doc__
        """ QXmlSerializer.attribute(QXmlName, QStringRef) """
        pass

    def characters(self, QStringRef): # real signature unknown; restored from __doc__
        """ QXmlSerializer.characters(QStringRef) """
        pass

    def codec(self): # real signature unknown; restored from __doc__
        """ QXmlSerializer.codec() -> QTextCodec """
        pass

    def comment(self, QString): # real signature unknown; restored from __doc__
        """ QXmlSerializer.comment(QString) """
        pass

    def endDocument(self): # real signature unknown; restored from __doc__
        """ QXmlSerializer.endDocument() """
        pass

    def endElement(self): # real signature unknown; restored from __doc__
        """ QXmlSerializer.endElement() """
        pass

    def endOfSequence(self): # real signature unknown; restored from __doc__
        """ QXmlSerializer.endOfSequence() """
        pass

    def namespaceBinding(self, QXmlName): # real signature unknown; restored from __doc__
        """ QXmlSerializer.namespaceBinding(QXmlName) """
        pass

    def outputDevice(self): # real signature unknown; restored from __doc__
        """ QXmlSerializer.outputDevice() -> QIODevice """
        pass

    def processingInstruction(self, QXmlName, QString): # real signature unknown; restored from __doc__
        """ QXmlSerializer.processingInstruction(QXmlName, QString) """
        pass

    def setCodec(self, QTextCodec): # real signature unknown; restored from __doc__
        """ QXmlSerializer.setCodec(QTextCodec) """
        pass

    def startDocument(self): # real signature unknown; restored from __doc__
        """ QXmlSerializer.startDocument() """
        pass

    def startElement(self, QXmlName): # real signature unknown; restored from __doc__
        """ QXmlSerializer.startElement(QXmlName) """
        pass

    def startOfSequence(self): # real signature unknown; restored from __doc__
        """ QXmlSerializer.startOfSequence() """
        pass

    def __init__(self, QXmlQuery, QIODevice): # real signature unknown; restored from __doc__
        pass


class QXmlFormatter(QXmlSerializer):
    """ QXmlFormatter(QXmlQuery, QIODevice) """
    def atomicValue(self, QVariant): # real signature unknown; restored from __doc__
        """ QXmlFormatter.atomicValue(QVariant) """
        pass

    def attribute(self, QXmlName, QStringRef): # real signature unknown; restored from __doc__
        """ QXmlFormatter.attribute(QXmlName, QStringRef) """
        pass

    def characters(self, QStringRef): # real signature unknown; restored from __doc__
        """ QXmlFormatter.characters(QStringRef) """
        pass

    def comment(self, QString): # real signature unknown; restored from __doc__
        """ QXmlFormatter.comment(QString) """
        pass

    def endDocument(self): # real signature unknown; restored from __doc__
        """ QXmlFormatter.endDocument() """
        pass

    def endElement(self): # real signature unknown; restored from __doc__
        """ QXmlFormatter.endElement() """
        pass

    def endOfSequence(self): # real signature unknown; restored from __doc__
        """ QXmlFormatter.endOfSequence() """
        pass

    def indentationDepth(self): # real signature unknown; restored from __doc__
        """ QXmlFormatter.indentationDepth() -> int """
        return 0

    def processingInstruction(self, QXmlName, QString): # real signature unknown; restored from __doc__
        """ QXmlFormatter.processingInstruction(QXmlName, QString) """
        pass

    def setIndentationDepth(self, p_int): # real signature unknown; restored from __doc__
        """ QXmlFormatter.setIndentationDepth(int) """
        pass

    def startDocument(self): # real signature unknown; restored from __doc__
        """ QXmlFormatter.startDocument() """
        pass

    def startElement(self, QXmlName): # real signature unknown; restored from __doc__
        """ QXmlFormatter.startElement(QXmlName) """
        pass

    def startOfSequence(self): # real signature unknown; restored from __doc__
        """ QXmlFormatter.startOfSequence() """
        pass

    def __init__(self, QXmlQuery, QIODevice): # real signature unknown; restored from __doc__
        pass


class QXmlItem(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QXmlItem()
    QXmlItem(QXmlItem)
    QXmlItem(QXmlNodeModelIndex)
    QXmlItem(QVariant)
    """
    def isAtomicValue(self): # real signature unknown; restored from __doc__
        """ QXmlItem.isAtomicValue() -> bool """
        return False

    def isNode(self): # real signature unknown; restored from __doc__
        """ QXmlItem.isNode() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QXmlItem.isNull() -> bool """
        return False

    def toAtomicValue(self): # real signature unknown; restored from __doc__
        """ QXmlItem.toAtomicValue() -> QVariant """
        pass

    def toNodeModelIndex(self): # real signature unknown; restored from __doc__
        """ QXmlItem.toNodeModelIndex() -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlName(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QXmlName()
    QXmlName(QXmlNamePool, QString, QString namespaceUri=QString(), QString prefix=QString())
    QXmlName(QXmlName)
    """
    def fromClarkName(self, QString, QXmlNamePool): # real signature unknown; restored from __doc__
        """ QXmlName.fromClarkName(QString, QXmlNamePool) -> QXmlName """
        return QXmlName

    def isNCName(self, QString): # real signature unknown; restored from __doc__
        """ QXmlName.isNCName(QString) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QXmlName.isNull() -> bool """
        return False

    def localName(self, QXmlNamePool): # real signature unknown; restored from __doc__
        """ QXmlName.localName(QXmlNamePool) -> QString """
        pass

    def namespaceUri(self, QXmlNamePool): # real signature unknown; restored from __doc__
        """ QXmlName.namespaceUri(QXmlNamePool) -> QString """
        pass

    def prefix(self, QXmlNamePool): # real signature unknown; restored from __doc__
        """ QXmlName.prefix(QXmlNamePool) -> QString """
        pass

    def toClarkName(self, QXmlNamePool): # real signature unknown; restored from __doc__
        """ QXmlName.toClarkName(QXmlNamePool) -> QString """
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



class QXmlNamePool(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QXmlNamePool()
    QXmlNamePool(QXmlNamePool)
    """
    def __init__(self, QXmlNamePool=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlNodeModelIndex(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QXmlNodeModelIndex()
    QXmlNodeModelIndex(QXmlNodeModelIndex)
    """
    def additionalData(self): # real signature unknown; restored from __doc__
        """ QXmlNodeModelIndex.additionalData() -> int """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ QXmlNodeModelIndex.data() -> int """
        return 0

    def internalPointer(self): # real signature unknown; restored from __doc__
        """ QXmlNodeModelIndex.internalPointer() -> object """
        return object()

    def isNull(self): # real signature unknown; restored from __doc__
        """ QXmlNodeModelIndex.isNull() -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ QXmlNodeModelIndex.model() -> QAbstractXmlNodeModel """
        return QAbstractXmlNodeModel

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

    def __init__(self, QXmlNodeModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    Attribute = 1
    Comment = 2
    Document = 4
    Element = 8
    Follows = 1
    Is = 0
    Namespace = 16
    Precedes = -1
    ProcessingInstruction = 32
    Text = 64


class QXmlQuery(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QXmlQuery()
    QXmlQuery(QXmlQuery)
    QXmlQuery(QXmlNamePool)
    QXmlQuery(QXmlQuery.QueryLanguage, QXmlNamePool pool=QXmlNamePool())
    """
    def bindVariable(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlQuery.bindVariable(QXmlName, QXmlItem)
        QXmlQuery.bindVariable(QXmlName, QIODevice)
        QXmlQuery.bindVariable(QXmlName, QXmlQuery)
        QXmlQuery.bindVariable(QString, QXmlItem)
        QXmlQuery.bindVariable(QString, QIODevice)
        QXmlQuery.bindVariable(QString, QXmlQuery)
        """
        pass

    def evaluateTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlQuery.evaluateTo(QXmlResultItems)
        QXmlQuery.evaluateTo(QAbstractXmlReceiver) -> bool
        QXmlQuery.evaluateTo(QStringList) -> bool
        QXmlQuery.evaluateTo(QIODevice) -> bool
        QXmlQuery.evaluateTo(QString) -> bool
        """
        return False

    def evaluateToString(self): # real signature unknown; restored from __doc__
        """ QXmlQuery.evaluateToString() -> QString """
        pass

    def evaluateToStringList(self): # real signature unknown; restored from __doc__
        """ QXmlQuery.evaluateToStringList() -> QStringList """
        pass

    def initialTemplateName(self): # real signature unknown; restored from __doc__
        """ QXmlQuery.initialTemplateName() -> QXmlName """
        return QXmlName

    def isValid(self): # real signature unknown; restored from __doc__
        """ QXmlQuery.isValid() -> bool """
        return False

    def messageHandler(self): # real signature unknown; restored from __doc__
        """ QXmlQuery.messageHandler() -> QAbstractMessageHandler """
        return QAbstractMessageHandler

    def namePool(self): # real signature unknown; restored from __doc__
        """ QXmlQuery.namePool() -> QXmlNamePool """
        return QXmlNamePool

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ QXmlQuery.networkAccessManager() -> QNetworkAccessManager """
        pass

    def queryLanguage(self): # real signature unknown; restored from __doc__
        """ QXmlQuery.queryLanguage() -> QXmlQuery.QueryLanguage """
        pass

    def setFocus(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlQuery.setFocus(QXmlItem)
        QXmlQuery.setFocus(QUrl) -> bool
        QXmlQuery.setFocus(QIODevice) -> bool
        QXmlQuery.setFocus(QString) -> bool
        """
        return False

    def setInitialTemplateName(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlQuery.setInitialTemplateName(QXmlName)
        QXmlQuery.setInitialTemplateName(QString)
        """
        pass

    def setMessageHandler(self, QAbstractMessageHandler): # real signature unknown; restored from __doc__
        """ QXmlQuery.setMessageHandler(QAbstractMessageHandler) """
        pass

    def setNetworkAccessManager(self, QNetworkAccessManager): # real signature unknown; restored from __doc__
        """ QXmlQuery.setNetworkAccessManager(QNetworkAccessManager) """
        pass

    def setQuery(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlQuery.setQuery(QString, QUrl documentUri=QUrl())
        QXmlQuery.setQuery(QIODevice, QUrl documentUri=QUrl())
        QXmlQuery.setQuery(QUrl, QUrl baseUri=QUrl())
        """
        pass

    def setUriResolver(self, QAbstractUriResolver): # real signature unknown; restored from __doc__
        """ QXmlQuery.setUriResolver(QAbstractUriResolver) """
        pass

    def uriResolver(self): # real signature unknown; restored from __doc__
        """ QXmlQuery.uriResolver() -> QAbstractUriResolver """
        return QAbstractUriResolver

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    XQuery10 = 1
    XSLT20 = 2


class QXmlResultItems(): # skipped bases: <type 'sip.simplewrapper'>
    """ QXmlResultItems() """
    def current(self): # real signature unknown; restored from __doc__
        """ QXmlResultItems.current() -> QXmlItem """
        return QXmlItem

    def hasError(self): # real signature unknown; restored from __doc__
        """ QXmlResultItems.hasError() -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ QXmlResultItems.next() -> QXmlItem """
        return QXmlItem

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlSchema(): # skipped bases: <type 'sip.simplewrapper'>
    """ QXmlSchema() """
    def documentUri(self): # real signature unknown; restored from __doc__
        """ QXmlSchema.documentUri() -> QUrl """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ QXmlSchema.isValid() -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlSchema.load(QUrl) -> bool
        QXmlSchema.load(QIODevice, QUrl documentUri=QUrl()) -> bool
        QXmlSchema.load(QByteArray, QUrl documentUri=QUrl()) -> bool
        """
        return False

    def messageHandler(self): # real signature unknown; restored from __doc__
        """ QXmlSchema.messageHandler() -> QAbstractMessageHandler """
        return QAbstractMessageHandler

    def namePool(self): # real signature unknown; restored from __doc__
        """ QXmlSchema.namePool() -> QXmlNamePool """
        return QXmlNamePool

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ QXmlSchema.networkAccessManager() -> QNetworkAccessManager """
        pass

    def setMessageHandler(self, QAbstractMessageHandler): # real signature unknown; restored from __doc__
        """ QXmlSchema.setMessageHandler(QAbstractMessageHandler) """
        pass

    def setNetworkAccessManager(self, QNetworkAccessManager): # real signature unknown; restored from __doc__
        """ QXmlSchema.setNetworkAccessManager(QNetworkAccessManager) """
        pass

    def setUriResolver(self, QAbstractUriResolver): # real signature unknown; restored from __doc__
        """ QXmlSchema.setUriResolver(QAbstractUriResolver) """
        pass

    def uriResolver(self): # real signature unknown; restored from __doc__
        """ QXmlSchema.uriResolver() -> QAbstractUriResolver """
        return QAbstractUriResolver

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlSchemaValidator(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QXmlSchemaValidator()
    QXmlSchemaValidator(QXmlSchema)
    """
    def messageHandler(self): # real signature unknown; restored from __doc__
        """ QXmlSchemaValidator.messageHandler() -> QAbstractMessageHandler """
        return QAbstractMessageHandler

    def namePool(self): # real signature unknown; restored from __doc__
        """ QXmlSchemaValidator.namePool() -> QXmlNamePool """
        return QXmlNamePool

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ QXmlSchemaValidator.networkAccessManager() -> QNetworkAccessManager """
        pass

    def schema(self): # real signature unknown; restored from __doc__
        """ QXmlSchemaValidator.schema() -> QXmlSchema """
        return QXmlSchema

    def setMessageHandler(self, QAbstractMessageHandler): # real signature unknown; restored from __doc__
        """ QXmlSchemaValidator.setMessageHandler(QAbstractMessageHandler) """
        pass

    def setNetworkAccessManager(self, QNetworkAccessManager): # real signature unknown; restored from __doc__
        """ QXmlSchemaValidator.setNetworkAccessManager(QNetworkAccessManager) """
        pass

    def setSchema(self, QXmlSchema): # real signature unknown; restored from __doc__
        """ QXmlSchemaValidator.setSchema(QXmlSchema) """
        pass

    def setUriResolver(self, QAbstractUriResolver): # real signature unknown; restored from __doc__
        """ QXmlSchemaValidator.setUriResolver(QAbstractUriResolver) """
        pass

    def uriResolver(self): # real signature unknown; restored from __doc__
        """ QXmlSchemaValidator.uriResolver() -> QAbstractUriResolver """
        return QAbstractUriResolver

    def validate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlSchemaValidator.validate(QUrl) -> bool
        QXmlSchemaValidator.validate(QIODevice, QUrl documentUri=QUrl()) -> bool
        QXmlSchemaValidator.validate(QByteArray, QUrl documentUri=QUrl()) -> bool
        """
        return False

    def __init__(self, QXmlSchema=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



