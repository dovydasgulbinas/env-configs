# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QFrame import QFrame

class QSplitter(QFrame):
    """
    QSplitter(QWidget parent=None)
    QSplitter(Qt.Orientation, QWidget parent=None)
    """
    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QSplitter.addWidget(QWidget) """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QSplitter.changeEvent(QEvent) """
        pass

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ QSplitter.childEvent(QChildEvent) """
        pass

    def childrenCollapsible(self): # real signature unknown; restored from __doc__
        """ QSplitter.childrenCollapsible() -> bool """
        return False

    def closestLegalPosition(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QSplitter.closestLegalPosition(int, int) -> int """
        return 0

    def count(self): # real signature unknown; restored from __doc__
        """ QSplitter.count() -> int """
        return 0

    def createHandle(self): # real signature unknown; restored from __doc__
        """ QSplitter.createHandle() -> QSplitterHandle """
        return QSplitterHandle

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QSplitter.event(QEvent) -> bool """
        return False

    def getRange(self, p_int): # real signature unknown; restored from __doc__
        """ QSplitter.getRange(int) -> (int, int) """
        pass

    def handle(self, p_int): # real signature unknown; restored from __doc__
        """ QSplitter.handle(int) -> QSplitterHandle """
        return QSplitterHandle

    def handleWidth(self): # real signature unknown; restored from __doc__
        """ QSplitter.handleWidth() -> int """
        return 0

    def indexOf(self, QWidget): # real signature unknown; restored from __doc__
        """ QSplitter.indexOf(QWidget) -> int """
        return 0

    def insertWidget(self, p_int, QWidget): # real signature unknown; restored from __doc__
        """ QSplitter.insertWidget(int, QWidget) """
        pass

    def isCollapsible(self, p_int): # real signature unknown; restored from __doc__
        """ QSplitter.isCollapsible(int) -> bool """
        return False

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QSplitter.minimumSizeHint() -> QSize """
        pass

    def moveSplitter(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QSplitter.moveSplitter(int, int) """
        pass

    def opaqueResize(self): # real signature unknown; restored from __doc__
        """ QSplitter.opaqueResize() -> bool """
        return False

    def orientation(self): # real signature unknown; restored from __doc__
        """ QSplitter.orientation() -> Qt.Orientation """
        pass

    def refresh(self): # real signature unknown; restored from __doc__
        """ QSplitter.refresh() """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QSplitter.resizeEvent(QResizeEvent) """
        pass

    def restoreState(self, QByteArray): # real signature unknown; restored from __doc__
        """ QSplitter.restoreState(QByteArray) -> bool """
        return False

    def saveState(self): # real signature unknown; restored from __doc__
        """ QSplitter.saveState() -> QByteArray """
        pass

    def setChildrenCollapsible(self, bool): # real signature unknown; restored from __doc__
        """ QSplitter.setChildrenCollapsible(bool) """
        pass

    def setCollapsible(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QSplitter.setCollapsible(int, bool) """
        pass

    def setHandleWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QSplitter.setHandleWidth(int) """
        pass

    def setOpaqueResize(self, bool_opaque=True): # real signature unknown; restored from __doc__
        """ QSplitter.setOpaqueResize(bool opaque=True) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QSplitter.setOrientation(Qt.Orientation) """
        pass

    def setRubberBand(self, p_int): # real signature unknown; restored from __doc__
        """ QSplitter.setRubberBand(int) """
        pass

    def setSizes(self, list_of_int): # real signature unknown; restored from __doc__
        """ QSplitter.setSizes(list-of-int) """
        pass

    def setStretchFactor(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QSplitter.setStretchFactor(int, int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QSplitter.sizeHint() -> QSize """
        pass

    def sizes(self): # real signature unknown; restored from __doc__
        """ QSplitter.sizes() -> list-of-int """
        pass

    def splitterMoved(self, *args, **kwargs): # real signature unknown
        """ QSplitter.splitterMoved[int, int] [signal] """
        pass

    def widget(self, p_int): # real signature unknown; restored from __doc__
        """ QSplitter.widget(int) -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass


