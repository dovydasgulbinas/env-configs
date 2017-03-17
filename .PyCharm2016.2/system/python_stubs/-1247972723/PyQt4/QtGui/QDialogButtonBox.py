# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QDialogButtonBox(QWidget):
    """
    QDialogButtonBox(QWidget parent=None)
    QDialogButtonBox(Qt.Orientation, QWidget parent=None)
    QDialogButtonBox(QDialogButtonBox.StandardButtons, Qt.Orientation orientation=Qt.Horizontal, QWidget parent=None)
    """
    def accepted(self, *args, **kwargs): # real signature unknown
        """ QDialogButtonBox.accepted [signal] """
        pass

    def addButton(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDialogButtonBox.addButton(QAbstractButton, QDialogButtonBox.ButtonRole)
        QDialogButtonBox.addButton(QString, QDialogButtonBox.ButtonRole) -> QPushButton
        QDialogButtonBox.addButton(QDialogButtonBox.StandardButton) -> QPushButton
        """
        return QPushButton

    def button(self, QDialogButtonBox_StandardButton): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.button(QDialogButtonBox.StandardButton) -> QPushButton """
        return QPushButton

    def buttonRole(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.buttonRole(QAbstractButton) -> QDialogButtonBox.ButtonRole """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.buttons() -> list-of-QAbstractButton """
        pass

    def centerButtons(self): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.centerButtons() -> bool """
        return False

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.changeEvent(QEvent) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.clear() """
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
        """ QDialogButtonBox.clicked[QAbstractButton] [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.event(QEvent) -> bool """
        return False

    def helpRequested(self, *args, **kwargs): # real signature unknown
        """ QDialogButtonBox.helpRequested [signal] """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.orientation() -> Qt.Orientation """
        pass

    def rejected(self, *args, **kwargs): # real signature unknown
        """ QDialogButtonBox.rejected [signal] """
        pass

    def removeButton(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.removeButton(QAbstractButton) """
        pass

    def setCenterButtons(self, bool): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.setCenterButtons(bool) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.setOrientation(Qt.Orientation) """
        pass

    def setStandardButtons(self, QDialogButtonBox_StandardButtons): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.setStandardButtons(QDialogButtonBox.StandardButtons) """
        pass

    def standardButton(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.standardButton(QAbstractButton) -> QDialogButtonBox.StandardButton """
        pass

    def standardButtons(self): # real signature unknown; restored from __doc__
        """ QDialogButtonBox.standardButtons() -> QDialogButtonBox.StandardButtons """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Abort = 262144
    AcceptRole = 0
    ActionRole = 3
    Apply = 33554432
    ApplyRole = 8
    Cancel = 4194304
    Close = 2097152
    DestructiveRole = 2
    Discard = 8388608
    GnomeLayout = 3
    Help = 16777216
    HelpRole = 4
    Ignore = 1048576
    InvalidRole = -1
    KdeLayout = 2
    MacLayout = 1
    No = 65536
    NoButton = 0
    NoRole = 6
    NoToAll = 131072
    Ok = 1024
    Open = 8192
    RejectRole = 1
    Reset = 67108864
    ResetRole = 7
    RestoreDefaults = 134217728
    Retry = 524288
    Save = 2048
    SaveAll = 4096
    WinLayout = 0
    Yes = 16384
    YesRole = 5
    YesToAll = 32768


