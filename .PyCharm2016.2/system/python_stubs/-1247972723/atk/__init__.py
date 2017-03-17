# encoding: utf-8
# module atk
# from /usr/lib/python2.7/dist-packages/gtk-2.0/atk.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import __main__ as ____main__


# Variables with simple values

HYPERLINK_IS_INLINE = 1

KEY_EVENT_LAST_DEFINED = 2

KEY_EVENT_PRESS = 0
KEY_EVENT_RELEASE = 1

LAYER_BACKGROUND = 1
LAYER_CANVAS = 2
LAYER_INVALID = 0
LAYER_MDI = 4
LAYER_OVERLAY = 6
LAYER_POPUP = 5
LAYER_WIDGET = 3
LAYER_WINDOW = 7

RELATION_CONTROLLED_BY = 1

RELATION_CONTROLLER_FOR = 2

RELATION_DESCRIBED_BY = 14

RELATION_DESCRIPTION_FOR = 15

RELATION_EMBEDDED_BY = 11

RELATION_EMBEDS = 10

RELATION_FLOWS_FROM = 8
RELATION_FLOWS_TO = 7

RELATION_LABELLED_BY = 4

RELATION_LABEL_FOR = 3

RELATION_LAST_DEFINED = 17

RELATION_MEMBER_OF = 5

RELATION_NODE_CHILD_OF = 6

RELATION_NODE_PARENT_OF = 16

RELATION_NULL = 0

RELATION_PARENT_WINDOW_OF = 13

RELATION_POPUP_FOR = 12

RELATION_SUBWINDOW_OF = 9

ROLE_ACCEL_LABEL = 1

ROLE_ALERT = 2
ROLE_ANIMATION = 3
ROLE_APPLICATION = 73
ROLE_ARROW = 4
ROLE_ARTICLE = 107
ROLE_AUDIO = 104
ROLE_AUTOCOMPLETE = 74

ROLE_BLOCK_QUOTE = 103

ROLE_CALENDAR = 5
ROLE_CANVAS = 6
ROLE_CAPTION = 79
ROLE_CHART = 78

ROLE_CHECK_BOX = 7

ROLE_CHECK_MENU_ITEM = 8

ROLE_COLOR_CHOOSER = 9

ROLE_COLUMN_HEADER = 10

ROLE_COMBO_BOX = 11

ROLE_COMMENT = 95

ROLE_DATE_EDITOR = 12

ROLE_DEFINITION = 106

ROLE_DESCRIPTION_LIST = 114
ROLE_DESCRIPTION_TERM = 115
ROLE_DESCRIPTION_VALUE = 116

ROLE_DESKTOP_FRAME = 14
ROLE_DESKTOP_ICON = 13

ROLE_DIAL = 15
ROLE_DIALOG = 16

ROLE_DIRECTORY_PANE = 17

ROLE_DOCUMENT_EMAIL = 94
ROLE_DOCUMENT_FRAME = 80
ROLE_DOCUMENT_PRESENTATION = 91
ROLE_DOCUMENT_SPREADSHEET = 90
ROLE_DOCUMENT_TEXT = 92
ROLE_DOCUMENT_WEB = 93

ROLE_DRAWING_AREA = 18

ROLE_EDITBAR = 75
ROLE_EMBEDDED = 76
ROLE_ENTRY = 77

ROLE_FILE_CHOOSER = 19

ROLE_FILLER = 20

ROLE_FONT_CHOOSER = 21

ROLE_FOOTER = 70
ROLE_FORM = 85
ROLE_FRAME = 22

ROLE_GLASS_PANE = 23

ROLE_GROUPING = 97
ROLE_HEADER = 69
ROLE_HEADING = 81

ROLE_HTML_CONTAINER = 24

ROLE_ICON = 25
ROLE_IMAGE = 26

ROLE_IMAGE_MAP = 98

ROLE_INFO_BAR = 100

ROLE_INPUT_METHOD_WINDOW = 87

ROLE_INTERNAL_FRAME = 27

ROLE_INVALID = 0
ROLE_LABEL = 28
ROLE_LANDMARK = 108

ROLE_LAST_DEFINED = 122

ROLE_LAYERED_PANE = 29

ROLE_LEVEL_BAR = 101

ROLE_LINK = 86
ROLE_LIST = 30

ROLE_LIST_BOX = 96
ROLE_LIST_ITEM = 31

ROLE_LOG = 109
ROLE_MARQUEE = 110
ROLE_MATH = 111

ROLE_MATH_FRACTION = 118
ROLE_MATH_ROOT = 119

