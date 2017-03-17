# encoding: utf-8
# module xmlsec.template
# from /opt/odoo/_venv/local/lib/python2.7/site-packages/xmlsec.so
# by generator 1.143
""" Xml Templates processing """
# no imports

# functions

def add_encrypted_key(*args, **kwargs): # real signature unknown
    """ Adds <enc:EncryptedKey/> node with given attributes to the <dsig:KeyInfo/> node of *node*. """
    pass

def add_ids(*args, **kwargs): # real signature unknown
    """
    Registers *ids* as ids used below *node*. *ids* is a sequence of attribute names
    used as XML ids in the subtree rooted at *node*.
    A call to `addIds` may be necessary to make known which attributes contain XML ids.
    This is the case, if a transform references an id via `XPointer` or a self document uri and
    the id inkey_data_formation is not available by other means (e.g. an associated DTD or XML schema).
    """
    pass

def add_key_name(*args, **kwargs): # real signature unknown
    """ Adds <dsig:KeyName/> node to the <dsig:KeyInfo/> node of *node*. """
    pass

def add_key_value(*args, **kwargs): # real signature unknown
    """ Adds <dsig:KeyValue/> node to the <dsig:KeyInfo/> node of *node*. """
    pass

def add_reference(*args, **kwargs): # real signature unknown
    """
    Adds <dsig:Reference/> node with given URI (uri ), Id (id ) and Type (type ) attributes and
    the required children <dsig:DigestMethod/> and <dsig:DigestValue/> to the <dsig:SignedInfo/> child of *node*.
    """
    pass

def add_transform(*args, **kwargs): # real signature unknown
    """ Adds <dsig:Transform/> node to the <dsig:Reference/> node of *node*. """
    pass

def add_x509_data(*args, **kwargs): # real signature unknown
    """ Adds <dsig:X509Data/> node to the <dsig:KeyInfo/> node of *node*. """
    pass

def create(*args, **kwargs): # real signature unknown
    """
    Creates new <dsig:Signature/> node with the mandatory <dsig:SignedInfo/>, <dsig:CanonicalizationMethod/>,
    <dsig:SignatureMethod/> and <dsig:SignatureValue/> children and sub-children.
    """
    pass

def encrypted_data_create(*args, **kwargs): # real signature unknown
    """ Creates new <{ns}:EncryptedData /> node for encryption template. """
    pass

def encrypted_data_ensure_cipher_value(*args, **kwargs): # real signature unknown
    """ Adds <CipherValue/> to the <enc:EncryptedData/> node of *node*. """
    pass

def encrypted_data_ensure_key_info(*args, **kwargs): # real signature unknown
    """ Adds <{ns}:KeyInfo/> to the <enc:EncryptedData/> node of *node*. """
    pass

def ensure_key_info(*args, **kwargs): # real signature unknown
    """ Adds (if necessary) <dsig:KeyInfo/> node to the <dsig:Signature/> node of *node*. """
    pass

def find_child(*args, **kwargs): # real signature unknown
    """ Searches a direct child of the parent node having given name and namespace href. """
    pass

def find_node(*args, **kwargs): # real signature unknown
    """ Searches all children of the parent node having given name and namespace href. """
    pass

def find_parent(*args, **kwargs): # real signature unknown
    """ Searches the ancestors axis of the node having given name and namespace href. """
    pass

def x509_data_add_certificate(*args, **kwargs): # real signature unknown
    """ Adds <dsig:X509Certificate/> node to the given <dsig:X509Data/> node of *node*. """
    pass

def x509_data_add_crl(*args, **kwargs): # real signature unknown
    """ Adds <dsig:X509CRL/> node to the given <dsig:X509Data/> node of *node*. """
    pass

def x509_data_add_issuer_serial(*args, **kwargs): # real signature unknown
    """ Adds <dsig:X509IssuerSerial/> node to the given <dsig:X509Data/> node of *node*. """
    pass

def x509_data_add_ski(*args, **kwargs): # real signature unknown
    """ Adds <dsig:X509SKI/> node to the given <dsig:X509Data/> node of *node*. """
    pass

def x509_data_add_subject_name(*args, **kwargs): # real signature unknown
    """ Adds <dsig:X509SubjectName/> node to the given <dsig:X509Data/> node of *node*. """
    pass

def x509_issuer_serial_add_issuer_name(*args, **kwargs): # real signature unknown
    """ Adds <dsig:X509IssuerName/> node to the <dsig:X509IssuerSerial/> node of *node*. """
    pass

def x509_issuer_serial_add_serial_number(*args, **kwargs): # real signature unknown
    """ Adds <dsig:X509SerialNumber/> node to the <dsig:X509IssuerSerial/> node of *node*. """
    pass

# no classes
