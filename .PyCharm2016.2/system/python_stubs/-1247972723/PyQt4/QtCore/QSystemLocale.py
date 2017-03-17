# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QSystemLocale(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QSystemLocale()
    QSystemLocale(QSystemLocale)
    """
    def fallbackLocale(self): # real signature unknown; restored from __doc__
        """ QSystemLocale.fallbackLocale() -> QLocale """
        return QLocale

    def query(self, QSystemLocale_QueryType, QVariant): # real signature unknown; restored from __doc__
        """ QSystemLocale.query(QSystemLocale.QueryType, QVariant) -> QVariant """
        return QVariant

    def __init__(self, QSystemLocale=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AMText = 24
    CountryId = 1
    CurrencySymbol = 28
    CurrencyToString = 29
    DateFormatLong = 6
    DateFormatShort = 7
    DateTimeFormatLong = 18
    DateTimeFormatShort = 19
    DateTimeToStringLong = 20
    DateTimeToStringShort = 21
    DateToStringLong = 14
    DateToStringShort = 15
    DayNameLong = 10
    DayNameShort = 11
    DecimalPoint = 2
    FirstDayOfWeek = 26
    GroupSeparator = 3
    LanguageId = 0
    ListToSeparatedString = 34
    LocaleChanged = 35
    MeasurementSystem = 22
    MonthNameLong = 12
    MonthNameShort = 13
    NativeCountryName = 37
    NativeLanguageName = 36
    NegativeSign = 5
    PMText = 25
    PositiveSign = 23
    ScriptId = 33
    StringToAlternateQuotation = 32
    StringToStandardQuotation = 31
    TimeFormatLong = 8
    TimeFormatShort = 9
    TimeToStringLong = 16
    TimeToStringShort = 17
    UILanguages = 30
    Weekdays = 27
    ZeroDigit = 4


