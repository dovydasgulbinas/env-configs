# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QTextCursor(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QTextCursor()
    QTextCursor(QTextDocument)
    QTextCursor(QTextFrame)
    QTextCursor(QTextBlock)
    QTextCursor(QTextCursor)
    """
    def anchor(self): # real signature unknown; restored from __doc__
        """ QTextCursor.anchor() -> int """
        return 0

    def atBlockEnd(self): # real signature unknown; restored from __doc__
        """ QTextCursor.atBlockEnd() -> bool """
        return False

    def atBlockStart(self): # real signature unknown; restored from __doc__
        """ QTextCursor.atBlockStart() -> bool """
        return False

    def atEnd(self): # real signature unknown; restored from __doc__
        """ QTextCursor.atEnd() -> bool """
        return False

    def atStart(self): # real signature unknown; restored from __doc__
        """ QTextCursor.atStart() -> bool """
        return False

    def beginEditBlock(self): # real signature unknown; restored from __doc__
        """ QTextCursor.beginEditBlock() """
        pass

    def block(self): # real signature unknown; restored from __doc__
        """ QTextCursor.block() -> QTextBlock """
        return QTextBlock

    def blockCharFormat(self): # real signature unknown; restored from __doc__
        """ QTextCursor.blockCharFormat() -> QTextCharFormat """
        return QTextCharFormat

    def blockFormat(self): # real signature unknown; restored from __doc__
        """ QTextCursor.blockFormat() -> QTextBlockFormat """
        return QTextBlockFormat

    def blockNumber(self): # real signature unknown; restored from __doc__
        """ QTextCursor.blockNumber() -> int """
        return 0

    def charFormat(self): # real signature unknown; restored from __doc__
        """ QTextCursor.charFormat() -> QTextCharFormat """
        return QTextCharFormat

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ QTextCursor.clearSelection() """
        pass

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ QTextCursor.columnNumber() -> int """
        return 0

    def createList(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextCursor.createList(QTextListFormat) -> QTextList
        QTextCursor.createList(QTextListFormat.Style) -> QTextList
        """
        return QTextList

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ QTextCursor.currentFrame() -> QTextFrame """
        return QTextFrame

    def currentList(self): # real signature unknown; restored from __doc__
        """ QTextCursor.currentList() -> QTextList """
        return QTextList

    def currentTable(self): # real signature unknown; restored from __doc__
        """ QTextCursor.currentTable() -> QTextTable """
        return QTextTable

    def deleteChar(self): # real signature unknown; restored from __doc__
        """ QTextCursor.deleteChar() """
        pass

    def deletePreviousChar(self): # real signature unknown; restored from __doc__
        """ QTextCursor.deletePreviousChar() """
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ QTextCursor.document() -> QTextDocument """
        return QTextDocument

    def endEditBlock(self): # real signature unknown; restored from __doc__
        """ QTextCursor.endEditBlock() """
        pass

    def hasComplexSelection(self): # real signature unknown; restored from __doc__
        """ QTextCursor.hasComplexSelection() -> bool """
        return False

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ QTextCursor.hasSelection() -> bool """
        return False

    def insertBlock(self, QTextBlockFormat=None, QTextCharFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextCursor.insertBlock()
        QTextCursor.insertBlock(QTextBlockFormat)
        QTextCursor.insertBlock(QTextBlockFormat, QTextCharFormat)
        """
        pass

    def insertFragment(self, QTextDocumentFragment): # real signature unknown; restored from __doc__
        """ QTextCursor.insertFragment(QTextDocumentFragment) """
        pass

    def insertFrame(self, QTextFrameFormat): # real signature unknown; restored from __doc__
        """ QTextCursor.insertFrame(QTextFrameFormat) -> QTextFrame """
        return QTextFrame

    def insertHtml(self, QString): # real signature unknown; restored from __doc__
        """ QTextCursor.insertHtml(QString) """
        pass

    def insertImage(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextCursor.insertImage(QTextImageFormat)
        QTextCursor.insertImage(QTextImageFormat, QTextFrameFormat.Position)
        QTextCursor.insertImage(QString)
        QTextCursor.insertImage(QImage, QString name=QString())
        """
        pass

    def insertList(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextCursor.insertList(QTextListFormat) -> QTextList
        QTextCursor.insertList(QTextListFormat.Style) -> QTextList
        """
        return QTextList

    def insertTable(self, p_int, p_int_1, QTextTableFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextCursor.insertTable(int, int, QTextTableFormat) -> QTextTable
        QTextCursor.insertTable(int, int) -> QTextTable
        """
        return QTextTable

    def insertText(self, QString, QTextCharFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextCursor.insertText(QString)
        QTextCursor.insertText(QString, QTextCharFormat)
        """
        pass

    def isCopyOf(self, QTextCursor): # real signature unknown; restored from __doc__
        """ QTextCursor.isCopyOf(QTextCursor) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QTextCursor.isNull() -> bool """
        return False

    def joinPreviousEditBlock(self): # real signature unknown; restored from __doc__
        """ QTextCursor.joinPreviousEditBlock() """
        pass

    def keepPositionOnInsert(self): # real signature unknown; restored from __doc__
        """ QTextCursor.keepPositionOnInsert() -> bool """
        return False

    def mergeBlockCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ QTextCursor.mergeBlockCharFormat(QTextCharFormat) """
        pass

    def mergeBlockFormat(self, QTextBlockFormat): # real signature unknown; restored from __doc__
        """ QTextCursor.mergeBlockFormat(QTextBlockFormat) """
        pass

    def mergeCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ QTextCursor.mergeCharFormat(QTextCharFormat) """
        pass

    def movePosition(self, QTextCursor_MoveOperation, QTextCursor_MoveMode_mode=None, int_n=1): # real signature unknown; restored from __doc__
        """ QTextCursor.movePosition(QTextCursor.MoveOperation, QTextCursor.MoveMode mode=QTextCursor.MoveAnchor, int n=1) -> bool """
        return False

    def position(self): # real signature unknown; restored from __doc__
        """ QTextCursor.position() -> int """
        return 0

    def positionInBlock(self): # real signature unknown; restored from __doc__
        """ QTextCursor.positionInBlock() -> int """
        return 0

    def removeSelectedText(self): # real signature unknown; restored from __doc__
        """ QTextCursor.removeSelectedText() """
        pass

    def select(self, QTextCursor_SelectionType): # real signature unknown; restored from __doc__
        """ QTextCursor.select(QTextCursor.SelectionType) """
        pass

    def selectedTableCells(self): # real signature unknown; restored from __doc__
        """ QTextCursor.selectedTableCells() -> (int, int, int, int) """
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ QTextCursor.selectedText() -> QString """
        pass

    def selection(self): # real signature unknown; restored from __doc__
        """ QTextCursor.selection() -> QTextDocumentFragment """
        return QTextDocumentFragment

    def selectionEnd(self): # real signature unknown; restored from __doc__
        """ QTextCursor.selectionEnd() -> int """
        return 0

    def selectionStart(self): # real signature unknown; restored from __doc__
        """ QTextCursor.selectionStart() -> int """
        return 0

    def setBlockCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ QTextCursor.setBlockCharFormat(QTextCharFormat) """
        pass

    def setBlockFormat(self, QTextBlockFormat): # real signature unknown; restored from __doc__
        """ QTextCursor.setBlockFormat(QTextBlockFormat) """
        pass

    def setCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ QTextCursor.setCharFormat(QTextCharFormat) """
        pass

    def setKeepPositionOnInsert(self, bool): # real signature unknown; restored from __doc__
        """ QTextCursor.setKeepPositionOnInsert(bool) """
        pass

    def setPosition(self, p_int, QTextCursor_MoveMode_mode=None): # real signature unknown; restored from __doc__
        """ QTextCursor.setPosition(int, QTextCursor.MoveMode mode=QTextCursor.MoveAnchor) """
        pass

    def setVerticalMovementX(self, p_int): # real signature unknown; restored from __doc__
        """ QTextCursor.setVerticalMovementX(int) """
        pass

    def setVisualNavigation(self, bool): # real signature unknown; restored from __doc__
        """ QTextCursor.setVisualNavigation(bool) """
        pass

    def verticalMovementX(self): # real signature unknown; restored from __doc__
        """ QTextCursor.verticalMovementX() -> int """
        return 0

    def visualNavigation(self): # real signature unknown; restored from __doc__
        """ QTextCursor.visualNavigation() -> bool """
        return False

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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BlockUnderCursor = 2
    Document = 3
    Down = 12
    End = 11
    EndOfBlock = 15
    EndOfLine = 13
    EndOfWord = 14
    KeepAnchor = 1
    Left = 9
    LineUnderCursor = 1
    MoveAnchor = 0
    NextBlock = 16
    NextCell = 21
    NextCharacter = 17
    NextRow = 23
    NextWord = 18
    NoMove = 0
    PreviousBlock = 6
    PreviousCell = 22
    PreviousCharacter = 7
    PreviousRow = 24
    PreviousWord = 8
    Right = 19
    Start = 1
    StartOfBlock = 4
    StartOfLine = 3
    StartOfWord = 5
    Up = 2
    WordLeft = 10
    WordRight = 20
    WordUnderCursor = 0


