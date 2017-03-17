# encoding: utf-8
# module PyQt4.QtSvg
# from /usr/lib/python2.7/dist-packages/PyQt4/QtSvg.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


# no functions
# classes

class QGraphicsSvgItem(__PyQt4_QtGui.QGraphicsObject):
    """
    QGraphicsSvgItem(QGraphicsItem parent=None)
    QGraphicsSvgItem(QString, QGraphicsItem parent=None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.boundingRect() -> QRectF """
        pass

    def elementId(self): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.elementId() -> QString """
        pass

    def isCachingEnabled(self): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.isCachingEnabled() -> bool """
        return False

    def maximumCacheSize(self): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.maximumCacheSize() -> QSize """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def renderer(self): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.renderer() -> QSvgRenderer """
        return QSvgRenderer

    def setCachingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.setCachingEnabled(bool) """
        pass

    def setElementId(self, QString): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.setElementId(QString) """
        pass

    def setMaximumCacheSize(self, QSize): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.setMaximumCacheSize(QSize) """
        pass

    def setSharedRenderer(self, QSvgRenderer): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.setSharedRenderer(QSvgRenderer) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsSvgItem.type() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSvgGenerator(__PyQt4_QtGui.QPaintDevice):
    """ QSvgGenerator() """
    def description(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.description() -> QString """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.fileName() -> QString """
        pass

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ QSvgGenerator.metric(QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def outputDevice(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.outputDevice() -> QIODevice """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.paintEngine() -> QPaintEngine """
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.resolution() -> int """
        return 0

    def setDescription(self, QString): # real signature unknown; restored from __doc__
        """ QSvgGenerator.setDescription(QString) """
        pass

    def setFileName(self, QString): # real signature unknown; restored from __doc__
        """ QSvgGenerator.setFileName(QString) """
        pass

    def setOutputDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ QSvgGenerator.setOutputDevice(QIODevice) """
        pass

    def setResolution(self, p_int): # real signature unknown; restored from __doc__
        """ QSvgGenerator.setResolution(int) """
        pass

    def setSize(self, QSize): # real signature unknown; restored from __doc__
        """ QSvgGenerator.setSize(QSize) """
        pass

    def setTitle(self, QString): # real signature unknown; restored from __doc__
        """ QSvgGenerator.setTitle(QString) """
        pass

    def setViewBox(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSvgGenerator.setViewBox(QRect)
        QSvgGenerator.setViewBox(QRectF)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.size() -> QSize """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.title() -> QString """
        pass

    def viewBox(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.viewBox() -> QRect """
        pass

    def viewBoxF(self): # real signature unknown; restored from __doc__
        """ QSvgGenerator.viewBoxF() -> QRectF """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


class QSvgRenderer(__PyQt4_QtCore.QObject):
    """
    QSvgRenderer(QObject parent=None)
    QSvgRenderer(QString, QObject parent=None)
    QSvgRenderer(QByteArray, QObject parent=None)
    QSvgRenderer(QXmlStreamReader, QObject parent=None)
    """
    def animated(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.animated() -> bool """
        return False

    def animationDuration(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.animationDuration() -> int """
        return 0

    def boundsOnElement(self, QString): # real signature unknown; restored from __doc__
        """ QSvgRenderer.boundsOnElement(QString) -> QRectF """
        pass

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.currentFrame() -> int """
        return 0

    def defaultSize(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.defaultSize() -> QSize """
        pass

    def elementExists(self, QString): # real signature unknown; restored from __doc__
        """ QSvgRenderer.elementExists(QString) -> bool """
        return False

    def framesPerSecond(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.framesPerSecond() -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.isValid() -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSvgRenderer.load(QString) -> bool
        QSvgRenderer.load(QByteArray) -> bool
        QSvgRenderer.load(QXmlStreamReader) -> bool
        """
        return False

    def matrixForElement(self, QString): # real signature unknown; restored from __doc__
        """ QSvgRenderer.matrixForElement(QString) -> QMatrix """
        pass

    def render(self, QPainter, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSvgRenderer.render(QPainter)
        QSvgRenderer.render(QPainter, QRectF)
        QSvgRenderer.render(QPainter, QString, QRectF bounds=QRectF())
        """
        pass

    def repaintNeeded(self, *args, **kwargs): # real signature unknown
        """ QSvgRenderer.repaintNeeded [signal] """
        pass

    def setCurrentFrame(self, p_int): # real signature unknown; restored from __doc__
        """ QSvgRenderer.setCurrentFrame(int) """
        pass

    def setFramesPerSecond(self, p_int): # real signature unknown; restored from __doc__
        """ QSvgRenderer.setFramesPerSecond(int) """
        pass

    def setViewBox(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSvgRenderer.setViewBox(QRect)
        QSvgRenderer.setViewBox(QRectF)
        """
        pass

    def viewBox(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.viewBox() -> QRect """
        pass

    def viewBoxF(self): # real signature unknown; restored from __doc__
        """ QSvgRenderer.viewBoxF() -> QRectF """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSvgWidget(__PyQt4_QtGui.QWidget):
    """
    QSvgWidget(QWidget parent=None)
    QSvgWidget(QString, QWidget parent=None)
    """
    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSvgWidget.load(QString)
        QSvgWidget.load(QByteArray)
        """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QSvgWidget.paintEvent(QPaintEvent) """
        pass

    def renderer(self): # real signature unknown; restored from __doc__
        """ QSvgWidget.renderer() -> QSvgRenderer """
        return QSvgRenderer

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QSvgWidget.sizeHint() -> QSize """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


