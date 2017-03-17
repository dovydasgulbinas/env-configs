# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QPrintPreviewWidget(QWidget):
    """
    QPrintPreviewWidget(QPrinter, QWidget parent=None, Qt.WindowFlags flags=0)
    QPrintPreviewWidget(QWidget parent=None, Qt.WindowFlags flags=0)
    """
    def currentPage(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.currentPage() -> int """
        return 0

    def fitInView(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.fitInView() """
        pass

    def fitToWidth(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.fitToWidth() """
        pass

    def numPages(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.numPages() -> int """
        return 0

    def orientation(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.orientation() -> QPrinter.Orientation """
        pass

    def pageCount(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.pageCount() -> int """
        return 0

    def paintRequested(self, *args, **kwargs): # real signature unknown
        """ QPrintPreviewWidget.paintRequested[QPrinter] [signal] """
        pass

    def previewChanged(self, *args, **kwargs): # real signature unknown
        """ QPrintPreviewWidget.previewChanged [signal] """
        pass

    def print_(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.print_() """
        pass

    def setAllPagesViewMode(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.setAllPagesViewMode() """
        pass

    def setCurrentPage(self, p_int): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.setCurrentPage(int) """
        pass

    def setFacingPagesViewMode(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.setFacingPagesViewMode() """
        pass

    def setLandscapeOrientation(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.setLandscapeOrientation() """
        pass

    def setOrientation(self, QPrinter_Orientation): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.setOrientation(QPrinter.Orientation) """
        pass

    def setPortraitOrientation(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.setPortraitOrientation() """
        pass

    def setSinglePageViewMode(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.setSinglePageViewMode() """
        pass

    def setViewMode(self, QPrintPreviewWidget_ViewMode): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.setViewMode(QPrintPreviewWidget.ViewMode) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.setVisible(bool) """
        pass

    def setZoomFactor(self, p_float): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.setZoomFactor(float) """
        pass

    def setZoomMode(self, QPrintPreviewWidget_ZoomMode): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.setZoomMode(QPrintPreviewWidget.ZoomMode) """
        pass

    def updatePreview(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.updatePreview() """
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.viewMode() -> QPrintPreviewWidget.ViewMode """
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.zoomFactor() -> float """
        return 0.0

    def zoomIn(self, float_factor=1.1): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.zoomIn(float factor=1.1) """
        pass

    def zoomMode(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.zoomMode() -> QPrintPreviewWidget.ZoomMode """
        pass

    def zoomOut(self, float_factor=1.1): # real signature unknown; restored from __doc__
        """ QPrintPreviewWidget.zoomOut(float factor=1.1) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllPagesView = 2
    CustomZoom = 0
    FacingPagesView = 1
    FitInView = 2
    FitToWidth = 1
    SinglePageView = 0


