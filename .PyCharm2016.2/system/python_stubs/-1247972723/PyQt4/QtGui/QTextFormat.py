# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QTextFormat(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QTextFormat()
    QTextFormat(int)
    QTextFormat(QTextFormat)
    QTextFormat(QVariant)
    """
    def background(self): # real signature unknown; restored from __doc__
        """ QTextFormat.background() -> QBrush """
        return QBrush

    def boolProperty(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.boolProperty(int) -> bool """
        return False

    def brushProperty(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.brushProperty(int) -> QBrush """
        return QBrush

    def clearBackground(self): # real signature unknown; restored from __doc__
        """ QTextFormat.clearBackground() """
        pass

    def clearForeground(self): # real signature unknown; restored from __doc__
        """ QTextFormat.clearForeground() """
        pass

    def clearProperty(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.clearProperty(int) """
        pass

    def colorProperty(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.colorProperty(int) -> QColor """
        return QColor

    def doubleProperty(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.doubleProperty(int) -> float """
        return 0.0

    def foreground(self): # real signature unknown; restored from __doc__
        """ QTextFormat.foreground() -> QBrush """
        return QBrush

    def hasProperty(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.hasProperty(int) -> bool """
        return False

    def intProperty(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.intProperty(int) -> int """
        return 0

    def isBlockFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.isBlockFormat() -> bool """
        return False

    def isCharFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.isCharFormat() -> bool """
        return False

    def isFrameFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.isFrameFormat() -> bool """
        return False

    def isImageFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.isImageFormat() -> bool """
        return False

    def isListFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.isListFormat() -> bool """
        return False

    def isTableCellFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.isTableCellFormat() -> bool """
        return False

    def isTableFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.isTableFormat() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QTextFormat.isValid() -> bool """
        return False

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ QTextFormat.layoutDirection() -> Qt.LayoutDirection """
        pass

    def lengthProperty(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.lengthProperty(int) -> QTextLength """
        return QTextLength

    def lengthVectorProperty(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.lengthVectorProperty(int) -> list-of-QTextLength """
        pass

    def merge(self, QTextFormat): # real signature unknown; restored from __doc__
        """ QTextFormat.merge(QTextFormat) """
        pass

    def objectIndex(self): # real signature unknown; restored from __doc__
        """ QTextFormat.objectIndex() -> int """
        return 0

    def objectType(self): # real signature unknown; restored from __doc__
        """ QTextFormat.objectType() -> int """
        return 0

    def penProperty(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.penProperty(int) -> QPen """
        return QPen

    def properties(self): # real signature unknown; restored from __doc__
        """ QTextFormat.properties() -> dict-of-int-QVariant """
        pass

    def property(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.property(int) -> QVariant """
        pass

    def propertyCount(self): # real signature unknown; restored from __doc__
        """ QTextFormat.propertyCount() -> int """
        return 0

    def setBackground(self, QBrush): # real signature unknown; restored from __doc__
        """ QTextFormat.setBackground(QBrush) """
        pass

    def setForeground(self, QBrush): # real signature unknown; restored from __doc__
        """ QTextFormat.setForeground(QBrush) """
        pass

    def setLayoutDirection(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ QTextFormat.setLayoutDirection(Qt.LayoutDirection) """
        pass

    def setObjectIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.setObjectIndex(int) """
        pass

    def setObjectType(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.setObjectType(int) """
        pass

    def setProperty(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextFormat.setProperty(int, QVariant)
        QTextFormat.setProperty(int, list-of-QTextLength)
        """
        pass

    def stringProperty(self, p_int): # real signature unknown; restored from __doc__
        """ QTextFormat.stringProperty(int) -> QString """
        pass

    def toBlockFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.toBlockFormat() -> QTextBlockFormat """
        return QTextBlockFormat

    def toCharFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.toCharFormat() -> QTextCharFormat """
        return QTextCharFormat

    def toFrameFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.toFrameFormat() -> QTextFrameFormat """
        return QTextFrameFormat

    def toImageFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.toImageFormat() -> QTextImageFormat """
        return QTextImageFormat

    def toListFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.toListFormat() -> QTextListFormat """
        return QTextListFormat

    def toTableCellFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.toTableCellFormat() -> QTextTableCellFormat """
        return QTextTableCellFormat

    def toTableFormat(self): # real signature unknown; restored from __doc__
        """ QTextFormat.toTableFormat() -> QTextTableFormat """
        return QTextTableFormat

    def type(self): # real signature unknown; restored from __doc__
        """ QTextFormat.type() -> int """
        return 0

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


    AnchorHref = 8241
    AnchorName = 8242
    BackgroundBrush = 2080
    BackgroundImageUrl = 2083
    BlockAlignment = 4112
    BlockBottomMargin = 4145
    BlockFormat = 1
    BlockIndent = 4160
    BlockLeftMargin = 4146
    BlockNonBreakableLines = 4176
    BlockRightMargin = 4147
    BlockTopMargin = 4144
    BlockTrailingHorizontalRulerWidth = 4192
    CharFormat = 2
    CssFloat = 2048
    FirstFontProperty = 8160
    FontCapitalization = 8160
    FontFamily = 8192
    FontFixedPitch = 8200
    FontHintingPreference = 8166
    FontItalic = 8196
    FontKerning = 8165
    FontLetterSpacing = 8161
    FontOverline = 8198
    FontPixelSize = 8201
    FontPointSize = 8193
    FontSizeAdjustment = 8194
    FontSizeIncrement = 8194
    FontStrikeOut = 8199
    FontStyleHint = 8163
    FontStyleStrategy = 8164
    FontUnderline = 8197
    FontWeight = 8195
    FontWordSpacing = 8162
    ForegroundBrush = 2081
    FrameBorder = 16384
    FrameBorderBrush = 16393
    FrameBorderStyle = 16400
    FrameBottomMargin = 16390
    FrameFormat = 5
    FrameHeight = 16388
    FrameLeftMargin = 16391
    FrameMargin = 16385
    FramePadding = 16386
    FrameRightMargin = 16392
    FrameTopMargin = 16389
    FrameWidth = 16387
    FullWidthSelection = 24576
    ImageHeight = 20497
    ImageName = 20480
    ImageObject = 1
    ImageWidth = 20496
    InvalidFormat = -1
    IsAnchor = 8240
    LastFontProperty = 8201
    LayoutDirection = 2049
    LineHeight = 4168
    LineHeightType = 4169
    ListFormat = 3
    ListIndent = 12289
    ListNumberPrefix = 12290
    ListNumberSuffix = 12291
    ListStyle = 12288
    NoObject = 0
    ObjectIndex = 0
    ObjectType = 12032
    OutlinePen = 2064
    PageBreakPolicy = 28672
    PageBreak_AlwaysAfter = 16
    PageBreak_AlwaysBefore = 1
    PageBreak_Auto = 0
    TableCellBottomPadding = 18451
    TableCellColumnSpan = 18449
    TableCellLeftPadding = 18452
    TableCellObject = 3
    TableCellPadding = 16643
    TableCellRightPadding = 18453
    TableCellRowSpan = 18448
    TableCellSpacing = 16642
    TableCellTopPadding = 18450
    TableColumns = 16640
    TableColumnWidthConstraints = 16641
    TableFormat = 4
    TableHeaderRowCount = 16644
    TableObject = 2
    TabPositions = 4149
    TextIndent = 4148
    TextOutline = 8226
    TextToolTip = 8228
    TextUnderlineColor = 8208
    TextUnderlineStyle = 8227
    TextVerticalAlignment = 8225
    UserFormat = 100
    UserObject = 4096
    UserProperty = 1048576


