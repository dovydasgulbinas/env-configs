# encoding: utf-8
# module gtk._gtk
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gtk/_gtk.so
# by generator 1.143
# no doc

# imports
import atk as __atk
import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject


# Variables with simple values

ACCEL_LOCKED = 2
ACCEL_MASK = 7
ACCEL_VISIBLE = 1

ANCHOR_CENTER = 0
ANCHOR_E = 8
ANCHOR_EAST = 8
ANCHOR_N = 1
ANCHOR_NE = 3
ANCHOR_NORTH = 1

ANCHOR_NORTH_EAST = 3
ANCHOR_NORTH_WEST = 2

ANCHOR_NW = 2
ANCHOR_S = 4
ANCHOR_SE = 6
ANCHOR_SOUTH = 4

ANCHOR_SOUTH_EAST = 6
ANCHOR_SOUTH_WEST = 5

ANCHOR_SW = 5
ANCHOR_W = 7
ANCHOR_WEST = 7

APP_PAINTABLE = 524288

ARG_CHILD_ARG = 16

ARG_CONSTRUCT = 4

ARG_CONSTRUCT_ONLY = 8

ARG_READABLE = 1
ARG_WRITABLE = 2

ARROW_DOWN = 1
ARROW_LEFT = 2
ARROW_NONE = 4
ARROW_RIGHT = 3
ARROW_UP = 0

ASSISTANT_PAGE_CONFIRM = 2
ASSISTANT_PAGE_CONTENT = 0
ASSISTANT_PAGE_INTRO = 1
ASSISTANT_PAGE_PROGRESS = 4
ASSISTANT_PAGE_SUMMARY = 3

BUILDER_ERROR_DUPLICATE_ID = 8

BUILDER_ERROR_INVALID_ATTRIBUTE = 3
BUILDER_ERROR_INVALID_TAG = 4

BUILDER_ERROR_INVALID_TYPE_FUNCTION = 0

BUILDER_ERROR_INVALID_VALUE = 6

BUILDER_ERROR_MISSING_ATTRIBUTE = 2

BUILDER_ERROR_MISSING_PROPERTY_VALUE = 5

BUILDER_ERROR_UNHANDLED_TAG = 1

BUILDER_ERROR_VERSION_MISMATCH = 7

BUTTONBOX_CENTER = 5

BUTTONBOX_DEFAULT_STYLE = 0

BUTTONBOX_EDGE = 2
BUTTONBOX_END = 4
BUTTONBOX_SPREAD = 1
BUTTONBOX_START = 3

BUTTONS_CANCEL = 3
BUTTONS_CLOSE = 2
BUTTONS_NONE = 0
BUTTONS_OK = 1

BUTTONS_OK_CANCEL = 5

BUTTONS_YES_NO = 4

BUTTON_DRAGS = 2
BUTTON_EXPANDS = 4
BUTTON_IGNORED = 0
BUTTON_SELECTS = 1

CALENDAR_NO_MONTH_CHANGE = 4

CALENDAR_SHOW_DAY_NAMES = 2

CALENDAR_SHOW_DETAILS = 32
CALENDAR_SHOW_HEADING = 1

CALENDAR_SHOW_WEEK_NUMBERS = 8

CALENDAR_WEEK_START_MONDAY = 16

CAN_DEFAULT = 8192
CAN_FOCUS = 2048

CELL_EMPTY = 0
CELL_PIXMAP = 2
CELL_PIXTEXT = 3

CELL_RENDERER_ACCEL_MODE_GTK = 0
CELL_RENDERER_ACCEL_MODE_OTHER = 1

CELL_RENDERER_FOCUSED = 16
CELL_RENDERER_INSENSITIVE = 4

CELL_RENDERER_MODE_ACTIVATABLE = 1
CELL_RENDERER_MODE_EDITABLE = 2
CELL_RENDERER_MODE_INERT = 0

CELL_RENDERER_PRELIT = 2
CELL_RENDERER_SELECTED = 1
CELL_RENDERER_SORTED = 8

CELL_TEXT = 1
CELL_WIDGET = 4

CENTIMETERS = 2

CLIST_DRAG_AFTER = 3
CLIST_DRAG_BEFORE = 1
CLIST_DRAG_INTO = 2
CLIST_DRAG_NONE = 0

COMPOSITE_CHILD = 131072

CORNER_BOTTOM_LEFT = 1
CORNER_BOTTOM_RIGHT = 3

CORNER_TOP_LEFT = 0
CORNER_TOP_RIGHT = 2

CTREE_EXPANDER_CIRCULAR = 3
CTREE_EXPANDER_NONE = 0
CTREE_EXPANDER_SQUARE = 1
CTREE_EXPANDER_TRIANGLE = 2

CTREE_EXPANSION_COLLAPSE = 2

CTREE_EXPANSION_COLLAPSE_RECURSIVE = 3

CTREE_EXPANSION_EXPAND = 0

CTREE_EXPANSION_EXPAND_RECURSIVE = 1

CTREE_EXPANSION_TOGGLE = 4

CTREE_EXPANSION_TOGGLE_RECURSIVE = 5

CTREE_LINES_DOTTED = 2
CTREE_LINES_NONE = 0
CTREE_LINES_SOLID = 1
CTREE_LINES_TABBED = 3

CTREE_POS_AFTER = 2

CTREE_POS_AS_CHILD = 1

CTREE_POS_BEFORE = 0

CURVE_TYPE_FREE = 2
CURVE_TYPE_LINEAR = 0
CURVE_TYPE_SPLINE = 1

DEBUG_BUILDER = 2048
DEBUG_GEOMETRY = 256
DEBUG_ICONTHEME = 512
DEBUG_KEYBINDINGS = 32
DEBUG_MISC = 1
DEBUG_MODULES = 128
DEBUG_MULTIHEAD = 64
DEBUG_PLUGSOCKET = 2
DEBUG_PRINTING = 1024
DEBUG_TEXT = 4
DEBUG_TREE = 8
DEBUG_UPDATES = 16

DELETE_CHARS = 0

DELETE_DISPLAY_LINES = 3

DELETE_DISPLAY_LINE_ENDS = 4

DELETE_PARAGRAPHS = 6

DELETE_PARAGRAPH_ENDS = 5

DELETE_WHITESPACE = 7
DELETE_WORDS = 2

DELETE_WORD_ENDS = 1

DEST_DEFAULT_ALL = 7
DEST_DEFAULT_DROP = 4
DEST_DEFAULT_HIGHLIGHT = 2
DEST_DEFAULT_MOTION = 1

DIALOG_DESTROY_WITH_PARENT = 2

DIALOG_MODAL = 1

DIALOG_NO_SEPARATOR = 4

DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1

DIR_DOWN = 3
DIR_LEFT = 4
DIR_RIGHT = 5

DIR_TAB_BACKWARD = 1
DIR_TAB_FORWARD = 0

DIR_UP = 2

DOUBLE_BUFFERED = 2097152

ENTRY_ICON_PRIMARY = 0
ENTRY_ICON_SECONDARY = 1

EXPAND = 1

EXPANDER_COLLAPSED = 0
EXPANDER_EXPANDED = 3

EXPANDER_SEMI_COLLAPSED = 1
EXPANDER_SEMI_EXPANDED = 2

FILE_CHOOSER_ACTION_CREATE_FOLDER = 3

FILE_CHOOSER_ACTION_OPEN = 0
FILE_CHOOSER_ACTION_SAVE = 1

FILE_CHOOSER_ACTION_SELECT_FOLDER = 2

FILE_CHOOSER_CONFIRMATION_ACCEPT_FILENAME = 1

FILE_CHOOSER_CONFIRMATION_CONFIRM = 0

FILE_CHOOSER_CONFIRMATION_SELECT_AGAIN = 2

FILE_CHOOSER_ERROR_ALREADY_EXISTS = 2

FILE_CHOOSER_ERROR_BAD_FILENAME = 1

FILE_CHOOSER_ERROR_INCOMPLETE_HOSTNAME = 3

FILE_CHOOSER_ERROR_NONEXISTENT = 0

FILE_FILTER_DISPLAY_NAME = 4

FILE_FILTER_FILENAME = 1

FILE_FILTER_MIME_TYPE = 8

FILE_FILTER_URI = 2

FILL = 4

FLOATING = 2

HAS_DEFAULT = 16384
HAS_FOCUS = 4096
HAS_GRAB = 32768

ICON_LOOKUP_FORCE_SIZE = 16
ICON_LOOKUP_FORCE_SVG = 2

ICON_LOOKUP_GENERIC_FALLBACK = 8

ICON_LOOKUP_NO_SVG = 1

ICON_LOOKUP_USE_BUILTIN = 4

ICON_SIZE_BUTTON = 4
ICON_SIZE_DIALOG = 6
ICON_SIZE_DND = 5
ICON_SIZE_INVALID = 0

ICON_SIZE_LARGE_TOOLBAR = 3

ICON_SIZE_MENU = 1

ICON_SIZE_SMALL_TOOLBAR = 2

ICON_THEME_FAILED = 1

ICON_THEME_NOT_FOUND = 0

ICON_VIEW_DROP_ABOVE = 4
ICON_VIEW_DROP_BELOW = 5
ICON_VIEW_DROP_INTO = 1
ICON_VIEW_DROP_LEFT = 2
ICON_VIEW_DROP_RIGHT = 3

ICON_VIEW_NO_DROP = 0

IMAGE_ANIMATION = 6
IMAGE_EMPTY = 0
IMAGE_GICON = 8

IMAGE_ICON_NAME = 7
IMAGE_ICON_SET = 5

IMAGE_IMAGE = 2
IMAGE_PIXBUF = 3
IMAGE_PIXMAP = 1
IMAGE_STOCK = 4

IM_PREEDIT_CALLBACK = 1
IM_PREEDIT_NONE = 2
IM_PREEDIT_NOTHING = 0

IM_STATUS_CALLBACK = 1
IM_STATUS_NONE = 2
IM_STATUS_NOTHING = 0

INCHES = 1
IN_DESTRUCTION = 1

JUSTIFY_CENTER = 2
JUSTIFY_FILL = 3
JUSTIFY_LEFT = 0
JUSTIFY_RIGHT = 1

LEFT_RIGHT = 1

MAPPED = 128

MATCH_ALL = 0

MATCH_ALL_TAIL = 1

MATCH_EXACT = 4
MATCH_HEAD = 2
MATCH_LAST = 5
MATCH_TAIL = 3

MENU_DIR_CHILD = 1
MENU_DIR_NEXT = 2
MENU_DIR_PARENT = 0
MENU_DIR_PREV = 3

MESSAGE_ERROR = 3
MESSAGE_INFO = 0
MESSAGE_OTHER = 4
MESSAGE_QUESTION = 2
MESSAGE_WARNING = 1

MOVEMENT_BUFFER_ENDS = 8

MOVEMENT_DISPLAY_LINES = 3

MOVEMENT_DISPLAY_LINE_ENDS = 4

MOVEMENT_HORIZONTAL_PAGES = 9

MOVEMENT_LOGICAL_POSITIONS = 0

MOVEMENT_PAGES = 7
MOVEMENT_PARAGRAPHS = 5

MOVEMENT_PARAGRAPH_ENDS = 6

MOVEMENT_VISUAL_POSITIONS = 1

MOVEMENT_WORDS = 2

NOTEBOOK_TAB_FIRST = 0
NOTEBOOK_TAB_LAST = 1

NO_REPARENT = 262144

NO_SHOW_ALL = 4194304

NO_WINDOW = 32

NUMBER_UP_LAYOUT_BOTTOM_TO_TOP_LEFT_TO_RIGHT = 6

NUMBER_UP_LAYOUT_BOTTOM_TO_TOP_RIGHT_TO_LEFT = 7

NUMBER_UP_LAYOUT_LEFT_TO_RIGHT_BOTTOM_TO_TOP = 1

NUMBER_UP_LAYOUT_LEFT_TO_RIGHT_TOP_TO_BOTTOM = 0

NUMBER_UP_LAYOUT_RIGHT_TO_LEFT_BOTTOM_TO_TOP = 3

NUMBER_UP_LAYOUT_RIGHT_TO_LEFT_TOP_TO_BOTTOM = 2

NUMBER_UP_LAYOUT_TOP_TO_BOTTOM_LEFT_TO_RIGHT = 4

NUMBER_UP_LAYOUT_TOP_TO_BOTTOM_RIGHT_TO_LEFT = 5

ORIENTATION_HORIZONTAL = 0
ORIENTATION_VERTICAL = 1

PACK_DIRECTION_BTT = 3
PACK_DIRECTION_LTR = 0
PACK_DIRECTION_RTL = 1
PACK_DIRECTION_TTB = 2

PACK_END = 1
PACK_START = 0

PAGE_ORIENTATION_LANDSCAPE = 1
PAGE_ORIENTATION_PORTRAIT = 0

PAGE_ORIENTATION_REVERSE_LANDSCAPE = 3
PAGE_ORIENTATION_REVERSE_PORTRAIT = 2

PAGE_SET_ALL = 0
PAGE_SET_EVEN = 1
PAGE_SET_ODD = 2

PAPER_NAME_A3 = 'iso_a3'
PAPER_NAME_A4 = 'iso_a4'
PAPER_NAME_A5 = 'iso_a5'
PAPER_NAME_B5 = 'iso_b5'
PAPER_NAME_EXECUTIVE = 'na_executive'
PAPER_NAME_LEGAL = 'na_legal'
PAPER_NAME_LETTER = 'na_letter'

PARENT_SENSITIVE = 1024

PATH_CLASS = 2

PATH_PRIO_APPLICATION = 8
PATH_PRIO_GTK = 4
PATH_PRIO_HIGHEST = 15
PATH_PRIO_LOWEST = 0
PATH_PRIO_RC = 12
PATH_PRIO_THEME = 10

PATH_WIDGET = 0

PATH_WIDGET_CLASS = 1

PIXELS = 0

POLICY_ALWAYS = 0
POLICY_AUTOMATIC = 1
POLICY_NEVER = 2

POS_BOTTOM = 3
POS_LEFT = 0
POS_RIGHT = 1
POS_TOP = 2

PREVIEW_COLOR = 0
PREVIEW_GRAYSCALE = 1

PRINT_DUPLEX_HORIZONTAL = 1
PRINT_DUPLEX_SIMPLEX = 0
PRINT_DUPLEX_VERTICAL = 2

PRINT_ERROR_GENERAL = 0

PRINT_ERROR_INTERNAL_ERROR = 1

PRINT_ERROR_INVALID_FILE = 3

PRINT_ERROR_NOMEM = 2

PRINT_OPERATION_ACTION_EXPORT = 3
PRINT_OPERATION_ACTION_PREVIEW = 2
PRINT_OPERATION_ACTION_PRINT = 1

PRINT_OPERATION_ACTION_PRINT_DIALOG = 0

PRINT_OPERATION_RESULT_APPLY = 1
PRINT_OPERATION_RESULT_CANCEL = 2
PRINT_OPERATION_RESULT_ERROR = 0

PRINT_OPERATION_RESULT_IN_PROGRESS = 3

PRINT_PAGES_ALL = 0
PRINT_PAGES_CURRENT = 1
PRINT_PAGES_RANGES = 2
PRINT_PAGES_SELECTION = 3

PRINT_QUALITY_DRAFT = 3
PRINT_QUALITY_HIGH = 2
PRINT_QUALITY_LOW = 0
PRINT_QUALITY_NORMAL = 1

PRINT_STATUS_FINISHED = 7

PRINT_STATUS_FINISHED_ABORTED = 8

PRINT_STATUS_GENERATING_DATA = 2

PRINT_STATUS_INITIAL = 0
PRINT_STATUS_PENDING = 4

PRINT_STATUS_PENDING_ISSUE = 5

PRINT_STATUS_PREPARING = 1
PRINT_STATUS_PRINTING = 6

PRINT_STATUS_SENDING_DATA = 3

PRIVATE_GTK_ALLOC_NEEDED = 4096

PRIVATE_GTK_ANCHORED = 512

PRIVATE_GTK_CHILD_VISIBLE = 1024

PRIVATE_GTK_DIRECTION_LTR = 256
PRIVATE_GTK_DIRECTION_SET = 128

PRIVATE_GTK_HAS_POINTER = 8

PRIVATE_GTK_HAS_SHAPE_MASK = 32

PRIVATE_GTK_IN_REPARENT = 64

PRIVATE_GTK_REDRAW_ON_ALLOC = 2048

PRIVATE_GTK_REQUEST_NEEDED = 8192

PRIVATE_GTK_RESIZE_PENDING = 4

PRIVATE_GTK_SHADOWED = 16

PRIVATE_GTK_USER_STYLE = 1

PROGRESS_BOTTOM_TO_TOP = 2

PROGRESS_CONTINUOUS = 0
PROGRESS_DISCRETE = 1

PROGRESS_LEFT_TO_RIGHT = 0

PROGRESS_RIGHT_TO_LEFT = 1

PROGRESS_TOP_TO_BOTTOM = 3

RC_BASE = 8
RC_BG = 2
RC_FG = 1
RC_STYLE = 65536
RC_TEXT = 4

RC_TOKEN_ACTIVE = 273
RC_TOKEN_APPLICATION = 296
RC_TOKEN_BASE = 280
RC_TOKEN_BG = 278

RC_TOKEN_BG_PIXMAP = 286

RC_TOKEN_BIND = 290
RC_TOKEN_BINDING = 289
RC_TOKEN_CLASS = 293
RC_TOKEN_COLOR = 307
RC_TOKEN_ENGINE = 300
RC_TOKEN_FG = 277
RC_TOKEN_FONT = 283
RC_TOKEN_FONTSET = 284

RC_TOKEN_FONT_NAME = 285

RC_TOKEN_GTK = 295
RC_TOKEN_HIGHEST = 299

RC_TOKEN_IM_MODULE_FILE = 303
RC_TOKEN_IM_MODULE_PATH = 302

RC_TOKEN_INCLUDE = 271
RC_TOKEN_INSENSITIVE = 276
RC_TOKEN_INVALID = 270
RC_TOKEN_LAST = 309
RC_TOKEN_LOWEST = 294
RC_TOKEN_LTR = 305

RC_TOKEN_MODULE_PATH = 301

RC_TOKEN_NORMAL = 272

RC_TOKEN_PIXMAP_PATH = 287

RC_TOKEN_PRELIGHT = 274
RC_TOKEN_RC = 298
RC_TOKEN_RTL = 306
RC_TOKEN_SELECTED = 275
RC_TOKEN_STOCK = 304
RC_TOKEN_STYLE = 288
RC_TOKEN_TEXT = 279
RC_TOKEN_THEME = 297
RC_TOKEN_UNBIND = 308
RC_TOKEN_WIDGET = 291

RC_TOKEN_WIDGET_CLASS = 292

RC_TOKEN_XTHICKNESS = 281
RC_TOKEN_YTHICKNESS = 282

REALIZED = 64

RECEIVES_DEFAULT = 1048576

RECENT_CHOOSER_ERROR_INVALID_URI = 1

RECENT_CHOOSER_ERROR_NOT_FOUND = 0

RECENT_FILTER_AGE = 32
RECENT_FILTER_APPLICATION = 8

RECENT_FILTER_DISPLAY_NAME = 2

RECENT_FILTER_GROUP = 16

RECENT_FILTER_MIME_TYPE = 4

RECENT_FILTER_URI = 1

RECENT_MANAGER_ERROR_INVALID_ENCODING = 2
RECENT_MANAGER_ERROR_INVALID_URI = 1

RECENT_MANAGER_ERROR_NOT_FOUND = 0
RECENT_MANAGER_ERROR_NOT_REGISTERED = 3

RECENT_MANAGER_ERROR_READ = 4
RECENT_MANAGER_ERROR_UNKNOWN = 6
RECENT_MANAGER_ERROR_WRITE = 5

RECENT_SORT_CUSTOM = 3
RECENT_SORT_LRU = 2
RECENT_SORT_MRU = 1
RECENT_SORT_NONE = 0

RELIEF_HALF = 1
RELIEF_NONE = 2
RELIEF_NORMAL = 0

RESERVED_1 = 4
RESERVED_2 = 8

RESIZE_IMMEDIATE = 2
RESIZE_PARENT = 0
RESIZE_QUEUE = 1

RESPONSE_ACCEPT = -3
RESPONSE_APPLY = -10
RESPONSE_CANCEL = -6
RESPONSE_CLOSE = -7

RESPONSE_DELETE_EVENT = -4

RESPONSE_HELP = -11
RESPONSE_NO = -9
RESPONSE_NONE = -1
RESPONSE_OK = -5
RESPONSE_REJECT = -2
RESPONSE_YES = -8

SCROLL_END = 15
SCROLL_ENDS = 2

SCROLL_HORIZONTAL_ENDS = 5
SCROLL_HORIZONTAL_PAGES = 4
SCROLL_HORIZONTAL_STEPS = 3

SCROLL_JUMP = 1
SCROLL_NONE = 0
SCROLL_PAGES = 1

SCROLL_PAGE_BACKWARD = 4
SCROLL_PAGE_DOWN = 9
SCROLL_PAGE_FORWARD = 5
SCROLL_PAGE_LEFT = 12
SCROLL_PAGE_RIGHT = 13
SCROLL_PAGE_UP = 8

SCROLL_START = 14
SCROLL_STEPS = 0

SCROLL_STEP_BACKWARD = 2
SCROLL_STEP_DOWN = 7
SCROLL_STEP_FORWARD = 3
SCROLL_STEP_LEFT = 10
SCROLL_STEP_RIGHT = 11
SCROLL_STEP_UP = 6

SELECTION_BROWSE = 2
SELECTION_EXTENDED = 3
SELECTION_MULTIPLE = 3
SELECTION_NONE = 0
SELECTION_SINGLE = 1

SENSITIVE = 512

SENSITIVITY_AUTO = 0
SENSITIVITY_OFF = 2
SENSITIVITY_ON = 1

SHADOW_ETCHED_IN = 3
SHADOW_ETCHED_OUT = 4

SHADOW_IN = 1
SHADOW_NONE = 0
SHADOW_OUT = 2

SHRINK = 2

SIDE_BOTTOM = 1
SIDE_LEFT = 2
SIDE_RIGHT = 3
SIDE_TOP = 0

SIZE_GROUP_BOTH = 3
SIZE_GROUP_HORIZONTAL = 1
SIZE_GROUP_NONE = 0
SIZE_GROUP_VERTICAL = 2

SORT_ASCENDING = 0
SORT_DESCENDING = 1

SPIN_END = 5
SPIN_HOME = 4

SPIN_PAGE_BACKWARD = 3
SPIN_PAGE_FORWARD = 2

SPIN_STEP_BACKWARD = 1
SPIN_STEP_FORWARD = 0

SPIN_USER_DEFINED = 6

STATE_ACTIVE = 1
STATE_INSENSITIVE = 4
STATE_NORMAL = 0
STATE_PRELIGHT = 2
STATE_SELECTED = 3

STOCK_ABOUT = 'gtk-about'
STOCK_ADD = 'gtk-add'
STOCK_APPLY = 'gtk-apply'
STOCK_BOLD = 'gtk-bold'
STOCK_CANCEL = 'gtk-cancel'

STOCK_CAPS_LOCK_WARNING = 'gtk-caps-lock-warning'

STOCK_CDROM = 'gtk-cdrom'
STOCK_CLEAR = 'gtk-clear'
STOCK_CLOSE = 'gtk-close'

STOCK_COLOR_PICKER = 'gtk-color-picker'

STOCK_CONNECT = 'gtk-connect'
STOCK_CONVERT = 'gtk-convert'
STOCK_COPY = 'gtk-copy'
STOCK_CUT = 'gtk-cut'
STOCK_DELETE = 'gtk-delete'

STOCK_DIALOG_AUTHENTICATION = 'gtk-dialog-authentication'
STOCK_DIALOG_ERROR = 'gtk-dialog-error'
STOCK_DIALOG_INFO = 'gtk-dialog-info'
STOCK_DIALOG_QUESTION = 'gtk-dialog-question'
STOCK_DIALOG_WARNING = 'gtk-dialog-warning'

STOCK_DIRECTORY = 'gtk-directory'
STOCK_DISCARD = 'gtk-discard'
STOCK_DISCONNECT = 'gtk-disconnect'
STOCK_DND = 'gtk-dnd'

STOCK_DND_MULTIPLE = 'gtk-dnd-multiple'

STOCK_EDIT = 'gtk-edit'
STOCK_EXECUTE = 'gtk-execute'
STOCK_FILE = 'gtk-file'
STOCK_FIND = 'gtk-find'

STOCK_FIND_AND_REPLACE = 'gtk-find-and-replace'

STOCK_FLOPPY = 'gtk-floppy'
STOCK_FULLSCREEN = 'gtk-fullscreen'

STOCK_GOTO_BOTTOM = 'gtk-goto-bottom'
STOCK_GOTO_FIRST = 'gtk-goto-first'
STOCK_GOTO_LAST = 'gtk-goto-last'
STOCK_GOTO_TOP = 'gtk-goto-top'

STOCK_GO_BACK = 'gtk-go-back'
STOCK_GO_DOWN = 'gtk-go-down'
STOCK_GO_FORWARD = 'gtk-go-forward'
STOCK_GO_UP = 'gtk-go-up'

STOCK_HARDDISK = 'gtk-harddisk'
STOCK_HELP = 'gtk-help'
STOCK_HOME = 'gtk-home'
STOCK_INDENT = 'gtk-indent'
STOCK_INDEX = 'gtk-index'
STOCK_INFO = 'gtk-info'
STOCK_ITALIC = 'gtk-italic'

STOCK_JUMP_TO = 'gtk-jump-to'

STOCK_JUSTIFY_CENTER = 'gtk-justify-center'
STOCK_JUSTIFY_FILL = 'gtk-justify-fill'
STOCK_JUSTIFY_LEFT = 'gtk-justify-left'
STOCK_JUSTIFY_RIGHT = 'gtk-justify-right'

STOCK_LEAVE_FULLSCREEN = 'gtk-leave-fullscreen'

STOCK_MEDIA_FORWARD = 'gtk-media-forward'
STOCK_MEDIA_NEXT = 'gtk-media-next'
STOCK_MEDIA_PAUSE = 'gtk-media-pause'
STOCK_MEDIA_PLAY = 'gtk-media-play'
STOCK_MEDIA_PREVIOUS = 'gtk-media-previous'
STOCK_MEDIA_RECORD = 'gtk-media-record'
STOCK_MEDIA_REWIND = 'gtk-media-rewind'
STOCK_MEDIA_STOP = 'gtk-media-stop'

STOCK_MISSING_IMAGE = 'gtk-missing-image'

STOCK_NETWORK = 'gtk-network'
STOCK_NEW = 'gtk-new'
STOCK_NO = 'gtk-no'
STOCK_OK = 'gtk-ok'
STOCK_OPEN = 'gtk-open'

STOCK_ORIENTATION_LANDSCAPE = 'gtk-orientation-landscape'
STOCK_ORIENTATION_PORTRAIT = 'gtk-orientation-portrait'

STOCK_ORIENTATION_REVERSE_LANDSCAPE = 'gtk-orientation-reverse-landscape'
STOCK_ORIENTATION_REVERSE_PORTRAIT = 'gtk-orientation-reverse-portrait'

STOCK_PAGE_SETUP = 'gtk-page-setup'

STOCK_PASTE = 'gtk-paste'
STOCK_PREFERENCES = 'gtk-preferences'
STOCK_PRINT = 'gtk-print'

STOCK_PRINT_ERROR = 'gtk-print-error'
STOCK_PRINT_PAUSED = 'gtk-print-paused'
STOCK_PRINT_PREVIEW = 'gtk-print-preview'
STOCK_PRINT_REPORT = 'gtk-print-report'
STOCK_PRINT_WARNING = 'gtk-print-warning'

STOCK_PROPERTIES = 'gtk-properties'
STOCK_QUIT = 'gtk-quit'
STOCK_REDO = 'gtk-redo'
STOCK_REFRESH = 'gtk-refresh'
STOCK_REMOVE = 'gtk-remove'

STOCK_REVERT_TO_SAVED = 'gtk-revert-to-saved'

STOCK_SAVE = 'gtk-save'

STOCK_SAVE_AS = 'gtk-save-as'

STOCK_SELECT_ALL = 'gtk-select-all'
STOCK_SELECT_COLOR = 'gtk-select-color'
STOCK_SELECT_FONT = 'gtk-select-font'

STOCK_SORT_ASCENDING = 'gtk-sort-ascending'
STOCK_SORT_DESCENDING = 'gtk-sort-descending'

STOCK_SPELL_CHECK = 'gtk-spell-check'

STOCK_STOP = 'gtk-stop'
STOCK_STRIKETHROUGH = 'gtk-strikethrough'
STOCK_UNDELETE = 'gtk-undelete'
STOCK_UNDERLINE = 'gtk-underline'
STOCK_UNDO = 'gtk-undo'
STOCK_UNINDENT = 'gtk-unindent'
STOCK_YES = 'gtk-yes'

STOCK_ZOOM_100 = 'gtk-zoom-100'
STOCK_ZOOM_FIT = 'gtk-zoom-fit'
STOCK_ZOOM_IN = 'gtk-zoom-in'
STOCK_ZOOM_OUT = 'gtk-zoom-out'

TARGET_OTHER_APP = 4
TARGET_OTHER_WIDGET = 8

TARGET_SAME_APP = 1
TARGET_SAME_WIDGET = 2

TEXT_BUFFER_TARGET_INFO_BUFFER_CONTENTS = -1

TEXT_BUFFER_TARGET_INFO_RICH_TEXT = -2

TEXT_BUFFER_TARGET_INFO_TEXT = -3

TEXT_DIR_LTR = 1
TEXT_DIR_NONE = 0
TEXT_DIR_RTL = 2

TEXT_SEARCH_TEXT_ONLY = 2

TEXT_SEARCH_VISIBLE_ONLY = 1

TEXT_WINDOW_BOTTOM = 6
TEXT_WINDOW_LEFT = 3
TEXT_WINDOW_PRIVATE = 0
TEXT_WINDOW_RIGHT = 4
TEXT_WINDOW_TEXT = 2
TEXT_WINDOW_TOP = 5
TEXT_WINDOW_WIDGET = 1

TOOLBAR_BOTH = 2

TOOLBAR_BOTH_HORIZ = 3

TOOLBAR_CHILD_BUTTON = 1
TOOLBAR_CHILD_RADIOBUTTON = 3
TOOLBAR_CHILD_SPACE = 0
TOOLBAR_CHILD_TOGGLEBUTTON = 2
TOOLBAR_CHILD_WIDGET = 4

TOOLBAR_ICONS = 0

TOOLBAR_SPACE_EMPTY = 0
TOOLBAR_SPACE_LINE = 1

TOOLBAR_TEXT = 1

TOOL_PALETTE_DRAG_GROUPS = 2
TOOL_PALETTE_DRAG_ITEMS = 1

TOPLEVEL = 16

TOP_BOTTOM = 0

TREE_MODEL_ITERS_PERSIST = 1

TREE_MODEL_LIST_ONLY = 2

TREE_SORTABLE_DEFAULT_SORT_COLUMN_ID = -1

TREE_SORTABLE_UNSORTED_SORT_COLUMN_ID = -2

TREE_VIEW_COLUMN_AUTOSIZE = 1
TREE_VIEW_COLUMN_FIXED = 2

TREE_VIEW_COLUMN_GROW_ONLY = 0

TREE_VIEW_DROP_AFTER = 1
TREE_VIEW_DROP_BEFORE = 0

TREE_VIEW_DROP_INTO_OR_AFTER = 3
TREE_VIEW_DROP_INTO_OR_BEFORE = 2

TREE_VIEW_GRID_LINES_BOTH = 3
TREE_VIEW_GRID_LINES_HORIZONTAL = 1
TREE_VIEW_GRID_LINES_NONE = 0
TREE_VIEW_GRID_LINES_VERTICAL = 2

TREE_VIEW_ITEM = 1
TREE_VIEW_LINE = 0

UI_MANAGER_ACCELERATOR = 256
UI_MANAGER_AUTO = 0
UI_MANAGER_MENU = 2
UI_MANAGER_MENUBAR = 1
UI_MANAGER_MENUITEM = 32
UI_MANAGER_PLACEHOLDER = 8
UI_MANAGER_POPUP = 16

UI_MANAGER_POPUP_WITH_ACCELS = 512

UI_MANAGER_SEPARATOR = 128
UI_MANAGER_TOOLBAR = 4
UI_MANAGER_TOOLITEM = 64

UNIT_INCH = 2
UNIT_MM = 3
UNIT_PIXEL = 0
UNIT_POINTS = 1

UPDATE_ALWAYS = 0
UPDATE_CONTINUOUS = 0
UPDATE_DELAYED = 2
UPDATE_DISCONTINUOUS = 1

UPDATE_IF_VALID = 1

VISIBILITY_FULL = 2
VISIBILITY_NONE = 0
VISIBILITY_PARTIAL = 1

VISIBLE = 256

WIDGET_HELP_TOOLTIP = 0

WIDGET_HELP_WHATS_THIS = 1

WINDOW_POPUP = 1
WINDOW_TOPLEVEL = 0

WIN_POS_CENTER = 1

WIN_POS_CENTER_ALWAYS = 3

WIN_POS_CENTER_ON_PARENT = 4

WIN_POS_MOUSE = 2
WIN_POS_NONE = 0

WRAP_CHAR = 1
WRAP_NONE = 0
WRAP_WORD = 2

WRAP_WORD_CHAR = 3

__version__ = '2.24.0'

# functions

def about_dialog_set_email_hook(*args, **kwargs): # real signature unknown
    pass

def about_dialog_set_url_hook(*args, **kwargs): # real signature unknown
    pass

def accelerator_get_default_mod_mask(*args, **kwargs): # real signature unknown
    pass

def accelerator_get_label(*args, **kwargs): # real signature unknown
    pass

def accelerator_name(*args, **kwargs): # real signature unknown
    pass

def accelerator_parse(*args, **kwargs): # real signature unknown
    pass

def accelerator_set_default_mod_mask(*args, **kwargs): # real signature unknown
    pass

def accelerator_valid(*args, **kwargs): # real signature unknown
    pass

def accel_groups_activate(*args, **kwargs): # real signature unknown
    pass

def accel_groups_from_object(*args, **kwargs): # real signature unknown
    pass

def accel_group_from_accel_closure(*args, **kwargs): # real signature unknown
    pass

def accel_map_add_entry(*args, **kwargs): # real signature unknown
    pass

def accel_map_add_filter(*args, **kwargs): # real signature unknown
    pass

def accel_map_change_entry(*args, **kwargs): # real signature unknown
    pass

def accel_map_foreach(*args, **kwargs): # real signature unknown
    pass

def accel_map_foreach_unfiltered(*args, **kwargs): # real signature unknown
    pass

def accel_map_get(*args, **kwargs): # real signature unknown
    pass

def accel_map_load(*args, **kwargs): # real signature unknown
    pass

def accel_map_load_fd(*args, **kwargs): # real signature unknown
    pass

def accel_map_lock_path(*args, **kwargs): # real signature unknown
    pass

def accel_map_lookup_entry(*args, **kwargs): # real signature unknown
    pass

def accel_map_save(*args, **kwargs): # real signature unknown
    pass

def accel_map_save_fd(*args, **kwargs): # real signature unknown
    pass

def accel_map_unlock_path(*args, **kwargs): # real signature unknown
    pass

def add_log_handlers(*args, **kwargs): # real signature unknown
    pass

def alternative_dialog_button_order(*args, **kwargs): # real signature unknown
    pass

def bindings_activate(*args, **kwargs): # real signature unknown
    pass

def bindings_activate_event(*args, **kwargs): # real signature unknown
    pass

def binding_entry_add_signal(*args, **kwargs): # real signature unknown
    pass

def binding_entry_remove(*args, **kwargs): # real signature unknown
    pass

def cell_view_new_with_markup(*args, **kwargs): # real signature unknown
    pass

def cell_view_new_with_pixbuf(*args, **kwargs): # real signature unknown
    pass

def cell_view_new_with_text(*args, **kwargs): # real signature unknown
    pass

def check_version(*args, **kwargs): # real signature unknown
    pass

def clipboard_get(*args, **kwargs): # real signature unknown
    pass

def color_selection_palette_from_string(*args, **kwargs): # real signature unknown
    pass

def color_selection_palette_to_string(*args, **kwargs): # real signature unknown
    pass

def combo_box_entry_new_text(*args, **kwargs): # real signature unknown
    pass

def combo_box_entry_new_with_model(*args, **kwargs): # real signature unknown
    pass

def combo_box_new_text(*args, **kwargs): # real signature unknown
    pass

def combo_box_new_with_entry(*args, **kwargs): # real signature unknown
    pass

def combo_box_new_with_model_and_entry(*args, **kwargs): # real signature unknown
    pass

def combo_box_text_new_with_entry(*args, **kwargs): # real signature unknown
    pass

def container_class_install_child_property(*args, **kwargs): # real signature unknown
    pass

def container_class_list_child_properties(*args, **kwargs): # real signature unknown
    pass

