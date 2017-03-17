# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QStyle(__PyQt4_QtCore.QObject):
    """ QStyle() """
    def alignedRect(self, Qt_LayoutDirection, Qt_Alignment, QSize, QRect): # real signature unknown; restored from __doc__
        """ QStyle.alignedRect(Qt.LayoutDirection, Qt.Alignment, QSize, QRect) -> QRect """
        pass

    def combinedLayoutSpacing(self, QSizePolicy_ControlTypes, QSizePolicy_ControlTypes_1, Qt_Orientation, QStyleOption_option=None, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.combinedLayoutSpacing(QSizePolicy.ControlTypes, QSizePolicy.ControlTypes, Qt.Orientation, QStyleOption option=None, QWidget widget=None) -> int """
        return 0

    def drawComplexControl(self, QStyle_ComplexControl, QStyleOptionComplex, QPainter, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.drawComplexControl(QStyle.ComplexControl, QStyleOptionComplex, QPainter, QWidget widget=None) """
        pass

    def drawControl(self, QStyle_ControlElement, QStyleOption, QPainter, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.drawControl(QStyle.ControlElement, QStyleOption, QPainter, QWidget widget=None) """
        pass

    def drawItemPixmap(self, QPainter, QRect, p_int, QPixmap): # real signature unknown; restored from __doc__
        """ QStyle.drawItemPixmap(QPainter, QRect, int, QPixmap) """
        pass

    def drawItemText(self, QPainter, QRect, p_int, QPalette, bool, QString, QPalette_ColorRole_textRole=None): # real signature unknown; restored from __doc__
        """ QStyle.drawItemText(QPainter, QRect, int, QPalette, bool, QString, QPalette.ColorRole textRole=QPalette.NoRole) """
        pass

    def drawPrimitive(self, QStyle_PrimitiveElement, QStyleOption, QPainter, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.drawPrimitive(QStyle.PrimitiveElement, QStyleOption, QPainter, QWidget widget=None) """
        pass

    def generatedIconPixmap(self, QIcon_Mode, QPixmap, QStyleOption): # real signature unknown; restored from __doc__
        """ QStyle.generatedIconPixmap(QIcon.Mode, QPixmap, QStyleOption) -> QPixmap """
        return QPixmap

    def hitTestComplexControl(self, QStyle_ComplexControl, QStyleOptionComplex, QPoint, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.hitTestComplexControl(QStyle.ComplexControl, QStyleOptionComplex, QPoint, QWidget widget=None) -> QStyle.SubControl """
        pass

    def itemPixmapRect(self, QRect, p_int, QPixmap): # real signature unknown; restored from __doc__
        """ QStyle.itemPixmapRect(QRect, int, QPixmap) -> QRect """
        pass

    def itemTextRect(self, QFontMetrics, QRect, p_int, bool, QString): # real signature unknown; restored from __doc__
        """ QStyle.itemTextRect(QFontMetrics, QRect, int, bool, QString) -> QRect """
        pass

    def layoutSpacing(self, QSizePolicy_ControlType, QSizePolicy_ControlType_1, Qt_Orientation, QStyleOption_option=None, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.layoutSpacing(QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation, QStyleOption option=None, QWidget widget=None) -> int """
        return 0

    def layoutSpacingImplementation(self, QSizePolicy_ControlType, QSizePolicy_ControlType_1, Qt_Orientation, QStyleOption_option=None, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.layoutSpacingImplementation(QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation, QStyleOption option=None, QWidget widget=None) -> int """
        return 0

    def pixelMetric(self, QStyle_PixelMetric, QStyleOption_option=None, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.pixelMetric(QStyle.PixelMetric, QStyleOption option=None, QWidget widget=None) -> int """
        return 0

    def polish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStyle.polish(QWidget)
        QStyle.polish(QApplication)
        QStyle.polish(QPalette) -> QPalette
        """
        return QPalette

    def proxy(self): # real signature unknown; restored from __doc__
        """ QStyle.proxy() -> QStyle """
        return QStyle

    def sizeFromContents(self, QStyle_ContentsType, QStyleOption, QSize, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.sizeFromContents(QStyle.ContentsType, QStyleOption, QSize, QWidget widget=None) -> QSize """
        pass

    def sliderPositionFromValue(self, p_int, p_int_1, p_int_2, p_int_3, bool_upsideDown=False): # real signature unknown; restored from __doc__
        """ QStyle.sliderPositionFromValue(int, int, int, int, bool upsideDown=False) -> int """
        return 0

    def sliderValueFromPosition(self, p_int, p_int_1, p_int_2, p_int_3, bool_upsideDown=False): # real signature unknown; restored from __doc__
        """ QStyle.sliderValueFromPosition(int, int, int, int, bool upsideDown=False) -> int """
        return 0

    def standardIcon(self, QStyle_StandardPixmap, QStyleOption_option=None, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.standardIcon(QStyle.StandardPixmap, QStyleOption option=None, QWidget widget=None) -> QIcon """
        return QIcon

    def standardIconImplementation(self, QStyle_StandardPixmap, QStyleOption_option=None, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.standardIconImplementation(QStyle.StandardPixmap, QStyleOption option=None, QWidget widget=None) -> QIcon """
        return QIcon

    def standardPalette(self): # real signature unknown; restored from __doc__
        """ QStyle.standardPalette() -> QPalette """
        return QPalette

    def standardPixmap(self, QStyle_StandardPixmap, QStyleOption_option=None, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.standardPixmap(QStyle.StandardPixmap, QStyleOption option=None, QWidget widget=None) -> QPixmap """
        return QPixmap

    def styleHint(self, QStyle_StyleHint, QStyleOption_option=None, QWidget_widget=None, QStyleHintReturn_returnData=None): # real signature unknown; restored from __doc__
        """ QStyle.styleHint(QStyle.StyleHint, QStyleOption option=None, QWidget widget=None, QStyleHintReturn returnData=None) -> int """
        return 0

    def subControlRect(self, QStyle_ComplexControl, QStyleOptionComplex, QStyle_SubControl, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.subControlRect(QStyle.ComplexControl, QStyleOptionComplex, QStyle.SubControl, QWidget widget=None) -> QRect """
        pass

    def subElementRect(self, QStyle_SubElement, QStyleOption, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QStyle.subElementRect(QStyle.SubElement, QStyleOption, QWidget widget=None) -> QRect """
        pass

    def unpolish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStyle.unpolish(QWidget)
        QStyle.unpolish(QApplication)
        """
        pass

    def visualAlignment(self, Qt_LayoutDirection, Qt_Alignment): # real signature unknown; restored from __doc__
        """ QStyle.visualAlignment(Qt.LayoutDirection, Qt.Alignment) -> Qt.Alignment """
        pass

    def visualPos(self, Qt_LayoutDirection, QRect, QPoint): # real signature unknown; restored from __doc__
        """ QStyle.visualPos(Qt.LayoutDirection, QRect, QPoint) -> QPoint """
        pass

    def visualRect(self, Qt_LayoutDirection, QRect, QRect_1): # real signature unknown; restored from __doc__
        """ QStyle.visualRect(Qt.LayoutDirection, QRect, QRect) -> QRect """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    CC_ComboBox = 1
    CC_CustomBase = -268435456
    CC_Dial = 7
    CC_GroupBox = 8
    CC_MdiControls = 9
    CC_Q3ListView = 6
    CC_ScrollBar = 2
    CC_Slider = 3
    CC_SpinBox = 0
    CC_TitleBar = 5
    CC_ToolButton = 4
    CE_CheckBox = 3
    CE_CheckBoxLabel = 4
    CE_ColumnViewGrip = 45
    CE_ComboBoxLabel = 40
    CE_CustomBase = -268435456
    CE_DockWidgetTitle = 31
    CE_FocusFrame = 39
    CE_Header = 23
    CE_HeaderEmptyArea = 44
    CE_HeaderLabel = 25
    CE_HeaderSection = 24
    CE_ItemViewItem = 46
    CE_MenuBarEmptyArea = 21
    CE_MenuBarItem = 20
    CE_MenuEmptyArea = 19
    CE_MenuHMargin = 17
    CE_MenuItem = 14
    CE_MenuScroller = 15
    CE_MenuTearoff = 18
    CE_MenuVMargin = 16
    CE_ProgressBar = 10
    CE_ProgressBarContents = 12
    CE_ProgressBarGroove = 11
    CE_ProgressBarLabel = 13
    CE_PushButton = 0
    CE_PushButtonBevel = 1
    CE_PushButtonLabel = 2
    CE_Q3DockWindowEmptyArea = 26
    CE_RadioButton = 5
    CE_RadioButtonLabel = 6
    CE_RubberBand = 30
    CE_ScrollBarAddLine = 32
    CE_ScrollBarAddPage = 34
    CE_ScrollBarFirst = 37
    CE_ScrollBarLast = 38
    CE_ScrollBarSlider = 36
    CE_ScrollBarSubLine = 33
    CE_ScrollBarSubPage = 35
    CE_ShapedFrame = 47
    CE_SizeGrip = 28
    CE_Splitter = 29
    CE_TabBarTab = 7
    CE_TabBarTabLabel = 9
    CE_TabBarTabShape = 8
    CE_ToolBar = 41
    CE_ToolBoxTab = 27
    CE_ToolBoxTabLabel = 43
    CE_ToolBoxTabShape = 42
    CE_ToolButtonLabel = 22
    CT_CheckBox = 1
    CT_ComboBox = 4
    CT_CustomBase = -268435456
    CT_DialogButtons = 20
    CT_GroupBox = 22
    CT_HeaderSection = 21
    CT_ItemViewItem = 24
    CT_LineEdit = 16
    CT_MdiControls = 23
    CT_Menu = 11
    CT_MenuBar = 10
    CT_MenuBarItem = 9
    CT_MenuItem = 8
    CT_ProgressBar = 7
    CT_PushButton = 0
    CT_Q3DockWindow = 6
    CT_Q3Header = 15
    CT_RadioButton = 2
    CT_ScrollBar = 14
    CT_SizeGrip = 18
    CT_Slider = 13
    CT_SpinBox = 17
    CT_Splitter = 5
    CT_TabBarTab = 12
    CT_TabWidget = 19
    CT_ToolButton = 3
    PE_CustomBase = 251658240
    PE_Frame = 5
    PE_FrameButtonBevel = 15
    PE_FrameButtonTool = 16
    PE_FrameDefaultButton = 6
    PE_FrameDockWidget = 7
    PE_FrameFocusRect = 8
    PE_FrameGroupBox = 9
    PE_FrameLineEdit = 10
    PE_FrameMenu = 11
    PE_FrameStatusBar = 12
    PE_FrameStatusBarItem = 12
    PE_FrameTabBarBase = 17
    PE_FrameTabWidget = 13
    PE_FrameWindow = 14
    PE_IndicatorArrowDown = 24
    PE_IndicatorArrowLeft = 25
    PE_IndicatorArrowRight = 26
    PE_IndicatorArrowUp = 27
    PE_IndicatorBranch = 28
    PE_IndicatorButtonDropDown = 29
    PE_IndicatorCheckBox = 31
    PE_IndicatorColumnViewArrow = 47
    PE_IndicatorDockWidgetResizeHandle = 32
    PE_IndicatorHeaderArrow = 33
    PE_IndicatorItemViewItemCheck = 30
    PE_IndicatorItemViewItemDrop = 48
    PE_IndicatorMenuCheckMark = 34
    PE_IndicatorProgressChunk = 35
    PE_IndicatorRadioButton = 36
    PE_IndicatorSpinDown = 37
    PE_IndicatorSpinMinus = 38
    PE_IndicatorSpinPlus = 39
    PE_IndicatorSpinUp = 40
    PE_IndicatorTabClose = 52
    PE_IndicatorTabTear = 44
    PE_IndicatorToolBarHandle = 41
    PE_IndicatorToolBarSeparator = 42
    PE_IndicatorViewItemCheck = 30
    PE_PanelButtonBevel = 19
    PE_PanelButtonCommand = 18
    PE_PanelButtonTool = 20
    PE_PanelItemViewItem = 49
    PE_PanelItemViewRow = 50
    PE_PanelLineEdit = 23
    PE_PanelMenu = 53
    PE_PanelMenuBar = 21
    PE_PanelScrollAreaCorner = 45
    PE_PanelStatusBar = 51
    PE_PanelTipLabel = 43
    PE_PanelToolBar = 22
    PE_Q3CheckListController = 0
    PE_Q3CheckListExclusiveIndicator = 1
    PE_Q3CheckListIndicator = 2
    PE_Q3DockWindowSeparator = 3
    PE_Q3Separator = 4
    PE_Widget = 46
    PM_ButtonDefaultIndicator = 1
    PM_ButtonIconSize = 77
    PM_ButtonMargin = 0
    PM_ButtonShiftHorizontal = 3
    PM_ButtonShiftVertical = 4
    PM_CheckBoxLabelSpacing = 72
    PM_CheckListButtonSize = 41
    PM_CheckListControllerSize = 42
    PM_ComboBoxFrameWidth = 7
    PM_CustomBase = -268435456
    PM_DefaultChildMargin = 62
    PM_DefaultFrameWidth = 5
    PM_DefaultLayoutSpacing = 63
    PM_DefaultTopLevelMargin = 61
    PM_DialogButtonsButtonHeight = 45
    PM_DialogButtonsButtonWidth = 44
    PM_DialogButtonsSeparator = 43
    PM_DockWidgetFrameWidth = 18
    PM_DockWidgetHandleExtent = 17
    PM_DockWidgetSeparatorExtent = 16
    PM_DockWidgetTitleBarButtonMargin = 78
    PM_DockWidgetTitleMargin = 75
    PM_ExclusiveIndicatorHeight = 40
    PM_ExclusiveIndicatorWidth = 39
    PM_FocusFrameHMargin = 70
    PM_FocusFrameVMargin = 69
    PM_HeaderGripMargin = 50
    PM_HeaderMargin = 48
    PM_HeaderMarkSize = 49
    PM_IconViewIconSize = 66
    PM_IndicatorHeight = 38
    PM_IndicatorWidth = 37
    PM_LargeIconSize = 68
    PM_LayoutBottomMargin = 83
    PM_LayoutHorizontalSpacing = 84
    PM_LayoutLeftMargin = 80
    PM_LayoutRightMargin = 82
    PM_LayoutTopMargin = 81
    PM_LayoutVerticalSpacing = 85
    PM_ListViewIconSize = 65
    PM_MaximumDragDistance = 8
    PM_MDIFrameWidth = 46
    PM_MDIMinimizedWidth = 47
    PM_MdiSubWindowFrameWidth = 46
    PM_MdiSubWindowMinimizedWidth = 47
    PM_MenuBarHMargin = 36
    PM_MenuBarItemSpacing = 34
    PM_MenuBarPanelWidth = 33
    PM_MenuBarVMargin = 35
    PM_MenuButtonIndicator = 2
    PM_MenuDesktopFrameWidth = 32
    PM_MenuHMargin = 28
    PM_MenuPanelWidth = 30
    PM_MenuScrollerHeight = 27
    PM_MenuTearoffHeight = 31
    PM_MenuVMargin = 29
    PM_MessageBoxIconSize = 76
    PM_ProgressBarChunkWidth = 24
    PM_RadioButtonLabelSpacing = 79
    PM_ScrollBarExtent = 9
    PM_ScrollBarSliderMin = 10
    PM_ScrollView_ScrollBarSpacing = 90
    PM_SizeGripSize = 74
    PM_SliderControlThickness = 12
    PM_SliderLength = 13
    PM_SliderSpaceAvailable = 15
    PM_SliderThickness = 11
    PM_SliderTickmarkOffset = 14
    PM_SmallIconSize = 67
    PM_SpinBoxFrameWidth = 6
    PM_SpinBoxSliderHeight = 60
    PM_SplitterWidth = 25
    PM_SubMenuOverlap = 91
    PM_TabBarBaseHeight = 22
    PM_TabBarBaseOverlap = 23
    PM_TabBarIconSize = 73
    PM_TabBarScrollButtonWidth = 53
    PM_TabBarTabHSpace = 20
    PM_TabBarTabOverlap = 19
    PM_TabBarTabShiftHorizontal = 51
    PM_TabBarTabShiftVertical = 52
    PM_TabBarTabVSpace = 21
    PM_TabBar_ScrollButtonOverlap = 86
    PM_TabCloseIndicatorHeight = 89
    PM_TabCloseIndicatorWidth = 88
    PM_TextCursorWidth = 87
    PM_TitleBarHeight = 26
    PM_ToolBarExtensionExtent = 59
    PM_ToolBarFrameWidth = 54
    PM_ToolBarHandleExtent = 55
    PM_ToolBarIconSize = 64
    PM_ToolBarItemMargin = 57
    PM_ToolBarItemSpacing = 56
    PM_ToolBarSeparatorExtent = 58
    PM_ToolTipLabelFrameWidth = 71
    RSIP_OnMouseClick = 1
    RSIP_OnMouseClickAndAlreadyFocused = 0
    SC_All = -1
    SC_ComboBoxArrow = 4
    SC_ComboBoxEditField = 2
    SC_ComboBoxFrame = 1
    SC_ComboBoxListBoxPopup = 8
    SC_CustomBase = -268435456
    SC_DialGroove = 1
    SC_DialHandle = 2
    SC_DialTickmarks = 4
    SC_GroupBoxCheckBox = 1
    SC_GroupBoxContents = 4
    SC_GroupBoxFrame = 8
    SC_GroupBoxLabel = 2
    SC_MdiCloseButton = 4
    SC_MdiMinButton = 1
    SC_MdiNormalButton = 2
    SC_None = 0
    SC_Q3ListView = 1
    SC_Q3ListViewBranch = 2
    SC_Q3ListViewExpand = 4
    SC_ScrollBarAddLine = 1
    SC_ScrollBarAddPage = 4
    SC_ScrollBarFirst = 16
    SC_ScrollBarGroove = 128
    SC_ScrollBarLast = 32
    SC_ScrollBarSlider = 64
    SC_ScrollBarSubLine = 2
    SC_ScrollBarSubPage = 8
    SC_SliderGroove = 1
    SC_SliderHandle = 2
    SC_SliderTickmarks = 4
    SC_SpinBoxDown = 2
    SC_SpinBoxEditField = 8
    SC_SpinBoxFrame = 4
    SC_SpinBoxUp = 1
    SC_TitleBarCloseButton = 8
    SC_TitleBarContextHelpButton = 128
    SC_TitleBarLabel = 256
    SC_TitleBarMaxButton = 4
    SC_TitleBarMinButton = 2
    SC_TitleBarNormalButton = 16
    SC_TitleBarShadeButton = 32
    SC_TitleBarSysMenu = 1
    SC_TitleBarUnshadeButton = 64
    SC_ToolButton = 1
    SC_ToolButtonMenu = 2
    SE_CheckBoxClickRect = 5
    SE_CheckBoxContents = 3
    SE_CheckBoxFocusRect = 4
    SE_CheckBoxIndicator = 2
    SE_CheckBoxLayoutItem = 42
    SE_ComboBoxFocusRect = 10
    SE_ComboBoxLayoutItem = 43
    SE_CustomBase = -268435456
    SE_DateTimeEditLayoutItem = 44
    SE_DialogButtonAbort = 21
    SE_DialogButtonAccept = 16
    SE_DialogButtonAll = 20
    SE_DialogButtonApply = 18
    SE_DialogButtonBoxLayoutItem = 45
    SE_DialogButtonCustom = 24
    SE_DialogButtonHelp = 19
    SE_DialogButtonIgnore = 22
    SE_DialogButtonReject = 17
    SE_DialogButtonRetry = 23
    SE_DockWidgetCloseButton = 38
    SE_DockWidgetFloatButton = 39
    SE_DockWidgetIcon = 41
    SE_DockWidgetTitleBarText = 40
    SE_FrameContents = 37
    SE_FrameLayoutItem = 53
    SE_GroupBoxLayoutItem = 54
    SE_HeaderArrow = 27
    SE_HeaderLabel = 26
    SE_ItemViewItemCheckIndicator = 33
    SE_ItemViewItemDecoration = 56
    SE_ItemViewItemFocusRect = 58
    SE_ItemViewItemText = 57
    SE_LabelLayoutItem = 46
    SE_LineEditContents = 36
    SE_ProgressBarContents = 14
    SE_ProgressBarGroove = 13
    SE_ProgressBarLabel = 15
    SE_ProgressBarLayoutItem = 47
    SE_PushButtonContents = 0
    SE_PushButtonFocusRect = 1
    SE_PushButtonLayoutItem = 48
    SE_Q3DockWindowHandleRect = 12
    SE_RadioButtonClickRect = 9
    SE_RadioButtonContents = 7
    SE_RadioButtonFocusRect = 8
    SE_RadioButtonIndicator = 6
    SE_RadioButtonLayoutItem = 49
    SE_ShapedFrameContents = 62
    SE_SliderFocusRect = 11
    SE_SliderLayoutItem = 50
    SE_SpinBoxLayoutItem = 51
    SE_TabBarTabLeftButton = 59
    SE_TabBarTabRightButton = 60
    SE_TabBarTabText = 61
    SE_TabBarTearIndicator = 34
    SE_TabWidgetLayoutItem = 55
    SE_TabWidgetLeftCorner = 31
    SE_TabWidgetRightCorner = 32
    SE_TabWidgetTabBar = 28
    SE_TabWidgetTabContents = 30
    SE_TabWidgetTabPane = 29
    SE_ToolBarHandle = 63
    SE_ToolBoxTabContents = 25
    SE_ToolButtonLayoutItem = 52
    SE_TreeViewDisclosureItem = 35
    SE_ViewItemCheckIndicator = 33
    SH_BlinkCursorWhenTextSelected = 28
    SH_Button_FocusPolicy = 49
    SH_ComboBox_LayoutDirection = 59
    SH_ComboBox_ListMouseTracking = 19
    SH_ComboBox_Popup = 25
    SH_ComboBox_PopupFrameStyle = 70
    SH_CustomBase = -268435456
    SH_DialogButtonBox_ButtonsHaveIcons = 72
    SH_DialogButtonLayout = 69
    SH_DialogButtons_DefaultButton = 36
    SH_Dial_BackgroundRole = 58
    SH_DitherDisabledText = 1
    SH_DockWidget_ButtonsHaveFrame = 95
    SH_DrawMenuBarSeparator = 47
    SH_EtchDisabledText = 0
    SH_FocusFrame_AboveWidget = 78
    SH_FocusFrame_Mask = 54
    SH_FontDialog_SelectAssociatedText = 13
    SH_FormLayoutFieldGrowthPolicy = 90
    SH_FormLayoutFormAlignment = 91
    SH_FormLayoutLabelAlignment = 92
    SH_FormLayoutWrapPolicy = 87
    SH_GroupBox_TextLabelColor = 32
    SH_GroupBox_TextLabelVerticalAlignment = 31
    SH_Header_ArrowAlignment = 6
    SH_ItemView_ActivateItemOnSingleClick = 62
    SH_ItemView_ArrowKeysNavigateIntoChildren = 81
    SH_ItemView_ChangeHighlightOnFocus = 22
    SH_ItemView_DrawDelegateFrame = 93
    SH_ItemView_EllipsisLocation = 60
    SH_ItemView_MovementWithoutUpdatingSelection = 76
    SH_ItemView_PaintAlternatingRowColorsForEmptyArea = 86
    SH_ItemView_ShowDecorationSelected = 61
    SH_LineEdit_PasswordCharacter = 35
    SH_MainWindow_SpaceBelowMenuBar = 12
    SH_MenuBar_AltKeyNavigation = 18
    SH_MenuBar_DismissOnSecondClick = 50
    SH_MenuBar_MouseTracking = 21
    SH_Menu_AllowActiveAndDisabled = 14
    SH_Menu_FadeOutOnHide = 84
    SH_Menu_FillScreenWithScroll = 45
    SH_Menu_FlashTriggeredItem = 83
    SH_Menu_KeyboardSearch = 67
    SH_Menu_Mask = 82
    SH_Menu_MouseTracking = 20
    SH_Menu_Scrollable = 30
    SH_Menu_SelectionWrap = 75
    SH_Menu_SloppySubMenus = 33
    SH_Menu_SpaceActivatesItem = 15
    SH_Menu_SubMenuPopupDelay = 16
    SH_MessageBox_CenterButtons = 74
    SH_MessageBox_TextInteractionFlags = 71
    SH_MessageBox_UseBorderForButtonSpacing = 51
    SH_PrintDialog_RightAlignButtons = 11
    SH_ProgressDialog_CenterCancelButton = 9
    SH_ProgressDialog_TextLabelAlignment = 10
    SH_Q3ListViewExpand_SelectMouseType = 40
    SH_RequestSoftwareInputPanel = 97
    SH_RichText_FullWidthSelection = 29
    SH_RubberBand_Mask = 55
    SH_ScrollBar_ContextMenu = 63
    SH_ScrollBar_LeftClickAbsolutePosition = 39
    SH_ScrollBar_MiddleClickAbsolutePosition = 2
    SH_ScrollBar_RollBetweenButtons = 64
    SH_ScrollBar_ScrollWhenPointerLeavesControl = 3
    SH_ScrollBar_StopMouseOverSlider = 27
    SH_ScrollView_FrameOnlyAroundContents = 17
    SH_Slider_AbsoluteSetButtons = 65
    SH_Slider_PageSetButtons = 66
    SH_Slider_SloppyKeyEvents = 8
    SH_Slider_SnapToValue = 7
    SH_Slider_StopMouseOverSlider = 27
    SH_SpellCheckUnderlineStyle = 73
    SH_SpinBox_AnimateButton = 42
    SH_SpinBox_ClickAutoRepeatRate = 44
    SH_SpinBox_ClickAutoRepeatThreshold = 85
    SH_SpinBox_KeyPressAutoRepeatRate = 43
    SH_SpinControls_DisableOnBounds = 57
    SH_TabBar_Alignment = 5
    SH_TabBar_CloseButtonPosition = 94
    SH_TabBar_ElideMode = 68
    SH_TabBar_PreferNoArrows = 38
    SH_TabBar_SelectMouseType = 4
    SH_Table_GridLineColor = 34
    SH_TabWidget_DefaultTabPosition = 88
    SH_TextControl_FocusIndicatorTextCharFormat = 79
    SH_TitleBar_AutoRaise = 52
    SH_TitleBar_ModifyNotification = 48
    SH_TitleBar_NoBorder = 26
    SH_ToolBar_Movable = 89
    SH_ToolBox_SelectedPageTitleBold = 37
    SH_ToolButtonStyle = 96
    SH_ToolButton_PopupDelay = 53
    SH_ToolTipLabel_Opacity = 46
    SH_ToolTip_Mask = 77
    SH_UnderlineShortcut = 41
    SH_Widget_ShareActivation = 23
    SH_WindowFrame_Mask = 56
    SH_WizardStyle = 80
    SH_Workspace_FillSpaceOnMaximize = 24
    SP_ArrowBack = 53
    SP_ArrowDown = 50
    SP_ArrowForward = 54
    SP_ArrowLeft = 51
    SP_ArrowRight = 52
    SP_ArrowUp = 49
    SP_BrowserReload = 58
    SP_BrowserStop = 59
    SP_CommandLink = 56
    SP_ComputerIcon = 15
    SP_CustomBase = -268435456
    SP_DesktopIcon = 13
    SP_DialogApplyButton = 44
    SP_DialogCancelButton = 39
    SP_DialogCloseButton = 43
    SP_DialogDiscardButton = 46
    SP_DialogHelpButton = 40
    SP_DialogNoButton = 48
    SP_DialogOkButton = 38
    SP_DialogOpenButton = 41
    SP_DialogResetButton = 45
    SP_DialogSaveButton = 42
    SP_DialogYesButton = 47
    SP_DirClosedIcon = 22
    SP_DirHomeIcon = 55
    SP_DirIcon = 37
    SP_DirLinkIcon = 23
    SP_DirOpenIcon = 21
    SP_DockWidgetCloseButton = 8
    SP_DriveCDIcon = 18
    SP_DriveDVDIcon = 19
    SP_DriveFDIcon = 16
    SP_DriveHDIcon = 17
    SP_DriveNetIcon = 20
    SP_FileDialogBack = 36
    SP_FileDialogContentsView = 34
    SP_FileDialogDetailedView = 32
    SP_FileDialogEnd = 29
    SP_FileDialogInfoView = 33
    SP_FileDialogListView = 35
    SP_FileDialogNewFolder = 31
    SP_FileDialogStart = 28
    SP_FileDialogToParent = 30
    SP_FileIcon = 24
    SP_FileLinkIcon = 25
    SP_MediaPause = 62
    SP_MediaPlay = 60
    SP_MediaSeekBackward = 66
    SP_MediaSeekForward = 65
    SP_MediaSkipBackward = 64
    SP_MediaSkipForward = 63
    SP_MediaStop = 61
    SP_MediaVolume = 67
    SP_MediaVolumeMuted = 68
    SP_MessageBoxCritical = 11
    SP_MessageBoxInformation = 9
    SP_MessageBoxQuestion = 12
    SP_MessageBoxWarning = 10
    SP_TitleBarCloseButton = 3
    SP_TitleBarContextHelpButton = 7
    SP_TitleBarMaxButton = 2
    SP_TitleBarMenuButton = 0
    SP_TitleBarMinButton = 1
    SP_TitleBarNormalButton = 4
    SP_TitleBarShadeButton = 5
    SP_TitleBarUnshadeButton = 6
    SP_ToolBarHorizontalExtensionButton = 26
    SP_ToolBarVerticalExtensionButton = 27
    SP_TrashIcon = 14
    SP_VistaShield = 57
    State_Active = 65536
    State_AutoRaise = 4096
    State_Bottom = 1024
    State_Children = 524288
    State_DownArrow = 64
    State_Editing = 4194304
    State_Enabled = 1
    State_FocusAtBorder = 2048
    State_HasFocus = 256
    State_Horizontal = 128
    State_Item = 1048576
    State_KeyboardFocusChange = 8388608
    State_Mini = 134217728
    State_MouseOver = 8192
    State_NoChange = 16
    State_None = 0
    State_Off = 8
    State_On = 32
    State_Open = 262144
    State_Raised = 2
    State_ReadOnly = 33554432
    State_Selected = 32768
    State_Sibling = 2097152
    State_Small = 67108864
    State_Sunken = 4
    State_Top = 512
    State_UpArrow = 16384
    State_Window = 131072


