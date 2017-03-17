# encoding: utf-8
# module gconf
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gconf.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject


# Variables with simple values

CLIENT_HANDLE_ALL = 2
CLIENT_HANDLE_NONE = 0
CLIENT_HANDLE_UNRETURNED = 1

CLIENT_PRELOAD_NONE = 0
CLIENT_PRELOAD_ONELEVEL = 1
CLIENT_PRELOAD_RECURSIVE = 2

ERROR_BAD_ADDRESS = 4
ERROR_BAD_KEY = 5

ERROR_CORRUPT = 7
ERROR_FAILED = 1

ERROR_IN_SHUTDOWN = 16

ERROR_IS_DIR = 9
ERROR_IS_KEY = 10

ERROR_LOCAL_ENGINE = 13

ERROR_LOCK_FAILED = 14

ERROR_NO_PERMISSION = 3
ERROR_NO_SERVER = 2

ERROR_NO_WRITABLE_DATABASE = 15

ERROR_OAF_ERROR = 12

ERROR_OVERRIDDEN = 11

ERROR_PARSE_ERROR = 6

ERROR_SUCCESS = 0

ERROR_TYPE_MISMATCH = 8

UNSET_INCLUDING_SCHEMA_NAMES = 1

VALUE_BOOL = 4
VALUE_FLOAT = 3
VALUE_INT = 2
VALUE_INVALID = 0
VALUE_LIST = 6
VALUE_PAIR = 7
VALUE_SCHEMA = 5
VALUE_STRING = 1

__version__ = '  2.28.1'

# functions

def client_get_default(*args, **kwargs): # real signature unknown
    pass

def client_get_for_engine(*args, **kwargs): # real signature unknown
    pass

def concat_dir_and_key(*args, **kwargs): # real signature unknown
    pass

def debug_shutdown(*args, **kwargs): # real signature unknown
    pass

def engine_get_default(*args, **kwargs): # real signature unknown
    pass

def engine_get_for_address(*args, **kwargs): # real signature unknown
    pass

def entry_new_nocopy(*args, **kwargs): # real signature unknown
    pass

def escape_key(*args, **kwargs): # real signature unknown
    pass

def is_initialized(*args, **kwargs): # real signature unknown
    pass

def key_is_below(*args, **kwargs): # real signature unknown
    pass

def unescape_key(*args, **kwargs): # real signature unknown
    pass

def unique_key(*args, **kwargs): # real signature unknown
    pass

def value_new_from_string(*args, **kwargs): # real signature unknown
    pass

# classes