def disable_setlocale(*args, **kwargs): # real signature unknown
    pass

def drag_get_source_widget(*args, **kwargs): # real signature unknown
    pass

def drag_set_default_icon(*args, **kwargs): # real signature unknown
    pass

def drag_source_set_icon_name(*args, **kwargs): # real signature unknown
    pass

def draw_insertion_cursor(*args, **kwargs): # real signature unknown
    pass

def events_pending(*args, **kwargs): # real signature unknown
    pass

def expander_new_with_mnemonic(*args, **kwargs): # real signature unknown
    pass

def file_chooser_widget_new_with_backend(*args, **kwargs): # real signature unknown
    pass

def get_current_event(*args, **kwargs): # real signature unknown
    pass

def get_current_event_state(*args, **kwargs): # real signature unknown
    pass

def get_current_event_time(*args, **kwargs): # real signature unknown
    pass

def get_default_language(*args, **kwargs): # real signature unknown
    pass

def grab_get_current(*args, **kwargs): # real signature unknown
    pass

def gtk_tooltips_data_get(*args, **kwargs): # real signature unknown
    pass

def gtk_window_get_default_icon_name(*args, **kwargs): # real signature unknown
    pass

def hbutton_box_get_layout_default(*args, **kwargs): # real signature unknown
    pass

def hbutton_box_get_spacing_default(*args, **kwargs): # real signature unknown
    pass

def hbutton_box_set_layout_default(*args, **kwargs): # real signature unknown
    pass

def hbutton_box_set_spacing_default(*args, **kwargs): # real signature unknown
    pass

def hsv_to_rgb(*args, **kwargs): # real signature unknown
    pass

def icon_factory_lookup_default(*args, **kwargs): # real signature unknown
    pass

def icon_info_new_for_pixbuf(*args, **kwargs): # real signature unknown
    pass

def icon_set_new(*args, **kwargs): # real signature unknown
    pass

def icon_size_from_name(*args, **kwargs): # real signature unknown
    pass

def icon_size_get_name(*args, **kwargs): # real signature unknown
    pass

def icon_size_lookup(*args, **kwargs): # real signature unknown
    pass

def icon_size_lookup_for_settings(*args, **kwargs): # real signature unknown
    pass

def icon_size_register(*args, **kwargs): # real signature unknown
    pass

def icon_size_register_alias(*args, **kwargs): # real signature unknown
    pass

def icon_theme_add_builtin_icon(*args, **kwargs): # real signature unknown
    pass

def icon_theme_get_default(*args, **kwargs): # real signature unknown
    pass

def icon_theme_get_for_screen(*args, **kwargs): # real signature unknown
    pass

def image_new_from_animation(*args, **kwargs): # real signature unknown
    pass

def image_new_from_file(*args, **kwargs): # real signature unknown
    pass

def image_new_from_gicon(*args, **kwargs): # real signature unknown
    pass

def image_new_from_icon_name(*args, **kwargs): # real signature unknown
    pass

def image_new_from_icon_set(*args, **kwargs): # real signature unknown
    pass

def image_new_from_image(*args, **kwargs): # real signature unknown
    pass

def image_new_from_pixbuf(*args, **kwargs): # real signature unknown
    pass

def image_new_from_pixmap(*args, **kwargs): # real signature unknown
    pass

def image_new_from_stock(*args, **kwargs): # real signature unknown
    pass

def init_check(*args, **kwargs): # real signature unknown
    pass

def item_factories_path_delete(*args, **kwargs): # real signature unknown
    pass

def item_factory_add_foreign(*args, **kwargs): # real signature unknown
    pass

def item_factory_from_path(*args, **kwargs): # real signature unknown
    pass

def item_factory_from_widget(*args, **kwargs): # real signature unknown
    pass

def item_factory_path_from_widget(*args, **kwargs): # real signature unknown
    pass

def link_button_new(*args, **kwargs): # real signature unknown
    pass

def link_button_set_uri_hook(*args, **kwargs): # real signature unknown
    pass

def main(*args, **kwargs): # real signature unknown
    pass

def main_do_event(*args, **kwargs): # real signature unknown
    pass

def main_iteration(*args, **kwargs): # real signature unknown
    pass

def main_iteration_do(*args, **kwargs): # real signature unknown
    pass

def main_level(*args, **kwargs): # real signature unknown
    pass

def main_quit(*args, **kwargs): # real signature unknown
    pass

def new_with_buffer(*args, **kwargs): # real signature unknown
    pass

def notebook_set_window_creation_hook(*args, **kwargs): # real signature unknown
    pass

def page_setup_new_from_file(*args, **kwargs): # real signature unknown
    pass

def paper_size_get_default(*args, **kwargs): # real signature unknown
    pass

def paper_size_new_custom(*args, **kwargs): # real signature unknown
    pass

def paper_size_new_from_ppd(*args, **kwargs): # real signature unknown
    pass

def plug_new_for_display(*args, **kwargs): # real signature unknown
    pass

def preview_get_cmap(*args, **kwargs): # real signature unknown
    pass

def preview_get_visual(*args, **kwargs): # real signature unknown
    pass

def preview_reset(*args, **kwargs): # real signature unknown
    pass

def preview_set_color_cube(*args, **kwargs): # real signature unknown
    pass

def preview_set_gamma(*args, **kwargs): # real signature unknown
    pass

def preview_set_install_cmap(*args, **kwargs): # real signature unknown
    pass

def preview_set_reserved(*args, **kwargs): # real signature unknown
    pass

def print_run_page_setup_dialog(*args, **kwargs): # real signature unknown
    pass

def print_settings_new_from_file(*args, **kwargs): # real signature unknown
    pass

def quit_add(*args, **kwargs): # real signature unknown
    pass

def quit_remove(*args, **kwargs): # real signature unknown
    pass

def rc_add_default_file(*args, **kwargs): # real signature unknown
    pass

def rc_find_module_in_path(*args, **kwargs): # real signature unknown
    pass

def rc_get_default_files(*args, **kwargs): # real signature unknown
    pass

def rc_get_im_module_file(*args, **kwargs): # real signature unknown
    pass

def rc_get_im_module_path(*args, **kwargs): # real signature unknown
    pass

def rc_get_module_dir(*args, **kwargs): # real signature unknown
    pass

def rc_get_style_by_paths(*args, **kwargs): # real signature unknown
    pass

def rc_get_theme_dir(*args, **kwargs): # real signature unknown
    pass

def rc_parse(*args, **kwargs): # real signature unknown
    pass

def rc_parse_string(*args, **kwargs): # real signature unknown
    pass

def rc_reparse_all(*args, **kwargs): # real signature unknown
    pass

def rc_reparse_all_for_settings(*args, **kwargs): # real signature unknown
    pass

def rc_reset_styles(*args, **kwargs): # real signature unknown
    pass

def rc_set_default_files(*args, **kwargs): # real signature unknown
    pass

def recent_action_new_for_manager(*args, **kwargs): # real signature unknown
    pass

def recent_manager_get_default(*args, **kwargs): # real signature unknown
    pass

def recent_manager_get_for_screen(*args, **kwargs): # real signature unknown
    pass

def remove_log_handlers(*args, **kwargs): # real signature unknown
    pass

def selection_owner_set_for_display(*args, **kwargs): # real signature unknown
    pass

def settings_get_default(*args, **kwargs): # real signature unknown
    pass

def settings_get_for_screen(*args, **kwargs): # real signature unknown
    pass

def set_interactive(*args, **kwargs): # real signature unknown
    pass

def show_about_dialog(*args, **kwargs): # real signature unknown
    pass

