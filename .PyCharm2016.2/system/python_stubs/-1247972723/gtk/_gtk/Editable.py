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


class Editable(__gobject.GInterface):
    # no doc
    def copy_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def cut_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def delete_selection(self, *args, **kwargs): # real signature unknown
        pass

    def delete_text(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_delete_text(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_do_delete_text(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_do_insert_text(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_chars(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_position(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_selection_bounds(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_insert_text(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_position(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_selection_bounds(cls, *args, **kwargs): # real signature unknown
        pass

    def get_chars(self, *args, **kwargs): # real signature unknown
        pass

    def get_editable(self, *args, **kwargs): # real signature unknown
        pass

    def get_position(self, *args, **kwargs): # real signature unknown
        pass

    def get_selection_bounds(self, *args, **kwargs): # real signature unknown
        pass

    def insert_text(self, *args, **kwargs): # real signature unknown
        pass

    def paste_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def select_region(self, *args, **kwargs): # real signature unknown
        pass

    def set_editable(self, *args, **kwargs): # real signature unknown
        pass

    def set_position(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


