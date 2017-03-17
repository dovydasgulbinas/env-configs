# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QTextCodec(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def aliases(self): # real signature unknown; restored from __doc__
        """ QTextCodec.aliases() -> list-of-QByteArray """
        pass

    def availableCodecs(self): # real signature unknown; restored from __doc__
        """ QTextCodec.availableCodecs() -> list-of-QByteArray """
        pass

    def availableMibs(self): # real signature unknown; restored from __doc__
        """ QTextCodec.availableMibs() -> list-of-int """
        pass

    def canEncode(self, QString): # real signature unknown; restored from __doc__
        """ QTextCodec.canEncode(QString) -> bool """
        return False

    def codecForCStrings(self): # real signature unknown; restored from __doc__
        """ QTextCodec.codecForCStrings() -> QTextCodec """
        return QTextCodec

    def codecForHtml(self, QByteArray, QTextCodec=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextCodec.codecForHtml(QByteArray) -> QTextCodec
        QTextCodec.codecForHtml(QByteArray, QTextCodec) -> QTextCodec
        """
        return QTextCodec

    def codecForLocale(self): # real signature unknown; restored from __doc__
        """ QTextCodec.codecForLocale() -> QTextCodec """
        return QTextCodec

    def codecForMib(self, p_int): # real signature unknown; restored from __doc__
        """ QTextCodec.codecForMib(int) -> QTextCodec """
        return QTextCodec

    def codecForName(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextCodec.codecForName(QByteArray) -> QTextCodec
        QTextCodec.codecForName(str) -> QTextCodec
        """
        return QTextCodec

    def codecForTr(self): # real signature unknown; restored from __doc__
        """ QTextCodec.codecForTr() -> QTextCodec """
        return QTextCodec

    def codecForUtfText(self, QByteArray, QTextCodec=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextCodec.codecForUtfText(QByteArray) -> QTextCodec
        QTextCodec.codecForUtfText(QByteArray, QTextCodec) -> QTextCodec
        """
        return QTextCodec

    def convertToUnicode(self, p_str, QTextCodec_ConverterState): # real signature unknown; restored from __doc__
        """ QTextCodec.convertToUnicode(str, QTextCodec.ConverterState) -> QString """
        return QString

    def fromUnicode(self, QString): # real signature unknown; restored from __doc__
        """ QTextCodec.fromUnicode(QString) -> QByteArray """
        return QByteArray

    def makeDecoder(self, QTextCodec_ConversionFlags=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextCodec.makeDecoder() -> QTextDecoder
        QTextCodec.makeDecoder(QTextCodec.ConversionFlags) -> QTextDecoder
        """
        return QTextDecoder

    def makeEncoder(self, QTextCodec_ConversionFlags=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextCodec.makeEncoder() -> QTextEncoder
        QTextCodec.makeEncoder(QTextCodec.ConversionFlags) -> QTextEncoder
        """
        return QTextEncoder

    def mibEnum(self): # real signature unknown; restored from __doc__
        """ QTextCodec.mibEnum() -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ QTextCodec.name() -> QByteArray """
        return QByteArray

    def setCodecForCStrings(self, QTextCodec): # real signature unknown; restored from __doc__
        """ QTextCodec.setCodecForCStrings(QTextCodec) """
        pass

    def setCodecForLocale(self, QTextCodec): # real signature unknown; restored from __doc__
        """ QTextCodec.setCodecForLocale(QTextCodec) """
        pass

    def setCodecForTr(self, QTextCodec): # real signature unknown; restored from __doc__
        """ QTextCodec.setCodecForTr(QTextCodec) """
        pass

    def toUnicode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextCodec.toUnicode(QByteArray) -> QString
        QTextCodec.toUnicode(str) -> QString
        QTextCodec.toUnicode(str, QTextCodec.ConverterState state=None) -> QString
        """
        return QString

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ConvertInvalidToNull = -2147483648
    DefaultConversion = 0
    IgnoreHeader = 1


