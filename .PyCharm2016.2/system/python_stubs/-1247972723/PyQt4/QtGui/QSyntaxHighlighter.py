# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QSyntaxHighlighter(__PyQt4_QtCore.QObject):
    """
    QSyntaxHighlighter(QTextEdit)
    QSyntaxHighlighter(QTextDocument)
    QSyntaxHighlighter(QObject)
    """
    def currentBlock(self): # real signature unknown; restored from __doc__
        """ QSyntaxHighlighter.currentBlock() -> QTextBlock """
        return QTextBlock

    def currentBlockState(self): # real signature unknown; restored from __doc__
        """ QSyntaxHighlighter.currentBlockState() -> int """
        return 0

    def currentBlockUserData(self): # real signature unknown; restored from __doc__
        """ QSyntaxHighlighter.currentBlockUserData() -> QTextBlockUserData """
        return QTextBlockUserData

    def document(self): # real signature unknown; restored from __doc__
        """ QSyntaxHighlighter.document() -> QTextDocument """
        return QTextDocument

    def format(self, p_int): # real signature unknown; restored from __doc__
        """ QSyntaxHighlighter.format(int) -> QTextCharFormat """
        return QTextCharFormat

    def highlightBlock(self, QString): # real signature unknown; restored from __doc__
        """ QSyntaxHighlighter.highlightBlock(QString) """
        pass

    def previousBlockState(self): # real signature unknown; restored from __doc__
        """ QSyntaxHighlighter.previousBlockState() -> int """
        return 0

    def rehighlight(self): # real signature unknown; restored from __doc__
        """ QSyntaxHighlighter.rehighlight() """
        pass

    def rehighlightBlock(self, QTextBlock): # real signature unknown; restored from __doc__
        """ QSyntaxHighlighter.rehighlightBlock(QTextBlock) """
        pass

    def setCurrentBlockState(self, p_int): # real signature unknown; restored from __doc__
        """ QSyntaxHighlighter.setCurrentBlockState(int) """
        pass

    def setCurrentBlockUserData(self, QTextBlockUserData): # real signature unknown; restored from __doc__
        """ QSyntaxHighlighter.setCurrentBlockUserData(QTextBlockUserData) """
        pass

    def setDocument(self, QTextDocument): # real signature unknown; restored from __doc__
        """ QSyntaxHighlighter.setDocument(QTextDocument) """
        pass

    def setFormat(self, p_int, p_int_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSyntaxHighlighter.setFormat(int, int, QTextCharFormat)
        QSyntaxHighlighter.setFormat(int, int, QColor)
        QSyntaxHighlighter.setFormat(int, int, QFont)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


