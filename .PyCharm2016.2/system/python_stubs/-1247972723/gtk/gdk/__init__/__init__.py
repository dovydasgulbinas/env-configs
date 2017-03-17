# encoding: utf-8
# module gtk.gdk
# from /usr/lib/python2.7/dist-packages/webkit/webkit.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
from exceptions import Warning

import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import pango as __pango
import pangocairo as __pangocairo


# Variables with simple values

ACTION_ASK = 32
ACTION_COPY = 2
ACTION_DEFAULT = 1
ACTION_LINK = 8
ACTION_MOVE = 4
ACTION_PRIVATE = 16

ALL_EVENTS_MASK = 4194302

AND = 4

AND_INVERT = 6
AND_REVERSE = 5

ARROW = 2

AXIS_IGNORE = 0
AXIS_LAST = 7
AXIS_PRESSURE = 3
AXIS_WHEEL = 6
AXIS_X = 1
AXIS_XTILT = 4
AXIS_Y = 2
AXIS_YTILT = 5

BASED_ARROW_DOWN = 4
BASED_ARROW_UP = 6

BLANK_CURSOR = -2

BOAT = 8
BOGOSITY = 10

BOTTOM_LEFT_CORNER = 12

BOTTOM_RIGHT_CORNER = 14

BOTTOM_SIDE = 16
BOTTOM_TEE = 18

BOX_SPIRAL = 20

BUTTON1_MASK = 256

BUTTON1_MOTION_MASK = 32

BUTTON2_MASK = 512

BUTTON2_MOTION_MASK = 64

BUTTON3_MASK = 1024

BUTTON3_MOTION_MASK = 128

BUTTON4_MASK = 2048

BUTTON5_MASK = 4096

BUTTON_MOTION_MASK = 16

BUTTON_PRESS = 4

BUTTON_PRESS_MASK = 256

BUTTON_RELEASE = 7

BUTTON_RELEASE_MASK = 512

CAP_BUTT = 1

CAP_NOT_LAST = 0

CAP_PROJECTING = 3
CAP_ROUND = 2

CENTER_PTR = 22

CIRCLE = 24

CLEAR = 3

CLIENT_EVENT = 28

CLIP_BY_CHILDREN = 0

CLOCK = 26

COFFEE_MUG = 28

COLORSPACE_RGB = 0

CONFIGURE = 13

CONTROL_MASK = 4

COPY = 0

COPY_INVERT = 11

CROSS = 30
CROSSHAIR = 34

CROSSING_GRAB = 1

CROSSING_GTK_GRAB = 3
CROSSING_GTK_UNGRAB = 4

CROSSING_NORMAL = 0

CROSSING_STATE_CHANGED = 5

CROSSING_UNGRAB = 2

CROSS_REVERSE = 32

CURRENT_TIME = 0L

CURSOR_IS_PIXMAP = -1

DAMAGE = 36

DECOR_ALL = 1
DECOR_BORDER = 2
DECOR_MAXIMIZE = 64
DECOR_MENU = 16
DECOR_MINIMIZE = 32
DECOR_RESIZEH = 4
DECOR_TITLE = 8

DELETE = 0
DESTROY = 1

DIAMOND_CROSS = 36

DOT = 38
DOTBOX = 40

DOUBLE_ARROW = 42

DRAFT_LARGE = 44
DRAFT_SMALL = 46

DRAG_ENTER = 22
DRAG_LEAVE = 23
DRAG_MOTION = 24

DRAG_PROTO_LOCAL = 6
DRAG_PROTO_MOTIF = 0
DRAG_PROTO_NONE = 3
DRAG_PROTO_OLE2 = 5
DRAG_PROTO_ROOTWIN = 2

DRAG_PROTO_WIN32_DROPFILES = 4

DRAG_PROTO_XDND = 1

DRAG_STATUS = 25

DRAPED_BOX = 48

DROP_FINISHED = 27
DROP_START = 26

