# encoding: utf-8
# module samba.smb
# from /usr/lib/python2.7/dist-packages/samba/smb.so
# by generator 1.143
""" SMB File I/O support """

# imports
import talloc as __talloc


# Variables with simple values

FILE_ATTRIBUTE_ALL_MASK = 32767

FILE_ATTRIBUTE_ARCHIVE = 32
FILE_ATTRIBUTE_COMPRESSED = 2048
FILE_ATTRIBUTE_DEVICE = 64
FILE_ATTRIBUTE_DIRECTORY = 16
FILE_ATTRIBUTE_ENCRYPTED = 16384
FILE_ATTRIBUTE_HIDDEN = 2
FILE_ATTRIBUTE_NONINDEXED = 8192
FILE_ATTRIBUTE_NORMAL = 128
FILE_ATTRIBUTE_OFFLINE = 4096
FILE_ATTRIBUTE_READONLY = 1

FILE_ATTRIBUTE_REPARSE_POINT = 1024

FILE_ATTRIBUTE_SPARSE = 512
FILE_ATTRIBUTE_SYSTEM = 4
FILE_ATTRIBUTE_TEMPORARY = 256
FILE_ATTRIBUTE_VOLUME = 8

# no functions
# classes

class SMB(__talloc.Object):
    """ SMB(hostname, service[, creds[, lp]]) -> SMB connection object """
    def chkpath(self, path): # real signature unknown; restored from __doc__
        """
        chkpath(path) -> True or False
        
         		Return true if path exists, false otherwise.
        """
        return False

    def close_file(self, fnum): # real signature unknown; restored from __doc__
        """
        close_file(fnum) -> None
        
         		Close the file based on fnum.
        """
        pass

    def deltree(self, path): # real signature unknown; restored from __doc__
        """
        deltree(path) -> None
        
         		Delete a directory and all its contents.
        """
        pass

    def get_acl(self, path, security_info=0): # real signature unknown; restored from __doc__
        """
        get_acl(path[, security_info=0]) -> security_descriptor object
        
         		Get security descriptor for file.
        """
        pass

    def list(self, path): # real signature unknown; restored from __doc__
        """
        list(path) -> directory contents as a dictionary
        
         		List contents of a directory. The keys are, 
         			name: Long name of the directory item
         			short_name: Short name of the directory item
         			size: File size in bytes
         			attrib: Attributes
         			mtime: Modification time
        """
        pass

    def loadfile(self, path): # real signature unknown; restored from __doc__
        """
        loadfile(path) -> file contents as a string
        
         		Read contents of a file.
        """
        return file('/dev/null')

    def mkdir(self, path): # real signature unknown; restored from __doc__
        """
        mkdir(path) -> None
        
         		Create a directory.
        """
        pass

    def open_file(self, path, access_mask, share_access=None, open_disposition=None, create_options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        open_file(path, access_mask[, share_access[, open_disposition[, create_options]]] -> fnum
        
         		Open a file. Throws NTSTATUS exceptions on errors.
        """
        pass

    def rmdir(self, path): # real signature unknown; restored from __doc__
        """
        rmdir(path) -> None
        
         		Delete a directory.
        """
        pass

    def savefile(self, path, p_str): # real signature unknown; restored from __doc__
        """
        savefile(path, str) -> None
        
         		Write string str to file.
        """
        pass

    def set_acl(self, path, security_descriptor, security_info=0): # real signature unknown; restored from __doc__
        """
        set_acl(path, security_descriptor[, security_info=0]) -> None
        
         		Set security descriptor for file.
        """
        pass

    def __init__(self, hostname, service, creds=None, lp=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


