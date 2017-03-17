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

class OrderList(object):
    """
    OrderList(depcache: DepCache)
    
    Sequence type for packages with special ordering methods.
    """
    def append(self, pkg): # real signature unknown; restored from __doc__
        """
        append(pkg: Package)
        
        Append a package to the end of the list.
        """
        pass

    def flag(self, pkg, flag, unset_flags=None): # real signature unknown; restored from __doc__
        """
        flag(pkg: Package, flag: int[, unset_flags: int])
        
        Flag the package, set flags in 'flag' and remove flags in
        'unset_flags'.
        """
        pass

    def is_flag(self, pkg, flag): # real signature unknown; restored from __doc__
        """
        is_flag(pkg: Package, flag: int)
        
        Check if the flag(s) are set.
        """
        pass

    def is_missing(self, *args, **kwargs): # real signature unknown
        """
        is_now(pkg: Package)
        
        Check if the package is marked for install.
        """
        pass

    def is_now(self, pkg): # real signature unknown; restored from __doc__
        """
        is_now(pkg: Package)
        
        Check if the package is flagged for any state but removal.
        """
        pass

    def order_configure(self): # real signature unknown; restored from __doc__
        """
        order_configure()
        
        Order the packages for configuration (see Debian Policy).
        """
        pass

    def order_critical(self): # real signature unknown; restored from __doc__
        """
        order_critical()
        
        Order by PreDepends only (critical unpack order).
        """
        pass

    def order_unpack(self): # real signature unknown; restored from __doc__
        """
        order_unpack()
        
        Order the packages for unpacking (see Debian Policy).
        """
        pass

    def score(self, pkg): # real signature unknown; restored from __doc__
        """
        score(pkg: Package) -> int
        
        Return the score of the package.
        """
        return 0

    def wipe_flags(self, flags): # real signature unknown; restored from __doc__
        """
        wipe_flags(flags: int)
        
        Remove the flags in 'flags' from all packages in this list
        """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, depcache): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    FLAG_ADDED = 1
    FLAG_ADD_PENDIG = 2
    FLAG_AFTER = 256
    FLAG_CONFIGURED = 32
    FLAG_IMMEDIATE = 4
    FLAG_IN_LIST = 128
    FLAG_LOOP = 8
    FLAG_REMOVED = 64
    FLAG_STATES_MASK = 112
    FLAG_UNPACKED = 16


