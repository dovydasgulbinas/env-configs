# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QPaintEngine(): # skipped bases: <type 'sip.simplewrapper'>
    """ QPaintEngine(QPaintEngine.PaintEngineFeatures features=0) """
    def begin(self, QPaintDevice): # real signature unknown; restored from __doc__
        """ QPaintEngine.begin(QPaintDevice) -> bool """
        return False

    def drawEllipse(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPaintEngine.drawEllipse(QRectF)
        QPaintEngine.drawEllipse(QRect)
        """
        pass

    def drawImage(self, QRectF, QImage, QRectF_1, Qt_ImageConversionFlags_flags=None): # real signature unknown; restored from __doc__
        """ QPaintEngine.drawImage(QRectF, QImage, QRectF, Qt.ImageConversionFlags flags=Qt.AutoColor) """
        pass

    def drawLines(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPaintEngine.drawLines(QLine)
        QPaintEngine.drawLines(QLineF)
        """
        pass

    def drawPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPaintEngine.drawPath(QPainterPath) """
        pass

    def drawPixmap(self, QRectF, QPixmap, QRectF_1): # real signature unknown; restored from __doc__
        """ QPaintEngine.drawPixmap(QRectF, QPixmap, QRectF) """
        pass

    def drawPoints(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPaintEngine.drawPoints(QPointF)
        QPaintEngine.drawPoints(QPoint)
        """
        pass

    def drawPolygon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPaintEngine.drawPolygon(QPointF, QPaintEngine.PolygonDrawMode)
        QPaintEngine.drawPolygon(QPoint, QPaintEngine.PolygonDrawMode)
        """
        pass

    def drawRects(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPaintEngine.drawRects(QRect)
        QPaintEngine.drawRects(QRectF)
        """
        pass

    def drawTextItem(self, QPointF, QTextItem): # real signature unknown; restored from __doc__
        """ QPaintEngine.drawTextItem(QPointF, QTextItem) """
        pass

    def drawTiledPixmap(self, QRectF, QPixmap, QPointF): # real signature unknown; restored from __doc__
        """ QPaintEngine.drawTiledPixmap(QRectF, QPixmap, QPointF) """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ QPaintEngine.end() -> bool """
        return False

    def hasFeature(self, QPaintEngine_PaintEngineFeatures): # real signature unknown; restored from __doc__
        """ QPaintEngine.hasFeature(QPaintEngine.PaintEngineFeatures) -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ QPaintEngine.isActive() -> bool """
        return False

    def paintDevice(self): # real signature unknown; restored from __doc__
        """ QPaintEngine.paintDevice() -> QPaintDevice """
        return QPaintDevice

    def painter(self): # real signature unknown; restored from __doc__
        """ QPaintEngine.painter() -> QPainter """
        return QPainter

    def setActive(self, bool): # real signature unknown; restored from __doc__
        """ QPaintEngine.setActive(bool) """
        pass

    def setPaintDevice(self, QPaintDevice): # real signature unknown; restored from __doc__
        """ QPaintEngine.setPaintDevice(QPaintDevice) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QPaintEngine.type() -> QPaintEngine.Type """
        pass

    def updateState(self, QPaintEngineState): # real signature unknown; restored from __doc__
        """ QPaintEngine.updateState(QPaintEngineState) """
        pass

    def __init__(self, QPaintEngine_PaintEngineFeatures_features=0): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AllDirty = 65535
    AllFeatures = -1
    AlphaBlend = 128
    Antialiasing = 1024
    BlendModes = 32768
    Blitter = 16
    BrushStroke = 2048
    ConicalGradientFill = 64
    ConstantOpacity = 4096
    ConvexMode = 2
    CoreGraphics = 3
    Direct3D = 11
    DirtyBackground = 16
    DirtyBackgroundMode = 32
    DirtyBrush = 2
    DirtyBrushOrigin = 4
    DirtyClipEnabled = 2048
    DirtyClipPath = 256
    DirtyClipRegion = 128
    DirtyCompositionMode = 1024
    DirtyFont = 8
    DirtyHints = 512
    DirtyOpacity = 4096
    DirtyPen = 1
    DirtyTransform = 64
    LinearGradientFill = 16
    MacPrinter = 4
    MaskedBrush = 8192
    MaxUser = 100
    ObjectBoundingModeGradients = 65536
    OddEvenMode = 0
    OpenGL = 7
    OpenGL2 = 14
    OpenVG = 13
    PaintBuffer = 15
    PainterPaths = 512
    PaintOutsidePaintEvent = 536870912
    PatternBrush = 8
    PatternTransform = 2
    Pdf = 12
    PerspectiveTransform = 16384
    Picture = 8
    PixmapTransform = 4
    PolylineMode = 3
    PorterDuff = 256
    PostScript = 6
    PrimitiveTransform = 1
    QuickDraw = 2
    QWindowSystem = 5
    RadialGradientFill = 32
    Raster = 10
    RasterOpModes = 131072
    SVG = 9
    User = 50
    WindingMode = 1
    Windows = 1
    X11 = 0


