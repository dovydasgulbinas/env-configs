# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractScrollArea import QAbstractScrollArea

class QScrollArea(QAbstractScrollArea):
    """ QScrollArea(QWidget parent=None) """
    def alignment(self): # real signature unknown; restored from __doc__
        """ QScrollArea.alignment() -> Qt.Alignment """
        pass

    def ensureVisible(self, p_int, p_int_1, int_xMargin=50, int_yMargin=50): # real signature unknown; restored from __doc__
        """ QScrollArea.ensureVisible(int, int, int xMargin=50, int yMargin=50) """
        pass

    def ensureWidgetVisible(self, QWidget, int_xMargin=50, int_yMargin=50): # real signature unknown; restored from __doc__
        """ QScrollArea.ensureWidgetVisible(QWidget, int xMargin=50, int yMargin=50) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QScrollArea.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QScrollArea.eventFilter(QObject, QEvent) -> bool """
        return False

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QScrollArea.focusNextPrevChild(bool) -> bool """
        return False

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QScrollArea.resizeEvent(QResizeEvent) """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QScrollArea.scrollContentsBy(int, int) """
        pass

    def setAlignment(self, Qt_Alignment): # real signature unknown; restored from __doc__
        """ QScrollArea.setAlignment(Qt.Alignment) """
        pass

    def setWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QScrollArea.setWidget(QWidget) """
        pass

    def setWidgetResizable(self, bool): # real signature unknown; restored from __doc__
        """ QScrollArea.setWidgetResizable(bool) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QScrollArea.sizeHint() -> QSize """
        pass

    def takeWidget(self): # real signature unknown; restored from __doc__
        """ QScrollArea.takeWidget() -> QWidget """
        return QWidget

    def widget(self): # real signature unknown; restored from __doc__
        """ QScrollArea.widget() -> QWidget """
        return QWidget

    def widgetResizable(self): # real signature unknown; restored from __doc__
        """ QScrollArea.widgetResizable() -> bool """
        return False

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


