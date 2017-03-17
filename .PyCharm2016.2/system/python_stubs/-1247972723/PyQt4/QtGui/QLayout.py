# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QLayoutItem import QLayoutItem

class QLayout(__PyQt4_QtCore.QObject, QLayoutItem):
    """
    QLayout(QWidget)
    QLayout()
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ QLayout.activate() -> bool """
        return False

    def addChildLayout(self, QLayout): # real signature unknown; restored from __doc__
        """ QLayout.addChildLayout(QLayout) """
        pass

    def addChildWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QLayout.addChildWidget(QWidget) """
        pass

    def addItem(self, QLayoutItem): # real signature unknown; restored from __doc__
        """ QLayout.addItem(QLayoutItem) """
        pass

    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QLayout.addWidget(QWidget) """
        pass

    def alignmentRect(self, QRect): # real signature unknown; restored from __doc__
        """ QLayout.alignmentRect(QRect) -> QRect """
        pass

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ QLayout.childEvent(QChildEvent) """
        pass

    def closestAcceptableSize(self, QWidget, QSize): # real signature unknown; restored from __doc__
        """ QLayout.closestAcceptableSize(QWidget, QSize) -> QSize """
        pass

    def contentsMargins(self): # real signature unknown; restored from __doc__
        """ QLayout.contentsMargins() -> QMargins """
        pass

    def contentsRect(self): # real signature unknown; restored from __doc__
        """ QLayout.contentsRect() -> QRect """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ QLayout.count() -> int """
        return 0

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ QLayout.expandingDirections() -> Qt.Orientations """
        pass

    def geometry(self): # real signature unknown; restored from __doc__
        """ QLayout.geometry() -> QRect """
        pass

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ QLayout.getContentsMargins() -> (int, int, int, int) """
        pass

    def indexOf(self, QWidget): # real signature unknown; restored from __doc__
        """ QLayout.indexOf(QWidget) -> int """
        return 0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ QLayout.invalidate() """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QLayout.isEmpty() -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ QLayout.isEnabled() -> bool """
        return False

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ QLayout.itemAt(int) -> QLayoutItem """
        return QLayoutItem

    def layout(self): # real signature unknown; restored from __doc__
        """ QLayout.layout() -> QLayout """
        return QLayout

    def margin(self): # real signature unknown; restored from __doc__
        """ QLayout.margin() -> int """
        return 0

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ QLayout.maximumSize() -> QSize """
        pass

    def menuBar(self): # real signature unknown; restored from __doc__
        """ QLayout.menuBar() -> QWidget """
        return QWidget

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ QLayout.minimumSize() -> QSize """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ QLayout.parentWidget() -> QWidget """
        return QWidget

    def removeItem(self, QLayoutItem): # real signature unknown; restored from __doc__
        """ QLayout.removeItem(QLayoutItem) """
        pass

    def removeWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QLayout.removeWidget(QWidget) """
        pass

    def setAlignment(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLayout.setAlignment(QWidget, Qt.Alignment) -> bool
        QLayout.setAlignment(QLayout, Qt.Alignment) -> bool
        QLayout.setAlignment(Qt.Alignment)
        """
        return False

    def setContentsMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLayout.setContentsMargins(int, int, int, int)
        QLayout.setContentsMargins(QMargins)
        """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QLayout.setEnabled(bool) """
        pass

    def setGeometry(self, QRect): # real signature unknown; restored from __doc__
        """ QLayout.setGeometry(QRect) """
        pass

    def setMargin(self, p_int): # real signature unknown; restored from __doc__
        """ QLayout.setMargin(int) """
        pass

    def setMenuBar(self, QWidget): # real signature unknown; restored from __doc__
        """ QLayout.setMenuBar(QWidget) """
        pass

    def setSizeConstraint(self, QLayout_SizeConstraint): # real signature unknown; restored from __doc__
        """ QLayout.setSizeConstraint(QLayout.SizeConstraint) """
        pass

    def setSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ QLayout.setSpacing(int) """
        pass

    def sizeConstraint(self): # real signature unknown; restored from __doc__
        """ QLayout.sizeConstraint() -> QLayout.SizeConstraint """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ QLayout.spacing() -> int """
        return 0

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ QLayout.takeAt(int) -> QLayoutItem """
        return QLayoutItem

    def totalHeightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QLayout.totalHeightForWidth(int) -> int """
        return 0

    def totalMaximumSize(self): # real signature unknown; restored from __doc__
        """ QLayout.totalMaximumSize() -> QSize """
        pass

    def totalMinimumSize(self): # real signature unknown; restored from __doc__
        """ QLayout.totalMinimumSize() -> QSize """
        pass

    def totalSizeHint(self): # real signature unknown; restored from __doc__
        """ QLayout.totalSizeHint() -> QSize """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ QLayout.update() """
        pass

    def widgetEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QLayout.widgetEvent(QEvent) """
        pass

    def __init__(self, QWidget=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    SetDefaultConstraint = 0
    SetFixedSize = 3
    SetMaximumSize = 4
    SetMinAndMaxSize = 5
    SetMinimumSize = 2
    SetNoConstraint = 1