ENTER_NOTIFY = 10

ENTER_NOTIFY_MASK = 4096

EQUIV = 9

ERROR = -1

ERROR_FILE = -3
ERROR_MEM = -4
ERROR_PARAM = -2

EVENT_LAST = 37

EVEN_ODD_RULE = 0

EXCHANGE = 50
EXPOSE = 2

EXPOSURE_MASK = 2

EXTENSION_EVENTS_ALL = 1
EXTENSION_EVENTS_CURSOR = 2
EXTENSION_EVENTS_NONE = 0

FILTER_CONTINUE = 0
FILTER_REMOVE = 2
FILTER_TRANSLATE = 1

FLEUR = 52

FOCUS_CHANGE = 12

FOCUS_CHANGE_MASK = 16384

FONT_FONT = 0
FONT_FONTSET = 1

FUNC_ALL = 1
FUNC_CLOSE = 32
FUNC_MAXIMIZE = 16
FUNC_MINIMIZE = 8
FUNC_MOVE = 4
FUNC_RESIZE = 2

GC_BACKGROUND = 2

GC_CAP_STYLE = 65536

GC_CLIP_MASK = 128

GC_CLIP_X_ORIGIN = 2048

GC_CLIP_Y_ORIGIN = 4096

GC_EXPOSURES = 8192
GC_FILL = 16
GC_FONT = 4
GC_FOREGROUND = 1
GC_FUNCTION = 8

GC_JOIN_STYLE = 131072

GC_LINE_STYLE = 32768
GC_LINE_WIDTH = 16384

GC_STIPPLE = 64
GC_SUBWINDOW = 256
GC_TILE = 32

GC_TS_X_ORIGIN = 512

GC_TS_Y_ORIGIN = 1024

GOBBLER = 54

GRAB_ALREADY_GRABBED = 1

GRAB_BROKEN = 35
GRAB_FROZEN = 4

GRAB_INVALID_TIME = 2

GRAB_NOT_VIEWABLE = 3

GRAB_SUCCESS = 0

GRAVITY_CENTER = 5
GRAVITY_EAST = 6
GRAVITY_NORTH = 2

GRAVITY_NORTH_EAST = 3
GRAVITY_NORTH_WEST = 1

GRAVITY_SOUTH = 8

GRAVITY_SOUTH_EAST = 9
GRAVITY_SOUTH_WEST = 7

GRAVITY_STATIC = 10
GRAVITY_WEST = 4

GUMBY = 56

HAND1 = 58
HAND2 = 60

HEART = 62

HINT_ASPECT = 16

HINT_BASE_SIZE = 8

HINT_MAX_SIZE = 4

HINT_MIN_SIZE = 2

HINT_POS = 1

HINT_RESIZE_INC = 32

HINT_USER_POS = 128
HINT_USER_SIZE = 256

HINT_WIN_GRAVITY = 64

HYPER_MASK = 134217728

ICON = 64

IMAGE_FASTEST = 2
IMAGE_NORMAL = 0
IMAGE_SHARED = 1

INCLUDE_INFERIORS = 1

INPUT_EXCEPTION = 2
INPUT_ONLY = 1
INPUT_OUTPUT = 0
INPUT_READ = 25
INPUT_WRITE = 20

INTERP_BILINEAR = 2
INTERP_HYPER = 3
INTERP_NEAREST = 0
INTERP_TILES = 1

INVERT = 1

IRON_CROSS = 66

JOIN_BEVEL = 2
JOIN_MITER = 0
JOIN_ROUND = 1

KEY_PRESS = 8

KEY_PRESS_MASK = 1024

KEY_RELEASE = 9

KEY_RELEASE_MASK = 2048

LAST_CURSOR = 153

LEAVE_NOTIFY = 11

LEAVE_NOTIFY_MASK = 8192

LEFTBUTTON = 74

LEFT_PTR = 68
LEFT_SIDE = 70
LEFT_TEE = 72

LINE_DOUBLE_DASH = 2

LINE_ON_OFF_DASH = 1

LINE_SOLID = 0

LL_ANGLE = 76

LOCK_MASK = 2

LR_ANGLE = 78

LSB_FIRST = 0

MAN = 80
MAP = 14

META_MASK = 268435456

MIDDLEBUTTON = 82

MOD1_MASK = 8

MOD2_MASK = 16

MOD3_MASK = 32

MOD4_MASK = 64

MOD5_MASK = 128

MODE_DISABLED = 0
MODE_SCREEN = 1
MODE_WINDOW = 2

MODIFIER_MASK = 1543512063

MOTION_NOTIFY = 3

MOUSE = 84

MSB_FIRST = 1

NAND = 13

NOOP = 7
NOR = 14
NOTHING = -1

NOTIFY_ANCESTOR = 0
NOTIFY_INFERIOR = 2
NOTIFY_NONLINEAR = 3

NOTIFY_NONLINEAR_VIRTUAL = 4

NOTIFY_UNKNOWN = 5
NOTIFY_VIRTUAL = 1

NO_EXPOSE = 30

OK = 0

OPAQUE_STIPPLED = 3

OR = 8
OR_INVERT = 12
OR_REVERSE = 10

OVERLAP_RECTANGLE_IN = 0
OVERLAP_RECTANGLE_OUT = 1
OVERLAP_RECTANGLE_PART = 2

OWNER_CHANGE = 34

OWNER_CHANGE_CLOSE = 2
OWNER_CHANGE_DESTROY = 1

OWNER_CHANGE_NEW_OWNER = 0

PARENT_RELATIVE = 1L

PENCIL = 86

PIRATE = 88

PIXBUF_ALPHA_BILEVEL = 0
PIXBUF_ALPHA_FULL = 1

PIXBUF_ERROR_BAD_OPTION = 2

PIXBUF_ERROR_CORRUPT_IMAGE = 0

PIXBUF_ERROR_FAILED = 5

PIXBUF_ERROR_INSUFFICIENT_MEMORY = 1

PIXBUF_ERROR_UNKNOWN_TYPE = 3

PIXBUF_ERROR_UNSUPPORTED_OPERATION = 4

PIXBUF_ROTATE_CLOCKWISE = 270
PIXBUF_ROTATE_COUNTERCLOCKWISE = 90
PIXBUF_ROTATE_NONE = 0
PIXBUF_ROTATE_UPSIDEDOWN = 180

PLUS = 90

POINTER_MOTION_HINT_MASK = 8

POINTER_MOTION_MASK = 4

PROPERTY_CHANGE_MASK = 65536

PROPERTY_DELETE = 1

PROPERTY_NEW_VALUE = 0

PROPERTY_NOTIFY = 16

PROP_MODE_APPEND = 2
PROP_MODE_PREPEND = 1
PROP_MODE_REPLACE = 0

PROXIMITY_IN = 20

PROXIMITY_IN_MASK = 262144

PROXIMITY_OUT = 21

PROXIMITY_OUT_MASK = 524288

QUESTION_ARROW = 92

RELEASE_MASK = 1073741824

RGB_DITHER_MAX = 2
RGB_DITHER_NONE = 0
RGB_DITHER_NORMAL = 1

RIGHTBUTTON = 100

RIGHT_PTR = 94
RIGHT_SIDE = 96
RIGHT_TEE = 98

RTL_LOGO = 102

SAILBOAT = 104

SB_DOWN_ARROW = 106

SB_H_DOUBLE_ARROW = 108

SB_LEFT_ARROW = 110

SB_RIGHT_ARROW = 112

SB_UP_ARROW = 114

SB_V_DOUBLE_ARROW = 116

SCROLL = 31

SCROLL_DOWN = 1
SCROLL_LEFT = 2
SCROLL_MASK = 2097152
SCROLL_RIGHT = 3
SCROLL_UP = 0

SELECTION_CLEAR = 17
SELECTION_CLIPBOARD = 'CLIPBOARD'
SELECTION_NOTIFY = 19
SELECTION_PRIMARY = 'PRIMARY'
SELECTION_REQUEST = 18
SELECTION_SECONDARY = 'SECONDARY'

SELECTION_TYPE_ATOM = 'ATOM'
SELECTION_TYPE_BITMAP = 'BITMAP'
SELECTION_TYPE_COLORMAP = 'COLORMAP'
SELECTION_TYPE_DRAWABLE = 'DRAWABLE'
SELECTION_TYPE_INTEGER = 'INTEGER'
SELECTION_TYPE_PIXMAP = 'PIXMAP'
SELECTION_TYPE_STRING = 'STRING'
SELECTION_TYPE_WINDOW = 'WINDOW'

SET = 15
SETTING = 33

SETTING_ACTION_CHANGED = 1
SETTING_ACTION_DELETED = 2
SETTING_ACTION_NEW = 0

SHIFT_MASK = 1

SHUTTLE = 118

SIZING = 120

SOLID = 0

SOURCE_CURSOR = 3
SOURCE_ERASER = 2
SOURCE_MOUSE = 0
SOURCE_PEN = 1

SPIDER = 122
SPRAYCAN = 124

STAR = 126
STIPPLED = 2

STRUCTURE_MASK = 32768

SUBSTRUCTURE_MASK = 1048576

SUPER_MASK = 67108864

TARGET = 128

TARGET_BITMAP = 'BITMAP'
TARGET_COLORMAP = 'COLORMAP'
TARGET_DRAWABLE = 'DRAWABLE'
TARGET_PIXMAP = 'PIXMAP'
TARGET_STRING = 'STRING'

TCROSS = 130

TILED = 1

TOP_LEFT_ARROW = 132
TOP_LEFT_CORNER = 134

TOP_RIGHT_CORNER = 136

TOP_SIDE = 138
TOP_TEE = 140

TREK = 142

UL_ANGLE = 144

UMBRELLA = 146

UNMAP = 15

UR_ANGLE = 148

VISIBILITY_FULLY_OBSCURED = 2

VISIBILITY_NOTIFY = 29

VISIBILITY_NOTIFY_MASK = 131072

VISIBILITY_PARTIAL = 1
VISIBILITY_UNOBSCURED = 0

VISUAL_DIRECT_COLOR = 5

VISUAL_GRAYSCALE = 1

VISUAL_PSEUDO_COLOR = 3

VISUAL_STATIC_COLOR = 2
VISUAL_STATIC_GRAY = 0

VISUAL_TRUE_COLOR = 4

WATCH = 150
WA_COLORMAP = 32
WA_CURSOR = 16
WA_NOREDIR = 256
WA_TITLE = 2

WA_TYPE_HINT = 512

WA_VISUAL = 64
WA_WMCLASS = 128
WA_X = 4
WA_Y = 8

WINDING_RULE = 1

WINDOWING = 'x11'

WINDOW_CHILD = 2
WINDOW_DIALOG = 3

WINDOW_EDGE_EAST = 4
WINDOW_EDGE_NORTH = 1

WINDOW_EDGE_NORTH_EAST = 2
WINDOW_EDGE_NORTH_WEST = 0

WINDOW_EDGE_SOUTH = 6

WINDOW_EDGE_SOUTH_EAST = 7
WINDOW_EDGE_SOUTH_WEST = 5

WINDOW_EDGE_WEST = 3

WINDOW_FOREIGN = 5
WINDOW_OFFSCREEN = 6
WINDOW_ROOT = 0
WINDOW_STATE = 32

WINDOW_STATE_ABOVE = 32
WINDOW_STATE_BELOW = 64
WINDOW_STATE_FULLSCREEN = 16
WINDOW_STATE_ICONIFIED = 2
WINDOW_STATE_MAXIMIZED = 4
WINDOW_STATE_STICKY = 8
WINDOW_STATE_WITHDRAWN = 1

WINDOW_TEMP = 4
WINDOW_TOPLEVEL = 1

WINDOW_TYPE_HINT_COMBO = 12
WINDOW_TYPE_HINT_DESKTOP = 7
WINDOW_TYPE_HINT_DIALOG = 1
WINDOW_TYPE_HINT_DND = 13
WINDOW_TYPE_HINT_DOCK = 6

WINDOW_TYPE_HINT_DROPDOWN_MENU = 8

WINDOW_TYPE_HINT_MENU = 2
WINDOW_TYPE_HINT_NORMAL = 0
WINDOW_TYPE_HINT_NOTIFICATION = 11

WINDOW_TYPE_HINT_POPUP_MENU = 9

WINDOW_TYPE_HINT_SPLASHSCREEN = 4
WINDOW_TYPE_HINT_TOOLBAR = 3
WINDOW_TYPE_HINT_TOOLTIP = 10
WINDOW_TYPE_HINT_UTILITY = 5

XOR = 2

XTERM = 152

X_CURSOR = 0

_2BUTTON_PRESS = 5

_3BUTTON_PRESS = 6

__version__ = '2.24.0'

# functions

def atom_intern(*args, **kwargs): # real signature unknown
    pass

def beep(*args, **kwargs): # real signature unknown
    pass

def bitmap_create_from_data(*args, **kwargs): # real signature unknown
    pass

def colormap_get_system(*args, **kwargs): # real signature unknown
    pass

def colormap_get_system_size(*args, **kwargs): # real signature unknown
    pass

def colors_store(*args, **kwargs): # real signature unknown
    pass

def color_change(*args, **kwargs): # real signature unknown
    pass

def color_from_hsv(*args, **kwargs): # real signature unknown
    pass

def color_parse(*args, **kwargs): # real signature unknown
    pass

def cursor_new_from_name(*args, **kwargs): # real signature unknown
    pass

def devices_list(*args, **kwargs): # real signature unknown
    pass

def device_get_core_pointer(*args, **kwargs): # real signature unknown
    pass

def display_get_default(*args, **kwargs): # real signature unknown
    pass

def display_manager_get(*args, **kwargs): # real signature unknown
    pass

def draw_glyphs_transformed(*args, **kwargs): # real signature unknown
    pass

def draw_layout_with_colors(*args, **kwargs): # real signature unknown
    pass

def error_trap_pop(*args, **kwargs): # real signature unknown
    pass

def error_trap_push(*args, **kwargs): # real signature unknown
    pass

def events_pending(*args, **kwargs): # real signature unknown
    pass

def event_get(*args, **kwargs): # real signature unknown
    pass

def event_get_graphics_expose(*args, **kwargs): # real signature unknown
    pass

def event_handler_set(*args, **kwargs): # real signature unknown
    pass

def event_peek(*args, **kwargs): # real signature unknown
    pass

def event_request_motions(*args, **kwargs): # real signature unknown
    pass

def event_send_client_message_for_display(*args, **kwargs): # real signature unknown
    pass

def exit(*args, **kwargs): # real signature unknown
    pass

def flush(*args, **kwargs): # real signature unknown
    pass

def fontset_load(*args, **kwargs): # real signature unknown
    pass

def fontset_load_for_display(*args, **kwargs): # real signature unknown
    pass

def font_from_description(*args, **kwargs): # real signature unknown
    pass

def font_from_description_for_display(*args, **kwargs): # real signature unknown
    pass

def font_load_for_display(*args, **kwargs): # real signature unknown
    pass

def free_compound_text(*args, **kwargs): # real signature unknown
    pass

def gc_new(*args, **kwargs): # real signature unknown
    pass

def get_default_root_window(*args, **kwargs): # real signature unknown
    pass

def get_display(*args, **kwargs): # real signature unknown
    pass

