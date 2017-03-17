# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QWizardPage(QWidget):
    """ QWizardPage(QWidget parent=None) """
    def buttonText(self, QWizard_WizardButton): # real signature unknown; restored from __doc__
        """ QWizardPage.buttonText(QWizard.WizardButton) -> QString """
        pass

    def cleanupPage(self): # real signature unknown; restored from __doc__
        """ QWizardPage.cleanupPage() """
        pass

    def completeChanged(self, *args, **kwargs): # real signature unknown
        """ QWizardPage.completeChanged [signal] """
        pass

    def field(self, QString): # real signature unknown; restored from __doc__
        """ QWizardPage.field(QString) -> QVariant """
        pass

    def initializePage(self): # real signature unknown; restored from __doc__
        """ QWizardPage.initializePage() """
        pass

    def isCommitPage(self): # real signature unknown; restored from __doc__
        """ QWizardPage.isCommitPage() -> bool """
        return False

    def isComplete(self): # real signature unknown; restored from __doc__
        """ QWizardPage.isComplete() -> bool """
        return False

    def isFinalPage(self): # real signature unknown; restored from __doc__
        """ QWizardPage.isFinalPage() -> bool """
        return False

    def nextId(self): # real signature unknown; restored from __doc__
        """ QWizardPage.nextId() -> int """
        return 0

    def pixmap(self, QWizard_WizardPixmap): # real signature unknown; restored from __doc__
        """ QWizardPage.pixmap(QWizard.WizardPixmap) -> QPixmap """
        return QPixmap

    def registerField(self, QString, QWidget, str_property=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWizardPage.registerField(QString, QWidget, str property=None, signal changedSignal=0)
        QWizardPage.registerField(QString, QWidget, str property=None, SIGNAL() changedSignal=0)
        """
        pass

    def setButtonText(self, QWizard_WizardButton, QString): # real signature unknown; restored from __doc__
        """ QWizardPage.setButtonText(QWizard.WizardButton, QString) """
        pass

    def setCommitPage(self, bool): # real signature unknown; restored from __doc__
        """ QWizardPage.setCommitPage(bool) """
        pass

    def setField(self, QString, QVariant): # real signature unknown; restored from __doc__
        """ QWizardPage.setField(QString, QVariant) """
        pass

    def setFinalPage(self, bool): # real signature unknown; restored from __doc__
        """ QWizardPage.setFinalPage(bool) """
        pass

    def setPixmap(self, QWizard_WizardPixmap, QPixmap): # real signature unknown; restored from __doc__
        """ QWizardPage.setPixmap(QWizard.WizardPixmap, QPixmap) """
        pass

    def setSubTitle(self, QString): # real signature unknown; restored from __doc__
        """ QWizardPage.setSubTitle(QString) """
        pass

    def setTitle(self, QString): # real signature unknown; restored from __doc__
        """ QWizardPage.setTitle(QString) """
        pass

    def subTitle(self): # real signature unknown; restored from __doc__
        """ QWizardPage.subTitle() -> QString """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ QWizardPage.title() -> QString """
        pass

    def validatePage(self): # real signature unknown; restored from __doc__
        """ QWizardPage.validatePage() -> bool """
        return False

    def wizard(self): # real signature unknown; restored from __doc__
        """ QWizardPage.wizard() -> QWizard """
        return QWizard

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


