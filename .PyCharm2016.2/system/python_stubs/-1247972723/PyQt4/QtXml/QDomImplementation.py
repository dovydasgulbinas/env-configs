# encoding: utf-8
# module PyQt4.QtXml
# from /usr/lib/python2.7/dist-packages/PyQt4/QtXml.so
# by generator 1.143
# no doc
# no imports

class QDomImplementation(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDomImplementation()
    QDomImplementation(QDomImplementation)
    """
    def createDocument(self, QString, QString_1, QDomDocumentType): # real signature unknown; restored from __doc__
        """ QDomImplementation.createDocument(QString, QString, QDomDocumentType) -> QDomDocument """
        return QDomDocument

    def createDocumentType(self, QString, QString_1, QString_2): # real signature unknown; restored from __doc__
        """ QDomImplementation.createDocumentType(QString, QString, QString) -> QDomDocumentType """
        return QDomDocumentType

    def hasFeature(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDomImplementation.hasFeature(QString, QString) -> bool """
        return False

    def invalidDataPolicy(self): # real signature unknown; restored from __doc__
        """ QDomImplementation.invalidDataPolicy() -> QDomImplementation.InvalidDataPolicy """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ QDomImplementation.isNull() -> bool """
        return False

    def setInvalidDataPolicy(self, QDomImplementation_InvalidDataPolicy): # real signature unknown; restored from __doc__
        """ QDomImplementation.setInvalidDataPolicy(QDomImplementation.InvalidDataPolicy) """
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

    def __init__(self, QDomImplementation=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    AcceptInvalidChars = 0
    DropInvalidChars = 1
    ReturnNullNode = 2


