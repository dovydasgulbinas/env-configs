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


from IMContext import IMContext

class IMContextSimple(IMContext):
    """
    Object GtkIMContextSimple
    
    Signals from GtkIMContext:
      preedit-changed ()
      preedit-start ()
      preedit-end ()
      commit (gchararray)
      retrieve-surrounding () -> gboolean
      delete-surrounding (gint, gint) -> gboolean
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


