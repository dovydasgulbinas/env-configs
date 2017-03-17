# encoding: utf-8
# module gio._gio
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gio/_gio.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
import gio as __gio
import glib as __glib
import gobject as __gobject
import gobject._gobject as __gobject__gobject


# Variables with simple values

APP_INFO_CREATE_NEEDS_TERMINAL = 1

APP_INFO_CREATE_NONE = 0

APP_INFO_CREATE_SUPPORTS_STARTUP_NOTIFICATION = 4

APP_INFO_CREATE_SUPPORTS_URIS = 2

ASK_PASSWORD_ANONYMOUS_SUPPORTED = 16

ASK_PASSWORD_NEED_DOMAIN = 4
ASK_PASSWORD_NEED_PASSWORD = 1
ASK_PASSWORD_NEED_USERNAME = 2

ASK_PASSWORD_SAVING_SUPPORTED = 8

CONVERTER_CONVERTED = 1
CONVERTER_ERROR = 0
CONVERTER_FINISHED = 2
CONVERTER_FLUSH = 2
CONVERTER_FLUSHED = 3

CONVERTER_INPUT_AT_END = 1

CONVERTER_NO_FLAGS = 0

DATA_STREAM_BYTE_ORDER_BIG_ENDIAN = 0

DATA_STREAM_BYTE_ORDER_HOST_ENDIAN = 2

DATA_STREAM_BYTE_ORDER_LITTLE_ENDIAN = 1

DATA_STREAM_NEWLINE_TYPE_ANY = 3
DATA_STREAM_NEWLINE_TYPE_CR = 1

DATA_STREAM_NEWLINE_TYPE_CR_LF = 2

DATA_STREAM_NEWLINE_TYPE_LF = 0

DRIVE_START_NONE = 0

DRIVE_START_STOP_TYPE_MULTIDISK = 3
DRIVE_START_STOP_TYPE_NETWORK = 2
DRIVE_START_STOP_TYPE_PASSWORD = 4
DRIVE_START_STOP_TYPE_SHUTDOWN = 1
DRIVE_START_STOP_TYPE_UNKNOWN = 0

EMBLEM_ORIGIN_DEVICE = 1
EMBLEM_ORIGIN_LIVEMETADATA = 2
EMBLEM_ORIGIN_TAG = 3
EMBLEM_ORIGIN_UNKNOWN = 0

ERROR = 'g-io-error-quark'

ERROR_ADDRESS_IN_USE = 33

ERROR_ALREADY_MOUNTED = 17

ERROR_BROKEN_PIPE = 44

ERROR_BUSY = 26
ERROR_CANCELLED = 19

ERROR_CANT_CREATE_BACKUP = 22

ERROR_CLOSED = 18

ERROR_CONNECTION_CLOSED = 44
ERROR_CONNECTION_REFUSED = 39

ERROR_DBUS_ERROR = 36

ERROR_EXISTS = 2
ERROR_FAILED = 0

ERROR_FAILED_HANDLED = 30

ERROR_FILENAME_TOO_LONG = 9

ERROR_HOST_NOT_FOUND = 28

ERROR_HOST_UNREACHABLE = 37

ERROR_INVALID_ARGUMENT = 13
ERROR_INVALID_DATA = 35
ERROR_INVALID_FILENAME = 10

ERROR_IS_DIRECTORY = 3

ERROR_MESSAGE_TOO_LARGE = 46

ERROR_NETWORK_UNREACHABLE = 38

ERROR_NOT_CONNECTED = 45
ERROR_NOT_DIRECTORY = 4
ERROR_NOT_EMPTY = 5
ERROR_NOT_FOUND = 1
ERROR_NOT_INITIALIZED = 32

ERROR_NOT_MOUNTABLE_FILE = 8

ERROR_NOT_MOUNTED = 16

ERROR_NOT_REGULAR_FILE = 6

ERROR_NOT_SUPPORTED = 15

ERROR_NOT_SYMBOLIC_LINK = 7

