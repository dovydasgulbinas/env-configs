# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QPaintDevice import QPaintDevice

class QPixmap(QPaintDevice):
    """
    QPixmap()
    QPixmap(int, int)
    QPixmap(QSize)
    QPixmap(QString, str format=None, Qt.ImageConversionFlags flags=Qt.AutoColor)
    QPixmap(list-of-str)
    QPixmap(QPixmap)
    QPixmap(QVariant)
    """
    def alphaChannel(self): # real signature unknown; restored from __doc__
        """ QPixmap.alphaChannel() -> QPixmap """
        return QPixmap

    def cacheKey(self): # real signature unknown; restored from __doc__
        """ QPixmap.cacheKey() -> int """
        return 0

    def convertFromImage(self, QImage, Qt_ImageConversionFlags_flags=None): # real signature unknown; restored from __doc__
        """ QPixmap.convertFromImage(QImage, Qt.ImageConversionFlags flags=Qt.AutoColor) -> bool """
        return False

    def copy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmap.copy(QRect rect=QRect()) -> QPixmap
        QPixmap.copy(int, int, int, int) -> QPixmap
        """
        return QPixmap

    def createHeuristicMask(self, bool_clipTight=True): # real signature unknown; restored from __doc__
        """ QPixmap.createHeuristicMask(bool clipTight=True) -> QBitmap """
        return QBitmap

    def createMaskFromColor(self, QColor, Qt_MaskMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmap.createMaskFromColor(QColor, Qt.MaskMode) -> QBitmap
        QPixmap.createMaskFromColor(QColor) -> QBitmap
        """
        return QBitmap

    def defaultDepth(self): # real signature unknown; restored from __doc__
        """ QPixmap.defaultDepth() -> int """
        return 0

    def depth(self): # real signature unknown; restored from __doc__
        """ QPixmap.depth() -> int """
        return 0

    def detach(self): # real signature unknown; restored from __doc__
        """ QPixmap.detach() """
        pass

    def devType(self): # real signature unknown; restored from __doc__
        """ QPixmap.devType() -> int """
        return 0

    def fill(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmap.fill(QColor color=Qt.white)
        QPixmap.fill(QWidget, QPoint)
        QPixmap.fill(QWidget, int, int)
        """
        pass

    def fromImage(self, QImage, Qt_ImageConversionFlags_flags=None): # real signature unknown; restored from __doc__
        """ QPixmap.fromImage(QImage, Qt.ImageConversionFlags flags=Qt.AutoColor) -> QPixmap """
        return QPixmap

    def fromImageReader(self, QImageReader, Qt_ImageConversionFlags_flags=None): # real signature unknown; restored from __doc__
        """ QPixmap.fromImageReader(QImageReader, Qt.ImageConversionFlags flags=Qt.AutoColor) -> QPixmap """
        return QPixmap

    def fromX11Pixmap(self, p_int, QPixmap_ShareMode_mode=None): # real signature unknown; restored from __doc__
        """ QPixmap.fromX11Pixmap(int, QPixmap.ShareMode mode=QPixmap.ImplicitlyShared) -> QPixmap """
        return QPixmap

    def grabWidget(self, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmap.grabWidget(QWidget, QRect) -> QPixmap
        QPixmap.grabWidget(QWidget, int x=0, int y=0, int width=-1, int height=-1) -> QPixmap
        """
        return QPixmap

    def grabWindow(self, p_int, int_x=0, int_y=0, int_width=-1, int_height=-1): # real signature unknown; restored from __doc__
        """ QPixmap.grabWindow(int, int x=0, int y=0, int width=-1, int height=-1) -> QPixmap """
        return QPixmap

    def handle(self): # real signature unknown; restored from __doc__
        """ QPixmap.handle() -> int """
        return 0

    def hasAlpha(self): # real signature unknown; restored from __doc__
        """ QPixmap.hasAlpha() -> bool """
        return False

    def hasAlphaChannel(self): # real signature unknown; restored from __doc__
        """ QPixmap.hasAlphaChannel() -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ QPixmap.height() -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ QPixmap.isNull() -> bool """
        return False

    def isQBitmap(self): # real signature unknown; restored from __doc__
        """ QPixmap.isQBitmap() -> bool """
        return False

    def load(self, QString, str_format=None, Qt_ImageConversionFlags_flags=None): # real signature unknown; restored from __doc__
        """ QPixmap.load(QString, str format=None, Qt.ImageConversionFlags flags=Qt.AutoColor) -> bool """
        return False

    def loadFromData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmap.loadFromData(str, str format=None, Qt.ImageConversionFlags flags=Qt.AutoColor) -> bool
        QPixmap.loadFromData(QByteArray, str format=None, Qt.ImageConversionFlags flags=Qt.AutoColor) -> bool
        """
        return False

    def mask(self): # real signature unknown; restored from __doc__
        """ QPixmap.mask() -> QBitmap """
        return QBitmap

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ QPixmap.metric(QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ QPixmap.paintEngine() -> QPaintEngine """
        return QPaintEngine

    def rect(self): # real signature unknown; restored from __doc__
        """ QPixmap.rect() -> QRect """
        pass

    def save(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmap.save(QString, str format=None, int quality=-1) -> bool
        QPixmap.save(QIODevice, str format=None, int quality=-1) -> bool
        """
        return False

    def scaled(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmap.scaled(int, int, Qt.AspectRatioMode aspectRatioMode=Qt.IgnoreAspectRatio, Qt.TransformationMode transformMode=Qt.FastTransformation) -> QPixmap
        QPixmap.scaled(QSize, Qt.AspectRatioMode aspectRatioMode=Qt.IgnoreAspectRatio, Qt.TransformationMode transformMode=Qt.FastTransformation) -> QPixmap
        """
        return QPixmap

    def scaledToHeight(self, p_int, Qt_TransformationMode_mode=None): # real signature unknown; restored from __doc__
        """ QPixmap.scaledToHeight(int, Qt.TransformationMode mode=Qt.FastTransformation) -> QPixmap """
        return QPixmap

    def scaledToWidth(self, p_int, Qt_TransformationMode_mode=None): # real signature unknown; restored from __doc__
        """ QPixmap.scaledToWidth(int, Qt.TransformationMode mode=Qt.FastTransformation) -> QPixmap """
        return QPixmap

    def scroll(self, p_int, p_int_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmap.scroll(int, int, QRect) -> QRegion
        QPixmap.scroll(int, int, int, int, int, int) -> QRegion
        """
        return QRegion

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ QPixmap.serialNumber() -> int """
        return 0

    def setAlphaChannel(self, QPixmap): # real signature unknown; restored from __doc__
        """ QPixmap.setAlphaChannel(QPixmap) """
        pass

    def setMask(self, QBitmap): # real signature unknown; restored from __doc__
        """ QPixmap.setMask(QBitmap) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QPixmap.size() -> QSize """
        pass

    def swap(self, QPixmap): # real signature unknown; restored from __doc__
        """ QPixmap.swap(QPixmap) """
        pass

    def toImage(self): # real signature unknown; restored from __doc__
        """ QPixmap.toImage() -> QImage """
        return QImage

    def transformed(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmap.transformed(QMatrix, Qt.TransformationMode mode=Qt.FastTransformation) -> QPixmap
        QPixmap.transformed(QTransform, Qt.TransformationMode mode=Qt.FastTransformation) -> QPixmap
        """
        return QPixmap

    def trueMatrix(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmap.trueMatrix(QMatrix, int, int) -> QMatrix
        QPixmap.trueMatrix(QTransform, int, int) -> QTransform
        """
        return QMatrix or QTransform

    def width(self): # real signature unknown; restored from __doc__
        """ QPixmap.width() -> int """
        return 0

    def x11Info(self): # real signature unknown; restored from __doc__
        """ QPixmap.x11Info() -> QX11Info """
        return QX11Info

    def x11PictureHandle(self): # real signature unknown; restored from __doc__
        """ QPixmap.x11PictureHandle() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ExplicitlyShared = 1
    ImplicitlyShared = 0


