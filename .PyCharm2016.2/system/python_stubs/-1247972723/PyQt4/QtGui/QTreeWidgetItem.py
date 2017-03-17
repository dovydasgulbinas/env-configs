# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QTreeWidgetItem(): # skipped bases: <type 'sip.wrapper'>
    """
    QTreeWidgetItem(int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QStringList, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidget, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidget, QStringList, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidget, QTreeWidgetItem, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidgetItem, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidgetItem, QStringList, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidgetItem, QTreeWidgetItem, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidgetItem)
    """
    def addChild(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.addChild(QTreeWidgetItem) """
        pass

    def addChildren(self, list_of_QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.addChildren(list-of-QTreeWidgetItem) """
        pass

    def background(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.background(int) -> QBrush """
        return QBrush

    def backgroundColor(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.backgroundColor(int) -> QColor """
        return QColor

    def checkState(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.checkState(int) -> Qt.CheckState """
        pass

    def child(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.child(int) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def childCount(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.childCount() -> int """
        return 0

    def childIndicatorPolicy(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.childIndicatorPolicy() -> QTreeWidgetItem.ChildIndicatorPolicy """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.clone() -> QTreeWidgetItem """
        return QTreeWidgetItem

    def columnCount(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.columnCount() -> int """
        return 0

    def data(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.data(int, int) -> QVariant """
        pass

    def emitDataChanged(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.emitDataChanged() """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.flags() -> Qt.ItemFlags """
        pass

    def font(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.font(int) -> QFont """
        return QFont

    def foreground(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.foreground(int) -> QBrush """
        return QBrush

    def icon(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.icon(int) -> QIcon """
        return QIcon

    def indexOfChild(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.indexOfChild(QTreeWidgetItem) -> int """
        return 0

    def insertChild(self, p_int, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.insertChild(int, QTreeWidgetItem) """
        pass

    def insertChildren(self, p_int, list_of_QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.insertChildren(int, list-of-QTreeWidgetItem) """
        pass

    def isDisabled(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.isDisabled() -> bool """
        return False

    def isExpanded(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.isExpanded() -> bool """
        return False

    def isFirstColumnSpanned(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.isFirstColumnSpanned() -> bool """
        return False

    def isHidden(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.isHidden() -> bool """
        return False

    def isSelected(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.isSelected() -> bool """
        return False

    def parent(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.parent() -> QTreeWidgetItem """
        return QTreeWidgetItem

    def read(self, QDataStream): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.read(QDataStream) """
        pass

    def removeChild(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.removeChild(QTreeWidgetItem) """
        pass

    def setBackground(self, p_int, QBrush): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setBackground(int, QBrush) """
        pass

    def setBackgroundColor(self, p_int, QColor): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setBackgroundColor(int, QColor) """
        pass

    def setCheckState(self, p_int, Qt_CheckState): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setCheckState(int, Qt.CheckState) """
        pass

    def setChildIndicatorPolicy(self, QTreeWidgetItem_ChildIndicatorPolicy): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setChildIndicatorPolicy(QTreeWidgetItem.ChildIndicatorPolicy) """
        pass

    def setData(self, p_int, p_int_1, QVariant): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setData(int, int, QVariant) """
        pass

    def setDisabled(self, bool): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setDisabled(bool) """
        pass

    def setExpanded(self, bool): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setExpanded(bool) """
        pass

    def setFirstColumnSpanned(self, bool): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setFirstColumnSpanned(bool) """
        pass

    def setFlags(self, Qt_ItemFlags): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setFlags(Qt.ItemFlags) """
        pass

    def setFont(self, p_int, QFont): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setFont(int, QFont) """
        pass

    def setForeground(self, p_int, QBrush): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setForeground(int, QBrush) """
        pass

    def setHidden(self, bool): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setHidden(bool) """
        pass

    def setIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setIcon(int, QIcon) """
        pass

    def setSelected(self, bool): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setSelected(bool) """
        pass

    def setSizeHint(self, p_int, QSize): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setSizeHint(int, QSize) """
        pass

    def setStatusTip(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setStatusTip(int, QString) """
        pass

    def setText(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setText(int, QString) """
        pass

    def setTextAlignment(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setTextAlignment(int, int) """
        pass

    def setTextColor(self, p_int, QColor): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setTextColor(int, QColor) """
        pass

    def setToolTip(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setToolTip(int, QString) """
        pass

    def setWhatsThis(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setWhatsThis(int, QString) """
        pass

    def sizeHint(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.sizeHint(int) -> QSize """
        pass

    def sortChildren(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.sortChildren(int, Qt.SortOrder) """
        pass

    def statusTip(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.statusTip(int) -> QString """
        pass

    def takeChild(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.takeChild(int) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def takeChildren(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.takeChildren() -> list-of-QTreeWidgetItem """
        pass

    def text(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.text(int) -> QString """
        pass

    def textAlignment(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.textAlignment(int) -> int """
        return 0

    def textColor(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.textColor(int) -> QColor """
        return QColor

    def toolTip(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.toolTip(int) -> QString """
        pass

    def treeWidget(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.treeWidget() -> QTreeWidget """
        return QTreeWidget

    def type(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.type() -> int """
        return 0

    def whatsThis(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.whatsThis(int) -> QString """
        pass

    def write(self, QDataStream): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.write(QDataStream) """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DontShowIndicator = 1
    DontShowIndicatorWhenChildless = 2
    ShowIndicator = 0
    Type = 0
    UserType = 1000


