# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QFileIconProvider(): # skipped bases: <type 'sip.simplewrapper'>
    """ QFileIconProvider() """
    def icon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileIconProvider.icon(QFileIconProvider.IconType) -> QIcon
        QFileIconProvider.icon(QFileInfo) -> QIcon
        """
        return QIcon

    def type(self, QFileInfo): # real signature unknown; restored from __doc__
        """ QFileIconProvider.type(QFileInfo) -> QString """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Computer = 0
    Desktop = 1
    Drive = 4
    File = 6
    Folder = 5
    Network = 3
    Trashcan = 2


