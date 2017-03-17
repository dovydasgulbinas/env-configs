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


from CellLayout import CellLayout

from Buildable import Buildable

class EntryCompletion(__gobject__gobject.GObject, CellLayout, Buildable):
    """
    Object GtkEntryCompletion
    
    Signals from GtkEntryCompletion:
      insert-prefix (gchararray) -> gboolean
      match-selected (GtkTreeModel, GtkTreeIter) -> gboolean
      cursor-on-match (GtkTreeModel, GtkTreeIter) -> gboolean
      action-activated (gint)
    
    Properties from GtkEntryCompletion:
      model -> GtkTreeModel: Completion Model
        The model to find matches in
      minimum-key-length -> gint: Minimum Key Length
        Minimum length of the search key in order to look up matches
      text-column -> gint: Text column
        The column of the model containing the strings.
      inline-completion -> gboolean: Inline completion
        Whether the common prefix should be inserted automatically
      popup-completion -> gboolean: Popup completion
        Whether the completions should be shown in a popup window
      popup-set-width -> gboolean: Popup set width
        If TRUE, the popup window will have the same size as the entry
      popup-single-match -> gboolean: Popup single match
        If TRUE, the popup window will appear for a single match.
      inline-selection -> gboolean: Inline selection
        Your description here
    
    Signals from GObject:
      notify (GParam)
    """
    def complete(self, *args, **kwargs): # real signature unknown
        pass

    def delete_action(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_action_activated(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_insert_prefix(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_match_selected(cls, *args, **kwargs): # real signature unknown
        pass

    def get_completion_prefix(self, *args, **kwargs): # real signature unknown
        pass

    def get_entry(self, *args, **kwargs): # real signature unknown
        pass

    def get_inline_completion(self, *args, **kwargs): # real signature unknown
        pass

    def get_inline_selection(self, *args, **kwargs): # real signature unknown
        pass

    def get_minimum_key_length(self, *args, **kwargs): # real signature unknown
        pass

    def get_model(self, *args, **kwargs): # real signature unknown
        pass

    def get_popup_completion(self, *args, **kwargs): # real signature unknown
        pass

    def get_popup_set_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_popup_single_match(self, *args, **kwargs): # real signature unknown
        pass

    def get_text_column(self, *args, **kwargs): # real signature unknown
        pass

    def insert_action_markup(self, *args, **kwargs): # real signature unknown
        pass

    def insert_action_text(self, *args, **kwargs): # real signature unknown
        pass

    def insert_prefix(self, *args, **kwargs): # real signature unknown
        pass

    def set_inline_completion(self, *args, **kwargs): # real signature unknown
        pass

    def set_inline_selection(self, *args, **kwargs): # real signature unknown
        pass

    def set_match_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_minimum_key_length(self, *args, **kwargs): # real signature unknown
        pass

    def set_model(self, *args, **kwargs): # real signature unknown
        pass

    def set_popup_completion(self, *args, **kwargs): # real signature unknown
        pass

    def set_popup_set_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_popup_single_match(self, *args, **kwargs): # real signature unknown
        pass

    def set_text_column(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


