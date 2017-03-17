# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QPaintDevice import QPaintDevice

class QPicture(QPaintDevice):
    """
    QPicture(int formatVersion=-1)
    QPicture(QPicture)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QPicture.boundingRect() -> QRect """
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ QPicture.data() -> str """
        return ""

    def detach(self): # real signature unknown; restored from __doc__
        """ QPicture.detach() """
        pass

    def devType(self): # real signature unknown; restored from __doc__
        """ QPicture.devType() -> int """
        return 0

    def inputFormatList(self): # real signature unknown; restored from __doc__
        """ QPicture.inputFormatList() -> QStringList """
        pass

    def inputFormats(self): # real signature unknown; restored from __doc__
        """ QPicture.inputFormats() -> list-of-QByteArray """
        pass

    def isDetached(self): # real signature unknown; restored from __doc__
        """ QPicture.isDetached() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QPicture.isNull() -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPicture.load(QIODevice, str format=None) -> bool
        QPicture.load(QString, str format=None) -> bool
        """
        return False

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ QPicture.metric(QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def outputFormatList(self): # real signature unknown; restored from __doc__
        """ QPicture.outputFormatList() -> QStringList """
        pass

    def outputFormats(self): # real signature unknown; restored from __doc__
        """ QPicture.outputFormats() -> list-of-QByteArray """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ QPicture.paintEngine() -> QPaintEngine """
        return QPaintEngine

    def pictureFormat(self, QString): # real signature unknown; restored from __doc__
        """ QPicture.pictureFormat(QString) -> str """
        return ""

    def play(self, QPainter): # real signature unknown; restored from __doc__
        """ QPicture.play(QPainter) -> bool """
        return False

    def save(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPicture.save(QIODevice, str format=None) -> bool
        QPicture.save(QString, str format=None) -> bool
        """
        return False

    def setBoundingRect(self, QRect): # real signature unknown; restored from __doc__
        """ QPicture.setBoundingRect(QRect) """
        pass

    def setData(self, p_str): # real signature unknown; restored from __doc__
        """ QPicture.setData(str) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QPicture.size() -> int """
        return 0

    def swap(self, QPicture): # real signature unknown; restored from __doc__
        """ QPicture.swap(QPicture) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


