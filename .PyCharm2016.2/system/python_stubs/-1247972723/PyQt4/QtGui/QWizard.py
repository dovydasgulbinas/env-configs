# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QWizard(QDialog):
    """ QWizard(QWidget parent=None, Qt.WindowFlags flags=0) """
    def addPage(self, QWizardPage): # real signature unknown; restored from __doc__
        """ QWizard.addPage(QWizardPage) -> int """
        return 0

    def back(self): # real signature unknown; restored from __doc__
        """ QWizard.back() """
        pass

    def button(self, QWizard_WizardButton): # real signature unknown; restored from __doc__
        """ QWizard.button(QWizard.WizardButton) -> QAbstractButton """
        return QAbstractButton

    def buttonText(self, QWizard_WizardButton): # real signature unknown; restored from __doc__
        """ QWizard.buttonText(QWizard.WizardButton) -> QString """
        pass

    def cleanupPage(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.cleanupPage(int) """
        pass

    def currentId(self): # real signature unknown; restored from __doc__
        """ QWizard.currentId() -> int """
        return 0

    def currentIdChanged(self, *args, **kwargs): # real signature unknown
        """ QWizard.currentIdChanged[int] [signal] """
        pass

    def currentPage(self): # real signature unknown; restored from __doc__
        """ QWizard.currentPage() -> QWizardPage """
        return QWizardPage

    def customButtonClicked(self, *args, **kwargs): # real signature unknown
        """ QWizard.customButtonClicked[int] [signal] """
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.done(int) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QWizard.event(QEvent) -> bool """
        return False

    def field(self, QString): # real signature unknown; restored from __doc__
        """ QWizard.field(QString) -> QVariant """
        pass

    def hasVisitedPage(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.hasVisitedPage(int) -> bool """
        return False

    def helpRequested(self, *args, **kwargs): # real signature unknown
        """ QWizard.helpRequested [signal] """
        pass

    def initializePage(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.initializePage(int) """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ QWizard.next() """
        pass

    def nextId(self): # real signature unknown; restored from __doc__
        """ QWizard.nextId() -> int """
        return 0

    def options(self): # real signature unknown; restored from __doc__
        """ QWizard.options() -> QWizard.WizardOptions """
        pass

    def page(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.page(int) -> QWizardPage """
        return QWizardPage

    def pageAdded(self, *args, **kwargs): # real signature unknown
        """ QWizard.pageAdded[int] [signal] """
        pass

    def pageIds(self): # real signature unknown; restored from __doc__
        """ QWizard.pageIds() -> list-of-int """
        pass

    def pageRemoved(self, *args, **kwargs): # real signature unknown
        """ QWizard.pageRemoved[int] [signal] """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QWizard.paintEvent(QPaintEvent) """
        pass

    def pixmap(self, QWizard_WizardPixmap): # real signature unknown; restored from __doc__
        """ QWizard.pixmap(QWizard.WizardPixmap) -> QPixmap """
        return QPixmap

    def removePage(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.removePage(int) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QWizard.resizeEvent(QResizeEvent) """
        pass

    def restart(self): # real signature unknown; restored from __doc__
        """ QWizard.restart() """
        pass

    def setButton(self, QWizard_WizardButton, QAbstractButton): # real signature unknown; restored from __doc__
        """ QWizard.setButton(QWizard.WizardButton, QAbstractButton) """
        pass

    def setButtonLayout(self, list_of_QWizard_WizardButton): # real signature unknown; restored from __doc__
        """ QWizard.setButtonLayout(list-of-QWizard.WizardButton) """
        pass

    def setButtonText(self, QWizard_WizardButton, QString): # real signature unknown; restored from __doc__
        """ QWizard.setButtonText(QWizard.WizardButton, QString) """
        pass

    def setDefaultProperty(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ QWizard.setDefaultProperty(str, str, str) """
        pass

    def setField(self, QString, QVariant): # real signature unknown; restored from __doc__
        """ QWizard.setField(QString, QVariant) """
        pass

    def setOption(self, QWizard_WizardOption, bool_on=True): # real signature unknown; restored from __doc__
        """ QWizard.setOption(QWizard.WizardOption, bool on=True) """
        pass

    def setOptions(self, QWizard_WizardOptions): # real signature unknown; restored from __doc__
        """ QWizard.setOptions(QWizard.WizardOptions) """
        pass

    def setPage(self, p_int, QWizardPage): # real signature unknown; restored from __doc__
        """ QWizard.setPage(int, QWizardPage) """
        pass

    def setPixmap(self, QWizard_WizardPixmap, QPixmap): # real signature unknown; restored from __doc__
        """ QWizard.setPixmap(QWizard.WizardPixmap, QPixmap) """
        pass

    def setSideWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QWizard.setSideWidget(QWidget) """
        pass

    def setStartId(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.setStartId(int) """
        pass

    def setSubTitleFormat(self, Qt_TextFormat): # real signature unknown; restored from __doc__
        """ QWizard.setSubTitleFormat(Qt.TextFormat) """
        pass

    def setTitleFormat(self, Qt_TextFormat): # real signature unknown; restored from __doc__
        """ QWizard.setTitleFormat(Qt.TextFormat) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QWizard.setVisible(bool) """
        pass

    def setWizardStyle(self, QWizard_WizardStyle): # real signature unknown; restored from __doc__
        """ QWizard.setWizardStyle(QWizard.WizardStyle) """
        pass

    def sideWidget(self): # real signature unknown; restored from __doc__
        """ QWizard.sideWidget() -> QWidget """
        return QWidget

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QWizard.sizeHint() -> QSize """
        pass

    def startId(self): # real signature unknown; restored from __doc__
        """ QWizard.startId() -> int """
        return 0

    def subTitleFormat(self): # real signature unknown; restored from __doc__
        """ QWizard.subTitleFormat() -> Qt.TextFormat """
        pass

    def testOption(self, QWizard_WizardOption): # real signature unknown; restored from __doc__
        """ QWizard.testOption(QWizard.WizardOption) -> bool """
        return False

    def titleFormat(self): # real signature unknown; restored from __doc__
        """ QWizard.titleFormat() -> Qt.TextFormat """
        pass

    def validateCurrentPage(self): # real signature unknown; restored from __doc__
        """ QWizard.validateCurrentPage() -> bool """
        return False

    def visitedPages(self): # real signature unknown; restored from __doc__
        """ QWizard.visitedPages() -> list-of-int """
        pass

    def wizardStyle(self): # real signature unknown; restored from __doc__
        """ QWizard.wizardStyle() -> QWizard.WizardStyle """
        pass

    def __init__(self, QWidget_parent=None, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass

    AeroStyle = 3
    BackButton = 0
    BackgroundPixmap = 3
    BannerPixmap = 2
    CancelButton = 4
    CancelButtonOnLeft = 1024
    ClassicStyle = 0
    CommitButton = 2
    CustomButton1 = 6
    CustomButton2 = 7
    CustomButton3 = 8
    DisabledBackButtonOnLastPage = 64
    ExtendedWatermarkPixmap = 4
    FinishButton = 3
    HaveCustomButton1 = 8192
    HaveCustomButton2 = 16384
    HaveCustomButton3 = 32768
    HaveFinishButtonOnEarlyPages = 256
    HaveHelpButton = 2048
    HaveNextButtonOnLastPage = 128
    HelpButton = 5
    HelpButtonOnRight = 4096
    IgnoreSubTitles = 2
    IndependentPages = 1
    LogoPixmap = 1
    MacStyle = 2
    ModernStyle = 1
    NextButton = 1
    NoBackButtonOnLastPage = 32
    NoBackButtonOnStartPage = 16
    NoCancelButton = 512
    NoDefaultButton = 8
    Stretch = 9
    WatermarkPixmap = 0


