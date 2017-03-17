# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QImageWriter(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QImageWriter()
    QImageWriter(QIODevice, QByteArray)
    QImageWriter(QString, QByteArray format=QByteArray())
    """
    def canWrite(self): # real signature unknown; restored from __doc__
        """ QImageWriter.canWrite() -> bool """
        return False

    def compression(self): # real signature unknown; restored from __doc__
        """ QImageWriter.compression() -> int """
        return 0

    def description(self): # real signature unknown; restored from __doc__
        """ QImageWriter.description() -> QString """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ QImageWriter.device() -> QIODevice """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QImageWriter.error() -> QImageWriter.ImageWriterError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QImageWriter.errorString() -> QString """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ QImageWriter.fileName() -> QString """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ QImageWriter.format() -> QByteArray """
        pass

    def gamma(self): # real signature unknown; restored from __doc__
        """ QImageWriter.gamma() -> float """
        return 0.0

    def quality(self): # real signature unknown; restored from __doc__
        """ QImageWriter.quality() -> int """
        return 0

    def setCompression(self, p_int): # real signature unknown; restored from __doc__
        """ QImageWriter.setCompression(int) """
        pass

    def setDescription(self, QString): # real signature unknown; restored from __doc__
        """ QImageWriter.setDescription(QString) """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ QImageWriter.setDevice(QIODevice) """
        pass

    def setFileName(self, QString): # real signature unknown; restored from __doc__
        """ QImageWriter.setFileName(QString) """
        pass

    def setFormat(self, QByteArray): # real signature unknown; restored from __doc__
        """ QImageWriter.setFormat(QByteArray) """
        pass

    def setGamma(self, p_float): # real signature unknown; restored from __doc__
        """ QImageWriter.setGamma(float) """
        pass

    def setQuality(self, p_int): # real signature unknown; restored from __doc__
        """ QImageWriter.setQuality(int) """
        pass

    def setText(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QImageWriter.setText(QString, QString) """
        pass

    def supportedImageFormats(self): # real signature unknown; restored from __doc__
        """ QImageWriter.supportedImageFormats() -> list-of-QByteArray """
        pass

    def supportsOption(self, QImageIOHandler_ImageOption): # real signature unknown; restored from __doc__
        """ QImageWriter.supportsOption(QImageIOHandler.ImageOption) -> bool """
        return False

    def write(self, QImage): # real signature unknown; restored from __doc__
        """ QImageWriter.write(QImage) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DeviceError = 1
    UnknownError = 0
    UnsupportedFormatError = 2


