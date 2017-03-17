# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QPaintDevice import QPaintDevice

class QPrinter(QPaintDevice):
    """
    QPrinter(QPrinter.PrinterMode mode=QPrinter.ScreenResolution)
    QPrinter(QPrinterInfo, QPrinter.PrinterMode mode=QPrinter.ScreenResolution)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ QPrinter.abort() -> bool """
        return False

    def actualNumCopies(self): # real signature unknown; restored from __doc__
        """ QPrinter.actualNumCopies() -> int """
        return 0

    def collateCopies(self): # real signature unknown; restored from __doc__
        """ QPrinter.collateCopies() -> bool """
        return False

    def colorMode(self): # real signature unknown; restored from __doc__
        """ QPrinter.colorMode() -> QPrinter.ColorMode """
        pass

    def copyCount(self): # real signature unknown; restored from __doc__
        """ QPrinter.copyCount() -> int """
        return 0

    def creator(self): # real signature unknown; restored from __doc__
        """ QPrinter.creator() -> QString """
        pass

    def docName(self): # real signature unknown; restored from __doc__
        """ QPrinter.docName() -> QString """
        pass

    def doubleSidedPrinting(self): # real signature unknown; restored from __doc__
        """ QPrinter.doubleSidedPrinting() -> bool """
        return False

    def duplex(self): # real signature unknown; restored from __doc__
        """ QPrinter.duplex() -> QPrinter.DuplexMode """
        pass

    def fontEmbeddingEnabled(self): # real signature unknown; restored from __doc__
        """ QPrinter.fontEmbeddingEnabled() -> bool """
        return False

    def fromPage(self): # real signature unknown; restored from __doc__
        """ QPrinter.fromPage() -> int """
        return 0

    def fullPage(self): # real signature unknown; restored from __doc__
        """ QPrinter.fullPage() -> bool """
        return False

    def getPageMargins(self, QPrinter_Unit): # real signature unknown; restored from __doc__
        """ QPrinter.getPageMargins(QPrinter.Unit) -> (float, float, float, float) """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ QPrinter.isValid() -> bool """
        return False

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ QPrinter.metric(QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def newPage(self): # real signature unknown; restored from __doc__
        """ QPrinter.newPage() -> bool """
        return False

    def numCopies(self): # real signature unknown; restored from __doc__
        """ QPrinter.numCopies() -> int """
        return 0

    def orientation(self): # real signature unknown; restored from __doc__
        """ QPrinter.orientation() -> QPrinter.Orientation """
        pass

    def outputFileName(self): # real signature unknown; restored from __doc__
        """ QPrinter.outputFileName() -> QString """
        pass

    def outputFormat(self): # real signature unknown; restored from __doc__
        """ QPrinter.outputFormat() -> QPrinter.OutputFormat """
        pass

    def pageOrder(self): # real signature unknown; restored from __doc__
        """ QPrinter.pageOrder() -> QPrinter.PageOrder """
        pass

    def pageRect(self, QPrinter_Unit=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPrinter.pageRect() -> QRect
        QPrinter.pageRect(QPrinter.Unit) -> QRectF
        """
        pass

    def pageSize(self): # real signature unknown; restored from __doc__
        """ QPrinter.pageSize() -> QPrinter.PageSize """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ QPrinter.paintEngine() -> QPaintEngine """
        return QPaintEngine

    def paperRect(self, QPrinter_Unit=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPrinter.paperRect() -> QRect
        QPrinter.paperRect(QPrinter.Unit) -> QRectF
        """
        pass

    def paperSize(self, QPrinter_Unit=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPrinter.paperSize() -> QPrinter.PageSize
        QPrinter.paperSize(QPrinter.Unit) -> QSizeF
        """
        pass

    def paperSource(self): # real signature unknown; restored from __doc__
        """ QPrinter.paperSource() -> QPrinter.PaperSource """
        pass

    def printEngine(self): # real signature unknown; restored from __doc__
        """ QPrinter.printEngine() -> QPrintEngine """
        return QPrintEngine

    def printerName(self): # real signature unknown; restored from __doc__
        """ QPrinter.printerName() -> QString """
        pass

    def printerSelectionOption(self): # real signature unknown; restored from __doc__
        """ QPrinter.printerSelectionOption() -> QString """
        pass

    def printerState(self): # real signature unknown; restored from __doc__
        """ QPrinter.printerState() -> QPrinter.PrinterState """
        pass

    def printProgram(self): # real signature unknown; restored from __doc__
        """ QPrinter.printProgram() -> QString """
        pass

    def printRange(self): # real signature unknown; restored from __doc__
        """ QPrinter.printRange() -> QPrinter.PrintRange """
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ QPrinter.resolution() -> int """
        return 0

    def setCollateCopies(self, bool): # real signature unknown; restored from __doc__
        """ QPrinter.setCollateCopies(bool) """
        pass

    def setColorMode(self, QPrinter_ColorMode): # real signature unknown; restored from __doc__
        """ QPrinter.setColorMode(QPrinter.ColorMode) """
        pass

    def setCopyCount(self, p_int): # real signature unknown; restored from __doc__
        """ QPrinter.setCopyCount(int) """
        pass

    def setCreator(self, QString): # real signature unknown; restored from __doc__
        """ QPrinter.setCreator(QString) """
        pass

    def setDocName(self, QString): # real signature unknown; restored from __doc__
        """ QPrinter.setDocName(QString) """
        pass

    def setDoubleSidedPrinting(self, bool): # real signature unknown; restored from __doc__
        """ QPrinter.setDoubleSidedPrinting(bool) """
        pass

    def setDuplex(self, QPrinter_DuplexMode): # real signature unknown; restored from __doc__
        """ QPrinter.setDuplex(QPrinter.DuplexMode) """
        pass

    def setEngines(self, QPrintEngine, QPaintEngine): # real signature unknown; restored from __doc__
        """ QPrinter.setEngines(QPrintEngine, QPaintEngine) """
        pass

    def setFontEmbeddingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QPrinter.setFontEmbeddingEnabled(bool) """
        pass

    def setFromTo(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QPrinter.setFromTo(int, int) """
        pass

    def setFullPage(self, bool): # real signature unknown; restored from __doc__
        """ QPrinter.setFullPage(bool) """
        pass

    def setNumCopies(self, p_int): # real signature unknown; restored from __doc__
        """ QPrinter.setNumCopies(int) """
        pass

    def setOrientation(self, QPrinter_Orientation): # real signature unknown; restored from __doc__
        """ QPrinter.setOrientation(QPrinter.Orientation) """
        pass

    def setOutputFileName(self, QString): # real signature unknown; restored from __doc__
        """ QPrinter.setOutputFileName(QString) """
        pass

    def setOutputFormat(self, QPrinter_OutputFormat): # real signature unknown; restored from __doc__
        """ QPrinter.setOutputFormat(QPrinter.OutputFormat) """
        pass

    def setPageMargins(self, p_float, p_float_1, p_float_2, p_float_3, QPrinter_Unit): # real signature unknown; restored from __doc__
        """ QPrinter.setPageMargins(float, float, float, float, QPrinter.Unit) """
        pass

    def setPageOrder(self, QPrinter_PageOrder): # real signature unknown; restored from __doc__
        """ QPrinter.setPageOrder(QPrinter.PageOrder) """
        pass

    def setPageSize(self, QPrinter_PageSize): # real signature unknown; restored from __doc__
        """ QPrinter.setPageSize(QPrinter.PageSize) """
        pass

    def setPaperSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPrinter.setPaperSize(QPrinter.PageSize)
        QPrinter.setPaperSize(QSizeF, QPrinter.Unit)
        """
        pass

    def setPaperSource(self, QPrinter_PaperSource): # real signature unknown; restored from __doc__
        """ QPrinter.setPaperSource(QPrinter.PaperSource) """
        pass

    def setPrinterName(self, QString): # real signature unknown; restored from __doc__
        """ QPrinter.setPrinterName(QString) """
        pass

    def setPrinterSelectionOption(self, QString): # real signature unknown; restored from __doc__
        """ QPrinter.setPrinterSelectionOption(QString) """
        pass

    def setPrintProgram(self, QString): # real signature unknown; restored from __doc__
        """ QPrinter.setPrintProgram(QString) """
        pass

    def setPrintRange(self, QPrinter_PrintRange): # real signature unknown; restored from __doc__
        """ QPrinter.setPrintRange(QPrinter.PrintRange) """
        pass

    def setResolution(self, p_int): # real signature unknown; restored from __doc__
        """ QPrinter.setResolution(int) """
        pass

    def supportedResolutions(self): # real signature unknown; restored from __doc__
        """ QPrinter.supportedResolutions() -> list-of-int """
        pass

    def supportsMultipleCopies(self): # real signature unknown; restored from __doc__
        """ QPrinter.supportsMultipleCopies() -> bool """
        return False

    def toPage(self): # real signature unknown; restored from __doc__
        """ QPrinter.toPage() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    A0 = 5
    A1 = 6
    A2 = 7
    A3 = 8
    A4 = 0
    A5 = 9
    A6 = 10
    A7 = 11
    A8 = 12
    A9 = 13
    Aborted = 2
    Active = 1
    AllPages = 0
    Auto = 6
    B0 = 14
    B1 = 15
    B10 = 16
    B2 = 17
    B3 = 18
    B4 = 19
    B5 = 1
    B6 = 20
    B7 = 21
    B8 = 22
    B9 = 23
    C5E = 24
    Cassette = 11
    Cicero = 5
    Color = 1
    Comm10E = 25
    CurrentPage = 3
    Custom = 30
    DevicePixel = 6
    Didot = 4
    DLE = 26
    DuplexAuto = 1
    DuplexLongSide = 2
    DuplexNone = 0
    DuplexShortSide = 3
    Envelope = 4
    EnvelopeManual = 5
    Error = 3
    Executive = 4
    FirstPageFirst = 0
    Folio = 27
    FormSource = 12
    GrayScale = 0
    HighResolution = 2
    Idle = 0
    Inch = 2
    Landscape = 1
    LargeCapacity = 10
    LargeFormat = 9
    LastPageFirst = 1
    Ledger = 28
    Legal = 3
    Letter = 2
    Lower = 1
    Manual = 3
    MaxPageSource = 13
    Middle = 2
    Millimeter = 0
    NativeFormat = 0
    OnlyOne = 0
    PageRange = 2
    PdfFormat = 1
    Pica = 3
    Point = 1
    Portrait = 0
    PostScriptFormat = 2
    PrinterResolution = 1
    ScreenResolution = 0
    Selection = 1
    SmallFormat = 8
    Tabloid = 29
    Tractor = 7


