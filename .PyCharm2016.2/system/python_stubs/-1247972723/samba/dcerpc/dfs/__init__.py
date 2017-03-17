# encoding: utf-8
# module samba.dcerpc.dfs
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/dfs.so
# by generator 1.143
""" dfs DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

DFS_GLOBAL_HIGH_PRIORITY_CLASS = 1

DFS_GLOBAL_LOW_PRIORITY_CLASS = 4

DFS_INVALID_PRIORITY_CLASS = 4294967295

DFS_MANAGER_VERSION_NT4 = 1
DFS_MANAGER_VERSION_W2K = 2
DFS_MANAGER_VERSION_W2K3 = 4
DFS_MANAGER_VERSION_W2K8 = 6

DFS_PROPERTY_FLAG_CLUSTER_ENABLED = 16

DFS_PROPERTY_FLAG_INSITE_REFERRALS = 1

DFS_PROPERTY_FLAG_ROOT_SCALABILITY = 2

DFS_PROPERTY_FLAG_SITE_COSTING = 4

DFS_PROPERTY_FLAG_TARGET_FAILBACK = 8

DFS_SITE_COST_HIGH_PRIORITY_CLASS = 2

DFS_SITE_COST_LOW_PRIORITY_CLASS = 3

DFS_SITE_COST_NORMAL_PRIORITY_CLASS = 0

DFS_STORAGE_STATES = 15

DFS_STORAGE_STATE_ACTIVE = 4
DFS_STORAGE_STATE_OFFLINE = 1
DFS_STORAGE_STATE_ONLINE = 2

DFS_VOLUME_FLAVOR_AD_BLOB = 512

DFS_VOLUME_FLAVOR_STANDALONE = 256

DFS_VOLUME_STATE_AD_BLOB = 512

DFS_VOLUME_STATE_INCONSISTENT = 2
DFS_VOLUME_STATE_OFFLINE = 3
DFS_VOLUME_STATE_OK = 1
DFS_VOLUME_STATE_ONLINE = 4
DFS_VOLUME_STATE_STANDALONE = 256

# no functions
# classes

from abstract_syntax import abstract_syntax
from EnumArray1 import EnumArray1
from EnumArray2 import EnumArray2
from EnumArray200 import EnumArray200
from EnumArray3 import EnumArray3
from EnumArray300 import EnumArray300
from EnumArray4 import EnumArray4
from EnumArray5 import EnumArray5
from EnumArray6 import EnumArray6
from EnumStruct import EnumStruct
from Info0 import Info0
from Info1 import Info1
from Info100 import Info100
from Info101 import Info101
from Info102 import Info102
from Info103 import Info103
from Info104 import Info104
from Info105 import Info105
from Info106 import Info106
from Info2 import Info2
from Info200 import Info200
from Info3 import Info3
from Info300 import Info300
from Info4 import Info4
from Info5 import Info5
from Info6 import Info6
from Info7 import Info7
from netdfs import netdfs
from StorageInfo import StorageInfo
from StorageInfo2 import StorageInfo2
from Target_Priority import Target_Priority
from UnknownStruct import UnknownStruct
