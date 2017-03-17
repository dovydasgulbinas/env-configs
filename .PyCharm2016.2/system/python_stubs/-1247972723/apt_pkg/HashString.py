# encoding: utf-8
# module apt_pkg
# from /usr/lib/python2.7/dist-packages/apt_pkg.x86_64-linux-gnu.so
# by generator 1.143
"""
Classes and functions wrapping the apt-pkg library.

The apt_pkg module provides several classes and functions for accessing
the functionality provided by the apt-pkg library. Typical uses might
include reading APT index files and configuration files and installing
or removing packages.
"""
# no imports

from object import object

class HashString(object):
    """
    HashString(type, hash) OR HashString('type:hash')
    
    Create a new HashString object. The first form allows you to specify
    a type and a hash, and the second form a single string where type and
    hash are separated by a colon, e.g.::
    
       HashString('MD5Sum', '6cc1b6e6655e3555ac47e5b5fe26d04e')
    
    Valid options for 'type' are: MD5Sum, SHA1, SHA256.
    """
    def verify_file(self, filename): # real signature unknown; restored from __doc__
        """
        verify_file(filename: str) -> bool
        
        Verify that the file indicated by filename matches the hash.
        """
        return False

    def __init__(self, type, hash): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    hashtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the hash, as a string (possible: MD5Sum,SHA1,SHA256)."""



