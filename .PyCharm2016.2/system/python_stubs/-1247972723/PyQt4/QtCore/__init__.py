# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


# Variables with simple values

PYQT_VERSION = 264964

PYQT_VERSION_STR = '4.11.4'

QtCriticalMsg = 2
QtDebugMsg = 0
QtFatalMsg = 3
QtSystemMsg = 2
QtWarningMsg = 1

QT_VERSION = 264199

QT_VERSION_STR = '4.8.7'

# functions

def bin(QTextStream): # real signature unknown; restored from __doc__
    """ bin(QTextStream) -> QTextStream """
    return QTextStream

def bom(QTextStream): # real signature unknown; restored from __doc__
    """ bom(QTextStream) -> QTextStream """
    return QTextStream

def center(QTextStream): # real signature unknown; restored from __doc__
    """ center(QTextStream) -> QTextStream """
    return QTextStream

def dec(QTextStream): # real signature unknown; restored from __doc__
    """ dec(QTextStream) -> QTextStream """
    return QTextStream

def endl(QTextStream): # real signature unknown; restored from __doc__
    """ endl(QTextStream) -> QTextStream """
    return QTextStream

def fixed(QTextStream): # real signature unknown; restored from __doc__
    """ fixed(QTextStream) -> QTextStream """
    return QTextStream

def flush(QTextStream): # real signature unknown; restored from __doc__
    """ flush(QTextStream) -> QTextStream """
    return QTextStream

def forcepoint(QTextStream): # real signature unknown; restored from __doc__
    """ forcepoint(QTextStream) -> QTextStream """
    return QTextStream

def forcesign(QTextStream): # real signature unknown; restored from __doc__
    """ forcesign(QTextStream) -> QTextStream """
    return QTextStream

def hex(QTextStream): # real signature unknown; restored from __doc__
    """ hex(QTextStream) -> QTextStream """
    return QTextStream

def left(QTextStream): # real signature unknown; restored from __doc__
    """ left(QTextStream) -> QTextStream """
    return QTextStream

def lowercasebase(QTextStream): # real signature unknown; restored from __doc__
    """ lowercasebase(QTextStream) -> QTextStream """
    return QTextStream

def lowercasedigits(QTextStream): # real signature unknown; restored from __doc__
    """ lowercasedigits(QTextStream) -> QTextStream """
    return QTextStream

def noforcepoint(QTextStream): # real signature unknown; restored from __doc__
    """ noforcepoint(QTextStream) -> QTextStream """
    return QTextStream

def noforcesign(QTextStream): # real signature unknown; restored from __doc__
    """ noforcesign(QTextStream) -> QTextStream """
    return QTextStream

def noshowbase(QTextStream): # real signature unknown; restored from __doc__
    """ noshowbase(QTextStream) -> QTextStream """
    return QTextStream

def oct(QTextStream): # real signature unknown; restored from __doc__
    """ oct(QTextStream) -> QTextStream """
    return QTextStream

def pyqtPickleProtocol(): # real signature unknown; restored from __doc__
    """ pyqtPickleProtocol() -> int-or-None """
    pass

def pyqtRemoveInputHook(): # real signature unknown; restored from __doc__
    """ pyqtRemoveInputHook() """
    pass

def pyqtRestoreInputHook(): # real signature unknown; restored from __doc__
    """ pyqtRestoreInputHook() """
    pass

def pyqtSetPickleProtocol(int_or_None): # real signature unknown; restored from __doc__
    """ pyqtSetPickleProtocol(int-or-None) """
    pass

def pyqtSignature(str_signature, str_result=None): # real signature unknown; restored from __doc__
    """
    @pyqtSignature(str signature,  str result=None)
    
    This is deprecated, use pyqtSlot() instead.
    
    This is a decorator applied to Python methods of a QObject that marks them
    as Qt slots.
    signature is a string specifying the C++ signature of the slot.
    result is type of the value returned by the slot.
    """
    pass

def pyqtSlot(*types, **keywords): # known case of PyQt4.QtCore.pyqtSlot
    """
    @pyqtSlot(*types, str name=None, str result=None)
    
    This is a decorator applied to Python methods of a QObject that marks them
    as Qt slots.
    The non-keyword arguments are the types of the slot arguments and each may
    be a Python type object or a string specifying a C++ type.
    name is the name of the slot and defaults to the name of the method.
    result is type of the value returned by the slot.
    """
    pass

