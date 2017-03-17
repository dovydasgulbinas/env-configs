# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractScrollArea import QAbstractScrollArea

class QGraphicsView(QAbstractScrollArea):
    """
    QGraphicsView(QWidget parent=None)
    QGraphicsView(QGraphicsScene, QWidget parent=None)
    """
    def alignment(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.alignment() -> Qt.Alignment """
        pass

    def backgroundBrush(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.backgroundBrush() -> QBrush """
        return QBrush

    def cacheMode(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.cacheMode() -> QGraphicsView.CacheMode """
        pass

    def centerOn(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsView.centerOn(QPointF)
        QGraphicsView.centerOn(QGraphicsItem)
        QGraphicsView.centerOn(float, float)
        """
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.contextMenuEvent(QContextMenuEvent) """
        pass

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.dragEnterEvent(QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.dragLeaveEvent(QDragLeaveEvent) """
        pass

    def dragMode(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.dragMode() -> QGraphicsView.DragMode """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.dragMoveEvent(QDragMoveEvent) """
        pass

    def drawBackground(self, QPainter, QRectF): # real signature unknown; restored from __doc__
        """ QGraphicsView.drawBackground(QPainter, QRectF) """
        pass

    def drawForeground(self, QPainter, QRectF): # real signature unknown; restored from __doc__
        """ QGraphicsView.drawForeground(QPainter, QRectF) """
        pass

    def drawItems(self, QPainter, list_of_QGraphicsItem, list_of_QStyleOptionGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsView.drawItems(QPainter, list-of-QGraphicsItem, list-of-QStyleOptionGraphicsItem) """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.dropEvent(QDropEvent) """
        pass

    def ensureVisible(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsView.ensureVisible(QRectF, int xMargin=50, int yMargin=50)
        QGraphicsView.ensureVisible(QGraphicsItem, int xMargin=50, int yMargin=50)
        QGraphicsView.ensureVisible(float, float, float, float, int xMargin=50, int yMargin=50)
        """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.event(QEvent) -> bool """
        return False

    def fitInView(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsView.fitInView(QRectF, Qt.AspectRatioMode mode=Qt.IgnoreAspectRatio)
        QGraphicsView.fitInView(QGraphicsItem, Qt.AspectRatioMode mode=Qt.IgnoreAspectRatio)
        QGraphicsView.fitInView(float, float, float, float, Qt.AspectRatioMode mode=Qt.IgnoreAspectRatio)
        """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.focusInEvent(QFocusEvent) """
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsView.focusNextPrevChild(bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.focusOutEvent(QFocusEvent) """
        pass

    def foregroundBrush(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.foregroundBrush() -> QBrush """
        return QBrush

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QGraphicsView.inputMethodQuery(Qt.InputMethodQuery) -> QVariant """
        pass

    def invalidateScene(self, QRectF_rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QGraphicsView.invalidateScene(QRectF rect=QRectF(), QGraphicsScene.SceneLayers layers=QGraphicsScene.AllLayers) """
        pass

    def isInteractive(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.isInteractive() -> bool """
        return False

    def isTransformed(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.isTransformed() -> bool """
        return False

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsView.itemAt(QPoint) -> QGraphicsItem
        QGraphicsView.itemAt(int, int) -> QGraphicsItem
        """
        return QGraphicsItem

    def items(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsView.items() -> list-of-QGraphicsItem
        QGraphicsView.items(QPoint) -> list-of-QGraphicsItem
        QGraphicsView.items(int, int) -> list-of-QGraphicsItem
        QGraphicsView.items(int, int, int, int, Qt.ItemSelectionMode mode=Qt.IntersectsItemShape) -> list-of-QGraphicsItem
        QGraphicsView.items(QRect, Qt.ItemSelectionMode mode=Qt.IntersectsItemShape) -> list-of-QGraphicsItem
        QGraphicsView.items(QPolygon, Qt.ItemSelectionMode mode=Qt.IntersectsItemShape) -> list-of-QGraphicsItem
        QGraphicsView.items(QPainterPath, Qt.ItemSelectionMode mode=Qt.IntersectsItemShape) -> list-of-QGraphicsItem
        """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.keyReleaseEvent(QKeyEvent) """
        pass

    def mapFromScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsView.mapFromScene(QPointF) -> QPoint
        QGraphicsView.mapFromScene(QRectF) -> QPolygon
        QGraphicsView.mapFromScene(QPolygonF) -> QPolygon
        QGraphicsView.mapFromScene(QPainterPath) -> QPainterPath
        QGraphicsView.mapFromScene(float, float) -> QPoint
        QGraphicsView.mapFromScene(float, float, float, float) -> QPolygon
        """
        return QPolygon or QPainterPath

    def mapToScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsView.mapToScene(QPoint) -> QPointF
        QGraphicsView.mapToScene(QRect) -> QPolygonF
        QGraphicsView.mapToScene(QPolygon) -> QPolygonF
        QGraphicsView.mapToScene(QPainterPath) -> QPainterPath
        QGraphicsView.mapToScene(int, int) -> QPointF
        QGraphicsView.mapToScene(int, int, int, int) -> QPolygonF
        """
        return QPolygonF or QPainterPath

    def matrix(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.matrix() -> QMatrix """
        return QMatrix

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.mouseDoubleClickEvent(QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.mouseReleaseEvent(QMouseEvent) """
        pass

    def optimizationFlags(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.optimizationFlags() -> QGraphicsView.OptimizationFlags """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.paintEvent(QPaintEvent) """
        pass

    def render(self, QPainter, QRectF_target=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QGraphicsView.render(QPainter, QRectF target=QRectF(), QRect source=QRect(), Qt.AspectRatioMode mode=Qt.KeepAspectRatio) """
        pass

    def renderHints(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.renderHints() -> QPainter.RenderHints """
        pass

    def resetCachedContent(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.resetCachedContent() """
        pass

    def resetMatrix(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.resetMatrix() """
        pass

    def resetTransform(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.resetTransform() """
        pass

    def resizeAnchor(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.resizeAnchor() -> QGraphicsView.ViewportAnchor """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.resizeEvent(QResizeEvent) """
        pass

    def rotate(self, p_float): # real signature unknown; restored from __doc__
        """ QGraphicsView.rotate(float) """
        pass

    def rubberBandSelectionMode(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.rubberBandSelectionMode() -> Qt.ItemSelectionMode """
        pass

    def scale(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QGraphicsView.scale(float, float) """
        pass

    def scene(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.scene() -> QGraphicsScene """
        return QGraphicsScene

    def sceneRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.sceneRect() -> QRectF """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QGraphicsView.scrollContentsBy(int, int) """
        pass

    def setAlignment(self, Qt_Alignment): # real signature unknown; restored from __doc__
        """ QGraphicsView.setAlignment(Qt.Alignment) """
        pass

    def setBackgroundBrush(self, QBrush): # real signature unknown; restored from __doc__
        """ QGraphicsView.setBackgroundBrush(QBrush) """
        pass

    def setCacheMode(self, QGraphicsView_CacheMode): # real signature unknown; restored from __doc__
        """ QGraphicsView.setCacheMode(QGraphicsView.CacheMode) """
        pass

    def setDragMode(self, QGraphicsView_DragMode): # real signature unknown; restored from __doc__
        """ QGraphicsView.setDragMode(QGraphicsView.DragMode) """
        pass

    def setForegroundBrush(self, QBrush): # real signature unknown; restored from __doc__
        """ QGraphicsView.setForegroundBrush(QBrush) """
        pass

    def setInteractive(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsView.setInteractive(bool) """
        pass

    def setMatrix(self, QMatrix, bool_combine=False): # real signature unknown; restored from __doc__
        """ QGraphicsView.setMatrix(QMatrix, bool combine=False) """
        pass

    def setOptimizationFlag(self, QGraphicsView_OptimizationFlag, bool_enabled=True): # real signature unknown; restored from __doc__
        """ QGraphicsView.setOptimizationFlag(QGraphicsView.OptimizationFlag, bool enabled=True) """
        pass

    def setOptimizationFlags(self, QGraphicsView_OptimizationFlags): # real signature unknown; restored from __doc__
        """ QGraphicsView.setOptimizationFlags(QGraphicsView.OptimizationFlags) """
        pass

    def setRenderHint(self, QPainter_RenderHint, bool_on=True): # real signature unknown; restored from __doc__
        """ QGraphicsView.setRenderHint(QPainter.RenderHint, bool on=True) """
        pass

    def setRenderHints(self, QPainter_RenderHints): # real signature unknown; restored from __doc__
        """ QGraphicsView.setRenderHints(QPainter.RenderHints) """
        pass

    def setResizeAnchor(self, QGraphicsView_ViewportAnchor): # real signature unknown; restored from __doc__
        """ QGraphicsView.setResizeAnchor(QGraphicsView.ViewportAnchor) """
        pass

    def setRubberBandSelectionMode(self, Qt_ItemSelectionMode): # real signature unknown; restored from __doc__
        """ QGraphicsView.setRubberBandSelectionMode(Qt.ItemSelectionMode) """
        pass

    def setScene(self, QGraphicsScene): # real signature unknown; restored from __doc__
        """ QGraphicsView.setScene(QGraphicsScene) """
        pass

    def setSceneRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsView.setSceneRect(QRectF)
        QGraphicsView.setSceneRect(float, float, float, float)
        """
        pass

    def setTransform(self, QTransform, bool_combine=False): # real signature unknown; restored from __doc__
        """ QGraphicsView.setTransform(QTransform, bool combine=False) """
        pass

    def setTransformationAnchor(self, QGraphicsView_ViewportAnchor): # real signature unknown; restored from __doc__
        """ QGraphicsView.setTransformationAnchor(QGraphicsView.ViewportAnchor) """
        pass

    def setupViewport(self, QWidget): # real signature unknown; restored from __doc__
        """ QGraphicsView.setupViewport(QWidget) """
        pass

    def setViewportUpdateMode(self, QGraphicsView_ViewportUpdateMode): # real signature unknown; restored from __doc__
        """ QGraphicsView.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode) """
        pass

    def shear(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QGraphicsView.shear(float, float) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.showEvent(QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.sizeHint() -> QSize """
        pass

    def transform(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.transform() -> QTransform """
        return QTransform

    def transformationAnchor(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.transformationAnchor() -> QGraphicsView.ViewportAnchor """
        pass

    def translate(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QGraphicsView.translate(float, float) """
        pass

    def updateScene(self, list_of_QRectF): # real signature unknown; restored from __doc__
        """ QGraphicsView.updateScene(list-of-QRectF) """
        pass

    def updateSceneRect(self, QRectF): # real signature unknown; restored from __doc__
        """ QGraphicsView.updateSceneRect(QRectF) """
        pass

    def viewportEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.viewportEvent(QEvent) -> bool """
        return False

    def viewportTransform(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.viewportTransform() -> QTransform """
        return QTransform

    def viewportUpdateMode(self): # real signature unknown; restored from __doc__
        """ QGraphicsView.viewportUpdateMode() -> QGraphicsView.ViewportUpdateMode """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ QGraphicsView.wheelEvent(QWheelEvent) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AnchorUnderMouse = 2
    AnchorViewCenter = 1
    BoundingRectViewportUpdate = 4
    CacheBackground = 1
    CacheNone = 0
    DontAdjustForAntialiasing = 4
    DontClipPainter = 1
    DontSavePainterState = 2
    FullViewportUpdate = 0
    MinimalViewportUpdate = 1
    NoAnchor = 0
    NoDrag = 0
    NoViewportUpdate = 3
    RubberBandDrag = 2
    ScrollHandDrag = 1
    SmartViewportUpdate = 2


