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

class TagSection(object):
    """
    TagSection(text: str, [bytes: bool = False])
    
    Provide methods to access RFC822-style header sections, like those
    found in debian/control or Packages files.
    
    TagSection() behave like read-only dictionaries and also provide access
    to the functions provided by the C++ class (e.g. find).
    
    By default, text read from files is treated as strings (binary data in
    Python 2, Unicode strings in Python 3). Use bytes=True to cause all
    header values read from this TagSection to be bytes even in Python 3.
    Header names are always treated as Unicode.
    """
    def bytes(self): # real signature unknown; restored from __doc__
        """
        bytes() -> int
        
        Return the number of bytes this section is large.
        """
        return 0

    def find(self, name, default=None): # real signature unknown; restored from __doc__
        """
        find(name: str[, default = None]) -> str
        
        Find the key given by 'name' and return the value. If the key can
        not be found, return 'default'.
        """
        return ""

    def find_flag(self, name): # real signature unknown; restored from __doc__
        """
        find_flag(name: str) -> int
        
        Return 1 if the key's value is 'yes' or a similar value describing
        a boolean true. If the field does not exist, or does not have such a
        value, return 0.
        """
        return 0

    def find_raw(self, name, default=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        find_raw(name: str[, default = None] -> str
        
        Same as find(), but returns the complete 'key: value' field; instead of
        just the value.
        """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """
        find(name: str[, default = None]) -> str
        
        Find the key given by 'name' and return the value. If the key can
        not be found, return 'default'.
        """
        pass

    def has_key(self, name): # real signature unknown; restored from __doc__
        """
        has_key(name: str) -> bool
        
        Return True if the key given by 'name' exists, False otherwise.
        """
        return False

    def keys(self): # real signature unknown; restored from __doc__
        """
        keys() -> list
        
        Return a list of all keys.
        """
        return []

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, text, bytes=False): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