ERROR_NO_SPACE = 12

ERROR_PARTIAL_INPUT = 34

ERROR_PENDING = 20

ERROR_PERMISSION_DENIED = 14

ERROR_PROXY_AUTH_FAILED = 41

ERROR_PROXY_FAILED = 40

ERROR_PROXY_NEED_AUTH = 42

ERROR_PROXY_NOT_ALLOWED = 43

ERROR_READ_ONLY = 21

ERROR_TIMED_OUT = 24

ERROR_TOO_MANY_LINKS = 11

ERROR_TOO_MANY_OPEN_FILES = 31

ERROR_WOULD_BLOCK = 27
ERROR_WOULD_MERGE = 29
ERROR_WOULD_RECURSE = 25

ERROR_WRONG_ETAG = 23

FILESYSTEM_PREVIEW_TYPE_IF_ALWAYS = 0
FILESYSTEM_PREVIEW_TYPE_IF_LOCAL = 1

FILESYSTEM_PREVIEW_TYPE_NEVER = 2

FILE_ATTRIBUTE_ACCESS_CAN_DELETE = 'access::can-delete'
FILE_ATTRIBUTE_ACCESS_CAN_EXECUTE = 'access::can-execute'
FILE_ATTRIBUTE_ACCESS_CAN_READ = 'access::can-read'
FILE_ATTRIBUTE_ACCESS_CAN_RENAME = 'access::can-rename'
FILE_ATTRIBUTE_ACCESS_CAN_TRASH = 'access::can-trash'
FILE_ATTRIBUTE_ACCESS_CAN_WRITE = 'access::can-write'

FILE_ATTRIBUTE_DOS_IS_ARCHIVE = 'dos::is-archive'
FILE_ATTRIBUTE_DOS_IS_SYSTEM = 'dos::is-system'

FILE_ATTRIBUTE_ETAG_VALUE = 'etag::value'

FILE_ATTRIBUTE_FILESYSTEM_FREE = 'filesystem::free'
FILE_ATTRIBUTE_FILESYSTEM_READONLY = 'filesystem::readonly'
FILE_ATTRIBUTE_FILESYSTEM_SIZE = 'filesystem::size'
FILE_ATTRIBUTE_FILESYSTEM_TYPE = 'filesystem::type'

FILE_ATTRIBUTE_FILESYSTEM_USE_PREVIEW = 'filesystem::use-preview'

FILE_ATTRIBUTE_GVFS_BACKEND = 'gvfs::backend'

FILE_ATTRIBUTE_ID_FILE = 'id::file'
FILE_ATTRIBUTE_ID_FILESYSTEM = 'id::filesystem'

FILE_ATTRIBUTE_INFO_COPY_WHEN_MOVED = 2

FILE_ATTRIBUTE_INFO_COPY_WITH_FILE = 1

FILE_ATTRIBUTE_INFO_NONE = 0

FILE_ATTRIBUTE_MOUNTABLE_CAN_EJECT = 'mountable::can-eject'
FILE_ATTRIBUTE_MOUNTABLE_CAN_MOUNT = 'mountable::can-mount'
FILE_ATTRIBUTE_MOUNTABLE_CAN_UNMOUNT = 'mountable::can-unmount'

FILE_ATTRIBUTE_MOUNTABLE_HAL_UDI = 'mountable::hal-udi'

FILE_ATTRIBUTE_MOUNTABLE_UNIX_DEVICE = 'mountable::unix-device'

FILE_ATTRIBUTE_OWNER_GROUP = 'owner::group'
FILE_ATTRIBUTE_OWNER_USER = 'owner::user'

FILE_ATTRIBUTE_OWNER_USER_REAL = 'owner::user-real'

FILE_ATTRIBUTE_SELINUX_CONTEXT = 'selinux::context'

FILE_ATTRIBUTE_STANDARD_CONTENT_TYPE = 'standard::content-type'

FILE_ATTRIBUTE_STANDARD_COPY_NAME = 'standard::copy-name'

