# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QLayout import QLayout

class QFormLayout(QLayout):
    """ QFormLayout(QWidget parent=None) """
    def addItem(self, QLayoutItem): # real signature unknown; restored from __doc__
        """ QFormLayout.addItem(QLayoutItem) """
        pass

    def addRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFormLayout.addRow(QWidget, QWidget)
        QFormLayout.addRow(QWidget, QLayout)
        QFormLayout.addRow(QString, QWidget)
        QFormLayout.addRow(QString, QLayout)
        QFormLayout.addRow(QWidget)
        QFormLayout.addRow(QLayout)
        """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ QFormLayout.count() -> int """
        return 0

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ QFormLayout.expandingDirections() -> Qt.Orientations """
        pass

    def fieldGrowthPolicy(self): # real signature unknown; restored from __doc__
        """ QFormLayout.fieldGrowthPolicy() -> QFormLayout.FieldGrowthPolicy """
        pass

    def formAlignment(self): # real signature unknown; restored from __doc__
        """ QFormLayout.formAlignment() -> Qt.Alignment """
        pass

    def getItemPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QFormLayout.getItemPosition(int) -> (int, QFormLayout.ItemRole) """
        pass

    def getLayoutPosition(self, QLayout): # real signature unknown; restored from __doc__
        """ QFormLayout.getLayoutPosition(QLayout) -> (int, QFormLayout.ItemRole) """
        pass

    def getWidgetPosition(self, QWidget): # real signature unknown; restored from __doc__
        """ QFormLayout.getWidgetPosition(QWidget) -> (int, QFormLayout.ItemRole) """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ QFormLayout.hasHeightForWidth() -> bool """
        return False

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QFormLayout.heightForWidth(int) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ QFormLayout.horizontalSpacing() -> int """
        return 0

    def insertRow(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFormLayout.insertRow(int, QWidget, QWidget)
        QFormLayout.insertRow(int, QWidget, QLayout)
        QFormLayout.insertRow(int, QString, QWidget)
        QFormLayout.insertRow(int, QString, QLayout)
        QFormLayout.insertRow(int, QWidget)
        QFormLayout.insertRow(int, QLayout)
        """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ QFormLayout.invalidate() """
        pass

    def itemAt(self, p_int, QFormLayout_ItemRole=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFormLayout.itemAt(int, QFormLayout.ItemRole) -> QLayoutItem
        QFormLayout.itemAt(int) -> QLayoutItem
        """
        return QLayoutItem

    def labelAlignment(self): # real signature unknown; restored from __doc__
        """ QFormLayout.labelAlignment() -> Qt.Alignment """
        pass

    def labelForField(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFormLayout.labelForField(QWidget) -> QWidget
        QFormLayout.labelForField(QLayout) -> QWidget
        """
        return QWidget

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ QFormLayout.minimumSize() -> QSize """
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ QFormLayout.rowCount() -> int """
        return 0

    def rowWrapPolicy(self): # real signature unknown; restored from __doc__
        """ QFormLayout.rowWrapPolicy() -> QFormLayout.RowWrapPolicy """
        pass

    def setFieldGrowthPolicy(self, QFormLayout_FieldGrowthPolicy): # real signature unknown; restored from __doc__
        """ QFormLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy) """
        pass

    def setFormAlignment(self, Qt_Alignment): # real signature unknown; restored from __doc__
        """ QFormLayout.setFormAlignment(Qt.Alignment) """
        pass

    def setGeometry(self, QRect): # real signature unknown; restored from __doc__
        """ QFormLayout.setGeometry(QRect) """
        pass

    def setHorizontalSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ QFormLayout.setHorizontalSpacing(int) """
        pass

    def setItem(self, p_int, QFormLayout_ItemRole, QLayoutItem): # real signature unknown; restored from __doc__
        """ QFormLayout.setItem(int, QFormLayout.ItemRole, QLayoutItem) """
        pass

    def setLabelAlignment(self, Qt_Alignment): # real signature unknown; restored from __doc__
        """ QFormLayout.setLabelAlignment(Qt.Alignment) """
        pass

    def setLayout(self, p_int, QFormLayout_ItemRole, QLayout): # real signature unknown; restored from __doc__
        """ QFormLayout.setLayout(int, QFormLayout.ItemRole, QLayout) """
        pass

    def setRowWrapPolicy(self, QFormLayout_RowWrapPolicy): # real signature unknown; restored from __doc__
        """ QFormLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy) """
        pass

    def setSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ QFormLayout.setSpacing(int) """
        pass

    def setVerticalSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ QFormLayout.setVerticalSpacing(int) """
        pass

    def setWidget(self, p_int, QFormLayout_ItemRole, QWidget): # real signature unknown; restored from __doc__
        """ QFormLayout.setWidget(int, QFormLayout.ItemRole, QWidget) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QFormLayout.sizeHint() -> QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ QFormLayout.spacing() -> int """
        return 0

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ QFormLayout.takeAt(int) -> QLayoutItem """
        return QLayoutItem

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ QFormLayout.verticalSpacing() -> int """
        return 0

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    AllNonFixedFieldsGrow = 2
    DontWrapRows = 0
    ExpandingFieldsGrow = 1
    FieldRole = 1
    FieldsStayAtSizeHint = 0
    LabelRole = 0
    SpanningRole = 2
    WrapAllRows = 2
    WrapLongRows = 1


