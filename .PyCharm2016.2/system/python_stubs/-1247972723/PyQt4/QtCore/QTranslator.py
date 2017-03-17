# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QTranslator(QObject):
    """ QTranslator(QObject parent=None) """
    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QTranslator.isEmpty() -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTranslator.load(QString, QString directory=QString(), QString searchDelimiters=QString(), QString suffix=QString()) -> bool
        QTranslator.load(QLocale, QString, QString prefix=QString(), QString directory=QString(), QString suffix=QString()) -> bool
        """
        pass

    def loadFromData(self, p_str): # real signature unknown; restored from __doc__
        """ QTranslator.loadFromData(str) -> bool """
        return False

    def translate(self, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTranslator.translate(str, str, str disambiguation=None) -> QString
        QTranslator.translate(str, str, str, int) -> QString
        """
        return QString

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