def show_uri(*args, **kwargs): # real signature unknown
    pass

def status_icon_new_from_file(*args, **kwargs): # real signature unknown
    pass

def status_icon_new_from_gicon(*args, **kwargs): # real signature unknown
    pass

def status_icon_new_from_icon_name(*args, **kwargs): # real signature unknown
    pass

def status_icon_new_from_pixbuf(*args, **kwargs): # real signature unknown
    pass

def status_icon_new_from_stock(*args, **kwargs): # real signature unknown
    pass

def status_icon_position_menu(*args, **kwargs): # real signature unknown
    pass

def stock_add(*args, **kwargs): # real signature unknown
    pass

def stock_list_ids(*args, **kwargs): # real signature unknown
    pass

def stock_lookup(*args, **kwargs): # real signature unknown
    pass

def targets_include_image(*args, **kwargs): # real signature unknown
    pass

def targets_include_rich_text(*args, **kwargs): # real signature unknown
    pass

def targets_include_text(*args, **kwargs): # real signature unknown
    pass

def targets_include_uri(*args, **kwargs): # real signature unknown
    pass

def target_list_add_image_targets(*args, **kwargs): # real signature unknown
    pass

def target_list_add_rich_text_targets(*args, **kwargs): # real signature unknown
    pass

def target_list_add_text_targets(*args, **kwargs): # real signature unknown
    pass

def target_list_add_uri_targets(*args, **kwargs): # real signature unknown
    pass

def tooltips_data_get(*args, **kwargs): # real signature unknown
    pass

def tooltip_trigger_tooltip_query(*args, **kwargs): # real signature unknown
    pass

def vbutton_box_get_layout_default(*args, **kwargs): # real signature unknown
    pass

def vbutton_box_get_spacing_default(*args, **kwargs): # real signature unknown
    pass

def vbutton_box_set_layout_default(*args, **kwargs): # real signature unknown
    pass

def vbutton_box_set_spacing_default(*args, **kwargs): # real signature unknown
    pass

def widget_class_find_style_property(*args, **kwargs): # real signature unknown
    pass

def widget_class_install_style_property(*args, **kwargs): # real signature unknown
    pass

def widget_class_list_style_properties(*args, **kwargs): # real signature unknown
    pass

def widget_get_default_colormap(*args, **kwargs): # real signature unknown
    pass

def widget_get_default_direction(*args, **kwargs): # real signature unknown
    pass

def widget_get_default_style(*args, **kwargs): # real signature unknown
    pass

def widget_get_default_visual(*args, **kwargs): # real signature unknown
    pass

def widget_pop_colormap(*args, **kwargs): # real signature unknown
    pass

def widget_pop_composite_child(*args, **kwargs): # real signature unknown
    pass

def widget_push_colormap(*args, **kwargs): # real signature unknown
    pass

def widget_push_composite_child(*args, **kwargs): # real signature unknown
    pass

def widget_set_default_colormap(*args, **kwargs): # real signature unknown
    pass

def widget_set_default_direction(*args, **kwargs): # real signature unknown
    pass

def window_get_default_icon_list(*args, **kwargs): # real signature unknown
    pass

def window_list_toplevels(*args, **kwargs): # real signature unknown
    pass

def window_set_auto_startup_notification(*args, **kwargs): # real signature unknown
    pass

def window_set_default_icon(*args, **kwargs): # real signature unknown
    pass

def window_set_default_icon_from_file(*args, **kwargs): # real signature unknown
    pass

def window_set_default_icon_list(*args, **kwargs): # real signature unknown
    pass

def window_set_default_icon_name(*args, **kwargs): # real signature unknown
    pass

# classes

