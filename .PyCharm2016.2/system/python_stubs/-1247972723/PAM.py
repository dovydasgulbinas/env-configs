# encoding: utf-8
# module PAM
# from /usr/lib/python2.7/dist-packages/PAM.x86_64-linux-gnu.so
# by generator 1.143
# no doc
# no imports

# Variables with simple values

PAM_ABORT = 26

PAM_ACCT_EXPIRED = 13

PAM_AUTHINFO_UNAVAIL = 9

PAM_AUTHTOK_DISABLE_AGING = 23

PAM_AUTHTOK_ERR = 20
PAM_AUTHTOK_EXPIRED = 27

PAM_AUTHTOK_LOCK_BUSY = 22

PAM_AUTHTOK_RECOVER_ERR = 21

PAM_AUTH_ERR = 7

PAM_BAD_ITEM = 29

PAM_BUF_ERR = 5

PAM_CHANGE_EXPIRED_AUTHTOK = 32

PAM_CONV = 5

PAM_CONV_ERR = 19

PAM_CRED_ERR = 17
PAM_CRED_EXPIRED = 16
PAM_CRED_INSUFFICIENT = 8
PAM_CRED_UNAVAIL = 15

PAM_DATA_SILENT = 1073741824

PAM_DELETE_CRED = 4

PAM_DISALLOW_NULL_AUTHTOK = 1

PAM_ERROR_MSG = 3

PAM_ESTABLISH_CRED = 2

PAM_IGNORE = 25
PAM_MAXTRIES = 11

PAM_MODULE_UNKNOWN = 28

PAM_NEW_AUTHTOK_REQD = 12

PAM_NO_MODULE_DATA = 18

PAM_OPEN_ERR = 1

PAM_PERM_DENIED = 6

PAM_PROMPT_ECHO_OFF = 1
PAM_PROMPT_ECHO_ON = 2

PAM_REFRESH_CRED = 16

PAM_REINITIALIZE_CRED = 8

PAM_RHOST = 4
PAM_RUSER = 8
PAM_SERVICE = 1

PAM_SERVICE_ERR = 3

PAM_SESSION_ERR = 14

PAM_SILENT = 32768
PAM_SUCCESS = 0

PAM_SYMBOL_ERR = 2

PAM_SYSTEM_ERR = 4

PAM_TEXT_INFO = 4

PAM_TRY_AGAIN = 24

PAM_TTY = 3
PAM_USER = 2

PAM_USER_PROMPT = 9
PAM_USER_UNKNOWN = 10

_PAM_RETURN_VALUES = 32

# functions

def pam(*args, **kwargs): # real signature unknown
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



