# encoding: utf-8
# module pango
# from /usr/lib/python2.7/dist-packages/gtk-2.0/pango.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject


# Variables with simple values

ALIGN_CENTER = 1
ALIGN_LEFT = 0
ALIGN_RIGHT = 2

ATTR_ABSOLUTE_SIZE = 20

ATTR_BACKGROUND = 10

ATTR_BACKGROUND_ALPHA = 25

ATTR_FALLBACK = 16
ATTR_FAMILY = 2

ATTR_FONT_DESC = 8
ATTR_FONT_FEATURES = 23

ATTR_FOREGROUND = 9

ATTR_FOREGROUND_ALPHA = 24

ATTR_GRAVITY = 21

ATTR_GRAVITY_HINT = 22

ATTR_INVALID = 0
ATTR_LANGUAGE = 1

ATTR_LETTER_SPACING = 17

ATTR_RISE = 13
ATTR_SCALE = 15
ATTR_SHAPE = 14
ATTR_SIZE = 7
ATTR_STRETCH = 6
ATTR_STRIKETHROUGH = 12

ATTR_STRIKETHROUGH_COLOR = 19

ATTR_STYLE = 3
ATTR_UNDERLINE = 11

ATTR_UNDERLINE_COLOR = 18

ATTR_VARIANT = 5
ATTR_WEIGHT = 4

COVERAGE_APPROXIMATE = 2
COVERAGE_EXACT = 3
COVERAGE_FALLBACK = 1
COVERAGE_NONE = 0

DIRECTION_LTR = 0
DIRECTION_NEUTRAL = 6
DIRECTION_RTL = 1

DIRECTION_TTB_LTR = 2
DIRECTION_TTB_RTL = 3

DIRECTION_WEAK_LTR = 4
DIRECTION_WEAK_RTL = 5

ELLIPSIZE_END = 3
ELLIPSIZE_MIDDLE = 2
ELLIPSIZE_NONE = 0
ELLIPSIZE_START = 1

FONT_MASK_FAMILY = 1
FONT_MASK_GRAVITY = 64
FONT_MASK_SIZE = 32
FONT_MASK_STRETCH = 16
FONT_MASK_STYLE = 2
FONT_MASK_VARIANT = 4
FONT_MASK_WEIGHT = 8

GRAVITY_AUTO = 4
GRAVITY_EAST = 1

GRAVITY_HINT_LINE = 2
GRAVITY_HINT_NATURAL = 0
GRAVITY_HINT_STRONG = 1

GRAVITY_NORTH = 2
GRAVITY_SOUTH = 0
GRAVITY_WEST = 3

RENDER_PART_BACKGROUND = 1
RENDER_PART_FOREGROUND = 0
RENDER_PART_STRIKETHROUGH = 3
RENDER_PART_UNDERLINE = 2

SCALE = 1024

SCALE_LARGE = 1.2
SCALE_MEDIUM = 1.0
SCALE_SMALL = 0.8333333333333

SCALE_XX_LARGE = 1.728
SCALE_XX_SMALL = 0.5787037037037

SCALE_X_LARGE = 1.4399999999999
SCALE_X_SMALL = 0.6444444444444

SCRIPT_ARABIC = 2
SCRIPT_ARMENIAN = 3
SCRIPT_BALINESE = 62
SCRIPT_BATAK = 78
SCRIPT_BENGALI = 4
SCRIPT_BOPOMOFO = 5
SCRIPT_BRAHMI = 79
SCRIPT_BRAILLE = 46
SCRIPT_BUGINESE = 55
SCRIPT_BUHID = 44

SCRIPT_CANADIAN_ABORIGINAL = 40

SCRIPT_CARIAN = 75
SCRIPT_CHAKMA = 81
SCRIPT_CHAM = 72
SCRIPT_CHEROKEE = 6
SCRIPT_COMMON = 0
SCRIPT_COPTIC = 7
SCRIPT_CUNEIFORM = 63
SCRIPT_CYPRIOT = 47
SCRIPT_CYRILLIC = 8
SCRIPT_DESERET = 9
SCRIPT_DEVANAGARI = 10
SCRIPT_ETHIOPIC = 11
SCRIPT_GEORGIAN = 12
SCRIPT_GLAGOLITIC = 56
SCRIPT_GOTHIC = 13
SCRIPT_GREEK = 14
SCRIPT_GUJARATI = 15
SCRIPT_GURMUKHI = 16
SCRIPT_HAN = 17
SCRIPT_HANGUL = 18
SCRIPT_HANUNOO = 43
SCRIPT_HEBREW = 19
SCRIPT_HIRAGANA = 20
SCRIPT_INHERITED = 1

