# encoding: utf-8
# module _ped
# from /usr/lib/python2.7/dist-packages/_ped.x86_64-linux-gnu.so
# by generator 1.143
"""
This module implements an interface to libparted.

pyparted provides two API layers:  a lower level that exposes the complete
libparted API, and a higher level built on top of that which provides a
more Python-like view.  The _ped module is the base of the lower level
API.  It provides:

	- Access to all the basic objects and submodules of pyparted
	- Basic unit handling and mathematical functions
	- A few basic device probing functions
	- The DEVICE_*, PARTITION_*, and UNIT_* constants from libparted
	- A variety of exceptions for handling error conditions

For complete documentation, refer to the docs strings for each _ped
method, exception class, and subclass.
"""
# no imports

# Variables with simple values

DEVICE_ATARAID = 6
DEVICE_CPQARRAY = 4
DEVICE_DAC960 = 3
DEVICE_DASD = 9
DEVICE_DM = 12
DEVICE_FILE = 5
DEVICE_I2O = 7
DEVICE_IDE = 2
DEVICE_SCSI = 1
DEVICE_SDMMC = 14
DEVICE_SX8 = 11
DEVICE_UBD = 8
DEVICE_UNKNOWN = 0
DEVICE_VIODASD = 10
DEVICE_VIRTBLK = 15
DEVICE_XVD = 13

DISK_CYLINDER_ALIGNMENT = 1

DISK_GPT_PMBR_BOOT = 2

DISK_TYPE_EXTENDED = 1

DISK_TYPE_PARTITION_NAME = 2

EXCEPTION_OPT_IGNORE_CANCEL = 96

EXCEPTION_OPT_OK_CANCEL = 72

EXCEPTION_OPT_RETRY_CANCEL = 80

EXCEPTION_OPT_RETRY_IGNORE_CANCEL = 112

EXCEPTION_OPT_YES_NO = 6

EXCEPTION_OPT_YES_NO_CANCEL = 70

EXCEPTION_RESOLVE_CANCEL = 64
EXCEPTION_RESOLVE_FIX = 1
EXCEPTION_RESOLVE_IGNORE = 32
EXCEPTION_RESOLVE_NO = 4
EXCEPTION_RESOLVE_OK = 8
EXCEPTION_RESOLVE_RETRY = 16
EXCEPTION_RESOLVE_UNHANDLED = 0
EXCEPTION_RESOLVE_YES = 2

EXCEPTION_TYPE_BUG = 5
EXCEPTION_TYPE_ERROR = 3
EXCEPTION_TYPE_FATAL = 4
EXCEPTION_TYPE_INFORMATION = 1

EXCEPTION_TYPE_NO_FEATURE = 6

EXCEPTION_TYPE_WARNING = 2

PARTITION_APPLE_TV_RECOVERY = 13

PARTITION_BIOS_GRUB = 12

PARTITION_BOOT = 1
PARTITION_DIAG = 14
PARTITION_EXTENDED = 2
PARTITION_FREESPACE = 4
PARTITION_HIDDEN = 4
PARTITION_HPSERVICE = 8
PARTITION_LBA = 7

PARTITION_LEGACY_BOOT = 15

PARTITION_LOGICAL = 1
PARTITION_LVM = 6
PARTITION_METADATA = 8

PARTITION_MSFT_RESERVED = 11

PARTITION_NORMAL = 0
PARTITION_PALO = 9
PARTITION_PREP = 10
PARTITION_PROTECTED = 16
PARTITION_RAID = 5
PARTITION_ROOT = 2
PARTITION_SWAP = 3

UNIT_BYTE = 1
UNIT_CHS = 8
UNIT_COMPACT = 6
UNIT_CYLINDER = 7
UNIT_GIBIBYTE = 12
UNIT_GIGABYTE = 4
UNIT_KIBIBYTE = 10
UNIT_KILOBYTE = 2
UNIT_MEBIBYTE = 11
UNIT_MEGABYTE = 3
UNIT_PERCENT = 9
UNIT_SECTOR = 0
UNIT_TEBIBYTE = 13
UNIT_TERABYTE = 5

# functions

def clear_exn_handler(): # real signature unknown; restored from __doc__
    """
    clear_exn_handler()
    
    Clear any previously added exception handling function.  This means the
    default behavior for all parted exceptions will be used, so only safe
    answers to any questions parted asks will be automatically provided.
    """
    pass

def constraint_any(Device): # real signature unknown; restored from __doc__
    """
    constraint_any(Device) -> Constraint
    
    Return a Constraint that any region on Device will satisfy.
    """
    return Constraint

def constraint_exact(Geometry): # real signature unknown; restored from __doc__
    """
    constraint_exact(Geometry) -> Constraint
    
    Return a Constraint that only the given Geometry will satisfy.
    """
    return Constraint

def constraint_new_from_max(Geometry): # real signature unknown; restored from __doc__
    """
    constraint_new_from_max(Geometry) -> Constraint
    
    Return a Constraint that requires a region to be entirely contained inside
    Geometry.
    """
    return Constraint

def constraint_new_from_min(Geometry): # real signature unknown; restored from __doc__
    """
    constraint_new_from_min(Geometry) -> Constraint
    
    Return a Constraint that requires a region to entirely contain Geometry.
    """
    return Constraint

def constraint_new_from_min_max(min, max): # real signature unknown; restored from __doc__
    """
    constraint_new_from_min_max(min, max) -> Constraint
    
    min and max are Geometry objects.  Return a Constraint that requires the region
    to be entirely contained inside max and to entirely contain min.
    """
    return Constraint

def device_free_all(): # real signature unknown; restored from __doc__
    """
    device_free_all()
    
    Close and free all devices.
    """
    pass

def device_get(string): # real signature unknown; restored from __doc__
    """
    device_get(string) -> Device
    
    Return the Device corresponding to the given path.  Typically, path will
    be a device name like /dev/sda.
    """
    return Device

