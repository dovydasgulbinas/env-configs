# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/nbt.so
# by generator 1.143
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class statistics(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    jumpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_number_pending_sessions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_total_number_command_blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_total_sessions_possible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number_alignment_errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number_free_command_blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number_good_receives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number_good_sends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number_no_resource_conditions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number_of_collisions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number_of_crcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number_pending_sessions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number_retransmits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number_send_aborts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    period_of_statistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    session_data_packet_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    test_result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_number_command_blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unit_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