SCRIPT_INVALID_CODE = -1

SCRIPT_KANNADA = 21
SCRIPT_KATAKANA = 22

SCRIPT_KAYAH_LI = 67

SCRIPT_KHAROSHTHI = 60
SCRIPT_KHMER = 23
SCRIPT_LAO = 24
SCRIPT_LATIN = 25
SCRIPT_LEPCHA = 68
SCRIPT_LIMBU = 48

SCRIPT_LINEAR_B = 51

SCRIPT_LYCIAN = 76
SCRIPT_LYDIAN = 77
SCRIPT_MALAYALAM = 26
SCRIPT_MANDAIC = 80

SCRIPT_MEROITIC_CURSIVE = 82
SCRIPT_MEROITIC_HIEROGLYPHS = 83

SCRIPT_MIAO = 84
SCRIPT_MONGOLIAN = 27
SCRIPT_MYANMAR = 28

SCRIPT_NEW_TAI_LUE = 54

SCRIPT_NKO = 66
SCRIPT_OGHAM = 29

SCRIPT_OLD_ITALIC = 30
SCRIPT_OLD_PERSIAN = 59

SCRIPT_OL_CHIKI = 73

SCRIPT_ORIYA = 31
SCRIPT_OSMANYA = 49

SCRIPT_PHAGS_PA = 65

SCRIPT_PHOENICIAN = 64
SCRIPT_REJANG = 69
SCRIPT_RUNIC = 32
SCRIPT_SAURASHTRA = 71
SCRIPT_SHARADA = 85
SCRIPT_SHAVIAN = 50
SCRIPT_SINHALA = 33

SCRIPT_SORA_SOMPENG = 86

SCRIPT_SUNDANESE = 70

SCRIPT_SYLOTI_NAGRI = 58

SCRIPT_SYRIAC = 34
SCRIPT_TAGALOG = 42
SCRIPT_TAGBANWA = 45

SCRIPT_TAI_LE = 52

SCRIPT_TAKRI = 87
SCRIPT_TAMIL = 35
SCRIPT_TELUGU = 36
SCRIPT_THAANA = 37
SCRIPT_THAI = 38
SCRIPT_TIBETAN = 39
SCRIPT_TIFINAGH = 57
SCRIPT_UGARITIC = 53
SCRIPT_UNKNOWN = 61
SCRIPT_VAI = 74
SCRIPT_YI = 41

STRETCH_CONDENSED = 2
STRETCH_EXPANDED = 6

STRETCH_EXTRA_CONDENSED = 1
STRETCH_EXTRA_EXPANDED = 7

STRETCH_NORMAL = 4

STRETCH_SEMI_CONDENSED = 3
STRETCH_SEMI_EXPANDED = 5

STRETCH_ULTRA_CONDENSED = 0
STRETCH_ULTRA_EXPANDED = 8

STYLE_ITALIC = 2
STYLE_NORMAL = 0
STYLE_OBLIQUE = 1

TAB_LEFT = 0

UNDERLINE_DOUBLE = 2
UNDERLINE_ERROR = 4
UNDERLINE_LOW = 3
UNDERLINE_NONE = 0
UNDERLINE_SINGLE = 1

VARIANT_NORMAL = 0

VARIANT_SMALL_CAPS = 1

WEIGHT_BOLD = 700
WEIGHT_BOOK = 380
WEIGHT_HEAVY = 900
WEIGHT_LIGHT = 300
WEIGHT_MEDIUM = 500
WEIGHT_NORMAL = 400
WEIGHT_SEMIBOLD = 600
WEIGHT_SEMILIGHT = 350
WEIGHT_THIN = 100
WEIGHT_ULTRABOLD = 800
WEIGHT_ULTRAHEAVY = 1000
WEIGHT_ULTRALIGHT = 200

WRAP_CHAR = 1
WRAP_WORD = 0

