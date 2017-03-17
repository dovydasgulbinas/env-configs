# encoding: utf-8
# module samba.dcerpc.winreg
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/winreg.so
# by generator 1.143
""" winreg DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

KEY_CREATE_LINK = 32

KEY_CREATE_SUB_KEY = 4

KEY_ENUMERATE_SUB_KEYS = 8

KEY_NOTIFY = 16

KEY_QUERY_VALUE = 1

KEY_SET_VALUE = 2

KEY_WOW64_32KEY = 512
KEY_WOW64_64KEY = 256

REG_ACTION_NONE = 0

REG_CREATED_NEW_KEY = 1

REG_FORCE_RESTORE = 8

REG_KEY_ALL = 983103
REG_KEY_EXECUTE = 131097
REG_KEY_READ = 131097
REG_KEY_WRITE = 851974

REG_NOTIFY_CHANGE_ATTRIBUTES = 2

REG_NOTIFY_CHANGE_LAST_SET = 4

REG_NOTIFY_CHANGE_NAME = 1
REG_NOTIFY_CHANGE_SECURITY = 8

REG_NO_LAZY_FLUSH = 4

REG_OPENED_EXISTING_KEY = 2

REG_OPTION_BACKUP_RESTORE = 4

REG_OPTION_CREATE_LINK = 2

REG_OPTION_NON_VOLATILE = 0

REG_OPTION_OPEN_LINK = 8

REG_OPTION_VOLATILE = 1

REG_REFRESH_HIVE = 2

REG_WHOLE_HIVE_VOLATILE = 1

# no functions
# classes

class abstract_syntax(__misc.ndr_syntax_id):
    """
    abstract_syntax()
    Remote Registry Service
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class KeySecurityAttribute(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    data_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inherit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sec_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class KeySecurityData(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class QueryMultipleValue(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    ve_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ve_valuelen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ve_valuename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ve_valueptr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SecBuf(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    inherit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class String(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class StringBuf(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ValNameBuf(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class winreg(__dcerpc.ClientConnection):
    """
    winreg(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Remote Registry Service
    """
    def AbortSystemShutdown(self, server): # real signature unknown; restored from __doc__
        """ S.AbortSystemShutdown(server) -> None """
        pass

    def CloseKey(self, handle): # real signature unknown; restored from __doc__
        """ S.CloseKey(handle) -> handle """
        pass

    def CreateKey(self, handle, name, keyclass, options, access_mask, secdesc, action_taken): # real signature unknown; restored from __doc__
        """ S.CreateKey(handle, name, keyclass, options, access_mask, secdesc, action_taken) -> (new_handle, action_taken) """
        pass

    def DeleteKey(self, handle, key): # real signature unknown; restored from __doc__
        """ S.DeleteKey(handle, key) -> None """
        pass

    def DeleteKeyEx(self, handle, key, access_mask, reserved): # real signature unknown; restored from __doc__
        """ S.DeleteKeyEx(handle, key, access_mask, reserved) -> None """
        pass

    def DeleteValue(self, handle, value): # real signature unknown; restored from __doc__
        """ S.DeleteValue(handle, value) -> None """
        pass

    def EnumKey(self, handle, enum_index, name, keyclass, last_changed_time): # real signature unknown; restored from __doc__
        """ S.EnumKey(handle, enum_index, name, keyclass, last_changed_time) -> (name, keyclass, last_changed_time) """
        pass

    def EnumValue(self, handle, enum_index, name, type, value, size, length): # real signature unknown; restored from __doc__
        """ S.EnumValue(handle, enum_index, name, type, value, size, length) -> (name, type, value, size, length) """
        pass

    def FlushKey(self, handle): # real signature unknown; restored from __doc__
        """ S.FlushKey(handle) -> None """
        pass

    def GetKeySecurity(self, handle, sec_info, sd): # real signature unknown; restored from __doc__
        """ S.GetKeySecurity(handle, sec_info, sd) -> sd """
        pass

    def GetVersion(self, handle): # real signature unknown; restored from __doc__
        """ S.GetVersion(handle) -> version """
        pass

    def InitiateSystemShutdown(self, hostname, message, timeout, force_apps, do_reboot): # real signature unknown; restored from __doc__
        """ S.InitiateSystemShutdown(hostname, message, timeout, force_apps, do_reboot) -> None """
        pass

    def InitiateSystemShutdownEx(self, hostname, message, timeout, force_apps, do_reboot, reason): # real signature unknown; restored from __doc__
        """ S.InitiateSystemShutdownEx(hostname, message, timeout, force_apps, do_reboot, reason) -> None """
        pass

    def LoadKey(self, handle, keyname, filename): # real signature unknown; restored from __doc__
        """ S.LoadKey(handle, keyname, filename) -> None """
        pass

    def NotifyChangeKeyValue(self, handle, watch_subtree, notify_filter, unknown, string1, string2, unknown2): # real signature unknown; restored from __doc__
        """ S.NotifyChangeKeyValue(handle, watch_subtree, notify_filter, unknown, string1, string2, unknown2) -> None """
        pass

    def OpenHKCC(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKCC(system_name, access_mask) -> handle """
        pass

    def OpenHKCR(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKCR(system_name, access_mask) -> handle """
        pass

    def OpenHKCU(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKCU(system_name, access_mask) -> handle """
        pass

    def OpenHKDD(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKDD(system_name, access_mask) -> handle """
        pass

    def OpenHKLM(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKLM(system_name, access_mask) -> handle """
        pass

    def OpenHKPD(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKPD(system_name, access_mask) -> handle """
        pass

    def OpenHKPN(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKPN(system_name, access_mask) -> handle """
        pass

    def OpenHKPT(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKPT(system_name, access_mask) -> handle """
        pass

    def OpenHKU(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKU(system_name, access_mask) -> handle """
        pass

    def OpenKey(self, parent_handle, keyname, options, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenKey(parent_handle, keyname, options, access_mask) -> handle """
        pass

    def QueryInfoKey(self, handle, classname): # real signature unknown; restored from __doc__
        """ S.QueryInfoKey(handle, classname) -> (classname, num_subkeys, max_subkeylen, max_classlen, num_values, max_valnamelen, max_valbufsize, secdescsize, last_changed_time) """
        pass

    def QueryMultipleValues(self, key_handle, values_in, buffer): # real signature unknown; restored from __doc__
        """ S.QueryMultipleValues(key_handle, values_in, buffer) -> (values_out, buffer) """
        pass

    def QueryMultipleValues2(self, key_handle, values_in, buffer): # real signature unknown; restored from __doc__
        """ S.QueryMultipleValues2(key_handle, values_in, buffer) -> (values_out, buffer, needed) """
        pass

    def QueryValue(self, handle, value_name, type, data, data_size, data_length): # real signature unknown; restored from __doc__
        """ S.QueryValue(handle, value_name, type, data, data_size, data_length) -> (type, data, data_size, data_length) """
        pass

    def ReplaceKey(self, handle, subkey, new_file, old_file): # real signature unknown; restored from __doc__
        """ S.ReplaceKey(handle, subkey, new_file, old_file) -> None """
        pass

    def RestoreKey(self, handle, filename, flags): # real signature unknown; restored from __doc__
        """ S.RestoreKey(handle, filename, flags) -> None """
        pass

    def SaveKey(self, handle, filename, sec_attrib): # real signature unknown; restored from __doc__
        """ S.SaveKey(handle, filename, sec_attrib) -> None """
        pass

    def SaveKeyEx(self, handle, filename, sec_attrib, flags): # real signature unknown; restored from __doc__
        """ S.SaveKeyEx(handle, filename, sec_attrib, flags) -> None """
        pass

    def SetKeySecurity(self, handle, sec_info, sd): # real signature unknown; restored from __doc__
        """ S.SetKeySecurity(handle, sec_info, sd) -> None """
        pass

    def SetValue(self, handle, name, type, data): # real signature unknown; restored from __doc__
        """ S.SetValue(handle, name, type, data) -> None """
        pass

    def UnLoadKey(self, handle, subkey): # real signature unknown; restored from __doc__
        """ S.UnLoadKey(handle, subkey) -> None """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


