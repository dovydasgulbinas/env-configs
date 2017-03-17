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

class IndexFile(object):
    """
    Represent an index file, i.e. package indexes, translation indexes,
    and source indexes.
    """
    def archive_uri(self, path): # real signature unknown; restored from __doc__
        """
        archive_uri(path: str) -> str
        
        Return the URI to the given path in the archive.
        """
        return ""

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    describe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string describing the index file."""

    exists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A boolean value determining whether the index file exists."""

    has_packages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A boolean value determining whether the index file has packages."""

    is_trusted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A boolean value determining whether the file can be trusted; e.g.
because it is from a source with a GPG signed Release file."""

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The label of the index file."""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the files, measured in bytes."""