ROLE_MENU = 32

ROLE_MENU_BAR = 33
ROLE_MENU_ITEM = 34

ROLE_NOTIFICATION = 99

ROLE_OPTION_PANE = 35

ROLE_PAGE = 82

ROLE_PAGE_TAB = 36

ROLE_PAGE_TAB_LIST = 37

ROLE_PANEL = 38
ROLE_PARAGRAPH = 71

ROLE_PASSWORD_TEXT = 39

ROLE_POPUP_MENU = 40

ROLE_PROGRESS_BAR = 41

ROLE_PUSH_BUTTON = 42

ROLE_RADIO_BUTTON = 43

ROLE_RADIO_MENU_ITEM = 44

ROLE_RATING = 112

ROLE_REDUNDANT_OBJECT = 84

ROLE_ROOT_PANE = 45

ROLE_ROW_HEADER = 46

ROLE_RULER = 72

ROLE_SCROLL_BAR = 47
ROLE_SCROLL_PANE = 48

ROLE_SECTION = 83
ROLE_SEPARATOR = 49
ROLE_SLIDER = 50

ROLE_SPIN_BUTTON = 52

ROLE_SPLIT_PANE = 51

ROLE_STATIC = 117
ROLE_STATUSBAR = 53
ROLE_SUBSCRIPT = 120
ROLE_SUPERSCRIPT = 121
ROLE_TABLE = 54

ROLE_TABLE_CELL = 55

ROLE_TABLE_COLUMN_HEADER = 56

ROLE_TABLE_ROW = 88

ROLE_TABLE_ROW_HEADER = 57

ROLE_TEAR_OFF_MENU_ITEM = 58

ROLE_TERMINAL = 59
ROLE_TEXT = 60
ROLE_TIMER = 113

ROLE_TITLE_BAR = 102

ROLE_TOGGLE_BUTTON = 61

ROLE_TOOL_BAR = 62
ROLE_TOOL_TIP = 63

ROLE_TREE = 64

ROLE_TREE_ITEM = 89
ROLE_TREE_TABLE = 65

ROLE_UNKNOWN = 66
ROLE_VIDEO = 105
ROLE_VIEWPORT = 67
ROLE_WINDOW = 68

STATE_ACTIVE = 1
STATE_ANIMATED = 37
STATE_ARMED = 2
STATE_BUSY = 3
STATE_CHECKABLE = 39
STATE_CHECKED = 4
STATE_DEFAULT = 36
STATE_DEFUNCT = 5
STATE_EDITABLE = 6
STATE_ENABLED = 7
STATE_EXPANDABLE = 8
STATE_EXPANDED = 9
STATE_FOCUSABLE = 10
STATE_FOCUSED = 11

STATE_HAS_POPUP = 40
STATE_HAS_TOOLTIP = 41

STATE_HORIZONTAL = 12
STATE_ICONIFIED = 13
STATE_INDETERMINATE = 30
STATE_INVALID = 0

STATE_INVALID_ENTRY = 33

STATE_LAST_DEFINED = 43

STATE_MANAGES_DESCENDANTS = 29

STATE_MODAL = 14
STATE_MULTISELECTABLE = 16

STATE_MULTI_LINE = 15

STATE_OPAQUE = 17
STATE_PRESSED = 18

STATE_READ_ONLY = 42

STATE_REQUIRED = 32
STATE_RESIZABLE = 19
STATE_SELECTABLE = 20

STATE_SELECTABLE_TEXT = 35

STATE_SELECTED = 21
STATE_SENSITIVE = 22
STATE_SHOWING = 23

STATE_SINGLE_LINE = 24

STATE_STALE = 25

STATE_SUPPORTS_AUTOCOMPLETION = 34

STATE_TRANSIENT = 26
STATE_TRUNCATED = 31
STATE_VERTICAL = 27
STATE_VISIBLE = 28
STATE_VISITED = 38

TEXT_ATTR_BG_COLOR = 18

TEXT_ATTR_BG_FULL_HEIGHT = 9

TEXT_ATTR_BG_STIPPLE = 20

TEXT_ATTR_DIRECTION = 23
TEXT_ATTR_EDITABLE = 5

TEXT_ATTR_FAMILY_NAME = 17

TEXT_ATTR_FG_COLOR = 19
TEXT_ATTR_FG_STIPPLE = 21

TEXT_ATTR_INDENT = 3
TEXT_ATTR_INVALID = 0
TEXT_ATTR_INVISIBLE = 4
TEXT_ATTR_JUSTIFICATION = 24
TEXT_ATTR_LANGUAGE = 16

