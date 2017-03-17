# encoding: utf-8
# module samba.param
# from /usr/lib/python2.7/dist-packages/samba/param.so
# by generator 1.143
""" Parsing and writing Samba configuration files. """

# imports
import talloc as __talloc


# functions

def bin_dir(*args, **kwargs): # real signature unknown
    """ Returns the compiled in BINDIR. """
    pass

def default_path(*args, **kwargs): # real signature unknown
    """ Returns the default smb.conf path. """
    pass

def modules_dir(*args, **kwargs): # real signature unknown
    """ Returns the compiled in location of modules. """
    pass

def sbin_dir(*args, **kwargs): # real signature unknown
    """ Returns the compiled in SBINDIR. """
    pass

def setup_dir(*args, **kwargs): # real signature unknown
    """ Returns the compiled in location of provision tempates. """
    pass

# classes

class LoadParm(__talloc.Object):
    # no doc
    def dump(self, stream, show_defaults=False): # real signature unknown; restored from __doc__
        """ S.dump(stream, show_defaults=False) """
        pass

    def dump_a_parameter(self, stream, name, service_name): # real signature unknown; restored from __doc__
        """ S.dump_a_parameter(stream, name, service_name) """
        pass

    def get(self, name, service_name): # real signature unknown; restored from __doc__
        """
        S.get(name, service_name) -> value
        Find specified parameter.
        """
        pass

    def is_mydomain(self, name): # real signature unknown; restored from __doc__
        """
        S.is_mydomain(name) -> bool
        Check whether the specified name matches our domain name.
        """
        return False

    def is_myname(self, name): # real signature unknown; restored from __doc__
        """
        S.is_myname(name) -> bool
        Check whether the specified name matches one of our netbios names.
        """
        return False

    def load(self, filename): # real signature unknown; restored from __doc__
        """
        S.load(filename) -> None
        Load specified file.
        """
        pass

    def load_default(self): # real signature unknown; restored from __doc__
        """
        S.load_default() -> None
        Load default smb.conf file.
        """
        pass

    def private_path(self, name): # real signature unknown; restored from __doc__
        """ S.private_path(name) -> path """
        pass

    def samdb_url(self): # real signature unknown; restored from __doc__
        """
        S.samdb_url() -> string
        Returns the current URL for sam.ldb.
        """
        return ""

    def server_role(self): # real signature unknown; restored from __doc__
        """
        S.server_role() -> value
        Get the server role.
        """
        pass

    def services(self): # real signature unknown; restored from __doc__
        """ S.services() -> list """
        return []

    def set(self, name, value): # real signature unknown; restored from __doc__
        """
        S.set(name, value) -> bool
        Change a parameter.
        """
        return False

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    configfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of last config file that was loaded."""

    default_service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



