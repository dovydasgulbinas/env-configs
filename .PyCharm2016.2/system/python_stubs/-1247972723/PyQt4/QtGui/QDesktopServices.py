# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QDesktopServices(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDesktopServices()
    QDesktopServices(QDesktopServices)
    """
    def displayName(self, QDesktopServices_StandardLocation): # real signature unknown; restored from __doc__
        """ QDesktopServices.displayName(QDesktopServices.StandardLocation) -> QString """
        pass

    def openUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QDesktopServices.openUrl(QUrl) -> bool """
        return False

    def setUrlHandler(self, QString, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDesktopServices.setUrlHandler(QString, QObject, str)
        QDesktopServices.setUrlHandler(QString, callable)
        """
        pass

    def storageLocation(self, QDesktopServices_StandardLocation): # real signature unknown; restored from __doc__
        """ QDesktopServices.storageLocation(QDesktopServices.StandardLocation) -> QString """
        pass

    def unsetUrlHandler(self, QString): # real signature unknown; restored from __doc__
        """ QDesktopServices.unsetUrlHandler(QString) """
        pass

    def __init__(self, QDesktopServices=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ApplicationsLocation = 3
    CacheLocation = 10
    DataLocation = 9
    DesktopLocation = 0
    DocumentsLocation = 1
    FontsLocation = 2
    HomeLocation = 8
    MoviesLocation = 5
    MusicLocation = 4
    PicturesLocation = 6
    TempLocation = 7