class ChangeSet(__gobject.GBoxed):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def ref(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def set(self, *args, **kwargs): # real signature unknown
        pass

    def set_bool(self, *args, **kwargs): # real signature unknown
        pass

    def set_float(self, *args, **kwargs): # real signature unknown
        pass

    def set_int(self, *args, **kwargs): # real signature unknown
        pass

    def set_list(self, *args, **kwargs): # real signature unknown
        pass

    def set_nocopy(self, *args, **kwargs): # real signature unknown
        pass

    def set_schema(self, *args, **kwargs): # real signature unknown
        pass

    def set_string(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def unref(self, *args, **kwargs): # real signature unknown
        pass

    def unset(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Client(__gobject__gobject.GObject):
    """
    Object GConfClient
    
    Signals from GConfClient:
      value-changed (gchararray, gpointer)
      unreturned-error (gpointer)
      error (gpointer)
    
    Signals from GObject:
      notify (GParam)
    """
    def add_dir(self, *args, **kwargs): # real signature unknown
        pass

    def all_dirs(self, *args, **kwargs): # real signature unknown
        pass

    def all_entries(self, *args, **kwargs): # real signature unknown
        pass

    def change_set_from_current(self, *args, **kwargs): # real signature unknown
        pass

    def clear_cache(self, *args, **kwargs): # real signature unknown
        pass

    def commit_change_set(self, *args, **kwargs): # real signature unknown
        pass

    def dir_exists(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def get_bool(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_from_schema(self, *args, **kwargs): # real signature unknown
        pass

    def get_entry(self, *args, **kwargs): # real signature unknown
        pass

    def get_float(self, *args, **kwargs): # real signature unknown
        pass

    def get_int(self, *args, **kwargs): # real signature unknown
        pass

    def get_list(self, *args, **kwargs): # real signature unknown
        pass

    def get_pair(self, *args, **kwargs): # real signature unknown
        pass

    def get_schema(self, *args, **kwargs): # real signature unknown
        pass

    def get_string(self, *args, **kwargs): # real signature unknown
        pass

    def get_value(self, *args, **kwargs): # real signature unknown
        pass

    def get_without_default(self, *args, **kwargs): # real signature unknown
        pass

    def key_is_writable(self, *args, **kwargs): # real signature unknown
        pass

    def notify(self, *args, **kwargs): # real signature unknown
        pass

    def notify_add(self, *args, **kwargs): # real signature unknown
        pass

    def notify_remove(self, *args, **kwargs): # real signature unknown
        pass

    def preload(self, *args, **kwargs): # real signature unknown
        pass

    def recursive_unset(self, *args, **kwargs): # real signature unknown
        pass

    def remove_dir(self, *args, **kwargs): # real signature unknown
        pass

    def reverse_change_set(self, *args, **kwargs): # real signature unknown
        pass

    def set(self, *args, **kwargs): # real signature unknown
        pass

    def set_bool(self, *args, **kwargs): # real signature unknown
        pass

    def set_error_handling(self, *args, **kwargs): # real signature unknown
        pass

    def set_float(self, *args, **kwargs): # real signature unknown
        pass

    def set_int(self, *args, **kwargs): # real signature unknown
        pass

    def set_list(self, *args, **kwargs): # real signature unknown
        pass

    def set_pair(self, *args, **kwargs): # real signature unknown
        pass

    def set_schema(self, *args, **kwargs): # real signature unknown
        pass

    def set_string(self, *args, **kwargs): # real signature unknown
        pass

    def set_value(self, *args, **kwargs): # real signature unknown
        pass

    def suggest_sync(self, *args, **kwargs): # real signature unknown
        pass

    def unset(self, *args, **kwargs): # real signature unknown
        pass

    def value_changed(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class ClientErrorHandlingMode(__gobject.GEnum):
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


class ClientPreloadType(__gobject.GEnum):
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


class Engine(object):
    # no doc
    def associate_schema(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Entry(__gobject.GBoxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_default(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_writable(self, *args, **kwargs): # real signature unknown
        pass

    def get_key(self, *args, **kwargs): # real signature unknown
        pass

    def get_schema_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_value(self, *args, **kwargs): # real signature unknown
        pass

    def ref(self, *args, **kwargs): # real signature unknown
        pass

    def set_is_default(self, *args, **kwargs): # real signature unknown
        pass

    def set_is_writable(self, *args, **kwargs): # real signature unknown
        pass

    def set_schema_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_value(self, *args, **kwargs): # real signature unknown
        pass

    def set_value_nocopy(self, *args, **kwargs): # real signature unknown
        pass

    def steal_value(self, *args, **kwargs): # real signature unknown
        pass

    def unref(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


class Error(__gobject.GEnum):
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
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
    }
    __gtype__ = None # (!) real value is ''


class MetaInfo(__gobject.GBoxed):
    # no doc
    def free(self, *args, **kwargs): # real signature unknown
        pass

    def get_mod_user(self, *args, **kwargs): # real signature unknown
        pass

    def get_schema(self, *args, **kwargs): # real signature unknown
        pass

    def mod_time(self, *args, **kwargs): # real signature unknown
        pass

    def set_mod_time(self, *args, **kwargs): # real signature unknown
        pass

    def set_mod_user(self, *args, **kwargs): # real signature unknown
        pass

    def set_schema(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Schema(__gobject.GBoxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self, *args, **kwargs): # real signature unknown
        pass

    def get_car_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_cdr_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_value(self, *args, **kwargs): # real signature unknown
        pass

    def get_list_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_locale(self, *args, **kwargs): # real signature unknown
        pass

    def get_long_desc(self, *args, **kwargs): # real signature unknown
        pass

    def get_owner(self, *args, **kwargs): # real signature unknown
        pass

    def get_short_desc(self, *args, **kwargs): # real signature unknown
        pass

    def get_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_car_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_cdr_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_default_value(self, *args, **kwargs): # real signature unknown
        pass

    def set_default_value_nocopy(self, *args, **kwargs): # real signature unknown
        pass

    def set_list_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_locale(self, *args, **kwargs): # real signature unknown
        pass

    def set_long_desc(self, *args, **kwargs): # real signature unknown
        pass

    def set_owner(self, *args, **kwargs): # real signature unknown
        pass

    def set_short_desc(self, *args, **kwargs): # real signature unknown
        pass

    def set_type(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class UnsetFlags(__gobject.GFlags):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __flags_values__ = {
        1: 1,
    }
    __gtype__ = None # (!) real value is ''


class Value(__gobject.GBoxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self, *args, **kwargs): # real signature unknown
        pass

    def get_bool(self, *args, **kwargs): # real signature unknown
        pass

    def get_car(self, *args, **kwargs): # real signature unknown
        pass

    def get_cdr(self, *args, **kwargs): # real signature unknown
        pass

    def get_float(self, *args, **kwargs): # real signature unknown
        pass

    def get_int(self, *args, **kwargs): # real signature unknown
        pass

    def get_list(self, *args, **kwargs): # real signature unknown
        pass

    def get_list_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_schema(self, *args, **kwargs): # real signature unknown
        pass

    def get_string(self, *args, **kwargs): # real signature unknown
        pass

    def set_bool(self, *args, **kwargs): # real signature unknown
        pass

    def set_car(self, *args, **kwargs): # real signature unknown
        pass

    def set_cdr(self, *args, **kwargs): # real signature unknown
        pass

    def set_float(self, *args, **kwargs): # real signature unknown
        pass

    def set_int(self, *args, **kwargs): # real signature unknown
        pass

    def set_list(self, *args, **kwargs): # real signature unknown
        pass

    def set_list_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_schema(self, *args, **kwargs): # real signature unknown
        pass

    def set_schema_nocopy(self, *args, **kwargs): # real signature unknown
        pass

    def set_string(self, *args, **kwargs): # real signature unknown
        pass

    def to_string(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


class ValueType(__gobject.GEnum):
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
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
    }
    __gtype__ = None # (!) real value is ''


