# encoding: utf-8
# module samba.dcerpc.atsvc
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/atsvc.so
# by generator 1.143
""" atsvc DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

DAYSOFWEEK_FRIDAY = 16
DAYSOFWEEK_MONDAY = 1
DAYSOFWEEK_SATURDAY = 32
DAYSOFWEEK_SUNDAY = 64
DAYSOFWEEK_THURSDAY = 8
DAYSOFWEEK_TUESDAY = 2
DAYSOFWEEK_WEDNESDAY = 4

Eight = 128
Eighteenth = 131072

Eleventh = 1024

Fifteenth = 16384
Fifth = 16
First = 1

Fourteenth = 8192
Fourth = 8

JOB_ADD_CURRENT_DATE = 8

JOB_EXEC_ERROR = 2

JOB_NONINTERACTIVE = 16

JOB_RUNS_TODAY = 4

JOB_RUN_PERIODICALLY = 1

Ninteenth = 262144
Ninth = 256

Second = 2
Seventeenth = 65536
Seventh = 64

Sixteenth = 32768
Sixth = 32

Tenth = 512

Third = 4
Thirtieth = 536870912
Thirtyfirst = 1073741824
Thitteenth = 4096

Twelfth = 2048
Twentyeighth = 134217728
Twentyfifth = 16777216
Twentyfirst = 1048576
Twentyfourth = 8388608
Twentyninth = 268435456
Twentysecond = 2097152
Twentyseventh = 67108864
Twentysixth = 33554432
Twentyth = 524288
Twentythird = 4194304

# no functions
# classes

class abstract_syntax(__misc.ndr_syntax_id):
    """
    abstract_syntax()
    Microsoft AT-Scheduler Service
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class atsvc(__dcerpc.ClientConnection):
    """
    atsvc(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Microsoft AT-Scheduler Service
    """
    def JobAdd(self, servername, job_info): # real signature unknown; restored from __doc__
        """ S.JobAdd(servername, job_info) -> job_id """
        pass

    def JobDel(self, servername, min_job_id, max_job_id): # real signature unknown; restored from __doc__
        """ S.JobDel(servername, min_job_id, max_job_id) -> None """
        pass

    def JobEnum(self, servername, ctr, preferred_max_len, resume_handle): # real signature unknown; restored from __doc__
        """ S.JobEnum(servername, ctr, preferred_max_len, resume_handle) -> (ctr, total_entries, resume_handle) """
        pass

    def JobGetInfo(self, servername, job_id): # real signature unknown; restored from __doc__
        """ S.JobGetInfo(servername, job_id) -> job_info """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class enum_ctr(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    entries_read = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_entry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class JobEnumInfo(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_of_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_of_week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    job_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    job_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class JobInfo(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_of_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_of_week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    job_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



