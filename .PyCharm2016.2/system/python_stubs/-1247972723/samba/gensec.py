# encoding: utf-8
# module samba.gensec
# from /usr/lib/python2.7/dist-packages/samba/gensec.so
# by generator 1.143
""" Generic Security Interface. """

# imports
import talloc as __talloc


# Variables with simple values

FEATURE_ASYNC_REPLIES = 16

FEATURE_DATAGRAM_MODE = 32

FEATURE_DCE_STYLE = 8

FEATURE_NEW_SPNEGO = 128

FEATURE_SEAL = 4

FEATURE_SESSION_KEY = 1

FEATURE_SIGN = 2

FEATURE_SIGN_PKT_HEADER = 64

# no functions
# classes

class Security(__talloc.Object):
    # no doc
    def check_packet(self, data, whole_pdu, sig): # real signature unknown; restored from __doc__
        """
        S.check_packet(data, whole_pdu, sig)
        Check a DCERPC packet.
        """
        pass

    def get_name_by_authtype(self, authtype): # real signature unknown; restored from __doc__
        """
        S.get_name_by_authtype(authtype) -> name
        Lookup an auth type.
        """
        pass

    def have_feature(self): # real signature unknown; restored from __doc__
        """
        S.have_feature()
         Return True if GENSEC negotiated a particular feature.
        """
        pass

    def max_update_size(self): # real signature unknown; restored from __doc__
        """
        S.max_update_size() 
         Return the current max_update_size.
        """
        pass

    def session_info(self): # real signature unknown; restored from __doc__
        """ S.session_info() -> info """
        pass

    def session_key(self): # real signature unknown; restored from __doc__
        """ S.session_key() -> key """
        pass

    def set_credentials(self, *args, **kwargs): # real signature unknown
        """ S.start_client(credentials) """
        pass

    def set_max_update_size(self, max_size): # real signature unknown; restored from __doc__
        """
        S.set_max_update_size(max_size) 
         Some mechs can fragment update packets, needs to be use before the mech is started.
        """
        pass

    def set_target_hostname(self, *args, **kwargs): # real signature unknown
        """ S.start_target_hostname(target_hostname) """
        pass

    def set_target_service(self, *args, **kwargs): # real signature unknown
        """ S.start_target_service(target_service) """
        pass

    def sign_packet(self, data, whole_pdu): # real signature unknown; restored from __doc__
        """
        S.sign_packet(data, whole_pdu) -> sig
        Sign a DCERPC packet.
        """
        pass

    def sig_size(self, data_size): # real signature unknown; restored from __doc__
        """
        S.sig_size(data_size) -> sig_size
        Size of the DCERPC packet signature
        """
        pass

    @classmethod
    def start_client(cls, settings): # real signature unknown; restored from __doc__
        """ S.start_client(settings) -> gensec """
        pass

    def start_mech_by_authtype(self, authtype, level): # real signature unknown; restored from __doc__
        """ S.start_mech_by_authtype(authtype, level) """
        pass

    def start_mech_by_name(self, name): # real signature unknown; restored from __doc__
        """ S.start_mech_by_name(name) """
        pass

    def start_mech_by_sasl_name(self, name): # real signature unknown; restored from __doc__
        """ S.start_mech_by_sasl_name(name) """
        pass

    @classmethod
    def start_server(cls, auth_ctx, settings): # real signature unknown; restored from __doc__
        """ S.start_server(auth_ctx, settings) -> gensec """
        pass

    def unwrap(self, blob_in): # real signature unknown; restored from __doc__
        """
        S.unwrap(blob_in) -> blob_out
        Perform one wrapped GENSEC packet into a clear packet.
        """
        pass

    def update(self, blob_in): # real signature unknown; restored from __doc__
        """
        S.update(blob_in) -> (finished, blob_out)
        Perform one step in a GENSEC dance.  Repeat with new packets until finished is true or exception.
        """
        pass

    def want_feature(self, feature): # real signature unknown; restored from __doc__
        """
        S.want_feature(feature)
         Request that GENSEC negotiate a particular feature.
        """
        pass

    def wrap(self, blob_in): # real signature unknown; restored from __doc__
        """
        S.wrap(blob_in) -> blob_out
        Package one clear packet into a wrapped GENSEC packet.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


