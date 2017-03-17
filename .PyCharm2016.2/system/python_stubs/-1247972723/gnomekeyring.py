# encoding: utf-8
# module gnomekeyring
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gnomekeyring.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject


# Variables with simple values

ACCESS_ALLOW = 2
ACCESS_ASK = 0
ACCESS_DENY = 1
ACCESS_READ = 1
ACCESS_REMOVE = 4
ACCESS_WRITE = 2

ATTRIBUTE_TYPE_STRING = 0
ATTRIBUTE_TYPE_UINT32 = 1

ITEM_GENERIC_SECRET = 0

ITEM_LAST_TYPE = 257

ITEM_NETWORK_PASSWORD = 1

ITEM_NOTE = 2

ITEM_NO_TYPE = 65535

__version__ = '2.32.0'

# functions

def change_password_sync(*args, **kwargs): # real signature unknown
    pass

def create_sync(*args, **kwargs): # real signature unknown
    pass

def daemon_set_display_sync(*args, **kwargs): # real signature unknown
    pass

def delete_sync(*args, **kwargs): # real signature unknown
    pass

def find_items(*args, **kwargs): # real signature unknown
    pass

def find_items_sync(*args, **kwargs): # real signature unknown
    pass

def find_network_password_sync(*args, **kwargs): # real signature unknown
    pass

def get_default_keyring_sync(*args, **kwargs): # real signature unknown
    pass

def get_info_sync(*args, **kwargs): # real signature unknown
    pass

def is_available(*args, **kwargs): # real signature unknown
    pass

def item_create(*args, **kwargs): # real signature unknown
    pass

def item_create_sync(*args, **kwargs): # real signature unknown
    pass

def item_delete_sync(*args, **kwargs): # real signature unknown
    pass

def item_get_acl_sync(*args, **kwargs): # real signature unknown
    pass

def item_get_attributes_sync(*args, **kwargs): # real signature unknown
    pass

def item_get_info(*args, **kwargs): # real signature unknown
    pass

def item_get_info_sync(*args, **kwargs): # real signature unknown
    pass

def item_set_acl_sync(*args, **kwargs): # real signature unknown
    pass

def item_set_attributes_sync(*args, **kwargs): # real signature unknown
    pass

def item_set_info_sync(*args, **kwargs): # real signature unknown
    pass

def list_item_ids_sync(*args, **kwargs): # real signature unknown
    pass

def list_keyring_names_sync(*args, **kwargs): # real signature unknown
    pass

def lock_all_sync(*args, **kwargs): # real signature unknown
    pass

def lock_sync(*args, **kwargs): # real signature unknown
    pass

def set_default_keyring_sync(*args, **kwargs): # real signature unknown
    pass

def set_info_sync(*args, **kwargs): # real signature unknown
    pass

def set_network_password_sync(*args, **kwargs): # real signature unknown
    pass

def unlock_sync(*args, **kwargs): # real signature unknown
    pass

# classes

class AccessControl(__gobject.GBoxed):
    # no doc
    def get_access_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_display_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_path_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_access_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_display_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_path_name(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class AlreadyExistsError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class AlreadyUnlockedError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ApplicationRef(__gobject.GBoxed):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class BadArgumentsError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class CancelledError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DeniedError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Found(__gobject.GBoxed):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    item_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keyring = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secret = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


class Info(__gobject.GBoxed):
    # no doc
    def get_ctime(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_locked(self, *args, **kwargs): # real signature unknown
        pass

    def get_lock_on_idle(self, *args, **kwargs): # real signature unknown
        pass

    def get_lock_timeout(self, *args, **kwargs): # real signature unknown
        pass

    def get_mtime(self, *args, **kwargs): # real signature unknown
        pass

    def set_lock_on_idle(self, *args, **kwargs): # real signature unknown
        pass

    def set_lock_timeout(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class IOError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ItemInfo(__gobject.GBoxed):
    # no doc
    def get_ctime(self, *args, **kwargs): # real signature unknown
        pass

    def get_display_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_mtime(self, *args, **kwargs): # real signature unknown
        pass

    def get_secret(self, *args, **kwargs): # real signature unknown
        pass

    def set_display_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_secret(self, *args, **kwargs): # real signature unknown
        pass

    def set_type(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class NoKeyringDaemonError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class NoMatchError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class NoSuchKeyringError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


