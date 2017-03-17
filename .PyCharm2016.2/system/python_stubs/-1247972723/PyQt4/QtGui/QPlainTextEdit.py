# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractScrollArea import QAbstractScrollArea

class QPlainTextEdit(QAbstractScrollArea):
    """
    QPlainTextEdit(QWidget parent=None)
    QPlainTextEdit(QString, QWidget parent=None)
    """
    def anchorAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.anchorAt(QPoint) -> QString """
        pass

    def appendHtml(self, QString): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.appendHtml(QString) """
        pass

    def appendPlainText(self, QString): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.appendPlainText(QString) """
        pass

    def backgroundVisible(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.backgroundVisible() -> bool """
        return False

    def blockBoundingGeometry(self, QTextBlock): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.blockBoundingGeometry(QTextBlock) -> QRectF """
        pass

    def blockBoundingRect(self, QTextBlock): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.blockBoundingRect(QTextBlock) -> QRectF """
        pass

    def blockCount(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.blockCount() -> int """
        return 0

    def blockCountChanged(self, *args, **kwargs): # real signature unknown
        """ QPlainTextEdit.blockCountChanged[int] [signal] """
        pass

    def canInsertFromMimeData(self, QMimeData): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.canInsertFromMimeData(QMimeData) -> bool """
        return False

    def canPaste(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.canPaste() -> bool """
        return False

    def centerCursor(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.centerCursor() """
        pass

    def centerOnScroll(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.centerOnScroll() -> bool """
        return False

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.changeEvent(QEvent) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.clear() """
        pass

    def contentOffset(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.contentOffset() -> QPointF """
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.contextMenuEvent(QContextMenuEvent) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.copy() """
        pass

    def copyAvailable(self, *args, **kwargs): # real signature unknown
        """ QPlainTextEdit.copyAvailable[bool] [signal] """
        pass

    def createMimeDataFromSelection(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.createMimeDataFromSelection() -> QMimeData """
        pass

    def createStandardContextMenu(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.createStandardContextMenu() -> QMenu """
        return QMenu

    def currentCharFormat(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.currentCharFormat() -> QTextCharFormat """
        return QTextCharFormat

    def cursorForPosition(self, QPoint): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.cursorForPosition(QPoint) -> QTextCursor """
        return QTextCursor

    def cursorPositionChanged(self, *args, **kwargs): # real signature unknown
        """ QPlainTextEdit.cursorPositionChanged [signal] """
        pass

    def cursorRect(self, QTextCursor=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPlainTextEdit.cursorRect(QTextCursor) -> QRect
        QPlainTextEdit.cursorRect() -> QRect
        """
        pass

    def cursorWidth(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.cursorWidth() -> int """
        return 0

    def cut(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.cut() """
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.document() -> QTextDocument """
        return QTextDocument

    def documentTitle(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.documentTitle() -> QString """
        pass

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.dragEnterEvent(QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.dragLeaveEvent(QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.dragMoveEvent(QDragMoveEvent) """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.dropEvent(QDropEvent) """
        pass

    def ensureCursorVisible(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.ensureCursorVisible() """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.event(QEvent) -> bool """
        return False

    def extraSelections(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.extraSelections() -> list-of-QTextEdit.ExtraSelection """
        pass

    def find(self, QString, QTextDocument_FindFlags_options=0): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.find(QString, QTextDocument.FindFlags options=0) -> bool """
        return False

    def firstVisibleBlock(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.firstVisibleBlock() -> QTextBlock """
        return QTextBlock

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.focusInEvent(QFocusEvent) """
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.focusNextPrevChild(bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.focusOutEvent(QFocusEvent) """
        pass

    def getPaintContext(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.getPaintContext() -> QAbstractTextDocumentLayout.PaintContext """
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.inputMethodQuery(Qt.InputMethodQuery) -> QVariant """
        pass

    def insertFromMimeData(self, QMimeData): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.insertFromMimeData(QMimeData) """
        pass

    def insertPlainText(self, QString): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.insertPlainText(QString) """
        pass

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.isReadOnly() -> bool """
        return False

    def isUndoRedoEnabled(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.isUndoRedoEnabled() -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.keyReleaseEvent(QKeyEvent) """
        pass

    def lineWrapMode(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.lineWrapMode() -> QPlainTextEdit.LineWrapMode """
        pass

    def loadResource(self, p_int, QUrl): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.loadResource(int, QUrl) -> QVariant """
        pass

    def maximumBlockCount(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.maximumBlockCount() -> int """
        return 0

    def mergeCurrentCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.mergeCurrentCharFormat(QTextCharFormat) """
        pass

    def modificationChanged(self, *args, **kwargs): # real signature unknown
        """ QPlainTextEdit.modificationChanged[bool] [signal] """
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.mouseDoubleClickEvent(QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.mouseReleaseEvent(QMouseEvent) """
        pass

    def moveCursor(self, QTextCursor_MoveOperation, QTextCursor_MoveMode_mode=None): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.moveCursor(QTextCursor.MoveOperation, QTextCursor.MoveMode mode=QTextCursor.MoveAnchor) """
        pass

    def overwriteMode(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.overwriteMode() -> bool """
        return False

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.paintEvent(QPaintEvent) """
        pass

    def paste(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.paste() """
        pass

    def print_(self, QPrinter): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.print_(QPrinter) """
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.redo() """
        pass

    def redoAvailable(self, *args, **kwargs): # real signature unknown
        """ QPlainTextEdit.redoAvailable[bool] [signal] """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.resizeEvent(QResizeEvent) """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.scrollContentsBy(int, int) """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.selectAll() """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ QPlainTextEdit.selectionChanged [signal] """
        pass

    def setBackgroundVisible(self, bool): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setBackgroundVisible(bool) """
        pass

    def setCenterOnScroll(self, bool): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setCenterOnScroll(bool) """
        pass

    def setCurrentCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setCurrentCharFormat(QTextCharFormat) """
        pass

    def setCursorWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setCursorWidth(int) """
        pass

    def setDocument(self, QTextDocument): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setDocument(QTextDocument) """
        pass

    def setDocumentTitle(self, QString): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setDocumentTitle(QString) """
        pass

    def setExtraSelections(self, list_of_QTextEdit_ExtraSelection): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setExtraSelections(list-of-QTextEdit.ExtraSelection) """
        pass

    def setLineWrapMode(self, QPlainTextEdit_LineWrapMode): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode) """
        pass

    def setMaximumBlockCount(self, p_int): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setMaximumBlockCount(int) """
        pass

    def setOverwriteMode(self, bool): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setOverwriteMode(bool) """
        pass

    def setPlainText(self, QString): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setPlainText(QString) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setReadOnly(bool) """
        pass

    def setTabChangesFocus(self, bool): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setTabChangesFocus(bool) """
        pass

    def setTabStopWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setTabStopWidth(int) """
        pass

    def setTextCursor(self, QTextCursor): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setTextCursor(QTextCursor) """
        pass

    def setTextInteractionFlags(self, Qt_TextInteractionFlags): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setTextInteractionFlags(Qt.TextInteractionFlags) """
        pass

    def setUndoRedoEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setUndoRedoEnabled(bool) """
        pass

    def setWordWrapMode(self, QTextOption_WrapMode): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.setWordWrapMode(QTextOption.WrapMode) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.showEvent(QShowEvent) """
        pass

    def tabChangesFocus(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.tabChangesFocus() -> bool """
        return False

    def tabStopWidth(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.tabStopWidth() -> int """
        return 0

    def textChanged(self, *args, **kwargs): # real signature unknown
        """ QPlainTextEdit.textChanged [signal] """
        pass

    def textCursor(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.textCursor() -> QTextCursor """
        return QTextCursor

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.textInteractionFlags() -> Qt.TextInteractionFlags """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.timerEvent(QTimerEvent) """
        pass

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.toPlainText() -> QString """
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.undo() """
        pass

    def undoAvailable(self, *args, **kwargs): # real signature unknown
        """ QPlainTextEdit.undoAvailable[bool] [signal] """
        pass

    def updateRequest(self, *args, **kwargs): # real signature unknown
        """ QPlainTextEdit.updateRequest[QRect, int] [signal] """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.wheelEvent(QWheelEvent) """
        pass

    def wordWrapMode(self): # real signature unknown; restored from __doc__
        """ QPlainTextEdit.wordWrapMode() -> QTextOption.WrapMode """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    NoWrap = 0
    WidgetWidth = 1


