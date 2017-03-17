# encoding: utf-8
# module samba.net
# from /usr/lib/python2.7/dist-packages/samba/net.so
# by generator 1.143
# no doc
# no imports

# Variables with simple values

LIBNET_JOINDOMAIN_AUTOMATIC = 0
LIBNET_JOINDOMAIN_SPECIFIED = 1

LIBNET_JOIN_AUTOMATIC = 0
LIBNET_JOIN_SPECIFIED = 1

# no functions
# classes

class Net(object):
    # no doc
    def change_password(self, newpassword): # real signature unknown; restored from __doc__
        """
        change_password(newpassword) -> True
        
        Change password for a user. You must supply credential with enough rights to do this.
        
        Sample usage is:
        net.change_password(newpassword=<new_password>)
        """
        return False

    def create_user(self, username): # real signature unknown; restored from __doc__
        """
        create_user(username)
        Create a new user.
        """
        pass

    def delete_user(self, username): # real signature unknown; restored from __doc__
        """
        delete_user(username)
        Delete a user.
        """
        pass

    def finddc(self, flags=None, domain=None, address=None): # real signature unknown; restored from __doc__
        """
        finddc(flags=server_type, domain=None, address=None)
        Find a DC with the specified 'server_type' bits. The 'domain' and/or 'address' have to be used as additional search criteria. Returns the whole netlogon struct
        """
        pass

    def join_member(self, domain_name, netbios_name, level): # real signature unknown; restored from __doc__
        """
        join_member(domain_name, netbios_name, level) -> (join_password, domain_sid, domain_name)
        
        Join the domain with the specified name.
        """
        pass

    def replicate_chunk(self, state, level, ctr, schema): # real signature unknown; restored from __doc__
        """
        replicate_chunk(state, level, ctr, schema)
        Process replication for one chunk
        """
        pass

    def replicate_init(self, samdb, lp, drspipe): # real signature unknown; restored from __doc__
        """
        replicate_init(samdb, lp, drspipe)
        Setup for replicate_chunk calls.
        """
        pass

    def set_password(self, account_name, domain_name, newpassword): # real signature unknown; restored from __doc__
        """
        set_password(account_name, domain_name, newpassword) -> True
        
        Set password for a user. You must supply credential with enough rights to do this.
        
        Sample usage is:
        net.set_password(account_name=account_name, domain_name=domain_name, newpassword=new_pass)
        """
        return False

    def time(self, server_name): # real signature unknown; restored from __doc__
        """
        time(server_name) -> timestr
        Retrieve the remote time on a server
        """
        pass

    def vampire(self, domain, target_dir=None): # real signature unknown; restored from __doc__
        """
        vampire(domain, target_dir=None)
        Vampire a domain.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


