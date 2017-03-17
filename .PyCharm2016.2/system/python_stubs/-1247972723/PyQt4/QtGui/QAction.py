# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QAction(__PyQt4_QtCore.QObject):
    """
    QAction(QObject)
    QAction(QString, QObject)
    QAction(QIcon, QString, QObject)
    """
    def actionGroup(self): # real signature unknown; restored from __doc__
        """ QAction.actionGroup() -> QActionGroup """
        return QActionGroup

    def activate(self, QAction_ActionEvent): # real signature unknown; restored from __doc__
        """ QAction.activate(QAction.ActionEvent) """
        pass

    def associatedGraphicsWidgets(self): # real signature unknown; restored from __doc__
        """ QAction.associatedGraphicsWidgets() -> list-of-QGraphicsWidget """
        pass

    def associatedWidgets(self): # real signature unknown; restored from __doc__
        """ QAction.associatedWidgets() -> list-of-QWidget """
        pass

    def autoRepeat(self): # real signature unknown; restored from __doc__
        """ QAction.autoRepeat() -> bool """
        return False

    def changed(self, *args, **kwargs): # real signature unknown
        """ QAction.changed [signal] """
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ QAction.data() -> QVariant """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QAction.event(QEvent) -> bool """
        return False

    def font(self): # real signature unknown; restored from __doc__
        """ QAction.font() -> QFont """
        return QFont

    def hover(self): # real signature unknown; restored from __doc__
        """ QAction.hover() """
        pass

    def hovered(self, *args, **kwargs): # real signature unknown
        """ QAction.hovered [signal] """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ QAction.icon() -> QIcon """
        return QIcon

    def iconText(self): # real signature unknown; restored from __doc__
        """ QAction.iconText() -> QString """
        pass

    def isCheckable(self): # real signature unknown; restored from __doc__
        """ QAction.isCheckable() -> bool """
        return False

    def isChecked(self): # real signature unknown; restored from __doc__
        """ QAction.isChecked() -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ QAction.isEnabled() -> bool """
        return False

    def isIconVisibleInMenu(self): # real signature unknown; restored from __doc__
        """ QAction.isIconVisibleInMenu() -> bool """
        return False

    def isSeparator(self): # real signature unknown; restored from __doc__
        """ QAction.isSeparator() -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ QAction.isVisible() -> bool """
        return False

    def menu(self): # real signature unknown; restored from __doc__
        """ QAction.menu() -> QMenu """
        return QMenu

    def menuRole(self): # real signature unknown; restored from __doc__
        """ QAction.menuRole() -> QAction.MenuRole """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ QAction.parentWidget() -> QWidget """
        return QWidget

    def priority(self): # real signature unknown; restored from __doc__
        """ QAction.priority() -> QAction.Priority """
        pass

    def setActionGroup(self, QActionGroup): # real signature unknown; restored from __doc__
        """ QAction.setActionGroup(QActionGroup) """
        pass

    def setAutoRepeat(self, bool): # real signature unknown; restored from __doc__
        """ QAction.setAutoRepeat(bool) """
        pass

    def setCheckable(self, bool): # real signature unknown; restored from __doc__
        """ QAction.setCheckable(bool) """
        pass

    def setChecked(self, bool): # real signature unknown; restored from __doc__
        """ QAction.setChecked(bool) """
        pass

    def setData(self, QVariant): # real signature unknown; restored from __doc__
        """ QAction.setData(QVariant) """
        pass

    def setDisabled(self, bool): # real signature unknown; restored from __doc__
        """ QAction.setDisabled(bool) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QAction.setEnabled(bool) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ QAction.setFont(QFont) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ QAction.setIcon(QIcon) """
        pass

    def setIconText(self, QString): # real signature unknown; restored from __doc__
        """ QAction.setIconText(QString) """
        pass

    def setIconVisibleInMenu(self, bool): # real signature unknown; restored from __doc__
        """ QAction.setIconVisibleInMenu(bool) """
        pass

    def setMenu(self, QMenu): # real signature unknown; restored from __doc__
        """ QAction.setMenu(QMenu) """
        pass

    def setMenuRole(self, QAction_MenuRole): # real signature unknown; restored from __doc__
        """ QAction.setMenuRole(QAction.MenuRole) """
        pass

    def setPriority(self, QAction_Priority): # real signature unknown; restored from __doc__
        """ QAction.setPriority(QAction.Priority) """
        pass

    def setSeparator(self, bool): # real signature unknown; restored from __doc__
        """ QAction.setSeparator(bool) """
        pass

    def setShortcut(self, QKeySequence): # real signature unknown; restored from __doc__
        """ QAction.setShortcut(QKeySequence) """
        pass

    def setShortcutContext(self, Qt_ShortcutContext): # real signature unknown; restored from __doc__
        """ QAction.setShortcutContext(Qt.ShortcutContext) """
        pass

    def setShortcuts(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAction.setShortcuts(list-of-QKeySequence)
        QAction.setShortcuts(QKeySequence.StandardKey)
        """
        pass

    def setSoftKeyRole(self, QAction_SoftKeyRole): # real signature unknown; restored from __doc__
        """ QAction.setSoftKeyRole(QAction.SoftKeyRole) """
        pass

    def setStatusTip(self, QString): # real signature unknown; restored from __doc__
        """ QAction.setStatusTip(QString) """
        pass

    def setText(self, QString): # real signature unknown; restored from __doc__
        """ QAction.setText(QString) """
        pass

    def setToolTip(self, QString): # real signature unknown; restored from __doc__
        """ QAction.setToolTip(QString) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QAction.setVisible(bool) """
        pass

    def setWhatsThis(self, QString): # real signature unknown; restored from __doc__
        """ QAction.setWhatsThis(QString) """
        pass

    def shortcut(self): # real signature unknown; restored from __doc__
        """ QAction.shortcut() -> QKeySequence """
        return QKeySequence

    def shortcutContext(self): # real signature unknown; restored from __doc__
        """ QAction.shortcutContext() -> Qt.ShortcutContext """
        pass

    def shortcuts(self): # real signature unknown; restored from __doc__
        """ QAction.shortcuts() -> list-of-QKeySequence """
        pass

    def showStatusText(self, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QAction.showStatusText(QWidget widget=None) -> bool """
        return False

    def softKeyRole(self): # real signature unknown; restored from __doc__
        """ QAction.softKeyRole() -> QAction.SoftKeyRole """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ QAction.statusTip() -> QString """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QAction.text() -> QString """
        pass

    def toggle(self): # real signature unknown; restored from __doc__
        """ QAction.toggle() """
        pass

    def toggled(self, *args, **kwargs): # real signature unknown
        """ QAction.toggled[bool] [signal] """
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ QAction.toolTip() -> QString """
        pass

    def trigger(self): # real signature unknown; restored from __doc__
        """ QAction.trigger() """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
        """
        QAction.triggered[bool] [signal]
        QAction.triggered [signal]
        """
        pass

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ QAction.whatsThis() -> QString """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AboutQtRole = 3
    AboutRole = 4
    ApplicationSpecificRole = 2
    HighPriority = 256
    Hover = 1
    LowPriority = 0
    NegativeSoftKey = 2
    NormalPriority = 128
    NoRole = 0
    NoSoftKey = 0
    PositiveSoftKey = 1
    PreferencesRole = 5
    QuitRole = 6
    SelectSoftKey = 3
    TextHeuristicRole = 1
    Trigger = 0


