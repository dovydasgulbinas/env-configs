# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QTextOption(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QTextOption()
    QTextOption(Qt.Alignment)
    QTextOption(QTextOption)
    """
    def alignment(self): # real signature unknown; restored from __doc__
        """ QTextOption.alignment() -> Qt.Alignment """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ QTextOption.flags() -> QTextOption.Flags """
        pass

    def setAlignment(self, Qt_Alignment): # real signature unknown; restored from __doc__
        """ QTextOption.setAlignment(Qt.Alignment) """
        pass

    def setFlags(self, QTextOption_Flags): # real signature unknown; restored from __doc__
        """ QTextOption.setFlags(QTextOption.Flags) """
        pass

    def setTabArray(self, list_of_float): # real signature unknown; restored from __doc__
        """ QTextOption.setTabArray(list-of-float) """
        pass

    def setTabs(self, list_of_QTextOption_Tab): # real signature unknown; restored from __doc__
        """ QTextOption.setTabs(list-of-QTextOption.Tab) """
        pass

    def setTabStop(self, p_float): # real signature unknown; restored from __doc__
        """ QTextOption.setTabStop(float) """
        pass

    def setTextDirection(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ QTextOption.setTextDirection(Qt.LayoutDirection) """
        pass

    def setUseDesignMetrics(self, bool): # real signature unknown; restored from __doc__
        """ QTextOption.setUseDesignMetrics(bool) """
        pass

    def setWrapMode(self, QTextOption_WrapMode): # real signature unknown; restored from __doc__
        """ QTextOption.setWrapMode(QTextOption.WrapMode) """
        pass

    def tabArray(self): # real signature unknown; restored from __doc__
        """ QTextOption.tabArray() -> list-of-float """
        pass

    def tabs(self): # real signature unknown; restored from __doc__
        """ QTextOption.tabs() -> list-of-QTextOption.Tab """
        pass

    def tabStop(self): # real signature unknown; restored from __doc__
        """ QTextOption.tabStop() -> float """
        return 0.0

    def textDirection(self): # real signature unknown; restored from __doc__
        """ QTextOption.textDirection() -> Qt.LayoutDirection """
        pass

    def useDesignMetrics(self): # real signature unknown; restored from __doc__
        """ QTextOption.useDesignMetrics() -> bool """
        return False

    def wrapMode(self): # real signature unknown; restored from __doc__
        """ QTextOption.wrapMode() -> QTextOption.WrapMode """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AddSpaceForLineAndParagraphSeparators = 4
    CenterTab = 2
    DelimiterTab = 3
    IncludeTrailingSpaces = -2147483648
    LeftTab = 0
    ManualWrap = 2
    NoWrap = 0
    RightTab = 1
    ShowLineAndParagraphSeparators = 2
    ShowTabsAndSpaces = 1
    SuppressColors = 8
    WordWrap = 1
    WrapAnywhere = 3
    WrapAtWordBoundaryOrAnywhere = 4


