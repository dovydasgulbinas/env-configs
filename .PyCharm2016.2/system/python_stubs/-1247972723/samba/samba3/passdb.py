# encoding: utf-8
# module samba.samba3.passdb
# from /usr/lib/python2.7/dist-packages/samba/samba3/passdb.so
# by generator 1.143
""" SAMBA Password Database """

# imports
import talloc as __talloc


# functions

def get_backends(): # real signature unknown; restored from __doc__
    """
    get_backends() -> list
    
     		Get a list of password database backends supported.
    """
    return []

def get_global_sam_sid(): # real signature unknown; restored from __doc__
    """
    get_global_sam_sid() -> dom_sid
    
     		Return domain SID.
    """
    pass

def reload_static_pdb(): # real signature unknown; restored from __doc__
    """
    reload_static_pdb() -> None
    
     		Re-initalise the static pdb used internally.  Needed if 'passdb backend' is changed.
    """
    pass

def set_secrets_dir(private_dir): # real signature unknown; restored from __doc__
    """
    set_secrets_dir(private_dir) -> None
    
     		Set path to private directory to load secrets database from non-default location.
    """
    pass

def set_smb_config(path): # real signature unknown; restored from __doc__
    """
    set_smb_config(path) -> None
    
     		Set path to smb.conf file to load configuration parameters.
    """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Groupmap(__talloc.Object):
    """ Groupmap() -> group map object """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nt_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sid_name_use = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class PDB(__talloc.Object):
    """ PDB(url[, read_write_flags]) -> Password DB object """
    def add_aliasmem(self, alias_sid, member_sid): # real signature unknown; restored from __doc__
        """
        add_aliasmem(alias_sid, member_sid) -> None
        
         		Add user to alias entry.
        """
        pass

    def add_groupmem(self, group_rid, member_rid): # real signature unknown; restored from __doc__
        """
        add_groupmem(group_rid, member_rid) -> None
        
         		Add user to group.
        """
        pass

    def add_group_mapping_entry(self, groupmap): # real signature unknown; restored from __doc__
        """
        add_group_mapping_entry(groupmap) -> None
         		Add group mapping entry for groupmap object.
        """
        pass

    def add_sam_account(self, samu_object): # real signature unknown; restored from __doc__
        """
        add_sam_account(samu object) -> None
        
         		Add SAM account.
        """
        pass

    def create_alias(self, alias_name): # real signature unknown; restored from __doc__
        """
        create_alias(alias_name) -> alias_rid
        
         		Create alias entry.
        """
        pass

    def create_dom_group(self, groupname): # real signature unknown; restored from __doc__
        """
        create_dom_group(groupname) -> group_rid
        
         		Create new domain group by name.
        """
        pass

    def create_user(self, username, acct_flags): # real signature unknown; restored from __doc__
        """
        create_user(username, acct_flags) -> rid
        
         		Create user. acct_flags are samr account control flags.
        """
        pass

    def delete_alias(self, alias_sid): # real signature unknown; restored from __doc__
        """
        delete_alias(alias_sid) -> None
        
         		Delete alias entry.
        """
        pass

    def delete_dom_group(self, group_rid): # real signature unknown; restored from __doc__
        """
        delete_dom_group(group_rid) -> None
        
         		Delete domain group identified by rid
        """
        pass

    def delete_group_mapping_entry(self, groupmap): # real signature unknown; restored from __doc__
        """
        delete_group_mapping_entry(groupmap) -> None
        
         		Delete group mapping entry for groupmap object.
        """
        pass

    def delete_sam_account(self, samu_object): # real signature unknown; restored from __doc__
        """
        delete_sam_account(samu object) -> None
        
         		Delete SAM account.
        """
        pass

    def delete_secret(self, secret_name): # real signature unknown; restored from __doc__
        """
        delete_secret(secret_name) -> None
        
         		Delete secret information for secret_name.
        """
        pass

    def delete_user(self, samu_object): # real signature unknown; restored from __doc__
        """
        delete_user(samu object) -> None
        
         		Delete user.
        """
        pass

    def del_aliasmem(self, alias_sid, member_sid): # real signature unknown; restored from __doc__
        """
        del_aliasmem(alias_sid, member_sid) -> None
        
         		Remove a user from alias entry.
        """
        pass

    def del_groupmem(self, group_rid, member_rid): # real signature unknown; restored from __doc__
        """
        del_groupmem(group_rid, member_rid) -> None
        
         		Remove user from from group.
        """
        pass

    def del_trusteddom_pw(self, domain): # real signature unknown; restored from __doc__
        """
        del_trusteddom_pw(domain) -> None
        
         		Delete trusted domain password.
        """
        pass

    def del_trusted_domain(self, domain): # real signature unknown; restored from __doc__
        """
        del_trusted_domain(domain) -> None
        
         		Delete trusted domain.
        """
        pass

    def domain_info(self): # real signature unknown; restored from __doc__
        """
        domain_info() -> str
        
         		Get domain information for the database.
        """
        return ""

    def enum_aliasmem(self, alias_sid): # real signature unknown; restored from __doc__
        """
        enum_aliasmem(alias_sid) -> List
        
         		Return a list of members (dom_sid object) for alias entry.
        """
        return []

    def enum_group_mapping(self, domain_sid=None, type=None, unix_only=None): # real signature unknown; restored from __doc__
        """
        enum_group_mapping([domain_sid, [type, [unix_only]]]) -> List
        
         		Return list of group mappings as groupmap objects. Optional arguments are domain_sid object, type of group, unix only flag.
        """
        return []

    def enum_group_members(self, group_sid): # real signature unknown; restored from __doc__
        """
        enum_group_members(group_sid) -> List
        
         		Return list of users (dom_sid object) in group.
        """
        return []

    def enum_group_memberships(self, samu_object): # real signature unknown; restored from __doc__
        """
        enum_group_memberships(samu object) -> List
        
         		Return list of groups (dom_sid object) this user is part of.
        """
        return []

    def enum_trusteddoms(self): # real signature unknown; restored from __doc__
        """
        enum_trusteddoms() -> List
        
         		Get list of trusted domains. Each item is a dictionary with name and sid keys
        """
        return []

    def enum_trusted_domains(self): # real signature unknown; restored from __doc__
        """
        enum_trusted_domains() -> List
        
         		Get list of trusted domains. Each entry is a dictionary with keys - domain_name, netbios_name, security_identifier, trust_auth_incoming, trust_auth_outgoing, trust_direction, trust_type, trust_attributes, trust_forest_trust_info.
        """
        return []

    def getgrgid(self, *args, **kwargs): # real signature unknown
        """
        getgrsid(gid) -> groupmap object
        
         		Get group information by gid.
        """
        pass

    def getgrnam(self, *args, **kwargs): # real signature unknown
        """
        getgrsid(groupname) -> groupmap object
        
         		Get group information by name.
        """
        pass

    def getgrsid(self, group_sid): # real signature unknown; restored from __doc__
        """
        getgrsid(group_sid) -> groupmap object
        
         		Get group information by sid (dcerpc.security.dom_sid object).
        """
        pass

    def getsampwnam(self, username): # real signature unknown; restored from __doc__
        """
        getsampwnam(username) -> samu object
        
         		Get user information by name.
        """
        pass

    def getsampwsid(self, user_sid): # real signature unknown; restored from __doc__
        """
        getsampwsid(user_sid) -> samu object
        
         		Get user information by sid (dcerpc.security.dom_sid object).
        """
        pass

    def get_account_policy(self): # real signature unknown; restored from __doc__
        """
        get_account_policy() -> Mapping
        
         		Get account policy information as a dictionary.
        """
        pass

    def get_aliasinfo(self, alias_sid): # real signature unknown; restored from __doc__
        """
        get_aliasinfo(alias_sid) -> Mapping
        
         		Get alias information as a dictionary with keys - acct_name, acct_desc, rid.
        """
        pass

    def get_secret(self, secret_name): # real signature unknown; restored from __doc__
        """
        get_secret(secret_name) -> Mapping
        
         		Get secret information for secret_name. Information is a dictionary with keys - secret_current, secret_current_lastchange, secret_old, secret_old_lastchange, sd.
        """
        pass

    def get_trusteddom_pw(self, domain): # real signature unknown; restored from __doc__
        """
        get_trusteddom_pw(domain) -> Mapping
        
         		Get trusted domain password, sid and last set time in a dictionary.
        """
        pass

    def get_trusted_domain(self, domain): # real signature unknown; restored from __doc__
        """
        get_trusted_domain(domain) -> Mapping
        
         		Get trusted domain information by name. Information is a dictionary with keys - domain_name, netbios_name, security_identifier, trust_auth_incoming, trust_auth_outgoing, trust_direction, trust_type, trust_attributes, trust_forest_trust_info.
        """
        pass

    def get_trusted_domain_by_sid(self, domain_sid): # real signature unknown; restored from __doc__
        """
        get_trusted_domain_by_sid(domain_sid) -> Mapping
        
         		Get trusted domain information by sid. Information is a dictionary with keys - domain_name, netbios_name, security_identifier, trust_auth_incoming, trust_auth_outgoing, trust_direction, trust_type, trust_attributes, trust_forest_trust_info
        """
        pass

    def gid_to_sid(self, gid): # real signature unknown; restored from __doc__
        """
        gid_to_sid(gid) -> sid
        
         		Return sid for given group id.
        """
        pass

    def new_rid(self): # real signature unknown; restored from __doc__
        """
        new_rid() -> rid
        
         		Get a new rid.
        """
        pass

    def rename_sam_account(self, samu_object1, new_username): # real signature unknown; restored from __doc__
        """
        rename_sam_account(samu object1, new_username) -> None
        
         		Rename SAM account.
        """
        pass

    def search_aliases(self, domain_sid=None): # real signature unknown; restored from __doc__
        """
        search_aliases([domain_sid]) -> List
        
         		Search aliases. domain_sid is dcerpc.security.dom_sid object.
         		Each list entry is dictionary with keys - idx, rid, acct_flags, account_name, fullname, description.
        """
        return []

    def search_groups(self): # real signature unknown; restored from __doc__
        """
        search_groups() -> List
        
         		Search unix only groups. 
         		Each list entry is dictionary with keys - idx, rid, acct_flags, account_name, fullname, description.
        """
        return []

    def search_users(self, acct_flags): # real signature unknown; restored from __doc__
        """
        search_users(acct_flags) -> List
        
         		Search users. acct_flags are samr account control flags.
         		Each list entry is dictionary with keys - idx, rid, acct_flags, account_name, fullname, description.
        """
        return []

    def set_account_policy(self, *args, **kwargs): # real signature unknown
        """
        get_account_policy(Mapping) -> None
        
         		Set account policy settings from a dicionary.
        """
        pass

    def set_aliasinfo(self, *args, **kwargs): # real signature unknown
        """
        set_alias_info(alias_sid, Mapping) -> None
        
         		Set alias information from a dictionary with keys - acct_name, acct_desc.
        """
        pass

    def set_secret(self, secret_name, Mapping): # real signature unknown; restored from __doc__
        """
        set_secret(secret_name, Mapping) -> None
        
         		Set secret information for secret_name using dictionary with keys - secret_current, sd.
        """
        pass

    def set_trusteddom_pw(self, domain, pwd, sid): # real signature unknown; restored from __doc__
        """
        set_trusteddom_pw(domain, pwd, sid) -> None
        
         		Set trusted domain password.
        """
        pass

    def set_trusted_domain(self, domain, Mapping): # real signature unknown; restored from __doc__
        """
        set_trusted_domain(domain, Mapping) -> None
        
         		Set trusted domain information for domain. Mapping is a dictionary with keys - domain_name, netbios_name, security_identifier, trust_auth_incoming, trust_auth_outgoing, trust_direction, trust_type, trust_attributes, trust_forest_trust_info.
        """
        pass

    def sid_to_id(self, sid): # real signature unknown; restored from __doc__
        """
        sid_to_id(sid) -> Tuple
        
         		Return id and type for given sid.
        """
        pass

    def uid_to_sid(self, uid): # real signature unknown; restored from __doc__
        """
        uid_to_sid(uid) -> sid
        
         		Return sid for given user id.
        """
        pass

    def update_group_mapping_entry(self, groupmap): # real signature unknown; restored from __doc__
        """
        update_group_mapping_entry(groupmap) -> None
        
         		Update group mapping entry for groupmap object.
        """
        pass

    def update_sam_account(self, samu_object): # real signature unknown; restored from __doc__
        """
        update_sam_account(samu object) -> None
        
         		Update SAM account.
        """
        pass

    def __init__(self, url, read_write_flags=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Samu(__talloc.Object):
    """ Samu() -> samu object """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    acct_ctrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    acct_desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bad_password_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bad_password_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    code_page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    country_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dir_drive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    group_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    home_dir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hours_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kickoff_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lanman_passwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logoff_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_divs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    munged_dial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nt_passwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nt_username = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pass_can_change_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pass_last_set_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pass_must_change_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    plaintext_passwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    profile_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pw_history = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    username = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    workstations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



