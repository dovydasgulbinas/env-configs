# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QFontDatabase(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QFontDatabase()
    QFontDatabase(QFontDatabase)
    """
    def addApplicationFont(self, QString): # real signature unknown; restored from __doc__
        """ QFontDatabase.addApplicationFont(QString) -> int """
        return 0

    def addApplicationFontFromData(self, QByteArray): # real signature unknown; restored from __doc__
        """ QFontDatabase.addApplicationFontFromData(QByteArray) -> int """
        return 0

    def applicationFontFamilies(self, p_int): # real signature unknown; restored from __doc__
        """ QFontDatabase.applicationFontFamilies(int) -> QStringList """
        pass

    def bold(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QFontDatabase.bold(QString, QString) -> bool """
        return False

    def families(self, QFontDatabase_WritingSystem_writingSystem=None): # real signature unknown; restored from __doc__
        """ QFontDatabase.families(QFontDatabase.WritingSystem writingSystem=QFontDatabase.Any) -> QStringList """
        pass

    def font(self, QString, QString_1, p_int): # real signature unknown; restored from __doc__
        """ QFontDatabase.font(QString, QString, int) -> QFont """
        return QFont

    def isBitmapScalable(self, QString, QString_style=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFontDatabase.isBitmapScalable(QString, QString style=QString()) -> bool """
        pass

    def isFixedPitch(self, QString, QString_style=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFontDatabase.isFixedPitch(QString, QString style=QString()) -> bool """
        pass

    def isScalable(self, QString, QString_style=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFontDatabase.isScalable(QString, QString style=QString()) -> bool """
        pass

    def isSmoothlyScalable(self, QString, QString_style=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFontDatabase.isSmoothlyScalable(QString, QString style=QString()) -> bool """
        pass

    def italic(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QFontDatabase.italic(QString, QString) -> bool """
        return False

    def pointSizes(self, QString, QString_style=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFontDatabase.pointSizes(QString, QString style=QString()) -> list-of-int """
        pass

    def removeAllApplicationFonts(self): # real signature unknown; restored from __doc__
        """ QFontDatabase.removeAllApplicationFonts() -> bool """
        return False

    def removeApplicationFont(self, p_int): # real signature unknown; restored from __doc__
        """ QFontDatabase.removeApplicationFont(int) -> bool """
        return False

    def smoothSizes(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QFontDatabase.smoothSizes(QString, QString) -> list-of-int """
        pass

    def standardSizes(self): # real signature unknown; restored from __doc__
        """ QFontDatabase.standardSizes() -> list-of-int """
        pass

    def styles(self, QString): # real signature unknown; restored from __doc__
        """ QFontDatabase.styles(QString) -> QStringList """
        pass

    def styleString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFontDatabase.styleString(QFont) -> QString
        QFontDatabase.styleString(QFontInfo) -> QString
        """
        pass

    def supportsThreadedFontRendering(self): # real signature unknown; restored from __doc__
        """ QFontDatabase.supportsThreadedFontRendering() -> bool """
        return False

    def weight(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QFontDatabase.weight(QString, QString) -> int """
        return 0

    def writingSystemName(self, QFontDatabase_WritingSystem): # real signature unknown; restored from __doc__
        """ QFontDatabase.writingSystemName(QFontDatabase.WritingSystem) -> QString """
        pass

    def writingSystems(self, QString=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFontDatabase.writingSystems() -> list-of-QFontDatabase.WritingSystem
        QFontDatabase.writingSystems(QString) -> list-of-QFontDatabase.WritingSystem
        """
        pass

    def writingSystemSample(self, QFontDatabase_WritingSystem): # real signature unknown; restored from __doc__
        """ QFontDatabase.writingSystemSample(QFontDatabase.WritingSystem) -> QString """
        pass

    def __init__(self, QFontDatabase=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Any = 0
    Arabic = 6
    Armenian = 4
    Bengali = 10
    Cyrillic = 3
    Devanagari = 9
    Georgian = 23
    Greek = 2
    Gujarati = 12
    Gurmukhi = 11
    Hebrew = 5
    Japanese = 27
    Kannada = 16
    Khmer = 24
    Korean = 28
    Lao = 20
    Latin = 1
    Malayalam = 17
    Myanmar = 22
    Nko = 33
    Ogham = 31
    Oriya = 13
    Other = 30
    Runic = 32
    SimplifiedChinese = 25
    Sinhala = 18
    Symbol = 30
    Syriac = 7
    Tamil = 14
    Telugu = 15
    Thaana = 8
    Thai = 19
    Tibetan = 21
    TraditionalChinese = 26
    Vietnamese = 29


