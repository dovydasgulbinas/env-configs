# encoding: utf-8
# module PyQt4.QtHelp
# from /usr/lib/python2.7/dist-packages/PyQt4/QtHelp.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


# no functions
# classes

class QHelpContentItem(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def child(self, p_int): # real signature unknown; restored from __doc__
        """ QHelpContentItem.child(int) -> QHelpContentItem """
        return QHelpContentItem

    def childCount(self): # real signature unknown; restored from __doc__
        """ QHelpContentItem.childCount() -> int """
        return 0

    def childPosition(self, QHelpContentItem): # real signature unknown; restored from __doc__
        """ QHelpContentItem.childPosition(QHelpContentItem) -> int """
        return 0

    def parent(self): # real signature unknown; restored from __doc__
        """ QHelpContentItem.parent() -> QHelpContentItem """
        return QHelpContentItem

    def row(self): # real signature unknown; restored from __doc__
        """ QHelpContentItem.row() -> int """
        return 0

    def title(self): # real signature unknown; restored from __doc__
        """ QHelpContentItem.title() -> QString """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ QHelpContentItem.url() -> QUrl """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QHelpContentModel(__PyQt4_QtCore.QAbstractItemModel):
    # no doc
    def columnCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QHelpContentModel.columnCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def contentItemAt(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QHelpContentModel.contentItemAt(QModelIndex) -> QHelpContentItem """
        return QHelpContentItem

    def contentsCreated(self, *args, **kwargs): # real signature unknown
        """ QHelpContentModel.contentsCreated [signal] """
        pass

    def contentsCreationStarted(self, *args, **kwargs): # real signature unknown
        """ QHelpContentModel.contentsCreationStarted [signal] """
        pass

    def createContents(self, QString): # real signature unknown; restored from __doc__
        """ QHelpContentModel.createContents(QString) """
        pass

    def data(self, QModelIndex, p_int): # real signature unknown; restored from __doc__
        """ QHelpContentModel.data(QModelIndex, int) -> QVariant """
        pass

    def index(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QHelpContentModel.index(int, int, QModelIndex parent=QModelIndex()) -> QModelIndex """
        pass

    def isCreatingContents(self): # real signature unknown; restored from __doc__
        """ QHelpContentModel.isCreatingContents() -> bool """
        return False

    def parent(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QHelpContentModel.parent(QModelIndex) -> QModelIndex """
        pass

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QHelpContentModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpContentWidget(__PyQt4_QtGui.QTreeView):
    # no doc
    def indexOf(self, QUrl): # real signature unknown; restored from __doc__
        """ QHelpContentWidget.indexOf(QUrl) -> QModelIndex """
        pass

    def linkActivated(self, *args, **kwargs): # real signature unknown
        """ QHelpContentWidget.linkActivated[QUrl] [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpEngineCore(__PyQt4_QtCore.QObject):
    """ QHelpEngineCore(QString, QObject parent=None) """
    def addCustomFilter(self, QString, QStringList): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.addCustomFilter(QString, QStringList) -> bool """
        return False

    def autoSaveFilter(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.autoSaveFilter() -> bool """
        return False

    def collectionFile(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.collectionFile() -> QString """
        pass

    def copyCollectionFile(self, QString): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.copyCollectionFile(QString) -> bool """
        return False

    def currentFilter(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.currentFilter() -> QString """
        pass

    def currentFilterChanged(self, *args, **kwargs): # real signature unknown
        """ QHelpEngineCore.currentFilterChanged[QString] [signal] """
        pass

    def customFilters(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.customFilters() -> QStringList """
        pass

    def customValue(self, QString, QVariant_defaultValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QHelpEngineCore.customValue(QString, QVariant defaultValue=QVariant()) -> QVariant """
        pass

    def documentationFileName(self, QString): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.documentationFileName(QString) -> QString """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.error() -> QString """
        pass

    def fileData(self, QUrl): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.fileData(QUrl) -> QByteArray """
        pass

    def files(self, QString, QStringList, QString_extensionFilter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QHelpEngineCore.files(QString, QStringList, QString extensionFilter=QString()) -> list-of-QUrl """
        pass

    def filterAttributes(self, QString=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHelpEngineCore.filterAttributes() -> QStringList
        QHelpEngineCore.filterAttributes(QString) -> QStringList
        """
        pass

    def filterAttributeSets(self, QString): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.filterAttributeSets(QString) -> list-of-QStringList """
        pass

    def findFile(self, QUrl): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.findFile(QUrl) -> QUrl """
        pass

    def linksForIdentifier(self, QString): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.linksForIdentifier(QString) -> dict-of-QString-QUrl """
        pass

    def metaData(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.metaData(QString, QString) -> QVariant """
        pass

    def namespaceName(self, QString): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.namespaceName(QString) -> QString """
        pass

    def registerDocumentation(self, QString): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.registerDocumentation(QString) -> bool """
        return False

    def registeredDocumentations(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.registeredDocumentations() -> QStringList """
        pass

    def removeCustomFilter(self, QString): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.removeCustomFilter(QString) -> bool """
        return False

    def removeCustomValue(self, QString): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.removeCustomValue(QString) -> bool """
        return False

    def setAutoSaveFilter(self, bool): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.setAutoSaveFilter(bool) """
        pass

    def setCollectionFile(self, QString): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.setCollectionFile(QString) """
        pass

    def setCurrentFilter(self, QString): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.setCurrentFilter(QString) """
        pass

    def setCustomValue(self, QString, QVariant): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.setCustomValue(QString, QVariant) -> bool """
        return False

    def setupData(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.setupData() -> bool """
        return False

    def setupFinished(self, *args, **kwargs): # real signature unknown
        """ QHelpEngineCore.setupFinished [signal] """
        pass

    def setupStarted(self, *args, **kwargs): # real signature unknown
        """ QHelpEngineCore.setupStarted [signal] """
        pass

    def unregisterDocumentation(self, QString): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.unregisterDocumentation(QString) -> bool """
        return False

    def warning(self, *args, **kwargs): # real signature unknown
        """ QHelpEngineCore.warning[QString] [signal] """
        pass

    def __init__(self, QString, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QHelpEngine(QHelpEngineCore):
    """ QHelpEngine(QString, QObject parent=None) """
    def contentModel(self): # real signature unknown; restored from __doc__
        """ QHelpEngine.contentModel() -> QHelpContentModel """
        return QHelpContentModel

    def contentWidget(self): # real signature unknown; restored from __doc__
        """ QHelpEngine.contentWidget() -> QHelpContentWidget """
        return QHelpContentWidget

    def indexModel(self): # real signature unknown; restored from __doc__
        """ QHelpEngine.indexModel() -> QHelpIndexModel """
        return QHelpIndexModel

    def indexWidget(self): # real signature unknown; restored from __doc__
        """ QHelpEngine.indexWidget() -> QHelpIndexWidget """
        return QHelpIndexWidget

    def searchEngine(self): # real signature unknown; restored from __doc__
        """ QHelpEngine.searchEngine() -> QHelpSearchEngine """
        return QHelpSearchEngine

    def __init__(self, QString, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QHelpIndexModel(__PyQt4_QtGui.QStringListModel):
    # no doc
    def createIndex(self, QString): # real signature unknown; restored from __doc__
        """ QHelpIndexModel.createIndex(QString) """
        pass

    def filter(self, QString, QString_wildcard=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QHelpIndexModel.filter(QString, QString wildcard=QString()) -> QModelIndex """
        pass

    def indexCreated(self, *args, **kwargs): # real signature unknown
        """ QHelpIndexModel.indexCreated [signal] """
        pass

    def indexCreationStarted(self, *args, **kwargs): # real signature unknown
        """ QHelpIndexModel.indexCreationStarted [signal] """
        pass

    def isCreatingIndex(self): # real signature unknown; restored from __doc__
        """ QHelpIndexModel.isCreatingIndex() -> bool """
        return False

    def linksForKeyword(self, QString): # real signature unknown; restored from __doc__
        """ QHelpIndexModel.linksForKeyword(QString) -> dict-of-QString-QUrl """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpIndexWidget(__PyQt4_QtGui.QListView):
    # no doc
    def activateCurrentItem(self): # real signature unknown; restored from __doc__
        """ QHelpIndexWidget.activateCurrentItem() """
        pass

    def filterIndices(self, QString, QString_wildcard=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QHelpIndexWidget.filterIndices(QString, QString wildcard=QString()) """
        pass

    def linkActivated(self, *args, **kwargs): # real signature unknown
        """ QHelpIndexWidget.linkActivated[QUrl, QString] [signal] """
        pass

    def linksActivated(self, *args, **kwargs): # real signature unknown
        """ QHelpIndexWidget.linksActivated[dict-of-QString-QUrl, QString] [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpSearchEngine(__PyQt4_QtCore.QObject):
    """ QHelpSearchEngine(QHelpEngineCore, QObject parent=None) """
    def cancelIndexing(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.cancelIndexing() """
        pass

    def cancelSearching(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.cancelSearching() """
        pass

    def hitCount(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.hitCount() -> int """
        return 0

    def hits(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.hits(int, int) -> list-of-tuple-of-QString-QString """
        pass

    def hitsCount(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.hitsCount() -> int """
        return 0

    def indexingFinished(self, *args, **kwargs): # real signature unknown
        """ QHelpSearchEngine.indexingFinished [signal] """
        pass

    def indexingStarted(self, *args, **kwargs): # real signature unknown
        """ QHelpSearchEngine.indexingStarted [signal] """
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.query() -> list-of-QHelpSearchQuery """
        pass

    def queryWidget(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.queryWidget() -> QHelpSearchQueryWidget """
        return QHelpSearchQueryWidget

    def reindexDocumentation(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.reindexDocumentation() """
        pass

    def resultWidget(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.resultWidget() -> QHelpSearchResultWidget """
        return QHelpSearchResultWidget

    def search(self, list_of_QHelpSearchQuery): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.search(list-of-QHelpSearchQuery) """
        pass

    def searchingFinished(self, *args, **kwargs): # real signature unknown
        """ QHelpSearchEngine.searchingFinished[int] [signal] """
        pass

    def searchingStarted(self, *args, **kwargs): # real signature unknown
        """ QHelpSearchEngine.searchingStarted [signal] """
        pass

    def __init__(self, QHelpEngineCore, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QHelpSearchQuery(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QHelpSearchQuery()
    QHelpSearchQuery(QHelpSearchQuery.FieldName, QStringList)
    QHelpSearchQuery(QHelpSearchQuery)
    """
    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ALL = 4
    ATLEAST = 5
    DEFAULT = 0
    FUZZY = 1
    PHRASE = 3
    WITHOUT = 2


class QHelpSearchQueryWidget(__PyQt4_QtGui.QWidget):
    """ QHelpSearchQueryWidget(QWidget parent=None) """
    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def collapseExtendedSearch(self): # real signature unknown; restored from __doc__
        """ QHelpSearchQueryWidget.collapseExtendedSearch() """
        pass

    def expandExtendedSearch(self): # real signature unknown; restored from __doc__
        """ QHelpSearchQueryWidget.expandExtendedSearch() """
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ QHelpSearchQueryWidget.query() -> list-of-QHelpSearchQuery """
        pass

    def search(self, *args, **kwargs): # real signature unknown
        """ QHelpSearchQueryWidget.search [signal] """
        pass

    def setQuery(self, list_of_QHelpSearchQuery): # real signature unknown; restored from __doc__
        """ QHelpSearchQueryWidget.setQuery(list-of-QHelpSearchQuery) """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


class QHelpSearchResultWidget(__PyQt4_QtGui.QWidget):
    # no doc
    def linkAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QHelpSearchResultWidget.linkAt(QPoint) -> QUrl """
        pass

    def requestShowLink(self, *args, **kwargs): # real signature unknown
        """ QHelpSearchResultWidget.requestShowLink[QUrl] [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


