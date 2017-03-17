# encoding: utf-8
# module PyQt4.QtXml
# from /usr/lib/python2.7/dist-packages/PyQt4/QtXml.so
# by generator 1.143
# no doc
# no imports

from QDomNode import QDomNode

class QDomElement(QDomNode):
    """
    QDomElement()
    QDomElement(QDomElement)
    """
    def attribute(self, QString, QString_defaultValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDomElement.attribute(QString, QString defaultValue=QString()) -> QString """
        pass

    def attributeNode(self, QString): # real signature unknown; restored from __doc__
        """ QDomElement.attributeNode(QString) -> QDomAttr """
        return QDomAttr

    def attributeNodeNS(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDomElement.attributeNodeNS(QString, QString) -> QDomAttr """
        return QDomAttr

    def attributeNS(self, QString, QString_1, QString_defaultValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDomElement.attributeNS(QString, QString, QString defaultValue=QString()) -> QString """
        pass

    def attributes(self): # real signature unknown; restored from __doc__
        """ QDomElement.attributes() -> QDomNamedNodeMap """
        return QDomNamedNodeMap

    def elementsByTagName(self, QString): # real signature unknown; restored from __doc__
        """ QDomElement.elementsByTagName(QString) -> QDomNodeList """
        return QDomNodeList

    def elementsByTagNameNS(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDomElement.elementsByTagNameNS(QString, QString) -> QDomNodeList """
        return QDomNodeList

    def hasAttribute(self, QString): # real signature unknown; restored from __doc__
        """ QDomElement.hasAttribute(QString) -> bool """
        return False

    def hasAttributeNS(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDomElement.hasAttributeNS(QString, QString) -> bool """
        return False

    def nodeType(self): # real signature unknown; restored from __doc__
        """ QDomElement.nodeType() -> QDomNode.NodeType """
        pass

    def removeAttribute(self, QString): # real signature unknown; restored from __doc__
        """ QDomElement.removeAttribute(QString) """
        pass

    def removeAttributeNode(self, QDomAttr): # real signature unknown; restored from __doc__
        """ QDomElement.removeAttributeNode(QDomAttr) -> QDomAttr """
        return QDomAttr

    def removeAttributeNS(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDomElement.removeAttributeNS(QString, QString) """
        pass

    def setAttribute(self, QString, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDomElement.setAttribute(QString, QString)
        QDomElement.setAttribute(QString, int)
        QDomElement.setAttribute(QString, int)
        QDomElement.setAttribute(QString, float)
        QDomElement.setAttribute(QString, int)
        """
        pass

    def setAttributeNode(self, QDomAttr): # real signature unknown; restored from __doc__
        """ QDomElement.setAttributeNode(QDomAttr) -> QDomAttr """
        return QDomAttr

    def setAttributeNodeNS(self, QDomAttr): # real signature unknown; restored from __doc__
        """ QDomElement.setAttributeNodeNS(QDomAttr) -> QDomAttr """
        return QDomAttr

    def setAttributeNS(self, QString, QString_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDomElement.setAttributeNS(QString, QString, QString)
        QDomElement.setAttributeNS(QString, QString, int)
        QDomElement.setAttributeNS(QString, QString, int)
        QDomElement.setAttributeNS(QString, QString, float)
        QDomElement.setAttributeNS(QString, QString, int)
        """
        pass

    def setTagName(self, QString): # real signature unknown; restored from __doc__
        """ QDomElement.setTagName(QString) """
        pass

    def tagName(self): # real signature unknown; restored from __doc__
        """ QDomElement.tagName() -> QString """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QDomElement.text() -> QString """
        pass

    def __init__(self, QDomElement=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass


