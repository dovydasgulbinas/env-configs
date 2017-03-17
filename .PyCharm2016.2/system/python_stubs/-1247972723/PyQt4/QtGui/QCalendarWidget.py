# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QCalendarWidget(QWidget):
    """ QCalendarWidget(QWidget parent=None) """
    def activated(self, *args, **kwargs): # real signature unknown
        """ QCalendarWidget.activated[QDate] [signal] """
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
        """ QCalendarWidget.clicked[QDate] [signal] """
        pass

    def currentPageChanged(self, *args, **kwargs): # real signature unknown
        """ QCalendarWidget.currentPageChanged[int, int] [signal] """
        pass

    def dateEditAcceptDelay(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.dateEditAcceptDelay() -> int """
        return 0

    def dateTextFormat(self, QDate=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QCalendarWidget.dateTextFormat() -> dict-of-QDate-QTextCharFormat
        QCalendarWidget.dateTextFormat(QDate) -> QTextCharFormat
        """
        return QTextCharFormat

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QCalendarWidget.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QCalendarWidget.eventFilter(QObject, QEvent) -> bool """
        return False

    def firstDayOfWeek(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.firstDayOfWeek() -> Qt.DayOfWeek """
        pass

    def headerTextFormat(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.headerTextFormat() -> QTextCharFormat """
        return QTextCharFormat

    def horizontalHeaderFormat(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.horizontalHeaderFormat() -> QCalendarWidget.HorizontalHeaderFormat """
        pass

    def isDateEditEnabled(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.isDateEditEnabled() -> bool """
        return False

    def isGridVisible(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.isGridVisible() -> bool """
        return False

    def isHeaderVisible(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.isHeaderVisible() -> bool """
        return False

    def isNavigationBarVisible(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.isNavigationBarVisible() -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QCalendarWidget.keyPressEvent(QKeyEvent) """
        pass

    def maximumDate(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.maximumDate() -> QDate """
        pass

    def minimumDate(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.minimumDate() -> QDate """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.minimumSizeHint() -> QSize """
        pass

    def monthShown(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.monthShown() -> int """
        return 0

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QCalendarWidget.mousePressEvent(QMouseEvent) """
        pass

    def paintCell(self, QPainter, QRect, QDate): # real signature unknown; restored from __doc__
        """ QCalendarWidget.paintCell(QPainter, QRect, QDate) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QCalendarWidget.resizeEvent(QResizeEvent) """
        pass

    def selectedDate(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.selectedDate() -> QDate """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ QCalendarWidget.selectionChanged [signal] """
        pass

    def selectionMode(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.selectionMode() -> QCalendarWidget.SelectionMode """
        pass

    def setCurrentPage(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setCurrentPage(int, int) """
        pass

    def setDateEditAcceptDelay(self, p_int): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setDateEditAcceptDelay(int) """
        pass

    def setDateEditEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setDateEditEnabled(bool) """
        pass

    def setDateRange(self, QDate, QDate_1): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setDateRange(QDate, QDate) """
        pass

    def setDateTextFormat(self, QDate, QTextCharFormat): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setDateTextFormat(QDate, QTextCharFormat) """
        pass

    def setFirstDayOfWeek(self, Qt_DayOfWeek): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setFirstDayOfWeek(Qt.DayOfWeek) """
        pass

    def setGridVisible(self, bool): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setGridVisible(bool) """
        pass

    def setHeaderTextFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setHeaderTextFormat(QTextCharFormat) """
        pass

    def setHeaderVisible(self, bool): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setHeaderVisible(bool) """
        pass

    def setHorizontalHeaderFormat(self, QCalendarWidget_HorizontalHeaderFormat): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat) """
        pass

    def setMaximumDate(self, QDate): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setMaximumDate(QDate) """
        pass

    def setMinimumDate(self, QDate): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setMinimumDate(QDate) """
        pass

    def setNavigationBarVisible(self, bool): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setNavigationBarVisible(bool) """
        pass

    def setSelectedDate(self, QDate): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setSelectedDate(QDate) """
        pass

    def setSelectionMode(self, QCalendarWidget_SelectionMode): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setSelectionMode(QCalendarWidget.SelectionMode) """
        pass

    def setVerticalHeaderFormat(self, QCalendarWidget_VerticalHeaderFormat): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat) """
        pass

    def setWeekdayTextFormat(self, Qt_DayOfWeek, QTextCharFormat): # real signature unknown; restored from __doc__
        """ QCalendarWidget.setWeekdayTextFormat(Qt.DayOfWeek, QTextCharFormat) """
        pass

    def showNextMonth(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.showNextMonth() """
        pass

    def showNextYear(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.showNextYear() """
        pass

    def showPreviousMonth(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.showPreviousMonth() """
        pass

    def showPreviousYear(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.showPreviousYear() """
        pass

    def showSelectedDate(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.showSelectedDate() """
        pass

    def showToday(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.showToday() """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.sizeHint() -> QSize """
        pass

    def updateCell(self, QDate): # real signature unknown; restored from __doc__
        """ QCalendarWidget.updateCell(QDate) """
        pass

    def updateCells(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.updateCells() """
        pass

    def verticalHeaderFormat(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.verticalHeaderFormat() -> QCalendarWidget.VerticalHeaderFormat """
        pass

    def weekdayTextFormat(self, Qt_DayOfWeek): # real signature unknown; restored from __doc__
        """ QCalendarWidget.weekdayTextFormat(Qt.DayOfWeek) -> QTextCharFormat """
        return QTextCharFormat

    def yearShown(self): # real signature unknown; restored from __doc__
        """ QCalendarWidget.yearShown() -> int """
        return 0

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    ISOWeekNumbers = 1
    LongDayNames = 3
    NoHorizontalHeader = 0
    NoSelection = 0
    NoVerticalHeader = 0
    ShortDayNames = 2
    SingleLetterDayNames = 1
    SingleSelection = 1


