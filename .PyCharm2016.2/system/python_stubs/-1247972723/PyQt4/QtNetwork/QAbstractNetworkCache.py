# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python2.7/dist-packages/PyQt4/QtNetwork.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QAbstractNetworkCache(__PyQt4_QtCore.QObject):
    """ QAbstractNetworkCache(QObject parent=None) """
    def cacheSize(self): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.cacheSize() -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.clear() """
        pass

    def data(self, QUrl): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.data(QUrl) -> QIODevice """
        pass

    def insert(self, QIODevice): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.insert(QIODevice) """
        pass

    def metaData(self, QUrl): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.metaData(QUrl) -> QNetworkCacheMetaData """
        return QNetworkCacheMetaData

    def prepare(self, QNetworkCacheMetaData): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.prepare(QNetworkCacheMetaData) -> QIODevice """
        pass

    def remove(self, QUrl): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.remove(QUrl) -> bool """
        return False

    def updateMetaData(self, QNetworkCacheMetaData): # real signature unknown; restored from __doc__
        """ QAbstractNetworkCache.updateMetaData(QNetworkCacheMetaData) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