FILE_ATTRIBUTE_STANDARD_DESCRIPTION = 'standard::description'

FILE_ATTRIBUTE_STANDARD_DISPLAY_NAME = 'standard::display-name'

FILE_ATTRIBUTE_STANDARD_EDIT_NAME = 'standard::edit-name'

FILE_ATTRIBUTE_STANDARD_FAST_CONTENT_TYPE = 'standard::fast-content-type'

FILE_ATTRIBUTE_STANDARD_ICON = 'standard::icon'

FILE_ATTRIBUTE_STANDARD_IS_BACKUP = 'standard::is-backup'
FILE_ATTRIBUTE_STANDARD_IS_HIDDEN = 'standard::is-hidden'
FILE_ATTRIBUTE_STANDARD_IS_SYMLINK = 'standard::is-symlink'
FILE_ATTRIBUTE_STANDARD_IS_VIRTUAL = 'standard::is-virtual'

FILE_ATTRIBUTE_STANDARD_NAME = 'standard::name'
FILE_ATTRIBUTE_STANDARD_SIZE = 'standard::size'

FILE_ATTRIBUTE_STANDARD_SORT_ORDER = 'standard::sort-order'

FILE_ATTRIBUTE_STANDARD_SYMLINK_TARGET = 'standard::symlink-target'

FILE_ATTRIBUTE_STANDARD_TARGET_URI = 'standard::target-uri'

FILE_ATTRIBUTE_STANDARD_TYPE = 'standard::type'

FILE_ATTRIBUTE_STATUS_ERROR_SETTING = 2

FILE_ATTRIBUTE_STATUS_SET = 1
FILE_ATTRIBUTE_STATUS_UNSET = 0

FILE_ATTRIBUTE_THUMBNAILING_FAILED = 'thumbnail::failed'

FILE_ATTRIBUTE_THUMBNAIL_PATH = 'thumbnail::path'

FILE_ATTRIBUTE_TIME_ACCESS = 'time::access'

FILE_ATTRIBUTE_TIME_ACCESS_USEC = 'time::access-usec'

FILE_ATTRIBUTE_TIME_CHANGED = 'time::changed'

FILE_ATTRIBUTE_TIME_CHANGED_USEC = 'time::changed-usec'

FILE_ATTRIBUTE_TIME_CREATED = 'time::created'

FILE_ATTRIBUTE_TIME_CREATED_USEC = 'time::created-usec'

FILE_ATTRIBUTE_TIME_MODIFIED = 'time::modified'

FILE_ATTRIBUTE_TIME_MODIFIED_USEC = 'time::modified-usec'

FILE_ATTRIBUTE_TRASH_ITEM_COUNT = 'trash::item-count'

FILE_ATTRIBUTE_TYPE_BOOLEAN = 3

FILE_ATTRIBUTE_TYPE_BYTE_STRING = 2

FILE_ATTRIBUTE_TYPE_INT32 = 5
FILE_ATTRIBUTE_TYPE_INT64 = 7
FILE_ATTRIBUTE_TYPE_INVALID = 0
FILE_ATTRIBUTE_TYPE_OBJECT = 8
FILE_ATTRIBUTE_TYPE_STRING = 1
FILE_ATTRIBUTE_TYPE_STRINGV = 9
FILE_ATTRIBUTE_TYPE_UINT32 = 4
FILE_ATTRIBUTE_TYPE_UINT64 = 6

FILE_ATTRIBUTE_UNIX_BLOCKS = 'unix::blocks'

FILE_ATTRIBUTE_UNIX_BLOCK_SIZE = 'unix::block-size'

FILE_ATTRIBUTE_UNIX_DEVICE = 'unix::device'
FILE_ATTRIBUTE_UNIX_GID = 'unix::gid'
FILE_ATTRIBUTE_UNIX_INODE = 'unix::inode'

FILE_ATTRIBUTE_UNIX_IS_MOUNTPOINT = 'unix::is-mountpoint'

FILE_ATTRIBUTE_UNIX_MODE = 'unix::mode'
FILE_ATTRIBUTE_UNIX_NLINK = 'unix::nlink'
FILE_ATTRIBUTE_UNIX_RDEV = 'unix::rdev'
FILE_ATTRIBUTE_UNIX_UID = 'unix::uid'

FILE_COPY_ALL_METADATA = 8

FILE_COPY_BACKUP = 2

FILE_COPY_NOFOLLOW_SYMLINKS = 4

FILE_COPY_NONE = 0

FILE_COPY_NO_FALLBACK_FOR_MOVE = 16

FILE_COPY_OVERWRITE = 1

FILE_COPY_TARGET_DEFAULT_PERMS = 32

FILE_CREATE_NONE = 0
FILE_CREATE_PRIVATE = 1

FILE_CREATE_REPLACE_DESTINATION = 2

FILE_MONITOR_EVENT_ATTRIBUTE_CHANGED = 4

FILE_MONITOR_EVENT_CHANGED = 0

FILE_MONITOR_EVENT_CHANGES_DONE_HINT = 1

FILE_MONITOR_EVENT_CREATED = 3
FILE_MONITOR_EVENT_DELETED = 2
FILE_MONITOR_EVENT_MOVED = 7

FILE_MONITOR_EVENT_MOVED_IN = 9
FILE_MONITOR_EVENT_MOVED_OUT = 10

FILE_MONITOR_EVENT_PRE_UNMOUNT = 5

FILE_MONITOR_EVENT_RENAMED = 8
FILE_MONITOR_EVENT_UNMOUNTED = 6

FILE_MONITOR_NONE = 0

FILE_MONITOR_SEND_MOVED = 2

FILE_MONITOR_WATCH_HARD_LINKS = 4

FILE_MONITOR_WATCH_MOUNTS = 1
FILE_MONITOR_WATCH_MOVES = 8

FILE_QUERY_INFO_NOFOLLOW_SYMLINKS = 1

FILE_QUERY_INFO_NONE = 0

FILE_TYPE_DIRECTORY = 2
FILE_TYPE_MOUNTABLE = 6
FILE_TYPE_REGULAR = 1
FILE_TYPE_SHORTCUT = 5
FILE_TYPE_SPECIAL = 4

FILE_TYPE_SYMBOLIC_LINK = 3

FILE_TYPE_UNKNOWN = 0

MOUNT_MOUNT_NONE = 0

MOUNT_OPERATION_ABORTED = 1
MOUNT_OPERATION_HANDLED = 0
MOUNT_OPERATION_UNHANDLED = 2

MOUNT_UNMOUNT_FORCE = 1
MOUNT_UNMOUNT_NONE = 0

OUTPUT_STREAM_SPLICE_CLOSE_SOURCE = 1
OUTPUT_STREAM_SPLICE_CLOSE_TARGET = 2

OUTPUT_STREAM_SPLICE_NONE = 0

PASSWORD_SAVE_FOR_SESSION = 1

PASSWORD_SAVE_NEVER = 0
PASSWORD_SAVE_PERMANENTLY = 2

RESOLVER_ERROR_INTERNAL = 2

RESOLVER_ERROR_NOT_FOUND = 0

RESOLVER_ERROR_TEMPORARY_FAILURE = 1

SOCKET_FAMILY_INVALID = 0
SOCKET_FAMILY_IPV4 = 2
SOCKET_FAMILY_IPV6 = 10
SOCKET_FAMILY_UNIX = 1

SOCKET_MSG_DONTROUTE = 4
SOCKET_MSG_NONE = 0
SOCKET_MSG_OOB = 1
SOCKET_MSG_PEEK = 2

SOCKET_PROTOCOL_DEFAULT = 0
SOCKET_PROTOCOL_SCTP = 132
SOCKET_PROTOCOL_TCP = 6
SOCKET_PROTOCOL_UDP = 17
SOCKET_PROTOCOL_UNKNOWN = -1