def get_display_arg_name(*args, **kwargs): # real signature unknown
    pass

def get_program_class(*args, **kwargs): # real signature unknown
    pass

def get_show_events(*args, **kwargs): # real signature unknown
    pass

def get_use_xshm(*args, **kwargs): # real signature unknown
    pass

def input_remove(*args, **kwargs): # real signature unknown
    pass

def keyboard_grab(*args, **kwargs): # real signature unknown
    pass

def keyboard_ungrab(*args, **kwargs): # real signature unknown
    pass

def keymap_get_default(*args, **kwargs): # real signature unknown
    pass

def keymap_get_for_display(*args, **kwargs): # real signature unknown
    pass

def keyval_convert_case(*args, **kwargs): # real signature unknown
    pass

def keyval_from_name(*args, **kwargs): # real signature unknown
    pass

def keyval_is_lower(*args, **kwargs): # real signature unknown
    pass

def keyval_is_upper(*args, **kwargs): # real signature unknown
    pass

def keyval_name(*args, **kwargs): # real signature unknown
    pass

def keyval_to_lower(*args, **kwargs): # real signature unknown
    pass

def keyval_to_unicode(*args, **kwargs): # real signature unknown
    pass

def keyval_to_upper(*args, **kwargs): # real signature unknown
    pass

def list_visuals(*args, **kwargs): # real signature unknown
    pass

def net_wm_supports(*args, **kwargs): # real signature unknown
    pass

def notify_startup_complete(*args, **kwargs): # real signature unknown
    pass

def notify_startup_complete_with_id(*args, **kwargs): # real signature unknown
    pass

def offscreen_window_get_embedder(*args, **kwargs): # real signature unknown
    pass

def offscreen_window_get_pixmap(*args, **kwargs): # real signature unknown
    pass

def offscreen_window_set_embedder(*args, **kwargs): # real signature unknown
    pass

def pango_context_get(*args, **kwargs): # real signature unknown
    pass

def pango_context_get_for_screen(*args, **kwargs): # real signature unknown
    pass

def pango_context_set_colormap(*args, **kwargs): # real signature unknown
    pass

def pango_renderer_get_default(*args, **kwargs): # real signature unknown
    pass

def pixbuf_get_file_info(*args, **kwargs): # real signature unknown
    pass

def pixbuf_get_formats(*args, **kwargs): # real signature unknown
    pass

def pixbuf_get_from_drawable(*args, **kwargs): # real signature unknown
    pass

def pixbuf_loader_new(*args, **kwargs): # real signature unknown
    pass

def pixbuf_loader_new_with_mime_type(*args, **kwargs): # real signature unknown
    pass

def pixbuf_new_from_array(*args, **kwargs): # real signature unknown
    pass

def pixbuf_new_from_data(*args, **kwargs): # real signature unknown
    pass

def pixbuf_new_from_file(*args, **kwargs): # real signature unknown
    pass

def pixbuf_new_from_file_at_scale(*args, **kwargs): # real signature unknown
    pass

def pixbuf_new_from_file_at_size(*args, **kwargs): # real signature unknown
    pass

def pixbuf_new_from_inline(*args, **kwargs): # real signature unknown
    pass

def pixbuf_new_from_stream(*args, **kwargs): # real signature unknown
    pass

def pixbuf_new_from_stream_at_scale(*args, **kwargs): # real signature unknown
    pass

def pixbuf_new_from_xpm_data(*args, **kwargs): # real signature unknown
    pass

def pixmap_colormap_create_from_xpm(*args, **kwargs): # real signature unknown
    pass

def pixmap_colormap_create_from_xpm_d(*args, **kwargs): # real signature unknown
    pass

def pixmap_create_from_data(*args, **kwargs): # real signature unknown
    pass

def pixmap_create_from_xpm(*args, **kwargs): # real signature unknown
    pass

def pixmap_create_from_xpm_d(*args, **kwargs): # real signature unknown
    pass

