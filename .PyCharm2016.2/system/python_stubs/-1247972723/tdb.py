# encoding: utf-8
# module tdb
# from /usr/lib/python2.7/dist-packages/tdb.x86_64-linux-gnu.so
# by generator 1.143
""" simple key-value database that supports multiple writers. """
# no imports

# Variables with simple values

ALLOW_NESTING = 512

BIGENDIAN = 32

CLEAR_IF_FIRST = 1

CONVERT = 16

DEFAULT = 0

DISALLOW_NESTING = 1024

INCOMPATIBLE_HASH = 2048

INSERT = 2
INTERNAL = 2

MODIFY = 3

NOLOCK = 4
NOMMAP = 8
NOSYNC = 64

REPLACE = 1

SEQNUM = 128

VOLATILE = 256

__docformat__ = 'restructuredText'

__version__ = '1.3.8'

# functions

def open(name, hash_size=0, tdb_flags=None, flags=None, mode=0600): # real signature unknown; restored from __doc__
    """
    open(name, hash_size=0, tdb_flags=TDB_DEFAULT, flags=O_RDWR, mode=0600)
    Open a TDB file.
    """
    pass

# classes

class Tdb(object):
    """ A TDB file """
    def add_flags(self, flags): # real signature unknown; restored from __doc__
        """ S.add_flags(flags) -> None """
        pass

    def append(self, key, value): # real signature unknown; restored from __doc__
        """
        S.append(key, value) -> None
        Append data to an existing key.
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """
        S.clear() -> None
        Wipe the entire database.
        """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, key): # real signature unknown; restored from __doc__
        """
        S.delete(key) -> None
        Delete an entry.
        """
        pass

    def enable_seqnum(self): # real signature unknown; restored from __doc__
        """ S.enable_seqnum() -> None """
        pass

    def firstkey(self): # real signature unknown; restored from __doc__
        """
        S.firstkey() -> data
        Return the first key in this database.
        """
        pass

    def get(self, key): # real signature unknown; restored from __doc__
        """
        S.get(key) -> value
        Fetch a value.
        """
        pass

    def has_key(self, key): # real signature unknown; restored from __doc__
        """
        S.has_key(key) -> None
        Check whether key exists in this database.
        """
        pass

    def increment_seqnum_nonblock(self): # real signature unknown; restored from __doc__
        """ S.increment_seqnum_nonblock() -> None """
        pass

    def iterkeys(self): # real signature unknown; restored from __doc__
        """ S.iterkeys() -> iterator """
        pass

    def lock_all(self, *args, **kwargs): # real signature unknown
        pass

    def nextkey(self, key): # real signature unknown; restored from __doc__
        """
        S.nextkey(key) -> data
        Return the next key in this database.
        """
        pass

    def read_lock_all(self, *args, **kwargs): # real signature unknown
        pass

    def read_unlock_all(self, *args, **kwargs): # real signature unknown
        pass

    def remove_flags(self, flags): # real signature unknown; restored from __doc__
        """ S.remove_flags(flags) -> None """
        pass

    def reopen(self, *args, **kwargs): # real signature unknown
        """ Reopen this file. """
        pass

    def repack(self): # real signature unknown; restored from __doc__
        """
        S.repack() -> None
        Repack the entire database.
        """
        pass

    def store(self, key, data, flag=None): # real signature unknown; restored from __doc__
        """ S.store(key, data, flag=REPLACE) -> NoneStore data. """
        pass

    def transaction_cancel(self): # real signature unknown; restored from __doc__
        """
        S.transaction_cancel() -> None
        Cancel the currently active transaction.
        """
        pass

    def transaction_commit(self): # real signature unknown; restored from __doc__
        """
        S.transaction_commit() -> None
        Commit the currently active transaction.
        """
        pass

    def transaction_prepare_commit(self): # real signature unknown; restored from __doc__
        """
        S.transaction_prepare_commit() -> None
        Prepare to commit the currently active transaction
        """
        pass

    def transaction_start(self): # real signature unknown; restored from __doc__
        """
        S.transaction_start() -> None
        Start a new transaction.
        """
        pass

    def unlock_all(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The filename of this TDB file."""

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freelist_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hash_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_dead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seqnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



