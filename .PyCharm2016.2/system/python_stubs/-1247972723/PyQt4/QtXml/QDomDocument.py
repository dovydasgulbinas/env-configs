# encoding: utf-8
# module PyQt4.QtXml
# from /usr/lib/python2.7/dist-packages/PyQt4/QtXml.so
# by generator 1.143
# no doc
# no imports

from QDomNode import QDomNode

class QDomDocument(QDomNode):
    """
    QDomDocument()
    QDomDocument(QString)
    QDomDocument(QDomDocumentType)
    QDomDocument(QDomDocument)
    """
    def createAttribute(self, QString): # real signature unknown; restored from __doc__
        """ QDomDocument.createAttribute(QString) -> QDomAttr """
        return QDomAttr

    def createAttributeNS(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDomDocument.createAttributeNS(QString, QString) -> QDomAttr """
        return QDomAttr

    def createCDATASection(self, QString): # real signature unknown; restored from __doc__
        """ QDomDocument.createCDATASection(QString) -> QDomCDATASection """
        return QDomCDATASection

    def createComment(self, QString): # real signature unknown; restored from __doc__
        """ QDomDocument.createComment(QString) -> QDomComment """
        return QDomComment

    def createDocumentFragment(self): # real signature unknown; restored from __doc__
        """ QDomDocument.createDocumentFragment() -> QDomDocumentFragment """
        return QDomDocumentFragment

    def createElement(self, QString): # real signature unknown; restored from __doc__
        """ QDomDocument.createElement(QString) -> QDomElement """
        return QDomElement

    def createElementNS(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDomDocument.createElementNS(QString, QString) -> QDomElement """
        return QDomElement

    def createEntityReference(self, QString): # real signature unknown; restored from __doc__
        """ QDomDocument.createEntityReference(QString) -> QDomEntityReference """
        return QDomEntityReference

    def createProcessingInstruction(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDomDocument.createProcessingInstruction(QString, QString) -> QDomProcessingInstruction """
        return QDomProcessingInstruction

    def createTextNode(self, QString): # real signature unknown; restored from __doc__
        """ QDomDocument.createTextNode(QString) -> QDomText """
        return QDomText

    def doctype(self): # real signature unknown; restored from __doc__
        """ QDomDocument.doctype() -> QDomDocumentType """
        return QDomDocumentType

    def documentElement(self): # real signature unknown; restored from __doc__
        """ QDomDocument.documentElement() -> QDomElement """
        return QDomElement

    def elementById(self, QString): # real signature unknown; restored from __doc__
        """ QDomDocument.elementById(QString) -> QDomElement """
        return QDomElement

    def elementsByTagName(self, QString): # real signature unknown; restored from __doc__
        """ QDomDocument.elementsByTagName(QString) -> QDomNodeList """
        return QDomNodeList

    def elementsByTagNameNS(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDomDocument.elementsByTagNameNS(QString, QString) -> QDomNodeList """
        return QDomNodeList

    def implementation(self): # real signature unknown; restored from __doc__
        """ QDomDocument.implementation() -> QDomImplementation """
        return QDomImplementation

    def importNode(self, QDomNode, bool): # real signature unknown; restored from __doc__
        """ QDomDocument.importNode(QDomNode, bool) -> QDomNode """
        return QDomNode

    def nodeType(self): # real signature unknown; restored from __doc__
        """ QDomDocument.nodeType() -> QDomNode.NodeType """
        pass

    def setContent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDomDocument.setContent(QByteArray, bool) -> (bool, QString, int, int)
        QDomDocument.setContent(QString, bool) -> (bool, QString, int, int)
        QDomDocument.setContent(QIODevice, bool) -> (bool, QString, int, int)
        QDomDocument.setContent(QXmlInputSource, bool) -> (bool, QString, int, int)
        QDomDocument.setContent(QByteArray) -> (bool, QString, int, int)
        QDomDocument.setContent(QString) -> (bool, QString, int, int)
        QDomDocument.setContent(QIODevice) -> (bool, QString, int, int)
        QDomDocument.setContent(QXmlInputSource, QXmlReader) -> (bool, QString, int, int)
        """
        pass

    def toByteArray(self, int_indent=1): # real signature unknown; restored from __doc__
        """ QDomDocument.toByteArray(int indent=1) -> QByteArray """
        pass

    def toString(self, int_indent=1): # real signature unknown; restored from __doc__
        """ QDomDocument.toString(int indent=1) -> QString """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


