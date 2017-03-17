# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QComboBox(QWidget):
    """ QComboBox(QWidget parent=None) """
    def activated(self, *args, **kwargs): # real signature unknown
        """
        QComboBox.activated[int] [signal]
        QComboBox.activated[QString] [signal]
        """
        pass

    def addItem(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QComboBox.addItem(QString, QVariant userData=QVariant())
        QComboBox.addItem(QIcon, QString, QVariant userData=QVariant())
        """
        pass

    def addItems(self, QStringList): # real signature unknown; restored from __doc__
        """ QComboBox.addItems(QStringList) """
        pass

    def autoCompletion(self): # real signature unknown; restored from __doc__
        """ QComboBox.autoCompletion() -> bool """
        return False

    def autoCompletionCaseSensitivity(self): # real signature unknown; restored from __doc__
        """ QComboBox.autoCompletionCaseSensitivity() -> Qt.CaseSensitivity """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QComboBox.changeEvent(QEvent) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QComboBox.clear() """
        pass

    def clearEditText(self): # real signature unknown; restored from __doc__
        """ QComboBox.clearEditText() """
        pass

    def completer(self): # real signature unknown; restored from __doc__
        """ QComboBox.completer() -> QCompleter """
        return QCompleter

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ QComboBox.contextMenuEvent(QContextMenuEvent) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ QComboBox.count() -> int """
        return 0

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ QComboBox.currentIndex() -> int """
        return 0

    def currentIndexChanged(self, *args, **kwargs): # real signature unknown
        """
        QComboBox.currentIndexChanged[int] [signal]
        QComboBox.currentIndexChanged[QString] [signal]
        """
        pass

    def currentText(self): # real signature unknown; restored from __doc__
        """ QComboBox.currentText() -> QString """
        pass

    def duplicatesEnabled(self): # real signature unknown; restored from __doc__
        """ QComboBox.duplicatesEnabled() -> bool """
        return False

    def editTextChanged(self, *args, **kwargs): # real signature unknown
        """ QComboBox.editTextChanged[QString] [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QComboBox.event(QEvent) -> bool """
        return False

    def findData(self, QVariant, int_role=None, Qt_MatchFlags_flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QComboBox.findData(QVariant, int role=Qt.UserRole, Qt.MatchFlags flags=Qt.MatchExactly|Qt.MatchCaseSensitive) -> int """
        pass

    def findText(self, QString, Qt_MatchFlags_flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QComboBox.findText(QString, Qt.MatchFlags flags=Qt.MatchExactly|Qt.MatchCaseSensitive) -> int """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QComboBox.focusInEvent(QFocusEvent) """
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QComboBox.focusOutEvent(QFocusEvent) """
        pass

    def hasFrame(self): # real signature unknown; restored from __doc__
        """ QComboBox.hasFrame() -> bool """
        return False

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ QComboBox.hideEvent(QHideEvent) """
        pass

    def hidePopup(self): # real signature unknown; restored from __doc__
        """ QComboBox.hidePopup() """
        pass

    def highlighted(self, *args, **kwargs): # real signature unknown
        """
        QComboBox.highlighted[int] [signal]
        QComboBox.highlighted[QString] [signal]
        """
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ QComboBox.iconSize() -> QSize """
        pass

    def initStyleOption(self, QStyleOptionComboBox): # real signature unknown; restored from __doc__
        """ QComboBox.initStyleOption(QStyleOptionComboBox) """
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QComboBox.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QComboBox.inputMethodQuery(Qt.InputMethodQuery) -> QVariant """
        pass

    def insertItem(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QComboBox.insertItem(int, QString, QVariant userData=QVariant())
        QComboBox.insertItem(int, QIcon, QString, QVariant userData=QVariant())
        """
        pass

    def insertItems(self, p_int, QStringList): # real signature unknown; restored from __doc__
        """ QComboBox.insertItems(int, QStringList) """
        pass

    def insertPolicy(self): # real signature unknown; restored from __doc__
        """ QComboBox.insertPolicy() -> QComboBox.InsertPolicy """
        pass

    def insertSeparator(self, p_int): # real signature unknown; restored from __doc__
        """ QComboBox.insertSeparator(int) """
        pass

    def isEditable(self): # real signature unknown; restored from __doc__
        """ QComboBox.isEditable() -> bool """
        return False

    def itemData(self, p_int, int_role=None): # real signature unknown; restored from __doc__
        """ QComboBox.itemData(int, int role=Qt.UserRole) -> QVariant """
        pass

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ QComboBox.itemDelegate() -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def itemIcon(self, p_int): # real signature unknown; restored from __doc__
        """ QComboBox.itemIcon(int) -> QIcon """
        return QIcon

    def itemText(self, p_int): # real signature unknown; restored from __doc__
        """ QComboBox.itemText(int) -> QString """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QComboBox.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QComboBox.keyReleaseEvent(QKeyEvent) """
        pass

    def lineEdit(self): # real signature unknown; restored from __doc__
        """ QComboBox.lineEdit() -> QLineEdit """
        return QLineEdit

    def maxCount(self): # real signature unknown; restored from __doc__
        """ QComboBox.maxCount() -> int """
        return 0

    def maxVisibleItems(self): # real signature unknown; restored from __doc__
        """ QComboBox.maxVisibleItems() -> int """
        return 0

    def minimumContentsLength(self): # real signature unknown; restored from __doc__
        """ QComboBox.minimumContentsLength() -> int """
        return 0

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QComboBox.minimumSizeHint() -> QSize """
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ QComboBox.model() -> QAbstractItemModel """
        pass

    def modelColumn(self): # real signature unknown; restored from __doc__
        """ QComboBox.modelColumn() -> int """
        return 0

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QComboBox.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QComboBox.mouseReleaseEvent(QMouseEvent) """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QComboBox.paintEvent(QPaintEvent) """
        pass

    def removeItem(self, p_int): # real signature unknown; restored from __doc__
        """ QComboBox.removeItem(int) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QComboBox.resizeEvent(QResizeEvent) """
        pass

    def rootModelIndex(self): # real signature unknown; restored from __doc__
        """ QComboBox.rootModelIndex() -> QModelIndex """
        pass

    def setAutoCompletion(self, bool): # real signature unknown; restored from __doc__
        """ QComboBox.setAutoCompletion(bool) """
        pass

    def setAutoCompletionCaseSensitivity(self, Qt_CaseSensitivity): # real signature unknown; restored from __doc__
        """ QComboBox.setAutoCompletionCaseSensitivity(Qt.CaseSensitivity) """
        pass

    def setCompleter(self, QCompleter): # real signature unknown; restored from __doc__
        """ QComboBox.setCompleter(QCompleter) """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QComboBox.setCurrentIndex(int) """
        pass

    def setDuplicatesEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QComboBox.setDuplicatesEnabled(bool) """
        pass

    def setEditable(self, bool): # real signature unknown; restored from __doc__
        """ QComboBox.setEditable(bool) """
        pass

    def setEditText(self, QString): # real signature unknown; restored from __doc__
        """ QComboBox.setEditText(QString) """
        pass

    def setFrame(self, bool): # real signature unknown; restored from __doc__
        """ QComboBox.setFrame(bool) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ QComboBox.setIconSize(QSize) """
        pass

    def setInsertPolicy(self, QComboBox_InsertPolicy): # real signature unknown; restored from __doc__
        """ QComboBox.setInsertPolicy(QComboBox.InsertPolicy) """
        pass

    def setItemData(self, p_int, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QComboBox.setItemData(int, QVariant, int role=Qt.UserRole) """
        pass

    def setItemDelegate(self, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ QComboBox.setItemDelegate(QAbstractItemDelegate) """
        pass

    def setItemIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ QComboBox.setItemIcon(int, QIcon) """
        pass

    def setItemText(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QComboBox.setItemText(int, QString) """
        pass

    def setLineEdit(self, QLineEdit): # real signature unknown; restored from __doc__
        """ QComboBox.setLineEdit(QLineEdit) """
        pass

    def setMaxCount(self, p_int): # real signature unknown; restored from __doc__
        """ QComboBox.setMaxCount(int) """
        pass

    def setMaxVisibleItems(self, p_int): # real signature unknown; restored from __doc__
        """ QComboBox.setMaxVisibleItems(int) """
        pass

    def setMinimumContentsLength(self, p_int): # real signature unknown; restored from __doc__
        """ QComboBox.setMinimumContentsLength(int) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ QComboBox.setModel(QAbstractItemModel) """
        pass

    def setModelColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QComboBox.setModelColumn(int) """
        pass

    def setRootModelIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QComboBox.setRootModelIndex(QModelIndex) """
        pass

    def setSizeAdjustPolicy(self, QComboBox_SizeAdjustPolicy): # real signature unknown; restored from __doc__
        """ QComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy) """
        pass

    def setValidator(self, QValidator): # real signature unknown; restored from __doc__
        """ QComboBox.setValidator(QValidator) """
        pass

    def setView(self, QAbstractItemView): # real signature unknown; restored from __doc__
        """ QComboBox.setView(QAbstractItemView) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QComboBox.showEvent(QShowEvent) """
        pass

    def showPopup(self): # real signature unknown; restored from __doc__
        """ QComboBox.showPopup() """
        pass

    def sizeAdjustPolicy(self): # real signature unknown; restored from __doc__
        """ QComboBox.sizeAdjustPolicy() -> QComboBox.SizeAdjustPolicy """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QComboBox.sizeHint() -> QSize """
        pass

    def validator(self): # real signature unknown; restored from __doc__
        """ QComboBox.validator() -> QValidator """
        return QValidator

    def view(self): # real signature unknown; restored from __doc__
        """ QComboBox.view() -> QAbstractItemView """
        return QAbstractItemView

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ QComboBox.wheelEvent(QWheelEvent) """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    AdjustToContents = 0
    AdjustToContentsOnFirstShow = 1
    AdjustToMinimumContentsLength = 2
    AdjustToMinimumContentsLengthWithIcon = 3
    InsertAfterCurrent = 4
    InsertAlphabetically = 6
    InsertAtBottom = 3
    InsertAtCurrent = 2
    InsertAtTop = 1
    InsertBeforeCurrent = 5
    NoInsert = 0


