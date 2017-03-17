# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QGraphicsObject import QGraphicsObject

class QGraphicsTextItem(QGraphicsObject):
    """
    QGraphicsTextItem(QGraphicsItem parent=None, QGraphicsScene scene=None)
    QGraphicsTextItem(QString, QGraphicsItem parent=None, QGraphicsScene scene=None)
    """
    def adjustSize(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.adjustSize() """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.boundingRect() -> QRectF """
        pass

    def contains(self, QPointF): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.contains(QPointF) -> bool """
        return False

    def contextMenuEvent(self, QGraphicsSceneContextMenuEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.contextMenuEvent(QGraphicsSceneContextMenuEvent) """
        pass

    def defaultTextColor(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.defaultTextColor() -> QColor """
        return QColor

    def document(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.document() -> QTextDocument """
        return QTextDocument

    def dragEnterEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.dragEnterEvent(QGraphicsSceneDragDropEvent) """
        pass

    def dragLeaveEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.dragLeaveEvent(QGraphicsSceneDragDropEvent) """
        pass

    def dragMoveEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.dragMoveEvent(QGraphicsSceneDragDropEvent) """
        pass

    def dropEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.dropEvent(QGraphicsSceneDragDropEvent) """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.focusInEvent(QFocusEvent) """
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.focusOutEvent(QFocusEvent) """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.font() -> QFont """
        return QFont

    def hoverEnterEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.hoverEnterEvent(QGraphicsSceneHoverEvent) """
        pass

    def hoverLeaveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.hoverLeaveEvent(QGraphicsSceneHoverEvent) """
        pass

    def hoverMoveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.hoverMoveEvent(QGraphicsSceneHoverEvent) """
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.inputMethodQuery(Qt.InputMethodQuery) -> QVariant """
        pass

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.isObscuredBy(QGraphicsItem) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.keyReleaseEvent(QKeyEvent) """
        pass

    def linkActivated(self, *args, **kwargs): # real signature unknown
        """ QGraphicsTextItem.linkActivated[QString] [signal] """
        pass

    def linkHovered(self, *args, **kwargs): # real signature unknown
        """ QGraphicsTextItem.linkHovered[QString] [signal] """
        pass

    def mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.mouseDoubleClickEvent(QGraphicsSceneMouseEvent) """
        pass

    def mouseMoveEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.mouseMoveEvent(QGraphicsSceneMouseEvent) """
        pass

    def mousePressEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.mousePressEvent(QGraphicsSceneMouseEvent) """
        pass

    def mouseReleaseEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.mouseReleaseEvent(QGraphicsSceneMouseEvent) """
        pass

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.opaqueArea() -> QPainterPath """
        return QPainterPath

    def openExternalLinks(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.openExternalLinks() -> bool """
        return False

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget) """
        pass

    def sceneEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.sceneEvent(QEvent) -> bool """
        return False

    def setDefaultTextColor(self, QColor): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.setDefaultTextColor(QColor) """
        pass

    def setDocument(self, QTextDocument): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.setDocument(QTextDocument) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.setFont(QFont) """
        pass

    def setHtml(self, QString): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.setHtml(QString) """
        pass

    def setOpenExternalLinks(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.setOpenExternalLinks(bool) """
        pass

    def setPlainText(self, QString): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.setPlainText(QString) """
        pass

    def setTabChangesFocus(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.setTabChangesFocus(bool) """
        pass

    def setTextCursor(self, QTextCursor): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.setTextCursor(QTextCursor) """
        pass

    def setTextInteractionFlags(self, Qt_TextInteractionFlags): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.setTextInteractionFlags(Qt.TextInteractionFlags) """
        pass

    def setTextWidth(self, p_float): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.setTextWidth(float) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.shape() -> QPainterPath """
        return QPainterPath

    def tabChangesFocus(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.tabChangesFocus() -> bool """
        return False

    def textCursor(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.textCursor() -> QTextCursor """
        return QTextCursor

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.textInteractionFlags() -> Qt.TextInteractionFlags """
        pass

    def textWidth(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.textWidth() -> float """
        return 0.0

    def toHtml(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.toHtml() -> QString """
        pass

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.toPlainText() -> QString """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsTextItem.type() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


