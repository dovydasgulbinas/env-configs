# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/nbt.so
# by generator 1.143
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

AnnouncementRequest = 2

BecomeBackup = 11

DGRAM_BCAST = 18

DGRAM_DIRECT_GROUP = 17
DGRAM_DIRECT_UNIQUE = 16

DGRAM_ERROR = 19

DGRAM_ERROR_INVALID_DEST = 132
DGRAM_ERROR_INVALID_SOURCE = 131

DGRAM_ERROR_NAME_NOT_PRESENT = 130

DGRAM_FLAG_FIRST = 2
DGRAM_FLAG_MORE = 1

DGRAM_FLAG_NODE_TYPE = 12

DGRAM_NODE_B = 0
DGRAM_NODE_M = 8
DGRAM_NODE_NBDD = 12
DGRAM_NODE_P = 4

DGRAM_QUERY = 20

DGRAM_QUERY_NEGATIVE = 22
DGRAM_QUERY_POSITIVE = 21

DGRAM_SMB = 4283649346

DomainAnnouncement = 12

Election = 8

GetBackupListReq = 9
GetBackupListResp = 10

HostAnnouncement = 1

LocalMasterAnnouncement = 15

LOGON_PRIMARY_QUERY = 7

LOGON_REQUEST = 0
LOGON_RESPONSE2 = 6

LOGON_SAM_LOGON_PAUSE_RESPONSE = 20

LOGON_SAM_LOGON_PAUSE_RESPONSE_EX = 24

LOGON_SAM_LOGON_REQUEST = 18
LOGON_SAM_LOGON_RESPONSE = 19

LOGON_SAM_LOGON_RESPONSE_EX = 23

LOGON_SAM_LOGON_USER_UNKNOWN = 21

LOGON_SAM_LOGON_USER_UNKNOWN_EX = 25

MasterAnnouncement = 13

NBT_DGRAM_SERVICE_PORT = 138

NBT_FLAG_AUTHORITATIVE = 1024
NBT_FLAG_BROADCAST = 16

NBT_FLAG_RECURSION_AVAIL = 128
NBT_FLAG_RECURSION_DESIRED = 256

NBT_FLAG_REPLY = 32768
NBT_FLAG_TRUNCATION = 512

NBT_MAILSLOT_BROWSE = '\\MAILSLOT\\BROWSE'
NBT_MAILSLOT_GETDC = '\\MAILSLOT\\NET\\GETDC'
NBT_MAILSLOT_NETLOGON = '\\MAILSLOT\\NET\\NETLOGON'
NBT_MAILSLOT_NTLOGON = '\\MAILSLOT\\NET\\NTLOGON'

NBT_NAME_BROWSER = 30
NBT_NAME_CLIENT = 0
NBT_NAME_LOGON = 28
NBT_NAME_MASTER = 29
NBT_NAME_MS = 1
NBT_NAME_PDC = 27
NBT_NAME_SERVER = 32

NBT_NAME_SERVICE_PORT = 137

NBT_NAME_USER = 3

NBT_NM_ACTIVE = 1024
NBT_NM_CONFLICT = 2048
NBT_NM_DEREGISTER = 4096
NBT_NM_GROUP = 32768

NBT_NM_OWNER_TYPE = 24576

NBT_NM_PERMANENT = 512

NBT_NODE_B = 0
NBT_NODE_H = 24576
NBT_NODE_M = 16384
NBT_NODE_P = 8192

NBT_OPCODE = 30720

NBT_OPCODE_MULTI_HOME_REG = 30720

NBT_OPCODE_QUERY = 0
NBT_OPCODE_REFRESH = 16384
NBT_OPCODE_REFRESH2 = 18432
NBT_OPCODE_REGISTER = 10240
NBT_OPCODE_RELEASE = 12288
NBT_OPCODE_WACK = 14336

NBT_QCLASS_IP = 1

NBT_QTYPE_ADDRESS = 1
NBT_QTYPE_NAMESERVICE = 2
NBT_QTYPE_NETBIOS = 32
NBT_QTYPE_NULL = 10
NBT_QTYPE_STATUS = 33