SOCKET_TYPE_DATAGRAM = 2
SOCKET_TYPE_INVALID = 0
SOCKET_TYPE_SEQPACKET = 3
SOCKET_TYPE_STREAM = 1

ZLIB_COMPRESSOR_FORMAT_GZIP = 1
ZLIB_COMPRESSOR_FORMAT_RAW = 2
ZLIB_COMPRESSOR_FORMAT_ZLIB = 0

# functions

def app_info_get_all(*args, **kwargs): # real signature unknown
    pass

def app_info_get_all_for_type(*args, **kwargs): # real signature unknown
    pass

def app_info_get_default_for_type(*args, **kwargs): # real signature unknown
    pass

def app_info_get_default_for_uri_scheme(*args, **kwargs): # real signature unknown
    pass

def app_info_reset_type_associations(*args, **kwargs): # real signature unknown
    pass

def buffered_input_stream_new_sized(*args, **kwargs): # real signature unknown
    pass

def buffered_output_stream_new_sized(*args, **kwargs): # real signature unknown
    pass

def cancellable_get_current(*args, **kwargs): # real signature unknown
    pass

def content_types_get_registered(*args, **kwargs): # real signature unknown
    pass

def content_type_can_be_executable(*args, **kwargs): # real signature unknown
    pass

def content_type_equals(*args, **kwargs): # real signature unknown
    pass

def content_type_from_mime_type(*args, **kwargs): # real signature unknown
    pass

def content_type_get_description(*args, **kwargs): # real signature unknown
    pass

def content_type_get_icon(*args, **kwargs): # real signature unknown
    pass

def content_type_get_mime_type(*args, **kwargs): # real signature unknown
    pass

def content_type_guess(filename=None, data=None, want_uncertain=None): # real signature unknown; restored from __doc__
    """
    content_type_guess([filename, data, want_uncertain]) -> mime type
    
    Guesses the content type based on the parameters passed.
    Either filename or data must be specified
    Returns a string containing the mime type.
    If want_uncertain is set to True, return a tuple with the mime type and 
    True/False if the type guess was uncertain or not.
    """
    pass

def content_type_is_a(*args, **kwargs): # real signature unknown
    pass

def content_type_is_unknown(*args, **kwargs): # real signature unknown
    pass

def emblem_new_with_origin(*args, **kwargs): # real signature unknown
    pass

def file_parse_name(*args, **kwargs): # real signature unknown
    pass

def icon_new_for_string(*args, **kwargs): # real signature unknown
    pass

def inet_address_new_any(*args, **kwargs): # real signature unknown
    pass

def inet_address_new_from_bytes(*args, **kwargs): # real signature unknown
    pass

def inet_address_new_from_string(*args, **kwargs): # real signature unknown
    pass

def inet_address_new_loopback(*args, **kwargs): # real signature unknown
    pass

def io_error_from_errno(*args, **kwargs): # real signature unknown
    pass

def memory_input_stream_new_from_data(*args, **kwargs): # real signature unknown
    pass

def network_address_parse(*args, **kwargs): # real signature unknown
    pass

def resolver_get_default(*args, **kwargs): # real signature unknown
    pass

def socket_connection_factory_lookup_type(*args, **kwargs): # real signature unknown
    pass

def socket_connection_factory_register_type(*args, **kwargs): # real signature unknown
    pass

def socket_new_from_fd(*args, **kwargs): # real signature unknown
    pass

def vfs_get_default(*args, **kwargs): # real signature unknown
    pass

def vfs_get_local(*args, **kwargs): # real signature unknown
    pass

def volume_monitor_adopt_orphan_mount(*args, **kwargs): # real signature unknown
    pass

def volume_monitor_get(*args, **kwargs): # real signature unknown
    pass

def _app_info_init(*args, **kwargs): # real signature unknown
    pass

def _file_init(*args, **kwargs): # real signature unknown
    pass

def _install_app_info_meta(*args, **kwargs): # real signature unknown
    pass