def qAbs(p_float): # real signature unknown; restored from __doc__
    """ qAbs(float) -> float """
    return 0.0

def qAddPostRoutine(callable): # real signature unknown; restored from __doc__
    """ qAddPostRoutine(callable) """
    pass

def qChecksum(p_str): # real signature unknown; restored from __doc__
    """ qChecksum(str) -> int """
    return 0

def qCompress(QByteArray, int_compressionLevel=-1): # real signature unknown; restored from __doc__
    """ qCompress(QByteArray, int compressionLevel=-1) -> QByteArray """
    return QByteArray

def qCritical(p_str): # real signature unknown; restored from __doc__
    """ qCritical(str) """
    pass

def qDebug(p_str): # real signature unknown; restored from __doc__
    """ qDebug(str) """
    pass

def qErrnoWarning(p_int, p_str): # real signature unknown; restored from __doc__
    """
    qErrnoWarning(int, str)
    qErrnoWarning(str)
    """
    pass

def qFatal(p_str): # real signature unknown; restored from __doc__
    """ qFatal(str) """
    pass

def qFuzzyCompare(p_float, p_float_1): # real signature unknown; restored from __doc__
    """ qFuzzyCompare(float, float) -> bool """
    return False

def qInf(): # real signature unknown; restored from __doc__
    """ qInf() -> float """
    return 0.0

def qInstallMsgHandler(callable): # real signature unknown; restored from __doc__
    """ qInstallMsgHandler(callable) -> callable """
    pass

def qIsFinite(p_float): # real signature unknown; restored from __doc__
    """ qIsFinite(float) -> bool """
    return False

def qIsInf(p_float): # real signature unknown; restored from __doc__
    """ qIsInf(float) -> bool """
    return False

def qIsNaN(p_float): # real signature unknown; restored from __doc__
    """ qIsNaN(float) -> bool """
    return False

def qIsNull(p_float): # real signature unknown; restored from __doc__
    """ qIsNull(float) -> bool """
    return False

def qQNaN(): # real signature unknown; restored from __doc__
    """ qQNaN() -> float """
    return 0.0

def qrand(): # real signature unknown; restored from __doc__
    """ qrand() -> int """
    return 0

