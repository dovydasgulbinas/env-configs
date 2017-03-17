# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QDataWidgetMapper(__PyQt4_QtCore.QObject):
    """ QDataWidgetMapper(QObject parent=None) """
    def addMapping(self, QWidget, p_int, QByteArray=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDataWidgetMapper.addMapping(QWidget, int)
        QDataWidgetMapper.addMapping(QWidget, int, QByteArray)
        """
        pass

    def clearMapping(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.clearMapping() """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.currentIndex() -> int """
        return 0

    def currentIndexChanged(self, *args, **kwargs): # real signature unknown
        """ QDataWidgetMapper.currentIndexChanged[int] [signal] """
        pass

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.itemDelegate() -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def mappedPropertyName(self, QWidget): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.mappedPropertyName(QWidget) -> QByteArray """
        pass

    def mappedSection(self, QWidget): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.mappedSection(QWidget) -> int """
        return 0

    def mappedWidgetAt(self, p_int): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.mappedWidgetAt(int) -> QWidget """
        return QWidget

    def model(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.model() -> QAbstractItemModel """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.orientation() -> Qt.Orientation """
        pass

    def removeMapping(self, QWidget): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.removeMapping(QWidget) """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.revert() """
        pass

    def rootIndex(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.rootIndex() -> QModelIndex """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.setCurrentIndex(int) """
        pass

    def setCurrentModelIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.setCurrentModelIndex(QModelIndex) """
        pass

    def setItemDelegate(self, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.setItemDelegate(QAbstractItemDelegate) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.setModel(QAbstractItemModel) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.setOrientation(Qt.Orientation) """
        pass

    def setRootIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.setRootIndex(QModelIndex) """
        pass

    def setSubmitPolicy(self, QDataWidgetMapper_SubmitPolicy): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.setSubmitPolicy(QDataWidgetMapper.SubmitPolicy) """
        pass

    def submit(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.submit() -> bool """
        return False

    def submitPolicy(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.submitPolicy() -> QDataWidgetMapper.SubmitPolicy """
        pass

    def toFirst(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.toFirst() """
        pass

    def toLast(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.toLast() """
        pass

    def toNext(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.toNext() """
        pass

    def toPrevious(self): # real signature unknown; restored from __doc__
        """ QDataWidgetMapper.toPrevious() """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    AutoSubmit = 0
    ManualSubmit = 1


