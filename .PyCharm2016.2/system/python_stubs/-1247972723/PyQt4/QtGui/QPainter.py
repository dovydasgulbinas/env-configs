# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QPainter(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QPainter()
    QPainter(QPaintDevice)
    """
    def background(self): # real signature unknown; restored from __doc__
        """ QPainter.background() -> QBrush """
        return QBrush

    def backgroundMode(self): # real signature unknown; restored from __doc__
        """ QPainter.backgroundMode() -> Qt.BGMode """
        pass

    def begin(self, QPaintDevice): # real signature unknown; restored from __doc__
        """ QPainter.begin(QPaintDevice) -> bool """
        return False

    def beginNativePainting(self): # real signature unknown; restored from __doc__
        """ QPainter.beginNativePainting() """
        pass

    def boundingRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.boundingRect(QRectF, int, QString) -> QRectF
        QPainter.boundingRect(QRect, int, QString) -> QRect
        QPainter.boundingRect(QRectF, QString, QTextOption option=QTextOption()) -> QRectF
        QPainter.boundingRect(int, int, int, int, int, QString) -> QRect
        """
        pass

    def brush(self): # real signature unknown; restored from __doc__
        """ QPainter.brush() -> QBrush """
        return QBrush

    def brushOrigin(self): # real signature unknown; restored from __doc__
        """ QPainter.brushOrigin() -> QPoint """
        pass

    def clipBoundingRect(self): # real signature unknown; restored from __doc__
        """ QPainter.clipBoundingRect() -> QRectF """
        pass

    def clipPath(self): # real signature unknown; restored from __doc__
        """ QPainter.clipPath() -> QPainterPath """
        return QPainterPath

    def clipRegion(self): # real signature unknown; restored from __doc__
        """ QPainter.clipRegion() -> QRegion """
        return QRegion

    def combinedMatrix(self): # real signature unknown; restored from __doc__
        """ QPainter.combinedMatrix() -> QMatrix """
        return QMatrix

    def combinedTransform(self): # real signature unknown; restored from __doc__
        """ QPainter.combinedTransform() -> QTransform """
        return QTransform

    def compositionMode(self): # real signature unknown; restored from __doc__
        """ QPainter.compositionMode() -> QPainter.CompositionMode """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ QPainter.device() -> QPaintDevice """
        return QPaintDevice

    def deviceMatrix(self): # real signature unknown; restored from __doc__
        """ QPainter.deviceMatrix() -> QMatrix """
        return QMatrix

    def deviceTransform(self): # real signature unknown; restored from __doc__
        """ QPainter.deviceTransform() -> QTransform """
        return QTransform

    def drawArc(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawArc(QRectF, int, int)
        QPainter.drawArc(QRect, int, int)
        QPainter.drawArc(int, int, int, int, int, int)
        """
        pass

    def drawChord(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawChord(QRectF, int, int)
        QPainter.drawChord(QRect, int, int)
        QPainter.drawChord(int, int, int, int, int, int)
        """
        pass

    def drawConvexPolygon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawConvexPolygon(QPointF, ...)
        QPainter.drawConvexPolygon(QPolygonF)
        QPainter.drawConvexPolygon(QPoint, ...)
        QPainter.drawConvexPolygon(QPolygon)
        """
        pass

    def drawEllipse(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawEllipse(QRectF)
        QPainter.drawEllipse(QRect)
        QPainter.drawEllipse(int, int, int, int)
        QPainter.drawEllipse(QPointF, float, float)
        QPainter.drawEllipse(QPoint, int, int)
        """
        pass

    def drawGlyphRun(self, QPointF, QGlyphRun): # real signature unknown; restored from __doc__
        """ QPainter.drawGlyphRun(QPointF, QGlyphRun) """
        pass

    def drawImage(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawImage(QRectF, QImage, QRectF, Qt.ImageConversionFlags flags=Qt.AutoColor)
        QPainter.drawImage(QRect, QImage, QRect, Qt.ImageConversionFlags flags=Qt.AutoColor)
        QPainter.drawImage(QPointF, QImage, QRectF, Qt.ImageConversionFlags flags=Qt.AutoColor)
        QPainter.drawImage(QPoint, QImage, QRect, Qt.ImageConversionFlags flags=Qt.AutoColor)
        QPainter.drawImage(QRectF, QImage)
        QPainter.drawImage(QRect, QImage)
        QPainter.drawImage(QPointF, QImage)
        QPainter.drawImage(QPoint, QImage)
        QPainter.drawImage(int, int, QImage, int sx=0, int sy=0, int sw=-1, int sh=-1, Qt.ImageConversionFlags flags=Qt.AutoColor)
        """
        pass

    def drawLine(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawLine(QLineF)
        QPainter.drawLine(QLine)
        QPainter.drawLine(int, int, int, int)
        QPainter.drawLine(QPoint, QPoint)
        QPainter.drawLine(QPointF, QPointF)
        """
        pass

    def drawLines(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawLines(QLineF, ...)
        QPainter.drawLines(list-of-QLineF)
        QPainter.drawLines(QPointF, ...)
        QPainter.drawLines(list-of-QPointF)
        QPainter.drawLines(QLine, ...)
        QPainter.drawLines(list-of-QLine)
        QPainter.drawLines(QPoint, ...)
        QPainter.drawLines(list-of-QPoint)
        """
        pass

    def drawPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainter.drawPath(QPainterPath) """
        pass

    def drawPicture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawPicture(QPointF, QPicture)
        QPainter.drawPicture(int, int, QPicture)
        QPainter.drawPicture(QPoint, QPicture)
        """
        pass

    def drawPie(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawPie(QRectF, int, int)
        QPainter.drawPie(QRect, int, int)
        QPainter.drawPie(int, int, int, int, int, int)
        """
        pass

    def drawPixmap(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawPixmap(QRectF, QPixmap, QRectF)
        QPainter.drawPixmap(QRect, QPixmap, QRect)
        QPainter.drawPixmap(QPointF, QPixmap)
        QPainter.drawPixmap(QPoint, QPixmap)
        QPainter.drawPixmap(QRect, QPixmap)
        QPainter.drawPixmap(int, int, QPixmap)
        QPainter.drawPixmap(int, int, int, int, QPixmap)
        QPainter.drawPixmap(int, int, int, int, QPixmap, int, int, int, int)
        QPainter.drawPixmap(int, int, QPixmap, int, int, int, int)
        QPainter.drawPixmap(QPointF, QPixmap, QRectF)
        QPainter.drawPixmap(QPoint, QPixmap, QRect)
        """
        pass

    def drawPixmapFragments(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawPixmapFragments(list-of-QPainter.PixmapFragment, QPixmap, QPainter.PixmapFragmentHints hints=0)
        QPainter.drawPixmapFragments(list-of-QRectF, list-of-QRectF, QPixmap, QPainter.PixmapFragmentHints hints=0)
        """
        pass

    def drawPoint(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawPoint(QPointF)
        QPainter.drawPoint(int, int)
        QPainter.drawPoint(QPoint)
        """
        pass

    def drawPoints(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawPoints(QPointF, ...)
        QPainter.drawPoints(QPolygonF)
        QPainter.drawPoints(QPoint, ...)
        QPainter.drawPoints(QPolygon)
        """
        pass

    def drawPolygon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawPolygon(QPointF, ...)
        QPainter.drawPolygon(QPolygonF, Qt.FillRule fillRule=Qt.OddEvenFill)
        QPainter.drawPolygon(QPoint, ...)
        QPainter.drawPolygon(QPolygon, Qt.FillRule fillRule=Qt.OddEvenFill)
        """
        pass

    def drawPolyline(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawPolyline(QPointF, ...)
        QPainter.drawPolyline(QPolygonF)
        QPainter.drawPolyline(QPoint, ...)
        QPainter.drawPolyline(QPolygon)
        """
        pass

    def drawRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawRect(QRectF)
        QPainter.drawRect(int, int, int, int)
        QPainter.drawRect(QRect)
        """
        pass

    def drawRects(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawRects(QRectF, ...)
        QPainter.drawRects(list-of-QRectF)
        QPainter.drawRects(QRect, ...)
        QPainter.drawRects(list-of-QRect)
        """
        pass

    def drawRoundedRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawRoundedRect(QRectF, float, float, Qt.SizeMode mode=Qt.AbsoluteSize)
        QPainter.drawRoundedRect(int, int, int, int, float, float, Qt.SizeMode mode=Qt.AbsoluteSize)
        QPainter.drawRoundedRect(QRect, float, float, Qt.SizeMode mode=Qt.AbsoluteSize)
        """
        pass

    def drawRoundRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawRoundRect(QRectF, int xRound=25, int yRound=25)
        QPainter.drawRoundRect(int, int, int, int, int xRound=25, int yRound=25)
        QPainter.drawRoundRect(QRect, int xRound=25, int yRound=25)
        """
        pass

    def drawStaticText(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawStaticText(QPointF, QStaticText)
        QPainter.drawStaticText(QPoint, QStaticText)
        QPainter.drawStaticText(int, int, QStaticText)
        """
        pass

    def drawText(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawText(QPointF, QString)
        QPainter.drawText(QRectF, int, QString) -> QRectF
        QPainter.drawText(QRect, int, QString) -> QRect
        QPainter.drawText(QRectF, QString, QTextOption option=QTextOption())
        QPainter.drawText(QPoint, QString)
        QPainter.drawText(int, int, int, int, int, QString) -> QRect
        QPainter.drawText(int, int, QString)
        """
        pass

    def drawTiledPixmap(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.drawTiledPixmap(QRectF, QPixmap, QPointF pos=QPointF())
        QPainter.drawTiledPixmap(QRect, QPixmap, QPoint pos=QPoint())
        QPainter.drawTiledPixmap(int, int, int, int, QPixmap, int sx=0, int sy=0)
        """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ QPainter.end() -> bool """
        return False

    def endNativePainting(self): # real signature unknown; restored from __doc__
        """ QPainter.endNativePainting() """
        pass

    def eraseRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.eraseRect(QRectF)
        QPainter.eraseRect(QRect)
        QPainter.eraseRect(int, int, int, int)
        """
        pass

    def fillPath(self, QPainterPath, QBrush): # real signature unknown; restored from __doc__
        """ QPainter.fillPath(QPainterPath, QBrush) """
        pass

    def fillRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.fillRect(QRectF, QBrush)
        QPainter.fillRect(QRect, QBrush)
        QPainter.fillRect(int, int, int, int, QBrush)
        QPainter.fillRect(QRectF, QColor)
        QPainter.fillRect(QRect, QColor)
        QPainter.fillRect(int, int, int, int, QColor)
        QPainter.fillRect(int, int, int, int, Qt.GlobalColor)
        QPainter.fillRect(QRect, Qt.GlobalColor)
        QPainter.fillRect(QRectF, Qt.GlobalColor)
        QPainter.fillRect(int, int, int, int, Qt.BrushStyle)
        QPainter.fillRect(QRect, Qt.BrushStyle)
        QPainter.fillRect(QRectF, Qt.BrushStyle)
        """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ QPainter.font() -> QFont """
        return QFont

    def fontInfo(self): # real signature unknown; restored from __doc__
        """ QPainter.fontInfo() -> QFontInfo """
        return QFontInfo

    def fontMetrics(self): # real signature unknown; restored from __doc__
        """ QPainter.fontMetrics() -> QFontMetrics """
        return QFontMetrics

    def hasClipping(self): # real signature unknown; restored from __doc__
        """ QPainter.hasClipping() -> bool """
        return False

    def initFrom(self, QWidget): # real signature unknown; restored from __doc__
        """ QPainter.initFrom(QWidget) """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ QPainter.isActive() -> bool """
        return False

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ QPainter.layoutDirection() -> Qt.LayoutDirection """
        pass

    def matrix(self): # real signature unknown; restored from __doc__
        """ QPainter.matrix() -> QMatrix """
        return QMatrix

    def matrixEnabled(self): # real signature unknown; restored from __doc__
        """ QPainter.matrixEnabled() -> bool """
        return False

    def opacity(self): # real signature unknown; restored from __doc__
        """ QPainter.opacity() -> float """
        return 0.0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ QPainter.paintEngine() -> QPaintEngine """
        return QPaintEngine

    def pen(self): # real signature unknown; restored from __doc__
        """ QPainter.pen() -> QPen """
        return QPen

    def redirected(self, QPaintDevice, QPoint_offset=None): # real signature unknown; restored from __doc__
        """ QPainter.redirected(QPaintDevice, QPoint offset=None) -> QPaintDevice """
        return QPaintDevice

    def renderHints(self): # real signature unknown; restored from __doc__
        """ QPainter.renderHints() -> QPainter.RenderHints """
        pass

    def resetMatrix(self): # real signature unknown; restored from __doc__
        """ QPainter.resetMatrix() """
        pass

    def resetTransform(self): # real signature unknown; restored from __doc__
        """ QPainter.resetTransform() """
        pass

    def restore(self): # real signature unknown; restored from __doc__
        """ QPainter.restore() """
        pass

    def restoreRedirected(self, QPaintDevice): # real signature unknown; restored from __doc__
        """ QPainter.restoreRedirected(QPaintDevice) """
        pass

    def rotate(self, p_float): # real signature unknown; restored from __doc__
        """ QPainter.rotate(float) """
        pass

    def save(self): # real signature unknown; restored from __doc__
        """ QPainter.save() """
        pass

    def scale(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QPainter.scale(float, float) """
        pass

    def setBackground(self, QBrush): # real signature unknown; restored from __doc__
        """ QPainter.setBackground(QBrush) """
        pass

    def setBackgroundMode(self, Qt_BGMode): # real signature unknown; restored from __doc__
        """ QPainter.setBackgroundMode(Qt.BGMode) """
        pass

    def setBrush(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.setBrush(QBrush)
        QPainter.setBrush(Qt.BrushStyle)
        """
        pass

    def setBrushOrigin(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.setBrushOrigin(QPointF)
        QPainter.setBrushOrigin(int, int)
        QPainter.setBrushOrigin(QPoint)
        """
        pass

    def setClipPath(self, QPainterPath, Qt_ClipOperation_operation=None): # real signature unknown; restored from __doc__
        """ QPainter.setClipPath(QPainterPath, Qt.ClipOperation operation=Qt.ReplaceClip) """
        pass

    def setClipping(self, bool): # real signature unknown; restored from __doc__
        """ QPainter.setClipping(bool) """
        pass

    def setClipRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.setClipRect(QRectF, Qt.ClipOperation operation=Qt.ReplaceClip)
        QPainter.setClipRect(int, int, int, int, Qt.ClipOperation operation=Qt.ReplaceClip)
        QPainter.setClipRect(QRect, Qt.ClipOperation operation=Qt.ReplaceClip)
        """
        pass

    def setClipRegion(self, QRegion, Qt_ClipOperation_operation=None): # real signature unknown; restored from __doc__
        """ QPainter.setClipRegion(QRegion, Qt.ClipOperation operation=Qt.ReplaceClip) """
        pass

    def setCompositionMode(self, QPainter_CompositionMode): # real signature unknown; restored from __doc__
        """ QPainter.setCompositionMode(QPainter.CompositionMode) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ QPainter.setFont(QFont) """
        pass

    def setLayoutDirection(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ QPainter.setLayoutDirection(Qt.LayoutDirection) """
        pass

    def setMatrix(self, QMatrix, bool_combine=False): # real signature unknown; restored from __doc__
        """ QPainter.setMatrix(QMatrix, bool combine=False) """
        pass

    def setMatrixEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QPainter.setMatrixEnabled(bool) """
        pass

    def setOpacity(self, p_float): # real signature unknown; restored from __doc__
        """ QPainter.setOpacity(float) """
        pass

    def setPen(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.setPen(QColor)
        QPainter.setPen(QPen)
        QPainter.setPen(Qt.PenStyle)
        """
        pass

    def setRedirected(self, QPaintDevice, QPaintDevice_1, QPoint_offset=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QPainter.setRedirected(QPaintDevice, QPaintDevice, QPoint offset=QPoint()) """
        pass

    def setRenderHint(self, QPainter_RenderHint, bool_on=True): # real signature unknown; restored from __doc__
        """ QPainter.setRenderHint(QPainter.RenderHint, bool on=True) """
        pass

    def setRenderHints(self, QPainter_RenderHints, bool_on=True): # real signature unknown; restored from __doc__
        """ QPainter.setRenderHints(QPainter.RenderHints, bool on=True) """
        pass

    def setTransform(self, QTransform, bool_combine=False): # real signature unknown; restored from __doc__
        """ QPainter.setTransform(QTransform, bool combine=False) """
        pass

    def setViewport(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.setViewport(QRect)
        QPainter.setViewport(int, int, int, int)
        """
        pass

    def setViewTransformEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QPainter.setViewTransformEnabled(bool) """
        pass

    def setWindow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.setWindow(QRect)
        QPainter.setWindow(int, int, int, int)
        """
        pass

    def setWorldMatrix(self, QMatrix, bool_combine=False): # real signature unknown; restored from __doc__
        """ QPainter.setWorldMatrix(QMatrix, bool combine=False) """
        pass

    def setWorldMatrixEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QPainter.setWorldMatrixEnabled(bool) """
        pass

    def setWorldTransform(self, QTransform, bool_combine=False): # real signature unknown; restored from __doc__
        """ QPainter.setWorldTransform(QTransform, bool combine=False) """
        pass

    def shear(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QPainter.shear(float, float) """
        pass

    def strokePath(self, QPainterPath, QPen): # real signature unknown; restored from __doc__
        """ QPainter.strokePath(QPainterPath, QPen) """
        pass

    def testRenderHint(self, QPainter_RenderHint): # real signature unknown; restored from __doc__
        """ QPainter.testRenderHint(QPainter.RenderHint) -> bool """
        return False

    def transform(self): # real signature unknown; restored from __doc__
        """ QPainter.transform() -> QTransform """
        return QTransform

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainter.translate(QPointF)
        QPainter.translate(float, float)
        QPainter.translate(QPoint)
        """
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ QPainter.viewport() -> QRect """
        pass

    def viewTransformEnabled(self): # real signature unknown; restored from __doc__
        """ QPainter.viewTransformEnabled() -> bool """
        return False

    def window(self): # real signature unknown; restored from __doc__
        """ QPainter.window() -> QRect """
        pass

    def worldMatrix(self): # real signature unknown; restored from __doc__
        """ QPainter.worldMatrix() -> QMatrix """
        return QMatrix

    def worldMatrixEnabled(self): # real signature unknown; restored from __doc__
        """ QPainter.worldMatrixEnabled() -> bool """
        return False

    def worldTransform(self): # real signature unknown; restored from __doc__
        """ QPainter.worldTransform() -> QTransform """
        return QTransform

    def __enter__(self): # real signature unknown; restored from __doc__
        """ QPainter.__enter__() -> object """
        return object()

    def __exit__(self, p_object, p_object_1, p_object_2): # real signature unknown; restored from __doc__
        """ QPainter.__exit__(object, object, object) """
        pass

    def __init__(self, QPaintDevice=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Antialiasing = 1
    CompositionMode_Clear = 2
    CompositionMode_ColorBurn = 19
    CompositionMode_ColorDodge = 18
    CompositionMode_Darken = 16
    CompositionMode_Destination = 4
    CompositionMode_DestinationAtop = 10
    CompositionMode_DestinationIn = 6
    CompositionMode_DestinationOut = 8
    CompositionMode_DestinationOver = 1
    CompositionMode_Difference = 22
    CompositionMode_Exclusion = 23
    CompositionMode_HardLight = 20
    CompositionMode_Lighten = 17
    CompositionMode_Multiply = 13
    CompositionMode_Overlay = 15
    CompositionMode_Plus = 12
    CompositionMode_Screen = 14
    CompositionMode_SoftLight = 21
    CompositionMode_Source = 3
    CompositionMode_SourceAtop = 9
    CompositionMode_SourceIn = 5
    CompositionMode_SourceOut = 7
    CompositionMode_SourceOver = 0
    CompositionMode_Xor = 11
    HighQualityAntialiasing = 8
    NonCosmeticDefaultPen = 16
    OpaqueHint = 1
    RasterOp_NotSource = 30
    RasterOp_NotSourceAndDestination = 31
    RasterOp_NotSourceAndNotDestination = 27
    RasterOp_NotSourceOrNotDestination = 28
    RasterOp_NotSourceXorDestination = 29
    RasterOp_SourceAndDestination = 25
    RasterOp_SourceAndNotDestination = 32
    RasterOp_SourceOrDestination = 24
    RasterOp_SourceXorDestination = 26
    SmoothPixmapTransform = 4
    TextAntialiasing = 2


