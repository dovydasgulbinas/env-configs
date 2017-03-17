# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QPaintDevice import QPaintDevice

class QImage(QPaintDevice):
    """
    QImage()
    QImage(QSize, QImage.Format)
    QImage(int, int, QImage.Format)
    QImage(str, int, int, QImage.Format)
    QImage(sip.voidptr, int, int, QImage.Format)
    QImage(str, int, int, int, QImage.Format)
    QImage(sip.voidptr, int, int, int, QImage.Format)
    QImage(list-of-str)
    QImage(QString, str format=None)
    QImage(QImage)
    QImage(QVariant)
    """
    def allGray(self): # real signature unknown; restored from __doc__
        """ QImage.allGray() -> bool """
        return False

    def alphaChannel(self): # real signature unknown; restored from __doc__
        """ QImage.alphaChannel() -> QImage """
        return QImage

    def bitPlaneCount(self): # real signature unknown; restored from __doc__
        """ QImage.bitPlaneCount() -> int """
        return 0

    def bits(self): # real signature unknown; restored from __doc__
        """ QImage.bits() -> sip.voidptr """
        pass

    def byteCount(self): # real signature unknown; restored from __doc__
        """ QImage.byteCount() -> int """
        return 0

    def bytesPerLine(self): # real signature unknown; restored from __doc__
        """ QImage.bytesPerLine() -> int """
        return 0

    def cacheKey(self): # real signature unknown; restored from __doc__
        """ QImage.cacheKey() -> int """
        return 0

    def color(self, p_int): # real signature unknown; restored from __doc__
        """ QImage.color(int) -> int """
        return 0

    def colorCount(self): # real signature unknown; restored from __doc__
        """ QImage.colorCount() -> int """
        return 0

    def colorTable(self): # real signature unknown; restored from __doc__
        """ QImage.colorTable() -> list-of-int """
        pass

    def constBits(self): # real signature unknown; restored from __doc__
        """ QImage.constBits() -> sip.voidptr """
        pass

    def constScanLine(self, p_int): # real signature unknown; restored from __doc__
        """ QImage.constScanLine(int) -> sip.voidptr """
        pass

    def convertToFormat(self, QImage_Format, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.convertToFormat(QImage.Format, Qt.ImageConversionFlags flags=Qt.AutoColor) -> QImage
        QImage.convertToFormat(QImage.Format, list-of-int, Qt.ImageConversionFlags flags=Qt.AutoColor) -> QImage
        """
        return QImage

    def copy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.copy(QRect rect=QRect()) -> QImage
        QImage.copy(int, int, int, int) -> QImage
        """
        return QImage

    def createAlphaMask(self, Qt_ImageConversionFlags_flags=None): # real signature unknown; restored from __doc__
        """ QImage.createAlphaMask(Qt.ImageConversionFlags flags=Qt.AutoColor) -> QImage """
        return QImage

    def createHeuristicMask(self, bool_clipTight=True): # real signature unknown; restored from __doc__
        """ QImage.createHeuristicMask(bool clipTight=True) -> QImage """
        return QImage

    def createMaskFromColor(self, p_int, Qt_MaskMode_mode=None): # real signature unknown; restored from __doc__
        """ QImage.createMaskFromColor(int, Qt.MaskMode mode=Qt.MaskInColor) -> QImage """
        return QImage

    def depth(self): # real signature unknown; restored from __doc__
        """ QImage.depth() -> int """
        return 0

    def detach(self): # real signature unknown; restored from __doc__
        """ QImage.detach() """
        pass

    def devType(self): # real signature unknown; restored from __doc__
        """ QImage.devType() -> int """
        return 0

    def dotsPerMeterX(self): # real signature unknown; restored from __doc__
        """ QImage.dotsPerMeterX() -> int """
        return 0

    def dotsPerMeterY(self): # real signature unknown; restored from __doc__
        """ QImage.dotsPerMeterY() -> int """
        return 0

    def fill(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.fill(Qt.GlobalColor)
        QImage.fill(QColor)
        QImage.fill(int)
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ QImage.format() -> QImage.Format """
        pass

    def fromData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.fromData(str, str format=None) -> QImage
        QImage.fromData(QByteArray, str format=None) -> QImage
        """
        return QImage

    def hasAlphaChannel(self): # real signature unknown; restored from __doc__
        """ QImage.hasAlphaChannel() -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ QImage.height() -> int """
        return 0

    def invertPixels(self, QImage_InvertMode_mode=None): # real signature unknown; restored from __doc__
        """ QImage.invertPixels(QImage.InvertMode mode=QImage.InvertRgb) """
        pass

    def isDetached(self): # real signature unknown; restored from __doc__
        """ QImage.isDetached() -> bool """
        return False

    def isGrayscale(self): # real signature unknown; restored from __doc__
        """ QImage.isGrayscale() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QImage.isNull() -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.load(QIODevice, str) -> bool
        QImage.load(QString, str format=None) -> bool
        """
        return False

    def loadFromData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.loadFromData(str, str format=None) -> bool
        QImage.loadFromData(QByteArray, str format=None) -> bool
        """
        return False

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ QImage.metric(QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def mirrored(self, bool_horizontal=False, bool_vertical=True): # real signature unknown; restored from __doc__
        """ QImage.mirrored(bool horizontal=False, bool vertical=True) -> QImage """
        return QImage

    def numBytes(self): # real signature unknown; restored from __doc__
        """ QImage.numBytes() -> int """
        return 0

    def numColors(self): # real signature unknown; restored from __doc__
        """ QImage.numColors() -> int """
        return 0

    def offset(self): # real signature unknown; restored from __doc__
        """ QImage.offset() -> QPoint """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ QImage.paintEngine() -> QPaintEngine """
        return QPaintEngine

    def pixel(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.pixel(QPoint) -> int
        QImage.pixel(int, int) -> int
        """
        return 0

    def pixelIndex(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.pixelIndex(QPoint) -> int
        QImage.pixelIndex(int, int) -> int
        """
        return 0

    def rect(self): # real signature unknown; restored from __doc__
        """ QImage.rect() -> QRect """
        pass

    def rgbSwapped(self): # real signature unknown; restored from __doc__
        """ QImage.rgbSwapped() -> QImage """
        return QImage

    def save(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.save(QString, str format=None, int quality=-1) -> bool
        QImage.save(QIODevice, str format=None, int quality=-1) -> bool
        """
        return False

    def scaled(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.scaled(int, int, Qt.AspectRatioMode aspectRatioMode=Qt.IgnoreAspectRatio, Qt.TransformationMode transformMode=Qt.FastTransformation) -> QImage
        QImage.scaled(QSize, Qt.AspectRatioMode aspectRatioMode=Qt.IgnoreAspectRatio, Qt.TransformationMode transformMode=Qt.FastTransformation) -> QImage
        """
        return QImage

    def scaledToHeight(self, p_int, Qt_TransformationMode_mode=None): # real signature unknown; restored from __doc__
        """ QImage.scaledToHeight(int, Qt.TransformationMode mode=Qt.FastTransformation) -> QImage """
        return QImage

    def scaledToWidth(self, p_int, Qt_TransformationMode_mode=None): # real signature unknown; restored from __doc__
        """ QImage.scaledToWidth(int, Qt.TransformationMode mode=Qt.FastTransformation) -> QImage """
        return QImage

    def scanLine(self, p_int): # real signature unknown; restored from __doc__
        """ QImage.scanLine(int) -> sip.voidptr """
        pass

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ QImage.serialNumber() -> int """
        return 0

    def setAlphaChannel(self, QImage): # real signature unknown; restored from __doc__
        """ QImage.setAlphaChannel(QImage) """
        pass

    def setColor(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QImage.setColor(int, int) """
        pass

    def setColorCount(self, p_int): # real signature unknown; restored from __doc__
        """ QImage.setColorCount(int) """
        pass

    def setColorTable(self, list_of_int): # real signature unknown; restored from __doc__
        """ QImage.setColorTable(list-of-int) """
        pass

    def setDotsPerMeterX(self, p_int): # real signature unknown; restored from __doc__
        """ QImage.setDotsPerMeterX(int) """
        pass

    def setDotsPerMeterY(self, p_int): # real signature unknown; restored from __doc__
        """ QImage.setDotsPerMeterY(int) """
        pass

    def setNumColors(self, p_int): # real signature unknown; restored from __doc__
        """ QImage.setNumColors(int) """
        pass

    def setOffset(self, QPoint): # real signature unknown; restored from __doc__
        """ QImage.setOffset(QPoint) """
        pass

    def setPixel(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.setPixel(QPoint, int)
        QImage.setPixel(int, int, int)
        """
        pass

    def setText(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QImage.setText(QString, QString) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QImage.size() -> QSize """
        pass

    def swap(self, QImage): # real signature unknown; restored from __doc__
        """ QImage.swap(QImage) """
        pass

    def text(self, QString_key=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QImage.text(QString key=QString()) -> QString """
        pass

    def textKeys(self): # real signature unknown; restored from __doc__
        """ QImage.textKeys() -> QStringList """
        pass

    def transformed(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.transformed(QMatrix, Qt.TransformationMode mode=Qt.FastTransformation) -> QImage
        QImage.transformed(QTransform, Qt.TransformationMode mode=Qt.FastTransformation) -> QImage
        """
        return QImage

    def trueMatrix(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.trueMatrix(QMatrix, int, int) -> QMatrix
        QImage.trueMatrix(QTransform, int, int) -> QTransform
        """
        return QMatrix or QTransform

    def valid(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QImage.valid(QPoint) -> bool
        QImage.valid(int, int) -> bool
        """
        return False

    def width(self): # real signature unknown; restored from __doc__
        """ QImage.width() -> int """
        return 0

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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

    Format_ARGB32 = 5
    Format_ARGB32_Premultiplied = 6
    Format_ARGB4444_Premultiplied = 15
    Format_ARGB6666_Premultiplied = 10
    Format_ARGB8555_Premultiplied = 12
    Format_ARGB8565_Premultiplied = 8
    Format_Indexed8 = 3
    Format_Invalid = 0
    Format_Mono = 1
    Format_MonoLSB = 2
    Format_RGB16 = 7
    Format_RGB32 = 4
    Format_RGB444 = 14
    Format_RGB555 = 11
    Format_RGB666 = 9
    Format_RGB888 = 13
    InvertRgb = 0
    InvertRgba = 1


