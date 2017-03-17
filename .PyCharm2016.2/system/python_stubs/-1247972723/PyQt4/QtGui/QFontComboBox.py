# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QComboBox import QComboBox

class QFontComboBox(QComboBox):
    """ QFontComboBox(QWidget parent=None) """
    def currentFont(self): # real signature unknown; restored from __doc__
        """ QFontComboBox.currentFont() -> QFont """
        return QFont

    def currentFontChanged(self, *args, **kwargs): # real signature unknown
        """ QFontComboBox.currentFontChanged[QFont] [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QFontComboBox.event(QEvent) -> bool """
        return False

    def fontFilters(self): # real signature unknown; restored from __doc__
        """ QFontComboBox.fontFilters() -> QFontComboBox.FontFilters """
        pass

    def setCurrentFont(self, QFont): # real signature unknown; restored from __doc__
        """ QFontComboBox.setCurrentFont(QFont) """
        pass

    def setFontFilters(self, QFontComboBox_FontFilters): # real signature unknown; restored from __doc__
        """ QFontComboBox.setFontFilters(QFontComboBox.FontFilters) """
        pass

    def setWritingSystem(self, QFontDatabase_WritingSystem): # real signature unknown; restored from __doc__
        """ QFontComboBox.setWritingSystem(QFontDatabase.WritingSystem) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QFontComboBox.sizeHint() -> QSize """
        pass

    def writingSystem(self): # real signature unknown; restored from __doc__
        """ QFontComboBox.writingSystem() -> QFontDatabase.WritingSystem """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    AllFonts = 0
    MonospacedFonts = 4
    NonScalableFonts = 2
    ProportionalFonts = 8
    ScalableFonts = 1