from Buildable import Buildable
from Object import Object
from Widget import Widget
from Container import Container
from Bin import Bin
from Window import Window
from Dialog import Dialog
from AboutDialog import AboutDialog
from AccelFlags import AccelFlags
from AccelGroup import AccelGroup
from Misc import Misc
from Label import Label
from AccelLabel import AccelLabel
from AccelMap import AccelMap
from Accessible import Accessible
from Action import Action
from ActionGroup import ActionGroup
from Activatable import Activatable
from Adjustment import Adjustment
from Alignment import Alignment
from AnchorType import AnchorType
from ArgFlags import ArgFlags
from Arrow import Arrow
from ArrowType import ArrowType
from Frame import Frame
from AspectFrame import AspectFrame
from Assistant import Assistant
from AssistantPageType import AssistantPageType
from AttachOptions import AttachOptions
from Border import Border
from Orientable import Orientable
from Box import Box
from Builder import Builder
from BuilderError import BuilderError
from Button import Button
from ButtonAction import ButtonAction
from ButtonBox import ButtonBox
from ButtonBoxStyle import ButtonBoxStyle
from ButtonsType import ButtonsType
from Calendar import Calendar
from CalendarDisplayOptions import CalendarDisplayOptions
from CellEditable import CellEditable
from CellLayout import CellLayout
from CellRenderer import CellRenderer
from CellRendererText import CellRendererText
from CellRendererAccel import CellRendererAccel
from CellRendererAccelMode import CellRendererAccelMode
from CellRendererCombo import CellRendererCombo
from CellRendererMode import CellRendererMode
from CellRendererPixbuf import CellRendererPixbuf
from CellRendererProgress import CellRendererProgress
from CellRendererSpin import CellRendererSpin
from CellRendererSpinner import CellRendererSpinner
from CellRendererState import CellRendererState
from CellRendererToggle import CellRendererToggle
from CellType import CellType
from CellView import CellView
from ToggleButton import ToggleButton
from CheckButton import CheckButton
from Item import Item
from MenuItem import MenuItem
from CheckMenuItem import CheckMenuItem
from Clipboard import Clipboard
from CList import CList
from CListDragPos import CListDragPos
from ColorButton import ColorButton
from VBox import VBox
from ColorSelection import ColorSelection
from ColorSelectionDialog import ColorSelectionDialog
from HBox import HBox
from Combo import Combo
from ComboBox import ComboBox
from ComboBoxEntry import ComboBoxEntry
from CornerType import CornerType
from CTree import CTree
from CTreeExpanderStyle import CTreeExpanderStyle
from CTreeExpansionType import CTreeExpansionType
from CTreeLineStyle import CTreeLineStyle
from CTreeNode import CTreeNode
from CTreePos import CTreePos
from DrawingArea import DrawingArea
from Curve import Curve
from CurveType import CurveType
from DebugFlag import DebugFlag
from DeleteType import DeleteType
from DeprecationWarning import DeprecationWarning
from DestDefaults import DestDefaults
from DialogFlags import DialogFlags
from DirectionType import DirectionType
from Editable import Editable
from Entry import Entry
from EntryBuffer import EntryBuffer
from EntryCompletion import EntryCompletion
from EntryIconPosition import EntryIconPosition
from EventBox import EventBox
from Expander import Expander
from ExpanderStyle import ExpanderStyle
from FileChooser import FileChooser
from FileChooserAction import FileChooserAction
from FileChooserButton import FileChooserButton
from FileChooserConfirmation import FileChooserConfirmation
from FileChooserDialog import FileChooserDialog
from FileChooserError import FileChooserError
from FileChooserWidget import FileChooserWidget
from FileFilter import FileFilter
from FileFilterFlags import FileFilterFlags
from FileSelection import FileSelection
from Fixed import Fixed
from FontButton import FontButton
from FontSelection import FontSelection
from FontSelectionDialog import FontSelectionDialog
from GammaCurve import GammaCurve
from GdkAtomType import GdkAtomType
from GenericCellRenderer import GenericCellRenderer
from TreeModel import TreeModel
from GenericTreeModel import GenericTreeModel
from HandleBox import HandleBox
from HButtonBox import HButtonBox
from Paned import Paned
from HPaned import HPaned
from Ruler import Ruler
from HRuler import HRuler
from Range import Range
from Scale import Scale
from HScale import HScale
from Scrollbar import Scrollbar
from HScrollbar import HScrollbar
from Separator import Separator
from HSeparator import HSeparator
from HSV import HSV
from IconFactory import IconFactory
from IconInfo import IconInfo
from IconLookupFlags import IconLookupFlags
from IconSet import IconSet
from IconSize import IconSize
from IconSource import IconSource
from IconTheme import IconTheme
from IconThemeError import IconThemeError
from IconView import IconView
from IconViewDropPosition import IconViewDropPosition
from Image import Image
from ImageMenuItem import ImageMenuItem
from ImageType import ImageType
from IMContext import IMContext
from IMContextSimple import IMContextSimple
from IMMulticontext import IMMulticontext
from IMPreeditStyle import IMPreeditStyle
from IMStatusStyle import IMStatusStyle
from InfoBar import InfoBar
from InputDialog import InputDialog
from Invisible import Invisible
from ItemFactory import ItemFactory
from Justification import Justification
from Layout import Layout
from LinkButton import LinkButton
from List import List
from ListItem import ListItem
from TreeDragDest import TreeDragDest
from TreeDragSource import TreeDragSource
from TreeSortable import TreeSortable
from ListStore import ListStore
from MatchType import MatchType
from MenuShell import MenuShell
from Menu import Menu
from MenuBar import MenuBar
from MenuDirectionType import MenuDirectionType
from ToolItem import ToolItem
from ToolButton import ToolButton
from MenuToolButton import MenuToolButton
from MessageDialog import MessageDialog
from MessageType import MessageType
from MetricType import MetricType
from MountOperation import MountOperation
from MovementStep import MovementStep
from Notebook import Notebook
from NotebookTab import NotebookTab
from NumberUpLayout import NumberUpLayout
from ObjectFlags import ObjectFlags
from OffscreenWindow import OffscreenWindow
from OldEditable import OldEditable
from OptionMenu import OptionMenu
from Orientation import Orientation
from PackDirection import PackDirection
from PackType import PackType
from PageOrientation import PageOrientation
from PageSet import PageSet
from PageSetup import PageSetup
from PaperSize import PaperSize
from PathPriorityType import PathPriorityType
from PathType import PathType
from Pixmap import Pixmap
from Plug import Plug
from PolicyType import PolicyType
from PositionType import PositionType
from Preview import Preview
from PreviewType import PreviewType
from PrintContext import PrintContext
from PrintDuplex import PrintDuplex
from PrintError import PrintError
from PrintOperationPreview import PrintOperationPreview
from PrintOperation import PrintOperation
from PrintOperationAction import PrintOperationAction
from PrintOperationResult import PrintOperationResult
from PrintPages import PrintPages
from PrintQuality import PrintQuality
from PrintSettings import PrintSettings
from PrintStatus import PrintStatus
from PrivateFlags import PrivateFlags
from Progress import Progress
from ProgressBar import ProgressBar
from ProgressBarOrientation import ProgressBarOrientation
from ProgressBarStyle import ProgressBarStyle
from ToggleAction import ToggleAction
from RadioAction import RadioAction
from RadioButton import RadioButton
from RadioMenuItem import RadioMenuItem
from ToggleToolButton import ToggleToolButton
from RadioToolButton import RadioToolButton
from RcFlags import RcFlags
from RcStyle import RcStyle
from RcTokenType import RcTokenType
from RecentChooser import RecentChooser
from RecentAction import RecentAction
from RecentChooserDialog import RecentChooserDialog
from RecentChooserError import RecentChooserError
from RecentChooserMenu import RecentChooserMenu
from RecentChooserWidget import RecentChooserWidget
from RecentFilter import RecentFilter
from RecentFilterFlags import RecentFilterFlags
from RecentInfo import RecentInfo
from RecentManager import RecentManager
from RecentManagerError import RecentManagerError
from RecentSortType import RecentSortType
from ReliefStyle import ReliefStyle
from Requisition import Requisition
from ResizeMode import ResizeMode
from ResponseType import ResponseType
from ScaleButton import ScaleButton
from ScrolledWindow import ScrolledWindow
from ScrollStep import ScrollStep
from ScrollType import ScrollType
from SelectionData import SelectionData
from SelectionMode import SelectionMode
from SensitivityType import SensitivityType
from SeparatorMenuItem import SeparatorMenuItem
from SeparatorToolItem import SeparatorToolItem
from Settings import Settings
from ShadowType import ShadowType
from SideType import SideType
from SizeGroup import SizeGroup
from SizeGroupMode import SizeGroupMode
from Socket import Socket
from SortType import SortType
from SpinButton import SpinButton
from SpinButtonUpdatePolicy import SpinButtonUpdatePolicy
from Spinner import Spinner
from SpinType import SpinType
from StateType import StateType
from Statusbar import Statusbar
from StatusIcon import StatusIcon
from Style import Style
from SubmenuDirection import SubmenuDirection
from SubmenuPlacement import SubmenuPlacement
from Table import Table
from TargetFlags import TargetFlags
from TearoffMenuItem import TearoffMenuItem
from TextAttributes import TextAttributes
from TextBuffer import TextBuffer
from TextBufferTargetInfo import TextBufferTargetInfo
from TextChildAnchor import TextChildAnchor
from TextDirection import TextDirection
from TextIter import TextIter
from TextMark import TextMark
from TextSearchFlags import TextSearchFlags
from TextTag import TextTag
from TextTagTable import TextTagTable
from TextView import TextView
from TextWindowType import TextWindowType
from ToolShell import ToolShell
from Toolbar import Toolbar
from ToolbarChildType import ToolbarChildType
from ToolbarSpaceStyle import ToolbarSpaceStyle
from ToolbarStyle import ToolbarStyle
from ToolItemGroup import ToolItemGroup
from ToolPalette import ToolPalette
from ToolPaletteDragTargets import ToolPaletteDragTargets
from Tooltip import Tooltip
from Tooltips import Tooltips
from TreeIter import TreeIter
from TreeModelFilter import TreeModelFilter
from TreeModelFlags import TreeModelFlags
from TreeModelSort import TreeModelSort
from TreeRowReference import TreeRowReference
from TreeSelection import TreeSelection
from TreeStore import TreeStore
from TreeView import TreeView
from TreeViewColumn import TreeViewColumn
from TreeViewColumnSizing import TreeViewColumnSizing
from TreeViewDropPosition import TreeViewDropPosition
from TreeViewGridLines import TreeViewGridLines
from TreeViewMode import TreeViewMode
from UIManager import UIManager
from UIManagerItemType import UIManagerItemType
from Unit import Unit
from UpdateType import UpdateType
from VButtonBox import VButtonBox
from Viewport import Viewport
from Visibility import Visibility
from VolumeButton import VolumeButton
from VPaned import VPaned
from VRuler import VRuler
from VScale import VScale
from VScrollbar import VScrollbar
from VSeparator import VSeparator
from Warning import Warning
from WidgetFlags import WidgetFlags
from WidgetHelpType import WidgetHelpType
from WindowGroup import WindowGroup
from WindowPosition import WindowPosition
from WindowType import WindowType
from WrapMode import WrapMode
# variables with complex values

gtk_version = (
    2,
    24,
    30,
)

pygtk_version = (
    2,
    24,
    0,
)

_PyGtk_API = None # (!) real value is ''

