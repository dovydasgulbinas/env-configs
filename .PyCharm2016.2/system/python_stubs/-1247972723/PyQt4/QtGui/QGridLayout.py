# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QLayout import QLayout

class QGridLayout(QLayout):
    """
    QGridLayout(QWidget)
    QGridLayout()
    """
    def addItem(self, QLayoutItem, p_int=None, p_int_1=None, int_rowSpan=1, int_columnSpan=1, Qt_Alignment_alignment=0): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGridLayout.addItem(QLayoutItem, int, int, int rowSpan=1, int columnSpan=1, Qt.Alignment alignment=0)
        QGridLayout.addItem(QLayoutItem)
        """
        pass

    def addLayout(self, QLayout, p_int, p_int_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGridLayout.addLayout(QLayout, int, int, Qt.Alignment alignment=0)
        QGridLayout.addLayout(QLayout, int, int, int, int, Qt.Alignment alignment=0)
        """
        pass

    def addWidget(self, QWidget, p_int=None, p_int_1=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGridLayout.addWidget(QWidget)
        QGridLayout.addWidget(QWidget, int, int, Qt.Alignment alignment=0)
        QGridLayout.addWidget(QWidget, int, int, int, int, Qt.Alignment alignment=0)
        """
        pass

    def cellRect(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QGridLayout.cellRect(int, int) -> QRect """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ QGridLayout.columnCount() -> int """
        return 0

    def columnMinimumWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QGridLayout.columnMinimumWidth(int) -> int """
        return 0

    def columnStretch(self, p_int): # real signature unknown; restored from __doc__
        """ QGridLayout.columnStretch(int) -> int """
        return 0

    def count(self): # real signature unknown; restored from __doc__
        """ QGridLayout.count() -> int """
        return 0

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ QGridLayout.expandingDirections() -> Qt.Orientations """
        pass

    def getItemPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QGridLayout.getItemPosition(int) -> (int, int, int, int) """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ QGridLayout.hasHeightForWidth() -> bool """
        return False

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QGridLayout.heightForWidth(int) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ QGridLayout.horizontalSpacing() -> int """
        return 0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ QGridLayout.invalidate() """
        pass

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ QGridLayout.itemAt(int) -> QLayoutItem """
        return QLayoutItem

    def itemAtPosition(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QGridLayout.itemAtPosition(int, int) -> QLayoutItem """
        return QLayoutItem

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ QGridLayout.maximumSize() -> QSize """
        pass

    def minimumHeightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QGridLayout.minimumHeightForWidth(int) -> int """
        return 0

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ QGridLayout.minimumSize() -> QSize """
        pass

    def originCorner(self): # real signature unknown; restored from __doc__
        """ QGridLayout.originCorner() -> Qt.Corner """
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ QGridLayout.rowCount() -> int """
        return 0

    def rowMinimumHeight(self, p_int): # real signature unknown; restored from __doc__
        """ QGridLayout.rowMinimumHeight(int) -> int """
        return 0

    def rowStretch(self, p_int): # real signature unknown; restored from __doc__
        """ QGridLayout.rowStretch(int) -> int """
        return 0

    def setColumnMinimumWidth(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QGridLayout.setColumnMinimumWidth(int, int) """
        pass

    def setColumnStretch(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QGridLayout.setColumnStretch(int, int) """
        pass

    def setDefaultPositioning(self, p_int, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QGridLayout.setDefaultPositioning(int, Qt.Orientation) """
        pass

    def setGeometry(self, QRect): # real signature unknown; restored from __doc__
        """ QGridLayout.setGeometry(QRect) """
        pass

    def setHorizontalSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ QGridLayout.setHorizontalSpacing(int) """
        pass

    def setOriginCorner(self, Qt_Corner): # real signature unknown; restored from __doc__
        """ QGridLayout.setOriginCorner(Qt.Corner) """
        pass

    def setRowMinimumHeight(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QGridLayout.setRowMinimumHeight(int, int) """
        pass

    def setRowStretch(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QGridLayout.setRowStretch(int, int) """
        pass

    def setSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ QGridLayout.setSpacing(int) """
        pass

    def setVerticalSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ QGridLayout.setVerticalSpacing(int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QGridLayout.sizeHint() -> QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ QGridLayout.spacing() -> int """
        return 0

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ QGridLayout.takeAt(int) -> QLayoutItem """
        return QLayoutItem

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ QGridLayout.verticalSpacing() -> int """
        return 0

    def __init__(self, QWidget=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass


