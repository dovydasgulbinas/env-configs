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

class MetaIndex(object):
    """
    Provide information on meta-indexes (i.e. Release files), such as
    whether they are trusted or their URI.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    dist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distribution, as a string."""

    index_files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all IndexFile objects associated with this meta index."""

    is_trusted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A boolean value determining whether the file can be trusted."""

    uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The uri the meta index is located at."""



