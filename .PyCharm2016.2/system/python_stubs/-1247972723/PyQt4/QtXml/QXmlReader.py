# encoding: utf-8
# module PyQt4.QtXml
# from /usr/lib/python2.7/dist-packages/PyQt4/QtXml.so
# by generator 1.143
# no doc
# no imports

class QXmlReader(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QXmlReader()
    QXmlReader(QXmlReader)
    """
    def contentHandler(self): # real signature unknown; restored from __doc__
        """ QXmlReader.contentHandler() -> QXmlContentHandler """
        return QXmlContentHandler

    def declHandler(self): # real signature unknown; restored from __doc__
        """ QXmlReader.declHandler() -> QXmlDeclHandler """
        return QXmlDeclHandler

    def DTDHandler(self): # real signature unknown; restored from __doc__
        """ QXmlReader.DTDHandler() -> QXmlDTDHandler """
        return QXmlDTDHandler

    def entityResolver(self): # real signature unknown; restored from __doc__
        """ QXmlReader.entityResolver() -> QXmlEntityResolver """
        return QXmlEntityResolver

    def errorHandler(self): # real signature unknown; restored from __doc__
        """ QXmlReader.errorHandler() -> QXmlErrorHandler """
        return QXmlErrorHandler

    def feature(self, QString): # real signature unknown; restored from __doc__
        """ QXmlReader.feature(QString) -> (bool, bool) """
        pass

    def hasFeature(self, QString): # real signature unknown; restored from __doc__
        """ QXmlReader.hasFeature(QString) -> bool """
        return False

    def hasProperty(self, QString): # real signature unknown; restored from __doc__
        """ QXmlReader.hasProperty(QString) -> bool """
        return False

    def lexicalHandler(self): # real signature unknown; restored from __doc__
        """ QXmlReader.lexicalHandler() -> QXmlLexicalHandler """
        return QXmlLexicalHandler

    def parse(self, QXmlInputSource): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlReader.parse(QXmlInputSource) -> bool
        QXmlReader.parse(QXmlInputSource) -> bool
        """
        return False

    def property(self, QString): # real signature unknown; restored from __doc__
        """ QXmlReader.property(QString) -> (sip.voidptr, bool) """
        pass

    def setContentHandler(self, QXmlContentHandler): # real signature unknown; restored from __doc__
        """ QXmlReader.setContentHandler(QXmlContentHandler) """
        pass

    def setDeclHandler(self, QXmlDeclHandler): # real signature unknown; restored from __doc__
        """ QXmlReader.setDeclHandler(QXmlDeclHandler) """
        pass

    def setDTDHandler(self, QXmlDTDHandler): # real signature unknown; restored from __doc__
        """ QXmlReader.setDTDHandler(QXmlDTDHandler) """
        pass

    def setEntityResolver(self, QXmlEntityResolver): # real signature unknown; restored from __doc__
        """ QXmlReader.setEntityResolver(QXmlEntityResolver) """
        pass

    def setErrorHandler(self, QXmlErrorHandler): # real signature unknown; restored from __doc__
        """ QXmlReader.setErrorHandler(QXmlErrorHandler) """
        pass

    def setFeature(self, QString, bool): # real signature unknown; restored from __doc__
        """ QXmlReader.setFeature(QString, bool) """
        pass

    def setLexicalHandler(self, QXmlLexicalHandler): # real signature unknown; restored from __doc__
        """ QXmlReader.setLexicalHandler(QXmlLexicalHandler) """
        pass

    def setProperty(self, QString, sip_voidptr): # real signature unknown; restored from __doc__
        """ QXmlReader.setProperty(QString, sip.voidptr) """
        pass

    def __init__(self, QXmlReader=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