def device_get_next(Device): # real signature unknown; restored from __doc__
    """
    device_get_next(Device) -> Device
    
    Return the next Device in the list detected by _ped.device_probe_all().
    """
    return Device

def device_probe_all(): # real signature unknown; restored from __doc__
    """
    device_probe_all()
    
    Attempt to detect all devices.
    """
    pass

def disk_flag_get_by_name(string): # real signature unknown; restored from __doc__
    """
    disk_flag_get_by_name(string) -> integer
    
    Return a disk flag given its name, or 0 if no flag matches the name.
    """
    return 0

def disk_flag_get_name(integer): # real signature unknown; restored from __doc__
    """
    disk_flag_get_name(integer) -> string
    
    Return a name for a disk flag constant.  If an invalid flag is provided,
    a ValueError will be raised.
    """
    return ""

def disk_flag_next(integer): # real signature unknown; restored from __doc__
    """
    disk_flag_next(integer) -> integer
    
    Given a disk flag, return the next flag.  If there is no next flag, 0
    is returned.
    """
    return 0

def disk_new(Device): # real signature unknown; restored from __doc__
    """
    disk_new(Device) -> Disk
    
    Given the Device, create a new Disk object. And probe, read the details of
    the disk.
    """
    return Disk

def disk_new_fresh(Device, DiskType): # real signature unknown; restored from __doc__
    """
    disk_new_fresh(Device, DiskType) -> Disk
    
    Given the Device and DiskType, create a new Disk object with using the
    DiskType specified.  The new disk label is only in-memory, the caller
    will have to use the commit_to_dev() method to write the new label to
    the disk.
    """
    return Disk

def disk_type_get(string): # real signature unknown; restored from __doc__
    """
    disk_type_get(string) -> DiskType
    
    Return a DiskType object with the given name.  If no DiskType exists with
    that name, raise _ped.UnknownTypeException.
    """
    return DiskType

def disk_type_get_next(self): # real signature unknown; restored from __doc__
    """
    disk_type_get_next(self) -> DiskType
    
    Return the next DiskType after self.  If self is the last DiskType, raise
    IndexError.
    """
    return DiskType

def file_system_probe(Geometry): # real signature unknown; restored from __doc__
    """
    file_system_probe(Geometry) -> FileSystemType
    
    Attempt to detect a file system in the region described by Geometry.
    This function tries to be clever at dealing with ambiguous
    situations, such as when one file system was not completely erased
    before a new file system was created on top of it.
    """
    return FileSystemType

def file_system_probe_specific(FileSystemType, Geometry): # real signature unknown; restored from __doc__
    """
    file_system_probe_specific(FileSystemType, Geometry) -> Geometry
    
    Attempt to find a file system and return the region it occupies.
    """
    return Geometry

def file_system_type_get(self, string): # real signature unknown; restored from __doc__
    """
    file_system_type_get(self, string) -> _ped.FileSystemType
    
    Get a FileSystemType by its name, or raise _ped.UnknownTypeException if no
    type by that name exists.
    """
    pass

def file_system_type_get_next(self): # real signature unknown; restored from __doc__
    """
    file_system_type_get_next(self) -> _ped.FileSystemType
    
    Get the next FileSystemType in parted's list after self, or raise IndexError
    if there are no more types.
    """
    pass

def libparted_version(): # real signature unknown; restored from __doc__
    """
    libparted_version() -> string
    
    Return the version of libparted that pyparted was built against.
    """
    return ""

def partition_flag_get_by_name(string): # real signature unknown; restored from __doc__
    """
    partition_flag_get_by_name(string) -> integer
    
    Return a partition flag given its name, or 0 if no flag matches the name.
    """
    return 0

def partition_flag_get_name(integer): # real signature unknown; restored from __doc__
    """
    partition_flag_get_name(integer) -> string
    
    Return a name for a partition flag constant.  If an invalid flag is provided,
    _ped.PartedExeption will be raised.
    """
    return ""

def partition_flag_next(integer): # real signature unknown; restored from __doc__
    """
    partition_flag_next(integer) -> integer
    
    Given a partition flag, return the next flag.  If there is no next flag, 0
    is returned.
    """
    return 0

def partition_type_get_name(integer): # real signature unknown; restored from __doc__
    """
    partition_type_get_name(integer) -> string
    
    Return a name for a partition type constant.  This mainly exists just to
    present something in user interfaces.  It doesn't really provide the best
    names for partition types.
    """
    return ""

def pyparted_version(): # real signature unknown; restored from __doc__
    """
    pyparted_version() -> (major, minor, update)
    
    Return the version of the pyparted module.
    """
    pass

def register_exn_handler(function): # real signature unknown; restored from __doc__
    """
    register_exn_handler(function)
    
    When parted raises an exception, the function registered here will be called
    to help determine what action to take.  This does not bypass the exception
    handler pyparted uses.  Instead, it can be used to pop up a dialog to ask the
    user which course of action to take, or to provide a different default answer,
    or other actions.
    
    The given function must accept as arguments:  (1) an integer corresponding to
    one of the EXCEPTION_TYPE_* constants; (2) an integer corresponding to one of the
    EXCEPTION_OPT_* constants; and (3) a string that is the problem encountered by
    parted.  This string will already be translated.  The given function must return
    one of the EXCEPTION_RESOLVE_* constants instructing parted how to proceed.
    """
    pass

def unit_get_by_name(string): # real signature unknown; restored from __doc__
    """
    unit_get_by_name(string) -> Unit
    
    Returns a Unit given its textual representation.  Returns one of the
    UNIT_* constants.
    """
    pass

def unit_get_default(): # real signature unknown; restored from __doc__
    """
    unit_get_default() -> Unit
    
    Returns the default Unit.
    """
    pass

