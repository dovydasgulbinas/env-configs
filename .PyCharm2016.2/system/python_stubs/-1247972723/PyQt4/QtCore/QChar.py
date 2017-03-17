# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QChar(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QChar()
    QChar(str)
    QChar(QLatin1Char)
    QChar(str, str)
    QChar(int)
    QChar(QChar.SpecialCharacter)
    QChar(QChar)
    """
    def category(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.category() -> QChar.Category
        QChar.category(int) -> QChar.Category
        """
        pass

    def cell(self): # real signature unknown; restored from __doc__
        """ QChar.cell() -> str """
        return ""

    def combiningClass(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.combiningClass() -> str
        QChar.combiningClass(int) -> str
        """
        return ""

    def currentUnicodeVersion(self): # real signature unknown; restored from __doc__
        """ QChar.currentUnicodeVersion() -> QChar.UnicodeVersion """
        pass

    def decomposition(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.decomposition() -> QString
        QChar.decomposition(int) -> QString
        """
        return QString

    def decompositionTag(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.decompositionTag() -> QChar.Decomposition
        QChar.decompositionTag(int) -> QChar.Decomposition
        """
        pass

    def digitValue(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.digitValue() -> int
        QChar.digitValue(int) -> int
        """
        return 0

    def direction(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.direction() -> QChar.Direction
        QChar.direction(int) -> QChar.Direction
        """
        pass

    def fromAscii(self, p_str): # real signature unknown; restored from __doc__
        """ QChar.fromAscii(str) -> QChar """
        return QChar

    def fromLatin1(self, p_str): # real signature unknown; restored from __doc__
        """ QChar.fromLatin1(str) -> QChar """
        return QChar

    def hasMirrored(self): # real signature unknown; restored from __doc__
        """ QChar.hasMirrored() -> bool """
        return False

    def highSurrogate(self, p_int): # real signature unknown; restored from __doc__
        """ QChar.highSurrogate(int) -> int """
        return 0

    def isDigit(self): # real signature unknown; restored from __doc__
        """ QChar.isDigit() -> bool """
        return False

    def isHighSurrogate(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.isHighSurrogate() -> bool
        QChar.isHighSurrogate(int) -> bool
        """
        return False

    def isLetter(self): # real signature unknown; restored from __doc__
        """ QChar.isLetter() -> bool """
        return False

    def isLetterOrNumber(self): # real signature unknown; restored from __doc__
        """ QChar.isLetterOrNumber() -> bool """
        return False

    def isLower(self): # real signature unknown; restored from __doc__
        """ QChar.isLower() -> bool """
        return False

    def isLowSurrogate(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.isLowSurrogate() -> bool
        QChar.isLowSurrogate(int) -> bool
        """
        return False

    def isMark(self): # real signature unknown; restored from __doc__
        """ QChar.isMark() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QChar.isNull() -> bool """
        return False

    def isNumber(self): # real signature unknown; restored from __doc__
        """ QChar.isNumber() -> bool """
        return False

    def isPrint(self): # real signature unknown; restored from __doc__
        """ QChar.isPrint() -> bool """
        return False

    def isPunct(self): # real signature unknown; restored from __doc__
        """ QChar.isPunct() -> bool """
        return False

    def isSpace(self): # real signature unknown; restored from __doc__
        """ QChar.isSpace() -> bool """
        return False

    def isSymbol(self): # real signature unknown; restored from __doc__
        """ QChar.isSymbol() -> bool """
        return False

    def isTitleCase(self): # real signature unknown; restored from __doc__
        """ QChar.isTitleCase() -> bool """
        return False

    def isUpper(self): # real signature unknown; restored from __doc__
        """ QChar.isUpper() -> bool """
        return False

    def joining(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.joining() -> QChar.Joining
        QChar.joining(int) -> QChar.Joining
        """
        pass

    def lowSurrogate(self, p_int): # real signature unknown; restored from __doc__
        """ QChar.lowSurrogate(int) -> int """
        return 0

    def mirroredChar(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.mirroredChar() -> QChar
        QChar.mirroredChar(int) -> int
        """
        return QChar or 0

    def requiresSurrogates(self, p_int): # real signature unknown; restored from __doc__
        """ QChar.requiresSurrogates(int) -> bool """
        return False

    def row(self): # real signature unknown; restored from __doc__
        """ QChar.row() -> str """
        return ""

    def setCell(self, p_str): # real signature unknown; restored from __doc__
        """ QChar.setCell(str) """
        pass

    def setRow(self, p_str): # real signature unknown; restored from __doc__
        """ QChar.setRow(str) """
        pass

    def surrogateToUcs4(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.surrogateToUcs4(int, int) -> int
        QChar.surrogateToUcs4(QChar, QChar) -> int
        """
        return 0

    def toAscii(self): # real signature unknown; restored from __doc__
        """ QChar.toAscii() -> str """
        return ""

    def toCaseFolded(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.toCaseFolded() -> QChar
        QChar.toCaseFolded(int) -> int
        """
        return QChar or 0

    def toLatin1(self): # real signature unknown; restored from __doc__
        """ QChar.toLatin1() -> str """
        return ""

    def toLower(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.toLower() -> QChar
        QChar.toLower(int) -> int
        """
        return QChar or 0

    def toTitleCase(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.toTitleCase() -> QChar
        QChar.toTitleCase(int) -> int
        """
        return QChar or 0

    def toUpper(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.toUpper() -> QChar
        QChar.toUpper(int) -> int
        """
        return QChar or 0

    def unicode(self): # real signature unknown; restored from __doc__
        """ QChar.unicode() -> int """
        return 0

    def unicodeVersion(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QChar.unicodeVersion() -> QChar.UnicodeVersion
        QChar.unicodeVersion(int) -> QChar.UnicodeVersion
        """
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
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

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
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

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ByteOrderMark = 65279
    ByteOrderSwapped = 65534
    Canonical = 1
    Center = 3
    Circle = 8
    Combining_Above = 230
    Combining_AboveAttached = 214
    Combining_AboveLeft = 228
    Combining_AboveLeftAttached = 212
    Combining_AboveRight = 232
    Combining_AboveRightAttached = 216
    Combining_Below = 220
    Combining_BelowAttached = 202
    Combining_BelowLeft = 218
    Combining_BelowLeftAttached = 200
    Combining_BelowRight = 222
    Combining_BelowRightAttached = 204
    Combining_DoubleAbove = 234
    Combining_DoubleBelow = 233
    Combining_IotaSubscript = 240
    Combining_Left = 224
    Combining_LeftAttached = 208
    Combining_Right = 226
    Combining_RightAttached = 210
    Compat = 16
    DirAL = 13
    DirAN = 5
    DirB = 7
    DirBN = 18
    DirCS = 6
    DirEN = 2
    DirES = 3
    DirET = 4
    DirL = 0
    DirLRE = 11
    DirLRO = 12
    DirNSM = 17
    DirON = 10
    DirPDF = 16
    DirR = 1
    DirRLE = 14
    DirRLO = 15
    DirS = 8
    DirWS = 9
    Dual = 1
    Final = 6
    Font = 2
    Fraction = 17
    Initial = 4
    Isolated = 7
    Letter_Lowercase = 16
    Letter_Modifier = 18
    Letter_Other = 19
    Letter_Titlecase = 17
    Letter_Uppercase = 15
    LineSeparator = 8232
    Mark_Enclosing = 3
    Mark_NonSpacing = 1
    Mark_SpacingCombining = 2
    Medial = 5
    Narrow = 13
    Nbsp = 160
    NoBreak = 3
    NoCategory = 0
    NoDecomposition = 0
    Null = 0
    Number_DecimalDigit = 4
    Number_Letter = 5
    Number_Other = 6
    ObjectReplacementCharacter = 65532
    OtherJoining = 0
    Other_Control = 10
    Other_Format = 11
    Other_NotAssigned = 14
    Other_PrivateUse = 13
    Other_Surrogate = 12
    ParagraphSeparator = 8233
    Punctuation_Close = 23
    Punctuation_Connector = 20
    Punctuation_Dash = 21
    Punctuation_Dask = 21
    Punctuation_FinalQuote = 25
    Punctuation_InitialQuote = 24
    Punctuation_Open = 22
    Punctuation_Other = 26
    ReplacementCharacter = 65533
    Right = 2
    Separator_Line = 8
    Separator_Paragraph = 9
    Separator_Space = 7
    Small = 14
    Square = 15
    Sub = 10
    Super = 9
    Symbol_Currency = 28
    Symbol_Math = 27
    Symbol_Modifier = 29
    Symbol_Other = 30
    Unicode_1_1 = 1
    Unicode_2_0 = 2
    Unicode_2_1_2 = 3
    Unicode_3_0 = 4
    Unicode_3_1 = 5
    Unicode_3_2 = 6
    Unicode_4_0 = 7
    Unicode_4_1 = 8
    Unicode_5_0 = 9
    Unicode_Unassigned = 0
    Vertical = 11
    Wide = 12


