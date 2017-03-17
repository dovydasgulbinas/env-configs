# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


# Variables with simple values

QWIDGETSIZE_MAX = 16777215

# functions

def qAlpha(p_int): # real signature unknown; restored from __doc__
    """ qAlpha(int) -> int """
    return 0

def qBlue(p_int): # real signature unknown; restored from __doc__
    """ qBlue(int) -> int """
    return 0

def qDrawBorderPixmap(QPainter, QRect, QMargins, QPixmap): # real signature unknown; restored from __doc__
    """ qDrawBorderPixmap(QPainter, QRect, QMargins, QPixmap) """
    pass

def qDrawPlainRect(QPainter, p_int, p_int_1, p_int_2, p_int_3, QColor, int_lineWidth=1, QBrush_fill=None): # real signature unknown; restored from __doc__
    """
    qDrawPlainRect(QPainter, int, int, int, int, QColor, int lineWidth=1, QBrush fill=None)
    qDrawPlainRect(QPainter, QRect, QColor, int lineWidth=1, QBrush fill=None)
    """
    pass

def qDrawShadeLine(QPainter, p_int, p_int_1, p_int_2, p_int_3, QPalette, bool_sunken=True, int_lineWidth=1, int_midLineWidth=0): # real signature unknown; restored from __doc__
    """
    qDrawShadeLine(QPainter, int, int, int, int, QPalette, bool sunken=True, int lineWidth=1, int midLineWidth=0)
    qDrawShadeLine(QPainter, QPoint, QPoint, QPalette, bool sunken=True, int lineWidth=1, int midLineWidth=0)
    """
    pass

def qDrawShadePanel(QPainter, p_int, p_int_1, p_int_2, p_int_3, QPalette, bool_sunken=False, int_lineWidth=1, QBrush_fill=None): # real signature unknown; restored from __doc__
    """
    qDrawShadePanel(QPainter, int, int, int, int, QPalette, bool sunken=False, int lineWidth=1, QBrush fill=None)
    qDrawShadePanel(QPainter, QRect, QPalette, bool sunken=False, int lineWidth=1, QBrush fill=None)
    """
    pass

def qDrawShadeRect(QPainter, p_int, p_int_1, p_int_2, p_int_3, QPalette, bool_sunken=False, int_lineWidth=1, int_midLineWidth=0, QBrush_fill=None): # real signature unknown; restored from __doc__
    """
    qDrawShadeRect(QPainter, int, int, int, int, QPalette, bool sunken=False, int lineWidth=1, int midLineWidth=0, QBrush fill=None)
    qDrawShadeRect(QPainter, QRect, QPalette, bool sunken=False, int lineWidth=1, int midLineWidth=0, QBrush fill=None)
    """
    pass

def qDrawWinButton(QPainter, p_int, p_int_1, p_int_2, p_int_3, QPalette, bool_sunken=False, QBrush_fill=None): # real signature unknown; restored from __doc__
    """
    qDrawWinButton(QPainter, int, int, int, int, QPalette, bool sunken=False, QBrush fill=None)
    qDrawWinButton(QPainter, QRect, QPalette, bool sunken=False, QBrush fill=None)
    """
    pass

def qDrawWinPanel(QPainter, p_int, p_int_1, p_int_2, p_int_3, QPalette, bool_sunken=False, QBrush_fill=None): # real signature unknown; restored from __doc__
    """
    qDrawWinPanel(QPainter, int, int, int, int, QPalette, bool sunken=False, QBrush fill=None)
    qDrawWinPanel(QPainter, QRect, QPalette, bool sunken=False, QBrush fill=None)
    """
    pass

def qFuzzyCompare(QMatrix, QMatrix_1): # real signature unknown; restored from __doc__
    """
    qFuzzyCompare(QMatrix, QMatrix) -> bool
    qFuzzyCompare(QMatrix4x4, QMatrix4x4) -> bool
    qFuzzyCompare(QQuaternion, QQuaternion) -> bool
    qFuzzyCompare(QTransform, QTransform) -> bool
    qFuzzyCompare(QVector2D, QVector2D) -> bool
    qFuzzyCompare(QVector3D, QVector3D) -> bool
    qFuzzyCompare(QVector4D, QVector4D) -> bool
    """
    return False

