# encoding: utf-8
# module gio.unix
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gio/unix.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject


# functions

def desktop_app_info_new_from_filename(*args, **kwargs): # real signature unknown
    pass

def desktop_app_info_set_desktop_env(*args, **kwargs): # real signature unknown
    pass

def g_unix_socket_address_abstract_names_supported(*args, **kwargs): # real signature unknown
    pass

def g_unix_socket_address_new_abstract(*args, **kwargs): # real signature unknown
    pass

def unix_is_mount_path_system_internal(*args, **kwargs): # real signature unknown
    pass

def unix_mounts_changed_since(*args, **kwargs): # real signature unknown
    pass

def unix_mount_compare(*args, **kwargs): # real signature unknown
    pass

def unix_mount_free(*args, **kwargs): # real signature unknown
    pass

def unix_mount_get_device_path(*args, **kwargs): # real signature unknown
    pass

def unix_mount_get_fs_type(*args, **kwargs): # real signature unknown
    pass

def unix_mount_get_mount_path(*args, **kwargs): # real signature unknown
    pass

def unix_mount_guess_can_eject(*args, **kwargs): # real signature unknown
    pass

def unix_mount_guess_icon(*args, **kwargs): # real signature unknown
    pass

def unix_mount_guess_name(*args, **kwargs): # real signature unknown
    pass

def unix_mount_guess_should_display(*args, **kwargs): # real signature unknown
    pass

def unix_mount_is_readonly(*args, **kwargs): # real signature unknown
    pass

def unix_mount_is_system_internal(*args, **kwargs): # real signature unknown
    pass

def unix_mount_points_changed_since(*args, **kwargs): # real signature unknown
    pass

# classes

class Connection(__gio.SocketConnection):
    """
    Object GUnixConnection
    
    Properties from GSocketConnection:
      socket -> GSocket: Socket
        The underlying GSocket
    
    Properties from GIOStream:
      input-stream -> GInputStream: Input stream
        The GInputStream to read from
      output-stream -> GOutputStream: Output stream
        The GOutputStream to write to
      closed -> gboolean: Closed
        Is the stream closed
    
    Signals from GObject:
      notify (GParam)
    """
    def receive_fd(self, *args, **kwargs): # real signature unknown
        pass

    def send_fd(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class DesktopAppInfo(__gobject__gobject.GObject, __gio.AppInfo):
    """
    Object GDesktopAppInfo
    
    DesktopAppInfo(desktop_id) -> gio.unix.DesktopAppInfo
    
    gio.Unix.DesktopAppInfo is an implementation of gio.AppInfo
    based on desktop files.
    
    Properties from GDesktopAppInfo:
      filename -> gchararray: Filename
        
    
    Signals from GObject:
      notify (GParam)
    """
    def get_is_hidden(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, desktop_id): # real signature unknown; restored from __doc__
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __gtype__ = None # (!) real value is ''


class FDMessage(__gio.SocketControlMessage):
    """
    Object GUnixFDMessage
    
    Properties from GUnixFDMessage:
      fd-list -> GUnixFDList: file descriptor list
        The GUnixFDList object to send with the message
    
    Signals from GObject:
      notify (GParam)
    """
    def append_fd(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class InputStream(__gio.InputStream, __gio.__main__.GPollableInputStream, __gio.__main__.GFileDescriptorBased):
    """
    Object GUnixInputStream
    
    Properties from GUnixInputStream:
      fd -> gint: File descriptor
        The file descriptor to read from
      close-fd -> gboolean: Close file descriptor
        Whether to close the file descriptor when the stream is closed
    
    Signals from GObject:
      notify (GParam)
    """
    def get_close_fd(self, *args, **kwargs): # real signature unknown
        pass

    def get_fd(self, *args, **kwargs): # real signature unknown
        pass

    def set_close_fd(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class MountEntry(__gobject.GPointer):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class OutputStream(__gio.OutputStream, __gio.__main__.GPollableOutputStream, __gio.__main__.GFileDescriptorBased):
    """
    Object GUnixOutputStream
    
    Properties from GUnixOutputStream:
      fd -> gint: File descriptor
        The file descriptor to write to
      close-fd -> gboolean: Close file descriptor
        Whether to close the file descriptor when the stream is closed
    
    Signals from GObject:
      notify (GParam)
    """
    def get_close_fd(self, *args, **kwargs): # real signature unknown
        pass

    def get_fd(self, *args, **kwargs): # real signature unknown
        pass

    def set_close_fd(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class SocketAddress(__gio.SocketAddress):
    """
    Object GUnixSocketAddress
    
    Properties from GUnixSocketAddress:
      path -> gchararray: Path
        UNIX socket path
      path-as-array -> GByteArray: Path array
        UNIX socket path, as byte array
      abstract -> gboolean: Abstract
        Whether or not this is an abstract address
      address-type -> GUnixSocketAddressType: Address type
        The type of UNIX socket address
    
    Properties from GSocketAddress:
      family -> GSocketFamily: Address family
        The family of the socket address
    
    Signals from GObject:
      notify (GParam)
    """
    def get_is_abstract(self, *args, **kwargs): # real signature unknown
        pass

    def get_path(self, *args, **kwargs): # real signature unknown
        pass

    def get_path_len(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