def pixmap_foreign_new(*args, **kwargs): # real signature unknown
    pass

def pixmap_foreign_new_for_display(*args, **kwargs): # real signature unknown
    pass

def pixmap_foreign_new_for_screen(*args, **kwargs): # real signature unknown
    pass

def pixmap_lookup(*args, **kwargs): # real signature unknown
    pass

def pixmap_lookup_for_display(*args, **kwargs): # real signature unknown
    pass

def pointer_grab(*args, **kwargs): # real signature unknown
    pass

def pointer_is_grabbed(*args, **kwargs): # real signature unknown
    pass

def pointer_ungrab(*args, **kwargs): # real signature unknown
    pass

def query_depths(*args, **kwargs): # real signature unknown
    pass

def query_visual_types(*args, **kwargs): # real signature unknown
    pass

def region_rectangle(*args, **kwargs): # real signature unknown
    pass

def rgb_colormap_ditherable(*args, **kwargs): # real signature unknown
    pass

def rgb_ditherable(*args, **kwargs): # real signature unknown
    pass

def rgb_find_color(*args, **kwargs): # real signature unknown
    pass

def rgb_gc_set_background(*args, **kwargs): # real signature unknown
    pass

def rgb_gc_set_foreground(*args, **kwargs): # real signature unknown
    pass

def rgb_get_cmap(*args, **kwargs): # real signature unknown
    pass

def rgb_get_colormap(*args, **kwargs): # real signature unknown
    pass

def rgb_get_visual(*args, **kwargs): # real signature unknown
    pass

def rgb_init(*args, **kwargs): # real signature unknown
    pass

def rgb_set_install(*args, **kwargs): # real signature unknown
    pass

def rgb_set_min_colors(*args, **kwargs): # real signature unknown
    pass

def rgb_set_verbose(*args, **kwargs): # real signature unknown
    pass

def rgb_xpixel_from_rgb(*args, **kwargs): # real signature unknown
    pass

def screen_get_default(*args, **kwargs): # real signature unknown
    pass

def screen_height(*args, **kwargs): # real signature unknown
    pass

def screen_height_mm(*args, **kwargs): # real signature unknown
    pass

def screen_width(*args, **kwargs): # real signature unknown
    pass

def screen_width_mm(*args, **kwargs): # real signature unknown
    pass

def selection_owner_get(*args, **kwargs): # real signature unknown
    pass

def selection_owner_get_for_display(*args, **kwargs): # real signature unknown
    pass

def selection_owner_set(*args, **kwargs): # real signature unknown
    pass

def selection_owner_set_for_display(*args, **kwargs): # real signature unknown
    pass

def selection_send_notify(*args, **kwargs): # real signature unknown
    pass

def selection_send_notify_for_display(*args, **kwargs): # real signature unknown
    pass

def set_double_click_time(*args, **kwargs): # real signature unknown
    pass

def set_locale(*args, **kwargs): # real signature unknown
    pass

def set_program_class(*args, **kwargs): # real signature unknown
    pass

def set_show_events(*args, **kwargs): # real signature unknown
    pass

def set_sm_client_id(*args, **kwargs): # real signature unknown
    pass

def set_use_xshm(*args, **kwargs): # real signature unknown
    pass

def synthesize_window_state(*args, **kwargs): # real signature unknown
    pass

def threads_enter(*args, **kwargs): # real signature unknown
    pass

def threads_init(*args, **kwargs): # real signature unknown
    pass

def threads_leave(*args, **kwargs): # real signature unknown
    pass

def unicode_to_keyval(*args, **kwargs): # real signature unknown
    pass

def utf8_to_string_target(*args, **kwargs): # real signature unknown
    pass

def visual_get_best(*args, **kwargs): # real signature unknown
    pass

def visual_get_best_depth(*args, **kwargs): # real signature unknown
    pass

def visual_get_best_type(*args, **kwargs): # real signature unknown
    pass

