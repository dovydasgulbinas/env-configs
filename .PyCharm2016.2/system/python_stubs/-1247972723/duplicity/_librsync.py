# encoding: utf-8
# module duplicity._librsync
# from /usr/lib/python2.7/dist-packages/duplicity/_librsync.so
# by generator 1.143
# no doc
# no imports

# Variables with simple values

RS_DEFAULT_BLOCK_LEN = 2048

RS_JOB_BLOCKSIZE = 65536

# functions

def new_deltamaker(*args, **kwargs): # real signature unknown
    """ Return a deltamaker object, for computing deltas """
    pass

def new_patchmaker(*args, **kwargs): # real signature unknown
    """ Return a patchmaker object, for patching basis files """
    pass

def new_sigmaker(*args, **kwargs): # real signature unknown
    """ Return a sigmaker object, for finding the signature of an object """
    pass

# classes

class librsyncError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



