# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QImageIOHandler(): # skipped bases: <type 'sip.simplewrapper'>
    """ QImageIOHandler() """
    def canRead(self): # real signature unknown; restored from __doc__
        """ QImageIOHandler.canRead() -> bool """
        return False

    def currentImageNumber(self): # real signature unknown; restored from __doc__
        """ QImageIOHandler.currentImageNumber() -> int """
        return 0

    def currentImageRect(self): # real signature unknown; restored from __doc__
        """ QImageIOHandler.currentImageRect() -> QRect """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ QImageIOHandler.device() -> QIODevice """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ QImageIOHandler.format() -> QByteArray """
        pass

    def imageCount(self): # real signature unknown; restored from __doc__
        """ QImageIOHandler.imageCount() -> int """
        return 0

    def jumpToImage(self, p_int): # real signature unknown; restored from __doc__
        """ QImageIOHandler.jumpToImage(int) -> bool """
        return False

    def jumpToNextImage(self): # real signature unknown; restored from __doc__
        """ QImageIOHandler.jumpToNextImage() -> bool """
        return False

    def loopCount(self): # real signature unknown; restored from __doc__
        """ QImageIOHandler.loopCount() -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ QImageIOHandler.name() -> QByteArray """
        pass

    def nextImageDelay(self): # real signature unknown; restored from __doc__
        """ QImageIOHandler.nextImageDelay() -> int """
        return 0

    def option(self, QImageIOHandler_ImageOption): # real signature unknown; restored from __doc__
        """ QImageIOHandler.option(QImageIOHandler.ImageOption) -> QVariant """
        pass

    def read(self, QImage): # real signature unknown; restored from __doc__
        """ QImageIOHandler.read(QImage) -> bool """
        return False

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ QImageIOHandler.setDevice(QIODevice) """
        pass

    def setFormat(self, QByteArray): # real signature unknown; restored from __doc__
        """ QImageIOHandler.setFormat(QByteArray) """
        pass

    def setOption(self, QImageIOHandler_ImageOption, QVariant): # real signature unknown; restored from __doc__
        """ QImageIOHandler.setOption(QImageIOHandler.ImageOption, QVariant) """
        pass

    def supportsOption(self, QImageIOHandler_ImageOption): # real signature unknown; restored from __doc__
        """ QImageIOHandler.supportsOption(QImageIOHandler.ImageOption) -> bool """
        return False

    def write(self, QImage): # real signature unknown; restored from __doc__
        """ QImageIOHandler.write(QImage) -> bool """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Animation = 12
    BackgroundColor = 13
    ClipRect = 1
    CompressionRatio = 5
    Description = 2
    Endianness = 11
    Gamma = 6
    IncrementalReading = 10
    Name = 8
    Quality = 7
    ScaledClipRect = 3
    ScaledSize = 4
    Size = 0
    SubType = 9


