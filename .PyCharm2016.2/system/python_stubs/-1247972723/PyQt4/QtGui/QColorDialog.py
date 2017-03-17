# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QColorDialog(QDialog):
    """
    QColorDialog(QWidget parent=None)
    QColorDialog(QColor, QWidget parent=None)
    """
    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QColorDialog.changeEvent(QEvent) """
        pass

    def colorSelected(self, *args, **kwargs): # real signature unknown
        """ QColorDialog.colorSelected[QColor] [signal] """
        pass

    def currentColor(self): # real signature unknown; restored from __doc__
        """ QColorDialog.currentColor() -> QColor """
        return QColor

    def currentColorChanged(self, *args, **kwargs): # real signature unknown
        """ QColorDialog.currentColorChanged[QColor] [signal] """
        pass

    def customColor(self, p_int): # real signature unknown; restored from __doc__
        """ QColorDialog.customColor(int) -> int """
        return 0

    def customCount(self): # real signature unknown; restored from __doc__
        """ QColorDialog.customCount() -> int """
        return 0

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ QColorDialog.done(int) """
        pass

    def getColor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QColorDialog.getColor(QColor initial=Qt.white, QWidget parent=None) -> QColor
        QColorDialog.getColor(QColor, QWidget, QString, QColorDialog.ColorDialogOptions options=0) -> QColor
        """
        return QColor

    def getRgba(self, int_initial=4294967295, QWidget_parent=None): # real signature unknown; restored from __doc__
        """ QColorDialog.getRgba(int initial=4294967295, QWidget parent=None) -> (int, bool) """
        pass

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QColorDialog.open()
        QColorDialog.open(QObject, SLOT())
        QColorDialog.open(callable)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ QColorDialog.options() -> QColorDialog.ColorDialogOptions """
        pass

    def selectedColor(self): # real signature unknown; restored from __doc__
        """ QColorDialog.selectedColor() -> QColor """
        return QColor

    def setCurrentColor(self, QColor): # real signature unknown; restored from __doc__
        """ QColorDialog.setCurrentColor(QColor) """
        pass

    def setCustomColor(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QColorDialog.setCustomColor(int, int) """
        pass

    def setOption(self, QColorDialog_ColorDialogOption, bool_on=True): # real signature unknown; restored from __doc__
        """ QColorDialog.setOption(QColorDialog.ColorDialogOption, bool on=True) """
        pass

    def setOptions(self, QColorDialog_ColorDialogOptions): # real signature unknown; restored from __doc__
        """ QColorDialog.setOptions(QColorDialog.ColorDialogOptions) """
        pass

    def setStandardColor(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QColorDialog.setStandardColor(int, int) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QColorDialog.setVisible(bool) """
        pass

    def testOption(self, QColorDialog_ColorDialogOption): # real signature unknown; restored from __doc__
        """ QColorDialog.testOption(QColorDialog.ColorDialogOption) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DontUseNativeDialog = 4
    NoButtons = 2
    ShowAlphaChannel = 1