def unit_get_name(Unit): # real signature unknown; restored from __doc__
    """
    unit_get_name(Unit) -> string
    
    Returns a textual representation of a given Unit.
    """
    return ""

def unit_set_default(Unit): # real signature unknown; restored from __doc__
    """
    unit_set_default(Unit)
    
    Sets the default Unit to be used by further unit_* calls.  This
    primarily affects the formatting of error messages.
    """
    pass

# classes

class Alignment(object):
    """
    A _ped.Alignment object describes constraints on how sectors and Geometry
    objects are aligned.  It includes a variety of methods for aligning sectors
    and calculating the intersection of two Alignment objects.  Most methods on
    this object can raise _ped.CreateException if creating temporary objects
    fails and ArithmeticError if calculating alignments and intersections fails.
    """
    def align_down(self, Geometry, Sector): # real signature unknown; restored from __doc__
        """
        align_down(self, Geometry, Sector) -> Sector
        
        Returns the closest Sector to the input Sector that lies inside Geometry
        and satisfies the alignment constraint.  This method prefers, but does not
        guarantee, that the result is below Sector.  If no such Sector can be
        found, an ArithmeticError is raised.
        """
        pass

    def align_nearest(self, Geometry, Sector): # real signature unknown; restored from __doc__
        """
        align_nearest(self, Geometry, Sector) -> Sector
        
        Returns the closest Sector to the input Sector that lies inside Geometry
        and satisfies the aligmnent constraint.  If no such Sector can be found,
        an ArithmeticError is raised.
        """
        pass

    def align_up(self, Geometry, Sector): # real signature unknown; restored from __doc__
        """
        align_up(self, Geometry, Sector) -> Sector
        
        Returns the closest Sector to the input Sector that lies inside Geometry
        and satisfies the alignment constraint.  This method prefers, but does not
        guarantee, that the result is beyond Sector.  If no such Sector can be
        found, an ArithmeticError is raised.
        """
        pass

    def duplicate(self): # real signature unknown; restored from __doc__
        """
        duplicate(self) -> _ped.Alignment
        
        Create an identical copy of self.  Raises _ped.CreateException if the
        operation fails
        """
        pass

    def intersect(self, Alignment): # real signature unknown; restored from __doc__
        """
        intersect(self, Alignment) -> _ped.Alignment
        
        Create a new Alignment that describes the intersection of self and
        Alignment.  A sector will satisfy the new Alignment iff it satisfies both
        of the original alignments, where 'satisfy' is determined by is_aligned().
        The proof of this is relatively complicated and is described thoroughly
        in the libparted source.  This method raises ArithmeticError if no
        intersection can be found.
        """
        pass

    def is_aligned(self, Geometry, Sector): # real signature unknown; restored from __doc__
        """
        is_aligned(self, Geometry, Sector) -> boolean
        
        Returns whether or not Sector lies inside Geometry and satisfies the
        alignment constraint.  This method defines what 'satisfy' means for
        intersection.
        """
        return False

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

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    grain_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alignment grain_size"""

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Offset in sectors from the start of a _ped.Geometry."""


    __hash__ = None


