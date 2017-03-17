# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QMovie(__PyQt4_QtCore.QObject):
    """
    QMovie(QObject parent=None)
    QMovie(QIODevice, QByteArray format=QByteArray(), QObject parent=None)
    QMovie(QString, QByteArray format=QByteArray(), QObject parent=None)
    """
    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ QMovie.backgroundColor() -> QColor """
        return QColor

    def cacheMode(self): # real signature unknown; restored from __doc__
        """ QMovie.cacheMode() -> QMovie.CacheMode """
        pass

    def currentFrameNumber(self): # real signature unknown; restored from __doc__
        """ QMovie.currentFrameNumber() -> int """
        return 0

    def currentImage(self): # real signature unknown; restored from __doc__
        """ QMovie.currentImage() -> QImage """
        return QImage

    def currentPixmap(self): # real signature unknown; restored from __doc__
        """ QMovie.currentPixmap() -> QPixmap """
        return QPixmap

    def device(self): # real signature unknown; restored from __doc__
        """ QMovie.device() -> QIODevice """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        """ QMovie.error[QImageReader.ImageReaderError] [signal] """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ QMovie.fileName() -> QString """
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        """ QMovie.finished [signal] """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ QMovie.format() -> QByteArray """
        pass

    def frameChanged(self, *args, **kwargs): # real signature unknown
        """ QMovie.frameChanged[int] [signal] """
        pass

    def frameCount(self): # real signature unknown; restored from __doc__
        """ QMovie.frameCount() -> int """
        return 0

    def frameRect(self): # real signature unknown; restored from __doc__
        """ QMovie.frameRect() -> QRect """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ QMovie.isValid() -> bool """
        return False

    def jumpToFrame(self, p_int): # real signature unknown; restored from __doc__
        """ QMovie.jumpToFrame(int) -> bool """
        return False

    def jumpToNextFrame(self): # real signature unknown; restored from __doc__
        """ QMovie.jumpToNextFrame() -> bool """
        return False

    def loopCount(self): # real signature unknown; restored from __doc__
        """ QMovie.loopCount() -> int """
        return 0

    def nextFrameDelay(self): # real signature unknown; restored from __doc__
        """ QMovie.nextFrameDelay() -> int """
        return 0

    def resized(self, *args, **kwargs): # real signature unknown
        """ QMovie.resized[QSize] [signal] """
        pass

    def scaledSize(self): # real signature unknown; restored from __doc__
        """ QMovie.scaledSize() -> QSize """
        pass

    def setBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QMovie.setBackgroundColor(QColor) """
        pass

    def setCacheMode(self, QMovie_CacheMode): # real signature unknown; restored from __doc__
        """ QMovie.setCacheMode(QMovie.CacheMode) """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ QMovie.setDevice(QIODevice) """
        pass

    def setFileName(self, QString): # real signature unknown; restored from __doc__
        """ QMovie.setFileName(QString) """
        pass

    def setFormat(self, QByteArray): # real signature unknown; restored from __doc__
        """ QMovie.setFormat(QByteArray) """
        pass

    def setPaused(self, bool): # real signature unknown; restored from __doc__
        """ QMovie.setPaused(bool) """
        pass

    def setScaledSize(self, QSize): # real signature unknown; restored from __doc__
        """ QMovie.setScaledSize(QSize) """
        pass

    def setSpeed(self, p_int): # real signature unknown; restored from __doc__
        """ QMovie.setSpeed(int) """
        pass

    def speed(self): # real signature unknown; restored from __doc__
        """ QMovie.speed() -> int """
        return 0

    def start(self): # real signature unknown; restored from __doc__
        """ QMovie.start() """
        pass

    def started(self, *args, **kwargs): # real signature unknown
        """ QMovie.started [signal] """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QMovie.state() -> QMovie.MovieState """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QMovie.stateChanged[QMovie.MovieState] [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ QMovie.stop() """
        pass

    def supportedFormats(self): # real signature unknown; restored from __doc__
        """ QMovie.supportedFormats() -> list-of-QByteArray """
        pass

    def updated(self, *args, **kwargs): # real signature unknown
        """ QMovie.updated[QRect] [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    CacheAll = 1
    CacheNone = 0
    NotRunning = 0
    Paused = 1
    Running = 2


