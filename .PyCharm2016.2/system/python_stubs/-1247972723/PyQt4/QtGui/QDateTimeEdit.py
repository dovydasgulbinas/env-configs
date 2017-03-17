# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractSpinBox import QAbstractSpinBox

class QDateTimeEdit(QAbstractSpinBox):
    """
    QDateTimeEdit(QWidget parent=None)
    QDateTimeEdit(QDateTime, QWidget parent=None)
    QDateTimeEdit(QDate, QWidget parent=None)
    QDateTimeEdit(QTime, QWidget parent=None)
    """
    def calendarPopup(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.calendarPopup() -> bool """
        return False

    def calendarWidget(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.calendarWidget() -> QCalendarWidget """
        return QCalendarWidget

    def clear(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.clear() """
        pass

    def clearMaximumDate(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.clearMaximumDate() """
        pass

    def clearMaximumDateTime(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.clearMaximumDateTime() """
        pass

    def clearMaximumTime(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.clearMaximumTime() """
        pass

    def clearMinimumDate(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.clearMinimumDate() """
        pass

    def clearMinimumDateTime(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.clearMinimumDateTime() """
        pass

    def clearMinimumTime(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.clearMinimumTime() """
        pass

    def currentSection(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.currentSection() -> QDateTimeEdit.Section """
        pass

    def currentSectionIndex(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.currentSectionIndex() -> int """
        return 0

    def date(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.date() -> QDate """
        pass

    def dateChanged(self, *args, **kwargs): # real signature unknown
        """ QDateTimeEdit.dateChanged[QDate] [signal] """
        pass

    def dateTime(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.dateTime() -> QDateTime """
        pass

    def dateTimeChanged(self, *args, **kwargs): # real signature unknown
        """ QDateTimeEdit.dateTimeChanged[QDateTime] [signal] """
        pass

    def dateTimeFromText(self, QString): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.dateTimeFromText(QString) -> QDateTime """
        pass

    def displayedSections(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.displayedSections() -> QDateTimeEdit.Sections """
        pass

    def displayFormat(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.displayFormat() -> QString """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.event(QEvent) -> bool """
        return False

    def fixup(self, QString): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.fixup(QString) """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.focusInEvent(QFocusEvent) """
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.focusNextPrevChild(bool) -> bool """
        return False

    def initStyleOption(self, QStyleOptionSpinBox): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.initStyleOption(QStyleOptionSpinBox) """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.keyPressEvent(QKeyEvent) """
        pass

    def maximumDate(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.maximumDate() -> QDate """
        pass

    def maximumDateTime(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.maximumDateTime() -> QDateTime """
        pass

    def maximumTime(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.maximumTime() -> QTime """
        pass

    def minimumDate(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.minimumDate() -> QDate """
        pass

    def minimumDateTime(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.minimumDateTime() -> QDateTime """
        pass

    def minimumTime(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.minimumTime() -> QTime """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.mousePressEvent(QMouseEvent) """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.paintEvent(QPaintEvent) """
        pass

    def sectionAt(self, p_int): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.sectionAt(int) -> QDateTimeEdit.Section """
        pass

    def sectionCount(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.sectionCount() -> int """
        return 0

    def sectionText(self, QDateTimeEdit_Section): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.sectionText(QDateTimeEdit.Section) -> QString """
        pass

    def setCalendarPopup(self, bool): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setCalendarPopup(bool) """
        pass

    def setCalendarWidget(self, QCalendarWidget): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setCalendarWidget(QCalendarWidget) """
        pass

    def setCurrentSection(self, QDateTimeEdit_Section): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setCurrentSection(QDateTimeEdit.Section) """
        pass

    def setCurrentSectionIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setCurrentSectionIndex(int) """
        pass

    def setDate(self, QDate): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setDate(QDate) """
        pass

    def setDateRange(self, QDate, QDate_1): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setDateRange(QDate, QDate) """
        pass

    def setDateTime(self, QDateTime): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setDateTime(QDateTime) """
        pass

    def setDateTimeRange(self, QDateTime, QDateTime_1): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setDateTimeRange(QDateTime, QDateTime) """
        pass

    def setDisplayFormat(self, QString): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setDisplayFormat(QString) """
        pass

    def setMaximumDate(self, QDate): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setMaximumDate(QDate) """
        pass

    def setMaximumDateTime(self, QDateTime): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setMaximumDateTime(QDateTime) """
        pass

    def setMaximumTime(self, QTime): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setMaximumTime(QTime) """
        pass

    def setMinimumDate(self, QDate): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setMinimumDate(QDate) """
        pass

    def setMinimumDateTime(self, QDateTime): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setMinimumDateTime(QDateTime) """
        pass

    def setMinimumTime(self, QTime): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setMinimumTime(QTime) """
        pass

    def setSelectedSection(self, QDateTimeEdit_Section): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setSelectedSection(QDateTimeEdit.Section) """
        pass

    def setTime(self, QTime): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setTime(QTime) """
        pass

    def setTimeRange(self, QTime, QTime_1): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setTimeRange(QTime, QTime) """
        pass

    def setTimeSpec(self, Qt_TimeSpec): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.setTimeSpec(Qt.TimeSpec) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.sizeHint() -> QSize """
        pass

    def stepBy(self, p_int): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.stepBy(int) """
        pass

    def stepEnabled(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.stepEnabled() -> QAbstractSpinBox.StepEnabled """
        pass

    def textFromDateTime(self, QDateTime): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.textFromDateTime(QDateTime) -> QString """
        pass

    def time(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.time() -> QTime """
        pass

    def timeChanged(self, *args, **kwargs): # real signature unknown
        """ QDateTimeEdit.timeChanged[QTime] [signal] """
        pass

    def timeSpec(self): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.timeSpec() -> Qt.TimeSpec """
        pass

    def validate(self, QString, p_int): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.validate(QString, int) -> (QValidator.State, int) """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ QDateTimeEdit.wheelEvent(QWheelEvent) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AmPmSection = 1
    DateSections_Mask = 1792
    DaySection = 256
    HourSection = 16
    MinuteSection = 8
    MonthSection = 512
    MSecSection = 2
    NoSection = 0
    SecondSection = 4
    TimeSections_Mask = 31
    YearSection = 1024


