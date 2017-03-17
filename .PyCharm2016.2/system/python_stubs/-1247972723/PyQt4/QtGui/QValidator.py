# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QValidator(__PyQt4_QtCore.QObject):
    """ QValidator(QObject parent=None) """
    def fixup(self, QString): # real signature unknown; restored from __doc__
        """ QValidator.fixup(QString) """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ QValidator.locale() -> QLocale """
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ QValidator.setLocale(QLocale) """
        pass

    def validate(self, QString, p_int): # real signature unknown; restored from __doc__
        """ QValidator.validate(QString, int) -> (QValidator.State, int) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Acceptable = 2
    Intermediate = 1
    Invalid = 0


