# encoding: utf-8
# module samba._glue
# from /usr/lib/python2.7/dist-packages/samba/_glue.so
# by generator 1.143
""" Python bindings for miscellaneous Samba functions. """
# no imports

# Variables with simple values

version = '4.3.8-Ubuntu'

# functions

def generate_random_password(min, max): # real signature unknown; restored from __doc__
    """
    generate_random_password(min, max) -> string
    Generate random password with a length >= min and <= max.
    """
    return ""

def generate_random_str(len): # real signature unknown; restored from __doc__
    """
    generate_random_str(len) -> string
    Generate random string with specified length.
    """
    return ""

def get_debug_level(*args, **kwargs): # real signature unknown
    """ get debug level """
    pass

def interface_ips(lp_ctx, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    interface_ips(lp_ctx[, all_interfaces) -> list_of_ifaces
    
    get interface IP address list
    """
    pass

def nttime2string(nttime): # real signature unknown; restored from __doc__
    """ nttime2string(nttime) -> string """
    return ""

def nttime2unix(nttime): # real signature unknown; restored from __doc__
    """ nttime2unix(nttime) -> timestamp """
    pass

def set_debug_level(*args, **kwargs): # real signature unknown
    """ set debug level """
    pass

def strcasecmp_m(): # real signature unknown; restored from __doc__
    """ (for testing) compare two strings using Samba's strcasecmp_m() """
    pass

def strstr_m(): # real signature unknown; restored from __doc__
    """ (for testing) find one string in another with Samba's strstr_m() """
    pass

def unix2nttime(timestamp): # real signature unknown; restored from __doc__
    """ unix2nttime(timestamp) -> nttime """
    pass

# no classes
