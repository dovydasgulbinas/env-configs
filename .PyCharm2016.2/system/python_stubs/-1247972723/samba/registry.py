# encoding: utf-8
# module samba.registry
# from /usr/lib/python2.7/dist-packages/samba/registry.so
# by generator 1.143
""" Registry """

# imports
import talloc as __talloc


# Variables with simple values

HKEY_CLASSES_ROOT = 2147483648

HKEY_CURRENT_CONFIG = 2147483653
HKEY_CURRENT_USER = 2147483649

HKEY_DYN_DATA = 2147483654

HKEY_LOCAL_MACHINE = 2147483650

HKEY_PERFORMANCE_DATA = 2147483652
HKEY_PERFORMANCE_NLSTEXT = 2147483744
HKEY_PERFORMANCE_TEXT = 2147483728

HKEY_USERS = 2147483651

# functions

def get_predef_name(hkey): # real signature unknown; restored from __doc__
    """ get_predef_name(hkey) -> str """
    return ""

def open_hive(location, session_info=None, credentials=None, loadparm_context=None): # real signature unknown; restored from __doc__
    """ open_hive(location, session_info=None, credentials=None, loadparm_context=None) -> key """
    pass

def open_ldb(location, session_info=None, credentials=None, loadparm_context=None): # real signature unknown; restored from __doc__
    """ open_ldb(location, session_info=None, credentials=None, loadparm_context=None) -> key """
    pass

def open_samba(): # real signature unknown; restored from __doc__
    """ open_samba() -> reg """
    pass

def str_regtype(p_int): # real signature unknown; restored from __doc__
    """ str_regtype(int) -> str """
    return ""

# classes

class HiveKey(__talloc.Object):
    # no doc
    def del_value(self, name): # real signature unknown; restored from __doc__
        """
        S.del_value(name) -> None
        Delete a value
        """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """
        S.flush() -> None
        Flush this key to disk
        """
        pass

    def set_value(self, name, type, data): # real signature unknown; restored from __doc__
        """
        S.set_value(name, type, data) -> None
        Set a value
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Registry(__talloc.Object):
    # no doc
    def diff_apply(self, filename): # real signature unknown; restored from __doc__
        """
        S.diff_apply(filename) -> None
        Apply the diff from the specified file
        """
        pass

    def get_predefined_key(self, hkey_id): # real signature unknown; restored from __doc__
        """
        S.get_predefined_key(hkey_id) -> key
        Find a predefined key by id
        """
        pass

    def get_predefined_key_by_name(self, name): # real signature unknown; restored from __doc__
        """
        S.get_predefined_key_by_name(name) -> key
        Find a predefined key by name
        """
        pass

    def key_del_abs(self, name): # real signature unknown; restored from __doc__
        """
        S.key_del_abs(name) -> None
        Delete a key by absolute path.
        """
        pass

    def mount_hive(self, key, key_id, elements=None): # real signature unknown; restored from __doc__
        """
        S.mount_hive(key, key_id, elements=None) -> None
        Mount the specified key at the specified path.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class RegistryKey(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


