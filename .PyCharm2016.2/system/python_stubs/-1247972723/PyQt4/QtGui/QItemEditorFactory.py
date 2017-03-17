# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QItemEditorFactory(): # skipped bases: <type 'sip.wrapper'>
    """
    QItemEditorFactory()
    QItemEditorFactory(QItemEditorFactory)
    """
    def createEditor(self, Type, QWidget): # real signature unknown; restored from __doc__
        """ QItemEditorFactory.createEditor(Type, QWidget) -> QWidget """
        return QWidget

    def defaultFactory(self): # real signature unknown; restored from __doc__
        """ QItemEditorFactory.defaultFactory() -> QItemEditorFactory """
        return QItemEditorFactory

    def registerEditor(self, Type, QItemEditorCreatorBase): # real signature unknown; restored from __doc__
        """ QItemEditorFactory.registerEditor(Type, QItemEditorCreatorBase) """
        pass

    def setDefaultFactory(self, QItemEditorFactory): # real signature unknown; restored from __doc__
        """ QItemEditorFactory.setDefaultFactory(QItemEditorFactory) """
        pass

    def valuePropertyName(self, Type): # real signature unknown; restored from __doc__
        """ QItemEditorFactory.valuePropertyName(Type) -> QByteArray """
        pass

    def __init__(self, QItemEditorFactory=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