def qRegisterResourceData(p_int, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
    """ qRegisterResourceData(int, str, str, str) -> bool """
    return False

def qRemovePostRoutine(callable): # real signature unknown; restored from __doc__
    """ qRemovePostRoutine(callable) """
    pass

def qRound(p_float): # real signature unknown; restored from __doc__
    """ qRound(float) -> int """
    return 0

def qRound64(p_float): # real signature unknown; restored from __doc__
    """ qRound64(float) -> int """
    return 0

def qSetFieldWidth(p_int): # real signature unknown; restored from __doc__
    """ qSetFieldWidth(int) -> QTextStreamManipulator """
    return QTextStreamManipulator

def qSetPadChar(QChar): # real signature unknown; restored from __doc__
    """ qSetPadChar(QChar) -> QTextStreamManipulator """
    return QTextStreamManipulator

def qSetRealNumberPrecision(p_int): # real signature unknown; restored from __doc__
    """ qSetRealNumberPrecision(int) -> QTextStreamManipulator """
    return QTextStreamManipulator

def qSharedBuild(): # real signature unknown; restored from __doc__
    """ qSharedBuild() -> bool """
    return False

def qSNaN(): # real signature unknown; restored from __doc__
    """ qSNaN() -> float """
    return 0.0

def qsrand(p_int): # real signature unknown; restored from __doc__
    """ qsrand(int) """
    pass

def qSwap(QBitArray, QBitArray_1): # real signature unknown; restored from __doc__
    """
    qSwap(QBitArray, QBitArray)
    qSwap(QByteArray, QByteArray)
    qSwap(QString, QString)
    qSwap(QUrl, QUrl)
    qSwap(QVariant, QVariant)
    """
    pass

def QT_TRANSLATE_NOOP(p_str, p_str_1): # real signature unknown; restored from __doc__
    """ QT_TRANSLATE_NOOP(str, str) -> str """
    return ""

def QT_TR_NOOP(p_str): # real signature unknown; restored from __doc__
    """ QT_TR_NOOP(str) -> str """
    return ""

def QT_TR_NOOP_UTF8(p_str): # real signature unknown; restored from __doc__
    """ QT_TR_NOOP_UTF8(str) -> str """
    return ""

def qUncompress(QByteArray): # real signature unknown; restored from __doc__
    """ qUncompress(QByteArray) -> QByteArray """
    return QByteArray

def qUnregisterResourceData(p_int, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
    """ qUnregisterResourceData(int, str, str, str) -> bool """
    return False

def qVersion(): # real signature unknown; restored from __doc__
    """ qVersion() -> str """
    return ""

def qWarning(p_str): # real signature unknown; restored from __doc__
    """ qWarning(str) """
    pass

def Q_ARG(p_object, p_object_1): # real signature unknown; restored from __doc__
    """ Q_ARG(object, object) -> QGenericArgument """
    return QGenericArgument

def Q_CLASSINFO(p_str, p_str_1): # real signature unknown; restored from __doc__
    """ Q_CLASSINFO(str, str) """
    pass

def Q_ENUMS(*more): # real signature unknown; restored from __doc__
    """ Q_ENUMS(...) """
    pass

def Q_FLAGS(*more): # real signature unknown; restored from __doc__
    """ Q_FLAGS(...) """
    pass

def Q_RETURN_ARG(p_object): # real signature unknown; restored from __doc__
    """ Q_RETURN_ARG(object) -> QGenericReturnArgument """
    return QGenericReturnArgument

def reset(QTextStream): # real signature unknown; restored from __doc__
    """ reset(QTextStream) -> QTextStream """
    return QTextStream

def right(QTextStream): # real signature unknown; restored from __doc__
    """ right(QTextStream) -> QTextStream """
    return QTextStream

def scientific(QTextStream): # real signature unknown; restored from __doc__
    """ scientific(QTextStream) -> QTextStream """
    return QTextStream

def showbase(QTextStream): # real signature unknown; restored from __doc__
    """ showbase(QTextStream) -> QTextStream """
    return QTextStream

def SIGNAL(p_str): # real signature unknown; restored from __doc__
    """ SIGNAL(str) -> str """
    return ""

def SLOT(p_str): # real signature unknown; restored from __doc__
    """ SLOT(str) -> str """
    return ""

def uppercasebase(QTextStream): # real signature unknown; restored from __doc__
    """ uppercasebase(QTextStream) -> QTextStream """
    return QTextStream

def uppercasedigits(QTextStream): # real signature unknown; restored from __doc__
    """ uppercasedigits(QTextStream) -> QTextStream """
    return QTextStream

def ws(QTextStream): # real signature unknown; restored from __doc__
    """ ws(QTextStream) -> QTextStream """
    return QTextStream

# classes

from pyqtBoundSignal import pyqtBoundSignal
from pyqtProperty import pyqtProperty
from pyqtSignal import pyqtSignal
from pyqtWrapperType import pyqtWrapperType
from QObject import QObject
from QAbstractAnimation import QAbstractAnimation
from QAbstractEventDispatcher import QAbstractEventDispatcher
from QAbstractFileEngine import QAbstractFileEngine
from QAbstractFileEngineHandler import QAbstractFileEngineHandler
from QAbstractFileEngineIterator import QAbstractFileEngineIterator
from QAbstractItemModel import QAbstractItemModel
from QAbstractListModel import QAbstractListModel
from QAbstractState import QAbstractState
from QAbstractTableModel import QAbstractTableModel
from QAbstractTransition import QAbstractTransition
from QAnimationGroup import QAnimationGroup
from QBasicTimer import QBasicTimer
from QBitArray import QBitArray
from QIODevice import QIODevice
from QBuffer import QBuffer
from QByteArray import QByteArray
from QByteArrayMatcher import QByteArrayMatcher
from QChar import QChar
from QEvent import QEvent
from QChildEvent import QChildEvent
from QCoreApplication import QCoreApplication
from QCryptographicHash import QCryptographicHash
from QDataStream import QDataStream
from QDate import QDate
from QDateTime import QDateTime
from QDir import QDir
from QDirIterator import QDirIterator
from QDynamicPropertyChangeEvent import QDynamicPropertyChangeEvent
from QEasingCurve import QEasingCurve
from QElapsedTimer import QElapsedTimer
from QEventLoop import QEventLoop
from QEventTransition import QEventTransition
from QFile import QFile
from QFileInfo import QFileInfo
from QFileSystemWatcher import QFileSystemWatcher
from QFinalState import QFinalState
from QFSFileEngine import QFSFileEngine
from QGenericArgument import QGenericArgument
from QGenericReturnArgument import QGenericReturnArgument
from QHistoryState import QHistoryState
from QLatin1Char import QLatin1Char
from QLatin1String import QLatin1String
from QLibrary import QLibrary
from QLibraryInfo import QLibraryInfo
from QLine import QLine
from QLineF import QLineF
from QLocale import QLocale
from QMargins import QMargins
from QMetaClassInfo import QMetaClassInfo
from QMetaEnum import QMetaEnum
from QMetaMethod import QMetaMethod
from QMetaObject import QMetaObject
from QMetaProperty import QMetaProperty
from QMetaType import QMetaType
from QMimeData import QMimeData
from QModelIndex import QModelIndex
from QMutex import QMutex
from QMutexLocker import QMutexLocker
from QObjectCleanupHandler import QObjectCleanupHandler
from QParallelAnimationGroup import QParallelAnimationGroup
from QPauseAnimation import QPauseAnimation
from QPersistentModelIndex import QPersistentModelIndex
from QPluginLoader import QPluginLoader
from QPoint import QPoint
from QPointF import QPointF
from QProcess import QProcess
from QProcessEnvironment import QProcessEnvironment
from QVariantAnimation import QVariantAnimation
from QPropertyAnimation import QPropertyAnimation
from QReadLocker import QReadLocker
from QReadWriteLock import QReadWriteLock
from QRect import QRect
from QRectF import QRectF
from QRegExp import QRegExp
from QResource import QResource
from QRunnable import QRunnable
from QSemaphore import QSemaphore
from QSequentialAnimationGroup import QSequentialAnimationGroup
from QSettings import QSettings
from QSharedMemory import QSharedMemory
from QSignalMapper import QSignalMapper
from QSignalTransition import QSignalTransition
from QSize import QSize
from QSizeF import QSizeF
from QSocketNotifier import QSocketNotifier
from QState import QState
from QStateMachine import QStateMachine
from QString import QString
from QStringList import QStringList
from QStringMatcher import QStringMatcher
from QStringRef import QStringRef
from QSysInfo import QSysInfo
from QSystemLocale import QSystemLocale
from QSystemSemaphore import QSystemSemaphore
from Qt import Qt
from QTemporaryFile import QTemporaryFile
from QTextBoundaryFinder import QTextBoundaryFinder
from QTextCodec import QTextCodec
from QTextDecoder import QTextDecoder
from QTextEncoder import QTextEncoder
from QTextStream import QTextStream
from QTextStreamManipulator import QTextStreamManipulator
from QThread import QThread
from QThreadPool import QThreadPool
from QTime import QTime
from QTimeLine import QTimeLine
from QTimer import QTimer
from QTimerEvent import QTimerEvent
from QtMsgType import QtMsgType
from QTranslator import QTranslator
from QUrl import QUrl
from QUuid import QUuid
from QVariant import QVariant
from QWaitCondition import QWaitCondition
from QWriteLocker import QWriteLocker
from QXmlStreamAttribute import QXmlStreamAttribute
from QXmlStreamAttributes import QXmlStreamAttributes
from QXmlStreamEntityDeclaration import QXmlStreamEntityDeclaration
from QXmlStreamEntityResolver import QXmlStreamEntityResolver
from QXmlStreamNamespaceDeclaration import QXmlStreamNamespaceDeclaration
from QXmlStreamNotationDeclaration import QXmlStreamNotationDeclaration
from QXmlStreamReader import QXmlStreamReader
from QXmlStreamWriter import QXmlStreamWriter
# variables with complex values

PYQT_CONFIGURATION = {
    'sip_flags': '-x VendorID -t WS_X11 -x PyQt_NoPrintRangeBug -t Qt_4_8_6 -x Py_v3',
}


