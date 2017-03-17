# encoding: utf-8
# module google.protobuf.pyext._message
# from /usr/lib/python2.7/dist-packages/google/protobuf/pyext/_message.x86_64-linux-gnu.so
# by generator 1.143
"""
python-proto2 is a module that can be used to enhance proto2 Python API
performance.

It provides access to the protocol buffers C++ reflection API that
implements the basic protocol buffer functions.
"""
# no imports

# no functions
# classes

class ExtensionDict(object):
    """ An extension dict """
    def ClearExtension(self, *args, **kwargs): # real signature unknown
        """ Clears an extension from the object. """
        pass

    def HasExtension(self, *args, **kwargs): # real signature unknown
        """ Checks if the object has an extension. """
        pass

    def _FindExtensionByName(self, *args, **kwargs): # real signature unknown
        """ Finds an extension by name. """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

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

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    __hash__ = None


class Message(object):
    """ A ProtocolMessage """
    @classmethod
    def AddDescriptors(cls, *args, **kwargs): # real signature unknown
        """ Adds field descriptors to the class """
        pass

    def ByteSize(self, *args, **kwargs): # real signature unknown
        """ Returns the size of the message in bytes. """
        pass

    def Clear(self, *args, **kwargs): # real signature unknown
        """ Clears the message. """
        pass

    def ClearExtension(self, *args, **kwargs): # real signature unknown
        """ Clears a message field. """
        pass

    def ClearField(self, *args, **kwargs): # real signature unknown
        """ Clears a message field. """
        pass

    def CopyFrom(self, *args, **kwargs): # real signature unknown
        """ Copies a protocol message into the current message. """
        pass

    def FindInitializationErrors(self, *args, **kwargs): # real signature unknown
        """ Finds unset required fields. """
        pass

    @classmethod
    def FromString(cls, *args, **kwargs): # real signature unknown
        """ Creates new method instance from given serialized data. """
        pass

    def HasExtension(self, *args, **kwargs): # real signature unknown
        """ Checks if a message field is set. """
        pass

    def HasField(self, *args, **kwargs): # real signature unknown
        """ Checks if a message field is set. """
        pass

    def IsInitialized(self, *args, **kwargs): # real signature unknown
        """ Checks if all required fields of a protocol message are set. """
        pass

    def ListFields(self, *args, **kwargs): # real signature unknown
        """ Lists all set fields of a message. """
        pass

    def MergeFrom(self, *args, **kwargs): # real signature unknown
        """ Merges a protocol message into the current message. """
        pass

    def MergeFromString(self, *args, **kwargs): # real signature unknown
        """ Merges a serialized message into the current message. """
        pass

    def ParseFromString(self, *args, **kwargs): # real signature unknown
        """ Parses a serialized message into the current message. """
        pass

    @classmethod
    def RegisterExtension(cls, *args, **kwargs): # real signature unknown
        """ Registers an extension with the current message. """
        pass

    def SerializePartialToString(self, *args, **kwargs): # real signature unknown
        """ Serializes the message to a string, even if it isn't initialized. """
        pass

    def SerializeToString(self, *args, **kwargs): # real signature unknown
        """ Serializes the message to a string, only for initialized messages. """
        pass

    def SetInParent(self, *args, **kwargs): # real signature unknown
        """ Sets the has bit of the given field in its parent message. """
        pass

    def WhichOneof(self, *args, **kwargs): # real signature unknown
        """ Returns the name of the field set inside a oneof, or None if no field is set. """
        pass

    def _BuildFile(self, *args, **kwargs): # real signature unknown
        """ Registers a new protocol buffer file in the global C++ descriptor pool. """
        pass

    def _GetExtensionDescriptor(self, *args, **kwargs): # real signature unknown
        """ Finds a extension descriptor in the message pool. """
        pass

    def _GetFieldDescriptor(self, *args, **kwargs): # real signature unknown
        """ Finds a field descriptor in the message pool. """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """ Makes a deep copy of the class. """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Outputs picklable representation of the message. """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Inputs picklable representation of the message. """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __unicode__(self, *args, **kwargs): # real signature unknown
        """ Outputs a unicode representation of the message. """
        pass

    Extensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extension dict"""


    DESCRIPTOR = None
    _extensions_by_name = None
    _extensions_by_number = None
    __hash__ = None


class RepeatedCompositeContainer(object):
    """ A Repeated scalar container """
    def add(self, *args, **kwargs): # real signature unknown
        """ Adds an object to the repeated container. """
        pass

    def extend(self, *args, **kwargs): # real signature unknown
        """ Adds objects to the repeated container. """
        pass

    def MergeFrom(self, *args, **kwargs): # real signature unknown
        """ Adds objects to the repeated container. """
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        """ Removes an object from the repeated container. """
        pass

    def sort(self, *args, **kwargs): # real signature unknown
        """ Sorts the repeated container. """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    __hash__ = None


class RepeatedScalarContainer(object):
    """ A Repeated scalar container """
    def append(self, *args, **kwargs): # real signature unknown
        """ Appends an object to the repeated container. """
        pass

    def extend(self, *args, **kwargs): # real signature unknown
        """ Appends objects to the repeated container. """
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        """ Appends objects to the repeated container. """
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        """ Removes an object from the repeated container. """
        pass

    def sort(self, *args, **kwargs): # real signature unknown
        """ Sorts the repeated container. """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """ Makes a deep copy of the class. """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Outputs picklable representation of the repeated field. """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    __hash__ = None


