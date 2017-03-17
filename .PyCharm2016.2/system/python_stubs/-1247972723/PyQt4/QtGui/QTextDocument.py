# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QTextDocument(__PyQt4_QtCore.QObject):
    """
    QTextDocument(QObject parent=None)
    QTextDocument(QString, QObject parent=None)
    """
    def addResource(self, p_int, QUrl, QVariant): # real signature unknown; restored from __doc__
        """ QTextDocument.addResource(int, QUrl, QVariant) """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ QTextDocument.adjustSize() """
        pass

    def allFormats(self): # real signature unknown; restored from __doc__
        """ QTextDocument.allFormats() -> list-of-QTextFormat """
        pass

    def availableRedoSteps(self): # real signature unknown; restored from __doc__
        """ QTextDocument.availableRedoSteps() -> int """
        return 0

    def availableUndoSteps(self): # real signature unknown; restored from __doc__
        """ QTextDocument.availableUndoSteps() -> int """
        return 0

    def begin(self): # real signature unknown; restored from __doc__
        """ QTextDocument.begin() -> QTextBlock """
        return QTextBlock

    def blockCount(self): # real signature unknown; restored from __doc__
        """ QTextDocument.blockCount() -> int """
        return 0

    def blockCountChanged(self, *args, **kwargs): # real signature unknown
        """ QTextDocument.blockCountChanged[int] [signal] """
        pass

    def characterAt(self, p_int): # real signature unknown; restored from __doc__
        """ QTextDocument.characterAt(int) -> QChar """
        pass

    def characterCount(self): # real signature unknown; restored from __doc__
        """ QTextDocument.characterCount() -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ QTextDocument.clear() """
        pass

    def clearUndoRedoStacks(self, QTextDocument_Stacks_stacks=None): # real signature unknown; restored from __doc__
        """ QTextDocument.clearUndoRedoStacks(QTextDocument.Stacks stacks=QTextDocument.UndoAndRedoStacks) """
        pass

    def clone(self, QObject_parent=None): # real signature unknown; restored from __doc__
        """ QTextDocument.clone(QObject parent=None) -> QTextDocument """
        return QTextDocument

    def contentsChange(self, *args, **kwargs): # real signature unknown
        """ QTextDocument.contentsChange[int, int, int] [signal] """
        pass

    def contentsChanged(self, *args, **kwargs): # real signature unknown
        """ QTextDocument.contentsChanged [signal] """
        pass

    def createObject(self, QTextFormat): # real signature unknown; restored from __doc__
        """ QTextDocument.createObject(QTextFormat) -> QTextObject """
        return QTextObject

    def cursorPositionChanged(self, *args, **kwargs): # real signature unknown
        """ QTextDocument.cursorPositionChanged[QTextCursor] [signal] """
        pass

    def defaultCursorMoveStyle(self): # real signature unknown; restored from __doc__
        """ QTextDocument.defaultCursorMoveStyle() -> Qt.CursorMoveStyle """
        pass

    def defaultFont(self): # real signature unknown; restored from __doc__
        """ QTextDocument.defaultFont() -> QFont """
        return QFont

    def defaultStyleSheet(self): # real signature unknown; restored from __doc__
        """ QTextDocument.defaultStyleSheet() -> QString """
        pass

    def defaultTextOption(self): # real signature unknown; restored from __doc__
        """ QTextDocument.defaultTextOption() -> QTextOption """
        return QTextOption

    def documentLayout(self): # real signature unknown; restored from __doc__
        """ QTextDocument.documentLayout() -> QAbstractTextDocumentLayout """
        return QAbstractTextDocumentLayout

    def documentLayoutChanged(self, *args, **kwargs): # real signature unknown
        """ QTextDocument.documentLayoutChanged [signal] """
        pass

    def documentMargin(self): # real signature unknown; restored from __doc__
        """ QTextDocument.documentMargin() -> float """
        return 0.0

    def drawContents(self, QPainter, QRectF_rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QTextDocument.drawContents(QPainter, QRectF rect=QRectF()) """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ QTextDocument.end() -> QTextBlock """
        return QTextBlock

    def find(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextDocument.find(QString, int position=0, QTextDocument.FindFlags options=0) -> QTextCursor
        QTextDocument.find(QRegExp, int position=0, QTextDocument.FindFlags options=0) -> QTextCursor
        QTextDocument.find(QString, QTextCursor, QTextDocument.FindFlags options=0) -> QTextCursor
        QTextDocument.find(QRegExp, QTextCursor, QTextDocument.FindFlags options=0) -> QTextCursor
        """
        return QTextCursor

    def findBlock(self, p_int): # real signature unknown; restored from __doc__
        """ QTextDocument.findBlock(int) -> QTextBlock """
        return QTextBlock

    def findBlockByLineNumber(self, p_int): # real signature unknown; restored from __doc__
        """ QTextDocument.findBlockByLineNumber(int) -> QTextBlock """
        return QTextBlock

    def findBlockByNumber(self, p_int): # real signature unknown; restored from __doc__
        """ QTextDocument.findBlockByNumber(int) -> QTextBlock """
        return QTextBlock

    def firstBlock(self): # real signature unknown; restored from __doc__
        """ QTextDocument.firstBlock() -> QTextBlock """
        return QTextBlock

    def idealWidth(self): # real signature unknown; restored from __doc__
        """ QTextDocument.idealWidth() -> float """
        return 0.0

    def indentWidth(self): # real signature unknown; restored from __doc__
        """ QTextDocument.indentWidth() -> float """
        return 0.0

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QTextDocument.isEmpty() -> bool """
        return False

    def isModified(self): # real signature unknown; restored from __doc__
        """ QTextDocument.isModified() -> bool """
        return False

    def isRedoAvailable(self): # real signature unknown; restored from __doc__
        """ QTextDocument.isRedoAvailable() -> bool """
        return False

    def isUndoAvailable(self): # real signature unknown; restored from __doc__
        """ QTextDocument.isUndoAvailable() -> bool """
        return False

    def isUndoRedoEnabled(self): # real signature unknown; restored from __doc__
        """ QTextDocument.isUndoRedoEnabled() -> bool """
        return False

    def lastBlock(self): # real signature unknown; restored from __doc__
        """ QTextDocument.lastBlock() -> QTextBlock """
        return QTextBlock

    def lineCount(self): # real signature unknown; restored from __doc__
        """ QTextDocument.lineCount() -> int """
        return 0

    def loadResource(self, p_int, QUrl): # real signature unknown; restored from __doc__
        """ QTextDocument.loadResource(int, QUrl) -> QVariant """
        pass

    def markContentsDirty(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTextDocument.markContentsDirty(int, int) """
        pass

    def maximumBlockCount(self): # real signature unknown; restored from __doc__
        """ QTextDocument.maximumBlockCount() -> int """
        return 0

    def metaInformation(self, QTextDocument_MetaInformation): # real signature unknown; restored from __doc__
        """ QTextDocument.metaInformation(QTextDocument.MetaInformation) -> QString """
        pass

    def modificationChanged(self, *args, **kwargs): # real signature unknown
        """ QTextDocument.modificationChanged[bool] [signal] """
        pass

    def object(self, p_int): # real signature unknown; restored from __doc__
        """ QTextDocument.object(int) -> QTextObject """
        return QTextObject

    def objectForFormat(self, QTextFormat): # real signature unknown; restored from __doc__
        """ QTextDocument.objectForFormat(QTextFormat) -> QTextObject """
        return QTextObject

    def pageCount(self): # real signature unknown; restored from __doc__
        """ QTextDocument.pageCount() -> int """
        return 0

    def pageSize(self): # real signature unknown; restored from __doc__
        """ QTextDocument.pageSize() -> QSizeF """
        pass

    def print_(self, QPrinter): # real signature unknown; restored from __doc__
        """ QTextDocument.print_(QPrinter) """
        pass

    def redo(self, QTextCursor=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextDocument.redo()
        QTextDocument.redo(QTextCursor)
        """
        pass

    def redoAvailable(self, *args, **kwargs): # real signature unknown
        """ QTextDocument.redoAvailable[bool] [signal] """
        pass

    def resource(self, p_int, QUrl): # real signature unknown; restored from __doc__
        """ QTextDocument.resource(int, QUrl) -> QVariant """
        pass

    def revision(self): # real signature unknown; restored from __doc__
        """ QTextDocument.revision() -> int """
        return 0

    def rootFrame(self): # real signature unknown; restored from __doc__
        """ QTextDocument.rootFrame() -> QTextFrame """
        return QTextFrame

    def setDefaultCursorMoveStyle(self, Qt_CursorMoveStyle): # real signature unknown; restored from __doc__
        """ QTextDocument.setDefaultCursorMoveStyle(Qt.CursorMoveStyle) """
        pass

    def setDefaultFont(self, QFont): # real signature unknown; restored from __doc__
        """ QTextDocument.setDefaultFont(QFont) """
        pass

    def setDefaultStyleSheet(self, QString): # real signature unknown; restored from __doc__
        """ QTextDocument.setDefaultStyleSheet(QString) """
        pass

    def setDefaultTextOption(self, QTextOption): # real signature unknown; restored from __doc__
        """ QTextDocument.setDefaultTextOption(QTextOption) """
        pass

    def setDocumentLayout(self, QAbstractTextDocumentLayout): # real signature unknown; restored from __doc__
        """ QTextDocument.setDocumentLayout(QAbstractTextDocumentLayout) """
        pass

    def setDocumentMargin(self, p_float): # real signature unknown; restored from __doc__
        """ QTextDocument.setDocumentMargin(float) """
        pass

    def setHtml(self, QString): # real signature unknown; restored from __doc__
        """ QTextDocument.setHtml(QString) """
        pass

    def setIndentWidth(self, p_float): # real signature unknown; restored from __doc__
        """ QTextDocument.setIndentWidth(float) """
        pass

    def setMaximumBlockCount(self, p_int): # real signature unknown; restored from __doc__
        """ QTextDocument.setMaximumBlockCount(int) """
        pass

    def setMetaInformation(self, QTextDocument_MetaInformation, QString): # real signature unknown; restored from __doc__
        """ QTextDocument.setMetaInformation(QTextDocument.MetaInformation, QString) """
        pass

    def setModified(self, bool_on=True): # real signature unknown; restored from __doc__
        """ QTextDocument.setModified(bool on=True) """
        pass

    def setPageSize(self, QSizeF): # real signature unknown; restored from __doc__
        """ QTextDocument.setPageSize(QSizeF) """
        pass

    def setPlainText(self, QString): # real signature unknown; restored from __doc__
        """ QTextDocument.setPlainText(QString) """
        pass

    def setTextWidth(self, p_float): # real signature unknown; restored from __doc__
        """ QTextDocument.setTextWidth(float) """
        pass

    def setUndoRedoEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QTextDocument.setUndoRedoEnabled(bool) """
        pass

    def setUseDesignMetrics(self, bool): # real signature unknown; restored from __doc__
        """ QTextDocument.setUseDesignMetrics(bool) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QTextDocument.size() -> QSizeF """
        pass

    def textWidth(self): # real signature unknown; restored from __doc__
        """ QTextDocument.textWidth() -> float """
        return 0.0

    def toHtml(self, QByteArray_encoding=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QTextDocument.toHtml(QByteArray encoding=QByteArray()) -> QString """
        pass

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ QTextDocument.toPlainText() -> QString """
        pass

    def undo(self, QTextCursor=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextDocument.undo()
        QTextDocument.undo(QTextCursor)
        """
        pass

    def undoAvailable(self, *args, **kwargs): # real signature unknown
        """ QTextDocument.undoAvailable[bool] [signal] """
        pass

    def undoCommandAdded(self, *args, **kwargs): # real signature unknown
        """ QTextDocument.undoCommandAdded [signal] """
        pass

    def useDesignMetrics(self): # real signature unknown; restored from __doc__
        """ QTextDocument.useDesignMetrics() -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DocumentTitle = 0
    DocumentUrl = 1
    FindBackward = 1
    FindCaseSensitively = 2
    FindWholeWords = 4
    HtmlResource = 1
    ImageResource = 2
    RedoStack = 2
    StyleSheetResource = 3
    UndoAndRedoStacks = 3
    UndoStack = 1
    UserResource = 100


