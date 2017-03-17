# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractScrollArea import QAbstractScrollArea

class QTextEdit(QAbstractScrollArea):
    """
    QTextEdit(QWidget parent=None)
    QTextEdit(QString, QWidget parent=None)
    """
    def acceptRichText(self): # real signature unknown; restored from __doc__
        """ QTextEdit.acceptRichText() -> bool """
        return False

    def alignment(self): # real signature unknown; restored from __doc__
        """ QTextEdit.alignment() -> Qt.Alignment """
        pass

    def anchorAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QTextEdit.anchorAt(QPoint) -> QString """
        pass

    def append(self, QString): # real signature unknown; restored from __doc__
        """ QTextEdit.append(QString) """
        pass

    def autoFormatting(self): # real signature unknown; restored from __doc__
        """ QTextEdit.autoFormatting() -> QTextEdit.AutoFormatting """
        pass

    def canInsertFromMimeData(self, QMimeData): # real signature unknown; restored from __doc__
        """ QTextEdit.canInsertFromMimeData(QMimeData) -> bool """
        return False

    def canPaste(self): # real signature unknown; restored from __doc__
        """ QTextEdit.canPaste() -> bool """
        return False

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.changeEvent(QEvent) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QTextEdit.clear() """
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.contextMenuEvent(QContextMenuEvent) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ QTextEdit.copy() """
        pass

    def copyAvailable(self, *args, **kwargs): # real signature unknown
        """ QTextEdit.copyAvailable[bool] [signal] """
        pass

    def createMimeDataFromSelection(self): # real signature unknown; restored from __doc__
        """ QTextEdit.createMimeDataFromSelection() -> QMimeData """
        pass

    def createStandardContextMenu(self, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextEdit.createStandardContextMenu() -> QMenu
        QTextEdit.createStandardContextMenu(QPoint) -> QMenu
        """
        return QMenu

    def currentCharFormat(self): # real signature unknown; restored from __doc__
        """ QTextEdit.currentCharFormat() -> QTextCharFormat """
        return QTextCharFormat

    def currentCharFormatChanged(self, *args, **kwargs): # real signature unknown
        """ QTextEdit.currentCharFormatChanged[QTextCharFormat] [signal] """
        pass

    def currentFont(self): # real signature unknown; restored from __doc__
        """ QTextEdit.currentFont() -> QFont """
        return QFont

    def cursorForPosition(self, QPoint): # real signature unknown; restored from __doc__
        """ QTextEdit.cursorForPosition(QPoint) -> QTextCursor """
        return QTextCursor

    def cursorPositionChanged(self, *args, **kwargs): # real signature unknown
        """ QTextEdit.cursorPositionChanged [signal] """
        pass

    def cursorRect(self, QTextCursor=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextEdit.cursorRect(QTextCursor) -> QRect
        QTextEdit.cursorRect() -> QRect
        """
        pass

    def cursorWidth(self): # real signature unknown; restored from __doc__
        """ QTextEdit.cursorWidth() -> int """
        return 0

    def cut(self): # real signature unknown; restored from __doc__
        """ QTextEdit.cut() """
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ QTextEdit.document() -> QTextDocument """
        return QTextDocument

    def documentTitle(self): # real signature unknown; restored from __doc__
        """ QTextEdit.documentTitle() -> QString """
        pass

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.dragEnterEvent(QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.dragLeaveEvent(QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.dragMoveEvent(QDragMoveEvent) """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.dropEvent(QDropEvent) """
        pass

    def ensureCursorVisible(self): # real signature unknown; restored from __doc__
        """ QTextEdit.ensureCursorVisible() """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.event(QEvent) -> bool """
        return False

    def extraSelections(self): # real signature unknown; restored from __doc__
        """ QTextEdit.extraSelections() -> list-of-QTextEdit.ExtraSelection """
        pass

    def find(self, QString, QTextDocument_FindFlags_options=0): # real signature unknown; restored from __doc__
        """ QTextEdit.find(QString, QTextDocument.FindFlags options=0) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.focusInEvent(QFocusEvent) """
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QTextEdit.focusNextPrevChild(bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.focusOutEvent(QFocusEvent) """
        pass

    def fontFamily(self): # real signature unknown; restored from __doc__
        """ QTextEdit.fontFamily() -> QString """
        pass

    def fontItalic(self): # real signature unknown; restored from __doc__
        """ QTextEdit.fontItalic() -> bool """
        return False

    def fontPointSize(self): # real signature unknown; restored from __doc__
        """ QTextEdit.fontPointSize() -> float """
        return 0.0

    def fontUnderline(self): # real signature unknown; restored from __doc__
        """ QTextEdit.fontUnderline() -> bool """
        return False

    def fontWeight(self): # real signature unknown; restored from __doc__
        """ QTextEdit.fontWeight() -> int """
        return 0

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QTextEdit.inputMethodQuery(Qt.InputMethodQuery) -> QVariant """
        pass

    def insertFromMimeData(self, QMimeData): # real signature unknown; restored from __doc__
        """ QTextEdit.insertFromMimeData(QMimeData) """
        pass

    def insertHtml(self, QString): # real signature unknown; restored from __doc__
        """ QTextEdit.insertHtml(QString) """
        pass

    def insertPlainText(self, QString): # real signature unknown; restored from __doc__
        """ QTextEdit.insertPlainText(QString) """
        pass

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ QTextEdit.isReadOnly() -> bool """
        return False

    def isUndoRedoEnabled(self): # real signature unknown; restored from __doc__
        """ QTextEdit.isUndoRedoEnabled() -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.keyReleaseEvent(QKeyEvent) """
        pass

    def lineWrapColumnOrWidth(self): # real signature unknown; restored from __doc__
        """ QTextEdit.lineWrapColumnOrWidth() -> int """
        return 0

    def lineWrapMode(self): # real signature unknown; restored from __doc__
        """ QTextEdit.lineWrapMode() -> QTextEdit.LineWrapMode """
        pass

    def loadResource(self, p_int, QUrl): # real signature unknown; restored from __doc__
        """ QTextEdit.loadResource(int, QUrl) -> QVariant """
        pass

    def mergeCurrentCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ QTextEdit.mergeCurrentCharFormat(QTextCharFormat) """
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.mouseDoubleClickEvent(QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.mouseReleaseEvent(QMouseEvent) """
        pass

    def moveCursor(self, QTextCursor_MoveOperation, QTextCursor_MoveMode_mode=None): # real signature unknown; restored from __doc__
        """ QTextEdit.moveCursor(QTextCursor.MoveOperation, QTextCursor.MoveMode mode=QTextCursor.MoveAnchor) """
        pass

    def overwriteMode(self): # real signature unknown; restored from __doc__
        """ QTextEdit.overwriteMode() -> bool """
        return False

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.paintEvent(QPaintEvent) """
        pass

    def paste(self): # real signature unknown; restored from __doc__
        """ QTextEdit.paste() """
        pass

    def print_(self, QPrinter): # real signature unknown; restored from __doc__
        """ QTextEdit.print_(QPrinter) """
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ QTextEdit.redo() """
        pass

    def redoAvailable(self, *args, **kwargs): # real signature unknown
        """ QTextEdit.redoAvailable[bool] [signal] """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.resizeEvent(QResizeEvent) """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTextEdit.scrollContentsBy(int, int) """
        pass

    def scrollToAnchor(self, QString): # real signature unknown; restored from __doc__
        """ QTextEdit.scrollToAnchor(QString) """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ QTextEdit.selectAll() """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ QTextEdit.selectionChanged [signal] """
        pass

    def setAcceptRichText(self, bool): # real signature unknown; restored from __doc__
        """ QTextEdit.setAcceptRichText(bool) """
        pass

    def setAlignment(self, Qt_Alignment): # real signature unknown; restored from __doc__
        """ QTextEdit.setAlignment(Qt.Alignment) """
        pass

    def setAutoFormatting(self, QTextEdit_AutoFormatting): # real signature unknown; restored from __doc__
        """ QTextEdit.setAutoFormatting(QTextEdit.AutoFormatting) """
        pass

    def setCurrentCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ QTextEdit.setCurrentCharFormat(QTextCharFormat) """
        pass

    def setCurrentFont(self, QFont): # real signature unknown; restored from __doc__
        """ QTextEdit.setCurrentFont(QFont) """
        pass

    def setCursorWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QTextEdit.setCursorWidth(int) """
        pass

    def setDocument(self, QTextDocument): # real signature unknown; restored from __doc__
        """ QTextEdit.setDocument(QTextDocument) """
        pass

    def setDocumentTitle(self, QString): # real signature unknown; restored from __doc__
        """ QTextEdit.setDocumentTitle(QString) """
        pass

    def setExtraSelections(self, list_of_QTextEdit_ExtraSelection): # real signature unknown; restored from __doc__
        """ QTextEdit.setExtraSelections(list-of-QTextEdit.ExtraSelection) """
        pass

    def setFontFamily(self, QString): # real signature unknown; restored from __doc__
        """ QTextEdit.setFontFamily(QString) """
        pass

    def setFontItalic(self, bool): # real signature unknown; restored from __doc__
        """ QTextEdit.setFontItalic(bool) """
        pass

    def setFontPointSize(self, p_float): # real signature unknown; restored from __doc__
        """ QTextEdit.setFontPointSize(float) """
        pass

    def setFontUnderline(self, bool): # real signature unknown; restored from __doc__
        """ QTextEdit.setFontUnderline(bool) """
        pass

    def setFontWeight(self, p_int): # real signature unknown; restored from __doc__
        """ QTextEdit.setFontWeight(int) """
        pass

    def setHtml(self, QString): # real signature unknown; restored from __doc__
        """ QTextEdit.setHtml(QString) """
        pass

    def setLineWrapColumnOrWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QTextEdit.setLineWrapColumnOrWidth(int) """
        pass

    def setLineWrapMode(self, QTextEdit_LineWrapMode): # real signature unknown; restored from __doc__
        """ QTextEdit.setLineWrapMode(QTextEdit.LineWrapMode) """
        pass

    def setOverwriteMode(self, bool): # real signature unknown; restored from __doc__
        """ QTextEdit.setOverwriteMode(bool) """
        pass

    def setPlainText(self, QString): # real signature unknown; restored from __doc__
        """ QTextEdit.setPlainText(QString) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ QTextEdit.setReadOnly(bool) """
        pass

    def setTabChangesFocus(self, bool): # real signature unknown; restored from __doc__
        """ QTextEdit.setTabChangesFocus(bool) """
        pass

    def setTabStopWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QTextEdit.setTabStopWidth(int) """
        pass

    def setText(self, QString): # real signature unknown; restored from __doc__
        """ QTextEdit.setText(QString) """
        pass

    def setTextBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QTextEdit.setTextBackgroundColor(QColor) """
        pass

    def setTextColor(self, QColor): # real signature unknown; restored from __doc__
        """ QTextEdit.setTextColor(QColor) """
        pass

    def setTextCursor(self, QTextCursor): # real signature unknown; restored from __doc__
        """ QTextEdit.setTextCursor(QTextCursor) """
        pass

    def setTextInteractionFlags(self, Qt_TextInteractionFlags): # real signature unknown; restored from __doc__
        """ QTextEdit.setTextInteractionFlags(Qt.TextInteractionFlags) """
        pass

    def setUndoRedoEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QTextEdit.setUndoRedoEnabled(bool) """
        pass

    def setWordWrapMode(self, QTextOption_WrapMode): # real signature unknown; restored from __doc__
        """ QTextEdit.setWordWrapMode(QTextOption.WrapMode) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.showEvent(QShowEvent) """
        pass

    def tabChangesFocus(self): # real signature unknown; restored from __doc__
        """ QTextEdit.tabChangesFocus() -> bool """
        return False

    def tabStopWidth(self): # real signature unknown; restored from __doc__
        """ QTextEdit.tabStopWidth() -> int """
        return 0

    def textBackgroundColor(self): # real signature unknown; restored from __doc__
        """ QTextEdit.textBackgroundColor() -> QColor """
        return QColor

    def textChanged(self, *args, **kwargs): # real signature unknown
        """ QTextEdit.textChanged [signal] """
        pass

    def textColor(self): # real signature unknown; restored from __doc__
        """ QTextEdit.textColor() -> QColor """
        return QColor

    def textCursor(self): # real signature unknown; restored from __doc__
        """ QTextEdit.textCursor() -> QTextCursor """
        return QTextCursor

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ QTextEdit.textInteractionFlags() -> Qt.TextInteractionFlags """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.timerEvent(QTimerEvent) """
        pass

    def toHtml(self): # real signature unknown; restored from __doc__
        """ QTextEdit.toHtml() -> QString """
        pass

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ QTextEdit.toPlainText() -> QString """
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ QTextEdit.undo() """
        pass

    def undoAvailable(self, *args, **kwargs): # real signature unknown
        """ QTextEdit.undoAvailable[bool] [signal] """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ QTextEdit.wheelEvent(QWheelEvent) """
        pass

    def wordWrapMode(self): # real signature unknown; restored from __doc__
        """ QTextEdit.wordWrapMode() -> QTextOption.WrapMode """
        pass

    def zoomIn(self, int_range=1): # real signature unknown; restored from __doc__
        """ QTextEdit.zoomIn(int range=1) """
        pass

    def zoomOut(self, int_range=1): # real signature unknown; restored from __doc__
        """ QTextEdit.zoomOut(int range=1) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AutoAll = -1
    AutoBulletList = 1
    AutoNone = 0
    FixedColumnWidth = 3
    FixedPixelWidth = 2
    NoWrap = 0
    WidgetWidth = 1


