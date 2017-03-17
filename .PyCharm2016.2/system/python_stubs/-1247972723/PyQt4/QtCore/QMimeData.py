# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QMimeData(QObject):
    """ QMimeData() """
    def clear(self): # real signature unknown; restored from __doc__
        """ QMimeData.clear() """
        pass

    def colorData(self): # real signature unknown; restored from __doc__
        """ QMimeData.colorData() -> QVariant """
        return QVariant

    def data(self, QString): # real signature unknown; restored from __doc__
        """ QMimeData.data(QString) -> QByteArray """
        return QByteArray

    def formats(self): # real signature unknown; restored from __doc__
        """ QMimeData.formats() -> QStringList """
        return QStringList

    def hasColor(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasColor() -> bool """
        return False

    def hasFormat(self, QString): # real signature unknown; restored from __doc__
        """ QMimeData.hasFormat(QString) -> bool """
        return False

    def hasHtml(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasHtml() -> bool """
        return False

    def hasImage(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasImage() -> bool """
        return False

    def hasText(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasText() -> bool """
        return False

    def hasUrls(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasUrls() -> bool """
        return False

    def html(self): # real signature unknown; restored from __doc__
        """ QMimeData.html() -> QString """
        return QString

    def imageData(self): # real signature unknown; restored from __doc__
        """ QMimeData.imageData() -> QVariant """
        return QVariant

    def removeFormat(self, QString): # real signature unknown; restored from __doc__
        """ QMimeData.removeFormat(QString) """
        pass

    def retrieveData(self, QString, Type): # real signature unknown; restored from __doc__
        """ QMimeData.retrieveData(QString, Type) -> QVariant """
        return QVariant

    def setColorData(self, QVariant): # real signature unknown; restored from __doc__
        """ QMimeData.setColorData(QVariant) """
        pass

    def setData(self, QString, QByteArray): # real signature unknown; restored from __doc__
        """ QMimeData.setData(QString, QByteArray) """
        pass

    def setHtml(self, QString): # real signature unknown; restored from __doc__
        """ QMimeData.setHtml(QString) """
        pass

    def setImageData(self, QVariant): # real signature unknown; restored from __doc__
        """ QMimeData.setImageData(QVariant) """
        pass

    def setText(self, QString): # real signature unknown; restored from __doc__
        """ QMimeData.setText(QString) """
        pass

    def setUrls(self, list_of_QUrl): # real signature unknown; restored from __doc__
        """ QMimeData.setUrls(list-of-QUrl) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QMimeData.text() -> QString """
        return QString

    def urls(self): # real signature unknown; restored from __doc__
        """ QMimeData.urls() -> list-of-QUrl """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


