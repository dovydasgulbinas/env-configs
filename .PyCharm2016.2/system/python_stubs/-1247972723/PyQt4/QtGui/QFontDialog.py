# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QFontDialog(QDialog):
    """
    QFontDialog(QWidget parent=None)
    QFontDialog(QFont, QWidget parent=None)
    """
    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QFontDialog.changeEvent(QEvent) """
        pass

    def currentFont(self): # real signature unknown; restored from __doc__
        """ QFontDialog.currentFont() -> QFont """
        return QFont

    def currentFontChanged(self, *args, **kwargs): # real signature unknown
        """ QFontDialog.currentFontChanged[QFont] [signal] """
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ QFontDialog.done(int) """
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def fontSelected(self, *args, **kwargs): # real signature unknown
        """ QFontDialog.fontSelected[QFont] [signal] """
        pass

    def getFont(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFontDialog.getFont(QFont, QWidget, QString, QFontDialog.FontDialogOptions) -> (QFont, bool)
        QFontDialog.getFont(QFont, QWidget, QString) -> (QFont, bool)
        QFontDialog.getFont(QFont, QWidget parent=None) -> (QFont, bool)
        QFontDialog.getFont(QWidget parent=None) -> (QFont, bool)
        """
        pass

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFontDialog.open()
        QFontDialog.open(QObject, SLOT())
        QFontDialog.open(callable)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ QFontDialog.options() -> QFontDialog.FontDialogOptions """
        pass

    def selectedFont(self): # real signature unknown; restored from __doc__
        """ QFontDialog.selectedFont() -> QFont """
        return QFont

    def setCurrentFont(self, QFont): # real signature unknown; restored from __doc__
        """ QFontDialog.setCurrentFont(QFont) """
        pass

    def setOption(self, QFontDialog_FontDialogOption, bool_on=True): # real signature unknown; restored from __doc__
        """ QFontDialog.setOption(QFontDialog.FontDialogOption, bool on=True) """
        pass

    def setOptions(self, QFontDialog_FontDialogOptions): # real signature unknown; restored from __doc__
        """ QFontDialog.setOptions(QFontDialog.FontDialogOptions) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QFontDialog.setVisible(bool) """
        pass

    def testOption(self, QFontDialog_FontDialogOption): # real signature unknown; restored from __doc__
        """ QFontDialog.testOption(QFontDialog.FontDialogOption) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DontUseNativeDialog = 2
    NoButtons = 1


