# encoding: utf-8
# module samba._ldb
# from /usr/lib/python2.7/dist-packages/samba/_ldb.so
# by generator 1.143
""" Samba-specific LDB python bindings """

# imports
import ldb as __ldb


# no functions
# classes

class Ldb(__ldb.Ldb):
    """ Connection to a LDB database. """
    def register_samba_handlers(self): # real signature unknown; restored from __doc__
        """
        register_samba_handlers()
        Register Samba-specific LDB modules and schemas.
        """
        pass

    def set_credentials(self, credentials): # real signature unknown; restored from __doc__
        """
        ldb_set_credentials(credentials)
        Set credentials to use when connecting.
        """
        pass

    def set_loadparm(self, session_info): # real signature unknown; restored from __doc__
        """
        ldb_set_loadparm(session_info)
        Set loadparm context to use when connecting.
        """
        pass

    def set_opaque_integer(self, *args, **kwargs): # real signature unknown
        pass

    def set_session_info(self, session_info): # real signature unknown; restored from __doc__
        """
        set_session_info(session_info)
        Set session info to use when connecting.
        """
        pass

    def set_utf8_casefold(self): # real signature unknown; restored from __doc__
        """
        ldb_set_utf8_casefold()
        Set the right Samba casefolding function for UTF8 charset.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


