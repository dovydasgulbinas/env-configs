# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QFileDialog(QDialog):
    """
    QFileDialog(QWidget, Qt.WindowFlags)
    QFileDialog(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString())
    """
    def accept(self): # real signature unknown; restored from __doc__
        """ QFileDialog.accept() """
        pass

    def acceptMode(self): # real signature unknown; restored from __doc__
        """ QFileDialog.acceptMode() -> QFileDialog.AcceptMode """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QFileDialog.changeEvent(QEvent) """
        pass

    def confirmOverwrite(self): # real signature unknown; restored from __doc__
        """ QFileDialog.confirmOverwrite() -> bool """
        return False

    def currentChanged(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.currentChanged[QString] [signal] """
        pass

    def defaultSuffix(self): # real signature unknown; restored from __doc__
        """ QFileDialog.defaultSuffix() -> QString """
        pass

    def directory(self): # real signature unknown; restored from __doc__
        """ QFileDialog.directory() -> QDir """
        pass

    def directoryEntered(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.directoryEntered[QString] [signal] """
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ QFileDialog.done(int) """
        pass

    def fileMode(self): # real signature unknown; restored from __doc__
        """ QFileDialog.fileMode() -> QFileDialog.FileMode """
        pass

    def fileSelected(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.fileSelected[QString] [signal] """
        pass

    def filesSelected(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.filesSelected[QStringList] [signal] """
        pass

    def filter(self): # real signature unknown; restored from __doc__
        """ QFileDialog.filter() -> QDir.Filters """
        pass

    def filters(self): # real signature unknown; restored from __doc__
        """ QFileDialog.filters() -> QStringList """
        pass

    def filterSelected(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.filterSelected[QString] [signal] """
        pass

    def getExistingDirectory(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getExistingDirectory(QWidget parent=None, QString caption=QString(), QString directory=QString(), QFileDialog.Options options=QFileDialog.ShowDirsOnly) -> QString """
        pass

    def getOpenFileName(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getOpenFileName(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString(), QString selectedFilter=None, QFileDialog.Options options=0) -> QString """
        pass

    def getOpenFileNameAndFilter(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getOpenFileNameAndFilter(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString(), QString initialFilter=QString(), QFileDialog.Options options=0) -> (QString, QString) """
        pass

    def getOpenFileNames(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getOpenFileNames(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString(), QString selectedFilter=None, QFileDialog.Options options=0) -> QStringList """
        pass

    def getOpenFileNamesAndFilter(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getOpenFileNamesAndFilter(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString(), QString initialFilter=QString(), QFileDialog.Options options=0) -> (QString, QString) """
        pass

    def getSaveFileName(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getSaveFileName(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString(), QString selectedFilter=None, QFileDialog.Options options=0) -> QString """
        pass

    def getSaveFileNameAndFilter(self, QWidget_parent=None, QString_caption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileDialog.getSaveFileNameAndFilter(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString(), QString initialFilter=QString(), QFileDialog.Options options=0) -> (QString, QString) """
        pass

    def history(self): # real signature unknown; restored from __doc__
        """ QFileDialog.history() -> QStringList """
        pass

    def iconProvider(self): # real signature unknown; restored from __doc__
        """ QFileDialog.iconProvider() -> QFileIconProvider """
        return QFileIconProvider

    def isNameFilterDetailsVisible(self): # real signature unknown; restored from __doc__
        """ QFileDialog.isNameFilterDetailsVisible() -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ QFileDialog.isReadOnly() -> bool """
        return False

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ QFileDialog.itemDelegate() -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def labelText(self, QFileDialog_DialogLabel): # real signature unknown; restored from __doc__
        """ QFileDialog.labelText(QFileDialog.DialogLabel) -> QString """
        pass

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ QFileDialog.nameFilters() -> QStringList """
        pass

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileDialog.open()
        QFileDialog.open(QObject, SLOT())
        QFileDialog.open(callable)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ QFileDialog.options() -> QFileDialog.Options """
        pass

    def proxyModel(self): # real signature unknown; restored from __doc__
        """ QFileDialog.proxyModel() -> QAbstractProxyModel """
        return QAbstractProxyModel

    def resolveSymlinks(self): # real signature unknown; restored from __doc__
        """ QFileDialog.resolveSymlinks() -> bool """
        return False

    def restoreState(self, QByteArray): # real signature unknown; restored from __doc__
        """ QFileDialog.restoreState(QByteArray) -> bool """
        return False

    def saveState(self): # real signature unknown; restored from __doc__
        """ QFileDialog.saveState() -> QByteArray """
        pass

    def selectedFiles(self): # real signature unknown; restored from __doc__
        """ QFileDialog.selectedFiles() -> QStringList """
        pass

    def selectedFilter(self): # real signature unknown; restored from __doc__
        """ QFileDialog.selectedFilter() -> QString """
        pass

    def selectedNameFilter(self): # real signature unknown; restored from __doc__
        """ QFileDialog.selectedNameFilter() -> QString """
        pass

    def selectFile(self, QString): # real signature unknown; restored from __doc__
        """ QFileDialog.selectFile(QString) """
        pass

    def selectFilter(self, QString): # real signature unknown; restored from __doc__
        """ QFileDialog.selectFilter(QString) """
        pass

    def selectNameFilter(self, QString): # real signature unknown; restored from __doc__
        """ QFileDialog.selectNameFilter(QString) """
        pass

    def setAcceptMode(self, QFileDialog_AcceptMode): # real signature unknown; restored from __doc__
        """ QFileDialog.setAcceptMode(QFileDialog.AcceptMode) """
        pass

    def setConfirmOverwrite(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setConfirmOverwrite(bool) """
        pass

    def setDefaultSuffix(self, QString): # real signature unknown; restored from __doc__
        """ QFileDialog.setDefaultSuffix(QString) """
        pass

    def setDirectory(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileDialog.setDirectory(QString)
        QFileDialog.setDirectory(QDir)
        """
        pass

    def setFileMode(self, QFileDialog_FileMode): # real signature unknown; restored from __doc__
        """ QFileDialog.setFileMode(QFileDialog.FileMode) """
        pass

    def setFilter(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileDialog.setFilter(QString)
        QFileDialog.setFilter(QDir.Filters)
        """
        pass

    def setFilters(self, QStringList): # real signature unknown; restored from __doc__
        """ QFileDialog.setFilters(QStringList) """
        pass

    def setHistory(self, QStringList): # real signature unknown; restored from __doc__
        """ QFileDialog.setHistory(QStringList) """
        pass

    def setIconProvider(self, QFileIconProvider): # real signature unknown; restored from __doc__
        """ QFileDialog.setIconProvider(QFileIconProvider) """
        pass

    def setItemDelegate(self, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ QFileDialog.setItemDelegate(QAbstractItemDelegate) """
        pass

    def setLabelText(self, QFileDialog_DialogLabel, QString): # real signature unknown; restored from __doc__
        """ QFileDialog.setLabelText(QFileDialog.DialogLabel, QString) """
        pass

    def setNameFilter(self, QString): # real signature unknown; restored from __doc__
        """ QFileDialog.setNameFilter(QString) """
        pass

    def setNameFilterDetailsVisible(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setNameFilterDetailsVisible(bool) """
        pass

    def setNameFilters(self, QStringList): # real signature unknown; restored from __doc__
        """ QFileDialog.setNameFilters(QStringList) """
        pass

    def setOption(self, QFileDialog_Option, bool_on=True): # real signature unknown; restored from __doc__
        """ QFileDialog.setOption(QFileDialog.Option, bool on=True) """
        pass

    def setOptions(self, QFileDialog_Options): # real signature unknown; restored from __doc__
        """ QFileDialog.setOptions(QFileDialog.Options) """
        pass

    def setProxyModel(self, QAbstractProxyModel): # real signature unknown; restored from __doc__
        """ QFileDialog.setProxyModel(QAbstractProxyModel) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setReadOnly(bool) """
        pass

    def setResolveSymlinks(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setResolveSymlinks(bool) """
        pass

    def setSidebarUrls(self, list_of_QUrl): # real signature unknown; restored from __doc__
        """ QFileDialog.setSidebarUrls(list-of-QUrl) """
        pass

    def setViewMode(self, QFileDialog_ViewMode): # real signature unknown; restored from __doc__
        """ QFileDialog.setViewMode(QFileDialog.ViewMode) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setVisible(bool) """
        pass

    def sidebarUrls(self): # real signature unknown; restored from __doc__
        """ QFileDialog.sidebarUrls() -> list-of-QUrl """
        pass

    def testOption(self, QFileDialog_Option): # real signature unknown; restored from __doc__
        """ QFileDialog.testOption(QFileDialog.Option) -> bool """
        return False

    def viewMode(self): # real signature unknown; restored from __doc__
        """ QFileDialog.viewMode() -> QFileDialog.ViewMode """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Accept = 3
    AcceptOpen = 0
    AcceptSave = 1
    AnyFile = 0
    Detail = 0
    Directory = 2
    DirectoryOnly = 4
    DontConfirmOverwrite = 4
    DontResolveSymlinks = 2
    DontUseCustomDirectoryIcons = 128
    DontUseNativeDialog = 16
    DontUseSheet = 8
    ExistingFile = 1
    ExistingFiles = 3
    FileName = 1
    FileType = 2
    HideNameFilterDetails = 64
    List = 1
    LookIn = 0
    ReadOnly = 32
    Reject = 4
    ShowDirsOnly = 1


