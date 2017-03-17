# encoding: utf-8
# module samba.dcerpc.epmapper
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/epmapper.so
# by generator 1.143
""" epmapper DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

EPMAPPER_STATUS_CANT_PERFORM_OP = 1752

EPMAPPER_STATUS_NO_MEMORY = 382312466

EPMAPPER_STATUS_NO_MORE_ENTRIES = 382312662

EPMAPPER_STATUS_OK = 0

EPM_PROTOCOL_APPLETALK = 24
EPM_PROTOCOL_DDP = 23

EPM_PROTOCOL_DNET_NSP = 4

EPM_PROTOCOL_DSP = 22
EPM_PROTOCOL_HTTP = 31
EPM_PROTOCOL_IP = 9
EPM_PROTOCOL_IPX = 14

EPM_PROTOCOL_NAMED_PIPE = 16

EPM_PROTOCOL_NB_IPX = 20

EPM_PROTOCOL_NCACN = 11
EPM_PROTOCOL_NCADG = 10
EPM_PROTOCOL_NCALRPC = 12
EPM_PROTOCOL_NETBEUI = 18
EPM_PROTOCOL_NETBIOS = 17
EPM_PROTOCOL_NULL = 33

EPM_PROTOCOL_OSI_CLNS = 6
EPM_PROTOCOL_OSI_TP4 = 5

EPM_PROTOCOL_SMB = 15
EPM_PROTOCOL_SPX = 19
EPM_PROTOCOL_STREETTALK = 28
EPM_PROTOCOL_TCP = 7
EPM_PROTOCOL_UDP = 8

EPM_PROTOCOL_UNIX_DS = 32

EPM_PROTOCOL_UUID = 13

EPM_PROTOCOL_VINES_IPC = 27
EPM_PROTOCOL_VINES_SPP = 26

RPC_C_EP_ALL_ELTS = 0

RPC_C_EP_MATCH_BY_BOTH = 3
RPC_C_EP_MATCH_BY_IF = 1
RPC_C_EP_MATCH_BY_OBJ = 2

RPC_C_VERS_ALL = 0
RPC_C_VERS_COMPATIBLE = 1
RPC_C_VERS_EXACT = 2

RPC_C_VERS_MAJOR_ONLY = 3

RPC_C_VERS_UPTO = 4

# no functions
# classes

from abstract_syntax import abstract_syntax
from epmapper import epmapper
from epm_entry_t import epm_entry_t
from epm_floor import epm_floor
from epm_lhs import epm_lhs
from epm_rhs_appletalk import epm_rhs_appletalk
from epm_rhs_atalk_datagram import epm_rhs_atalk_datagram
from epm_rhs_atalk_stream import epm_rhs_atalk_stream
from epm_rhs_dnet_nsp import epm_rhs_dnet_nsp
from epm_rhs_http import epm_rhs_http
from epm_rhs_ip import epm_rhs_ip
from epm_rhs_ipx import epm_rhs_ipx
from epm_rhs_named_pipe import epm_rhs_named_pipe
from epm_rhs_nb_ipx import epm_rhs_nb_ipx
from epm_rhs_ncacn import epm_rhs_ncacn
from epm_rhs_ncadg import epm_rhs_ncadg
from epm_rhs_ncalrpc import epm_rhs_ncalrpc
from epm_rhs_netbeui import epm_rhs_netbeui
from epm_rhs_netbios import epm_rhs_netbios
from epm_rhs_null import epm_rhs_null
from epm_rhs_osi_clns import epm_rhs_osi_clns
from epm_rhs_osi_tp4 import epm_rhs_osi_tp4
from epm_rhs_smb import epm_rhs_smb
from epm_rhs_spx import epm_rhs_spx
from epm_rhs_streettalk import epm_rhs_streettalk
from epm_rhs_tcp import epm_rhs_tcp
from epm_rhs_udp import epm_rhs_udp
from epm_rhs_unix_ds import epm_rhs_unix_ds
from epm_rhs_uuid import epm_rhs_uuid
from epm_rhs_vines_ipc import epm_rhs_vines_ipc
from epm_rhs_vines_spp import epm_rhs_vines_spp
from epm_tower import epm_tower
from epm_twr_p_t import epm_twr_p_t
from epm_twr_t import epm_twr_t
from rpc_if_id_t import rpc_if_id_t
