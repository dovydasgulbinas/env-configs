# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QCompleter(__PyQt4_QtCore.QObject):
    """
    QCompleter(QObject parent=None)
    QCompleter(QAbstractItemModel, QObject parent=None)
    QCompleter(QStringList, QObject parent=None)
    """
    def activated(self, *args, **kwargs): # real signature unknown
        """
        QCompleter.activated[QString] [signal]
        QCompleter.activated[QModelIndex] [signal]
        """
        pass

    def caseSensitivity(self): # real signature unknown; restored from __doc__
        """ QCompleter.caseSensitivity() -> Qt.CaseSensitivity """
        pass

    def complete(self, QRect_rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QCompleter.complete(QRect rect=QRect()) """
        pass

    def completionColumn(self): # real signature unknown; restored from __doc__
        """ QCompleter.completionColumn() -> int """
        return 0

    def completionCount(self): # real signature unknown; restored from __doc__
        """ QCompleter.completionCount() -> int """
        return 0

    def completionMode(self): # real signature unknown; restored from __doc__
        """ QCompleter.completionMode() -> QCompleter.CompletionMode """
        pass

    def completionModel(self): # real signature unknown; restored from __doc__
        """ QCompleter.completionModel() -> QAbstractItemModel """
        pass

    def completionPrefix(self): # real signature unknown; restored from __doc__
        """ QCompleter.completionPrefix() -> QString """
        pass

    def completionRole(self): # real signature unknown; restored from __doc__
        """ QCompleter.completionRole() -> int """
        return 0

    def currentCompletion(self): # real signature unknown; restored from __doc__
        """ QCompleter.currentCompletion() -> QString """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ QCompleter.currentIndex() -> QModelIndex """
        pass

    def currentRow(self): # real signature unknown; restored from __doc__
        """ QCompleter.currentRow() -> int """
        return 0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QCompleter.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QCompleter.eventFilter(QObject, QEvent) -> bool """
        return False

    def highlighted(self, *args, **kwargs): # real signature unknown
        """
        QCompleter.highlighted[QString] [signal]
        QCompleter.highlighted[QModelIndex] [signal]
        """
        pass

    def maxVisibleItems(self): # real signature unknown; restored from __doc__
        """ QCompleter.maxVisibleItems() -> int """
        return 0

    def model(self): # real signature unknown; restored from __doc__
        """ QCompleter.model() -> QAbstractItemModel """
        pass

    def modelSorting(self): # real signature unknown; restored from __doc__
        """ QCompleter.modelSorting() -> QCompleter.ModelSorting """
        pass

    def pathFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QCompleter.pathFromIndex(QModelIndex) -> QString """
        pass

    def popup(self): # real signature unknown; restored from __doc__
        """ QCompleter.popup() -> QAbstractItemView """
        return QAbstractItemView

    def setCaseSensitivity(self, Qt_CaseSensitivity): # real signature unknown; restored from __doc__
        """ QCompleter.setCaseSensitivity(Qt.CaseSensitivity) """
        pass

    def setCompletionColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QCompleter.setCompletionColumn(int) """
        pass

    def setCompletionMode(self, QCompleter_CompletionMode): # real signature unknown; restored from __doc__
        """ QCompleter.setCompletionMode(QCompleter.CompletionMode) """
        pass

    def setCompletionPrefix(self, QString): # real signature unknown; restored from __doc__
        """ QCompleter.setCompletionPrefix(QString) """
        pass

    def setCompletionRole(self, p_int): # real signature unknown; restored from __doc__
        """ QCompleter.setCompletionRole(int) """
        pass

    def setCurrentRow(self, p_int): # real signature unknown; restored from __doc__
        """ QCompleter.setCurrentRow(int) -> bool """
        return False

    def setMaxVisibleItems(self, p_int): # real signature unknown; restored from __doc__
        """ QCompleter.setMaxVisibleItems(int) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ QCompleter.setModel(QAbstractItemModel) """
        pass

    def setModelSorting(self, QCompleter_ModelSorting): # real signature unknown; restored from __doc__
        """ QCompleter.setModelSorting(QCompleter.ModelSorting) """
        pass

    def setPopup(self, QAbstractItemView): # real signature unknown; restored from __doc__
        """ QCompleter.setPopup(QAbstractItemView) """
        pass

    def setWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QCompleter.setWidget(QWidget) """
        pass

    def setWrapAround(self, bool): # real signature unknown; restored from __doc__
        """ QCompleter.setWrapAround(bool) """
        pass

    def splitPath(self, QString): # real signature unknown; restored from __doc__
        """ QCompleter.splitPath(QString) -> QStringList """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ QCompleter.widget() -> QWidget """
        return QWidget

    def wrapAround(self): # real signature unknown; restored from __doc__
        """ QCompleter.wrapAround() -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    CaseInsensitivelySortedModel = 2
    CaseSensitivelySortedModel = 1
    InlineCompletion = 2
    PopupCompletion = 0
    UnfilteredPopupCompletion = 1
    UnsortedModel = 0


