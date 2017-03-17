# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QKeySequence(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QKeySequence()
    QKeySequence(QKeySequence)
    QKeySequence(QString, QKeySequence.SequenceFormat)
    QKeySequence(int, int key2=0, int key3=0, int key4=0)
    QKeySequence(QVariant)
    """
    def count(self): # real signature unknown; restored from __doc__
        """ QKeySequence.count() -> int """
        return 0

    def fromString(self, QString, QKeySequence_SequenceFormat_format=None): # real signature unknown; restored from __doc__
        """ QKeySequence.fromString(QString, QKeySequence.SequenceFormat format=QKeySequence.PortableText) -> QKeySequence """
        return QKeySequence

    def isDetached(self): # real signature unknown; restored from __doc__
        """ QKeySequence.isDetached() -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QKeySequence.isEmpty() -> bool """
        return False

    def keyBindings(self, QKeySequence_StandardKey): # real signature unknown; restored from __doc__
        """ QKeySequence.keyBindings(QKeySequence.StandardKey) -> list-of-QKeySequence """
        pass

    def matches(self, QKeySequence): # real signature unknown; restored from __doc__
        """ QKeySequence.matches(QKeySequence) -> QKeySequence.SequenceMatch """
        pass

    def mnemonic(self, QString): # real signature unknown; restored from __doc__
        """ QKeySequence.mnemonic(QString) -> QKeySequence """
        return QKeySequence

    def swap(self, QKeySequence): # real signature unknown; restored from __doc__
        """ QKeySequence.swap(QKeySequence) """
        pass

    def toString(self, QKeySequence_SequenceFormat_format=None): # real signature unknown; restored from __doc__
        """ QKeySequence.toString(QKeySequence.SequenceFormat format=QKeySequence.PortableText) -> QString """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ x.__int__() <==> int(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AddTab = 19
    Back = 13
    Bold = 27
    Close = 4
    Copy = 9
    Cut = 8
    Delete = 7
    DeleteEndOfLine = 60
    DeleteEndOfWord = 59
    DeleteStartOfWord = 58
    ExactMatch = 2
    Find = 22
    FindNext = 23
    FindPrevious = 24
    Forward = 14
    HelpContents = 1
    InsertLineSeparator = 62
    InsertParagraphSeparator = 61
    Italic = 28
    MoveToEndOfBlock = 41
    MoveToEndOfDocument = 43
    MoveToEndOfLine = 39
    MoveToNextChar = 30
    MoveToNextLine = 34
    MoveToNextPage = 36
    MoveToNextWord = 32
    MoveToPreviousChar = 31
    MoveToPreviousLine = 35
    MoveToPreviousPage = 37
    MoveToPreviousWord = 33
    MoveToStartOfBlock = 40
    MoveToStartOfDocument = 42
    MoveToStartOfLine = 38
    NativeText = 0
    New = 6
    NextChild = 20
    NoMatch = 0
    Open = 3
    PartialMatch = 1
    Paste = 10
    PortableText = 1
    Preferences = 64
    PreviousChild = 21
    Print = 18
    Quit = 65
    Redo = 12
    Refresh = 15
    Replace = 25
    Save = 5
    SaveAs = 63
    SelectAll = 26
    SelectEndOfBlock = 55
    SelectEndOfDocument = 57
    SelectEndOfLine = 53
    SelectNextChar = 44
    SelectNextLine = 48
    SelectNextPage = 50
    SelectNextWord = 46
    SelectPreviousChar = 45
    SelectPreviousLine = 49
    SelectPreviousPage = 51
    SelectPreviousWord = 47
    SelectStartOfBlock = 54
    SelectStartOfDocument = 56
    SelectStartOfLine = 52
    Underline = 29
    Undo = 11
    UnknownKey = 0
    WhatsThis = 2
    ZoomIn = 16
    ZoomOut = 17


