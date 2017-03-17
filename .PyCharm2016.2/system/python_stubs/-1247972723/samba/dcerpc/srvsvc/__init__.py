# encoding: utf-8
# module samba.dcerpc.srvsvc
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/srvsvc.so
# by generator 1.143
""" srvsvc DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

PLATFORM_ID_DOS = 300
PLATFORM_ID_NT = 500
PLATFORM_ID_OS2 = 400
PLATFORM_ID_OSF = 600
PLATFORM_ID_VMS = 700

SHARE_1005_ACCESS_BASED_DIRECTORY_ENUM = 2048

SHARE_1005_ALLOW_NAMESPACE_CACHING = 1024

SHARE_1005_CSC_CACHE_AUTO_REINT = 16

SHARE_1005_CSC_CACHE_MANUAL_REINT = 0

SHARE_1005_CSC_CACHE_NONE = 48
SHARE_1005_CSC_CACHE_VDO = 32

SHARE_1005_CSC_POLICY_MASK = 48
SHARE_1005_CSC_POLICY_SHIFT = 4

SHARE_1005_DFS_ROOT = 2

SHARE_1005_ENABLE_CA = 16384
SHARE_1005_ENABLE_HASH = 8192

SHARE_1005_ENCRYPT_DATA = 32768

SHARE_1005_FORCE_LEVELII_OPLOCK = 4096

SHARE_1005_FORCE_SHARED_DELETE = 512

SHARE_1005_IN_DFS = 1

SHARE_1005_RESTRICT_EXCLUSIVE_OPENS = 256

STYPE_CLUSTER_DFS = 134217728

STYPE_CLUSTER_DFS_HIDDEN = 2281701376
STYPE_CLUSTER_DFS_TEMPORARY = 1207959552

STYPE_CLUSTER_FS = 33554432

STYPE_CLUSTER_FS_HIDDEN = 2181038080
STYPE_CLUSTER_FS_TEMPORARY = 1107296256

STYPE_CLUSTER_SOFS = 67108864

STYPE_CLUSTER_SOFS_HIDDEN = 2214592512
STYPE_CLUSTER_SOFS_TEMPORARY = 1140850688

STYPE_DEVICE = 2

STYPE_DEVICE_HIDDEN = 2147483650
STYPE_DEVICE_TEMPORARY = 1073741826

STYPE_DISKTREE = 0

STYPE_DISKTREE_HIDDEN = 2147483648
STYPE_DISKTREE_TEMPORARY = 1073741824

STYPE_HIDDEN = 2147483648
STYPE_IPC = 3

STYPE_IPC_HIDDEN = 2147483651
STYPE_IPC_TEMPORARY = 1073741827

STYPE_PRINTQ = 1

STYPE_PRINTQ_HIDDEN = 2147483649
STYPE_PRINTQ_TEMPORARY = 1073741825

STYPE_TEMPORARY = 1073741824

# no functions
# classes

from abstract_syntax import abstract_syntax
from NetCharDevCtr0 import NetCharDevCtr0
from NetCharDevCtr1 import NetCharDevCtr1
from NetCharDevInfo0 import NetCharDevInfo0
from NetCharDevInfo1 import NetCharDevInfo1
from NetCharDevInfoCtr import NetCharDevInfoCtr
from NetCharDevQCtr0 import NetCharDevQCtr0
from NetCharDevQCtr1 import NetCharDevQCtr1
from NetCharDevQInfo0 import NetCharDevQInfo0
from NetCharDevQInfo1 import NetCharDevQInfo1
from NetCharDevQInfoCtr import NetCharDevQInfoCtr
from NetConnCtr0 import NetConnCtr0
from NetConnCtr1 import NetConnCtr1
from NetConnInfo0 import NetConnInfo0
from NetConnInfo1 import NetConnInfo1
from NetConnInfoCtr import NetConnInfoCtr
from NetDiskInfo import NetDiskInfo
from NetDiskInfo0 import NetDiskInfo0
from NetFileCtr2 import NetFileCtr2
from NetFileCtr3 import NetFileCtr3
from NetFileInfo2 import NetFileInfo2
from NetFileInfo3 import NetFileInfo3
from NetFileInfoCtr import NetFileInfoCtr
from NetRemoteTODInfo import NetRemoteTODInfo
from NetSessCtr0 import NetSessCtr0
from NetSessCtr1 import NetSessCtr1
from NetSessCtr10 import NetSessCtr10
from NetSessCtr2 import NetSessCtr2
from NetSessCtr502 import NetSessCtr502
from NetSessInfo0 import NetSessInfo0
from NetSessInfo1 import NetSessInfo1
from NetSessInfo10 import NetSessInfo10
from NetSessInfo2 import NetSessInfo2
from NetSessInfo502 import NetSessInfo502
from NetSessInfoCtr import NetSessInfoCtr
from NetShareCtr0 import NetShareCtr0
from NetShareCtr1 import NetShareCtr1
from NetShareCtr1004 import NetShareCtr1004
from NetShareCtr1005 import NetShareCtr1005
from NetShareCtr1006 import NetShareCtr1006
from NetShareCtr1007 import NetShareCtr1007
from NetShareCtr1501 import NetShareCtr1501
from NetShareCtr2 import NetShareCtr2
from NetShareCtr501 import NetShareCtr501
from NetShareCtr502 import NetShareCtr502
from NetShareInfo0 import NetShareInfo0
from NetShareInfo1 import NetShareInfo1
from NetShareInfo1004 import NetShareInfo1004
from NetShareInfo1005 import NetShareInfo1005
from NetShareInfo1006 import NetShareInfo1006
from NetShareInfo1007 import NetShareInfo1007
from NetShareInfo2 import NetShareInfo2
from NetShareInfo501 import NetShareInfo501
from NetShareInfo502 import NetShareInfo502
from NetShareInfoCtr import NetShareInfoCtr
from NetSrvInfo100 import NetSrvInfo100
from NetSrvInfo1005 import NetSrvInfo1005
from NetSrvInfo101 import NetSrvInfo101
from NetSrvInfo1010 import NetSrvInfo1010
from NetSrvInfo1016 import NetSrvInfo1016
from NetSrvInfo1017 import NetSrvInfo1017
from NetSrvInfo1018 import NetSrvInfo1018
from NetSrvInfo102 import NetSrvInfo102
from NetSrvInfo1107 import NetSrvInfo1107
from NetSrvInfo1501 import NetSrvInfo1501
from NetSrvInfo1502 import NetSrvInfo1502
from NetSrvInfo1503 import NetSrvInfo1503
from NetSrvInfo1506 import NetSrvInfo1506
from NetSrvInfo1509 import NetSrvInfo1509
from NetSrvInfo1510 import NetSrvInfo1510
from NetSrvInfo1511 import NetSrvInfo1511
from NetSrvInfo1512 import NetSrvInfo1512
from NetSrvInfo1513 import NetSrvInfo1513
from NetSrvInfo1514 import NetSrvInfo1514
from NetSrvInfo1515 import NetSrvInfo1515
from NetSrvInfo1516 import NetSrvInfo1516
from NetSrvInfo1518 import NetSrvInfo1518
from NetSrvInfo1520 import NetSrvInfo1520
from NetSrvInfo1521 import NetSrvInfo1521
from NetSrvInfo1522 import NetSrvInfo1522
from NetSrvInfo1523 import NetSrvInfo1523
from NetSrvInfo1524 import NetSrvInfo1524
from NetSrvInfo1525 import NetSrvInfo1525
from NetSrvInfo1528 import NetSrvInfo1528
from NetSrvInfo1529 import NetSrvInfo1529
from NetSrvInfo1530 import NetSrvInfo1530
from NetSrvInfo1533 import NetSrvInfo1533
from NetSrvInfo1534 import NetSrvInfo1534
from NetSrvInfo1535 import NetSrvInfo1535
from NetSrvInfo1536 import NetSrvInfo1536
from NetSrvInfo1537 import NetSrvInfo1537
from NetSrvInfo1538 import NetSrvInfo1538
from NetSrvInfo1539 import NetSrvInfo1539
from NetSrvInfo1540 import NetSrvInfo1540
from NetSrvInfo1541 import NetSrvInfo1541
from NetSrvInfo1542 import NetSrvInfo1542
from NetSrvInfo1543 import NetSrvInfo1543
from NetSrvInfo1544 import NetSrvInfo1544
from NetSrvInfo1545 import NetSrvInfo1545
from NetSrvInfo1546 import NetSrvInfo1546
from NetSrvInfo1547 import NetSrvInfo1547
from NetSrvInfo1548 import NetSrvInfo1548
from NetSrvInfo1549 import NetSrvInfo1549
from NetSrvInfo1550 import NetSrvInfo1550
from NetSrvInfo1552 import NetSrvInfo1552
from NetSrvInfo1553 import NetSrvInfo1553
from NetSrvInfo1554 import NetSrvInfo1554
from NetSrvInfo1555 import NetSrvInfo1555
from NetSrvInfo1556 import NetSrvInfo1556
from NetSrvInfo402 import NetSrvInfo402
from NetSrvInfo403 import NetSrvInfo403
from NetSrvInfo502 import NetSrvInfo502
from NetSrvInfo503 import NetSrvInfo503
from NetSrvInfo599 import NetSrvInfo599
from NetTransportCtr0 import NetTransportCtr0
from NetTransportCtr1 import NetTransportCtr1
from NetTransportCtr2 import NetTransportCtr2
from NetTransportCtr3 import NetTransportCtr3
from NetTransportInfo0 import NetTransportInfo0
from NetTransportInfo1 import NetTransportInfo1
from NetTransportInfo2 import NetTransportInfo2
from NetTransportInfo3 import NetTransportInfo3
from NetTransportInfoCtr import NetTransportInfoCtr
from srvsvc import srvsvc
from Statistics import Statistics
