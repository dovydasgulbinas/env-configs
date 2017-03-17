# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QRawFont(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QRawFont()
    QRawFont(QString, float, QFont.HintingPreference hintingPreference=QFont.PreferDefaultHinting)
    QRawFont(QByteArray, float, QFont.HintingPreference hintingPreference=QFont.PreferDefaultHinting)
    QRawFont(QRawFont)
    """
    def advancesForGlyphIndexes(self, list_of_int): # real signature unknown; restored from __doc__
        """ QRawFont.advancesForGlyphIndexes(list-of-int) -> list-of-QPointF """
        pass

    def alphaMapForGlyph(self, p_int, QRawFont_AntialiasingType_antialiasingType=None, QTransform_transform=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QRawFont.alphaMapForGlyph(int, QRawFont.AntialiasingType antialiasingType=QRawFont.SubPixelAntialiasing, QTransform transform=QTransform()) -> QImage """
        pass

    def ascent(self): # real signature unknown; restored from __doc__
        """ QRawFont.ascent() -> float """
        return 0.0

    def averageCharWidth(self): # real signature unknown; restored from __doc__
        """ QRawFont.averageCharWidth() -> float """
        return 0.0

    def descent(self): # real signature unknown; restored from __doc__
        """ QRawFont.descent() -> float """
        return 0.0

    def familyName(self): # real signature unknown; restored from __doc__
        """ QRawFont.familyName() -> QString """
        pass

    def fontTable(self, p_str): # real signature unknown; restored from __doc__
        """ QRawFont.fontTable(str) -> QByteArray """
        pass

    def fromFont(self, QFont, QFontDatabase_WritingSystem_writingSystem=None): # real signature unknown; restored from __doc__
        """ QRawFont.fromFont(QFont, QFontDatabase.WritingSystem writingSystem=QFontDatabase.Any) -> QRawFont """
        return QRawFont

    def glyphIndexesForString(self, QString): # real signature unknown; restored from __doc__
        """ QRawFont.glyphIndexesForString(QString) -> list-of-int """
        pass

    def hintingPreference(self): # real signature unknown; restored from __doc__
        """ QRawFont.hintingPreference() -> QFont.HintingPreference """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ QRawFont.isValid() -> bool """
        return False

    def leading(self): # real signature unknown; restored from __doc__
        """ QRawFont.leading() -> float """
        return 0.0

    def loadFromData(self, QByteArray, p_float, QFont_HintingPreference): # real signature unknown; restored from __doc__
        """ QRawFont.loadFromData(QByteArray, float, QFont.HintingPreference) """
        pass

    def loadFromFile(self, QString, p_float, QFont_HintingPreference): # real signature unknown; restored from __doc__
        """ QRawFont.loadFromFile(QString, float, QFont.HintingPreference) """
        pass

    def maxCharWidth(self): # real signature unknown; restored from __doc__
        """ QRawFont.maxCharWidth() -> float """
        return 0.0

    def pathForGlyph(self, p_int): # real signature unknown; restored from __doc__
        """ QRawFont.pathForGlyph(int) -> QPainterPath """
        return QPainterPath

    def pixelSize(self): # real signature unknown; restored from __doc__
        """ QRawFont.pixelSize() -> float """
        return 0.0

    def setPixelSize(self, p_float): # real signature unknown; restored from __doc__
        """ QRawFont.setPixelSize(float) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ QRawFont.style() -> QFont.Style """
        pass

    def styleName(self): # real signature unknown; restored from __doc__
        """ QRawFont.styleName() -> QString """
        pass

    def supportedWritingSystems(self): # real signature unknown; restored from __doc__
        """ QRawFont.supportedWritingSystems() -> list-of-QFontDatabase.WritingSystem """
        pass

    def supportsCharacter(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRawFont.supportsCharacter(int) -> bool
        QRawFont.supportsCharacter(QChar) -> bool
        """
        return False

    def unitsPerEm(self): # real signature unknown; restored from __doc__
        """ QRawFont.unitsPerEm() -> float """
        return 0.0

    def weight(self): # real signature unknown; restored from __doc__
        """ QRawFont.weight() -> int """
        return 0

    def xHeight(self): # real signature unknown; restored from __doc__
        """ QRawFont.xHeight() -> float """
        return 0.0

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


    PixelAntialiasing = 0
    SubPixelAntialiasing = 1


