# encoding: utf-8
# module samba.dcerpc.svcctl
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/svcctl.so
# by generator 1.143
""" svcctl DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

SC_ACTION_NONE = 0
SC_ACTION_REBOOT = 2
SC_ACTION_RESTART = 1

SC_ACTION_RUN_COMMAND = 3

SC_MANAGER_ALL_ACCESS = 983103

SC_MANAGER_EXECUTE_ACCESS = 131093

SC_MANAGER_READ_ACCESS = 131093

SC_MANAGER_WRITE_ACCESS = 983103

SC_MAX_ARGUMENTS = 1024

SC_MAX_ARGUMENT_LENGTH = 1024

SC_RIGHT_MGR_CONNECT = 1

SC_RIGHT_MGR_CREATE_SERVICE = 2

SC_RIGHT_MGR_ENUMERATE_SERVICE = 4

SC_RIGHT_MGR_LOCK = 8

SC_RIGHT_MGR_MODIFY_BOOT_CONFIG = 32

SC_RIGHT_MGR_QUERY_LOCK_STATUS = 16

SC_RIGHT_SVC_CHANGE_CONFIG = 2

SC_RIGHT_SVC_ENUMERATE_DEPENDENTS = 8

SC_RIGHT_SVC_INTERROGATE = 128

SC_RIGHT_SVC_PAUSE_CONTINUE = 64

SC_RIGHT_SVC_QUERY_CONFIG = 1
SC_RIGHT_SVC_QUERY_STATUS = 4

SC_RIGHT_SVC_START = 16
SC_RIGHT_SVC_STOP = 32

SC_RIGHT_SVC_USER_DEFINED_CONTROL = 256

SERVICE_ALL_ACCESS = 983551

SERVICE_CONFIG_DESCRIPTION = 1

SERVICE_CONFIG_FAILURE_ACTIONS = 2

SERVICE_EXECUTE_ACCESS = 131581

SERVICE_READ_ACCESS = 131469

SERVICE_STATE_ACTIVE = 1
SERVICE_STATE_ALL = 3
SERVICE_STATE_INACTIVE = 2

SERVICE_TYPE_ADAPTER = 4
SERVICE_TYPE_DRIVER = 11

SERVICE_TYPE_FS_DRIVER = 2

SERVICE_TYPE_INTERACTIVE_PROCESS = 256

SERVICE_TYPE_KERNEL_DRIVER = 1

SERVICE_TYPE_RECOGNIZER_DRIVER = 8

SERVICE_TYPE_WIN32 = 48

SERVICE_TYPE_WIN32_OWN_PROCESS = 16

SERVICE_TYPE_WIN32_SHARE_PROCESS = 32

SERVICE_WRITE_ACCESS = 983551

SVCCTL_ACCEPT_HARDWAREPROFILECHANGE = 32
SVCCTL_ACCEPT_NETBINDCHANGE = 16
SVCCTL_ACCEPT_NONE = 0
SVCCTL_ACCEPT_PARAMCHANGE = 8

SVCCTL_ACCEPT_PAUSE_CONTINUE = 2

SVCCTL_ACCEPT_POWEREVENT = 64
SVCCTL_ACCEPT_SHUTDOWN = 4
SVCCTL_ACCEPT_STOP = 1

SVCCTL_AUTO_START = 2

SVCCTL_BOOT_START = 0

SVCCTL_CONTINUE_PENDING = 5

SVCCTL_CONTROL_CONTINUE = 3
SVCCTL_CONTROL_INTERROGATE = 4
SVCCTL_CONTROL_PAUSE = 2
SVCCTL_CONTROL_SHUTDOWN = 5
SVCCTL_CONTROL_STOP = 1

SVCCTL_DEMAND_START = 3

SVCCTL_DISABLED = 4
SVCCTL_PAUSED = 7

SVCCTL_PAUSE_PENDING = 6

SVCCTL_RUNNING = 4

SVCCTL_START_PENDING = 2

SVCCTL_STATE_UNKNOWN = 0

SVCCTL_STOPPED = 1

SVCCTL_STOP_PENDING = 3

SVCCTL_SVC_ERROR_CRITICAL = 2
SVCCTL_SVC_ERROR_IGNORE = 0
SVCCTL_SVC_ERROR_NORMAL = 1
SVCCTL_SVC_ERROR_SEVERE = 3

SVCCTL_SYSTEM_START = 1

SVC_STATUS_PROCESS_INFO = 0

# no functions
# classes

class abstract_syntax(__misc.ndr_syntax_id):
    """
    abstract_syntax()
    Service Control
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class ArgumentString(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ENUM_SERVICE_STATUSA(__talloc.Object):
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

    display_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    service_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ENUM_SERVICE_STATUSW(__talloc.Object):
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

    display_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    service_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class QUERY_SERVICE_CONFIG(__talloc.Object):
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

    dependencies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    displayname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    error_control = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    executablepath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loadordergroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    service_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    startname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tag_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SC_ACTION(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    delay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SERVICE_DESCRIPTION(__talloc.Object):
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

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SERVICE_FAILURE_ACTIONS(__talloc.Object):
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

    actions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_actions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rebootmsg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reset_period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SERVICE_LOCK_STATUS(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    is_locked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock_duration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock_owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SERVICE_STATUS(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    check_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    controls_accepted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    service_exit_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wait_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    win32_exit_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SERVICE_STATUS_PROCESS(__talloc.Object):
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

    process_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    service_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class svcctl(__dcerpc.ClientConnection):
    """
    svcctl(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Service Control
    """
    def ChangeServiceConfig2A(self, handle, info_level, info): # real signature unknown; restored from __doc__
        """ S.ChangeServiceConfig2A(handle, info_level, info) -> None """
        pass

    def ChangeServiceConfig2W(self, handle, info_level, info): # real signature unknown; restored from __doc__
        """ S.ChangeServiceConfig2W(handle, info_level, info) -> None """
        pass

    def ChangeServiceConfigA(self, handle, type, start_type, error_control, binary_path, load_order_group, dependencies, service_start_name, password, display_name): # real signature unknown; restored from __doc__
        """ S.ChangeServiceConfigA(handle, type, start_type, error_control, binary_path, load_order_group, dependencies, service_start_name, password, display_name) -> tag_id """
        pass

    def ChangeServiceConfigW(self, handle, type, start_type, error_control, binary_path, load_order_group, dependencies, service_start_name, password, display_name): # real signature unknown; restored from __doc__
        """ S.ChangeServiceConfigW(handle, type, start_type, error_control, binary_path, load_order_group, dependencies, service_start_name, password, display_name) -> tag_id """
        pass

    def CloseServiceHandle(self, handle): # real signature unknown; restored from __doc__
        """ S.CloseServiceHandle(handle) -> handle """
        pass

    def ControlService(self, handle, control): # real signature unknown; restored from __doc__
        """ S.ControlService(handle, control) -> service_status """
        pass

    def CreateServiceA(self, handle, ServiceName, DisplayName, desired_access, type, start_type, error_control, binary_path, LoadOrderGroupKey, dependencies, service_start_name, password): # real signature unknown; restored from __doc__
        """ S.CreateServiceA(handle, ServiceName, DisplayName, desired_access, type, start_type, error_control, binary_path, LoadOrderGroupKey, dependencies, service_start_name, password) -> TagId """
        pass

    def CreateServiceW(self, scmanager_handle, ServiceName, DisplayName, desired_access, type, start_type, error_control, binary_path, LoadOrderGroupKey, TagId, dependencies, service_start_name, password): # real signature unknown; restored from __doc__
        """ S.CreateServiceW(scmanager_handle, ServiceName, DisplayName, desired_access, type, start_type, error_control, binary_path, LoadOrderGroupKey, TagId, dependencies, service_start_name, password) -> (TagId, handle) """
        pass

    def DeleteService(self, handle): # real signature unknown; restored from __doc__
        """ S.DeleteService(handle) -> None """
        pass

    def EnumDependentServicesA(self, service, state, offered): # real signature unknown; restored from __doc__
        """ S.EnumDependentServicesA(service, state, offered) -> (service_status, needed, services_returned) """
        pass

    def EnumDependentServicesW(self, service, state, offered): # real signature unknown; restored from __doc__
        """ S.EnumDependentServicesW(service, state, offered) -> (service_status, needed, services_returned) """
        pass

    def EnumServicesStatusA(self, handle, type, state, offered, resume_handle): # real signature unknown; restored from __doc__
        """ S.EnumServicesStatusA(handle, type, state, offered, resume_handle) -> (service, needed, services_returned, resume_handle) """
        pass

    def EnumServicesStatusExA(self, scmanager, info_level, type, state, offered, resume_handle): # real signature unknown; restored from __doc__
        """ S.EnumServicesStatusExA(scmanager, info_level, type, state, offered, resume_handle) -> (services, needed, service_returned, resume_handle, group_name) """
        pass

    def EnumServicesStatusExW(self, scmanager, info_level, type, state, offered, resume_handle, group_name): # real signature unknown; restored from __doc__
        """ S.EnumServicesStatusExW(scmanager, info_level, type, state, offered, resume_handle, group_name) -> (services, needed, service_returned, resume_handle) """
        pass

    def EnumServicesStatusW(self, handle, type, state, offered, resume_handle): # real signature unknown; restored from __doc__
        """ S.EnumServicesStatusW(handle, type, state, offered, resume_handle) -> (service, needed, services_returned, resume_handle) """
        pass

    def GetServiceDisplayNameA(self, handle, service_name, display_name_length): # real signature unknown; restored from __doc__
        """ S.GetServiceDisplayNameA(handle, service_name, display_name_length) -> (display_name, display_name_length) """
        pass

    def GetServiceDisplayNameW(self, handle, service_name, display_name_length): # real signature unknown; restored from __doc__
        """ S.GetServiceDisplayNameW(handle, service_name, display_name_length) -> (display_name, display_name_length) """
        pass

    def GetServiceKeyNameA(self, handle, service_name, display_name_length): # real signature unknown; restored from __doc__
        """ S.GetServiceKeyNameA(handle, service_name, display_name_length) -> (key_name, display_name_length) """
        pass

    def GetServiceKeyNameW(self, handle, service_name, display_name_length): # real signature unknown; restored from __doc__
        """ S.GetServiceKeyNameW(handle, service_name, display_name_length) -> (key_name, display_name_length) """
        pass

    def LockServiceDatabase(self, handle): # real signature unknown; restored from __doc__
        """ S.LockServiceDatabase(handle) -> lock """
        pass

    def OpenSCManagerA(self, MachineName, DatabaseName, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenSCManagerA(MachineName, DatabaseName, access_mask) -> handle """
        pass

    def OpenSCManagerW(self, MachineName, DatabaseName, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenSCManagerW(MachineName, DatabaseName, access_mask) -> handle """
        pass

    def OpenServiceA(self, scmanager_handle, ServiceName, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenServiceA(scmanager_handle, ServiceName, access_mask) -> handle """
        pass

    def OpenServiceW(self, scmanager_handle, ServiceName, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenServiceW(scmanager_handle, ServiceName, access_mask) -> handle """
        pass

    def QueryServiceConfig2A(self, handle, info_level, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceConfig2A(handle, info_level, offered) -> (buffer, needed) """
        pass

    def QueryServiceConfig2W(self, handle, info_level, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceConfig2W(handle, info_level, offered) -> (buffer, needed) """
        pass

    def QueryServiceConfigA(self, handle, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceConfigA(handle, offered) -> (query, needed) """
        pass

    def QueryServiceConfigW(self, handle, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceConfigW(handle, offered) -> (query, needed) """
        pass

    def QueryServiceLockStatusA(self, handle, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceLockStatusA(handle, offered) -> (lock_status, needed) """
        pass

    def QueryServiceLockStatusW(self, handle, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceLockStatusW(handle, offered) -> (lock_status, needed) """
        pass

    def QueryServiceObjectSecurity(self, handle, security_flags, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceObjectSecurity(handle, security_flags, offered) -> (buffer, needed) """
        pass

    def QueryServiceStatus(self, handle): # real signature unknown; restored from __doc__
        """ S.QueryServiceStatus(handle) -> service_status """
        pass

    def QueryServiceStatusEx(self, handle, info_level, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceStatusEx(handle, info_level, offered) -> (buffer, needed) """
        pass

    def SCSetServiceBitsA(self, handle, bits, bitson, immediate): # real signature unknown; restored from __doc__
        """ S.SCSetServiceBitsA(handle, bits, bitson, immediate) -> None """
        pass

    def SCSetServiceBitsW(self, handle, bits, bitson, immediate): # real signature unknown; restored from __doc__
        """ S.SCSetServiceBitsW(handle, bits, bitson, immediate) -> None """
        pass

    def SetServiceObjectSecurity(self, handle, security_flags, buffer): # real signature unknown; restored from __doc__
        """ S.SetServiceObjectSecurity(handle, security_flags, buffer) -> None """
        pass

    def StartServiceA(self, handle, NumArgs, Arguments): # real signature unknown; restored from __doc__
        """ S.StartServiceA(handle, NumArgs, Arguments) -> None """
        pass

    def StartServiceW(self, handle, Arguments): # real signature unknown; restored from __doc__
        """ S.StartServiceW(handle, Arguments) -> None """
        pass

    def UnlockServiceDatabase(self, lock): # real signature unknown; restored from __doc__
        """ S.UnlockServiceDatabase(lock) -> lock """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


