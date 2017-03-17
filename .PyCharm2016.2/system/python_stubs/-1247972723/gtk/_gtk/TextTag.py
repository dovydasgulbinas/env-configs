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


class TextTag(__gobject__gobject.GObject):
    """
    Object GtkTextTag
    
    Signals from GtkTextTag:
      event (GObject, GdkEvent, GtkTextIter) -> gboolean
    
    Properties from GtkTextTag:
      name -> gchararray: Tag name
        Name used to refer to the text tag. NULL for anonymous tags
      background -> gchararray: Background color name
        Background color as a string
      foreground -> gchararray: Foreground color name
        Foreground color as a string
      background-gdk -> GdkColor: Background color
        Background color as a (possibly unallocated) GdkColor
      foreground-gdk -> GdkColor: Foreground color
        Foreground color as a (possibly unallocated) GdkColor
      background-stipple -> GdkPixmap: Background stipple mask
        Bitmap to use as a mask when drawing the text background
      foreground-stipple -> GdkPixmap: Foreground stipple mask
        Bitmap to use as a mask when drawing the text foreground
      font -> gchararray: Font
        Font description as a string, e.g. "Sans Italic 12"
      font-desc -> PangoFontDescription: Font
        Font description as a PangoFontDescription struct
      family -> gchararray: Font family
        Name of the font family, e.g. Sans, Helvetica, Times, Monospace
      style -> PangoStyle: Font style
        Font style as a PangoStyle, e.g. PANGO_STYLE_ITALIC
      variant -> PangoVariant: Font variant
        Font variant as a PangoVariant, e.g. PANGO_VARIANT_SMALL_CAPS
      weight -> gint: Font weight
        Font weight as an integer, see predefined values in PangoWeight; for example, PANGO_WEIGHT_BOLD
      stretch -> PangoStretch: Font stretch
        Font stretch as a PangoStretch, e.g. PANGO_STRETCH_CONDENSED
      size -> gint: Font size
        Font size in Pango units
      size-points -> gdouble: Font points
        Font size in points
      scale -> gdouble: Font scale
        Font size as a scale factor relative to the default font size. This properly adapts to theme changes etc. so is recommended. Pango predefines some scales such as PANGO_SCALE_X_LARGE
      pixels-above-lines -> gint: Pixels above lines
        Pixels of blank space above paragraphs
      pixels-below-lines -> gint: Pixels below lines
        Pixels of blank space below paragraphs
      pixels-inside-wrap -> gint: Pixels inside wrap
        Pixels of blank space between wrapped lines in a paragraph
      editable -> gboolean: Editable
        Whether the text can be modified by the user
      wrap-mode -> GtkWrapMode: Wrap mode
        Whether to wrap lines never, at word boundaries, or at character boundaries
      justification -> GtkJustification: Justification
        Left, right, or center justification
      direction -> GtkTextDirection: Text direction
        Text direction, e.g. right-to-left or left-to-right
      left-margin -> gint: Left margin
        Width of the left margin in pixels
      indent -> gint: Indent
        Amount to indent the paragraph, in pixels
      strikethrough -> gboolean: Strikethrough
        Whether to strike through the text
      right-margin -> gint: Right margin
        Width of the right margin in pixels
      underline -> PangoUnderline: Underline
        Style of underline for this text
      rise -> gint: Rise
        Offset of text above the baseline (below the baseline if rise is negative) in Pango units
      background-full-height -> gboolean: Background full height
        Whether the background color fills the entire line height or only the height of the tagged characters
      language -> gchararray: Language
        The language this text is in, as an ISO code. Pango can use this as a hint when rendering the text. If not set, an appropriate default will be used.
      tabs -> PangoTabArray: Tabs
        Custom tabs for this text
      invisible -> gboolean: Invisible
        Whether this text is hidden.
      paragraph-background -> gchararray: Paragraph background color name
        Paragraph background color as a string
      paragraph-background-gdk -> GdkColor: Paragraph background color
        Paragraph background color as a (possibly unallocated) GdkColor
      accumulative-margin -> gboolean: Margin Accumulates
        Whether left and right margins accumulate.
      background-set -> gboolean: Background set
        Whether this tag affects the background color
      foreground-set -> gboolean: Foreground set
        Whether this tag affects the foreground color
      background-stipple-set -> gboolean: Background stipple set
        Whether this tag affects the background stipple
      foreground-stipple-set -> gboolean: Foreground stipple set
        Whether this tag affects the foreground stipple
      family-set -> gboolean: Font family set
        Whether this tag affects the font family
      style-set -> gboolean: Font style set
        Whether this tag affects the font style
      variant-set -> gboolean: Font variant set
        Whether this tag affects the font variant
      weight-set -> gboolean: Font weight set
        Whether this tag affects the font weight
      stretch-set -> gboolean: Font stretch set
        Whether this tag affects the font stretch
      size-set -> gboolean: Font size set
        Whether this tag affects the font size
      scale-set -> gboolean: Font scale set
        Whether this tag scales the font size by a factor
      pixels-above-lines-set -> gboolean: Pixels above lines set
        Whether this tag affects the number of pixels above lines
      pixels-below-lines-set -> gboolean: Pixels below lines set
        Whether this tag affects the number of pixels above lines
      pixels-inside-wrap-set -> gboolean: Pixels inside wrap set
        Whether this tag affects the number of pixels between wrapped lines
      editable-set -> gboolean: Editability set
        Whether this tag affects text editability
      wrap-mode-set -> gboolean: Wrap mode set
        Whether this tag affects line wrap mode
      justification-set -> gboolean: Justification set
        Whether this tag affects paragraph justification
      left-margin-set -> gboolean: Left margin set
        Whether this tag affects the left margin
      indent-set -> gboolean: Indent set
        Whether this tag affects indentation
      strikethrough-set -> gboolean: Strikethrough set
        Whether this tag affects strikethrough
      right-margin-set -> gboolean: Right margin set
        Whether this tag affects the right margin
      underline-set -> gboolean: Underline set
        Whether this tag affects underlining
      rise-set -> gboolean: Rise set
        Whether this tag affects the rise
      background-full-height-set -> gboolean: Background full height set
        Whether this tag affects background height
      language-set -> gboolean: Language set
        Whether this tag affects the language the text is rendered as
      tabs-set -> gboolean: Tabs set
        Whether this tag affects tabs
      invisible-set -> gboolean: Invisible set
        Whether this tag affects text visibility
      paragraph-background-set -> gboolean: Paragraph background set
        Whether this tag affects the paragraph background color
    
    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def do_event(cls, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def get_priority(self, *args, **kwargs): # real signature unknown
        pass

    def set_priority(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


