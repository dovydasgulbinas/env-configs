# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QEvent(): # skipped bases: <type 'sip.wrapper'>
    """
    QEvent(QEvent.Type)
    QEvent(QEvent)
    """
    def accept(self): # real signature unknown; restored from __doc__
        """ QEvent.accept() """
        pass

    def ignore(self): # real signature unknown; restored from __doc__
        """ QEvent.ignore() """
        pass

    def isAccepted(self): # real signature unknown; restored from __doc__
        """ QEvent.isAccepted() -> bool """
        return False

    def registerEventType(self, int_hint=-1): # real signature unknown; restored from __doc__
        """ QEvent.registerEventType(int hint=-1) -> int """
        return 0

    def setAccepted(self, bool): # real signature unknown; restored from __doc__
        """ QEvent.setAccepted(bool) """
        pass

    def spontaneous(self): # real signature unknown; restored from __doc__
        """ QEvent.spontaneous() -> bool """
        return False

    def type(self): # real signature unknown; restored from __doc__
        """ QEvent.type() -> QEvent.Type """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccessibilityDescription = 130
    AccessibilityHelp = 119
    AccessibilityPrepare = 86
    ActionAdded = 114
    ActionChanged = 113
    ActionRemoved = 115
    ActivationChange = 99
    ApplicationActivate = 121
    ApplicationActivated = 121
    ApplicationDeactivate = 122
    ApplicationDeactivated = 122
    ApplicationFontChange = 36
    ApplicationLayoutDirectionChange = 37
    ApplicationPaletteChange = 38
    ApplicationWindowIconChange = 35
    ChildAdded = 68
    ChildPolished = 69
    ChildRemoved = 71
    Clipboard = 40
    Close = 19
    CloseSoftwareInputPanel = 200
    ContentsRectChange = 178
    ContextMenu = 82
    CursorChange = 183
    DeferredDelete = 52
    DragEnter = 60
    DragLeave = 62
    DragMove = 61
    Drop = 63
    DynamicPropertyChange = 170
    EnabledChange = 98
    Enter = 10
    EnterWhatsThisMode = 124
    FileOpen = 116
    FocusIn = 8
    FocusOut = 9
    FontChange = 97
    Gesture = 198
    GestureOverride = 202
    GrabKeyboard = 188
    GrabMouse = 186
    GraphicsSceneContextMenu = 159
    GraphicsSceneDragEnter = 164
    GraphicsSceneDragLeave = 166
    GraphicsSceneDragMove = 165
    GraphicsSceneDrop = 167
    GraphicsSceneHelp = 163
    GraphicsSceneHoverEnter = 160
    GraphicsSceneHoverLeave = 162
    GraphicsSceneHoverMove = 161
    GraphicsSceneMouseDoubleClick = 158
    GraphicsSceneMouseMove = 155
    GraphicsSceneMousePress = 156
    GraphicsSceneMouseRelease = 157
    GraphicsSceneMove = 182
    GraphicsSceneResize = 181
    GraphicsSceneWheel = 168
    Hide = 18
    HideToParent = 27
    HoverEnter = 127
    HoverLeave = 128
    HoverMove = 129
    IconDrag = 96
    IconTextChange = 101
    InputMethod = 83
    KeyboardLayoutChange = 169
    KeyPress = 6
    KeyRelease = 7
    LanguageChange = 89
    LayoutDirectionChange = 90
    LayoutRequest = 76
    Leave = 11
    LeaveWhatsThisMode = 125
    LocaleChange = 88
    MacSizeChange = 177
    MaxUser = 65535
    MenubarUpdated = 153
    MetaCall = 43
    ModifiedChange = 102
    MouseButtonDblClick = 4
    MouseButtonPress = 2
    MouseButtonRelease = 3
    MouseMove = 5
    MouseTrackingChange = 109
    Move = 13
    NonClientAreaMouseButtonDblClick = 176
    NonClientAreaMouseButtonPress = 174
    NonClientAreaMouseButtonRelease = 175
    NonClientAreaMouseMove = 173
    None = 0
    OkRequest = 94
    Paint = 12
    PaletteChange = 39
    ParentAboutToChange = 131
    ParentChange = 21
    PlatformPanel = 212
    Polish = 75
    PolishRequest = 74
    QueryWhatsThis = 123
    RequestSoftwareInputPanel = 199
    Resize = 14
    Shortcut = 117
    ShortcutOverride = 51
    Show = 17
    ShowToParent = 26
    SockAct = 50
    StateMachineSignal = 192
    StateMachineWrapped = 193
    StatusTip = 112
    StyleChange = 100
    TabletEnterProximity = 171
    TabletLeaveProximity = 172
    TabletMove = 87
    TabletPress = 92
    TabletRelease = 93
    Timer = 1
    ToolBarChange = 120
    ToolTip = 110
    ToolTipChange = 184
    TouchBegin = 194
    TouchEnd = 196
    TouchUpdate = 195
    UngrabKeyboard = 189
    UngrabMouse = 187
    UpdateLater = 78
    UpdateRequest = 77
    User = 1000
    WhatsThis = 111
    WhatsThisClicked = 118
    Wheel = 31
    WindowActivate = 24
    WindowBlocked = 103
    WindowDeactivate = 25
    WindowIconChange = 34
    WindowStateChange = 105
    WindowTitleChange = 33
    WindowUnblocked = 104
    WinEventAct = 132
    WinIdChange = 203
    ZOrderChange = 126


