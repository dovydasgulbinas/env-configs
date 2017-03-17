# encoding: utf-8
# module samba.credentials
# from /usr/lib/python2.7/dist-packages/samba/credentials.so
# by generator 1.143
""" Credentials management. """

# imports
import talloc as __talloc


# Variables with simple values

AUTO_KRB_FORWARDABLE = 0

AUTO_USE_KERBEROS = 0

DONT_USE_KERBEROS = 1

FORCE_KRB_FORWARDABLE = 2

MUST_USE_KERBEROS = 2

NO_KRB_FORWARDABLE = 1

# no functions
# classes

class CredentialCacheContainer(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Credentials(__talloc.Object):
    # no doc
    def authentication_requested(self, *args, **kwargs): # real signature unknown
        pass

    def get_bind_dn(self): # real signature unknown; restored from __doc__
        """
        S.get_bind_dn() -> bind dn
        Obtain bind DN.
        """
        pass

    def get_domain(self): # real signature unknown; restored from __doc__
        """
        S.get_domain() -> domain
        Obtain domain name.
        """
        pass

    def get_forced_sasl_mech(self): # real signature unknown; restored from __doc__
        """
        S.get_forced_sasl_mech() -> SASL mechanism
        Obtain forced SASL mechanism.
        """
        pass

    def get_gensec_features(self, *args, **kwargs): # real signature unknown
        pass

    def get_kerberos_state(self, *args, **kwargs): # real signature unknown
        pass

    def get_named_ccache(self, *args, **kwargs): # real signature unknown
        pass

    def get_nt_hash(self, *args, **kwargs): # real signature unknown
        pass

    def get_password(self): # real signature unknown; restored from __doc__
        """
        S.get_password() -> password
        Obtain password.
        """
        pass

    def get_realm(self): # real signature unknown; restored from __doc__
        """
        S.get_realm() -> realm
        Obtain realm name.
        """
        pass

    def get_username(self): # real signature unknown; restored from __doc__
        """
        S.get_username() -> username
        Obtain username.
        """
        pass

    def get_workstation(self, *args, **kwargs): # real signature unknown
        pass

    def guess(self, *args, **kwargs): # real signature unknown
        pass

    def is_anonymous(self, *args, **kwargs): # real signature unknown
        pass

    def parse_string(self, text, obtained=None): # real signature unknown; restored from __doc__
        """
        S.parse_string(text, obtained=CRED_SPECIFIED) -> None
        Parse credentials string.
        """
        pass

    def set_anonymous(self): # real signature unknown; restored from __doc__
        """
        S.set_anonymous() -> None
        Use anonymous credentials.
        """
        pass

    def set_bind_dn(self, bind_dn): # real signature unknown; restored from __doc__
        """
        S.set_bind_dn(bind_dn) -> None
        Change bind DN.
        """
        pass

    def set_cmdline_callbacks(self): # real signature unknown; restored from __doc__
        """
        S.set_cmdline_callbacks() -> bool
        Use command-line to obtain credentials not explicitly set.
        """
        return False

    def set_domain(self, domain, obtained=None): # real signature unknown; restored from __doc__
        """
        S.set_domain(domain, obtained=CRED_SPECIFIED) -> None
        Change domain name.
        """
        pass

    def set_forced_sasl_mech(self, name): # real signature unknown; restored from __doc__
        """
        S.set_forced_sasl_mech(name) -> None
        Set forced SASL mechanism.
        """
        pass

    def set_gensec_features(self, *args, **kwargs): # real signature unknown
        pass

    def set_kerberos_state(self, *args, **kwargs): # real signature unknown
        pass

    def set_krb_forwardable(self, *args, **kwargs): # real signature unknown
        pass

    def set_machine_account(self, *args, **kwargs): # real signature unknown
        pass

    def set_password(self, password, obtained=None): # real signature unknown; restored from __doc__
        """
        S.set_password(password, obtained=CRED_SPECIFIED) -> None
        Change password.
        """
        pass

    def set_realm(self, realm, obtained=None): # real signature unknown; restored from __doc__
        """
        S.set_realm(realm, obtained=CRED_SPECIFIED) -> None
        Change realm name.
        """
        pass

    def set_username(self, name, obtained=None): # real signature unknown; restored from __doc__
        """
        S.set_username(name, obtained=CRED_SPECIFIED) -> None
        Change username.
        """
        pass

    def set_workstation(self, *args, **kwargs): # real signature unknown
        pass

    def wrong_password(self): # real signature unknown; restored from __doc__
        """
        S.wrong_password() -> bool
        Indicate the returned password was incorrect.
        """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


