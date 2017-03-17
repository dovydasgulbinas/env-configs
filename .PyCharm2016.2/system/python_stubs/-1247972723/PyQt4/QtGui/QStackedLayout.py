# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QLayout import QLayout

class QStackedLayout(QLayout):
    """
    QStackedLayout()
    QStackedLayout(QWidget)
    QStackedLayout(QLayout)
    """
    def addItem(self, QLayoutItem): # real signature unknown; restored from __doc__
        """ QStackedLayout.addItem(QLayoutItem) """
        pass

    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QStackedLayout.addWidget(QWidget) -> int """
        return 0

    def count(self): # real signature unknown; restored from __doc__
        """ QStackedLayout.count() -> int """
        return 0

    def currentChanged(self, *args, **kwargs): # real signature unknown
        """ QStackedLayout.currentChanged[int] [signal] """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ QStackedLayout.currentIndex() -> int """
        return 0

    def currentWidget(self): # real signature unknown; restored from __doc__
        """ QStackedLayout.currentWidget() -> QWidget """
        return QWidget

    def insertWidget(self, p_int, QWidget): # real signature unknown; restored from __doc__
        """ QStackedLayout.insertWidget(int, QWidget) -> int """
        return 0

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ QStackedLayout.itemAt(int) -> QLayoutItem """
        return QLayoutItem

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ QStackedLayout.minimumSize() -> QSize """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QStackedLayout.setCurrentIndex(int) """
        pass

    def setCurrentWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QStackedLayout.setCurrentWidget(QWidget) """
        pass

    def setGeometry(self, QRect): # real signature unknown; restored from __doc__
        """ QStackedLayout.setGeometry(QRect) """
        pass

    def setStackingMode(self, QStackedLayout_StackingMode): # real signature unknown; restored from __doc__
        """ QStackedLayout.setStackingMode(QStackedLayout.StackingMode) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QStackedLayout.sizeHint() -> QSize """
        pass

    def stackingMode(self): # real signature unknown; restored from __doc__
        """ QStackedLayout.stackingMode() -> QStackedLayout.StackingMode """
        pass

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ QStackedLayout.takeAt(int) -> QLayoutItem """
        return QLayoutItem

    def widget(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStackedLayout.widget(int) -> QWidget
        QStackedLayout.widget() -> QWidget
        """
        return QWidget

    def widgetRemoved(self, *args, **kwargs): # real signature unknown
        """ QStackedLayout.widgetRemoved[int] [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    StackAll = 1
    StackOne = 0


