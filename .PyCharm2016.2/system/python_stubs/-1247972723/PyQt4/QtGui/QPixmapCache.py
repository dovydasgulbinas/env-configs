# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QPixmapCache(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QPixmapCache()
    QPixmapCache(QPixmapCache)
    """
    def cacheLimit(self): # real signature unknown; restored from __doc__
        """ QPixmapCache.cacheLimit() -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ QPixmapCache.clear() """
        pass

    def find(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmapCache.find(QString) -> QPixmap
        QPixmapCache.find(QString, QPixmap) -> bool
        QPixmapCache.find(QPixmapCache.Key, QPixmap) -> bool
        """
        return QPixmap or False

    def insert(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmapCache.insert(QString, QPixmap) -> bool
        QPixmapCache.insert(QPixmap) -> QPixmapCache.Key
        """
        return False

    def remove(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmapCache.remove(QString)
        QPixmapCache.remove(QPixmapCache.Key)
        """
        pass

    def replace(self, QPixmapCache_Key, QPixmap): # real signature unknown; restored from __doc__
        """ QPixmapCache.replace(QPixmapCache.Key, QPixmap) -> bool """
        return False

    def setCacheLimit(self, p_int): # real signature unknown; restored from __doc__
        """ QPixmapCache.setCacheLimit(int) """
        pass

    def __init__(self, QPixmapCache=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