TEXT_ATTR_LAST_DEFINED = 28

TEXT_ATTR_LEFT_MARGIN = 1

TEXT_ATTR_PIXELS_ABOVE_LINES = 6

TEXT_ATTR_PIXELS_BELOW_LINES = 7

TEXT_ATTR_PIXELS_INSIDE_WRAP = 8

TEXT_ATTR_RIGHT_MARGIN = 2

TEXT_ATTR_RISE = 10
TEXT_ATTR_SCALE = 14
TEXT_ATTR_SIZE = 13
TEXT_ATTR_STRETCH = 25
TEXT_ATTR_STRIKETHROUGH = 12
TEXT_ATTR_STYLE = 27
TEXT_ATTR_UNDERLINE = 11
TEXT_ATTR_VARIANT = 26
TEXT_ATTR_WEIGHT = 15

TEXT_ATTR_WRAP_MODE = 22

TEXT_BOUNDARY_CHAR = 0

TEXT_BOUNDARY_LINE_END = 6
TEXT_BOUNDARY_LINE_START = 5

TEXT_BOUNDARY_SENTENCE_END = 4
TEXT_BOUNDARY_SENTENCE_START = 3

TEXT_BOUNDARY_WORD_END = 2
TEXT_BOUNDARY_WORD_START = 1

TEXT_CLIP_BOTH = 3
TEXT_CLIP_MAX = 2
TEXT_CLIP_MIN = 1
TEXT_CLIP_NONE = 0

XY_SCREEN = 0
XY_WINDOW = 1

# functions

def focus_tracker_notify(*args, **kwargs): # real signature unknown
    pass

def get_default_registry(*args, **kwargs): # real signature unknown
    pass

def get_focus_object(*args, **kwargs): # real signature unknown
    pass

def get_root(*args, **kwargs): # real signature unknown
    pass

def get_toolkit_name(*args, **kwargs): # real signature unknown
    pass

def get_toolkit_version(*args, **kwargs): # real signature unknown
    pass

def gobject_accessible_for_object(*args, **kwargs): # real signature unknown
    pass

def relation_type_for_name(*args, **kwargs): # real signature unknown
    pass

def relation_type_get_name(*args, **kwargs): # real signature unknown
    pass

def relation_type_register(*args, **kwargs): # real signature unknown
    pass

def remove_focus_tracker(*args, **kwargs): # real signature unknown
    pass

def remove_global_event_listener(*args, **kwargs): # real signature unknown
    pass

def remove_key_event_listener(*args, **kwargs): # real signature unknown
    pass

def role_for_name(*args, **kwargs): # real signature unknown
    pass

def role_get_localized_name(*args, **kwargs): # real signature unknown
    pass

def role_get_name(*args, **kwargs): # real signature unknown
    pass

def role_register(*args, **kwargs): # real signature unknown
    pass

def state_type_for_name(*args, **kwargs): # real signature unknown
    pass

def state_type_get_name(*args, **kwargs): # real signature unknown
    pass

def state_type_register(*args, **kwargs): # real signature unknown
    pass

def text_attribute_for_name(*args, **kwargs): # real signature unknown
    pass

def text_attribute_get_name(*args, **kwargs): # real signature unknown
    pass

def text_attribute_get_value(*args, **kwargs): # real signature unknown
    pass

def text_attribute_register(*args, **kwargs): # real signature unknown
    pass

# classes

from Action import Action
from Component import Component
from CoordType import CoordType
from Document import Document
from EditableText import EditableText
from Object import Object
from GObjectAccessible import GObjectAccessible
from Hyperlink import Hyperlink
from HyperlinkImpl import HyperlinkImpl
from HyperlinkStateFlags import HyperlinkStateFlags
from Hypertext import Hypertext
from Image import Image
from ImplementorIface import ImplementorIface
from KeyEventType import KeyEventType
from Layer import Layer
from Selection import Selection
from Table import Table
from TableCell import TableCell
from Text import Text
from Value import Value
from Window import Window
from NoOpObject import NoOpObject
from ObjectFactory import ObjectFactory
from NoOpObjectFactory import NoOpObjectFactory
from Rectangle import Rectangle
from Registry import Registry
from Relation import Relation
from RelationSet import RelationSet
from RelationType import RelationType
from Role import Role
from StateSet import StateSet
from StateType import StateType
from StreamableContent import StreamableContent
from TextAttribute import TextAttribute
from TextBoundary import TextBoundary
from TextClipType import TextClipType
from Util import Util
