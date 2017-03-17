# encoding: utf-8
# module pynotify._pynotify
# from /usr/lib/python2.7/dist-packages/gtk-2.0/pynotify/_pynotify.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject


# Variables with simple values

EXPIRES_DEFAULT = -1
EXPIRES_NEVER = 0

URGENCY_CRITICAL = 2
URGENCY_LOW = 0
URGENCY_NORMAL = 1

# functions

def get_app_name(*args, **kwargs): # real signature unknown
    pass

def get_server_caps(*args, **kwargs): # real signature unknown
    pass

def get_server_info(*args, **kwargs): # real signature unknown
    pass

def init(*args, **kwargs): # real signature unknown
    pass

def is_initted(*args, **kwargs): # real signature unknown
    pass

def uninit(*args, **kwargs): # real signature unknown
    pass

# classes

class Notification(__gobject__gobject.GObject):
    """
    Object NotifyNotification
    
    Signals from NotifyNotification:
      closed ()
    
    Properties from NotifyNotification:
      id -> gint: ID
        The notification ID
      app-name -> gchararray: Application name
        The application name to use for this notification
      summary -> gchararray: Summary
        The summary text
      body -> gchararray: Message Body
        The message body text
      icon-name -> gchararray: Icon Name
        The icon filename or icon theme-compliant name
      closed-reason -> gint: Closed Reason
        The reason code for why the notification was closed
    
    Signals from GObject:
      notify (GParam)
    """
    def add_action(self, *args, **kwargs): # real signature unknown
        pass

    def clear_actions(self, *args, **kwargs): # real signature unknown
        pass

    def clear_hints(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def set_category(self, *args, **kwargs): # real signature unknown
        pass

    def set_hint(self, *args, **kwargs): # real signature unknown
        pass

    def set_hint_byte(self, *args, **kwargs): # real signature unknown
        pass

    def set_hint_byte_array(self, *args, **kwargs): # real signature unknown
        pass

    def set_hint_double(self, *args, **kwargs): # real signature unknown
        pass

    def set_hint_int32(self, *args, **kwargs): # real signature unknown
        pass

    def set_hint_string(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_from_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def set_timeout(self, *args, **kwargs): # real signature unknown
        pass

    def set_urgency(self, *args, **kwargs): # real signature unknown
        pass

    def show(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Urgency(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is ''


