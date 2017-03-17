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


from CellRendererText import CellRendererText

class CellRendererAccel(CellRendererText):
    """
    Object GtkCellRendererAccel
    
    Signals from GtkCellRendererAccel:
      accel-edited (gchararray, guint, GdkModifierType, guint)
      accel-cleared (gchararray)
    
    Properties from GtkCellRendererAccel:
      accel-key -> guint: Accelerator key
        The keyval of the accelerator
      accel-mods -> GdkModifierType: Accelerator modifiers
        The modifier mask of the accelerator
      keycode -> guint: Accelerator keycode
        The hardware keycode of the accelerator
      accel-mode -> GtkCellRendererAccelMode: Accelerator Mode
        The type of accelerators
    
    Signals from GtkCellRendererText:
      edited (gchararray, gchararray)
    
    Properties from GtkCellRendererText:
      text -> gchararray: Text
        Text to render
      markup -> gchararray: Markup
        Marked up text to render
      attributes -> PangoAttrList: Attributes
        A list of style attributes to apply to the text of the renderer
      single-paragraph-mode -> gboolean: Single Paragraph Mode
        Whether or not to keep all text in a single paragraph
      width-chars -> gint: Width In Characters
        The desired width of the label, in characters
      wrap-width -> gint: Wrap width
        The width at which the text is wrapped
      alignment -> PangoAlignment: Alignment
        How to align the lines
      background -> gchararray: Background color name
        Background color as a string
      foreground -> gchararray: Foreground color name
        Foreground color as a string
      background-gdk -> GdkColor: Background color
        Background color as a GdkColor
      foreground-gdk -> GdkColor: Foreground color
        Foreground color as a GdkColor
      font -> gchararray: Font
        Font description as a string, e.g. "Sans Italic 12"
      font-desc -> PangoFontDescription: Font
        Font description as a PangoFontDescription struct
      family -> gchararray: Font family
        Name of the font family, e.g. Sans, Helvetica, Times, Monospace
      style -> PangoStyle: Font style
        Font style
      variant -> PangoVariant: Font variant
        Font variant
      weight -> gint: Font weight
        Font weight
      stretch -> PangoStretch: Font stretch
        Font stretch
      size -> gint: Font size
        Font size
      size-points -> gdouble: Font points
        Font size in points
      scale -> gdouble: Font scale
        Font scaling factor
      editable -> gboolean: Editable
        Whether the text can be modified by the user
      strikethrough -> gboolean: Strikethrough
        Whether to strike through the text
      underline -> PangoUnderline: Underline
        Style of underline for this text
      rise -> gint: Rise
        Offset of text above the baseline (below the baseline if rise is negative)
      language -> gchararray: Language
        The language this text is in, as an ISO code. Pango can use this as a hint when rendering the text. If you don't understand this parameter, you probably don't need it
      ellipsize -> PangoEllipsizeMode: Ellipsize
        The preferred place to ellipsize the string, if the cell renderer does not have enough room to display the entire string
      wrap-mode -> PangoWrapMode: Wrap mode
        How to break the string into multiple lines, if the cell renderer does not have enough room to display the entire string
      background-set -> gboolean: Background set
        Whether this tag affects the background color
      foreground-set -> gboolean: Foreground set
        Whether this tag affects the foreground color
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
      editable-set -> gboolean: Editability set
        Whether this tag affects text editability
      strikethrough-set -> gboolean: Strikethrough set
        Whether this tag affects strikethrough
      underline-set -> gboolean: Underline set
        Whether this tag affects underlining
      rise-set -> gboolean: Rise set
        Whether this tag affects the rise
      language-set -> gboolean: Language set
        Whether this tag affects the language the text is rendered as
      ellipsize-set -> gboolean: Ellipsize set
        Whether this tag affects the ellipsize mode
      align-set -> gboolean: Align set
        Whether this tag affects the alignment mode
    
    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)
    
    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
        Editable mode of the CellRenderer
      visible -> gboolean: visible
        Display the cell
      sensitive -> gboolean: Sensitive
        Display the cell sensitive
      xalign -> gfloat: xalign
        The x-align
      yalign -> gfloat: yalign
        The y-align
      xpad -> guint: xpad
        The xpad
      ypad -> guint: ypad
        The ypad
      width -> gint: width
        The fixed width
      height -> gint: height
        The fixed height
      is-expander -> gboolean: Is Expander
        Row has children
      is-expanded -> gboolean: Is Expanded
        Row is an expander row, and is expanded
      cell-background -> gchararray: Cell background color name
        Cell background color as a string
      cell-background-gdk -> GdkColor: Cell background color
        Cell background color as a GdkColor
      cell-background-set -> gboolean: Cell background set
        Whether this tag affects the cell background color
      editing -> gboolean: Editing
        Whether the cell renderer is currently in editing mode
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def do_accel_cleared(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_accel_edited(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


