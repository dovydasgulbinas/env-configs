# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QAbstractItemModel import QAbstractItemModel

class QAbstractListModel(QAbstractItemModel):
    """ QAbstractListModel(QObject parent=None) """
    def columnCount(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractListModel.dropMimeData(QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def hasChildren(self, *args, **kwargs): # real signature unknown
        pass

    def index(self, p_int, int_column=0, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractListModel.index(int, int column=0, QModelIndex parent=QModelIndex()) -> QModelIndex """
        pass

    def parent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