class AlignmentException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class CHSGeometry(object):
    """
    A _ped.CHSGeometry object describes a disk using the older CHS style
    of defining disk geometry.  CHS stands for cylinders-heads-sectors.
    
    The _ped.CHSGeometry objects are created automatically when devices are
    probed by libparted.  They are used for reference purposes to get the
    number of cylinders, heads, or sectors on a disk.  They cannot be used
    to change the CHS values on a device.
    """
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

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    cylinders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of cylinders."""

    heads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of heads"""

    sectors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of sectors"""


    __hash__ = None


class Constraint(object):
    """
    A _ped.Constraint object describes a set of restrictions on other pyparted
    operations.  Constraints can restrict the location and alignment of the start
    and end of a partition, and its minimum and maximum size.  Constraint
    operations include various methods of creating constraints, intersecting,
    and solving sets of constraints.
    
    Most constraint operations can raise _ped.CreateException if creating
    temporary objects fails, or ArithmeticError if an error occurrs during
    calculations.
    """
    def duplicate(self, Constraint): # real signature unknown; restored from __doc__
        """
        duplicate(Constraint) -> Constraint
        
        Return a new Constraint that is a copy of the given Constraint.
        """
        return Constraint

    def intersect(self, Constraint): # real signature unknown; restored from __doc__
        """
        intersect(Constraint) -> Constraint
        
        Return a Constraint that requires a region to satisfy both this
        Constraint object and the one passed in to the method.  Any
        region satisfying both Constraints will also satisfy the returned
        Constraint.
        """
        return Constraint

    def is_solution(self, Geometry): # real signature unknown; restored from __doc__
        """
        is_solution(Geometry) -> bool
        
        Return True if Geometry satisfies this Constraint, False otherwise.
        """
        return False

    def solve_max(self): # real signature unknown; restored from __doc__
        """
        solve_max() -> Constraint
        
        Find the largest region that satisfies this Constraint object and
        return a new Constraint.  There may be more than one solution.
        There are no guarantees about which solution will be returned.
        """
        return Constraint

    def solve_nearest(self, Geometry): # real signature unknown; restored from __doc__
        """
        solve_nearest(Geometry) -> Constraint
        
        Return the nearest region to Geometry that will satisfy this
        Constraint object.  This function does not guarantee what nearest
        means.
        """
        return Constraint

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

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    end_align = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The _ped.Alignment describing the ending alignment constraints of the partition."""

    end_range = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The _ped.Geometry describing the maximum size constraints of the partition."""

    max_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum size in _ped.Sectors of the partition."""

    min_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mimimum size in _ped.Sectors of the partition."""

    start_align = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The _ped.Alignment describing the starting alignment constraints of the partition."""

    start_range = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The _ped.Geometry describing the minimum size constraints of the partition."""


    __hash__ = None


class ConstraintException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class CreateException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Device(object):
    """
    A _ped.Device object describes a block device accessible via the
    operating system.  On Linux, an example block device is /dev/sda.
    
    It is important to note that _ped.Device objects describe entire
    block devices and not just partitions.
    """
    def begin_external_access(self, *args, **kwargs): # real signature unknown
        """
        begin_external_accessself() -> bool
        
        Begins external access mode for this Device.  External access mode allows
        you to safely do I/O on the device.  If a Device is open, then you should
        not do any I/O on that Device, e.g. by calling an external program like
        e2fsck, unless you put it in external access mode.  You should not use
        any commands that do I/O to a Device while it is in external access mode.
        
        Also, you should not close a Device while it is in external access mode.
        
        Return True if the Device was successfully put in external access mode,
        False otherwise.
        """
        pass

    def cache_remove(self): # real signature unknown; restored from __doc__
        """
        cache_remove(self) -> None
        
        Remove the Device from the device list, but does not destroy it or any
        allocated resources associated with it.  USE WITH CAUTION.
        """
        pass

    def check(self): # real signature unknown; restored from __doc__
        """
        check(self) -> long int
        
        Architecture-dependent function that returns the number of sectors on
        this Device that are ok.
        """
        return 0

    def clobber(self): # real signature unknown; restored from __doc__
        """
        clobber(self) -> boolean
        
        Remove all identifying information from a partition table.  If the partition
        table cannot be cleared, a _ped.DiskException is raised.
        """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """
        close(self) -> bool
        
        Close this Device.  All allocated resources are freed.  If a failure
        occurs while closing the Device, this method returns False.  The method
        returns True on success.
        """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """
        destroy(self) -> None
        
        Destroys the Device, removes it from the device list, destroys all
        allocated resources associated with it, and destroys the object.
        """
        pass

    def disk_probe(self): # real signature unknown; restored from __doc__
        """
        disk_probe(self) -> DiskType
        
        Return the type of partition table detected, or raise _ped.IOException if
        there is an error reading self.
        """
        return DiskType

    def end_external_access(self): # real signature unknown; restored from __doc__
        """
        end_external_access(self) -> bool
        
        Ends external access mode for this Device.  Returns True on success,
        False on failure.
        """
        return False

    def get_constraint(self): # real signature unknown; restored from __doc__
        """
        get_constraint(self) -> Constraint
        
        Get a constraint that represents hardware requirements on geometry.
        This method will return a constraint representing the limits imposed by
        the size of the disk, it will *not* provide any alignment constraints.
        
        Alignment constraints may be desirable when using media that have a
        physical sector size that is a multiple of the logical sector size, as
        in this case proper partition alignment can benefit disk performance
        signigicantly.
        """
        return Constraint

    def get_minimal_aligned_constraint(self): # real signature unknown; restored from __doc__
        """
        get_minimal_aligned_constraint(self) -> Constraint
        
        Get a constraint that represents hardware requirements on geometry and
        alignment. This method returns a constraint representing the limits
        imposed by the size of the disk and the minimal alignment requirements
        for proper performance of the disk.
        """
        return Constraint

    def get_minimum_alignment(self): # real signature unknown; restored from __doc__
        """
        get_minimum_alignment(self) -> Alignment
        
        Get an alignment that represents minimum hardware requirements on
        alignment. When for example using media that has a physical sector size
        that is a multiple of the logical sector size, it is desirable to have
        disk accesses (and thus partitions) properly aligned. Having partitions
        not aligned to the minimum hardware requirements may lead to a
        performance penalty.
        
        The returned alignment describes the alignment for the start sector of
        the partition, the end sector should be aligned too, to get the end
        sector alignment decrease the returned alignment's offset by 1.
        """
        return Alignment

    def get_optimal_aligned_constraint(self): # real signature unknown; restored from __doc__
        """
        get_optimal_aligned_constraint(self) -> Constraint
        
        Get a constraint that represents hardware requirements on geometry and
        alignment. This method returns a constraint representing the limits
        imposed by the size of the disk and the alignment requirements for
        optimal performance of the disk.
        """
        return Constraint

    def get_optimum_alignment(self): # real signature unknown; restored from __doc__
        """
        get_optimum_alignment(self) -> Alignment
        
        Get an alignment that represents the hardware requirements for optimal
        performance.
        
        The returned alignment describes the alignment for the start sector of
        the partition, the end sector should be aligned too, to get the end
        sector alignment decrease the returned alignment's offset by 1.
        """
        return Alignment

    def is_busy(self): # real signature unknown; restored from __doc__
        """
        is_busy(self) -> bool
        
        Return True if this Device is currently in use, False otherwise.
        """
        return False

    def open(self): # real signature unknown; restored from __doc__
        """
        open(self) -> bool
        
        Attempt to open this Device to allow use of read(), write(), and sync()
        methods.  The open() call is architecture-dependent.  Apart from
        requesting access to the device from the operating system, it does things
        flushing caches.
        
        This method may allocate internal resources depending on the architecture
        All allocated resources are freed when you call the close() method.
        
        Return True if the Device could be opened, False otherwise.
        """
        return False

    def read(self, start, count): # real signature unknown; restored from __doc__
        """
        read(self, start, count) -> bool
        
        Read and return count sectors from this Device, starting at sector start.
        Both start and count are long integers and buffer is a Python object large
        enough to hold what you want to read.
        """
        return False

    def sync(self): # real signature unknown; restored from __doc__
        """
        sync(self) -> bool
        
        Flushes all write-behind caches that might be holding up writes.  It is
        slow because it guarantees cache coherency among all relevant caches.
        Return True on success, False otherwise.
        """
        return False

    def sync_fast(self): # real signature unknown; restored from __doc__
        """
        sync_fast(self) -> bool
        
        Flushes all write-behind caches that might be holding writes.  WARNING:
        Does NOT ensure cache coherency with other caches.  If you need cache
        coherency, use sync() instead.  Return True on success, False otherwise.
        """
        return False

    def unit_format(self, Device, Sector): # real signature unknown; restored from __doc__
        """
        unit_format(Device, Sector) -> string
        
        Return a string that describes the location of Sector on self, as
        described by the default Unit.
        """
        return ""

    def unit_format_byte(self, Sector): # real signature unknown; restored from __doc__
        """
        unit_format_byte(Sector) -> string
        
        Return a string that describes the location of the byte Sector on
        self, as described by the default Unit.
        """
        return ""

    def unit_format_custom(self, Sector, Unit): # real signature unknown; restored from __doc__
        """
        unit_format_custom(Sector, Unit) -> string
        
        Return a string that describes the location of Sector on self, as
        described by Unit.  The Unit is any of the _ped.UNIT_* constants.
        """
        return ""

    def unit_format_custom_byte(self, Sector, Unit): # real signature unknown; restored from __doc__
        """
        unit_format_custom_byte(Sector, Unit) -> string
        
        Return a string that describes the location of the byte Sector on
        self, as described by Unit.  The Unit is any of the _ped.UNIT_*
        constants.
        """
        return ""

    def unit_get_size(self, Unit): # real signature unknown; restored from __doc__
        """
        unit_get_size(self, Unit) -> long
        
        Returns the byte size of self in the specified Unit.  The Unit
        is any of the _ped.UNIT_* constants.
        """
        return 0

    def unit_parse(self, string, Sector, Geometry): # real signature unknown; restored from __doc__
        """
        unit_parse(string, Sector, Geometry) -> boolean
        
        Given a string providing a valid description of a location on self,
        create a Geometry and Sector describing it.  Geometry will be two units
        large, centered on Sector.  If this makes the Geometry exist partially
        outside self, the Geometry will be intersected with the whole device
        geometry.  This uses the default unit.
        """
        return False

    def unit_parse_custom(self, *args, **kwargs): # real signature unknown
        """
        unit_parse(string, Unit, Sector, Geometry) -> boolean
        
        Follows the same description as unit_parse_doc, but takes a Unit as
        well.  The Unit is any of the _ped.UNIT_* constants.
        """
        pass

    def write(self, buffer, start, count): # real signature unknown; restored from __doc__
        """
        write(self, buffer, start, count) -> bool
        
        Write count sectors from buffer to this Device, starting at sector start.
        Both start and count are long integers and buffer is a Python object holding
        what you want to write to this Device.
        
        Return True if the write was successful, False otherwise.
        """
        return False

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

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    bios_geom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The CHSGeometry of the Device as reported by the BIOS."""

    boot_dirty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Have any unflushed changes been made to the bootloader?"""

    did = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Any SCSI device ID associated with self."""

    dirty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Have any unflushed changes been made to self?"""

    external_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PedDevice external_mode"""

    host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Any SCSI host ID associated with self."""

    hw_geom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The CHSGeometry of the Device as reported by the hardware."""

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Device length, in sectors (LBA)."""

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A brief description of the hardware, usually mfr and model."""

    open_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many times self.open() has been called."""

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The operating system level path to the device node."""

    phys_sector_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Physical sector size."""

    read_only = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is the device opened in read-only mode?"""

    sector_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Logical sector size."""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of device, deprecated in favor of PedDeviceType"""


    __hash__ = None