def visual_get_best_with_depth(*args, **kwargs): # real signature unknown
    pass

def visual_get_best_with_type(*args, **kwargs): # real signature unknown
    pass

def visual_get_system(*args, **kwargs): # real signature unknown
    pass

def window_at_pointer(*args, **kwargs): # real signature unknown
    pass

def window_foreign_new(*args, **kwargs): # real signature unknown
    pass

def window_foreign_new_for_display(*args, **kwargs): # real signature unknown
    pass

def window_get_toplevels(*args, **kwargs): # real signature unknown
    pass

def window_lookup(*args, **kwargs): # real signature unknown
    pass

def window_lookup_for_display(*args, **kwargs): # real signature unknown
    pass

def window_process_all_updates(*args, **kwargs): # real signature unknown
    pass

def x11_display_get_startup_notification_id(*args, **kwargs): # real signature unknown
    pass

def x11_get_default_screen(*args, **kwargs): # real signature unknown
    pass

def x11_get_server_time(*args, **kwargs): # real signature unknown
    pass

def x11_grab_server(*args, **kwargs): # real signature unknown
    pass

def x11_register_standard_event_type(*args, **kwargs): # real signature unknown
    pass

def x11_ungrab_server(*args, **kwargs): # real signature unknown
    pass

# classes

from AppLaunchContext import AppLaunchContext
from AxisUse import AxisUse
from ByteOrder import ByteOrder
from CairoContext import CairoContext
from CapStyle import CapStyle
from Color import Color
from Colormap import Colormap
from Colorspace import Colorspace
from CrossingMode import CrossingMode
from Cursor import Cursor
from CursorType import CursorType
from Device import Device
from Display import Display
from DisplayManager import DisplayManager
from DragAction import DragAction
from DragContext import DragContext
from DragProtocol import DragProtocol
from Drawable import Drawable
from Event import Event
from EventMask import EventMask
from EventType import EventType
from ExtensionMode import ExtensionMode
from Fill import Fill
from FillRule import FillRule
from FilterReturn import FilterReturn
from Font import Font
from FontType import FontType
from Function import Function
from GC import GC
from GCValuesMask import GCValuesMask
from GrabStatus import GrabStatus
from Gravity import Gravity
from Image import Image
from ImageType import ImageType
from InputCondition import InputCondition
from InputMode import InputMode
from InputSource import InputSource
from InterpType import InterpType
from JoinStyle import JoinStyle
from Keymap import Keymap
from LineStyle import LineStyle
from ModifierType import ModifierType
from NotifyType import NotifyType
from OverlapType import OverlapType
from OwnerChange import OwnerChange
from PangoRenderer import PangoRenderer
from Pixbuf import Pixbuf
from PixbufAlphaMode import PixbufAlphaMode
from PixbufAnimation import PixbufAnimation
from PixbufAnimationIter import PixbufAnimationIter
from PixbufError import PixbufError
from PixbufLoader import PixbufLoader
from PixbufRotation import PixbufRotation
from PixbufSimpleAnim import PixbufSimpleAnim
from PixbufSimpleAnimIter import PixbufSimpleAnimIter
from Pixmap import Pixmap
from PropertyState import PropertyState
from PropMode import PropMode
from Rectangle import Rectangle
from Region import Region
from RgbDither import RgbDither
from Screen import Screen
from ScrollDirection import ScrollDirection
from SettingAction import SettingAction
from Status import Status
from SubwindowMode import SubwindowMode
from VisibilityState import VisibilityState
from Visual import Visual
from VisualType import VisualType
from Window import Window
from WindowAttributesType import WindowAttributesType
from WindowClass import WindowClass
from WindowEdge import WindowEdge
from WindowHints import WindowHints
from WindowState import WindowState
from WindowType import WindowType
from WindowTypeHint import WindowTypeHint
from WMDecoration import WMDecoration
from WMFunction import WMFunction
# variables with complex values

lock = None # (!) real value is ''