WRAP_WORD_CHAR = 2

# functions

def ASCENT(*args, **kwargs): # real signature unknown
    pass

def AttrBackground(*args, **kwargs): # real signature unknown
    pass

def AttrFallback(*args, **kwargs): # real signature unknown
    pass

def AttrFamily(*args, **kwargs): # real signature unknown
    pass

def AttrFontDesc(*args, **kwargs): # real signature unknown
    pass

def AttrForeground(*args, **kwargs): # real signature unknown
    pass

def AttrLanguage(*args, **kwargs): # real signature unknown
    pass

def AttrLetterSpacing(*args, **kwargs): # real signature unknown
    pass

def AttrRise(*args, **kwargs): # real signature unknown
    pass

def AttrScale(*args, **kwargs): # real signature unknown
    pass

def AttrShape(*args, **kwargs): # real signature unknown
    pass

def AttrSize(*args, **kwargs): # real signature unknown
    pass

def AttrSizeAbsolute(*args, **kwargs): # real signature unknown
    pass

def AttrStretch(*args, **kwargs): # real signature unknown
    pass

def AttrStrikethrough(*args, **kwargs): # real signature unknown
    pass

def AttrStrikethroughColor(*args, **kwargs): # real signature unknown
    pass

def AttrStyle(*args, **kwargs): # real signature unknown
    pass

def AttrUnderline(*args, **kwargs): # real signature unknown
    pass

def AttrUnderlineColor(*args, **kwargs): # real signature unknown
    pass

def AttrVariant(*args, **kwargs): # real signature unknown
    pass

def AttrWeight(*args, **kwargs): # real signature unknown
    pass

def DESCENT(*args, **kwargs): # real signature unknown
    pass

def find_base_dir(*args, **kwargs): # real signature unknown
    pass

def get_sample_language(*args, **kwargs): # real signature unknown
    pass

def gravity_get_for_matrix(*args, **kwargs): # real signature unknown
    pass

def gravity_get_for_script(*args, **kwargs): # real signature unknown
    pass

def gravity_to_rotation(*args, **kwargs): # real signature unknown
    pass

def LBEARING(*args, **kwargs): # real signature unknown
    pass

def pango_attr_type_register(*args, **kwargs): # real signature unknown
    pass

def pango_language_from_string(*args, **kwargs): # real signature unknown
    pass

def pango_language_matches(*args, **kwargs): # real signature unknown
    pass

def parse_markup(*args, **kwargs): # real signature unknown
    pass

def PIXELS(*args, **kwargs): # real signature unknown
    pass

def RBEARING(*args, **kwargs): # real signature unknown
    pass

def script_for_unichar(*args, **kwargs): # real signature unknown
    pass

def unichar_direction(*args, **kwargs): # real signature unknown
    pass

def units_from_double(*args, **kwargs): # real signature unknown
    pass

def units_to_double(*args, **kwargs): # real signature unknown
    pass

def version(*args, **kwargs): # real signature unknown
    pass

def version_check(*args, **kwargs): # real signature unknown
    pass

def version_string(*args, **kwargs): # real signature unknown
    pass

# classes

from Alignment import Alignment
from AttrList import AttrList
from AttrType import AttrType
from Color import Color
from Context import Context
from CoverageLevel import CoverageLevel
from Direction import Direction
from EllipsizeMode import EllipsizeMode
from Engine import Engine
from EngineLang import EngineLang
from EngineShape import EngineShape
from Font import Font
from FontDescription import FontDescription
from FontFace import FontFace
from FontFamily import FontFamily
from FontMap import FontMap
from FontMask import FontMask
from FontMetrics import FontMetrics
from Fontset import Fontset
from FontsetSimple import FontsetSimple
from GlyphString import GlyphString
from Gravity import Gravity
from GravityHint import GravityHint
from Item import Item
from Language import Language
from Layout import Layout
from LayoutIter import LayoutIter
from LayoutLine import LayoutLine
from Matrix import Matrix
from Renderer import Renderer
from RenderPart import RenderPart
from Script import Script
from Stretch import Stretch
from Style import Style
from TabAlign import TabAlign
from TabArray import TabArray
from Underline import Underline
from Variant import Variant
from Warning import Warning
from Weight import Weight
from WrapMode import WrapMode
