# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QTextLine(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QTextLine()
    QTextLine(QTextLine)
    """
    def ascent(self): # real signature unknown; restored from __doc__
        """ QTextLine.ascent() -> float """
        return 0.0

    def cursorToX(self, p_int, QTextLine_Edge_edge=None): # real signature unknown; restored from __doc__
        """ QTextLine.cursorToX(int, QTextLine.Edge edge=QTextLine.Leading) -> (float, int) """
        pass

    def descent(self): # real signature unknown; restored from __doc__
        """ QTextLine.descent() -> float """
        return 0.0

    def draw(self, QPainter, QPointF, QTextLayout_FormatRange_selection=None): # real signature unknown; restored from __doc__
        """ QTextLine.draw(QPainter, QPointF, QTextLayout.FormatRange selection=None) """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ QTextLine.height() -> float """
        return 0.0

    def horizontalAdvance(self): # real signature unknown; restored from __doc__
        """ QTextLine.horizontalAdvance() -> float """
        return 0.0

    def isValid(self): # real signature unknown; restored from __doc__
        """ QTextLine.isValid() -> bool """
        return False

    def leading(self): # real signature unknown; restored from __doc__
        """ QTextLine.leading() -> float """
        return 0.0

    def leadingIncluded(self): # real signature unknown; restored from __doc__
        """ QTextLine.leadingIncluded() -> bool """
        return False

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ QTextLine.lineNumber() -> int """
        return 0

    def naturalTextRect(self): # real signature unknown; restored from __doc__
        """ QTextLine.naturalTextRect() -> QRectF """
        pass

    def naturalTextWidth(self): # real signature unknown; restored from __doc__
        """ QTextLine.naturalTextWidth() -> float """
        return 0.0

    def position(self): # real signature unknown; restored from __doc__
        """ QTextLine.position() -> QPointF """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ QTextLine.rect() -> QRectF """
        pass

    def setLeadingIncluded(self, bool): # real signature unknown; restored from __doc__
        """ QTextLine.setLeadingIncluded(bool) """
        pass

    def setLineWidth(self, p_float): # real signature unknown; restored from __doc__
        """ QTextLine.setLineWidth(float) """
        pass

    def setNumColumns(self, p_int, p_float=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextLine.setNumColumns(int)
        QTextLine.setNumColumns(int, float)
        """
        pass

    def setPosition(self, QPointF): # real signature unknown; restored from __doc__
        """ QTextLine.setPosition(QPointF) """
        pass

    def textLength(self): # real signature unknown; restored from __doc__
        """ QTextLine.textLength() -> int """
        return 0

    def textStart(self): # real signature unknown; restored from __doc__
        """ QTextLine.textStart() -> int """
        return 0

    def width(self): # real signature unknown; restored from __doc__
        """ QTextLine.width() -> float """
        return 0.0

    def x(self): # real signature unknown; restored from __doc__
        """ QTextLine.x() -> float """
        return 0.0

    def xToCursor(self, p_float, QTextLine_CursorPosition_edge=None): # real signature unknown; restored from __doc__
        """ QTextLine.xToCursor(float, QTextLine.CursorPosition edge=QTextLine.CursorBetweenCharacters) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ QTextLine.y() -> float """
        return 0.0

    def __init__(self, QTextLine=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CursorBetweenCharacters = 0
    CursorOnCharacter = 1
    Leading = 0
    Trailing = 1