NBT_RCODE = 15

NBT_RCODE_ACT = 6
NBT_RCODE_CFT = 7
NBT_RCODE_FMT = 1
NBT_RCODE_IMP = 4
NBT_RCODE_NAM = 3
NBT_RCODE_OK = 0
NBT_RCODE_RFS = 5
NBT_RCODE_SVR = 2

NBT_SERVER_ADS_WEB_SERVICE = 8192

NBT_SERVER_CLOSEST = 128
NBT_SERVER_DS = 16

NBT_SERVER_DS_8 = 16384

NBT_SERVER_FOREST_ROOT = 2147483648

NBT_SERVER_FULL_SECRET_DOMAIN_6 = 4096

NBT_SERVER_GC = 4

NBT_SERVER_GOOD_TIMESERV = 512

NBT_SERVER_HAS_DNS_NAME = 536870912

NBT_SERVER_IS_DEFAULT_NC = 1073741824

NBT_SERVER_KDC = 32
NBT_SERVER_LDAP = 8
NBT_SERVER_NDNC = 1024
NBT_SERVER_PDC = 1

NBT_SERVER_SELECT_SECRET_DOMAIN_6 = 2048

NBT_SERVER_TIMESERV = 64
NBT_SERVER_WRITABLE = 256

NETLOGON_ANNOUNCE_UAS = 10

NETLOGON_NT_VERSION_1 = 1
NETLOGON_NT_VERSION_5 = 2
NETLOGON_NT_VERSION_5EX = 4

NETLOGON_NT_VERSION_5EX_WITH_IP = 8

NETLOGON_NT_VERSION_AVOID_NT4EMUL = 16777216

NETLOGON_NT_VERSION_GC = 2147483648
NETLOGON_NT_VERSION_IP = 536870912
NETLOGON_NT_VERSION_LOCAL = 1073741824
NETLOGON_NT_VERSION_PDC = 268435456

NETLOGON_NT_VERSION_WITH_CLOSEST_SITE = 16

NETLOGON_RESPONSE_FROM_PDC = 12

ResetBrowserState = 14

SMB_TRANSACTION = 37

# no functions
# classes

from abstract_syntax import abstract_syntax
from browse_announcement_request import browse_announcement_request
from browse_backup_list_request import browse_backup_list_request
from browse_backup_list_response import browse_backup_list_response
from browse_become_backup import browse_become_backup
from browse_domain_announcement import browse_domain_announcement
from browse_election_request import browse_election_request
from browse_host_announcement import browse_host_announcement
from browse_local_master_announcement import browse_local_master_announcement
from browse_master_announcement import browse_master_announcement
from browse_packet import browse_packet
from browse_reset_state import browse_reset_state
from db_change_info import db_change_info
from dgram_message import dgram_message
from dgram_packet import dgram_packet
from dgram_smb_packet import dgram_smb_packet
from name import name
from name_packet import name_packet
from name_question import name_question
from nbt import nbt
from NETLOGON_DB_CHANGE import NETLOGON_DB_CHANGE
from NETLOGON_LOGON_REQUEST import NETLOGON_LOGON_REQUEST
from netlogon_packet import netlogon_packet
from netlogon_query_for_pdc import netlogon_query_for_pdc
from netlogon_response2 import netlogon_response2
from netlogon_response_from_pdc import netlogon_response_from_pdc
from NETLOGON_SAM_LOGON_REQUEST import NETLOGON_SAM_LOGON_REQUEST
from NETLOGON_SAM_LOGON_RESPONSE import NETLOGON_SAM_LOGON_RESPONSE
from NETLOGON_SAM_LOGON_RESPONSE_EX import NETLOGON_SAM_LOGON_RESPONSE_EX
from NETLOGON_SAM_LOGON_RESPONSE_NT40 import NETLOGON_SAM_LOGON_RESPONSE_NT40
from rdata_address import rdata_address
from rdata_data import rdata_data
from rdata_netbios import rdata_netbios
from rdata_status import rdata_status
from res_rec import res_rec
from smb_trans_body import smb_trans_body
from sockaddr import sockaddr
from statistics import statistics
from status_name import status_name
