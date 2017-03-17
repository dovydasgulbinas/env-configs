# encoding: utf-8
# module glib._glib
# from /usr/lib/python2.7/dist-packages/glib/_glib.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
import glib as __glib


# Variables with simple values

IO_ERR = 8

IO_FLAG_APPEND = 1

IO_FLAG_GET_MASK = 31

IO_FLAG_IS_READABLE = 4
IO_FLAG_IS_SEEKABLE = 16
IO_FLAG_IS_WRITEABLE = 8

IO_FLAG_MASK = 31
IO_FLAG_NONBLOCK = 2

IO_FLAG_SET_MASK = 3

IO_HUP = 16
IO_IN = 1
IO_NVAL = 32
IO_OUT = 4
IO_PRI = 2

IO_STATUS_AGAIN = 3
IO_STATUS_EOF = 2
IO_STATUS_ERROR = 0
IO_STATUS_NORMAL = 1

OPTION_ERROR = 'g-option-context-error-quark'

OPTION_ERROR_BAD_VALUE = 1

OPTION_ERROR_FAILED = 2

OPTION_ERROR_UNKNOWN_OPTION = 0

OPTION_FLAG_FILENAME = 16
OPTION_FLAG_HIDDEN = 1

OPTION_FLAG_IN_MAIN = 2

OPTION_FLAG_NOALIAS = 64

OPTION_FLAG_NO_ARG = 8

OPTION_FLAG_OPTIONAL_ARG = 32

OPTION_FLAG_REVERSE = 4

OPTION_REMAINING = ''

PRIORITY_DEFAULT = 0

PRIORITY_DEFAULT_IDLE = 200

PRIORITY_HIGH = -100

PRIORITY_HIGH_IDLE = 100

PRIORITY_LOW = 300

SPAWN_CHILD_INHERITS_STDIN = 32

SPAWN_DO_NOT_REAP_CHILD = 2

SPAWN_FILE_AND_ARGV_ZERO = 64

SPAWN_LEAVE_DESCRIPTORS_OPEN = 1

SPAWN_SEARCH_PATH = 4

SPAWN_STDERR_TO_DEV_NULL = 16

SPAWN_STDOUT_TO_DEV_NULL = 8

USER_DIRECTORY_DESKTOP = 0
USER_DIRECTORY_DOCUMENTS = 1
USER_DIRECTORY_DOWNLOAD = 2
USER_DIRECTORY_MUSIC = 3
USER_DIRECTORY_PICTURES = 4

USER_DIRECTORY_PUBLIC_SHARE = 5

USER_DIRECTORY_TEMPLATES = 6
USER_DIRECTORY_VIDEOS = 7

# functions

def child_watch_add(pid, callable, user_data=None, priority=None): # real signature unknown; restored from __doc__
    """
    child_watch_add(pid, callable, user_data=None,
    priority=None) -> source id
      callable receives (pid, condition, user_data)
    Sets the function specified by function to be called with the user
    data specified by data when the child indicated by pid exits.
    Condition is a combination of glib.IO_IN, glib.IO_OUT, glib.IO_PRI,
    gio.IO_ERR and gio.IO_HUB.
    """
    pass

def filename_display_basename(*args, **kwargs): # real signature unknown
    pass

def filename_display_name(*args, **kwargs): # real signature unknown
    pass

def filename_from_utf8(*args, **kwargs): # real signature unknown
    pass

def find_program_in_path(*args, **kwargs): # real signature unknown
    pass

def get_application_name(*args, **kwargs): # real signature unknown
    pass

def get_current_time(*args, **kwargs): # real signature unknown
    pass

def get_prgname(*args, **kwargs): # real signature unknown
    pass

def get_system_config_dirs(*args, **kwargs): # real signature unknown
    pass

def get_system_data_dirs(*args, **kwargs): # real signature unknown
    pass

def get_user_cache_dir(*args, **kwargs): # real signature unknown
    pass

def get_user_config_dir(*args, **kwargs): # real signature unknown
    pass

def get_user_data_dir(*args, **kwargs): # real signature unknown
    pass

def get_user_special_dir(*args, **kwargs): # real signature unknown
    pass

def idle_add(callable, user_data=None, priority=None): # real signature unknown; restored from __doc__
    """
    idle_add(callable, user_data=None, priority=None) -> source id
      callable receives (user_data)
    Adds a callable to be called whenever there are no higher priority
    events pending to the default main loop.
    """
    pass

def io_add_watch(fd, condition, callback, user_data=None): # real signature unknown; restored from __doc__
    """
    io_add_watch(fd, condition, callback, user_data=None) -> source id
      callable receives (fd, condition, user_data)
    Arranges for the fd to be monitored by the main loop for the
    specified condition. Condition is a combination of glib.IO_IN,
    glib.IO_OUT, glib.IO_PRI, gio.IO_ERR and gio.IO_HUB.
    """
    pass

def main_context_default(): # real signature unknown; restored from __doc__
    """
    main_context_default() -> a main context
    Returns the default main context. This is the main context used
    for main loop functions when a main loop is not explicitly specified.
    """
    pass

def main_depth(): # real signature unknown; restored from __doc__
    """
    main_depth() -> stack depth
    Returns the depth of the stack of calls in the main context.
    """
    pass

def markup_escape_text(*args, **kwargs): # real signature unknown
    pass

def set_application_name(*args, **kwargs): # real signature unknown
    pass

def set_prgname(*args, **kwargs): # real signature unknown
    pass

def source_remove(source_id): # real signature unknown; restored from __doc__
    """
    source_remove(source_id) -> True if removed
    Removes the event source specified by source id as returned by the
    glib.idle_add(), glib.timeout_add() or glib.io_add_watch()
    functions.
    """
    return False

def spawn_async(argv, envp=None, working_directory=None, flags=0, child_setup=None, user_data=None, standard_input=None, standard_output=None, standard_error=None): # real signature unknown; restored from __doc__
    """
    spawn_async(argv, envp=None, working_directory=None,
                flags=0, child_setup=None, user_data=None,
                standard_input=None, standard_output=None,
                standard_error=None) -> (pid, stdin, stdout, stderr)
    Execute a child program asynchronously within a glib.MainLoop()
    See the reference manual for a complete reference.
    """
    pass

def threads_init(): # real signature unknown; restored from __doc__
    """
    threads_init()
    Initialize GLib for use from multiple threads. If you also use GTK+
    itself (i.e. GUI, not just PyGObject), use gtk.gdk.threads_init()
    instead.
    """
    pass

def timeout_add(interval, callable, user_data=None, priority=None): # real signature unknown; restored from __doc__
    """
    timeout_add(interval, callable, user_data=None,
                priority=None) -> source id
      callable receives (user_data)
    Sets a callable be called repeatedly until it returns False.
    """
    pass

def timeout_add_seconds(*args, **kwargs): # real signature unknown
    """
    timeout_add(interval, callable, user_data=None,
                priority=None) -> source_id
      callable receives (user_data)
    Sets a callable be called repeatedly until it returns False.
    Use this if you want to have a timer in the "seconds" range
    and do not care about the exact time of the first call of the
    timer, use this for more efficient system power usage.
    """
    pass

def uri_list_extract_uris(uri_list): # real signature unknown; restored from __doc__
    """
    uri_list_extract_uris(uri_list) -> tuple of strings holding URIs
    Splits an string containing an URI list conforming to the 
    text/uri-list mime type defined in RFC 2483 into individual URIs, 
    discarding any comments. The URIs are not validated.
    """
    return ()

# classes

class GError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    message = None


class Source(object):
    # no doc
    def add_poll(self, *args, **kwargs): # real signature unknown
        pass

    def attach(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def get_context(self, *args, **kwargs): # real signature unknown
        pass

    def get_current_time(self, *args, **kwargs): # real signature unknown
        pass

    def remove_poll(self, *args, **kwargs): # real signature unknown
        pass

    def set_callback(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    can_recurse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


class Idle(__glib.Source):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class IOChannel(object):
    # no doc
    def add_watch(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def get_buffered(self, *args, **kwargs): # real signature unknown
        pass

    def get_buffer_condition(self, *args, **kwargs): # real signature unknown
        pass

    def get_buffer_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_close_on_unref(self, *args, **kwargs): # real signature unknown
        pass

    def get_encoding(self, *args, **kwargs): # real signature unknown
        pass

    def get_flags(self, *args, **kwargs): # real signature unknown
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        pass

    def readlines(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def set_buffered(self, *args, **kwargs): # real signature unknown
        pass

    def set_buffer_size(self, *args, **kwargs): # real signature unknown
        pass

    def set_close_on_unref(self, *args, **kwargs): # real signature unknown
        pass

    def set_encoding(self, *args, **kwargs): # real signature unknown
        pass

    def set_flags(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def writelines(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    softspace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class MainContext(object):
    # no doc
    def iteration(self, *args, **kwargs): # real signature unknown
        pass

    def pending(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass


class MainLoop(object):
    # no doc
    def get_context(self, *args, **kwargs): # real signature unknown
        pass

    def is_running(self, *args, **kwargs): # real signature unknown
        pass

    def quit(self, *args, **kwargs): # real signature unknown
        pass

    def run(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass


class OptionContext(object):
    # no doc
    def add_group(self, *args, **kwargs): # real signature unknown
        pass

    def get_help_enabled(self, *args, **kwargs): # real signature unknown
        pass

    def get_ignore_unknown_options(self, *args, **kwargs): # real signature unknown
        pass

    def get_main_group(self, *args, **kwargs): # real signature unknown
        pass

    def parse(self, *args, **kwargs): # real signature unknown
        pass

    def set_help_enabled(self, *args, **kwargs): # real signature unknown
        pass

    def set_ignore_unknown_options(self, *args, **kwargs): # real signature unknown
        pass

    def set_main_group(self, *args, **kwargs): # real signature unknown
        pass

    def _get_context(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass


class OptionGroup(object):
    # no doc
    def add_entries(self, *args, **kwargs): # real signature unknown
        pass

    def set_translation_domain(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass


class Pid(int):
    # no doc
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class PollFD(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    revents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Timeout(__glib.Source):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


# variables with complex values

glib_version = (
    2,
    48,
    0,
)

pyglib_version = (
    2,
    28,
    6,
)

_PyGLib_API = None # (!) real value is ''

