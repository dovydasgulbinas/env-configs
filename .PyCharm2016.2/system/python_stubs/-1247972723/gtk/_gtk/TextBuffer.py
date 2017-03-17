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


class TextBuffer(__gobject__gobject.GObject):
    """
    Object GtkTextBuffer
    
    Signals from GtkTextBuffer:
      changed ()
      insert-text (GtkTextIter, gchararray, gint)
      insert-pixbuf (GtkTextIter, GdkPixbuf)
      insert-child-anchor (GtkTextIter, GtkTextChildAnchor)
      delete-range (GtkTextIter, GtkTextIter)
      modified-changed ()
      mark-set (GtkTextIter, GtkTextMark)
      mark-deleted (GtkTextMark)
      apply-tag (GtkTextTag, GtkTextIter, GtkTextIter)
      remove-tag (GtkTextTag, GtkTextIter, GtkTextIter)
      begin-user-action ()
      end-user-action ()
      paste-done (GtkClipboard)
    
    Properties from GtkTextBuffer:
      tag-table -> GtkTextTagTable: Tag Table
        Text Tag Table
      text -> gchararray: Text
        Current text of the buffer
      has-selection -> gboolean: Has selection
        Whether the buffer has some text currently selected
      cursor-position -> gint: Cursor position
        The position of the insert mark (as offset from the beginning of the buffer)
      copy-target-list -> GtkTargetList: Copy target list
        The list of targets this buffer supports for clipboard copying and DND source
      paste-target-list -> GtkTargetList: Paste target list
        The list of targets this buffer supports for clipboard pasting and DND destination
    
    Signals from GObject:
      notify (GParam)
    """
    def add_mark(self, *args, **kwargs): # real signature unknown
        pass

    def add_selection_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def apply_tag(self, *args, **kwargs): # real signature unknown
        pass

    def apply_tag_by_name(self, *args, **kwargs): # real signature unknown
        pass

    def backspace(self, *args, **kwargs): # real signature unknown
        pass

    def begin_user_action(self, *args, **kwargs): # real signature unknown
        pass

    def copy_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def create_child_anchor(self, *args, **kwargs): # real signature unknown
        pass

    def create_mark(self, *args, **kwargs): # real signature unknown
        pass

    def create_tag(self, *args, **kwargs): # real signature unknown
        pass

    def cut_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        pass

    def delete_interactive(self, *args, **kwargs): # real signature unknown
        pass

    def delete_mark(self, *args, **kwargs): # real signature unknown
        pass

    def delete_mark_by_name(self, *args, **kwargs): # real signature unknown
        pass

    def delete_selection(self, *args, **kwargs): # real signature unknown
        pass

    def deserialize(self, *args, **kwargs): # real signature unknown
        pass

    def deserialize_get_can_create_tags(self, *args, **kwargs): # real signature unknown
        pass

    def deserialize_set_can_create_tags(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_apply_tag(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_begin_user_action(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_delete_range(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_end_user_action(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_insert_child_anchor(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_insert_pixbuf(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_insert_text(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_mark_deleted(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_mark_set(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_modified_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_remove_tag(cls, *args, **kwargs): # real signature unknown
        pass

    def end_user_action(self, *args, **kwargs): # real signature unknown
        pass

    def get_bounds(self, *args, **kwargs): # real signature unknown
        pass

    def get_char_count(self, *args, **kwargs): # real signature unknown
        pass

    def get_copy_target_list(self, *args, **kwargs): # real signature unknown
        pass

    def get_deserialize_formats(self, *args, **kwargs): # real signature unknown
        pass

    def get_end_iter(self, *args, **kwargs): # real signature unknown
        pass

    def get_has_selection(self, *args, **kwargs): # real signature unknown
        pass

    def get_insert(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_at_child_anchor(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_at_line(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_at_line_index(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_at_line_offset(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_at_mark(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_at_offset(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_count(self, *args, **kwargs): # real signature unknown
        pass

    def get_mark(self, *args, **kwargs): # real signature unknown
        pass

    def get_modified(self, *args, **kwargs): # real signature unknown
        pass

    def get_paste_target_list(self, *args, **kwargs): # real signature unknown
        pass

    def get_selection_bound(self, *args, **kwargs): # real signature unknown
        pass

    def get_selection_bounds(self, *args, **kwargs): # real signature unknown
        pass

    def get_serialize_formats(self, *args, **kwargs): # real signature unknown
        pass

    def get_slice(self, *args, **kwargs): # real signature unknown
        pass

    def get_start_iter(self, *args, **kwargs): # real signature unknown
        pass

    def get_tag_table(self, *args, **kwargs): # real signature unknown
        pass

    def get_text(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def insert_at_cursor(self, *args, **kwargs): # real signature unknown
        pass

    def insert_child_anchor(self, *args, **kwargs): # real signature unknown
        pass

    def insert_interactive(self, *args, **kwargs): # real signature unknown
        pass

    def insert_interactive_at_cursor(self, *args, **kwargs): # real signature unknown
        pass

    def insert_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def insert_range(self, *args, **kwargs): # real signature unknown
        pass

    def insert_range_interactive(self, *args, **kwargs): # real signature unknown
        pass

    def insert_with_tags(self, *args, **kwargs): # real signature unknown
        pass

    def insert_with_tags_by_name(self, *args, **kwargs): # real signature unknown
        pass

    def move_mark(self, *args, **kwargs): # real signature unknown
        pass

    def move_mark_by_name(self, *args, **kwargs): # real signature unknown
        pass

    def paste_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def place_cursor(self, *args, **kwargs): # real signature unknown
        pass

    def register_deserialize_format(self, *args, **kwargs): # real signature unknown
        pass

    def register_deserialize_tagset(self, *args, **kwargs): # real signature unknown
        pass

    def register_serialize_format(self, *args, **kwargs): # real signature unknown
        pass

    def register_serialize_tagset(self, *args, **kwargs): # real signature unknown
        pass

    def remove_all_tags(self, *args, **kwargs): # real signature unknown
        pass

    def remove_selection_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def remove_tag(self, *args, **kwargs): # real signature unknown
        pass

    def remove_tag_by_name(self, *args, **kwargs): # real signature unknown
        pass

    def select_range(self, *args, **kwargs): # real signature unknown
        pass

    def serialize(self, *args, **kwargs): # real signature unknown
        pass

    def set_modified(self, *args, **kwargs): # real signature unknown
        pass

    def set_text(self, *args, **kwargs): # real signature unknown
        pass

    def unregister_deserialize_format(self, *args, **kwargs): # real signature unknown
        pass

    def unregister_serialize_format(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    tag_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


