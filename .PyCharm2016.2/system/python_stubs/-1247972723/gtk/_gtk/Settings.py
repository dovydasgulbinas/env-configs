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


class Settings(__gobject__gobject.GObject):
    """
    Object GtkSettings
    
    Properties from GtkSettings:
      gtk-double-click-time -> gint: Double Click Time
        Maximum time allowed between two clicks for them to be considered a double click (in milliseconds)
      gtk-double-click-distance -> gint: Double Click Distance
        Maximum distance allowed between two clicks for them to be considered a double click (in pixels)
      gtk-cursor-blink -> gboolean: Cursor Blink
        Whether the cursor should blink
      gtk-cursor-blink-time -> gint: Cursor Blink Time
        Length of the cursor blink cycle, in milliseconds
      gtk-cursor-blink-timeout -> gint: Cursor Blink Timeout
        Time after which the cursor stops blinking, in seconds
      gtk-split-cursor -> gboolean: Split Cursor
        Whether two cursors should be displayed for mixed left-to-right and right-to-left text
      gtk-theme-name -> gchararray: Theme Name
        Name of theme RC file to load
      gtk-icon-theme-name -> gchararray: Icon Theme Name
        Name of icon theme to use
      gtk-fallback-icon-theme -> gchararray: Fallback Icon Theme Name
        Name of a icon theme to fall back to
      gtk-key-theme-name -> gchararray: Key Theme Name
        Name of key theme RC file to load
      gtk-menu-bar-accel -> gchararray: Menu bar accelerator
        Keybinding to activate the menu bar
      gtk-dnd-drag-threshold -> gint: Drag threshold
        Number of pixels the cursor can move before dragging
      gtk-font-name -> gchararray: Font Name
        Name of default font to use
      gtk-icon-sizes -> gchararray: Icon Sizes
        List of icon sizes (gtk-menu=16,16:gtk-button=20,20...
      gtk-modules -> gchararray: GTK Modules
        List of currently active GTK modules
      gtk-xft-antialias -> gint: Xft Antialias
        Whether to antialias Xft fonts; 0=no, 1=yes, -1=default
      gtk-xft-hinting -> gint: Xft Hinting
        Whether to hint Xft fonts; 0=no, 1=yes, -1=default
      gtk-xft-hintstyle -> gchararray: Xft Hint Style
        What degree of hinting to use; hintnone, hintslight, hintmedium, or hintfull
      gtk-xft-rgba -> gchararray: Xft RGBA
        Type of subpixel antialiasing; none, rgb, bgr, vrgb, vbgr
      gtk-xft-dpi -> gint: Xft DPI
        Resolution for Xft, in 1024 * dots/inch. -1 to use default value
      gtk-cursor-theme-name -> gchararray: Cursor theme name
        Name of the cursor theme to use, or NULL to use the default theme
      gtk-cursor-theme-size -> gint: Cursor theme size
        Size to use for cursors, or 0 to use the default size
      gtk-alternative-button-order -> gboolean: Alternative button order
        Whether buttons in dialogs should use the alternative button order
      gtk-alternative-sort-arrows -> gboolean: Alternative sort indicator direction
        Whether the direction of the sort indicators in list and tree views is inverted compared to the default (where down means ascending)
      gtk-show-input-method-menu -> gboolean: Show the 'Input Methods' menu
        Whether the context menus of entries and text views should offer to change the input method
      gtk-show-unicode-menu -> gboolean: Show the 'Insert Unicode Control Character' menu
        Whether the context menus of entries and text views should offer to insert control characters
      gtk-timeout-initial -> gint: Start timeout
        Starting value for timeouts, when button is pressed
      gtk-timeout-repeat -> gint: Repeat timeout
        Repeat value for timeouts, when button is pressed
      gtk-timeout-expand -> gint: Expand timeout
        Expand value for timeouts, when a widget is expanding a new region
      gtk-color-scheme -> gchararray: Color scheme
        A palette of named colors for use in themes
      gtk-enable-animations -> gboolean: Enable Animations
        Whether to enable toolkit-wide animations.
      gtk-touchscreen-mode -> gboolean: Enable Touchscreen Mode
        When TRUE, there are no motion notify events delivered on this screen
      gtk-tooltip-timeout -> gint: Tooltip timeout
        Timeout before tooltip is shown
      gtk-tooltip-browse-timeout -> gint: Tooltip browse timeout
        Timeout before tooltip is shown when browse mode is enabled
      gtk-tooltip-browse-mode-timeout -> gint: Tooltip browse mode timeout
        Timeout after which browse mode is disabled
      gtk-keynav-cursor-only -> gboolean: Keynav Cursor Only
        When TRUE, there are only cursor keys available to navigate widgets
      gtk-keynav-wrap-around -> gboolean: Keynav Wrap Around
        Whether to wrap around when keyboard-navigating widgets
      gtk-error-bell -> gboolean: Error Bell
        When TRUE, keyboard navigation and other errors will cause a beep
      color-hash -> GHashTable: Color Hash
        A hash table representation of the color scheme.
      gtk-file-chooser-backend -> gchararray: Default file chooser backend
        Name of the GtkFileChooser backend to use by default
      gtk-print-backends -> gchararray: Default print backend
        List of the GtkPrintBackend backends to use by default
      gtk-print-preview-command -> gchararray: Default command to run when displaying a print preview
        Command to run when displaying a print preview
      gtk-enable-mnemonics -> gboolean: Enable Mnemonics
        Whether labels should have mnemonics
      gtk-enable-accels -> gboolean: Enable Accelerators
        Whether menu items should have accelerators
      gtk-recent-files-limit -> gint: Recent Files Limit
        Number of recently used files
      gtk-im-module -> gchararray: Default IM module
        Which IM module should be used by default
      gtk-recent-files-max-age -> gint: Recent Files Max Age
        Maximum age of recently used files, in days
      gtk-fontconfig-timestamp -> guint: Fontconfig configuration timestamp
        Timestamp of current fontconfig configuration
      gtk-sound-theme-name -> gchararray: Sound Theme Name
        XDG sound theme name
      gtk-enable-input-feedback-sounds -> gboolean: Audible Input Feedback
        Whether to play event sounds as feedback to user input
      gtk-enable-event-sounds -> gboolean: Enable Event Sounds
        Whether to play any event sounds at all
      gtk-enable-tooltips -> gboolean: Enable Tooltips
        Whether tooltips should be shown on widgets
      gtk-toolbar-style -> GtkToolbarStyle: Toolbar style
        Whether default toolbars have text only, text and icons, icons only, etc.
      gtk-toolbar-icon-size -> GtkIconSize: Toolbar Icon Size
        The size of icons in default toolbars.
      gtk-auto-mnemonics -> gboolean: Auto Mnemonics
        Whether mnemonics should be automatically shown and hidden when the user presses the mnemonic activator.
      gtk-primary-button-warps-slider -> gboolean: Primary button warps slider
        Whether a primary click on the trough should warp the slider into position
      gtk-button-images -> gboolean: Show button images
        Whether images should be shown on buttons
      gtk-entry-select-on-focus -> gboolean: Select on focus
        Whether to select the contents of an entry when it is focused
      gtk-entry-password-hint-timeout -> guint: Password Hint Timeout
        How long to show the last input character in hidden entries
      gtk-menu-images -> gboolean: Show menu images
        Whether images should be shown in menus
      gtk-menu-bar-popup-delay -> gint: Delay before drop down menus appear
        Delay before the submenus of a menu bar appear
      gtk-scrolled-window-placement -> GtkCornerType: Scrolled Window Placement
        Where the contents of scrolled windows are located with respect to the scrollbars, if not overridden by the scrolled window's own placement.
      gtk-can-change-accels -> gboolean: Can change accelerators
        Whether menu accelerators can be changed by pressing a key over the menu item
      gtk-menu-popup-delay -> gint: Delay before submenus appear
        Minimum time the pointer must stay over a menu item before the submenu appear
      gtk-menu-popdown-delay -> gint: Delay before hiding a submenu
        The time before hiding a submenu when the pointer is moving towards the submenu
      gtk-label-select-on-focus -> gboolean: Select on focus
        Whether to select the contents of a selectable label when it is focused
      gtk-color-palette -> gchararray: Custom palette
        Palette to use in the color selector
      gtk-im-preedit-style -> GtkIMPreeditStyle: IM Preedit style
        How to draw the input method preedit string
      gtk-im-status-style -> GtkIMStatusStyle: IM Status style
        How to draw the input method statusbar
      gtk-shell-shows-menubar -> gboolean: Desktop shell shows the menubar
        Set to TRUE if the desktop environment is displaying the menubar, FALSE if the app should display it itself.
    
    Signals from GObject:
      notify (GParam)
    """
    def set_double_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_long_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_string_property(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


