# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QInputContext(__PyQt4_QtCore.QObject):
    """ QInputContext(QObject parent=None) """
    def actions(self): # real signature unknown; restored from __doc__
        """ QInputContext.actions() -> list-of-QAction """
        pass

    def filterEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QInputContext.filterEvent(QEvent) -> bool """
        return False

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ QInputContext.focusWidget() -> QWidget """
        return QWidget

    def font(self): # real signature unknown; restored from __doc__
        """ QInputContext.font() -> QFont """
        return QFont

    def identifierName(self): # real signature unknown; restored from __doc__
        """ QInputContext.identifierName() -> QString """
        pass

    def isComposing(self): # real signature unknown; restored from __doc__
        """ QInputContext.isComposing() -> bool """
        return False

    def language(self): # real signature unknown; restored from __doc__
        """ QInputContext.language() -> QString """
        pass

    def mouseHandler(self, p_int, QMouseEvent): # real signature unknown; restored from __doc__
        """ QInputContext.mouseHandler(int, QMouseEvent) """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QInputContext.reset() """
        pass

    def sendEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QInputContext.sendEvent(QInputMethodEvent) """
        pass

    def setFocusWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QInputContext.setFocusWidget(QWidget) """
        pass

    def standardFormat(self, QInputContext_StandardFormat): # real signature unknown; restored from __doc__
        """ QInputContext.standardFormat(QInputContext.StandardFormat) -> QTextFormat """
        return QTextFormat

    def update(self): # real signature unknown; restored from __doc__
        """ QInputContext.update() """
        pass

    def widgetDestroyed(self, QWidget): # real signature unknown; restored from __doc__
        """ QInputContext.widgetDestroyed(QWidget) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    PreeditFormat = 0
    SelectionFormat = 1


