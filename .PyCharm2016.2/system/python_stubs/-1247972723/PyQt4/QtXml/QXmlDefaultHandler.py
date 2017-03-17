# encoding: utf-8
# module PyQt4.QtXml
# from /usr/lib/python2.7/dist-packages/PyQt4/QtXml.so
# by generator 1.143
# no doc
# no imports

from QXmlContentHandler import QXmlContentHandler

from QXmlErrorHandler import QXmlErrorHandler

from QXmlDTDHandler import QXmlDTDHandler

from QXmlEntityResolver import QXmlEntityResolver

from QXmlLexicalHandler import QXmlLexicalHandler

from QXmlDeclHandler import QXmlDeclHandler

class QXmlDefaultHandler(QXmlContentHandler, QXmlErrorHandler, QXmlDTDHandler, QXmlEntityResolver, QXmlLexicalHandler, QXmlDeclHandler):
    """ QXmlDefaultHandler() """
    def attributeDecl(self, QString, QString_1, QString_2, QString_3, QString_4): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.attributeDecl(QString, QString, QString, QString, QString) -> bool """
        return False

    def characters(self, QString): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.characters(QString) -> bool """
        return False

    def comment(self, QString): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.comment(QString) -> bool """
        return False

    def endCDATA(self): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.endCDATA() -> bool """
        return False

    def endDocument(self): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.endDocument() -> bool """
        return False

    def endDTD(self): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.endDTD() -> bool """
        return False

    def endElement(self, QString, QString_1, QString_2): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.endElement(QString, QString, QString) -> bool """
        return False

    def endEntity(self, QString): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.endEntity(QString) -> bool """
        return False

    def endPrefixMapping(self, QString): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.endPrefixMapping(QString) -> bool """
        return False

    def error(self, QXmlParseException): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.error(QXmlParseException) -> bool """
        return False

    def errorString(self): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.errorString() -> QString """
        pass

    def externalEntityDecl(self, QString, QString_1, QString_2): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.externalEntityDecl(QString, QString, QString) -> bool """
        return False

    def fatalError(self, QXmlParseException): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.fatalError(QXmlParseException) -> bool """
        return False

    def ignorableWhitespace(self, QString): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.ignorableWhitespace(QString) -> bool """
        return False

    def internalEntityDecl(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.internalEntityDecl(QString, QString) -> bool """
        return False

    def notationDecl(self, QString, QString_1, QString_2): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.notationDecl(QString, QString, QString) -> bool """
        return False

    def processingInstruction(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.processingInstruction(QString, QString) -> bool """
        return False

    def resolveEntity(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.resolveEntity(QString, QString) -> (bool, QXmlInputSource) """
        pass

    def setDocumentLocator(self, QXmlLocator): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.setDocumentLocator(QXmlLocator) """
        pass

    def skippedEntity(self, QString): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.skippedEntity(QString) -> bool """
        return False

    def startCDATA(self): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.startCDATA() -> bool """
        return False

    def startDocument(self): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.startDocument() -> bool """
        return False

    def startDTD(self, QString, QString_1, QString_2): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.startDTD(QString, QString, QString) -> bool """
        return False

    def startElement(self, QString, QString_1, QString_2, QXmlAttributes): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.startElement(QString, QString, QString, QXmlAttributes) -> bool """
        return False

    def startEntity(self, QString): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.startEntity(QString) -> bool """
        return False

    def startPrefixMapping(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.startPrefixMapping(QString, QString) -> bool """
        return False

    def unparsedEntityDecl(self, QString, QString_1, QString_2, QString_3): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.unparsedEntityDecl(QString, QString, QString, QString) -> bool """
        return False

    def warning(self, QXmlParseException): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.warning(QXmlParseException) -> bool """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass


