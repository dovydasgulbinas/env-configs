# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QIcon(): # skipped bases: <type 'sip.wrapper'>
    """
    QIcon()
    QIcon(QPixmap)
    QIcon(QIcon)
    QIcon(QString)
    QIcon(QIconEngine)
    QIcon(QIconEngineV2)
    QIcon(QVariant)
    """
    def actualSize(self, QSize, QIcon_Mode_mode=None, QIcon_State_state=None): # real signature unknown; restored from __doc__
        """ QIcon.actualSize(QSize, QIcon.Mode mode=QIcon.Normal, QIcon.State state=QIcon.Off) -> QSize """
        pass

    def addFile(self, QString, QSize_size=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QIcon.addFile(QString, QSize size=QSize(), QIcon.Mode mode=QIcon.Normal, QIcon.State state=QIcon.Off) """
        pass

    def addPixmap(self, QPixmap, QIcon_Mode_mode=None, QIcon_State_state=None): # real signature unknown; restored from __doc__
        """ QIcon.addPixmap(QPixmap, QIcon.Mode mode=QIcon.Normal, QIcon.State state=QIcon.Off) """
        pass

    def availableSizes(self, QIcon_Mode_mode=None, QIcon_State_state=None): # real signature unknown; restored from __doc__
        """ QIcon.availableSizes(QIcon.Mode mode=QIcon.Normal, QIcon.State state=QIcon.Off) -> list-of-QSize """
        pass

    def cacheKey(self): # real signature unknown; restored from __doc__
        """ QIcon.cacheKey() -> int """
        return 0

    def fromTheme(self, QString, QIcon_fallback=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QIcon.fromTheme(QString, QIcon fallback=QIcon()) -> QIcon """
        pass

    def hasThemeIcon(self, QString): # real signature unknown; restored from __doc__
        """ QIcon.hasThemeIcon(QString) -> bool """
        return False

    def isDetached(self): # real signature unknown; restored from __doc__
        """ QIcon.isDetached() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QIcon.isNull() -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ QIcon.name() -> QString """
        pass

    def paint(self, QPainter, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QIcon.paint(QPainter, QRect, Qt.Alignment alignment=Qt.AlignCenter, QIcon.Mode mode=QIcon.Normal, QIcon.State state=QIcon.Off)
        QIcon.paint(QPainter, int, int, int, int, Qt.Alignment alignment=Qt.AlignCenter, QIcon.Mode mode=QIcon.Normal, QIcon.State state=QIcon.Off)
        """
        pass

    def pixmap(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QIcon.pixmap(QSize, QIcon.Mode mode=QIcon.Normal, QIcon.State state=QIcon.Off) -> QPixmap
        QIcon.pixmap(int, int, QIcon.Mode mode=QIcon.Normal, QIcon.State state=QIcon.Off) -> QPixmap
        QIcon.pixmap(int, QIcon.Mode mode=QIcon.Normal, QIcon.State state=QIcon.Off) -> QPixmap
        """
        return QPixmap

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ QIcon.serialNumber() -> int """
        return 0

    def setThemeName(self, QString): # real signature unknown; restored from __doc__
        """ QIcon.setThemeName(QString) """
        pass

    def setThemeSearchPaths(self, QStringList): # real signature unknown; restored from __doc__
        """ QIcon.setThemeSearchPaths(QStringList) """
        pass

    def swap(self, QIcon): # real signature unknown; restored from __doc__
        """ QIcon.swap(QIcon) """
        pass

    def themeName(self): # real signature unknown; restored from __doc__
        """ QIcon.themeName() -> QString """
        pass

    def themeSearchPaths(self): # real signature unknown; restored from __doc__
        """ QIcon.themeSearchPaths() -> QStringList """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Active = 2
    Disabled = 1
    Normal = 0
    Off = 1
    On = 0
    Selected = 3


