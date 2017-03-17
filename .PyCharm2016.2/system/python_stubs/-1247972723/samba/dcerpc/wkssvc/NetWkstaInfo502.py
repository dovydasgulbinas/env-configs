# encoding: utf-8
# module samba.dcerpc.wkssvc
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/wkssvc.so
# by generator 1.143
""" wkssvc DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class NetWkstaInfo502(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    buf_files_deny_write = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buf_named_pipes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buf_read_only_files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cache_file_timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    char_wait = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collection_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dgram_event_reset_freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dormant_file_limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    force_core_create_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keep_connection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock_increment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock_maximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock_quota = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    log_election_packets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maximum_collection_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_commands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_illegal_dgram_events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_mailslot_buffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_srv_announce_buffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pipe_increment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pipe_maximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_ahead_throughput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    session_timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size_char_buf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_512_byte_max_transfer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_close_behind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_encryption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_lock_read_unlock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_opportunistic_locking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_raw_read = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_raw_write = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_unlock_behind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_write_raw_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    utilize_nt_caching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



