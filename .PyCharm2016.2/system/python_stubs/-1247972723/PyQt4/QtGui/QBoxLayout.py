# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QLayout import QLayout

class QBoxLayout(QLayout):
    """ QBoxLayout(QBoxLayout.Direction, QWidget parent=None) """
    def addItem(self, QLayoutItem): # real signature unknown; restored from __doc__
        """ QBoxLayout.addItem(QLayoutItem) """
        pass

    def addLayout(self, QLayout, int_stretch=0): # real signature unknown; restored from __doc__
        """ QBoxLayout.addLayout(QLayout, int stretch=0) """
        pass

    def addSpacerItem(self, QSpacerItem): # real signature unknown; restored from __doc__
        """ QBoxLayout.addSpacerItem(QSpacerItem) """
        pass

    def addSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ QBoxLayout.addSpacing(int) """
        pass

    def addStretch(self, int_stretch=0): # real signature unknown; restored from __doc__
        """ QBoxLayout.addStretch(int stretch=0) """
        pass

    def addStrut(self, p_int): # real signature unknown; restored from __doc__
        """ QBoxLayout.addStrut(int) """
        pass

    def addWidget(self, QWidget, int_stretch=0, Qt_Alignment_alignment=0): # real signature unknown; restored from __doc__
        """ QBoxLayout.addWidget(QWidget, int stretch=0, Qt.Alignment alignment=0) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ QBoxLayout.count() -> int """
        return 0

    def direction(self): # real signature unknown; restored from __doc__
        """ QBoxLayout.direction() -> QBoxLayout.Direction """
        pass

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ QBoxLayout.expandingDirections() -> Qt.Orientations """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ QBoxLayout.hasHeightForWidth() -> bool """
        return False

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QBoxLayout.heightForWidth(int) -> int """
        return 0

    def insertItem(self, p_int, QLayoutItem): # real signature unknown; restored from __doc__
        """ QBoxLayout.insertItem(int, QLayoutItem) """
        pass

    def insertLayout(self, p_int, QLayout, int_stretch=0): # real signature unknown; restored from __doc__
        """ QBoxLayout.insertLayout(int, QLayout, int stretch=0) """
        pass

    def insertSpacerItem(self, p_int, QSpacerItem): # real signature unknown; restored from __doc__
        """ QBoxLayout.insertSpacerItem(int, QSpacerItem) """
        pass

    def insertSpacing(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QBoxLayout.insertSpacing(int, int) """
        pass

    def insertStretch(self, p_int, int_stretch=0): # real signature unknown; restored from __doc__
        """ QBoxLayout.insertStretch(int, int stretch=0) """
        pass

    def insertWidget(self, p_int, QWidget, int_stretch=0, Qt_Alignment_alignment=0): # real signature unknown; restored from __doc__
        """ QBoxLayout.insertWidget(int, QWidget, int stretch=0, Qt.Alignment alignment=0) """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ QBoxLayout.invalidate() """
        pass

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ QBoxLayout.itemAt(int) -> QLayoutItem """
        return QLayoutItem

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ QBoxLayout.maximumSize() -> QSize """
        pass

    def minimumHeightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QBoxLayout.minimumHeightForWidth(int) -> int """
        return 0

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ QBoxLayout.minimumSize() -> QSize """
        pass

    def setDirection(self, QBoxLayout_Direction): # real signature unknown; restored from __doc__
        """ QBoxLayout.setDirection(QBoxLayout.Direction) """
        pass

    def setGeometry(self, QRect): # real signature unknown; restored from __doc__
        """ QBoxLayout.setGeometry(QRect) """
        pass

    def setSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ QBoxLayout.setSpacing(int) """
        pass

    def setStretch(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QBoxLayout.setStretch(int, int) """
        pass

    def setStretchFactor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QBoxLayout.setStretchFactor(QWidget, int) -> bool
        QBoxLayout.setStretchFactor(QLayout, int) -> bool
        """
        return False

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QBoxLayout.sizeHint() -> QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ QBoxLayout.spacing() -> int """
        return 0

    def stretch(self, p_int): # real signature unknown; restored from __doc__
        """ QBoxLayout.stretch(int) -> int """
        return 0

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ QBoxLayout.takeAt(int) -> QLayoutItem """
        return QLayoutItem

    def __init__(self, QBoxLayout_Direction, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    BottomToTop = 3
    Down = 2
    LeftToRight = 0
    RightToLeft = 1
    TopToBottom = 2
    Up = 3


