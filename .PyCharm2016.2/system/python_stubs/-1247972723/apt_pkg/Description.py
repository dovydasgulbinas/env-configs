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

class Description(object):
    """
    Represent a package description and some attributes. Needed for
    things like translated descriptions.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    file_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all apt_pkg.PackageFile objects related to this description."""

    language_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The language code of the description. Empty string for untranslated
descriptions."""

    md5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The MD5 hash of the description."""



