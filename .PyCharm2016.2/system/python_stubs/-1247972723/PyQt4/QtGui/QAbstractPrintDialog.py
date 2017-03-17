# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QAbstractPrintDialog(QDialog):
    """ QAbstractPrintDialog(QPrinter, QWidget parent=None) """
    def addEnabledOption(self, QAbstractPrintDialog_PrintDialogOption): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.addEnabledOption(QAbstractPrintDialog.PrintDialogOption) """
        pass

    def enabledOptions(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.enabledOptions() -> QAbstractPrintDialog.PrintDialogOptions """
        pass

    def exec_(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.exec_() -> int """
        return 0

    def fromPage(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.fromPage() -> int """
        return 0

    def isOptionEnabled(self, QAbstractPrintDialog_PrintDialogOption): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.isOptionEnabled(QAbstractPrintDialog.PrintDialogOption) -> bool """
        return False

    def maxPage(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.maxPage() -> int """
        return 0

    def minPage(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.minPage() -> int """
        return 0

    def printer(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.printer() -> QPrinter """
        return QPrinter

    def printRange(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.printRange() -> QAbstractPrintDialog.PrintRange """
        pass

    def setEnabledOptions(self, QAbstractPrintDialog_PrintDialogOptions): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.setEnabledOptions(QAbstractPrintDialog.PrintDialogOptions) """
        pass

    def setFromTo(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.setFromTo(int, int) """
        pass

    def setMinMax(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.setMinMax(int, int) """
        pass

    def setOptionTabs(self, list_of_QWidget): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.setOptionTabs(list-of-QWidget) """
        pass

    def setPrintRange(self, QAbstractPrintDialog_PrintRange): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.setPrintRange(QAbstractPrintDialog.PrintRange) """
        pass

    def toPage(self): # real signature unknown; restored from __doc__
        """ QAbstractPrintDialog.toPage() -> int """
        return 0

    def __init__(self, QPrinter, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    AllPages = 0
    CurrentPage = 3
    None = 0
    None_ = 0
    PageRange = 2
    PrintCollateCopies = 16
    PrintCurrentPage = 64
    PrintPageRange = 4
    PrintSelection = 2
    PrintShowPageSize = 8
    PrintToFile = 1
    Selection = 1