class DeviceException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Disk(object):
    """
    A _ped.Disk object represents a disk label, or partition table, on a single
    _ped.Device.  Since parted supports a variety of platforms, it must also
    support a variety of disk labels, not all of which may support the same set
    of features.  For instance, DOS disk labels support extended partitions while
    other systems do not.  The Disk object therefore includes a DiskType
    reference to enumerate supported features.  However, all other Disk operations
    are supported on all disk label types.
    
    Operations on Disk objects include creating, deleting, moving, and resizing
    partitions in various ways.  Creating filesystems within these partitions is
    left up to the FileSystem objects.
    
    For most errors involving a Disk object, _ped.PartitionException will be
    raised.  Some operations can also raise _ped.IOException or IndexError.
    """
    def add_partition(self, Partition, Constraint): # real signature unknown; restored from __doc__
        """
        add_partition(self, Partition, Constraint) -> boolean
        
        Adds the new partition Partition to self.  This operation may modify the
        partition's geometry, subject to Constraint.  Having a strict Constraint
        will likely cause this operation to fail, raising a _ped.PartitionException
        in the process.
        """
        return False

    def check(self): # real signature unknown; restored from __doc__
        """
        check(self) -> boolean
        
        Perform a basic sanity check on the partition table.  This check does not
        depend on the type of disk.  If there is an error performing the check,
        _ped.DiskException is raised.
        """
        return False

    def commit(self): # real signature unknown; restored from __doc__
        """
        commit(self) -> boolean
        
        Write the in-memory changes to the disk's partition table and inform the
        operating system of the changes.  This method is equivalent to calling:
        	self.disk_commit_to_dev()
        	self.disk_commit_to_os()
        On error, _ped.DiskException is raised.
        """
        return False

    def commit_to_dev(self): # real signature unknown; restored from __doc__
        """
        commit_to_dev(self) -> boolean
        
        Write the in-memory changes to the disk's partition table.  On error,
        _ped.DiskException is raised.
        """
        return False

    def commit_to_os(self): # real signature unknown; restored from __doc__
        """
        commit_to_os(self) -> boolean
        
        Inform the operating system that disk's partition table layout has changed.
        What exactly this means depends on the operating system.  On error, a
        _ped.DiskException is raised.
        """
        return False

    def delete_all(self): # real signature unknown; restored from __doc__
        """
        disk_delete_all(self) -> boolean
        
        Remove and destroy all partitions on self, raising _ped.PartitionException on
        any error case.
        """
        return False

    def delete_partition(self, Partition): # real signature unknown; restored from __doc__
        """
        delete_partition(self, Partition) -> boolean
        
        Remove Partition from self and destroy the Partition object afterwards.  This
        is equivalent to calling:
        	self.remove_partition(Partition)
        	Partition.destroy()
        For all error cases, _ped.PartitionException will be raised.
        """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """
        destroy(self) -> None
        
        Destroy the Disk object.
        """
        pass

    def duplicate(self): # real signature unknown; restored from __doc__
        """
        duplicate(self) -> Disk
        
        Return a new Disk that is a copy of self.  This method raises
        _ped.DiskException if there is an error making the copy.
        """
        return Disk

    def extended_partition(self): # real signature unknown; restored from __doc__
        """
        extended_partition(self) -> Partition
        
        If an extended partition exists on self, return it.  Otherwise, raise
        _ped.PartitionException
        """
        return Partition

    def get_flag(self, flag): # real signature unknown; restored from __doc__
        """
        get_flag(self, flag) -> boolean
        
        Return the state of the given flag on self.  There is no check for invalid
        flag types, so these will always return 0.  It is therefore recommended to
        call self.is_flag_available() first to make sure.
        """
        return False

    def get_last_partition_num(self): # real signature unknown; restored from __doc__
        """
        get_last_partition_num(self) -> integer
        
        Return the highest in-use partition number on self.
        """
        return 0

    def get_max_partition_geometry(self, Partition, Constraint): # real signature unknown; restored from __doc__
        """
        get_max_partition_geometry(self, Partition, Constraint) -> Geometry
        
        Return the maximum Geometry that Partition can be grown to, subject to the
        restrictions of Constraint.  Raise _ped.PartitionException on error.
        """
        return Geometry

    def get_max_primary_partition_count(self): # real signature unknown; restored from __doc__
        """
        get_max_primary_partition_count(self) -> integer
        
        Get the maximum number of primary partitions spported by the disk label.
        """
        return 0

    def get_max_supported_partition_count(self): # real signature unknown; restored from __doc__
        """
        get_max_supported_partition_count(self) -> integer
        
        Get the highest supported partition number of this disk.
        """
        return 0

    def get_partition(self, num): # real signature unknown; restored from __doc__
        """
        get_partition(self, num) -> Partition
        
        Return the Partition given by num, or raise _ped.PartitionException if no
        partition with that index exists.
        """
        return Partition

    def get_partition_alignment(self): # real signature unknown; restored from __doc__
        """
        get_partition_alignment(self) -> Alignment
        
        Get the alignment needed for partition boundaries on this disk.
        The returned alignment describes the alignment for the start sector
        of the partition, for all disklabel types which require alignment,
        except Sun disklabels, the end sector must be aligned too.
        To get the end sector alignment decrease the PedAlignment offset by 1.
        """
        return Alignment

    def get_partition_by_sector(self, sector): # real signature unknown; restored from __doc__
        """
        get_partition_by_sector(self, sector) -> Partition
        
        Return the Partition containing sector, or raise _ped.PartitionException
        otherwise.  If sector exists within a logical partition, the logical
        partition is returned.
        """
        return Partition

    def get_primary_partition_count(self): # real signature unknown; restored from __doc__
        """
        get_primary_partition_count(self) -> integer
        
        Return the number of primary partitions on self.
        """
        return 0

    def is_flag_available(self, flag): # real signature unknown; restored from __doc__
        """
        is_flag_available(self, flag) -> boolean
        
        Return whether the given flag is valid for self.
        """
        return False

    def maximize_partition(self, Partition, Constraint): # real signature unknown; restored from __doc__
        """
        maximize_partition(self, Partition, Constraint) -> boolean
        
        Grow the Partition to the largest possibly size, subject to the restrictions
        of Constraint.  Raise _ped.PartitionException on error.
        """
        return False

    def max_partition_length(self): # real signature unknown; restored from __doc__
        """
        max_partition_length(self) -> long
        
        This returns the maximum length for a partition the label on this disk
        can represent. This does not necessarily mean that there is enough
        freespace to create such a partition.
        If this information is not available 0 is returned
        """
        return 0

    def max_partition_start_sector(self): # real signature unknown; restored from __doc__
        """
        max_partition_start_sector(self) -> long
        
        This returns the maximum partition start sector the label on this disk
        can represent.
        If this information is not available 0 is returned
        """
        return 0

    def minimize_extended_partition(self): # real signature unknown; restored from __doc__
        """
        minimize_extended_partition(self) -> boolean
        
        Reduce the size of an extended partition on self to the minimum while still
        including all logical partitions.  If there are no logical partitions, the
        extended partition will be deleted.  If the extended partition cannot be
        shrunk, a _ped.PartitionException will be raised.
        """
        return False

    def next_partition(self, Partition): # real signature unknown; restored from __doc__
        """
        next_partition(self, Partition) -> Partition
        
        Return the next partition on self after Partition.  If Partition is None,
        return the first partition.  If Partition is an extended partition, return
        the first logical partition inside it.  If Partition is the last partition,
        raise IndexError.  Repeatedly calling this method has the effect of
        performing a depth-first traversal on self.
        """
        return Partition

    def remove_partition(self, Partition): # real signature unknown; restored from __doc__
        """
        remove_partition(self, Partition) -> boolean
        
        Remove Partition from self.  If Partition is an extended partition, it must
        not contain any logical partitions.  The Partition object itself is not
        destroyed.  The caller must use Partition.destroy() or self.delete_partition().
        For all error cases, _ped.PartitionException will be raised.
        """
        return False

    def set_flag(self, flag, state): # real signature unknown; restored from __doc__
        """
        set_flag(self, flag, state) -> boolean
        
        Sets the state of the given flag on self .
        If provided with an invalid flag for the disk's label,
        a PartedException is raised.
        """
        return False

    def set_partition_geom(self, Partition, Constraint, start_sector, end_sector): # real signature unknown; restored from __doc__
        """
        set_partition_geom(self, Partition, Constraint, start_sector, end_sector) ->
                          boolean
        
        Change the location of Partition by setting a new Geometry on it, subject to
        the restrictions of Constraint.  This operation can fail for many reasons,
        all of which result in a _ped.PartitionException.  One of the most likely
        failure cases is that the new location overlaps with an existing partition.
        On error, Partition will be unchanged.  On success, the contents of the
        partition will still not be changed - the file system itself will still
        need to be resized.
        """
        return False

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

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    dev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A _ped.Device object holding self's partition table."""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the disk label as a _ped.DiskType."""


    __hash__ = None


