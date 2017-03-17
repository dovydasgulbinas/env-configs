# encoding: utf-8
# module xmlsec
# from /opt/odoo/_venv/local/lib/python2.7/site-packages/xmlsec.so
# by generator 1.143
""" Python bindings for the XML Security Library """

# imports
import KeyData as KeyData # <module 'KeyData' (built-in)>
import Namespace as Namespace # <module 'Namespace' (built-in)>
import Transform as Transform # <module 'Transform' (built-in)>
import xmlsec.template as template # <module 'xmlsec.template' (built-in)>
import Node as Node # <module 'Node' (built-in)>
import KeyFormat as KeyFormat # <module 'KeyFormat' (built-in)>
import KeyDataType as KeyDataType # <module 'KeyDataType' (built-in)>
import EncryptionType as EncryptionType # <module 'EncryptionType' (built-in)>
import xmlsec.constants as constants # <module 'xmlsec.constants' (built-in)>
import xmlsec.template as tree # <module 'xmlsec.template' (built-in)>

# Variables with simple values

__version__ = '1.0.5'

# functions

def enable_debug_trace(*args, **kwargs): # real signature unknown
    """ Enables or disables calling LibXML2 callback from the default errors callback. """
    pass

def init(*args, **kwargs): # real signature unknown
    """
    Initialize the library for general operation.
    This is called upon library import and does not need to be called
    again (unless @ref _shutdown is called explicitly).
    """
    pass

def shutdown(*args, **kwargs): # real signature unknown
    """
    Shutdown the library and cleanup any leftover resources.
    This is called automatically upon interpreter termination and
    should not need to be called explicitly.
    """
    pass

# classes

class EncryptionContext(object):
    """ XML Encryption implementation """
    def decrypt(self, *args, **kwargs): # real signature unknown
        """
        Decrypts *node* (an `EncryptedData` element) and return the result.
        The decryption may result in binary data or an XML subtree.
        In the former case, the binary data is returned. In the latter case,
        the input tree is modified and a reference to the decrypted XML subtree is returned.
        If the operation modifies the tree, `lxml` references to or into this tree may see a surprising state.
        You should no longer rely on them. Especially, you should use `getroottree()` on the result
        to obtain the decrypted result tree.
        """
        pass

    def encrypt_binary(self, *args, **kwargs): # real signature unknown
        """
        Encrypts binary *data* according to `EncryptedData` template *template*
        returns the resulting `EncryptedData` subtree.
        Note: *template* is modified in place.
        """
        pass

    def encrypt_uri(self, *args, **kwargs): # real signature unknown
        """ Encrypts binary data obtained from *uri* according to *template*. """
        pass

    def encrypt_xml(self, *args, **kwargs): # real signature unknown
        """
        Encrpyts *node* using *template*.
        Returns the resulting `EncryptedData` element.
        
        Note: The `Type` attribute of *template* decides whether *node* itself is encrypted
        (`http://www.w3.org/2001/04/xmlenc#Element`) or its content (`http://www.w3.org/2001/04/xmlenc#Content`).
        It must have one of these two values (or an exception is raised).
        The operation modifies the tree containing *node* in a way that
        `lxml` references to or into this tree may see a surprising state.
        You should no longer rely on them. Especially, you should use
        `getroottree()` on the result to obtain the encrypted result tree.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encryption key.
"""



class Error(Exception):
    """ The common exception class. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class InternalError(Error):
    """ The internal exception class. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Key(object):
    """ Key """
    @classmethod
    def from_binary_file(cls, *args, **kwargs): # real signature unknown
        """ Loads (symmetric) key of kind *data* from *filename*. """
        pass

    @classmethod
    def from_file(cls, *args, **kwargs): # real signature unknown
        """ Load PKI key from a file. """
        pass

    @classmethod
    def from_memory(cls, *args, **kwargs): # real signature unknown
        """ Load PKI key from memory. """
        pass

    @classmethod
    def generate(cls, *args, **kwargs): # real signature unknown
        """ Generate key of kind *data* with *size* and *type*. """
        pass

    def load_cert_from_file(self, *args, **kwargs): # real signature unknown
        """ Load certificate from file. """
        pass

    def load_cert_from_memory(self, *args, **kwargs): # real signature unknown
        """ Load certificate from memory. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the name of *key*.
"""



class KeysManager(object):
    """ Keys Manager """
    def add_key(self, *args, **kwargs): # real signature unknown
        """ Adds a copy of *key*. """
        pass

    def load_cert(self, *args, **kwargs): # real signature unknown
        """
        load certificate from *filename*
        *format* - file format
        *type* - key type.
        """
        pass

    def load_cert_from_memory(self, *args, **kwargs): # real signature unknown
        """
        load certificate from *data*
        *format* - file format
        *type* - key type.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class SignatureContext(object):
    """ XML Digital Signature implementation """
    def enable_reference_transform(self, *args, **kwargs): # real signature unknown
        """
        Enables use of *t* as reference transform.
        Note: by default, all transforms are enabled. The first call of
        `enable_reference_transform` will switch to explicitly enabled transforms.
        """
        pass

    def enable_signature_transform(self, *args, **kwargs): # real signature unknown
        """
        Enables use of *t* as signature transform.
        Note: by default, all transforms are enabled. The first call of
        `enable_signature_transform` will switch to explicitly enabled transforms.
        """
        pass

    def register_id(self, *args, **kwargs): # real signature unknown
        """ Register new id. """
        pass

    def set_enabled_key_data(self, *args, **kwargs): # real signature unknown
        """ Adds selected *KeyData* to the list of enabled key data list. """
        pass

    def sign(self, *args, **kwargs): # real signature unknown
        """ Sign according to the signature template. """
        pass

    def sign_binary(self, *args, **kwargs): # real signature unknown
        """ Sign binary data *data* with *algorithm* and return the signature. """
        pass

    def verify(self, *args, **kwargs): # real signature unknown
        """ Verify according to the signature template. """
        pass

    def verify_binary(self, *args, **kwargs): # real signature unknown
        """ Sign binary data *data* with *algorithm* and return the signature. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Signature key.
"""



class VerificationError(Error):
    """ The verification exception class. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__guard = None # (!) real value is ''

