# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QRegExp(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QRegExp()
    QRegExp(QString, Qt.CaseSensitivity cs=Qt.CaseSensitive, QRegExp.PatternSyntax syntax=QRegExp.RegExp)
    QRegExp(QRegExp)
    """
    def cap(self, int_nth=0): # real signature unknown; restored from __doc__
        """ QRegExp.cap(int nth=0) -> QString """
        return QString

    def captureCount(self): # real signature unknown; restored from __doc__
        """ QRegExp.captureCount() -> int """
        return 0

    def capturedTexts(self): # real signature unknown; restored from __doc__
        """ QRegExp.capturedTexts() -> QStringList """
        return QStringList

    def caseSensitivity(self): # real signature unknown; restored from __doc__
        """ QRegExp.caseSensitivity() -> Qt.CaseSensitivity """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QRegExp.errorString() -> QString """
        return QString

    def escape(self, QString): # real signature unknown; restored from __doc__
        """ QRegExp.escape(QString) -> QString """
        return QString

    def exactMatch(self, QString): # real signature unknown; restored from __doc__
        """ QRegExp.exactMatch(QString) -> bool """
        return False

    def indexIn(self, QString, int_offset=0, QRegExp_CaretMode_caretMode=None): # real signature unknown; restored from __doc__
        """ QRegExp.indexIn(QString, int offset=0, QRegExp.CaretMode caretMode=QRegExp.CaretAtZero) -> int """
        return 0

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QRegExp.isEmpty() -> bool """
        return False

    def isMinimal(self): # real signature unknown; restored from __doc__
        """ QRegExp.isMinimal() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QRegExp.isValid() -> bool """
        return False

    def lastIndexIn(self, QString, int_offset=-1, QRegExp_CaretMode_caretMode=None): # real signature unknown; restored from __doc__
        """ QRegExp.lastIndexIn(QString, int offset=-1, QRegExp.CaretMode caretMode=QRegExp.CaretAtZero) -> int """
        return 0

    def matchedLength(self): # real signature unknown; restored from __doc__
        """ QRegExp.matchedLength() -> int """
        return 0

    def numCaptures(self): # real signature unknown; restored from __doc__
        """ QRegExp.numCaptures() -> int """
        return 0

    def pattern(self): # real signature unknown; restored from __doc__
        """ QRegExp.pattern() -> QString """
        return QString

    def patternSyntax(self): # real signature unknown; restored from __doc__
        """ QRegExp.patternSyntax() -> QRegExp.PatternSyntax """
        pass

    def pos(self, int_nth=0): # real signature unknown; restored from __doc__
        """ QRegExp.pos(int nth=0) -> int """
        return 0

    def setCaseSensitivity(self, Qt_CaseSensitivity): # real signature unknown; restored from __doc__
        """ QRegExp.setCaseSensitivity(Qt.CaseSensitivity) """
        pass

    def setMinimal(self, bool): # real signature unknown; restored from __doc__
        """ QRegExp.setMinimal(bool) """
        pass

    def setPattern(self, QString): # real signature unknown; restored from __doc__
        """ QRegExp.setPattern(QString) """
        pass

    def setPatternSyntax(self, QRegExp_PatternSyntax): # real signature unknown; restored from __doc__
        """ QRegExp.setPatternSyntax(QRegExp.PatternSyntax) """
        pass

    def swap(self, QRegExp): # real signature unknown; restored from __doc__
        """ QRegExp.swap(QRegExp) """
        pass

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

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CaretAtOffset = 1
    CaretAtZero = 0
    CaretWontMatch = 2
    FixedString = 2
    RegExp = 0
    RegExp2 = 3
    W3CXmlSchema11 = 5
    Wildcard = 1
    WildcardUnix = 4


