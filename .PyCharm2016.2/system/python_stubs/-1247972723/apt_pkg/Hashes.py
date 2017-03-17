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

class Hashes(object):
    """
    Hashes([object: (bytes, file)])
    
    Calculate hashes for the given object. It can be used to create all
    supported hashes for a file.
    
    The parameter 'object' can be a bytestring, an object providing the
    fileno() method, or an integer describing a file descriptor.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    md5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The MD5Sum of the file as a string."""

    sha1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SHA1Sum of the file as a string."""

    sha256 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SHA256Sum of the file as a string."""



