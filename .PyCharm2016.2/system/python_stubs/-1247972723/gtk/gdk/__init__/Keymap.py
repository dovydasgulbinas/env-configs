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


class Keymap(__gobject__gobject.GObject):
    """
    Object GdkKeymap
    
    Signals from GdkKeymap:
      state-changed ()
      direction-changed ()
      keys-changed ()
    
    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def do_direction_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_keys_changed(cls, *args, **kwargs): # real signature unknown
        pass

    def get_caps_lock_state(self, *args, **kwargs): # real signature unknown
        pass

    def get_direction(self, *args, **kwargs): # real signature unknown
        pass

    def get_entries_for_keycode(self, *args, **kwargs): # real signature unknown
        pass

    def get_entries_for_keyval(self, *args, **kwargs): # real signature unknown
        pass

    def have_bidi_layouts(self, *args, **kwargs): # real signature unknown
        pass

    def lookup_key(self, *args, **kwargs): # real signature unknown
        pass

    def translate_keyboard_state(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


