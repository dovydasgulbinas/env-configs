# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QTextLayout(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QTextLayout()
    QTextLayout(QString)
    QTextLayout(QString, QFont, QPaintDevice paintDevice=None)
    QTextLayout(QTextBlock)
    """
    def additionalFormats(self): # real signature unknown; restored from __doc__
        """ QTextLayout.additionalFormats() -> list-of-QTextLayout.FormatRange """
        pass

    def beginLayout(self): # real signature unknown; restored from __doc__
        """ QTextLayout.beginLayout() """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QTextLayout.boundingRect() -> QRectF """
        pass

    def cacheEnabled(self): # real signature unknown; restored from __doc__
        """ QTextLayout.cacheEnabled() -> bool """
        return False

    def clearAdditionalFormats(self): # real signature unknown; restored from __doc__
        """ QTextLayout.clearAdditionalFormats() """
        pass

    def clearLayout(self): # real signature unknown; restored from __doc__
        """ QTextLayout.clearLayout() """
        pass

    def createLine(self): # real signature unknown; restored from __doc__
        """ QTextLayout.createLine() -> QTextLine """
        return QTextLine

    def cursorMoveStyle(self): # real signature unknown; restored from __doc__
        """ QTextLayout.cursorMoveStyle() -> Qt.CursorMoveStyle """
        pass

    def draw(self, QPainter, QPointF, list_of_QTextLayout_FormatRange_selections=None, QRectF_clip=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QTextLayout.draw(QPainter, QPointF, list-of-QTextLayout.FormatRange selections=list-of-QTextLayout.FormatRange, QRectF clip=QRectF()) """
        pass

    def drawCursor(self, QPainter, QPointF, p_int, p_int_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextLayout.drawCursor(QPainter, QPointF, int)
        QTextLayout.drawCursor(QPainter, QPointF, int, int)
        """
        pass

    def endLayout(self): # real signature unknown; restored from __doc__
        """ QTextLayout.endLayout() """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ QTextLayout.font() -> QFont """
        return QFont

    def glyphRuns(self): # real signature unknown; restored from __doc__
        """ QTextLayout.glyphRuns() -> list-of-QGlyphRun """
        pass

    def isValidCursorPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QTextLayout.isValidCursorPosition(int) -> bool """
        return False

    def leftCursorPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QTextLayout.leftCursorPosition(int) -> int """
        return 0

    def lineAt(self, p_int): # real signature unknown; restored from __doc__
        """ QTextLayout.lineAt(int) -> QTextLine """
        return QTextLine

    def lineCount(self): # real signature unknown; restored from __doc__
        """ QTextLayout.lineCount() -> int """
        return 0

    def lineForTextPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QTextLayout.lineForTextPosition(int) -> QTextLine """
        return QTextLine

    def maximumWidth(self): # real signature unknown; restored from __doc__
        """ QTextLayout.maximumWidth() -> float """
        return 0.0

    def minimumWidth(self): # real signature unknown; restored from __doc__
        """ QTextLayout.minimumWidth() -> float """
        return 0.0

    def nextCursorPosition(self, p_int, QTextLayout_CursorMode_mode=None): # real signature unknown; restored from __doc__
        """ QTextLayout.nextCursorPosition(int, QTextLayout.CursorMode mode=QTextLayout.SkipCharacters) -> int """
        return 0

    def position(self): # real signature unknown; restored from __doc__
        """ QTextLayout.position() -> QPointF """
        pass

    def preeditAreaPosition(self): # real signature unknown; restored from __doc__
        """ QTextLayout.preeditAreaPosition() -> int """
        return 0

    def preeditAreaText(self): # real signature unknown; restored from __doc__
        """ QTextLayout.preeditAreaText() -> QString """
        pass

    def previousCursorPosition(self, p_int, QTextLayout_CursorMode_mode=None): # real signature unknown; restored from __doc__
        """ QTextLayout.previousCursorPosition(int, QTextLayout.CursorMode mode=QTextLayout.SkipCharacters) -> int """
        return 0

    def rightCursorPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QTextLayout.rightCursorPosition(int) -> int """
        return 0

    def setAdditionalFormats(self, list_of_QTextLayout_FormatRange): # real signature unknown; restored from __doc__
        """ QTextLayout.setAdditionalFormats(list-of-QTextLayout.FormatRange) """
        pass

    def setCacheEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QTextLayout.setCacheEnabled(bool) """
        pass

    def setCursorMoveStyle(self, Qt_CursorMoveStyle): # real signature unknown; restored from __doc__
        """ QTextLayout.setCursorMoveStyle(Qt.CursorMoveStyle) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ QTextLayout.setFont(QFont) """
        pass

    def setPosition(self, QPointF): # real signature unknown; restored from __doc__
        """ QTextLayout.setPosition(QPointF) """
        pass

    def setPreeditArea(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QTextLayout.setPreeditArea(int, QString) """
        pass

    def setText(self, QString): # real signature unknown; restored from __doc__
        """ QTextLayout.setText(QString) """
        pass

    def setTextOption(self, QTextOption): # real signature unknown; restored from __doc__
        """ QTextLayout.setTextOption(QTextOption) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QTextLayout.text() -> QString """
        pass

    def textOption(self): # real signature unknown; restored from __doc__
        """ QTextLayout.textOption() -> QTextOption """
        return QTextOption

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    SkipCharacters = 0
    SkipWords = 1


