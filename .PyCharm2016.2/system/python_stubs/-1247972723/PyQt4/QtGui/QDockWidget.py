# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QDockWidget(QWidget):
    """
    QDockWidget(QString, QWidget parent=None, Qt.WindowFlags flags=0)
    QDockWidget(QWidget parent=None, Qt.WindowFlags flags=0)
    """
    def allowedAreas(self): # real signature unknown; restored from __doc__
        """ QDockWidget.allowedAreas() -> Qt.DockWidgetAreas """
        pass

    def allowedAreasChanged(self, *args, **kwargs): # real signature unknown
        """ QDockWidget.allowedAreasChanged[Qt.DockWidgetAreas] [signal] """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QDockWidget.changeEvent(QEvent) """
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ QDockWidget.closeEvent(QCloseEvent) """
        pass

    def dockLocationChanged(self, *args, **kwargs): # real signature unknown
        """ QDockWidget.dockLocationChanged[Qt.DockWidgetArea] [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QDockWidget.event(QEvent) -> bool """
        return False

    def features(self): # real signature unknown; restored from __doc__
        """ QDockWidget.features() -> QDockWidget.DockWidgetFeatures """
        pass

    def featuresChanged(self, *args, **kwargs): # real signature unknown
        """ QDockWidget.featuresChanged[QDockWidget.DockWidgetFeatures] [signal] """
        pass

    def initStyleOption(self, QStyleOptionDockWidget): # real signature unknown; restored from __doc__
        """ QDockWidget.initStyleOption(QStyleOptionDockWidget) """
        pass

    def isAreaAllowed(self, Qt_DockWidgetArea): # real signature unknown; restored from __doc__
        """ QDockWidget.isAreaAllowed(Qt.DockWidgetArea) -> bool """
        return False

    def isFloating(self): # real signature unknown; restored from __doc__
        """ QDockWidget.isFloating() -> bool """
        return False

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QDockWidget.paintEvent(QPaintEvent) """
        pass

    def setAllowedAreas(self, Qt_DockWidgetAreas): # real signature unknown; restored from __doc__
        """ QDockWidget.setAllowedAreas(Qt.DockWidgetAreas) """
        pass

    def setFeatures(self, QDockWidget_DockWidgetFeatures): # real signature unknown; restored from __doc__
        """ QDockWidget.setFeatures(QDockWidget.DockWidgetFeatures) """
        pass

    def setFloating(self, bool): # real signature unknown; restored from __doc__
        """ QDockWidget.setFloating(bool) """
        pass

    def setTitleBarWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QDockWidget.setTitleBarWidget(QWidget) """
        pass

    def setWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QDockWidget.setWidget(QWidget) """
        pass

    def titleBarWidget(self): # real signature unknown; restored from __doc__
        """ QDockWidget.titleBarWidget() -> QWidget """
        return QWidget

    def toggleViewAction(self): # real signature unknown; restored from __doc__
        """ QDockWidget.toggleViewAction() -> QAction """
        return QAction

    def topLevelChanged(self, *args, **kwargs): # real signature unknown
        """ QDockWidget.topLevelChanged[bool] [signal] """
        pass

    def visibilityChanged(self, *args, **kwargs): # real signature unknown
        """ QDockWidget.visibilityChanged[bool] [signal] """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ QDockWidget.widget() -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllDockWidgetFeatures = 7
    DockWidgetClosable = 1
    DockWidgetFloatable = 4
    DockWidgetMovable = 2
    DockWidgetVerticalTitleBar = 8
    NoDockWidgetFeatures = 0


