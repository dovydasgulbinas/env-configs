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

class ActionGroup(object):
    """
    ActionGroup(depcache)
    
    Create a new ActionGroup() object. The parameter *depcache* refers to an
    apt_pkg.DepCache() object.
    
    ActionGroups disable certain cleanup actions, so modifying many packages
    is much faster.
    
    ActionGroup() can also be used with the 'with' statement, but be aware
    that the ActionGroup() is active as soon as it is created, and not just
    when entering the context. This means you can write::
    
        with apt_pkg.ActionGroup(depcache):
            depcache.markInstall(pkg)
    
    Once the block of the with statement is left, the action group is 
    automatically released from the cache.
    """
    def release(self): # real signature unknown; restored from __doc__
        """
        release()
        
        End the scope of this action group.  If this is the only action
        group bound to the cache, this will cause any deferred cleanup
        actions to be performed.
        """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """
        __enter__() -> ActionGroup
        
        A dummy action which just returns the object itself, so it can
        be used as a context manager.
        """
        return ActionGroup

    def __exit__(self, *excinfo): # real signature unknown; restored from __doc__
        """
        __exit__(*excinfo) -> bool
        
        Same as release(), but for use as a context manager.
        """
        return False

    def __init__(self, depcache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


