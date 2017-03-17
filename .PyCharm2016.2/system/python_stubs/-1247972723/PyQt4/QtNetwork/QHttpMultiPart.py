# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QHttpMultiPart(__PyQt4_QtCore.QObject):
    """
    QHttpMultiPart(QObject parent=None)
    QHttpMultiPart(QHttpMultiPart.ContentType, QObject parent=None)
    """
    def append(self, QHttpPart): # real signature unknown; restored from __doc__
        """ QHttpMultiPart.append(QHttpPart) """
        pass

    def boundary(self): # real signature unknown; restored from __doc__
        """ QHttpMultiPart.boundary() -> QByteArray """
        pass

    def setBoundary(self, QByteArray): # real signature unknown; restored from __doc__
        """ QHttpMultiPart.setBoundary(QByteArray) """
        pass

    def setContentType(self, QHttpMultiPart_ContentType): # real signature unknown; restored from __doc__
        """ QHttpMultiPart.setContentType(QHttpMultiPart.ContentType) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AlternativeType = 3
    FormDataType = 2
    MixedType = 0
    RelatedType = 1