def _install_file_meta(*args, **kwargs): # real signature unknown
    pass

# classes

from AppInfo import AppInfo
from AppInfoCreateFlags import AppInfoCreateFlags
from AppLaunchContext import AppLaunchContext
from AskPasswordFlags import AskPasswordFlags
from AsyncInitable import AsyncInitable
from AsyncResult import AsyncResult
from InputStream import InputStream
from FilterInputStream import FilterInputStream
from Seekable import Seekable
from BufferedInputStream import BufferedInputStream
from OutputStream import OutputStream
from FilterOutputStream import FilterOutputStream
from BufferedOutputStream import BufferedOutputStream
from Cancellable import Cancellable
from ConverterFlags import ConverterFlags
from ConverterResult import ConverterResult
from DataInputStream import DataInputStream
from DataOutputStream import DataOutputStream
from DataStreamByteOrder import DataStreamByteOrder
from DataStreamNewlineType import DataStreamNewlineType
from Drive import Drive
from DriveStartFlags import DriveStartFlags
from DriveStartStopType import DriveStartStopType
from Icon import Icon
from Emblem import Emblem
from EmblemedIcon import EmblemedIcon
from EmblemOrigin import EmblemOrigin
from Error import Error
from ErrorEnum import ErrorEnum
from File import File
from FileAttributeInfo import FileAttributeInfo
from FileAttributeInfoFlags import FileAttributeInfoFlags
from FileAttributeMatcher import FileAttributeMatcher
from FileAttributeStatus import FileAttributeStatus
from FileAttributeType import FileAttributeType
from FileCopyFlags import FileCopyFlags
from FileCreateFlags import FileCreateFlags
from FileEnumerator import FileEnumerator
from LoadableIcon import LoadableIcon
from FileIcon import FileIcon
from FileInfo import FileInfo
from FileInputStream import FileInputStream
from IOStream import IOStream
from FileIOStream import FileIOStream
from FileMonitor import FileMonitor
from FileMonitorEvent import FileMonitorEvent
from FileMonitorFlags import FileMonitorFlags
from FileOutputStream import FileOutputStream
from FileQueryInfoFlags import FileQueryInfoFlags
from FilesystemPreviewType import FilesystemPreviewType
from FileType import FileType
from InetAddress import InetAddress
from SocketConnectable import SocketConnectable
from SocketAddress import SocketAddress
from InetSocketAddress import InetSocketAddress
from Initable import Initable
from MemoryInputStream import MemoryInputStream
from MemoryOutputStream import MemoryOutputStream
from Mount import Mount
from MountMountFlags import MountMountFlags
from MountOperation import MountOperation
from MountOperationResult import MountOperationResult
from MountUnmountFlags import MountUnmountFlags
from VolumeMonitor import VolumeMonitor
from NativeVolumeMonitor import NativeVolumeMonitor
from NetworkAddress import NetworkAddress
from NetworkService import NetworkService
from OutputStreamSpliceFlags import OutputStreamSpliceFlags
from PasswordSave import PasswordSave
from Resolver import Resolver
from ResolverError import ResolverError
from SimpleAsyncResult import SimpleAsyncResult
from Socket import Socket
from SocketAddressEnumerator import SocketAddressEnumerator
from SocketClient import SocketClient
from SocketConnection import SocketConnection
from SocketControlMessage import SocketControlMessage
from SocketFamily import SocketFamily
from SocketListener import SocketListener
from SocketMsgFlags import SocketMsgFlags
from SocketProtocol import SocketProtocol
from SocketService import SocketService
from SocketType import SocketType
from SrvTarget import SrvTarget
from TcpConnection import TcpConnection
from ThemedIcon import ThemedIcon
from ThreadedSocketService import ThreadedSocketService
from Vfs import Vfs
from Volume import Volume
from ZlibCompressorFormat import ZlibCompressorFormat
# variables with complex values

pygio_version = (
    2,
    28,
    6,
)

