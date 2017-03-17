# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QXmlStreamWriter(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QXmlStreamWriter()
    QXmlStreamWriter(QIODevice)
    QXmlStreamWriter(QByteArray)
    QXmlStreamWriter(QString)
    """
    def autoFormatting(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.autoFormatting() -> bool """
        return False

    def autoFormattingIndent(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.autoFormattingIndent() -> int """
        return 0

    def codec(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.codec() -> QTextCodec """
        return QTextCodec

    def device(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.device() -> QIODevice """
        return QIODevice

    def hasError(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.hasError() -> bool """
        return False

    def setAutoFormatting(self, bool): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.setAutoFormatting(bool) """
        pass

    def setAutoFormattingIndent(self, p_int): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.setAutoFormattingIndent(int) """
        pass

    def setCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamWriter.setCodec(QTextCodec)
        QXmlStreamWriter.setCodec(str)
        """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.setDevice(QIODevice) """
        pass

    def writeAttribute(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamWriter.writeAttribute(QString, QString)
        QXmlStreamWriter.writeAttribute(QString, QString, QString)
        QXmlStreamWriter.writeAttribute(QXmlStreamAttribute)
        """
        pass

    def writeAttributes(self, QXmlStreamAttributes): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeAttributes(QXmlStreamAttributes) """
        pass

    def writeCDATA(self, QString): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeCDATA(QString) """
        pass

    def writeCharacters(self, QString): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeCharacters(QString) """
        pass

    def writeComment(self, QString): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeComment(QString) """
        pass

    def writeCurrentToken(self, QXmlStreamReader): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeCurrentToken(QXmlStreamReader) """
        pass

    def writeDefaultNamespace(self, QString): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeDefaultNamespace(QString) """
        pass

    def writeDTD(self, QString): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeDTD(QString) """
        pass

    def writeEmptyElement(self, QString, QString_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamWriter.writeEmptyElement(QString)
        QXmlStreamWriter.writeEmptyElement(QString, QString)
        """
        pass

    def writeEndDocument(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeEndDocument() """
        pass

    def writeEndElement(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeEndElement() """
        pass

    def writeEntityReference(self, QString): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeEntityReference(QString) """
        pass

    def writeNamespace(self, QString, QString_prefix=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QXmlStreamWriter.writeNamespace(QString, QString prefix=QString()) """
        pass

    def writeProcessingInstruction(self, QString, QString_data=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QXmlStreamWriter.writeProcessingInstruction(QString, QString data=QString()) """
        pass

    def writeStartDocument(self, QString=None, bool=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamWriter.writeStartDocument()
        QXmlStreamWriter.writeStartDocument(QString)
        QXmlStreamWriter.writeStartDocument(QString, bool)
        """
        pass

    def writeStartElement(self, QString, QString_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamWriter.writeStartElement(QString)
        QXmlStreamWriter.writeStartElement(QString, QString)
        """
        pass

    def writeTextElement(self, QString, QString_1, QString_2=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamWriter.writeTextElement(QString, QString)
        QXmlStreamWriter.writeTextElement(QString, QString, QString)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



