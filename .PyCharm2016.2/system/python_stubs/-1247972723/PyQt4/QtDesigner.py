# encoding: utf-8
# module PyQt4.QtDesigner
# from /usr/lib/python2.7/dist-packages/PyQt4/QtDesigner.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


# no functions
# classes

class QAbstractExtensionFactory(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QAbstractExtensionFactory()
    QAbstractExtensionFactory(QAbstractExtensionFactory)
    """
    def extension(self, QObject, QString): # real signature unknown; restored from __doc__
        """ QAbstractExtensionFactory.extension(QObject, QString) -> QObject """
        pass

    def __init__(self, QAbstractExtensionFactory=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QAbstractExtensionManager(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QAbstractExtensionManager()
    QAbstractExtensionManager(QAbstractExtensionManager)
    """
    def extension(self, QObject, QString): # real signature unknown; restored from __doc__
        """ QAbstractExtensionManager.extension(QObject, QString) -> QObject """
        pass

    def registerExtensions(self, QAbstractExtensionFactory, QString): # real signature unknown; restored from __doc__
        """ QAbstractExtensionManager.registerExtensions(QAbstractExtensionFactory, QString) """
        pass

    def unregisterExtensions(self, QAbstractExtensionFactory, QString): # real signature unknown; restored from __doc__
        """ QAbstractExtensionManager.unregisterExtensions(QAbstractExtensionFactory, QString) """
        pass

    def __init__(self, QAbstractExtensionManager=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QAbstractFormBuilder(): # skipped bases: <type 'sip.simplewrapper'>
    """ QAbstractFormBuilder() """
    def load(self, QIODevice, QWidget_parent=None): # real signature unknown; restored from __doc__
        """ QAbstractFormBuilder.load(QIODevice, QWidget parent=None) -> QWidget """
        pass

    def save(self, QIODevice, QWidget): # real signature unknown; restored from __doc__
        """ QAbstractFormBuilder.save(QIODevice, QWidget) """
        pass

    def setWorkingDirectory(self, QDir): # real signature unknown; restored from __doc__
        """ QAbstractFormBuilder.setWorkingDirectory(QDir) """
        pass

    def workingDirectory(self): # real signature unknown; restored from __doc__
        """ QAbstractFormBuilder.workingDirectory() -> QDir """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerActionEditorInterface(__PyQt4_QtGui.QWidget):
    """ QDesignerActionEditorInterface(QWidget, Qt.WindowFlags flags=0) """
    def core(self): # real signature unknown; restored from __doc__
        """ QDesignerActionEditorInterface.core() -> QDesignerFormEditorInterface """
        return QDesignerFormEditorInterface

    def manageAction(self, QAction): # real signature unknown; restored from __doc__
        """ QDesignerActionEditorInterface.manageAction(QAction) """
        pass

    def setFormWindow(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ QDesignerActionEditorInterface.setFormWindow(QDesignerFormWindowInterface) """
        pass

    def unmanageAction(self, QAction): # real signature unknown; restored from __doc__
        """ QDesignerActionEditorInterface.unmanageAction(QAction) """
        pass

    def __init__(self, QWidget, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass


class QDesignerContainerExtension(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDesignerContainerExtension()
    QDesignerContainerExtension(QDesignerContainerExtension)
    """
    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QDesignerContainerExtension.addWidget(QWidget) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ QDesignerContainerExtension.count() -> int """
        return 0

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ QDesignerContainerExtension.currentIndex() -> int """
        return 0

    def insertWidget(self, p_int, QWidget): # real signature unknown; restored from __doc__
        """ QDesignerContainerExtension.insertWidget(int, QWidget) """
        pass

    def remove(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerContainerExtension.remove(int) """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerContainerExtension.setCurrentIndex(int) """
        pass

    def widget(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerContainerExtension.widget(int) -> QWidget """
        pass

    def __init__(self, QDesignerContainerExtension=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerCustomWidgetCollectionInterface(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDesignerCustomWidgetCollectionInterface()
    QDesignerCustomWidgetCollectionInterface(QDesignerCustomWidgetCollectionInterface)
    """
    def customWidgets(self): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetCollectionInterface.customWidgets() -> list-of-QDesignerCustomWidgetInterface """
        pass

    def __init__(self, QDesignerCustomWidgetCollectionInterface=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerCustomWidgetInterface(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDesignerCustomWidgetInterface()
    QDesignerCustomWidgetInterface(QDesignerCustomWidgetInterface)
    """
    def codeTemplate(self): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetInterface.codeTemplate() -> QString """
        pass

    def createWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetInterface.createWidget(QWidget) -> QWidget """
        pass

    def domXml(self): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetInterface.domXml() -> QString """
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetInterface.group() -> QString """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetInterface.icon() -> QIcon """
        pass

    def includeFile(self): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetInterface.includeFile() -> QString """
        pass

    def initialize(self, QDesignerFormEditorInterface): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetInterface.initialize(QDesignerFormEditorInterface) """
        pass

    def isContainer(self): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetInterface.isContainer() -> bool """
        return False

    def isInitialized(self): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetInterface.isInitialized() -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetInterface.name() -> QString """
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetInterface.toolTip() -> QString """
        pass

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ QDesignerCustomWidgetInterface.whatsThis() -> QString """
        pass

    def __init__(self, QDesignerCustomWidgetInterface=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerFormEditorInterface(__PyQt4_QtCore.QObject):
    """ QDesignerFormEditorInterface(QObject parent=None) """
    def actionEditor(self): # real signature unknown; restored from __doc__
        """ QDesignerFormEditorInterface.actionEditor() -> QDesignerActionEditorInterface """
        return QDesignerActionEditorInterface

    def extensionManager(self): # real signature unknown; restored from __doc__
        """ QDesignerFormEditorInterface.extensionManager() -> QExtensionManager """
        return QExtensionManager

    def formWindowManager(self): # real signature unknown; restored from __doc__
        """ QDesignerFormEditorInterface.formWindowManager() -> QDesignerFormWindowManagerInterface """
        return QDesignerFormWindowManagerInterface

    def objectInspector(self): # real signature unknown; restored from __doc__
        """ QDesignerFormEditorInterface.objectInspector() -> QDesignerObjectInspectorInterface """
        return QDesignerObjectInspectorInterface

    def propertyEditor(self): # real signature unknown; restored from __doc__
        """ QDesignerFormEditorInterface.propertyEditor() -> QDesignerPropertyEditorInterface """
        return QDesignerPropertyEditorInterface

    def setActionEditor(self, QDesignerActionEditorInterface): # real signature unknown; restored from __doc__
        """ QDesignerFormEditorInterface.setActionEditor(QDesignerActionEditorInterface) """
        pass

    def setObjectInspector(self, QDesignerObjectInspectorInterface): # real signature unknown; restored from __doc__
        """ QDesignerFormEditorInterface.setObjectInspector(QDesignerObjectInspectorInterface) """
        pass

    def setPropertyEditor(self, QDesignerPropertyEditorInterface): # real signature unknown; restored from __doc__
        """ QDesignerFormEditorInterface.setPropertyEditor(QDesignerPropertyEditorInterface) """
        pass

    def setWidgetBox(self, QDesignerWidgetBoxInterface): # real signature unknown; restored from __doc__
        """ QDesignerFormEditorInterface.setWidgetBox(QDesignerWidgetBoxInterface) """
        pass

    def topLevel(self): # real signature unknown; restored from __doc__
        """ QDesignerFormEditorInterface.topLevel() -> QWidget """
        pass

    def widgetBox(self): # real signature unknown; restored from __doc__
        """ QDesignerFormEditorInterface.widgetBox() -> QDesignerWidgetBoxInterface """
        return QDesignerWidgetBoxInterface

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QDesignerFormWindowCursorInterface(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDesignerFormWindowCursorInterface()
    QDesignerFormWindowCursorInterface(QDesignerFormWindowCursorInterface)
    """
    def current(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.current() -> QWidget """
        pass

    def formWindow(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.formWindow() -> QDesignerFormWindowInterface """
        return QDesignerFormWindowInterface

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.hasSelection() -> bool """
        return False

    def isWidgetSelected(self, QWidget): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.isWidgetSelected(QWidget) -> bool """
        return False

    def movePosition(self, QDesignerFormWindowCursorInterface_MoveOperation, QDesignerFormWindowCursorInterface_MoveMode_mode=None): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.movePosition(QDesignerFormWindowCursorInterface.MoveOperation, QDesignerFormWindowCursorInterface.MoveMode mode=QDesignerFormWindowCursorInterface.MoveAnchor) -> bool """
        return False

    def position(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.position() -> int """
        return 0

    def resetWidgetProperty(self, QWidget, QString): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.resetWidgetProperty(QWidget, QString) """
        pass

    def selectedWidget(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.selectedWidget(int) -> QWidget """
        pass

    def selectedWidgetCount(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.selectedWidgetCount() -> int """
        return 0

    def setPosition(self, p_int, QDesignerFormWindowCursorInterface_MoveMode_mode=None): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.setPosition(int, QDesignerFormWindowCursorInterface.MoveMode mode=QDesignerFormWindowCursorInterface.MoveAnchor) """
        pass

    def setProperty(self, QString, QVariant): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.setProperty(QString, QVariant) """
        pass

    def setWidgetProperty(self, QWidget, QString, QVariant): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.setWidgetProperty(QWidget, QString, QVariant) """
        pass

    def widget(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.widget(int) -> QWidget """
        pass

    def widgetCount(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowCursorInterface.widgetCount() -> int """
        return 0

    def __init__(self, QDesignerFormWindowCursorInterface=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Down = 8
    End = 2
    KeepAnchor = 1
    Left = 5
    MoveAnchor = 0
    Next = 3
    NoMove = 0
    Prev = 4
    Right = 6
    Start = 1
    Up = 7


class QDesignerFormWindowInterface(__PyQt4_QtGui.QWidget):
    # no doc
    def aboutToUnmanageWidget(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.aboutToUnmanageWidget[QWidget] [signal] """
        pass

    def absoluteDir(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.absoluteDir() -> QDir """
        pass

    def activated(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.activated[QWidget] [signal] """
        pass

    def addResourceFile(self, QString): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.addResourceFile(QString) """
        pass

    def author(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.author() -> QString """
        pass

    def changed(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.changed [signal] """
        pass

    def clearSelection(self, bool_update=True): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.clearSelection(bool update=True) """
        pass

    def comment(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.comment() -> QString """
        pass

    def contents(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.contents() -> QString """
        pass

    def core(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.core() -> QDesignerFormEditorInterface """
        return QDesignerFormEditorInterface

    def cursor(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.cursor() -> QDesignerFormWindowCursorInterface """
        return QDesignerFormWindowCursorInterface

    def emitSelectionChanged(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.emitSelectionChanged() """
        pass

    def exportMacro(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.exportMacro() -> QString """
        pass

    def featureChanged(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.featureChanged[QDesignerFormWindowInterface.Feature] [signal] """
        pass

    def features(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.features() -> QDesignerFormWindowInterface.Feature """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.fileName() -> QString """
        pass

    def fileNameChanged(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.fileNameChanged[QString] [signal] """
        pass

    def findFormWindow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDesignerFormWindowInterface.findFormWindow(QWidget) -> QDesignerFormWindowInterface
        QDesignerFormWindowInterface.findFormWindow(QObject) -> QDesignerFormWindowInterface
        """
        return QDesignerFormWindowInterface

    def geometryChanged(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.geometryChanged [signal] """
        pass

    def grid(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.grid() -> QPoint """
        pass

    def hasFeature(self, QDesignerFormWindowInterface_Feature): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.hasFeature(QDesignerFormWindowInterface.Feature) -> bool """
        return False

    def includeHints(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.includeHints() -> QStringList """
        pass

    def isDirty(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.isDirty() -> bool """
        return False

    def isManaged(self, QWidget): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.isManaged(QWidget) -> bool """
        return False

    def layoutDefault(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.layoutDefault() -> (int, int) """
        pass

    def layoutFunction(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.layoutFunction() -> (QString, QString) """
        pass

    def mainContainer(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.mainContainer() -> QWidget """
        pass

    def mainContainerChanged(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.mainContainerChanged[QWidget] [signal] """
        pass

    def manageWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.manageWidget(QWidget) """
        pass

    def objectRemoved(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.objectRemoved[QObject] [signal] """
        pass

    def pixmapFunction(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.pixmapFunction() -> QString """
        pass

    def removeResourceFile(self, QString): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.removeResourceFile(QString) """
        pass

    def resourceFiles(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.resourceFiles() -> QStringList """
        pass

    def resourceFilesChanged(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.resourceFilesChanged [signal] """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.selectionChanged [signal] """
        pass

    def selectWidget(self, QWidget, bool_select=True): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.selectWidget(QWidget, bool select=True) """
        pass

    def setAuthor(self, QString): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.setAuthor(QString) """
        pass

    def setComment(self, QString): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.setComment(QString) """
        pass

    def setContents(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDesignerFormWindowInterface.setContents(QIODevice)
        QDesignerFormWindowInterface.setContents(QString)
        """
        pass

    def setDirty(self, bool): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.setDirty(bool) """
        pass

    def setExportMacro(self, QString): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.setExportMacro(QString) """
        pass

    def setFeatures(self, QDesignerFormWindowInterface_Feature): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.setFeatures(QDesignerFormWindowInterface.Feature) """
        pass

    def setFileName(self, QString): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.setFileName(QString) """
        pass

    def setGrid(self, QPoint): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.setGrid(QPoint) """
        pass

    def setIncludeHints(self, QStringList): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.setIncludeHints(QStringList) """
        pass

    def setLayoutDefault(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.setLayoutDefault(int, int) """
        pass

    def setLayoutFunction(self, QString, QString_1): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.setLayoutFunction(QString, QString) """
        pass

    def setMainContainer(self, QWidget): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.setMainContainer(QWidget) """
        pass

    def setPixmapFunction(self, QString): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.setPixmapFunction(QString) """
        pass

    def unmanageWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowInterface.unmanageWidget(QWidget) """
        pass

    def widgetManaged(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.widgetManaged[QWidget] [signal] """
        pass

    def widgetRemoved(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.widgetRemoved[QWidget] [signal] """
        pass

    def widgetUnmanaged(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowInterface.widgetUnmanaged[QWidget] [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    DefaultFeature = 3
    EditFeature = 1
    GridFeature = 2
    TabOrderFeature = 4


class QDesignerFormWindowManagerInterface(__PyQt4_QtCore.QObject):
    # no doc
    def actionAdjustSize(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionAdjustSize() -> QAction """
        pass

    def actionBreakLayout(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionBreakLayout() -> QAction """
        pass

    def actionCopy(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionCopy() -> QAction """
        pass

    def actionCut(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionCut() -> QAction """
        pass

    def actionDelete(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionDelete() -> QAction """
        pass

    def actionFormLayout(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionFormLayout() -> QAction """
        pass

    def actionGridLayout(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionGridLayout() -> QAction """
        pass

    def actionHorizontalLayout(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionHorizontalLayout() -> QAction """
        pass

    def actionLower(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionLower() -> QAction """
        pass

    def actionPaste(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionPaste() -> QAction """
        pass

    def actionRaise(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionRaise() -> QAction """
        pass

    def actionRedo(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionRedo() -> QAction """
        pass

    def actionSelectAll(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionSelectAll() -> QAction """
        pass

    def actionSimplifyLayout(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionSimplifyLayout() -> QAction """
        pass

    def actionSplitHorizontal(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionSplitHorizontal() -> QAction """
        pass

    def actionSplitVertical(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionSplitVertical() -> QAction """
        pass

    def actionUndo(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionUndo() -> QAction """
        pass

    def actionVerticalLayout(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.actionVerticalLayout() -> QAction """
        pass

    def activeFormWindow(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.activeFormWindow() -> QDesignerFormWindowInterface """
        return QDesignerFormWindowInterface

    def activeFormWindowChanged(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowManagerInterface.activeFormWindowChanged[QDesignerFormWindowInterface] [signal] """
        pass

    def addFormWindow(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.addFormWindow(QDesignerFormWindowInterface) """
        pass

    def core(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.core() -> QDesignerFormEditorInterface """
        return QDesignerFormEditorInterface

    def createFormWindow(self, QWidget_parent=None, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.createFormWindow(QWidget parent=None, Qt.WindowFlags flags=0) -> QDesignerFormWindowInterface """
        return QDesignerFormWindowInterface

    def formWindow(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.formWindow(int) -> QDesignerFormWindowInterface """
        return QDesignerFormWindowInterface

    def formWindowAdded(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowManagerInterface.formWindowAdded[QDesignerFormWindowInterface] [signal] """
        pass

    def formWindowCount(self): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.formWindowCount() -> int """
        return 0

    def formWindowRemoved(self, *args, **kwargs): # real signature unknown
        """ QDesignerFormWindowManagerInterface.formWindowRemoved[QDesignerFormWindowInterface] [signal] """
        pass

    def removeFormWindow(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.removeFormWindow(QDesignerFormWindowInterface) """
        pass

    def setActiveFormWindow(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ QDesignerFormWindowManagerInterface.setActiveFormWindow(QDesignerFormWindowInterface) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QDesignerMemberSheetExtension(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDesignerMemberSheetExtension()
    QDesignerMemberSheetExtension(QDesignerMemberSheetExtension)
    """
    def count(self): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.count() -> int """
        return 0

    def declaredInClass(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.declaredInClass(int) -> QString """
        pass

    def indexOf(self, QString): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.indexOf(QString) -> int """
        return 0

    def inheritedFromWidget(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.inheritedFromWidget(int) -> bool """
        return False

    def isSignal(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.isSignal(int) -> bool """
        return False

    def isSlot(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.isSlot(int) -> bool """
        return False

    def isVisible(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.isVisible(int) -> bool """
        return False

    def memberGroup(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.memberGroup(int) -> QString """
        pass

    def memberName(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.memberName(int) -> QString """
        pass

    def parameterNames(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.parameterNames(int) -> list-of-QByteArray """
        pass

    def parameterTypes(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.parameterTypes(int) -> list-of-QByteArray """
        pass

    def setMemberGroup(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.setMemberGroup(int, QString) """
        pass

    def setVisible(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.setVisible(int, bool) """
        pass

    def signature(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerMemberSheetExtension.signature(int) -> QString """
        pass

    def __init__(self, QDesignerMemberSheetExtension=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerObjectInspectorInterface(__PyQt4_QtGui.QWidget):
    """ QDesignerObjectInspectorInterface(QWidget, Qt.WindowFlags flags=0) """
    def core(self): # real signature unknown; restored from __doc__
        """ QDesignerObjectInspectorInterface.core() -> QDesignerFormEditorInterface """
        return QDesignerFormEditorInterface

    def setFormWindow(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ QDesignerObjectInspectorInterface.setFormWindow(QDesignerFormWindowInterface) """
        pass

    def __init__(self, QWidget, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass


class QDesignerPropertyEditorInterface(__PyQt4_QtGui.QWidget):
    """ QDesignerPropertyEditorInterface(QWidget, Qt.WindowFlags flags=0) """
    def core(self): # real signature unknown; restored from __doc__
        """ QDesignerPropertyEditorInterface.core() -> QDesignerFormEditorInterface """
        return QDesignerFormEditorInterface

    def currentPropertyName(self): # real signature unknown; restored from __doc__
        """ QDesignerPropertyEditorInterface.currentPropertyName() -> QString """
        pass

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ QDesignerPropertyEditorInterface.isReadOnly() -> bool """
        return False

    def object(self): # real signature unknown; restored from __doc__
        """ QDesignerPropertyEditorInterface.object() -> QObject """
        pass

    def propertyChanged(self, *args, **kwargs): # real signature unknown
        """ QDesignerPropertyEditorInterface.propertyChanged[QString, QVariant] [signal] """
        pass

    def setObject(self, QObject): # real signature unknown; restored from __doc__
        """ QDesignerPropertyEditorInterface.setObject(QObject) """
        pass

    def setPropertyValue(self, QString, QVariant, bool_changed=True): # real signature unknown; restored from __doc__
        """ QDesignerPropertyEditorInterface.setPropertyValue(QString, QVariant, bool changed=True) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ QDesignerPropertyEditorInterface.setReadOnly(bool) """
        pass

    def __init__(self, QWidget, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass


class QDesignerPropertySheetExtension(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDesignerPropertySheetExtension()
    QDesignerPropertySheetExtension(QDesignerPropertySheetExtension)
    """
    def count(self): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.count() -> int """
        return 0

    def hasReset(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.hasReset(int) -> bool """
        return False

    def indexOf(self, QString): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.indexOf(QString) -> int """
        return 0

    def isAttribute(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.isAttribute(int) -> bool """
        return False

    def isChanged(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.isChanged(int) -> bool """
        return False

    def isVisible(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.isVisible(int) -> bool """
        return False

    def property(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.property(int) -> QVariant """
        pass

    def propertyGroup(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.propertyGroup(int) -> QString """
        pass

    def propertyName(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.propertyName(int) -> QString """
        pass

    def reset(self, p_int): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.reset(int) -> bool """
        return False

    def setAttribute(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.setAttribute(int, bool) """
        pass

    def setChanged(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.setChanged(int, bool) """
        pass

    def setProperty(self, p_int, QVariant): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.setProperty(int, QVariant) """
        pass

    def setPropertyGroup(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.setPropertyGroup(int, QString) """
        pass

    def setVisible(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QDesignerPropertySheetExtension.setVisible(int, bool) """
        pass

    def __init__(self, QDesignerPropertySheetExtension=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerTaskMenuExtension(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QDesignerTaskMenuExtension()
    QDesignerTaskMenuExtension(QDesignerTaskMenuExtension)
    """
    def preferredEditAction(self): # real signature unknown; restored from __doc__
        """ QDesignerTaskMenuExtension.preferredEditAction() -> QAction """
        pass

    def taskActions(self): # real signature unknown; restored from __doc__
        """ QDesignerTaskMenuExtension.taskActions() -> list-of-QAction """
        pass

    def __init__(self, QDesignerTaskMenuExtension=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerWidgetBoxInterface(__PyQt4_QtGui.QWidget):
    # no doc
    def fileName(self): # real signature unknown; restored from __doc__
        """ QDesignerWidgetBoxInterface.fileName() -> QString """
        pass

    def load(self): # real signature unknown; restored from __doc__
        """ QDesignerWidgetBoxInterface.load() -> bool """
        return False

    def save(self): # real signature unknown; restored from __doc__
        """ QDesignerWidgetBoxInterface.save() -> bool """
        return False

    def setFileName(self, QString): # real signature unknown; restored from __doc__
        """ QDesignerWidgetBoxInterface.setFileName(QString) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QExtensionFactory(__PyQt4_QtCore.QObject, QAbstractExtensionFactory):
    """ QExtensionFactory(QExtensionManager parent=None) """
    def createExtension(self, QObject, QString, QObject_1): # real signature unknown; restored from __doc__
        """ QExtensionFactory.createExtension(QObject, QString, QObject) -> QObject """
        pass

    def extension(self, QObject, QString): # real signature unknown; restored from __doc__
        """ QExtensionFactory.extension(QObject, QString) -> QObject """
        pass

    def extensionManager(self): # real signature unknown; restored from __doc__
        """ QExtensionFactory.extensionManager() -> QExtensionManager """
        return QExtensionManager

    def __init__(self, QExtensionManager_parent=None): # real signature unknown; restored from __doc__
        pass


class QExtensionManager(__PyQt4_QtCore.QObject, QAbstractExtensionManager):
    """ QExtensionManager(QObject parent=None) """
    def extension(self, QObject, QString): # real signature unknown; restored from __doc__
        """ QExtensionManager.extension(QObject, QString) -> QObject """
        pass

    def registerExtensions(self, QAbstractExtensionFactory, QString_iid=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QExtensionManager.registerExtensions(QAbstractExtensionFactory, QString iid=QString()) """
        pass

    def unregisterExtensions(self, QAbstractExtensionFactory, QString_iid=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QExtensionManager.unregisterExtensions(QAbstractExtensionFactory, QString iid=QString()) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QFormBuilder(QAbstractFormBuilder):
    """ QFormBuilder() """
    def addPluginPath(self, QString): # real signature unknown; restored from __doc__
        """ QFormBuilder.addPluginPath(QString) """
        pass

    def clearPluginPaths(self): # real signature unknown; restored from __doc__
        """ QFormBuilder.clearPluginPaths() """
        pass

    def customWidgets(self): # real signature unknown; restored from __doc__
        """ QFormBuilder.customWidgets() -> list-of-QDesignerCustomWidgetInterface """
        pass

    def pluginPaths(self): # real signature unknown; restored from __doc__
        """ QFormBuilder.pluginPaths() -> QStringList """
        pass

    def setPluginPath(self, QStringList): # real signature unknown; restored from __doc__
        """ QFormBuilder.setPluginPath(QStringList) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


class QPyDesignerContainerExtension(__PyQt4_QtCore.QObject, QDesignerContainerExtension):
    """ QPyDesignerContainerExtension(QObject) """
    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


class QPyDesignerCustomWidgetCollectionPlugin(__PyQt4_QtCore.QObject, QDesignerCustomWidgetCollectionInterface):
    """ QPyDesignerCustomWidgetCollectionPlugin(QObject parent=None) """
    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QPyDesignerCustomWidgetPlugin(__PyQt4_QtCore.QObject, QDesignerCustomWidgetInterface):
    """ QPyDesignerCustomWidgetPlugin(QObject parent=None) """
    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QPyDesignerMemberSheetExtension(__PyQt4_QtCore.QObject, QDesignerMemberSheetExtension):
    """ QPyDesignerMemberSheetExtension(QObject) """
    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


class QPyDesignerPropertySheetExtension(__PyQt4_QtCore.QObject, QDesignerPropertySheetExtension):
    """ QPyDesignerPropertySheetExtension(QObject) """
    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


class QPyDesignerTaskMenuExtension(__PyQt4_QtCore.QObject, QDesignerTaskMenuExtension):
    """ QPyDesignerTaskMenuExtension(QObject) """
    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


