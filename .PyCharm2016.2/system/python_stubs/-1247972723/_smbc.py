# encoding: utf-8
# module _smbc
# from /usr/lib/python2.7/dist-packages/_smbc.x86_64-linux-gnu.so
# by generator 1.143
# no doc
# no imports

# Variables with simple values

COMMS_SHARE = 5L

DIR = 7L

FILE = 8L

FILE_SHARE = 3L

FLAG_FALLBACK_AFTER_KERBEROS = 2L

FLAG_NO_AUTO_ANONYMOUS_LOGON = 4L

FLAG_USE_KERBEROS = 1L

IPC_SHARE = 6L

LINK = 9L

PRINTER_SHARE = 4L

SERVER = 2L

WORKGROUP = 1L

XATTR_ACL = 'system.nt_sec_desc.acl'

XATTR_ACL_SID = 'system.nt_sec_desc.acl+'

XATTR_ALL = 'system.nt_sec_desc.*'

XATTR_ALL_SID = 'system.nt_sec_desc.*+'

XATTR_FLAG_CREATE = 1L
XATTR_FLAG_REPLACE = 2L

XATTR_GROUP = 'system.nt_sec_desc.group'

XATTR_GROUP_SID = 'system.nt_sec_desc.group+'

XATTR_OWNER = 'system.nt_sec_desc.owner'

XATTR_OWNER_SID = 'system.nt_sec_desc.owner+'

XATTR_REVISION = 'system.nt_sec_desc.revision'

# no functions
# classes

class ConnectionRefusedError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Context(object):
    """
    SMBC context
    ============
    
      A context for libsmbclient calls.
    
    Optional parameters are:
    
    auth_fn: a function for collecting authentication details from
    the user. This is called whenever authentication details are needed.
    The parameters it will be given are all strings: server, share,
    workgroup, username, and password (these last two can be ignored).
    The function should return a tuple of strings: workgroup, username,
    and password.
    
    debug: an integer representing the debug level to use.
    """
    def chmod(self, uri, mode): # real signature unknown; restored from __doc__
        """
        chmod(uri, mode) -> int
        
        @type uri: string
        @param uri: URI to chmod
        @type mode: int
        @param mode: permissions to set
        @return: 0 on success, < 0 on error
        """
        return 0

    def creat(self, uri): # real signature unknown; restored from __doc__
        """
        creat(uri) -> File
        
        @type uri: string
        @param uri: URI to creat
        @return: a L{smbc.File} object for the URI
        """
        return File

    def getxattr(self, uri, the_acl): # real signature unknown; restored from __doc__
        """
        getxattr(uri, the_acl) -> int
        
        @type uri: string
        @param uri: URI to scan
        @type name: string
        @param name: the acl to get with the following syntax
        
                              system.nt_sec_desc.<attribute name>
                             system.nt_sec_desc.*
                             system.nt_sec_desc.*+
                             
                          where <attribute name> is one of:
                          
                             revision
                             owner
                             owner+
                             group
                             group+
                             acl:<name or sid>
                             acl+:<name or sid>
                             
                          In the forms "system.nt_sec_desc.*" and
                          "system.nt_sec_desc.*+", the asterisk and plus signs are
                          literal, i.e. the string is provided exactly as shown, and
                          the value parameter will return a complete security
                          descriptor with name:value pairs separated by tabs,
                          commas, or newlines (not spaces!).
        
                          The plus sign ('+') indicates that SIDs should be mapped
                          to names.  Without the plus sign, SIDs are not mapped;
                          rather they are simply converted to a string format.
        @return: a string representing the actual extended attributes of the uri
        """
        return 0

    def mkdir(self, uri, mode): # real signature unknown; restored from __doc__
        """
        mkdir(uri, mode) -> int
        
        @type uri: string
        @param uri: URI to mkdir
        @param mode: Specifies the permissions to use.
        @return: 0 on success, < 0 on error
        """
        return 0

    def open(self, uri): # real signature unknown; restored from __doc__
        """
        open(uri) -> File
        
        @type uri: string
        @param uri: URI to open
        @return: a L{smbc.File} object for the URI
        """
        return File

    def opendir(self, uri): # real signature unknown; restored from __doc__
        """
        opendir(uri) -> Dir
        
        @type uri: string
        @param uri: URI to opendir
        @return: a L{smbc.Dir} object for the URI
        """
        return Dir

    def rename(self, ouri, nuri): # real signature unknown; restored from __doc__
        """
        rename(ouri, nuri) -> int
        
        @type ouri: string
        @param ouri: The original smb uri
        @type nuri: string
        @param nuri: The new smb uri
        @return: 0 on success, < 0 on error
        """
        return 0

    def rmdir(self, uri): # real signature unknown; restored from __doc__
        """
        rmdir(uri) -> int
        
        @type uri: string
        @param uri: URI to rmdir
        @return: 0 on success, < 0 on error
        """
        return 0

    def setxattr(self, uri, the_acl): # real signature unknown; restored from __doc__
        """
        setxattr(uri, the_acl) -> int
        
        @type uri: string
        @param uri: URI to modify
        @type name: string
        @param name: the acl to set with the following syntax
        
                              system.nt_sec_desc.<attribute name>
                             system.nt_sec_desc.*
                             system.nt_sec_desc.*+
                             
                          where <attribute name> is one of:
                          
                             revision
                             owner
                             owner+
                             group
                             group+
                             acl:<name or sid>
                             acl+:<name or sid>
                             
                          In the forms "system.nt_sec_desc.*" and
                          "system.nt_sec_desc.*+", the asterisk and plus signs are
                          literal, i.e. the string is provided exactly as shown, and
                          the value parameter will return a complete security
                          descriptor with name:value pairs separated by tabs,
                          commas, or newlines (not spaces!).
        
                          The plus sign ('+') indicates that SIDs should be mapped
                          to names.  Without the plus sign, SIDs are not mapped;
                          rather they are simply converted to a string format.
        @type	string
        @param value - a string representing the acl
        @type	int
        @param flags - XATTR_FLAG_CREATE or XATTR_FLAG_REPLACE
        @return: 0 on success
        """
        return 0

    def set_credentials_with_fallback(self, workgroup, user, password): # real signature unknown; restored from __doc__
        """
        set_credentials_with_fallback(workgroup, user, password)
        
        @type workgroup: string
        @param workgroup: Workgroup of user
        @type user: string
        @param user: Username of user
        @type password: string
        @param password: Password of user
        """
        pass

    def stat(self, uri): # real signature unknown; restored from __doc__
        """
        stat(uri) -> tuple
        
        @type uri: string
        @param uri: URI to get stat information
        @return: stat information
        """
        return ()

    def unlink(self, uri): # real signature unknown; restored from __doc__
        """
        unlink(uri) -> int
        
        @type uri: string
        @param uri: URI to unlink
        @return: 0 on success, < 0 on error
        """
        return 0

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    debug = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Debug level."""

    functionAuthData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function for obtaining authentication data."""

    netbiosName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Netbios name used for making connections."""

    optionDebugToStderr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to log to standard error instead of standard output."""

    optionFallbackAfterKerberos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to fallback after Kerberos."""

    optionNoAutoAnonymousLogin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to automatically select anonymous login."""

    optionUseKerberos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to enable use of Kerberos."""

    timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the timeout used for waiting on connections and response data(in milliseconds)"""

    workgroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Workgroup used for making connections."""



class Dir(object):
    """
    SMBC Dir
    ========
    
      A directory object.
    """
    def getdents(self): # real signature unknown; restored from __doc__
        """
        getdents() -> list
        
        @return: a list of L{smbc.Dirent} objects
        """
        return []

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Dirent(object):
    """
    SMBC Dirent
    ===========
    
      A directory entry object.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """comment"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name"""

    smbc_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """smbc_type"""



class ExistsError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class File(object):
    """
    SMBC File
    =========
    
      A file object.
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close() -> int
        
        @return: on success, < 0 on error
        """
        return 0

    def fstat(self): # real signature unknown; restored from __doc__
        """
        fstat() -> tuple
        
        @return: fstat information
        """
        return ()

    def lseek(self, offset, whence=0): # real signature unknown; restored from __doc__
        """
        lseek(offset, whence=0)
        
        @return: on success, current offset location, othwerwise -1
        """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def read(self, size): # real signature unknown; restored from __doc__
        """
        read(size) -> string
        
        @type size: int
        @param size: size of reading
        @return: read data
        """
        return ""

    def seek(self, offset, whence=0): # real signature unknown; restored from __doc__
        """
        seek(offset, whence=0)
        
        @return: on success, current offset location, othwerwise -1
        """
        pass

    def write(self, buf): # real signature unknown; restored from __doc__
        """
        write(buf) -> int
        
        @type buf: string
        @param buf: write data
        @return: size of written
        """
        return 0

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class NoEntryError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class NoSpaceError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class NotDirectoryError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class NotEmptyError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class PermissionError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class TimedOutError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