class DiskException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class DiskLabelException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class DiskType(object):
    """
    A _ped.DiskType object is a simple object that gives a partition table a
    name and describes features it supports.  A reference to one of these
    objects is stored inside a _ped.Disk object.
    """
    def check_feature(self, DiskTypeFeature): # real signature unknown; restored from __doc__
        """
        check_feature(self, DiskTypeFeature) -> boolean
        
        Return whether or not self supports a particular partition table feature.
        DiskTypeFeatures are given by the _ped.DISK_TYPE_* constants.
        """
        return False

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

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    features = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A bitmask of features supported by this DiskType."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the partition table type."""


    __hash__ = None


class FileSystem(object):
    """
    A _ped.FileSystem object describes a filesystem that exists in a given
    region on a device.  The region is given by a _ped.Geometry object, and
    the filesystem is further described by a _ped.FileSystemType object.
    
    Filesystem operations are especially prone to failures, and pyparted raises
    a variety of exceptions when error conditions are encountered.  The most
    common is _ped.FileSystemException, though _ped.IOException and
    _ped.CreateException may also be raised.
    """
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

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    geom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The on-disk region where this FileSystem object exists."""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A _ped.FileSystemType object describing the filesystem on self.geom."""


    __hash__ = None


class FileSystemException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class FileSystemType(object):
    """
    A _ped.FileSystemType object gives a name to a single filesystem that parted
    understands.  parted maintains a list of these objects which can be
    traversed with the self.get_next method or accessed directly via self.get().
    """
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

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the FileSystemType."""


    __hash__ = None


class Geometry(object):
    """
    A _ped.Geometry object describes a continuous region on a physical device.
    This device is given by the dev attribute when the Geometry is created.
    Most methods on this object involve creating new Geometry objects as needed
    and can therefore raise _ped.CreateException when an error occurs creating
    the new object.  Most methods can also raise _ped.IOException when reading
    or writing the underlying physical device fails.
    
    libparted (and therefore pyparted) attempts to enforce the following
    conditions on Geometry objects:
    
    	- start + length - 1 == end
    	- length > 0
    	- start >= 0
    	- end < dev.length
    """
    def check(self, offset, granularity, count, timer=None): # real signature unknown; restored from __doc__
        """
        check(self, offset, granularity, count, timer=None) -> Sector
        
        This method checks the region described by self for errors on the disk.
        The region to check starts at offset Sectors from the beginning of the
        region and is count Sectors long.  granularity specifies how Sectors should
        be grouped together.
        
        This method returns the first bad sector, or 0 if there are no errors.
        """
        pass

    def duplicate(self): # real signature unknown; restored from __doc__
        """
        duplicate(self) -> _ped.Geometry
        
        Create an identical copy of self.  Raises _ped.CreateException if the
        operation fails
        """
        pass

    def intersect(self, Geometry): # real signature unknown; restored from __doc__
        """
        intersect(self, Geometry) -> _ped.Geometry
        
        Create a new Geometry describing the region common to both self and
        Geometry.  Raises ArithmeticError if the two regions do not intersect.
        """
        pass

    def map(self, Geometry, Sector): # real signature unknown; restored from __doc__
        """
        map(self, Geometry, Sector) -> integer
        
        Given a Geometry that overlaps with self and a Sector inside Geometry,
        this method translates the address of Sector into an address inside self.
        The new address is returned, or ArithmeticError is raised if Sector does
        not exist within self.
        """
        return 0

    def read(self, buffer, offset, count): # real signature unknown; restored from __doc__
        """
        read(self, buffer, offset, count) -> boolean
        
        Read data from the region described by self.  This method reads count
        Sectors starting at Sector offset (from the start of the region, not
        from the start of the disk) into buffer.  This method raises
        _ped.IOException on error.
        """
        return False

    def set(self, start, length): # real signature unknown; restored from __doc__
        """
        set(self, start, length) -> boolean
        
        Sets a new start Sector and length Sector in the Geometry object,
        also implicitly setting the end Sector as well.
        """
        return False

    def set_end(self, end): # real signature unknown; restored from __doc__
        """
        set_end(self, end) -> boolean
        
        Sets a new ending Sector without modifying the start Sector.  Length
        will be modified to match the new ending position.
        """
        return False

    def set_start(self, start): # real signature unknown; restored from __doc__
        """
        set_start(self, start) -> boolean
        
        Sets a new start Sector without modifying the end Sector.  Length
        will be modified to match the new starting position.
        """
        return False

    def sync(self): # real signature unknown; restored from __doc__
        """
        sync(self) -> boolean
        
        Flushes all caches on the device described by self.  This operation can be
        slow because it must guarantee cache coherency among multiple caches.  This
        method raises _ped.IOException on error.
        """
        return False

    def sync_fast(self): # real signature unknown; restored from __doc__
        """
        sync_fast(self) -> boolean
        
        Flushes all caches on the device described by self without guaranteeing
        cache coherency.  This makes it fast but more prone to error.  This method
        raises _ped.IOException on error.
        """
        return False

    def test_equal(self, Geometry): # real signature unknown; restored from __doc__
        """
        test_equal(self, Geometry) -> boolean
        
        Return whether self and Geometry are on the same device and have the same
        region.
        """
        return False

    def test_inside(self, Geometry): # real signature unknown; restored from __doc__
        """
        test_inside(self, Geometry) -> boolean
        
        Return whether Geometry is entirely within self and on the same physical
        device.
        """
        return False

    def test_overlap(self, Geometry): # real signature unknown; restored from __doc__
        """
        test_overlap(self, Geometry) -> boolean
        
        Return whether self and Geometry are on the same physical device and
        share at least part of the same region.
        """
        return False

    def test_sector_inside(self, Sector): # real signature unknown; restored from __doc__
        """
        test_sector_inside(self, Sector) -> boolean
        
        Return whether Sector is entirely within the region described by self.
        """
        return False

    def write(self, buffer, offset, count): # real signature unknown; restored from __doc__
        """
        write(self, buffer, offset, count) -> boolean
        
        Write data into the region described by self.  This method writes count
        Sectors of buffer into the region starting at Sector offset.  The offset is
        from the beginning of the region, not of the disk.  This method raises
        _ped.IOException on error.
        """
        return False

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

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    dev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The _ped.Device described by this _ped.Geometry object."""

    end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ending Sector of the region."""

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of the region described by this Geometry object."""

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The starting Sector of the region."""


    __hash__ = None


class GeometryException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class IOException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class NotNeededException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class PartedException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Partition(object):
    """
    A _ped.Partition object describes a single partition on a disk.  Operations
    on Partition objects are limited to getting and setting flags, names, and
    paths.  All other operations you may wish to do involving partitions are
    done through a _ped.Disk or _ped.FileSystem object.  These objects all exist
    as attributes of a Partition, though.
    
    Valid flags for Partitions are given by the _ped.PARTITION_* constants,
    though not all flags are valid for every disk label type.
    
    For most errors involving a Partition object, _ped.PartitionException will
    be raised.
    """
    def destroy(self): # real signature unknown; restored from __doc__
        """
        destroy(self) -> None
        
        Destroys the Partition object.
        """
        pass

    def get_flag(self, flag): # real signature unknown; restored from __doc__
        """
        get_flag(self, flag) -> integer
        
        Return the state of the given flag on self.  There is no check for invalid
        flag types, so these will always return 0.  It is therefore recommended to
        call self.is_flag_available() first to make sure.
        """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """
        get_name(self) -> string
        
        On disk labels that support it, this method returns the partition's name.  On
        all other disk labels, _ped.PartitionException will be raised.  Before calling
        this method, DiskType.check_feature() can be called to check for support.
        """
        return ""

    def get_path(self): # real signature unknown; restored from __doc__
        """
        get_path(self) -> string
        
        Return a path that could be used for addressing self at an operating system
        level.  For instance, on Linux this could return '/dev/sda' for a partition.
        If an error occurs, _ped.PartitionException is raised.
        """
        return ""

    def is_active(self): # real signature unknown; restored from __doc__
        """
        is_active(self) -> boolean
        
        Return whether self is active or not.
        """
        return False

    def is_busy(self): # real signature unknown; restored from __doc__
        """
        is_busy(self) -> boolean
        
        Return whether self is busy or not.  The most likely reason for a partition
        to be busy is because it's mounted.  Additionally, extended partitions are
        busy if any of their logical partitions are busy.
        """
        return False

    def is_flag_available(self, flag): # real signature unknown; restored from __doc__
        """
        is_flag_available(self, flag) -> boolean
        
        Return whether the given flag is valid for self.
        """
        return False

    def reset_num(self): # real signature unknown; restored from __doc__
        """
        reset_num(self) -> boolean
        
        Reset the partition's number to value allowing it to be set correctly when
        the partition is added to _ped.PartedDisk. The returned value means
        success/failure
        """
        return False

    def set_flag(self, flag, state): # real signature unknown; restored from __doc__
        """
        set_flag(self, flag, state) -> boolean
        
        Sets the state of the given flag on self .  Flags have different types of
        different types of disk labels, and are not guaranteed to exist on all disk
        label types.  If provided with an invalid flag for the disk's label,
        _ped.PartitionException is raised.
        """
        return False

    def set_name(self, string): # real signature unknown; restored from __doc__
        """
        set_name(self, string) -> boolean
        
        On disk labels that support it, this method sets the partition's name.
        Before attempting this operation, DiskType.check_feature() can be used to
        determine if it is even supported.  On error, _ped.PartitionException will
        be raised.
        """
        return False

    def set_system(self, FileSystemType): # real signature unknown; restored from __doc__
        """
        set_system(self, FileSystemType) -> boolean
        
        Set the system type on self to FileSystemType.  On error,
        _ped.PartitionException is raised.
        """
        return False

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

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    disk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The _ped.Disk this Partition exists on."""

    fs_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A _ped.FileSystemType object describing the filesystem on this Partition."""

    geom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A _ped.Geometry object describing the region this Partition occupies."""

    num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of this Partition on self.disk."""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PedPartition type"""


    __hash__ = None


class PartitionException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Timer(object):
    """ PedTimer objects """
    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def destroy_nested(self, *args, **kwargs): # real signature unknown
        pass

    def new_nested(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def set_state_name(self, *args, **kwargs): # real signature unknown
        pass

    def touch(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
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

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    frac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PedTimer frac"""

    now = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PedTimer.now"""

    predicted_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PedTimer.predicted_end"""

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PedTimer.start"""

    state_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PedTimer.state_name"""


    __hash__ = None


class TimerException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class UnknownDeviceException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class UnknownTypeException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



