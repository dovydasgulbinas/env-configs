# encoding: utf-8
# module gio._gio
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gio/_gio.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
import gio as __gio
import glib as __glib
import gobject as __gobject
import gobject._gobject as __gobject__gobject


class InetAddress(__gobject__gobject.GObject):
    """
    Object GInetAddress
    
    Properties from GInetAddress:
      family -> GSocketFamily: Address family
        The address family (IPv4 or IPv6)
      bytes -> gpointer: Bytes
        The raw address data
      is-any -> gboolean: Is any
        Whether this is the "any" address for its family
      is-loopback -> gboolean: Is loopback
        Whether this is the loopback address for its family
      is-link-local -> gboolean: Is link-local
        Whether this is a link-local address
      is-site-local -> gboolean: Is site-local
        Whether this is a site-local address
      is-multicast -> gboolean: Is multicast
        Whether this is a multicast address
      is-mc-global -> gboolean: Is multicast global
        Whether this is a global multicast address
      is-mc-link-local -> gboolean: Is multicast link-local
        Whether this is a link-local multicast address
      is-mc-node-local -> gboolean: Is multicast node-local
        Whether this is a node-local multicast address
      is-mc-org-local -> gboolean: Is multicast org-local
        Whether this is an organization-local multicast address
      is-mc-site-local -> gboolean: Is multicast site-local
        Whether this is a site-local multicast address
    
    Signals from GObject:
      notify (GParam)
    """
    def get_family(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_any(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_link_local(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_loopback(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_mc_global(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_mc_link_local(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_mc_node_local(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_mc_org_local(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_mc_site_local(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_multicast(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_site_local(self, *args, **kwargs): # real signature unknown
        pass

    def get_native_size(self, *args, **kwargs): # real signature unknown
        pass

    def to_string(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


