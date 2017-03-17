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


class Clipboard(__gobject__gobject.GObject):
    """
    Object GtkClipboard
    
    Signals from GtkClipboard:
      owner-change (GdkEvent)
    
    Signals from GObject:
      notify (GParam)
    """
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def get_display(self, *args, **kwargs): # real signature unknown
        pass

    def get_owner(self, *args, **kwargs): # real signature unknown
        pass

    def request_contents(self, *args, **kwargs): # real signature unknown
        pass

    def request_image(self, *args, **kwargs): # real signature unknown
        pass

    def request_rich_text(self, *args, **kwargs): # real signature unknown
        pass

    def request_targets(self, *args, **kwargs): # real signature unknown
        pass

    def request_text(self, *args, **kwargs): # real signature unknown
        pass

    def set_can_store(self, *args, **kwargs): # real signature unknown
        pass

    def set_image(self, *args, **kwargs): # real signature unknown
        pass

    def set_text(self, *args, **kwargs): # real signature unknown
        pass

    def set_with_data(self, *args, **kwargs): # real signature unknown
        pass

    def store(self, *args, **kwargs): # real signature unknown
        pass

    def wait_for_contents(self, *args, **kwargs): # real signature unknown
        pass

    def wait_for_image(self, *args, **kwargs): # real signature unknown
        pass

    def wait_for_rich_text(self, *args, **kwargs): # real signature unknown
        pass

    def wait_for_targets(self, *args, **kwargs): # real signature unknown
        pass

    def wait_for_text(self, *args, **kwargs): # real signature unknown
        pass

    def wait_for_uris(self, *args, **kwargs): # real signature unknown
        pass

    def wait_is_image_available(self, *args, **kwargs): # real signature unknown
        pass

    def wait_is_rich_text_available(self, *args, **kwargs): # real signature unknown
        pass

    def wait_is_target_available(self, *args, **kwargs): # real signature unknown
        pass

    def wait_is_text_available(self, *args, **kwargs): # real signature unknown
        pass

    def wait_is_uris_available(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


