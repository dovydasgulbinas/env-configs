# encoding: utf-8
# module samba.dcerpc.initshutdown
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/initshutdown.so
# by generator 1.143
""" initshutdown DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc


# Variables with simple values

SHTDN_REASON_FLAG_PLANNED = 2147483648

SHTDN_REASON_FLAG_USER_DEFINED = 1073741824

SHTDN_REASON_MAJOR_APPLICATION = 262144
SHTDN_REASON_MAJOR_HARDWARE = 65536

SHTDN_REASON_MAJOR_LEGACY_API = 458752

SHTDN_REASON_MAJOR_OPERATINGSYSTEM = 131072
SHTDN_REASON_MAJOR_OTHER = 0
SHTDN_REASON_MAJOR_POWER = 393216
SHTDN_REASON_MAJOR_SOFTWARE = 196608
SHTDN_REASON_MAJOR_SYSTEM = 327680

SHTDN_REASON_MINOR_BLUESCREEN = 15
SHTDN_REASON_MINOR_CORDUNPLUGGED = 11
SHTDN_REASON_MINOR_DISK = 7
SHTDN_REASON_MINOR_ENVIRONMENT = 12

SHTDN_REASON_MINOR_HARDWARE_DRIVER = 13

SHTDN_REASON_MINOR_HOTFIX = 17

SHTDN_REASON_MINOR_HOTFIX_UNINSTALL = 23

SHTDN_REASON_MINOR_HUNG = 5
SHTDN_REASON_MINOR_INSTALLATION = 2
SHTDN_REASON_MINOR_MAINTENANCE = 1
SHTDN_REASON_MINOR_MMC = 25
SHTDN_REASON_MINOR_NETWORKCARD = 9

SHTDN_REASON_MINOR_NETWORK_CONNECTIVITY = 20

SHTDN_REASON_MINOR_OTHER = 0
SHTDN_REASON_MINOR_OTHERDRIVER = 14

SHTDN_REASON_MINOR_POWER_SUPPLY = 10

SHTDN_REASON_MINOR_PROCESSOR = 8
SHTDN_REASON_MINOR_RECONFIG = 4
SHTDN_REASON_MINOR_SECURITY = 19
SHTDN_REASON_MINOR_SECURITYFIX = 18

SHTDN_REASON_MINOR_SECURITYFIX_UNINSTALL = 24

SHTDN_REASON_MINOR_SERVICEPACK = 16

SHTDN_REASON_MINOR_SERVICEPACK_UNINSTALL = 22

SHTDN_REASON_MINOR_TERMSRV = 32
SHTDN_REASON_MINOR_UNSTABLE = 6
SHTDN_REASON_MINOR_UPGRADE = 3
SHTDN_REASON_MINOR_WMI = 21

# no functions
# classes

class abstract_syntax(__misc.ndr_syntax_id):
    """
    abstract_syntax()
    Init shutdown service
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class initshutdown(__dcerpc.ClientConnection):
    """
    initshutdown(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Init shutdown service
    """
    def Abort(self, server): # real signature unknown; restored from __doc__
        """ S.Abort(server) -> None """
        pass

    def Init(self, hostname, message, timeout, force_apps, do_reboot): # real signature unknown; restored from __doc__
        """ S.Init(hostname, message, timeout, force_apps, do_reboot) -> None """
        pass

    def InitEx(self, hostname, message, timeout, force_apps, do_reboot, reason): # real signature unknown; restored from __doc__
        """ S.InitEx(hostname, message, timeout, force_apps, do_reboot, reason) -> None """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


