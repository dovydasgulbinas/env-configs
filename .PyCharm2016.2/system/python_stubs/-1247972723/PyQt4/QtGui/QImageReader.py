# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QImageReader(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QImageReader()
    QImageReader(QIODevice, QByteArray format=QByteArray())
    QImageReader(QString, QByteArray format=QByteArray())
    """
    def autoDetectImageFormat(self): # real signature unknown; restored from __doc__
        """ QImageReader.autoDetectImageFormat() -> bool """
        return False

    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ QImageReader.backgroundColor() -> QColor """
        return QColor

    def canRead(self): # real signature unknown; restored from __doc__
        """ QImageReader.canRead() -> bool """
        return False

    def clipRect(self): # real signature unknown; restored from __doc__
        """ QImageReader.clipRect() -> QRect """
        pass

    def currentImageNumber(self): # real signature unknown; restored from __doc__
        """ QImageReader.currentImageNumber() -> int """
        return 0

    def currentImageRect(self): # real signature unknown; restored from __doc__
        """ QImageReader.currentImageRect() -> QRect """
        pass

    def decideFormatFromContent(self): # real signature unknown; restored from __doc__
        """ QImageReader.decideFormatFromContent() -> bool """
        return False

    def device(self): # real signature unknown; restored from __doc__
        """ QImageReader.device() -> QIODevice """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QImageReader.error() -> QImageReader.ImageReaderError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QImageReader.errorString() -> QString """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ QImageReader.fileName() -> QString """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ QImageReader.format() -> QByteArray """
        pass

    def imageCount(self): # real signature unknown; restored from __doc__
        """ QImageReader.imageCount() -> int """
        return 0

    def imageFormat(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImageReader.imageFormat(QString) -> QByteArray
        QImageReader.imageFormat(QIODevice) -> QByteArray
        QImageReader.imageFormat() -> QImage.Format
        """
        pass

    def jumpToImage(self, p_int): # real signature unknown; restored from __doc__
        """ QImageReader.jumpToImage(int) -> bool """
        return False

    def jumpToNextImage(self): # real signature unknown; restored from __doc__
        """ QImageReader.jumpToNextImage() -> bool """
        return False

    def loopCount(self): # real signature unknown; restored from __doc__
        """ QImageReader.loopCount() -> int """
        return 0

    def nextImageDelay(self): # real signature unknown; restored from __doc__
        """ QImageReader.nextImageDelay() -> int """
        return 0

    def quality(self): # real signature unknown; restored from __doc__
        """ QImageReader.quality() -> int """
        return 0

    def read(self, QImage=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImageReader.read() -> QImage
        QImageReader.read(QImage) -> bool
        """
        return QImage or False

    def scaledClipRect(self): # real signature unknown; restored from __doc__
        """ QImageReader.scaledClipRect() -> QRect """
        pass

    def scaledSize(self): # real signature unknown; restored from __doc__
        """ QImageReader.scaledSize() -> QSize """
        pass

    def setAutoDetectImageFormat(self, bool): # real signature unknown; restored from __doc__
        """ QImageReader.setAutoDetectImageFormat(bool) """
        pass

    def setBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QImageReader.setBackgroundColor(QColor) """
        pass

    def setClipRect(self, QRect): # real signature unknown; restored from __doc__
        """ QImageReader.setClipRect(QRect) """
        pass

    def setDecideFormatFromContent(self, bool): # real signature unknown; restored from __doc__
        """ QImageReader.setDecideFormatFromContent(bool) """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ QImageReader.setDevice(QIODevice) """
        pass

    def setFileName(self, QString): # real signature unknown; restored from __doc__
        """ QImageReader.setFileName(QString) """
        pass

    def setFormat(self, QByteArray): # real signature unknown; restored from __doc__
        """ QImageReader.setFormat(QByteArray) """
        pass

    def setQuality(self, p_int): # real signature unknown; restored from __doc__
        """ QImageReader.setQuality(int) """
        pass

    def setScaledClipRect(self, QRect): # real signature unknown; restored from __doc__
        """ QImageReader.setScaledClipRect(QRect) """
        pass

    def setScaledSize(self, QSize): # real signature unknown; restored from __doc__
        """ QImageReader.setScaledSize(QSize) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QImageReader.size() -> QSize """
        pass

    def supportedImageFormats(self): # real signature unknown; restored from __doc__
        """ QImageReader.supportedImageFormats() -> list-of-QByteArray """
        pass

    def supportsAnimation(self): # real signature unknown; restored from __doc__
        """ QImageReader.supportsAnimation() -> bool """
        return False

    def supportsOption(self, QImageIOHandler_ImageOption): # real signature unknown; restored from __doc__
        """ QImageReader.supportsOption(QImageIOHandler.ImageOption) -> bool """
        return False

    def text(self, QString): # real signature unknown; restored from __doc__
        """ QImageReader.text(QString) -> QString """
        pass

    def textKeys(self): # real signature unknown; restored from __doc__
        """ QImageReader.textKeys() -> QStringList """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DeviceError = 2
    FileNotFoundError = 1
    InvalidDataError = 4
    UnknownError = 0
    UnsupportedFormatError = 3


