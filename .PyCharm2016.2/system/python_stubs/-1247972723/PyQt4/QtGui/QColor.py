# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QColor(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QColor(Qt.GlobalColor)
    QColor(int)
    QColor(QVariant)
    QColor()
    QColor(int, int, int, int alpha=255)
    QColor(QString)
    QColor(QColor)
    """
    def allowX11ColorNames(self): # real signature unknown; restored from __doc__
        """ QColor.allowX11ColorNames() -> bool """
        return False

    def alpha(self): # real signature unknown; restored from __doc__
        """ QColor.alpha() -> int """
        return 0

    def alphaF(self): # real signature unknown; restored from __doc__
        """ QColor.alphaF() -> float """
        return 0.0

    def black(self): # real signature unknown; restored from __doc__
        """ QColor.black() -> int """
        return 0

    def blackF(self): # real signature unknown; restored from __doc__
        """ QColor.blackF() -> float """
        return 0.0

    def blue(self): # real signature unknown; restored from __doc__
        """ QColor.blue() -> int """
        return 0

    def blueF(self): # real signature unknown; restored from __doc__
        """ QColor.blueF() -> float """
        return 0.0

    def colorNames(self): # real signature unknown; restored from __doc__
        """ QColor.colorNames() -> QStringList """
        pass

    def convertTo(self, QColor_Spec): # real signature unknown; restored from __doc__
        """ QColor.convertTo(QColor.Spec) -> QColor """
        return QColor

    def cyan(self): # real signature unknown; restored from __doc__
        """ QColor.cyan() -> int """
        return 0

    def cyanF(self): # real signature unknown; restored from __doc__
        """ QColor.cyanF() -> float """
        return 0.0

    def dark(self, int_factor=200): # real signature unknown; restored from __doc__
        """ QColor.dark(int factor=200) -> QColor """
        return QColor

    def darker(self, int_factor=200): # real signature unknown; restored from __doc__
        """ QColor.darker(int factor=200) -> QColor """
        return QColor

    def fromCmyk(self, p_int, p_int_1, p_int_2, p_int_3, int_alpha=255): # real signature unknown; restored from __doc__
        """ QColor.fromCmyk(int, int, int, int, int alpha=255) -> QColor """
        return QColor

    def fromCmykF(self, p_float, p_float_1, p_float_2, p_float_3, float_alpha=1): # real signature unknown; restored from __doc__
        """ QColor.fromCmykF(float, float, float, float, float alpha=1) -> QColor """
        return QColor

    def fromHsl(self, p_int, p_int_1, p_int_2, int_alpha=255): # real signature unknown; restored from __doc__
        """ QColor.fromHsl(int, int, int, int alpha=255) -> QColor """
        return QColor

    def fromHslF(self, p_float, p_float_1, p_float_2, float_alpha=1): # real signature unknown; restored from __doc__
        """ QColor.fromHslF(float, float, float, float alpha=1) -> QColor """
        return QColor

    def fromHsv(self, p_int, p_int_1, p_int_2, int_alpha=255): # real signature unknown; restored from __doc__
        """ QColor.fromHsv(int, int, int, int alpha=255) -> QColor """
        return QColor

    def fromHsvF(self, p_float, p_float_1, p_float_2, float_alpha=1): # real signature unknown; restored from __doc__
        """ QColor.fromHsvF(float, float, float, float alpha=1) -> QColor """
        return QColor

    def fromRgb(self, p_int, p_int_1=None, p_int_2=None, int_alpha=255): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QColor.fromRgb(int) -> QColor
        QColor.fromRgb(int, int, int, int alpha=255) -> QColor
        """
        return QColor

    def fromRgba(self, p_int): # real signature unknown; restored from __doc__
        """ QColor.fromRgba(int) -> QColor """
        return QColor

    def fromRgbF(self, p_float, p_float_1, p_float_2, float_alpha=1): # real signature unknown; restored from __doc__
        """ QColor.fromRgbF(float, float, float, float alpha=1) -> QColor """
        return QColor

    def getCmyk(self): # real signature unknown; restored from __doc__
        """ QColor.getCmyk() -> (int, int, int, int, int) """
        pass

    def getCmykF(self): # real signature unknown; restored from __doc__
        """ QColor.getCmykF() -> (float, float, float, float, float) """
        pass

    def getHsl(self): # real signature unknown; restored from __doc__
        """ QColor.getHsl() -> (int, int, int, int) """
        pass

    def getHslF(self): # real signature unknown; restored from __doc__
        """ QColor.getHslF() -> (float, float, float, float) """
        pass

    def getHsv(self): # real signature unknown; restored from __doc__
        """ QColor.getHsv() -> (int, int, int, int) """
        pass

    def getHsvF(self): # real signature unknown; restored from __doc__
        """ QColor.getHsvF() -> (float, float, float, float) """
        pass

    def getRgb(self): # real signature unknown; restored from __doc__
        """ QColor.getRgb() -> (int, int, int, int) """
        pass

    def getRgbF(self): # real signature unknown; restored from __doc__
        """ QColor.getRgbF() -> (float, float, float, float) """
        pass

    def green(self): # real signature unknown; restored from __doc__
        """ QColor.green() -> int """
        return 0

    def greenF(self): # real signature unknown; restored from __doc__
        """ QColor.greenF() -> float """
        return 0.0

    def hslHue(self): # real signature unknown; restored from __doc__
        """ QColor.hslHue() -> int """
        return 0

    def hslHueF(self): # real signature unknown; restored from __doc__
        """ QColor.hslHueF() -> float """
        return 0.0

    def hslSaturation(self): # real signature unknown; restored from __doc__
        """ QColor.hslSaturation() -> int """
        return 0

    def hslSaturationF(self): # real signature unknown; restored from __doc__
        """ QColor.hslSaturationF() -> float """
        return 0.0

    def hsvHue(self): # real signature unknown; restored from __doc__
        """ QColor.hsvHue() -> int """
        return 0

    def hsvHueF(self): # real signature unknown; restored from __doc__
        """ QColor.hsvHueF() -> float """
        return 0.0

    def hsvSaturation(self): # real signature unknown; restored from __doc__
        """ QColor.hsvSaturation() -> int """
        return 0

    def hsvSaturationF(self): # real signature unknown; restored from __doc__
        """ QColor.hsvSaturationF() -> float """
        return 0.0

    def hue(self): # real signature unknown; restored from __doc__
        """ QColor.hue() -> int """
        return 0

    def hueF(self): # real signature unknown; restored from __doc__
        """ QColor.hueF() -> float """
        return 0.0

    def isValid(self): # real signature unknown; restored from __doc__
        """ QColor.isValid() -> bool """
        return False

    def isValidColor(self, QString): # real signature unknown; restored from __doc__
        """ QColor.isValidColor(QString) -> bool """
        return False

    def light(self, int_factor=150): # real signature unknown; restored from __doc__
        """ QColor.light(int factor=150) -> QColor """
        return QColor

    def lighter(self, int_factor=150): # real signature unknown; restored from __doc__
        """ QColor.lighter(int factor=150) -> QColor """
        return QColor

    def lightness(self): # real signature unknown; restored from __doc__
        """ QColor.lightness() -> int """
        return 0

    def lightnessF(self): # real signature unknown; restored from __doc__
        """ QColor.lightnessF() -> float """
        return 0.0

    def magenta(self): # real signature unknown; restored from __doc__
        """ QColor.magenta() -> int """
        return 0

    def magentaF(self): # real signature unknown; restored from __doc__
        """ QColor.magentaF() -> float """
        return 0.0

    def name(self): # real signature unknown; restored from __doc__
        """ QColor.name() -> QString """
        pass

    def red(self): # real signature unknown; restored from __doc__
        """ QColor.red() -> int """
        return 0

    def redF(self): # real signature unknown; restored from __doc__
        """ QColor.redF() -> float """
        return 0.0

    def rgb(self): # real signature unknown; restored from __doc__
        """ QColor.rgb() -> int """
        return 0

    def rgba(self): # real signature unknown; restored from __doc__
        """ QColor.rgba() -> int """
        return 0

    def saturation(self): # real signature unknown; restored from __doc__
        """ QColor.saturation() -> int """
        return 0

    def saturationF(self): # real signature unknown; restored from __doc__
        """ QColor.saturationF() -> float """
        return 0.0

    def setAllowX11ColorNames(self, bool): # real signature unknown; restored from __doc__
        """ QColor.setAllowX11ColorNames(bool) """
        pass

    def setAlpha(self, p_int): # real signature unknown; restored from __doc__
        """ QColor.setAlpha(int) """
        pass

    def setAlphaF(self, p_float): # real signature unknown; restored from __doc__
        """ QColor.setAlphaF(float) """
        pass

    def setBlue(self, p_int): # real signature unknown; restored from __doc__
        """ QColor.setBlue(int) """
        pass

    def setBlueF(self, p_float): # real signature unknown; restored from __doc__
        """ QColor.setBlueF(float) """
        pass

    def setCmyk(self, p_int, p_int_1, p_int_2, p_int_3, int_alpha=255): # real signature unknown; restored from __doc__
        """ QColor.setCmyk(int, int, int, int, int alpha=255) """
        pass

    def setCmykF(self, p_float, p_float_1, p_float_2, p_float_3, float_alpha=1): # real signature unknown; restored from __doc__
        """ QColor.setCmykF(float, float, float, float, float alpha=1) """
        pass

    def setGreen(self, p_int): # real signature unknown; restored from __doc__
        """ QColor.setGreen(int) """
        pass

    def setGreenF(self, p_float): # real signature unknown; restored from __doc__
        """ QColor.setGreenF(float) """
        pass

    def setHsl(self, p_int, p_int_1, p_int_2, int_alpha=255): # real signature unknown; restored from __doc__
        """ QColor.setHsl(int, int, int, int alpha=255) """
        pass

    def setHslF(self, p_float, p_float_1, p_float_2, float_alpha=1): # real signature unknown; restored from __doc__
        """ QColor.setHslF(float, float, float, float alpha=1) """
        pass

    def setHsv(self, p_int, p_int_1, p_int_2, int_alpha=255): # real signature unknown; restored from __doc__
        """ QColor.setHsv(int, int, int, int alpha=255) """
        pass

    def setHsvF(self, p_float, p_float_1, p_float_2, float_alpha=1): # real signature unknown; restored from __doc__
        """ QColor.setHsvF(float, float, float, float alpha=1) """
        pass

    def setNamedColor(self, QString): # real signature unknown; restored from __doc__
        """ QColor.setNamedColor(QString) """
        pass

    def setRed(self, p_int): # real signature unknown; restored from __doc__
        """ QColor.setRed(int) """
        pass

    def setRedF(self, p_float): # real signature unknown; restored from __doc__
        """ QColor.setRedF(float) """
        pass

    def setRgb(self, p_int, p_int_1=None, p_int_2=None, int_alpha=255): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QColor.setRgb(int, int, int, int alpha=255)
        QColor.setRgb(int)
        """
        pass

    def setRgba(self, p_int): # real signature unknown; restored from __doc__
        """ QColor.setRgba(int) """
        pass

    def setRgbF(self, p_float, p_float_1, p_float_2, float_alpha=1): # real signature unknown; restored from __doc__
        """ QColor.setRgbF(float, float, float, float alpha=1) """
        pass

    def spec(self): # real signature unknown; restored from __doc__
        """ QColor.spec() -> QColor.Spec """
        pass

    def toCmyk(self): # real signature unknown; restored from __doc__
        """ QColor.toCmyk() -> QColor """
        return QColor

    def toHsl(self): # real signature unknown; restored from __doc__
        """ QColor.toHsl() -> QColor """
        return QColor

    def toHsv(self): # real signature unknown; restored from __doc__
        """ QColor.toHsv() -> QColor """
        return QColor

    def toRgb(self): # real signature unknown; restored from __doc__
        """ QColor.toRgb() -> QColor """
        return QColor

    def value(self): # real signature unknown; restored from __doc__
        """ QColor.value() -> int """
        return 0

    def valueF(self): # real signature unknown; restored from __doc__
        """ QColor.valueF() -> float """
        return 0.0

    def yellow(self): # real signature unknown; restored from __doc__
        """ QColor.yellow() -> int """
        return 0

    def yellowF(self): # real signature unknown; restored from __doc__
        """ QColor.yellowF() -> float """
        return 0.0

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Cmyk = 3
    Hsl = 4
    Hsv = 2
    Invalid = 0
    Rgb = 1