def qGray(p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
    """
    qGray(int, int, int) -> int
    qGray(int) -> int
    """
    return 0

def qGreen(p_int): # real signature unknown; restored from __doc__
    """ qGreen(int) -> int """
    return 0

def qIsGray(p_int): # real signature unknown; restored from __doc__
    """ qIsGray(int) -> bool """
    return False

def qRed(p_int): # real signature unknown; restored from __doc__
    """ qRed(int) -> int """
    return 0

def qRgb(p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
    """ qRgb(int, int, int) -> int """
    return 0

def qRgba(p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
    """ qRgba(int, int, int, int) -> int """
    return 0

def qSwap(QBitmap, QBitmap_1): # real signature unknown; restored from __doc__
    """
    qSwap(QBitmap, QBitmap)
    qSwap(QBrush, QBrush)
    qSwap(QIcon, QIcon)
    qSwap(QImage, QImage)
    qSwap(QKeySequence, QKeySequence)
    qSwap(QPen, QPen)
    qSwap(QPicture, QPicture)
    qSwap(QPixmap, QPixmap)
    """
    pass

def qt_x11_wait_for_window_manager(QWidget): # real signature unknown; restored from __doc__
    """ qt_x11_wait_for_window_manager(QWidget) """
    pass

# classes

from Display import Display
from QPaintDevice import QPaintDevice
from QWidget import QWidget
from QAbstractButton import QAbstractButton
from QGraphicsItem import QGraphicsItem
from QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem
from QAbstractItemDelegate import QAbstractItemDelegate
from QFrame import QFrame
from QAbstractScrollArea import QAbstractScrollArea
from QAbstractItemView import QAbstractItemView
from QDialog import QDialog
from QAbstractPrintDialog import QAbstractPrintDialog
from QAbstractProxyModel import QAbstractProxyModel
from QAbstractSlider import QAbstractSlider
from QAbstractSpinBox import QAbstractSpinBox
from QAbstractTextDocumentLayout import QAbstractTextDocumentLayout
from QAction import QAction
from QActionEvent import QActionEvent
from QActionGroup import QActionGroup
from QApplication import QApplication
from QPixmap import QPixmap
from QBitmap import QBitmap
from QLayoutItem import QLayoutItem
from QLayout import QLayout
from QBoxLayout import QBoxLayout
from QBrush import QBrush
from QButtonGroup import QButtonGroup
from QCalendarWidget import QCalendarWidget
from QCheckBox import QCheckBox
from QClipboard import QClipboard
from QCloseEvent import QCloseEvent
from QColor import QColor
from QColorDialog import QColorDialog
from QColumnView import QColumnView
from QComboBox import QComboBox
from QPushButton import QPushButton
from QCommandLinkButton import QCommandLinkButton
from QStyle import QStyle
from QCommonStyle import QCommonStyle
from QCompleter import QCompleter
from QGradient import QGradient
from QConicalGradient import QConicalGradient
from QInputEvent import QInputEvent
from QContextMenuEvent import QContextMenuEvent
from QCursor import QCursor
from QDataWidgetMapper import QDataWidgetMapper
from QDateTimeEdit import QDateTimeEdit
from QDateEdit import QDateEdit
from QDesktopServices import QDesktopServices
from QDesktopWidget import QDesktopWidget
from QDial import QDial
from QDialogButtonBox import QDialogButtonBox
from QDirModel import QDirModel
from QDockWidget import QDockWidget
from QDoubleSpinBox import QDoubleSpinBox
from QValidator import QValidator
from QDoubleValidator import QDoubleValidator
from QDrag import QDrag
from QMimeSource import QMimeSource
from QDropEvent import QDropEvent
from QDragMoveEvent import QDragMoveEvent
from QDragEnterEvent import QDragEnterEvent
from QDragLeaveEvent import QDragLeaveEvent
from QErrorMessage import QErrorMessage
from QFileDialog import QFileDialog
from QFileIconProvider import QFileIconProvider
from QFileOpenEvent import QFileOpenEvent
from QFileSystemModel import QFileSystemModel
from QFocusEvent import QFocusEvent
from QFocusFrame import QFocusFrame
from QFont import QFont
from QFontComboBox import QFontComboBox
from QFontDatabase import QFontDatabase
from QFontDialog import QFontDialog
from QFontInfo import QFontInfo
from QFontMetrics import QFontMetrics
from QFontMetricsF import QFontMetricsF
from QFormLayout import QFormLayout
from QGesture import QGesture
from QGestureEvent import QGestureEvent
from QGestureRecognizer import QGestureRecognizer
from QGlyphRun import QGlyphRun
from QGraphicsAnchor import QGraphicsAnchor
from QGraphicsLayoutItem import QGraphicsLayoutItem
from QGraphicsLayout import QGraphicsLayout
from QGraphicsAnchorLayout import QGraphicsAnchorLayout
from QGraphicsEffect import QGraphicsEffect
from QGraphicsBlurEffect import QGraphicsBlurEffect
from QGraphicsColorizeEffect import QGraphicsColorizeEffect
from QGraphicsDropShadowEffect import QGraphicsDropShadowEffect
from QGraphicsEllipseItem import QGraphicsEllipseItem
from QGraphicsGridLayout import QGraphicsGridLayout
from QGraphicsItemAnimation import QGraphicsItemAnimation
from QGraphicsItemGroup import QGraphicsItemGroup
from QGraphicsLinearLayout import QGraphicsLinearLayout
from QGraphicsLineItem import QGraphicsLineItem
from QGraphicsObject import QGraphicsObject
from QGraphicsOpacityEffect import QGraphicsOpacityEffect
from QGraphicsPathItem import QGraphicsPathItem
from QGraphicsPixmapItem import QGraphicsPixmapItem
from QGraphicsPolygonItem import QGraphicsPolygonItem
from QGraphicsWidget import QGraphicsWidget
from QGraphicsProxyWidget import QGraphicsProxyWidget
from QGraphicsRectItem import QGraphicsRectItem
from QGraphicsTransform import QGraphicsTransform
from QGraphicsRotation import QGraphicsRotation
from QGraphicsScale import QGraphicsScale
from QGraphicsScene import QGraphicsScene
from QGraphicsSceneEvent import QGraphicsSceneEvent
from QGraphicsSceneContextMenuEvent import QGraphicsSceneContextMenuEvent
from QGraphicsSceneDragDropEvent import QGraphicsSceneDragDropEvent
from QGraphicsSceneHelpEvent import QGraphicsSceneHelpEvent
from QGraphicsSceneHoverEvent import QGraphicsSceneHoverEvent
from QGraphicsSceneMouseEvent import QGraphicsSceneMouseEvent
from QGraphicsSceneMoveEvent import QGraphicsSceneMoveEvent
from QGraphicsSceneResizeEvent import QGraphicsSceneResizeEvent
from QGraphicsSceneWheelEvent import QGraphicsSceneWheelEvent
from QGraphicsSimpleTextItem import QGraphicsSimpleTextItem
from QGraphicsTextItem import QGraphicsTextItem
from QGraphicsView import QGraphicsView
from QGridLayout import QGridLayout
from QGroupBox import QGroupBox
from QHBoxLayout import QHBoxLayout
from QHeaderView import QHeaderView
from QHelpEvent import QHelpEvent
from QHideEvent import QHideEvent
from QHoverEvent import QHoverEvent
from QIcon import QIcon
from QIconDragEvent import QIconDragEvent
from QIconEngine import QIconEngine
from QIconEngineV2 import QIconEngineV2
from QIdentityProxyModel import QIdentityProxyModel
from QImage import QImage
from QImageIOHandler import QImageIOHandler
from QImageReader import QImageReader
from QImageWriter import QImageWriter
from QInputContext import QInputContext
from QInputContextFactory import QInputContextFactory
from QInputDialog import QInputDialog
from QInputMethodEvent import QInputMethodEvent
from QIntValidator import QIntValidator
from QItemDelegate import QItemDelegate
from QItemEditorCreatorBase import QItemEditorCreatorBase
from QItemEditorFactory import QItemEditorFactory
from QItemSelection import QItemSelection
from QItemSelectionModel import QItemSelectionModel
from QItemSelectionRange import QItemSelectionRange
from QKeyEvent import QKeyEvent
from QKeyEventTransition import QKeyEventTransition
from QKeySequence import QKeySequence
from QLabel import QLabel
from QLCDNumber import QLCDNumber
from QLinearGradient import QLinearGradient
from QLineEdit import QLineEdit
from QListView import QListView
from QListWidget import QListWidget
from QListWidgetItem import QListWidgetItem
from QMainWindow import QMainWindow
from QMatrix import QMatrix
from QMatrix2x2 import QMatrix2x2
from QMatrix2x3 import QMatrix2x3
from QMatrix2x4 import QMatrix2x4
from QMatrix3x2 import QMatrix3x2
from QMatrix3x3 import QMatrix3x3
from QMatrix3x4 import QMatrix3x4
from QMatrix4x2 import QMatrix4x2
from QMatrix4x3 import QMatrix4x3
from QMatrix4x4 import QMatrix4x4
from QMdiArea import QMdiArea
from QMdiSubWindow import QMdiSubWindow
from QMenu import QMenu
from QMenuBar import QMenuBar
from QMessageBox import QMessageBox
from QMouseEvent import QMouseEvent
from QMouseEventTransition import QMouseEventTransition
from QMoveEvent import QMoveEvent
from QMovie import QMovie
from QPageSetupDialog import QPageSetupDialog
from QPaintEngine import QPaintEngine
from QPaintEngineState import QPaintEngineState
from QPainter import QPainter
from QPainterPath import QPainterPath
from QPainterPathStroker import QPainterPathStroker
from QPaintEvent import QPaintEvent
from QPalette import QPalette
from QPanGesture import QPanGesture
from QPen import QPen
from QPicture import QPicture
from QPictureIO import QPictureIO
from QPinchGesture import QPinchGesture
from QPixmapCache import QPixmapCache
from QPlainTextDocumentLayout import QPlainTextDocumentLayout
from QPlainTextEdit import QPlainTextEdit
from QPolygon import QPolygon
from QPolygonF import QPolygonF
from QPrintDialog import QPrintDialog
from QPrintEngine import QPrintEngine
from QPrinter import QPrinter
from QPrinterInfo import QPrinterInfo
from QPrintPreviewDialog import QPrintPreviewDialog
from QPrintPreviewWidget import QPrintPreviewWidget
from QProgressBar import QProgressBar
from QProgressDialog import QProgressDialog
from QProxyModel import QProxyModel
from QTextObjectInterface import QTextObjectInterface
from QPyTextObject import QPyTextObject
from QQuaternion import QQuaternion
from QRadialGradient import QRadialGradient
from QRadioButton import QRadioButton
from QRawFont import QRawFont
from QRegExpValidator import QRegExpValidator
from QRegion import QRegion
from QResizeEvent import QResizeEvent
from QRubberBand import QRubberBand
from QScrollArea import QScrollArea
from QScrollBar import QScrollBar
from QSessionManager import QSessionManager
from QShortcut import QShortcut
from QShortcutEvent import QShortcutEvent
from QShowEvent import QShowEvent
from QSizeGrip import QSizeGrip
from QSizePolicy import QSizePolicy
from QSlider import QSlider
from QSortFilterProxyModel import QSortFilterProxyModel
from QSound import QSound
from QSpacerItem import QSpacerItem
from QSpinBox import QSpinBox
from QSplashScreen import QSplashScreen
from QSplitter import QSplitter
from QSplitterHandle import QSplitterHandle
from QStackedLayout import QStackedLayout
from QStackedWidget import QStackedWidget
from QStandardItem import QStandardItem
from QStandardItemModel import QStandardItemModel
from QStaticText import QStaticText
from QStatusBar import QStatusBar
from QStatusTipEvent import QStatusTipEvent
from QStringListModel import QStringListModel
from QStyledItemDelegate import QStyledItemDelegate
from QStyleFactory import QStyleFactory
from QStyleHintReturn import QStyleHintReturn
from QStyleHintReturnMask import QStyleHintReturnMask
from QStyleHintReturnVariant import QStyleHintReturnVariant
from QStyleOption import QStyleOption
from QStyleOptionButton import QStyleOptionButton
from QStyleOptionComplex import QStyleOptionComplex
from QStyleOptionComboBox import QStyleOptionComboBox
from QStyleOptionDockWidget import QStyleOptionDockWidget
from QStyleOptionDockWidgetV2 import QStyleOptionDockWidgetV2
from QStyleOptionFocusRect import QStyleOptionFocusRect
from QStyleOptionFrame import QStyleOptionFrame
from QStyleOptionFrameV2 import QStyleOptionFrameV2
from QStyleOptionFrameV3 import QStyleOptionFrameV3
from QStyleOptionGraphicsItem import QStyleOptionGraphicsItem
from QStyleOptionGroupBox import QStyleOptionGroupBox
from QStyleOptionHeader import QStyleOptionHeader
from QStyleOptionMenuItem import QStyleOptionMenuItem
from QStyleOptionProgressBar import QStyleOptionProgressBar
from QStyleOptionProgressBarV2 import QStyleOptionProgressBarV2
from QStyleOptionRubberBand import QStyleOptionRubberBand
from QStyleOptionSizeGrip import QStyleOptionSizeGrip
from QStyleOptionSlider import QStyleOptionSlider
from QStyleOptionSpinBox import QStyleOptionSpinBox
from QStyleOptionTab import QStyleOptionTab
from QStyleOptionTabBarBase import QStyleOptionTabBarBase
from QStyleOptionTabBarBaseV2 import QStyleOptionTabBarBaseV2
from QStyleOptionTabV2 import QStyleOptionTabV2
from QStyleOptionTabV3 import QStyleOptionTabV3
from QStyleOptionTabWidgetFrame import QStyleOptionTabWidgetFrame
from QStyleOptionTabWidgetFrameV2 import QStyleOptionTabWidgetFrameV2
from QStyleOptionTitleBar import QStyleOptionTitleBar
from QStyleOptionToolBar import QStyleOptionToolBar
from QStyleOptionToolBox import QStyleOptionToolBox
from QStyleOptionToolBoxV2 import QStyleOptionToolBoxV2
from QStyleOptionToolButton import QStyleOptionToolButton
from QStyleOptionViewItem import QStyleOptionViewItem
from QStyleOptionViewItemV2 import QStyleOptionViewItemV2
from QStyleOptionViewItemV3 import QStyleOptionViewItemV3
from QStyleOptionViewItemV4 import QStyleOptionViewItemV4
from QStylePainter import QStylePainter
from QSwipeGesture import QSwipeGesture
from QSyntaxHighlighter import QSyntaxHighlighter
from QSystemTrayIcon import QSystemTrayIcon
from QTabBar import QTabBar
from QTabletEvent import QTabletEvent
from QTableView import QTableView
from QTableWidget import QTableWidget
from QTableWidgetItem import QTableWidgetItem
from QTableWidgetSelectionRange import QTableWidgetSelectionRange
from QTabWidget import QTabWidget
from QTapAndHoldGesture import QTapAndHoldGesture
from QTapGesture import QTapGesture
from QTextBlock import QTextBlock
from QTextFormat import QTextFormat
from QTextBlockFormat import QTextBlockFormat
from QTextObject import QTextObject
from QTextBlockGroup import QTextBlockGroup
from QTextBlockUserData import QTextBlockUserData
from QTextEdit import QTextEdit
from QTextBrowser import QTextBrowser
from QTextCharFormat import QTextCharFormat
from QTextCursor import QTextCursor
from QTextDocument import QTextDocument
from QTextDocumentFragment import QTextDocumentFragment
from QTextDocumentWriter import QTextDocumentWriter
from QTextFragment import QTextFragment
from QTextFrame import QTextFrame
from QTextFrameFormat import QTextFrameFormat
from QTextImageFormat import QTextImageFormat
from QTextInlineObject import QTextInlineObject
from QTextItem import QTextItem
from QTextLayout import QTextLayout
from QTextLength import QTextLength
from QTextLine import QTextLine
from QTextList import QTextList
from QTextListFormat import QTextListFormat
from QTextOption import QTextOption
from QTextTable import QTextTable
from QTextTableCell import QTextTableCell
from QTextTableCellFormat import QTextTableCellFormat
from QTextTableFormat import QTextTableFormat
from QTimeEdit import QTimeEdit
from QToolBar import QToolBar
from QToolBox import QToolBox
from QToolButton import QToolButton
from QToolTip import QToolTip
from QTouchEvent import QTouchEvent
from QTransform import QTransform
from QTreeView import QTreeView
from QTreeWidget import QTreeWidget
from QTreeWidgetItem import QTreeWidgetItem
from QTreeWidgetItemIterator import QTreeWidgetItemIterator
from QUndoCommand import QUndoCommand
from QUndoGroup import QUndoGroup
from QUndoStack import QUndoStack
from QUndoView import QUndoView
from QVBoxLayout import QVBoxLayout
from QVector2D import QVector2D
from QVector3D import QVector3D
from QVector4D import QVector4D
from QWhatsThis import QWhatsThis
from QWhatsThisClickedEvent import QWhatsThisClickedEvent
from QWheelEvent import QWheelEvent
from QWidgetAction import QWidgetAction
from QWidgetItem import QWidgetItem
from QWindowStateChangeEvent import QWindowStateChangeEvent
from QWizard import QWizard
from QWizardPage import QWizardPage
from QWorkspace import QWorkspace
from QX11EmbedContainer import QX11EmbedContainer
from QX11EmbedWidget import QX11EmbedWidget
from QX11Info import QX11Info
# variables with complex values


