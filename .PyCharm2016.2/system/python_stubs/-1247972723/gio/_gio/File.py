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


class File(__gobject.GInterface):
    """
    File(arg, path=None, uri=None) -> gio.File subclass
    
    If arg is specified; creates a GFile with the given argument from the
    command line.  The value of arg can be either a URI, an absolute path
    or a relative path resolved relative to the current working directory.
    If path is specified, create a file from an absolute or relative path.
    If uri is specified, create a file from a URI.
    
    This operation never fails, but the returned object might not 
    support any I/O operation if arg points to a malformed path.
    """
    def append_to(self, *args, **kwargs): # real signature unknown
        pass

    def append_to_async(self, callback, flags=None, io_priority=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.append_to_async(callback [flags, [,io_priority [,cancellable
                          [,user_data]]]]) -> open for append
        
        Asynchronously opens file for appending.
        For more details, see gio.File.append_to() which is the synchronous
        version of this call. When the operation is finished, callback will
        be called. You can then call F.append_to_finish() to get the result
        of the operation.
        """
        pass

    def append_to_finish(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, destination, callback=None, flags=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.copy(destination, [callback, flags, cancellable, user_data])
        Copies the file source to the location specified by destination.
        Can not handle recursive copies of directories.
        
        If the flag gio.FILE_COPY_OVERWRITE is specified an already existing
        destination file is overwritten.
        
        If the flag gio.FILE_COPY_NOFOLLOW_SYMLINKS is specified then symlink
        will be copied as symlinks, otherwise the target of the source symlink
        will be copied.
        
        If cancellable is not None, then the operation can be cancelled b
        triggering the cancellable object from another thread.
        If the operation was cancelled, the error gio.ERROR_CANCELLED
        will be returned.
        
        If progress_callback is not None, then the operation can be monitored
        by setting this to a callable. if specified progress_callback_data will
        be passed to this function. It is guaranteed that this callback
        will be called after all data has been transferred with the total number
        of bytes copied during the operation.
        
        If the source file does not exist then the gio.ERROR_NOT_FOUND
        error is returned, independent on the status of the destination.
        
        If gio.FILE_COPY_OVERWRITE is not specified and the target exists
        then the error gio.ERROR_EXISTS is returned.
        
        If trying to overwrite a file over a directory the gio.ERROR_IS_DIRECTORY
        error is returned. If trying to overwrite a directory with a directory
        the gio.ERROR_WOULD_MERGE error is returned.
        
        If the source is a directory and the target does not exist
        or gio.FILE_COPY_OVERWRITE is specified and the target is a file
        then the gio.ERROR_WOULD_RECURSE error is returned.
        
        If you are interested in copying the GFile object itself
        (not the on-disk file), see gio.File.dup().
        """
        pass

    def copy_async(self, destination, callback, flags=None, io_priority=None, user_data=None, cancellable=None, progress_callback=None): # real signature unknown; restored from __doc__
        """
        F.copy_async(destination, callback, [flags, io_priority, user_data, cancellable, progress_callback])
        -> start copy
        
        For more details, see gio.File.copy() which is the synchronous
        version of this call. Asynchronously copies file.
        When the operation is finished, callback will be called.
        You can then call g_file_copy_finish() to get the result of the
        operation.
        """
        pass

    def copy_attributes(self, *args, **kwargs): # real signature unknown
        pass

    def copy_finish(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def create_async(self, callback, flags=None, io_priority=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.create_async(callback [flags, [,io_priority [,cancellable
                       [,user_data]]]]) -> file created
        
        Asynchronously creates a new file and returns an output stream for
        writing to it. The file must not already exist.
        For more details, see F.create() which is the synchronous
        version of this call.
        When the operation is finished, callback will be called. You can
        then call F.create_finish() to get the result of the operation.
        """
        return file('/dev/null')

    def create_finish(self, *args, **kwargs): # real signature unknown
        pass

    def create_readwrite(self, *args, **kwargs): # real signature unknown
        pass

    def create_readwrite_async(self, *args, **kwargs): # real signature unknown
        pass

    def create_readwrite_finish(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self, *args, **kwargs): # real signature unknown
        pass

    def eject_mountable(self, *args, **kwargs): # real signature unknown
        pass

    def eject_mountable_finish(self, *args, **kwargs): # real signature unknown
        pass

    def eject_mountable_with_operation(self, *args, **kwargs): # real signature unknown
        pass

    def eject_mountable_with_operation_finish(self, *args, **kwargs): # real signature unknown
        pass

    def enumerate_children(self, attributes, flags=None, cancellable=None): # real signature unknown; restored from __doc__
        """
        F.enumerate_children(attributes, [flags, cancellable]) -> enumerator
        Gets the requested information about the files in a directory.
        The result is a gio.FileEnumerator object that will give out gio.FileInfo
        objects for all the files in the directory.
        The attribute value is a string that specifies the file attributes that
        should be gathered. It is not an error if it's not possible to read a 
        particular requested attribute from a file - it just won't be set.
        attribute should be a comma-separated list of attribute or attribute
        wildcards. The wildcard "*" means all attributes, and a wildcard like
        "standard::*" means all attributes in the standard namespace.
        An example attribute query be "standard::*,owner::user". The standard
        attributes are available as defines, like gio.FILE_ATTRIBUTE_STANDARD_NAME.
        
        If cancellable is not None, then the operation can be cancelled by
        triggering the cancellable object from another thread. If the operation was
        cancelled, the error gio.ERROR_CANCELLED will be returned.
        
        If the file does not exist, the gio.ERROR_NOT_FOUND error will be returned.
        If the file is not a directory, the gio.FILE_ERROR_NOTDIR error will
        be returned. Other errors are possible too.
        """
        pass

    def enumerate_children_async(self, attributes, callback, flags=None, io_priority=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.enumerate_children_async(attributes, callback,
                                   [flags, io_priority, cancellable, user_data])
        Asynchronously gets the requested information about the files in a
        directory. The result is a GFileEnumerator object that will give out
        GFileInfo objects for all the files in the directory.
        
        For more details, see gio.File.enumerate_children() which is the synchronous
        version of this call.
        
        When the operation is finished, callback will be called. You can then call
        gio.File.enumerate_children_finish() to get the result of the operation.
        """
        pass

    def enumerate_children_finish(self, *args, **kwargs): # real signature unknown
        pass

    def equal(self, *args, **kwargs): # real signature unknown
        pass

    def find_enclosing_mount(self, *args, **kwargs): # real signature unknown
        pass

    def find_enclosing_mount_async(self, *args, **kwargs): # real signature unknown
        pass

    def find_enclosing_mount_finish(self, *args, **kwargs): # real signature unknown
        pass

    def get_basename(self, *args, **kwargs): # real signature unknown
        pass

    def get_child(self, *args, **kwargs): # real signature unknown
        pass

    def get_child_for_display_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_parse_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_path(self, *args, **kwargs): # real signature unknown
        pass

    def get_relative_path(self, *args, **kwargs): # real signature unknown
        pass

    def get_uri(self, *args, **kwargs): # real signature unknown
        pass

    def get_uri_scheme(self, *args, **kwargs): # real signature unknown
        pass

    def has_prefix(self, *args, **kwargs): # real signature unknown
        pass

    def has_uri_scheme(self, *args, **kwargs): # real signature unknown
        pass

    def is_native(self, *args, **kwargs): # real signature unknown
        pass

    def load_contents(self, cancellable=None): # real signature unknown; restored from __doc__
        """
        F.load_contents([cancellable]) -> contents, length, etag_out
        
        Loads the content of the file into memory, returning the size of the
        data. The data is always zero terminated, but this is not included
        in the resultant length.
        If cancellable is not None, then the operation can be cancelled by
        triggering the cancellable object from another thread. If the operation
        was cancelled, the error gio.IO_ERROR_CANCELLED will be returned.
        """
        pass

    def load_contents_async(self, callback, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.load_contents_async(callback, [cancellable, [user_data]])->start loading
        
        Starts an asynchronous load of the file's contents.
        
        For more details, see F.load_contents() which is the synchronous
        version of this call.
        
        When the load operation has completed, callback will be called with
        user data. To finish the operation, call F.load_contents_finish() with
        the parameter 'res' returned by the callback.
        
        If cancellable is not None, then the operation can be cancelled by
        triggering the cancellable object from another thread. If the operation
        was cancelled, the error gio.IO_ERROR_CANCELLED will be returned.
        """
        pass

    def load_contents_finish(self, res): # real signature unknown; restored from __doc__
        """
        F.load_contents_finish(res) -> contents, length, etag_out
        
        Finishes an asynchronous load of the file's contents. The contents are
        placed in contents, and length is set to the size of the contents
        string. If etag_out is present, it will be set to the new entity
        tag for the file.
        """
        pass

    def make_directory(self, *args, **kwargs): # real signature unknown
        pass

    def make_directory_with_parents(self, *args, **kwargs): # real signature unknown
        pass

    def make_symbolic_link(self, *args, **kwargs): # real signature unknown
        pass

    def monitor(self, *args, **kwargs): # real signature unknown
        pass

    def monitor_directory(self, *args, **kwargs): # real signature unknown
        pass

    def monitor_file(self, *args, **kwargs): # real signature unknown
        pass

    def mount_enclosing_volume(self, mount_operation, callback, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.mount_enclosing_volume(mount_operation, callback, [cancellable,
                                 user_data])
        Starts a mount_operation, mounting the volume that contains
        the file location.
        
        When this operation has completed, callback will be called with
        user_user data, and the operation can be finalized with
        gio.File.mount_enclosing_volume_finish().
        
        If cancellable is not None, then the operation can be cancelled
        by triggering the cancellable object from another thread.
        If the operation was cancelled, the error gio.ERROR_CANCELLED
        will be returned.
        """
        pass

    def mount_enclosing_volume_finish(self, *args, **kwargs): # real signature unknown
        pass

    def mount_mountable(self, mount_operation, callback, flags=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.mount_mountable(mount_operation, callback, [flags, cancellable,
                          user_data])
        Mounts a file of type gio.FILE_TYPE_MOUNTABLE. Using mount_operation,
        you can request callbacks when, for instance, passwords are needed
        during authentication.
        
        If cancellable is not None, then the operation can be cancelled by
         triggering the cancellable object from another thread. If the
        operation was cancelled, the error gio.ERROR_CANCELLED will be returned.
        
        When the operation is finished, callback will be called. You can then
        call g_file_mount_mountable_finish() to get the result of the operation.
        """
        pass

    def mount_mountable_finish(self, *args, **kwargs): # real signature unknown
        pass

    def move(self, destination, callback=None, flags=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.move(destination, [callback, flags, cancellable, user_data])
        Tries to move the file or directory source to the location
        specified by destination. If native move operations are
        supported then this is used, otherwise a copy + delete fallback
        is used. The native implementation may support moving directories
        (for instance on moves inside the same filesystem), but the 
        fallback code does not.
        
        If the flag gio.FILE_COPY_OVERWRITE is specified an already existing
        destination file is overwritten.
        
        If the flag gio.FILE_COPY_NOFOLLOW_SYMLINKS is specified then symlink
        will be copied as symlinks, otherwise the target of the source symlink
        will be copied.
        
        If cancellable is not None, then the operation can be cancelled b
        triggering the cancellable object from another thread.
        If the operation was cancelled, the error gio.ERROR_CANCELLED
        will be returned.
        
        If progress_callback is not None, then the operation can be monitored
        by setting this to a callable. if specified progress_callback_data will
        be passed to this function. It is guaranteed that this callback
        will be called after all data has been transferred with the total number
        of bytes copied during the operation.
        
        If the source file does not exist then the gio.ERROR_NOT_FOUND
        error is returned, independent on the status of the destination.
        
        If gio.FILE_COPY_OVERWRITE is not specified and the target exists
        then the error gio.ERROR_EXISTS is returned.
        
        If trying to overwrite a file over a directory the gio.ERROR_IS_DIRECTORY
        error is returned. If trying to overwrite a directory with a directory
        the gio.ERROR_WOULD_MERGE error is returned.
        
        If the source is a directory and the target does not exist
        or gio.FILE_COPY_OVERWRITE is specified and the target is a file
        then the gio.ERROR_WOULD_RECURSE error is returned.
        """
        pass

    def open_readwrite(self, *args, **kwargs): # real signature unknown
        pass

    def open_readwrite_async(self, *args, **kwargs): # real signature unknown
        pass

    def open_readwrite_finish(self, *args, **kwargs): # real signature unknown
        pass

    def poll_mountable(self, *args, **kwargs): # real signature unknown
        pass

    def poll_mountable_finish(self, *args, **kwargs): # real signature unknown
        pass

    def query_default_handler(self, *args, **kwargs): # real signature unknown
        pass

    def query_exists(self, *args, **kwargs): # real signature unknown
        pass

    def query_filesystem_info(self, *args, **kwargs): # real signature unknown
        pass

    def query_filesystem_info_async(self, *args, **kwargs): # real signature unknown
        pass

    def query_filesystem_info_finish(self, *args, **kwargs): # real signature unknown
        pass

    def query_file_type(self, *args, **kwargs): # real signature unknown
        pass

    def query_info(self, *args, **kwargs): # real signature unknown
        pass

    def query_info_async(self, attributes, callback, flags=None, io_priority=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.query_info_async(attributes, callback, [flags, [io_priority,
                           [cancellable, [user_data]]]]) -> query attributes
        
        Asynchronously gets the requested information about specified file.
        The result is a GFileInfo object that contains key-value attributes
        (such as type or size for the file).
        For more details, see F.query_info() which is the synchronous
        version of this call. 
        When the operation is finished, callback will be called. You can
        then call F.query_info_finish() to get the result of the operation.
        """
        pass

    def query_info_finish(self, *args, **kwargs): # real signature unknown
        pass

    def query_settable_attributes(self, cancellable=None): # real signature unknown; restored from __doc__
        """
        F.query_settable_attributes([cancellable]) -> list
        
        Obtain the list of settable attributes for the file.
        Returns the type and full attribute name of all the attributes that
        can be set on this file. This doesn't mean setting it will always
        succeed though, you might get an access failure, or some specific
        file may not support a specific attribute.
        
        If cancellable is not None, then the operation can be cancelled by
        triggering the cancellable object from another thread. If the operation
        was cancelled, the error gio.IO_ERROR_CANCELLED will be returned.
        """
        return []

    def query_writable_namespaces(self, cancellable=None): # real signature unknown; restored from __doc__
        """
        F.query_writable_namespaces([cancellable]) -> list
        
        Obtain the list of attribute namespaces where new attributes can
        be created by a user. An example of this is extended attributes
        (in the xattr namespace).
        If cancellable is not None, then the operation can be cancelled
        by triggering the cancellable object from another thread. If the
        operation was cancelled, the error gio.IO_ERROR_CANCELLED
        will be returned.
        """
        return []

    def read(self, cancellable=None): # real signature unknown; restored from __doc__
        """
        F.read([cancellable]) -> input stream
        Opens a file for reading. The result is a GFileInputStream that
        can be used to read the contents of the file.
        
        If cancellable is specified, then the operation can be cancelled
        by triggering the cancellable object from another thread. If the
        operation was cancelled, the error gio.IO_ERROR_CANCELLED will
        be returned. If the file does not exist, the gio.IO_ERROR_NOT_FOUND
        error will be returned. If the file is a directory, the
        gio.IO_ERROR_IS_DIRECTORY error will be returned. Other errors
        are possible too, and depend on what kind of filesystem the file is on.
        """
        pass

    def read_async(self, callback, io_priority=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.read_async(callback [,io_priority [,cancellable [,user_data]]])
        -> start read
        
        For more details, see gio.File.read() which is the synchronous
        version of this call. Asynchronously opens file for reading.
        When the operation is finished, callback will be called.
        You can then call g_file_read_finish() to get the result of the
        operation.
        """
        pass

    def read_finish(self, *args, **kwargs): # real signature unknown
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        pass

    def replace_async(self, callback, etag=None, make_backup=None, flags=None, io_priority=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.replace_async(callback [etag, [make_backup, [flags, [io_priority,
                        [cancellable, [user_data]]]]]]) -> file replace
        
        Asynchronously overwrites the file, replacing the contents, possibly
        creating a backup copy of the file first.
        For more details, see F.replace() which is the synchronous
        version of this call.
        When the operation is finished, callback will be called. You can
        then call F.replace_finish() to get the result of the operation.
        """
        return file('/dev/null')

    def replace_contents(self, contents, etag=None, make_backup=None, flags=None, cancellable=None): # real signature unknown; restored from __doc__
        """
        F.replace_contents(contents, [etag, [make_backup, [flags, [cancellable]]]])
        -> etag_out
        
        Replaces the content of the file, returning the new etag value for the
        file. If an etag is specified, any existing file must have that etag, or
        the error gio.IO_ERROR_WRONG_ETAG will be returned.
        If make_backup is True, this method will attempt to make a backup of the
        file. If cancellable is not None, then the operation can be cancelled by
        triggering the cancellable object from another thread. If the operation
        was cancelled, the error gio.IO_ERROR_CANCELLED will be returned.
        """
        pass

    def replace_contents_async(self, contents, callback, etag=None, make_backup=None, flags=None, cancellable=None): # real signature unknown; restored from __doc__
        """
        F.replace_contents_async(contents, callback, [etag, [make_backup, [flags,
                                 [cancellable]]]]) -> etag_out
        
        Starts an asynchronous replacement of the file with the given contents.
        For more details, see F.replace_contents() which is the synchronous
        version of this call.
        
        When the load operation has completed, callback will be called with
        user data. To finish the operation, call F.replace_contents_finish() with
        the parameter 'res' returned by the callback.
        
        If cancellable is not None, then the operation can be cancelled by
        triggering the cancellable object from another thread. If the operation
        was cancelled, the error gio.IO_ERROR_CANCELLED will be returned.
        """
        pass

    def replace_contents_finish(self, res): # real signature unknown; restored from __doc__
        """
        F.replace_contents_finish(res) -> etag_out
        
        Finishes an asynchronous replacement of the file's contents.
        The new entity tag for the file is returned.
        """
        pass

    def replace_finish(self, *args, **kwargs): # real signature unknown
        pass

    def replace_readwrite(self, *args, **kwargs): # real signature unknown
        pass

    def replace_readwrite_async(self, *args, **kwargs): # real signature unknown
        pass

    def replace_readwrite_finish(self, *args, **kwargs): # real signature unknown
        pass

    def resolve_relative_path(self, *args, **kwargs): # real signature unknown
        pass

    def set_attribute(self, attribute, type, value_p, flags=None, cancellable=None): # real signature unknown; restored from __doc__
        """
        F.set_attribute(attribute, type, value_p [,flags [,cancellable ]])->bool
        
        Sets an attribute in the file with attribute name attribute to value_p.
        If cancellable is not None, then the operation can be cancelled by
        triggering the cancellable object from another thread. If the operation
        was cancelled, the error gio.IO_ERROR_CANCELLED will be returned.
        """
        return False

    def set_attributes_async(self, *args, **kwargs): # real signature unknown
        pass

    def set_attributes_finish(self, *args, **kwargs): # real signature unknown
        pass

    def set_attributes_from_info(self, *args, **kwargs): # real signature unknown
        pass

    def set_attribute_byte_string(self, *args, **kwargs): # real signature unknown
        pass

    def set_attribute_int32(self, *args, **kwargs): # real signature unknown
        pass

    def set_attribute_int64(self, *args, **kwargs): # real signature unknown
        pass

    def set_attribute_string(self, *args, **kwargs): # real signature unknown
        pass

    def set_attribute_uint32(self, *args, **kwargs): # real signature unknown
        pass

    def set_attribute_uint64(self, *args, **kwargs): # real signature unknown
        pass

    def set_display_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_display_name_async(self, *args, **kwargs): # real signature unknown
        pass

    def set_display_name_finish(self, *args, **kwargs): # real signature unknown
        pass

    def start_mountable(self, *args, **kwargs): # real signature unknown
        pass

    def start_mountable_finish(self, *args, **kwargs): # real signature unknown
        pass

    def stop_mountable(self, *args, **kwargs): # real signature unknown
        pass

    def stop_mountable_finish(self, *args, **kwargs): # real signature unknown
        pass

    def supports_thread_contexts(self, *args, **kwargs): # real signature unknown
        pass

    def trash(self, *args, **kwargs): # real signature unknown
        pass

    def unmount_mountable(self, callback, flags=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.unmount_mountable(callback, [flags, cancellable, user_data])
        Unmounts a file of type gio.FILE_TYPE_MOUNTABLE.
        
        If cancellable is not None, then the operation can be cancelled by
        triggering the cancellable object from another thread. If the
        operation was cancelled, the error gio.ERROR_CANCELLED will be returned.
        
        When the operation is finished, callback will be called. You can
        then call gio.File.unmount_mountable_finish() to get the
        result of the operation.
        """
        pass

    def unmount_mountable_finish(self, *args, **kwargs): # real signature unknown
        pass

    def unmount_mountable_with_operation(self, *args, **kwargs): # real signature unknown
        pass

    def unmount_mountable_with_operation_finish(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, arg, path=None, uri=None): # real signature unknown; restored from __doc__
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


