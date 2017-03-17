# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QPrintEngine(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QPrintEngine()
    QPrintEngine(QPrintEngine)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ QPrintEngine.abort() -> bool """
        return False

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ QPrintEngine.metric(QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def newPage(self): # real signature unknown; restored from __doc__
        """ QPrintEngine.newPage() -> bool """
        return False

    def printerState(self): # real signature unknown; restored from __doc__
        """ QPrintEngine.printerState() -> QPrinter.PrinterState """
        pass

    def property(self, QPrintEngine_PrintEnginePropertyKey): # real signature unknown; restored from __doc__
        """ QPrintEngine.property(QPrintEngine.PrintEnginePropertyKey) -> QVariant """
        pass

    def setProperty(self, QPrintEngine_PrintEnginePropertyKey, QVariant): # real signature unknown; restored from __doc__
        """ QPrintEngine.setProperty(QPrintEngine.PrintEnginePropertyKey, QVariant) """
        pass

    def __init__(self, QPrintEngine=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    PPK_CollateCopies = 0
    PPK_ColorMode = 1
    PPK_CopyCount = 25
    PPK_Creator = 2
    PPK_CustomBase = 65280
    PPK_CustomPaperSize = 23
    PPK_DocumentName = 3
    PPK_Duplex = 21
    PPK_FontEmbedding = 19
    PPK_FullPage = 4
    PPK_NumberOfCopies = 5
    PPK_Orientation = 6
    PPK_OutputFileName = 7
    PPK_PageMargins = 24
    PPK_PageOrder = 8
    PPK_PageRect = 9
    PPK_PageSize = 10
    PPK_PaperRect = 11
    PPK_PaperSize = 10
    PPK_PaperSource = 12
    PPK_PaperSources = 22
    PPK_PrinterName = 13
    PPK_PrinterProgram = 14
    PPK_Resolution = 15
    PPK_SelectionOption = 16
    PPK_SupportedResolutions = 17
    PPK_SupportsMultipleCopies = 26
    PPK_SuppressSystemPrintStatus = 20
    PPK_WindowsPageSize = 18


