# encoding: utf-8
# module PyQt4.QtXml
# from /usr/lib/python2.7/dist-packages/PyQt4/QtXml.so
# by generator 1.143
# no doc
# no imports

from QXmlReader import QXmlReader

class QXmlSimpleReader(QXmlReader):
    """ QXmlSimpleReader() """
    def contentHandler(self): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.contentHandler() -> QXmlContentHandler """
        return QXmlContentHandler

    def declHandler(self): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.declHandler() -> QXmlDeclHandler """
        return QXmlDeclHandler

    def DTDHandler(self): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.DTDHandler() -> QXmlDTDHandler """
        return QXmlDTDHandler

    def entityResolver(self): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.entityResolver() -> QXmlEntityResolver """
        return QXmlEntityResolver

    def errorHandler(self): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.errorHandler() -> QXmlErrorHandler """
        return QXmlErrorHandler

    def feature(self, QString): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.feature(QString) -> (bool, bool) """
        pass

    def hasFeature(self, QString): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.hasFeature(QString) -> bool """
        return False

    def hasProperty(self, QString): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.hasProperty(QString) -> bool """
        return False

    def lexicalHandler(self): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.lexicalHandler() -> QXmlLexicalHandler """
        return QXmlLexicalHandler

    def parse(self, QXmlInputSource, bool=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlSimpleReader.parse(QXmlInputSource) -> bool
        QXmlSimpleReader.parse(QXmlInputSource, bool) -> bool
        """
        return False

    def parseContinue(self): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.parseContinue() -> bool """
        return False

    def property(self, QString): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.property(QString) -> (sip.voidptr, bool) """
        pass

    def setContentHandler(self, QXmlContentHandler): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.setContentHandler(QXmlContentHandler) """
        pass

    def setDeclHandler(self, QXmlDeclHandler): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.setDeclHandler(QXmlDeclHandler) """
        pass

    def setDTDHandler(self, QXmlDTDHandler): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.setDTDHandler(QXmlDTDHandler) """
        pass

    def setEntityResolver(self, QXmlEntityResolver): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.setEntityResolver(QXmlEntityResolver) """
        pass

    def setErrorHandler(self, QXmlErrorHandler): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.setErrorHandler(QXmlErrorHandler) """
        pass

    def setFeature(self, QString, bool): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.setFeature(QString, bool) """
        pass

    def setLexicalHandler(self, QXmlLexicalHandler): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.setLexicalHandler(QXmlLexicalHandler) """
        pass

    def setProperty(self, QString, sip_voidptr): # real signature unknown; restored from __doc__
        """ QXmlSimpleReader.setProperty(QString, sip.voidptr) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


