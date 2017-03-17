# encoding: utf-8
# module _openssl.lib
# from /opt/odoo/_venv/local/lib/python2.7/site-packages/cryptography/hazmat/bindings/_openssl.so
# by generator 1.143
# no doc

# imports
from _cffi_backend import (Cryptography_locking_cb, 
    Cryptography_osrandom_engine_id, Cryptography_osrandom_engine_name, 
    Cryptography_pem_password_cb, Cryptography_rand_bytes, 
    Cryptography_rand_status, ERR_add_error_data, OPENSSL_VERSION_TEXT, 
    SN_X9_62_c2onb191v4, SN_X9_62_c2onb191v5, SN_X9_62_c2onb239v4, 
    SN_X9_62_c2onb239v5, SN_X9_62_c2pnb163v1, SN_X9_62_c2pnb163v2, 
    SN_X9_62_c2pnb163v3, SN_X9_62_c2pnb176v1, SN_X9_62_c2pnb208w1, 
    SN_X9_62_c2pnb272w1, SN_X9_62_c2pnb304w1, SN_X9_62_c2pnb368w1, 
    SN_X9_62_c2tnb191v1, SN_X9_62_c2tnb191v2, SN_X9_62_c2tnb191v3, 
    SN_X9_62_c2tnb239v1, SN_X9_62_c2tnb239v2, SN_X9_62_c2tnb239v3, 
    SN_X9_62_c2tnb359v1, SN_X9_62_c2tnb431r1, SN_X9_62_prime192v1, 
    SN_X9_62_prime192v2, SN_X9_62_prime192v3, SN_X9_62_prime239v1, 
    SN_X9_62_prime239v2, SN_X9_62_prime239v3, SN_X9_62_prime256v1, SN_ipsec3, 
    SN_ipsec4, SN_secp112r1, SN_secp112r2, SN_secp128r1, SN_secp128r2, 
    SN_secp160k1, SN_secp160r1, SN_secp160r2, SN_secp192k1, SN_secp224k1, 
    SN_secp224r1, SN_secp256k1, SN_secp384r1, SN_secp521r1, SN_sect113r1, 
    SN_sect113r2, SN_sect131r1, SN_sect131r2, SN_sect163k1, SN_sect163r1, 
    SN_sect163r2, SN_sect193r1, SN_sect193r2, SN_sect233k1, SN_sect233r1, 
    SN_sect239k1, SN_sect283k1, SN_sect283r1, SN_sect409k1, SN_sect409r1, 
    SN_sect571k1, SN_sect571r1, SN_wap_wsg_idm_ecid_wtls1, 
    SN_wap_wsg_idm_ecid_wtls10, SN_wap_wsg_idm_ecid_wtls11, 
    SN_wap_wsg_idm_ecid_wtls12, SN_wap_wsg_idm_ecid_wtls3, 
    SN_wap_wsg_idm_ecid_wtls4, SN_wap_wsg_idm_ecid_wtls5, 
    SN_wap_wsg_idm_ecid_wtls6, SN_wap_wsg_idm_ecid_wtls7, 
    SN_wap_wsg_idm_ecid_wtls8, SN_wap_wsg_idm_ecid_wtls9)


# Variables with simple values

ASN1_F_ASN1_EX_C2I = 204

ASN1_F_ASN1_FIND_END = 190

ASN1_F_ASN1_GENERATE_V3 = 178

ASN1_F_ASN1_GET_OBJECT = 114

ASN1_F_ASN1_ITEM_I2D_FP = 193

ASN1_F_ASN1_ITEM_PACK = 198
ASN1_F_ASN1_ITEM_SIGN = 195
ASN1_F_ASN1_ITEM_UNPACK = 199
ASN1_F_ASN1_ITEM_VERIFY = 197

ASN1_F_ASN1_MBSTRING_NCOPY = 122

ASN1_F_ASN1_TEMPLATE_EX_D2I = 132

ASN1_F_ASN1_TEMPLATE_NEW = 133

ASN1_F_ASN1_TEMPLATE_NOEXP_D2I = 131

ASN1_F_ASN1_TYPE_GET_INT_OCTETSTRING = 134

ASN1_F_ASN1_TYPE_GET_OCTETSTRING = 135

ASN1_F_ASN1_VERIFY = 137

ASN1_F_B64_READ_ASN1 = 209

ASN1_F_B64_WRITE_ASN1 = 210

ASN1_F_BITSTR_CB = 180

ASN1_F_D2I_ASN1_UINTEGER = 150

ASN1_F_D2I_PRIVATEKEY = 154

ASN1_F_I2D_DSA_PUBKEY = 161

ASN1_F_LONG_C2I = 166

ASN1_F_OID_MODULE_INIT = 174

ASN1_F_PARSE_TAGGING = 182

ASN1_F_PKCS5_PBE_SET = 202

ASN1_F_SMIME_READ_ASN1 = 212

ASN1_F_SMIME_TEXT = 213

ASN1_R_BOOLEAN_IS_WRONG_LENGTH = 106

ASN1_R_BUFFER_TOO_SMALL = 107

ASN1_R_CIPHER_HAS_NO_OBJECT_IDENTIFIER = 108

ASN1_R_DATA_IS_WRONG = 109

ASN1_R_DECODE_ERROR = 110

ASN1_R_DEPTH_EXCEEDED = 174

ASN1_R_ENCODE_ERROR = 112

ASN1_R_ERROR_GETTING_TIME = 173

ASN1_R_ERROR_LOADING_SECTION = 172

ASN1_R_HEADER_TOO_LONG = 123

ASN1_R_MSTRING_WRONG_TAG = 140

ASN1_R_NESTED_ASN1_STRING = 197

ASN1_R_NO_CONTENT_TYPE = 209

ASN1_R_NO_MATCHING_CHOICE_TYPE = 143

ASN1_R_NO_MULTIPART_BODY_FAILURE = 210

ASN1_R_NO_MULTIPART_BOUNDARY = 211

ASN1_R_UNKNOWN_MESSAGE_DIGEST_ALGORITHM = 161

ASN1_R_UNKNOWN_OBJECT_TYPE = 162

ASN1_R_UNKNOWN_PUBLIC_KEY_TYPE = 163

ASN1_R_UNKNOWN_TAG = 194

ASN1_R_UNSUPPORTED_ANY_DEFINED_BY_TYPE = 164

ASN1_R_UNSUPPORTED_PUBLIC_KEY_TYPE = 167

ASN1_R_UNSUPPORTED_TYPE = 196

ASN1_R_WRONG_TAG = 168

BIO_CLOSE = 1

BIO_CTRL_DUP = 12
BIO_CTRL_EOF = 2
BIO_CTRL_FLUSH = 11
BIO_CTRL_GET = 5

BIO_CTRL_GET_CLOSE = 8

BIO_CTRL_INFO = 3
BIO_CTRL_PENDING = 10
BIO_CTRL_RESET = 1
BIO_CTRL_SET = 4

BIO_CTRL_SET_CLOSE = 9

BIO_CTRL_WPENDING = 13

BIO_C_FILE_SEEK = 128
BIO_C_FILE_TELL = 133

BIO_FLAGS_IO_SPECIAL = 4

BIO_FLAGS_READ = 1
BIO_FLAGS_RWS = 7

BIO_FLAGS_SHOULD_RETRY = 8

BIO_FLAGS_WRITE = 2

BIO_NOCLOSE = 0

BIO_TYPE_ACCEPT = 1293
BIO_TYPE_BASE64 = 523
BIO_TYPE_BIO = 1043
BIO_TYPE_BUFFER = 521
BIO_TYPE_CIPHER = 522
BIO_TYPE_CONNECT = 1292
BIO_TYPE_DESCRIPTOR = 256
BIO_TYPE_FD = 1284
BIO_TYPE_FILE = 1026
BIO_TYPE_FILTER = 512
BIO_TYPE_MD = 520
BIO_TYPE_MEM = 1025

BIO_TYPE_NBIO_TEST = 528

BIO_TYPE_NONE = 0
BIO_TYPE_NULL = 1030

BIO_TYPE_NULL_FILTER = 529

BIO_TYPE_SOCKET = 1285

BIO_TYPE_SOURCE_SINK = 1024

BIO_TYPE_SSL = 519

CMS_BINARY = 128
CMS_CRLFEOL = 2048

CMS_DEBUG_DECRYPT = 131072

CMS_DETACHED = 64
CMS_NOATTR = 256
CMS_NOCERTS = 2
CMS_NOCRL = 8192
CMS_NOINTERN = 16
CMS_NOOLDMIMETYPE = 1024
CMS_NOSIGS = 12
CMS_NOSMIMECAP = 512
CMS_NOVERIFY = 32

CMS_NO_ATTR_VERIFY = 8

CMS_NO_CONTENT_VERIFY = 4

CMS_NO_SIGNER_CERT_VERIFY = 32

CMS_PARTIAL = 16384

CMS_REUSE_DIGEST = 32768

CMS_STREAM = 4096
CMS_TEXT = 1

CMS_USE_KEYID = 65536

Cryptography_HAS_102_VERIFICATION_ERROR_CODES = 1

Cryptography_HAS_102_VERIFICATION_PARAMS = 1

Cryptography_HAS_AES_CTR128_ENCRYPT = 1

Cryptography_HAS_AES_WRAP = 1

Cryptography_HAS_ALPN = 1
Cryptography_HAS_CMAC = 1
Cryptography_HAS_CMS = 1

Cryptography_HAS_CMS_BIO_FUNCTIONS = 1

Cryptography_HAS_COMPRESSION = 1
Cryptography_HAS_EC = 1
Cryptography_HAS_EC2M = 1
Cryptography_HAS_ECDH = 1
Cryptography_HAS_ECDSA = 1

Cryptography_HAS_EC_1_0_1 = 1
Cryptography_HAS_EC_1_0_2 = 1

Cryptography_HAS_EC_CODES = 1

Cryptography_HAS_EGD = 1

Cryptography_HAS_ENGINE_CRYPTODEV = 1

Cryptography_HAS_GCM = 1

Cryptography_HAS_GET_SERVER_TMP_KEY = 1

Cryptography_HAS_LOCKING_CALLBACKS = 1

Cryptography_HAS_MGF1_MD = 1

Cryptography_HAS_NETBSD_D1_METH = 1

Cryptography_HAS_NEXTPROTONEG = 1

Cryptography_HAS_NPN_NEGOTIATED = 1

Cryptography_HAS_OP_NO_COMPRESSION = 1

Cryptography_HAS_PBKDF2_HMAC = 1

Cryptography_HAS_PKEY_CTX = 1

Cryptography_HAS_PSS_PADDING = 1

Cryptography_HAS_RELEASE_BUFFERS = 1

Cryptography_HAS_RSA_OAEP_MD = 1

Cryptography_HAS_RSA_R_PKCS_DECODING_ERROR = 1

Cryptography_HAS_SCRYPT = 0

Cryptography_HAS_SECURE_RENEGOTIATION = 1

Cryptography_HAS_SET_CERT_CB = 1

Cryptography_HAS_SET_ECDH_AUTO = 1

Cryptography_HAS_SSL2 = 0

Cryptography_HAS_SSL3_METHOD = 1

Cryptography_HAS_SSL_CTX_CLEAR_OPTIONS = 1

Cryptography_HAS_SSL_CTX_SET_CLIENT_CERT_ENGINE = 1

Cryptography_HAS_SSL_OP_MSIE_SSLV2_RSA_PADDING = 1

Cryptography_HAS_SSL_OP_NO_TICKET = 1

Cryptography_HAS_SSL_SET_SSL_CTX = 1

Cryptography_HAS_SSL_ST = 1

Cryptography_HAS_STATUS_REQ_OCSP_RESP = 1

Cryptography_HAS_TLSEXT_HOSTNAME = 1

Cryptography_HAS_TLSEXT_STATUS_REQ_CB = 1
Cryptography_HAS_TLSEXT_STATUS_REQ_TYPE = 1

Cryptography_HAS_TLSv1_1 = 1
Cryptography_HAS_TLSv1_2 = 1

Cryptography_HAS_TLS_ST = 0

Cryptography_HAS_X509_V_FLAG_PARTIAL_CHAIN = 1

Cryptography_HAS_X509_V_FLAG_TRUSTED_FIRST = 1

CRYPTOGRAPHY_IS_LIBRESSL = 0

CRYPTOGRAPHY_OPENSSL_101_OR_GREATER = 1

CRYPTOGRAPHY_OPENSSL_110_OR_GREATER = 0

CRYPTOGRAPHY_OPENSSL_LESS_THAN_101 = 0
CRYPTOGRAPHY_OPENSSL_LESS_THAN_102I = 1

Cryptography_STATIC_CALLBACKS = 1

CRYPTO_LOCK = 1

CRYPTO_LOCK_SSL = 16

CRYPTO_MEM_CHECK_DISABLE = 3
CRYPTO_MEM_CHECK_ENABLE = 2
CRYPTO_MEM_CHECK_OFF = 0
CRYPTO_MEM_CHECK_ON = 1

CRYPTO_READ = 4
CRYPTO_UNLOCK = 2

DH_F_COMPUTE_KEY = 102

DH_R_INVALID_PUBKEY = 102

EC_F_EC_GROUP_NEW_BY_CURVE_NAME = 174

EC_R_UNKNOWN_GROUP = 129

ENGINE_METHOD_ALL = 65535
ENGINE_METHOD_CIPHERS = 64
ENGINE_METHOD_DIGESTS = 128
ENGINE_METHOD_DSA = 2
ENGINE_METHOD_NONE = 0
ENGINE_METHOD_RAND = 8
ENGINE_METHOD_RSA = 1

ENGINE_R_CONFLICTING_ENGINE_ID = 103

ERR_LIB_ASN1 = 13
ERR_LIB_DH = 5
ERR_LIB_EC = 16
ERR_LIB_EVP = 6
ERR_LIB_PEM = 9
ERR_LIB_PKCS12 = 35
ERR_LIB_RSA = 4
ERR_LIB_SSL = 20
ERR_LIB_X509 = 11

EVP_CTRL_GCM_GET_TAG = 16

EVP_CTRL_GCM_SET_IVLEN = 9
EVP_CTRL_GCM_SET_TAG = 17

EVP_F_AES_INIT_KEY = 133

EVP_F_CAMELLIA_INIT_KEY = 159

EVP_F_EVP_CIPHERINIT_EX = 123

EVP_F_EVP_CIPHER_CTX_CTRL = 124

EVP_F_EVP_CIPHER_CTX_SET_KEY_LENGTH = 122

EVP_F_EVP_DECRYPTFINAL_EX = 101

EVP_F_EVP_DIGESTINIT_EX = 128

EVP_F_EVP_ENCRYPTFINAL_EX = 127

EVP_F_EVP_MD_CTX_COPY_EX = 110

EVP_F_EVP_OPENINIT = 102

EVP_F_EVP_PBE_ALG_ADD = 115

EVP_F_EVP_PBE_CIPHERINIT = 116

EVP_F_EVP_PKCS82PKEY = 111

EVP_F_EVP_PKEY_COPY_PARAMETERS = 103

EVP_F_EVP_PKEY_DECRYPT = 104
EVP_F_EVP_PKEY_ENCRYPT = 105
EVP_F_EVP_PKEY_NEW = 106

EVP_F_EVP_SIGNFINAL = 107
EVP_F_EVP_VERIFYFINAL = 108

EVP_F_PKCS5_PBE_KEYIVGEN = 117

EVP_F_PKCS5_V2_PBE_KEYIVGEN = 118

EVP_F_RC2_MAGIC_TO_METH = 109

EVP_F_RC5_CTRL = 125

EVP_MAX_MD_SIZE = 64

EVP_PKEY_DH = 28
EVP_PKEY_DSA = 116
EVP_PKEY_EC = 408
EVP_PKEY_RSA = 6

EVP_R_AES_KEY_SETUP_FAILED = 143

EVP_R_BAD_DECRYPT = 100

EVP_R_CAMELLIA_KEY_SETUP_FAILED = 157

EVP_R_CIPHER_PARAMETER_ERROR = 122

EVP_R_CTRL_NOT_IMPLEMENTED = 132

EVP_R_CTRL_OPERATION_NOT_IMPLEMENTED = 133

EVP_R_DATA_NOT_MULTIPLE_OF_BLOCK_LENGTH = 138

EVP_R_DECODE_ERROR = 114

EVP_R_DIFFERENT_KEY_TYPES = 101

EVP_R_INITIALIZATION_ERROR = 134

EVP_R_INPUT_NOT_INITIALIZED = 111

EVP_R_INVALID_KEY_LENGTH = 130

EVP_R_KEYGEN_FAILURE = 120

EVP_R_MISSING_PARAMETERS = 103

EVP_R_NO_CIPHER_SET = 131

EVP_R_NO_DIGEST_SET = 139

EVP_R_PUBLIC_KEY_NOT_RSA = 106

EVP_R_UNKNOWN_PBE_ALGORITHM = 121

EVP_R_UNSUPPORTED_CIPHER = 107
EVP_R_UNSUPPORTED_KEYLENGTH = 123

EVP_R_UNSUPPORTED_KEY_DERIVATION_FUNCTION = 124

EVP_R_UNSUPPORTED_PRIVATE_KEY_ALGORITHM = 118

EVP_R_UNSUPPORTED_SALT_TYPE = 126

EVP_R_WRONG_FINAL_BLOCK_LENGTH = 109

GEN_DIRNAME = 4
GEN_DNS = 2
GEN_EDIPARTY = 5
GEN_EMAIL = 1
GEN_IPADD = 7
GEN_OTHERNAME = 0
GEN_RID = 8
GEN_URI = 6
GEN_X400 = 3

MBSTRING_ASC = 4097
MBSTRING_BMP = 4098
MBSTRING_FLAG = 4096
MBSTRING_UNIV = 4100
MBSTRING_UTF8 = 4096

NID_ad_ca_issuers = 179

NID_ad_OCSP = 178

NID_any_policy = 746

NID_authority_key_identifier = 90

NID_basic_constraints = 87

NID_certificate_issuer = 771
NID_certificate_policies = 89

NID_commonName = 13
NID_countryName = 14

NID_crl_distribution_points = 103

NID_crl_number = 88
NID_crl_reason = 141

NID_delta_crl = 140

NID_dnQualifier = 174
NID_domainComponent = 391
NID_dsa = 116
NID_dsaWithSHA = 66
NID_dsaWithSHA1 = 113

NID_ecdsa_with_SHA1 = 416
NID_ecdsa_with_SHA224 = 793
NID_ecdsa_with_SHA256 = 794
NID_ecdsa_with_SHA384 = 795
NID_ecdsa_with_SHA512 = 796

NID_ext_key_usage = 126

NID_generationQualifier = 509
NID_givenName = 99

NID_info_access = 177

NID_inhibit_any_policy = 748

NID_invalidity_date = 142

NID_ipsec3 = 749
NID_ipsec4 = 750

NID_issuer_alt_name = 86

NID_issuing_distribution_point = 770

NID_key_usage = 83

NID_localityName = 15
NID_md2 = 3
NID_md4 = 257
NID_md5 = 4
NID_mdc2 = 95

NID_name_constraints = 666

NID_no_rev_avail = 403

NID_organizationalUnitName = 18
NID_organizationName = 17

NID_pbe_WithSHA1And3_Key_TripleDES_CBC = 146

NID_pkcs9_emailAddress = 48

NID_policy_constraints = 401
NID_policy_mappings = 747

NID_private_key_usage_period = 84

NID_pseudonym = 510
NID_ripemd160 = 117
NID_secp112r1 = 704
NID_secp112r2 = 705
NID_secp128r1 = 706
NID_secp128r2 = 707
NID_secp160k1 = 708
NID_secp160r1 = 709
NID_secp160r2 = 710
NID_secp192k1 = 711
NID_secp224k1 = 712
NID_secp224r1 = 713
NID_secp256k1 = 714
NID_secp384r1 = 715
NID_secp521r1 = 716
NID_sect113r1 = 717
NID_sect113r2 = 718
NID_sect131r1 = 719
NID_sect131r2 = 720
NID_sect163k1 = 721
NID_sect163r1 = 722
NID_sect163r2 = 723
NID_sect193r1 = 724
NID_sect193r2 = 725
NID_sect233k1 = 726
NID_sect233r1 = 727
NID_sect239k1 = 728
NID_sect283k1 = 729
NID_sect283r1 = 730
NID_sect409k1 = 731
NID_sect409r1 = 732
NID_sect571k1 = 733
NID_sect571r1 = 734
NID_serialNumber = 105
NID_sha = 41
NID_sha1 = 64
NID_sha224 = 675
NID_sha256 = 672
NID_sha384 = 673
NID_sha512 = 674
NID_stateOrProvinceName = 16

NID_subject_alt_name = 85

NID_subject_key_identifier = 82

NID_surname = 100

NID_target_information = 402

NID_title = 106
NID_undef = 0

NID_wap_wsg_idm_ecid_wtls1 = 735
NID_wap_wsg_idm_ecid_wtls10 = 743
NID_wap_wsg_idm_ecid_wtls11 = 744
NID_wap_wsg_idm_ecid_wtls12 = 745
NID_wap_wsg_idm_ecid_wtls3 = 736
NID_wap_wsg_idm_ecid_wtls4 = 737
NID_wap_wsg_idm_ecid_wtls5 = 738
NID_wap_wsg_idm_ecid_wtls6 = 739
NID_wap_wsg_idm_ecid_wtls7 = 740
NID_wap_wsg_idm_ecid_wtls8 = 741
NID_wap_wsg_idm_ecid_wtls9 = 742

NID_X9_62_c2onb191v4 = 691
NID_X9_62_c2onb191v5 = 692
NID_X9_62_c2onb239v4 = 697
NID_X9_62_c2onb239v5 = 698
NID_X9_62_c2pnb163v1 = 684
NID_X9_62_c2pnb163v2 = 685
NID_X9_62_c2pnb163v3 = 686
NID_X9_62_c2pnb176v1 = 687
NID_X9_62_c2pnb208w1 = 693
NID_X9_62_c2pnb272w1 = 699
NID_X9_62_c2pnb304w1 = 700
NID_X9_62_c2pnb368w1 = 702
NID_X9_62_c2tnb191v1 = 688
NID_X9_62_c2tnb191v2 = 689
NID_X9_62_c2tnb191v3 = 690
NID_X9_62_c2tnb239v1 = 694
NID_X9_62_c2tnb239v2 = 695
NID_X9_62_c2tnb239v3 = 696
NID_X9_62_c2tnb359v1 = 701
NID_X9_62_c2tnb431r1 = 703
NID_X9_62_prime192v1 = 409
NID_X9_62_prime192v2 = 410
NID_X9_62_prime192v3 = 411
NID_X9_62_prime239v1 = 412
NID_X9_62_prime239v2 = 413
NID_X9_62_prime239v3 = 414
NID_X9_62_prime256v1 = 415

OBJ_NAME_TYPE_MD_METH = 1

OPENSSL_BUILT_ON = 3

OPENSSL_CFLAGS = 2
OPENSSL_DIR = 5

OPENSSL_EC_NAMED_CURVE = 1

OPENSSL_NPN_NEGOTIATED = 1

OPENSSL_PLATFORM = 4
OPENSSL_VERSION = 0

OPENSSL_VERSION_NUMBER = 268443775

PEM_F_D2I_PKCS8PRIVATEKEY_BIO = 120
PEM_F_D2I_PKCS8PRIVATEKEY_FP = 121

PEM_F_DO_PK8PKEY = 126

PEM_F_DO_PK8PKEY_FP = 125

PEM_F_LOAD_IV = 101

PEM_F_PEM_ASN1_READ = 102

PEM_F_PEM_ASN1_READ_BIO = 103

PEM_F_PEM_ASN1_WRITE = 104

PEM_F_PEM_ASN1_WRITE_BIO = 105

PEM_F_PEM_DEF_CALLBACK = 100

PEM_F_PEM_DO_HEADER = 106

PEM_F_PEM_GET_EVP_CIPHER_INFO = 107

PEM_F_PEM_READ = 108

PEM_F_PEM_READ_BIO = 109

PEM_F_PEM_READ_BIO_PRIVATEKEY = 123

PEM_F_PEM_READ_PRIVATEKEY = 124

PEM_F_PEM_SIGNFINAL = 112
PEM_F_PEM_WRITE = 113

PEM_F_PEM_WRITE_BIO = 114

PEM_F_PEM_X509_INFO_READ = 115

PEM_F_PEM_X509_INFO_READ_BIO = 116

PEM_F_PEM_X509_INFO_WRITE_BIO = 117

PEM_R_BAD_BASE64_DECODE = 100

PEM_R_BAD_DECRYPT = 101

PEM_R_BAD_END_LINE = 102

PEM_R_BAD_IV_CHARS = 103

PEM_R_BAD_PASSWORD_READ = 104

PEM_R_ERROR_CONVERTING_PRIVATE_KEY = 115

PEM_R_NOT_DEK_INFO = 105

PEM_R_NOT_ENCRYPTED = 106

PEM_R_NOT_PROC_TYPE = 107

PEM_R_NO_START_LINE = 108

PEM_R_PROBLEMS_GETTING_PASSWORD = 109

PEM_R_READ_KEY = 111

PEM_R_SHORT_HEADER = 112

PEM_R_UNSUPPORTED_CIPHER = 113
PEM_R_UNSUPPORTED_ENCRYPTION = 114

PKCS12_F_PKCS12_PBE_CRYPT = 119

PKCS12_R_PKCS12_CIPHERFINAL_ERROR = 116

PKCS7_BINARY = 128
PKCS7_DETACHED = 64
PKCS7_NOATTR = 256
PKCS7_NOCERTS = 2
PKCS7_NOCHAIN = 8
PKCS7_NOINTERN = 16
PKCS7_NOSIGS = 4
PKCS7_NOSMIMECAP = 512
PKCS7_NOVERIFY = 32
PKCS7_STREAM = 4096
PKCS7_TEXT = 1

POINT_CONVERSION_COMPRESSED = 2
POINT_CONVERSION_HYBRID = 6
POINT_CONVERSION_UNCOMPRESSED = 4

RSA_F4 = 65537

RSA_F_RSA_SIGN = 117

RSA_NO_PADDING = 3

RSA_PKCS1_OAEP_PADDING = 4

RSA_PKCS1_PADDING = 1

RSA_PKCS1_PSS_PADDING = 6

RSA_R_BLOCK_TYPE_IS_NOT_01 = 106
RSA_R_BLOCK_TYPE_IS_NOT_02 = 107

RSA_R_DATA_TOO_LARGE_FOR_KEY_SIZE = 110

RSA_R_DATA_TOO_LARGE_FOR_MODULUS = 132

RSA_R_DIGEST_TOO_BIG_FOR_RSA_KEY = 112

RSA_R_OAEP_DECODING_ERROR = 121

RSA_R_PKCS_DECODING_ERROR = 159

RSA_SSLV23_PADDING = 2

RSA_X931_PADDING = 5

SSL3_RANDOM_SIZE = 32

SSLEAY_BUILT_ON = 3

SSLEAY_CFLAGS = 2
SSLEAY_DIR = 5
SSLEAY_PLATFORM = 4
SSLEAY_VERSION = 0

SSL_AD_ACCESS_DENIED = 49

SSL_AD_BAD_CERTIFICATE = 42

SSL_AD_BAD_CERTIFICATE_HASH_VALUE = 114

SSL_AD_BAD_CERTIFICATE_STATUS_RESPONSE = 113

SSL_AD_BAD_RECORD_MAC = 20

SSL_AD_CERTIFICATE_EXPIRED = 45
SSL_AD_CERTIFICATE_REVOKED = 44
SSL_AD_CERTIFICATE_UNKNOWN = 46
SSL_AD_CERTIFICATE_UNOBTAINABLE = 111

SSL_AD_CLOSE_NOTIFY = 0

SSL_AD_DECODE_ERROR = 50

SSL_AD_DECOMPRESSION_FAILURE = 30

SSL_AD_DECRYPT_ERROR = 51

SSL_AD_HANDSHAKE_FAILURE = 40

SSL_AD_ILLEGAL_PARAMETER = 47

SSL_AD_INSUFFICIENT_SECURITY = 71

SSL_AD_INTERNAL_ERROR = 80

SSL_AD_NO_RENEGOTIATION = 100

SSL_AD_PROTOCOL_VERSION = 70

SSL_AD_RECORD_OVERFLOW = 22

SSL_AD_UNEXPECTED_MESSAGE = 10

SSL_AD_UNKNOWN_CA = 48

SSL_AD_UNKNOWN_PSK_IDENTITY = 115

SSL_AD_UNRECOGNIZED_NAME = 112

SSL_AD_UNSUPPORTED_CERTIFICATE = 43
SSL_AD_UNSUPPORTED_EXTENSION = 110

SSL_AD_USER_CANCELLED = 90

SSL_CB_ACCEPT_EXIT = 8194
SSL_CB_ACCEPT_LOOP = 8193

SSL_CB_ALERT = 16384

SSL_CB_CONNECT_EXIT = 4098
SSL_CB_CONNECT_LOOP = 4097

SSL_CB_EXIT = 2

SSL_CB_HANDSHAKE_DONE = 32
SSL_CB_HANDSHAKE_START = 16

SSL_CB_LOOP = 1
SSL_CB_READ = 4

SSL_CB_READ_ALERT = 16388

SSL_CB_WRITE = 8

SSL_CB_WRITE_ALERT = 16392

SSL_ERROR_NONE = 0
SSL_ERROR_SSL = 1
SSL_ERROR_SYSCALL = 5

SSL_ERROR_WANT_CONNECT = 7
SSL_ERROR_WANT_READ = 2
SSL_ERROR_WANT_WRITE = 3

SSL_ERROR_WANT_X509_LOOKUP = 4

SSL_ERROR_ZERO_RETURN = 6

SSL_FILETYPE_ASN1 = 2
SSL_FILETYPE_PEM = 1

SSL_MODE_ACCEPT_MOVING_WRITE_BUFFER = 2

SSL_MODE_AUTO_RETRY = 4

SSL_MODE_ENABLE_PARTIAL_WRITE = 1

SSL_MODE_RELEASE_BUFFERS = 16

SSL_OP_ALL = 2147486719

SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION = 262144

SSL_OP_CIPHER_SERVER_PREFERENCE = 4194304

SSL_OP_COOKIE_EXCHANGE = 8192

SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS = 2048

SSL_OP_EPHEMERAL_RSA = 0

SSL_OP_LEGACY_SERVER_CONNECT = 4

SSL_OP_MICROSOFT_BIG_SSLV3_BUFFER = 32

SSL_OP_MICROSOFT_SESS_ID_BUG = 1

SSL_OP_MSIE_SSLV2_RSA_PADDING = 0

SSL_OP_NETSCAPE_CA_DN_BUG = 536870912

SSL_OP_NETSCAPE_CHALLENGE_BUG = 2

SSL_OP_NETSCAPE_DEMO_CIPHER_CHANGE_BUG = 1073741824

SSL_OP_NETSCAPE_REUSE_CIPHER_CHANGE_BUG = 8

SSL_OP_NO_COMPRESSION = 131072

SSL_OP_NO_QUERY_MTU = 4096

SSL_OP_NO_SSLv2 = 16777216
SSL_OP_NO_SSLv3 = 33554432
SSL_OP_NO_TICKET = 16384
SSL_OP_NO_TLSv1 = 67108864

SSL_OP_NO_TLSv1_1 = 268435456
SSL_OP_NO_TLSv1_2 = 134217728

SSL_OP_PKCS1_CHECK_1 = 0
SSL_OP_PKCS1_CHECK_2 = 0

SSL_OP_SINGLE_DH_USE = 1048576

SSL_OP_SINGLE_ECDH_USE = 524288

SSL_OP_SSLEAY_080_CLIENT_DH_BUG = 128

SSL_OP_SSLREF2_REUSE_CERT_TYPE_BUG = 0

SSL_OP_TLS_BLOCK_PADDING_BUG = 512

SSL_OP_TLS_D5_BUG = 256

SSL_OP_TLS_ROLLBACK_BUG = 8388608

SSL_RECEIVED_SHUTDOWN = 2

SSL_SENT_SHUTDOWN = 1

SSL_SESS_CACHE_BOTH = 3
SSL_SESS_CACHE_CLIENT = 1

SSL_SESS_CACHE_NO_AUTO_CLEAR = 128

SSL_SESS_CACHE_NO_INTERNAL = 768

SSL_SESS_CACHE_NO_INTERNAL_LOOKUP = 256
SSL_SESS_CACHE_NO_INTERNAL_STORE = 512

SSL_SESS_CACHE_OFF = 0
SSL_SESS_CACHE_SERVER = 2

SSL_ST_ACCEPT = 8192
SSL_ST_BEFORE = 16384
SSL_ST_CONNECT = 4096
SSL_ST_INIT = 12288
SSL_ST_MASK = 4095
SSL_ST_OK = 3
SSL_ST_RENEGOTIATE = 12292

SSL_TLSEXT_ERR_ALERT_FATAL = 2
SSL_TLSEXT_ERR_ALERT_WARNING = 1

SSL_TLSEXT_ERR_NOACK = 3
SSL_TLSEXT_ERR_OK = 0

SSL_VERIFY_CLIENT_ONCE = 4

SSL_VERIFY_FAIL_IF_NO_PEER_CERT = 2

SSL_VERIFY_NONE = 0
SSL_VERIFY_PEER = 1

TLSEXT_NAMETYPE_host_name = 0

TLSEXT_STATUSTYPE_ocsp = 1

TLS_ST_BEFORE = 0
TLS_ST_OK = 0

V_ASN1_GENERALIZEDTIME = 24

X509_FLAG_COMPAT = 0

X509_FLAG_NO_ATTRIBUTES = 2048
X509_FLAG_NO_AUX = 1024
X509_FLAG_NO_EXTENSIONS = 256
X509_FLAG_NO_HEADER = 1
X509_FLAG_NO_ISSUER = 16
X509_FLAG_NO_PUBKEY = 128
X509_FLAG_NO_SERIAL = 4
X509_FLAG_NO_SIGDUMP = 512
X509_FLAG_NO_SIGNAME = 8
X509_FLAG_NO_SUBJECT = 64
X509_FLAG_NO_VALIDITY = 32
X509_FLAG_NO_VERSION = 2

X509_LU_CRL = 2
X509_LU_X509 = 1

X509_R_CERT_ALREADY_IN_HASH_TABLE = 101

X509_V_ERR_AKID_ISSUER_SERIAL_MISMATCH = 31

X509_V_ERR_AKID_SKID_MISMATCH = 30

X509_V_ERR_APPLICATION_VERIFICATION = 50

X509_V_ERR_CERT_CHAIN_TOO_LONG = 22

X509_V_ERR_CERT_HAS_EXPIRED = 10

X509_V_ERR_CERT_NOT_YET_VALID = 9

X509_V_ERR_CERT_REJECTED = 28
X509_V_ERR_CERT_REVOKED = 23

X509_V_ERR_CERT_SIGNATURE_FAILURE = 7

X509_V_ERR_CERT_UNTRUSTED = 27

X509_V_ERR_CRL_HAS_EXPIRED = 12

X509_V_ERR_CRL_NOT_YET_VALID = 11

X509_V_ERR_CRL_PATH_VALIDATION_ERROR = 54

X509_V_ERR_CRL_SIGNATURE_FAILURE = 8

X509_V_ERR_DEPTH_ZERO_SELF_SIGNED_CERT = 18

X509_V_ERR_DIFFERENT_CRL_SCOPE = 44

X509_V_ERR_EMAIL_MISMATCH = 63

X509_V_ERR_ERROR_IN_CERT_NOT_AFTER_FIELD = 14

X509_V_ERR_ERROR_IN_CERT_NOT_BEFORE_FIELD = 13

X509_V_ERR_ERROR_IN_CRL_LAST_UPDATE_FIELD = 15

X509_V_ERR_ERROR_IN_CRL_NEXT_UPDATE_FIELD = 16

X509_V_ERR_EXCLUDED_VIOLATION = 48

X509_V_ERR_HOSTNAME_MISMATCH = 62

X509_V_ERR_INVALID_CA = 24
X509_V_ERR_INVALID_EXTENSION = 41

X509_V_ERR_INVALID_NON_CA = 37

X509_V_ERR_INVALID_POLICY_EXTENSION = 42

X509_V_ERR_INVALID_PURPOSE = 26

X509_V_ERR_IP_ADDRESS_MISMATCH = 64

X509_V_ERR_KEYUSAGE_NO_CERTSIGN = 32

X509_V_ERR_KEYUSAGE_NO_CRL_SIGN = 35

X509_V_ERR_KEYUSAGE_NO_DIGITAL_SIGNATURE = 39

X509_V_ERR_NO_EXPLICIT_POLICY = 43

X509_V_ERR_OUT_OF_MEM = 17

X509_V_ERR_PATH_LENGTH_EXCEEDED = 25

X509_V_ERR_PERMITTED_VIOLATION = 47

X509_V_ERR_PROXY_CERTIFICATES_NOT_ALLOWED = 40

X509_V_ERR_PROXY_PATH_LENGTH_EXCEEDED = 38

X509_V_ERR_SELF_SIGNED_CERT_IN_CHAIN = 19

X509_V_ERR_SUBJECT_ISSUER_MISMATCH = 29

X509_V_ERR_SUBTREE_MINMAX = 49

X509_V_ERR_SUITE_B_CANNOT_SIGN_P_384_WITH_P_256 = 61

X509_V_ERR_SUITE_B_INVALID_ALGORITHM = 57
X509_V_ERR_SUITE_B_INVALID_CURVE = 58

X509_V_ERR_SUITE_B_INVALID_SIGNATURE_ALGORITHM = 59

X509_V_ERR_SUITE_B_INVALID_VERSION = 56

X509_V_ERR_SUITE_B_LOS_NOT_ALLOWED = 60

X509_V_ERR_UNABLE_TO_DECODE_ISSUER_PUBLIC_KEY = 6

X509_V_ERR_UNABLE_TO_DECRYPT_CERT_SIGNATURE = 4

X509_V_ERR_UNABLE_TO_DECRYPT_CRL_SIGNATURE = 5

X509_V_ERR_UNABLE_TO_GET_CRL = 3

X509_V_ERR_UNABLE_TO_GET_CRL_ISSUER = 33

X509_V_ERR_UNABLE_TO_GET_ISSUER_CERT = 2

X509_V_ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY = 20

X509_V_ERR_UNABLE_TO_VERIFY_LEAF_SIGNATURE = 21

X509_V_ERR_UNHANDLED_CRITICAL_CRL_EXTENSION = 36

X509_V_ERR_UNHANDLED_CRITICAL_EXTENSION = 34

X509_V_ERR_UNNESTED_RESOURCE = 46

X509_V_ERR_UNSUPPORTED_CONSTRAINT_SYNTAX = 52
X509_V_ERR_UNSUPPORTED_CONSTRAINT_TYPE = 51

X509_V_ERR_UNSUPPORTED_EXTENSION_FEATURE = 45

X509_V_ERR_UNSUPPORTED_NAME_SYNTAX = 53

X509_V_FLAG_ALLOW_PROXY_CERTS = 64

X509_V_FLAG_CB_ISSUER_CHECK = 1

X509_V_FLAG_CHECK_SS_SIGNATURE = 16384

X509_V_FLAG_CRL_CHECK = 4

X509_V_FLAG_CRL_CHECK_ALL = 8

X509_V_FLAG_EXPLICIT_POLICY = 256

X509_V_FLAG_EXTENDED_CRL_SUPPORT = 4096

X509_V_FLAG_IGNORE_CRITICAL = 16

X509_V_FLAG_INHIBIT_ANY = 512
X509_V_FLAG_INHIBIT_MAP = 1024

X509_V_FLAG_NOTIFY_POLICY = 2048

X509_V_FLAG_PARTIAL_CHAIN = 524288

X509_V_FLAG_POLICY_CHECK = 128

X509_V_FLAG_SUITEB_128_LOS = 196608

X509_V_FLAG_SUITEB_128_LOS_ONLY = 65536

X509_V_FLAG_SUITEB_192_LOS = 131072

X509_V_FLAG_TRUSTED_FIRST = 32768

X509_V_FLAG_USE_CHECK_TIME = 2

X509_V_FLAG_USE_DELTAS = 8192

X509_V_FLAG_X509_STRICT = 32

X509_V_OK = 0

XN_FLAG_COMPAT = 0

XN_FLAG_DN_REV = 1048576

XN_FLAG_DUMP_UNKNOWN_FIELDS = 16777216

XN_FLAG_FN_ALIGN = 33554432
XN_FLAG_FN_LN = 2097152
XN_FLAG_FN_MASK = 6291456
XN_FLAG_FN_NONE = 6291456
XN_FLAG_FN_OID = 4194304
XN_FLAG_FN_SN = 0

XN_FLAG_MULTILINE = 44302342
XN_FLAG_ONELINE = 8520479
XN_FLAG_RFC2253 = 17892119

XN_FLAG_SEP_COMMA_PLUS = 65536

XN_FLAG_SEP_CPLUS_SPC = 131072

XN_FLAG_SEP_MASK = 983040
XN_FLAG_SEP_MULTILINE = 262144

XN_FLAG_SEP_SPLUS_SPC = 196608

XN_FLAG_SPC_EQ = 8388608

# functions

def ACCESS_DESCRIPTION_free(ACCESS_DESCRIPTION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ACCESS_DESCRIPTION_free(ACCESS_DESCRIPTION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ACCESS_DESCRIPTION_new(): # real signature unknown; restored from __doc__
    """
    ACCESS_DESCRIPTION *ACCESS_DESCRIPTION_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def AES_ctr128_encrypt(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void AES_ctr128_encrypt(unsigned char *, unsigned char *, size_t, struct aes_key_st *, unsigned char *, unsigned char *, unsigned int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def AES_set_decrypt_key(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int AES_set_decrypt_key(unsigned char *, int, struct aes_key_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def AES_set_encrypt_key(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int AES_set_encrypt_key(unsigned char *, int, struct aes_key_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def AES_unwrap_key(struct_aes_key_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int AES_unwrap_key(struct aes_key_st *, unsigned char *, unsigned char *, unsigned char *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def AES_wrap_key(struct_aes_key_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int AES_wrap_key(struct aes_key_st *, unsigned char *, unsigned char *, unsigned char *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_BIT_STRING_free(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ASN1_BIT_STRING_free(struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_BIT_STRING_get_bit(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_BIT_STRING_get_bit(struct asn1_string_st *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_BIT_STRING_new(): # real signature unknown; restored from __doc__
    """
    struct asn1_string_st *ASN1_BIT_STRING_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_BIT_STRING_set_bit(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_BIT_STRING_set_bit(struct asn1_string_st *, int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_ENUMERATED_free(ASN1_ENUMERATED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ASN1_ENUMERATED_free(ASN1_ENUMERATED *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_ENUMERATED_get(ASN1_ENUMERATED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long ASN1_ENUMERATED_get(ASN1_ENUMERATED *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_ENUMERATED_new(): # real signature unknown; restored from __doc__
    """
    ASN1_ENUMERATED *ASN1_ENUMERATED_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_ENUMERATED_set(ASN1_ENUMERATED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_ENUMERATED_set(ASN1_ENUMERATED *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_GENERALIZEDTIME_check(ASN1_GENERALIZEDTIME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_GENERALIZEDTIME_check(ASN1_GENERALIZEDTIME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_GENERALIZEDTIME_free(ASN1_GENERALIZEDTIME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ASN1_GENERALIZEDTIME_free(ASN1_GENERALIZEDTIME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_GENERALIZEDTIME_set(ASN1_GENERALIZEDTIME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_GENERALIZEDTIME *ASN1_GENERALIZEDTIME_set(ASN1_GENERALIZEDTIME *, int64_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_GENERALIZEDTIME_set_string(ASN1_GENERALIZEDTIME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_GENERALIZEDTIME_set_string(ASN1_GENERALIZEDTIME *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_IA5STRING_new(): # real signature unknown; restored from __doc__
    """
    struct asn1_string_st *ASN1_IA5STRING_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_INTEGER_cmp(ASN1_INTEGER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_INTEGER_cmp(ASN1_INTEGER *, ASN1_INTEGER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_INTEGER_dup(ASN1_INTEGER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_INTEGER *ASN1_INTEGER_dup(ASN1_INTEGER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_INTEGER_free(ASN1_INTEGER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ASN1_INTEGER_free(ASN1_INTEGER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_INTEGER_get(ASN1_INTEGER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long ASN1_INTEGER_get(ASN1_INTEGER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_INTEGER_new(): # real signature unknown; restored from __doc__
    """
    ASN1_INTEGER *ASN1_INTEGER_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_INTEGER_set(ASN1_INTEGER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_INTEGER_set(ASN1_INTEGER *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_INTEGER_to_BN(ASN1_INTEGER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    BIGNUM *ASN1_INTEGER_to_BN(ASN1_INTEGER *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_item_d2i(ASN1_VALUE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_VALUE *ASN1_item_d2i(ASN1_VALUE * *, unsigned char * *, long, ASN1_ITEM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_ITEM_ptr(ASN1_ITEM_EXP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_ITEM *ASN1_ITEM_ptr(ASN1_ITEM_EXP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_OBJECT_free(ASN1_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ASN1_OBJECT_free(ASN1_OBJECT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_OBJECT_new(): # real signature unknown; restored from __doc__
    """
    ASN1_OBJECT *ASN1_OBJECT_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_OCTET_STRING_cmp(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_OCTET_STRING_cmp(struct asn1_string_st *, struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_OCTET_STRING_dup(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct asn1_string_st *ASN1_OCTET_STRING_dup(struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_OCTET_STRING_free(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ASN1_OCTET_STRING_free(struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_OCTET_STRING_new(): # real signature unknown; restored from __doc__
    """
    struct asn1_string_st *ASN1_OCTET_STRING_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_OCTET_STRING_set(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_OCTET_STRING_set(struct asn1_string_st *, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_STRING_cmp(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_STRING_cmp(struct asn1_string_st *, struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_STRING_data(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned char *ASN1_STRING_data(struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_STRING_dup(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct asn1_string_st *ASN1_STRING_dup(struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_STRING_free(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ASN1_STRING_free(struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_STRING_length(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_STRING_length(struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_STRING_new(): # real signature unknown; restored from __doc__
    """
    struct asn1_string_st *ASN1_STRING_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_STRING_set(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_STRING_set(struct asn1_string_st *, void *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_STRING_set_default_mask_asc(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_STRING_set_default_mask_asc(char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_STRING_to_UTF8(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_STRING_to_UTF8(unsigned char * *, struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_STRING_type(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_STRING_type(struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_STRING_type_new(p_int): # real signature unknown; restored from __doc__
    """
    struct asn1_string_st *ASN1_STRING_type_new(int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_TIME_free(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ASN1_TIME_free(struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_TIME_new(): # real signature unknown; restored from __doc__
    """
    struct asn1_string_st *ASN1_TIME_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_TIME_print(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_TIME_print(struct bio_st *, struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_TIME_set(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct asn1_string_st *ASN1_TIME_set(struct asn1_string_st *, int64_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_TIME_to_generalizedtime(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_GENERALIZEDTIME *ASN1_TIME_to_generalizedtime(struct asn1_string_st *, ASN1_GENERALIZEDTIME * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_UTCTIME_check(ASN1_UTCTIME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_UTCTIME_check(ASN1_UTCTIME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_UTCTIME_cmp_time_t(ASN1_UTCTIME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_UTCTIME_cmp_time_t(ASN1_UTCTIME *, int64_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_UTCTIME_free(ASN1_UTCTIME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ASN1_UTCTIME_free(ASN1_UTCTIME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_UTCTIME_new(): # real signature unknown; restored from __doc__
    """
    ASN1_UTCTIME *ASN1_UTCTIME_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_UTCTIME_print(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ASN1_UTCTIME_print(struct bio_st *, ASN1_UTCTIME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_UTCTIME_set(ASN1_UTCTIME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_UTCTIME *ASN1_UTCTIME_set(ASN1_UTCTIME *, int64_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_UTF8STRING_free(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ASN1_UTF8STRING_free(struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ASN1_UTF8STRING_new(): # real signature unknown; restored from __doc__
    """
    struct asn1_string_st *ASN1_UTF8STRING_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def AUTHORITY_KEYID_free(AUTHORITY_KEYID, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void AUTHORITY_KEYID_free(AUTHORITY_KEYID *);
    
    CFFI C function from _openssl.lib
    """
    pass

def AUTHORITY_KEYID_new(): # real signature unknown; restored from __doc__
    """
    AUTHORITY_KEYID *AUTHORITY_KEYID_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def BASIC_CONSTRAINTS_free(BASIC_CONSTRAINTS, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BASIC_CONSTRAINTS_free(BASIC_CONSTRAINTS *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BASIC_CONSTRAINTS_new(): # real signature unknown; restored from __doc__
    """
    BASIC_CONSTRAINTS *BASIC_CONSTRAINTS_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_append_filename(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_append_filename(struct bio_st *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_callback_ctrl(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_callback_ctrl(struct bio_st *, int, void(*)(struct bio_st *, int, char *, int, long, long));
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_clear_retry_flags(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BIO_clear_retry_flags(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_ctrl(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_ctrl(struct bio_st *, int, long, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_ctrl_pending(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    size_t BIO_ctrl_pending(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_ctrl_wpending(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    size_t BIO_ctrl_wpending(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_eof(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_eof(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_find_type(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct bio_st *BIO_find_type(struct bio_st *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_flush(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_flush(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_free(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_free(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_free_all(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BIO_free_all(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_f_buffer(): # real signature unknown; restored from __doc__
    """
    BIO_METHOD *BIO_f_buffer();
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_f_null(): # real signature unknown; restored from __doc__
    """
    BIO_METHOD *BIO_f_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_gets(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_gets(struct bio_st *, char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_get_buffer_num_lines(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_get_buffer_num_lines(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_get_close(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_get_close(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_get_fd(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_get_fd(struct bio_st *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_get_fp(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_get_fp(struct bio_st *, FILE * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_get_info_callback(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_get_info_callback(struct bio_st *, void(* *)(struct bio_st *, int, char *, int, long, long));
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_get_mem_data(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_get_mem_data(struct bio_st *, char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_get_mem_ptr(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_get_mem_ptr(struct bio_st *, BUF_MEM * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_int_ctrl(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_int_ctrl(struct bio_st *, int, long, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_method_type(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_method_type(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_new(BIO_METHOD, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct bio_st *BIO_new(BIO_METHOD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_new_CMS(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct bio_st *BIO_new_CMS(struct bio_st *, CMS_ContentInfo *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_new_fd(p_int, p_int_1): # real signature unknown; restored from __doc__
    """
    struct bio_st *BIO_new_fd(int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_new_file(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct bio_st *BIO_new_file(char *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_new_fp(FILE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct bio_st *BIO_new_fp(FILE *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_new_mem_buf(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct bio_st *BIO_new_mem_buf(void *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_new_socket(p_int, p_int_1): # real signature unknown; restored from __doc__
    """
    struct bio_st *BIO_new_socket(int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_next(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct bio_st *BIO_next(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_pending(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_pending(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_pop(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct bio_st *BIO_pop(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_push(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct bio_st *BIO_push(struct bio_st *, struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_puts(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_puts(struct bio_st *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_read(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_read(struct bio_st *, void *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_read_filename(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_read_filename(struct bio_st *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_reset(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_reset(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_retry_type(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_retry_type(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_rw_filename(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_rw_filename(struct bio_st *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_seek(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_seek(struct bio_st *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_set_buffer_read_data(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_set_buffer_read_data(struct bio_st *, void *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_set_buffer_size(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_set_buffer_size(struct bio_st *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_set_close(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_set_close(struct bio_st *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_set_fd(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_set_fd(struct bio_st *, long, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_set_fp(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_set_fp(struct bio_st *, FILE *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_set_info_callback(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_set_info_callback(struct bio_st *, void(*)(struct bio_st *, int, char *, int, long, long));
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_set_mem_buf(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_set_mem_buf(struct bio_st *, BUF_MEM *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_set_mem_eof_return(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_set_mem_eof_return(struct bio_st *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_set_nbio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_set_nbio(struct bio_st *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_set_read_buffer_size(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_set_read_buffer_size(struct bio_st *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_set_retry_read(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BIO_set_retry_read(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_set_write_buffer_size(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_set_write_buffer_size(struct bio_st *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_should_io_special(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_should_io_special(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_should_read(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_should_read(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_should_retry(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_should_retry(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_should_write(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_should_write(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_s_fd(): # real signature unknown; restored from __doc__
    """
    BIO_METHOD *BIO_s_fd();
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_s_file(): # real signature unknown; restored from __doc__
    """
    BIO_METHOD *BIO_s_file();
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_s_mem(): # real signature unknown; restored from __doc__
    """
    BIO_METHOD *BIO_s_mem();
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_s_null(): # real signature unknown; restored from __doc__
    """
    BIO_METHOD *BIO_s_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_s_socket(): # real signature unknown; restored from __doc__
    """
    BIO_METHOD *BIO_s_socket();
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_tell(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_tell(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_up_ref(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_up_ref(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_vfree(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BIO_vfree(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_wpending(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_wpending(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_write(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BIO_write(struct bio_st *, void *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BIO_write_filename(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long BIO_write_filename(struct bio_st *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_add(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_add(BIGNUM *, BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_bin2bn(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    BIGNUM *BN_bin2bn(unsigned char *, int, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_bn2bin(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_bn2bin(BIGNUM *, unsigned char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_bn2hex(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *BN_bn2hex(BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_clear_bit(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_clear_bit(BIGNUM *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_cmp(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_cmp(BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_copy(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    BIGNUM *BN_copy(BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_CTX_end(BN_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BN_CTX_end(BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_CTX_free(BN_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BN_CTX_free(BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_CTX_get(BN_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    BIGNUM *BN_CTX_get(BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_CTX_new(): # real signature unknown; restored from __doc__
    """
    BN_CTX *BN_CTX_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_CTX_start(BN_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BN_CTX_start(BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_dec2bn(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_dec2bn(BIGNUM * *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_div(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_div(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_dup(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    BIGNUM *BN_dup(BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_exp(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_exp(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_free(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BN_free(BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_gcd(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_gcd(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_get_word(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    uint64_t BN_get_word(BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_hex2bn(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_hex2bn(BIGNUM * *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_is_bit_set(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_is_bit_set(BIGNUM *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_lshift(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_lshift(BIGNUM *, BIGNUM *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_lshift1(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_lshift1(BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_mask_bits(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_mask_bits(BIGNUM *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_mod(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_mod(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_mod_add(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_mod_add(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_mod_exp(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_mod_exp(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_mod_inverse(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    BIGNUM *BN_mod_inverse(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_mod_mul(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_mod_mul(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_mod_sqr(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_mod_sqr(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_mod_sub(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_mod_sub(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_mul(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_mul(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_new(): # real signature unknown; restored from __doc__
    """
    BIGNUM *BN_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_nnmod(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_nnmod(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_num_bits(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_num_bits(BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_num_bytes(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_num_bytes(BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_one(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_one(BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_rshift(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_rshift(BIGNUM *, BIGNUM *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_rshift1(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_rshift1(BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_set_bit(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_set_bit(BIGNUM *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_set_word(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_set_word(BIGNUM *, uint64_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_sqr(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_sqr(BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_sub(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_sub(BIGNUM *, BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_to_ASN1_INTEGER(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_INTEGER *BN_to_ASN1_INTEGER(BIGNUM *, ASN1_INTEGER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_value_one(): # real signature unknown; restored from __doc__
    """
    BIGNUM *BN_value_one();
    
    CFFI C function from _openssl.lib
    """
    pass

def BN_zero(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int BN_zero(BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def CMAC_CTX_copy(CMAC_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int CMAC_CTX_copy(CMAC_CTX *, CMAC_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def CMAC_CTX_free(CMAC_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void CMAC_CTX_free(CMAC_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def CMAC_CTX_new(): # real signature unknown; restored from __doc__
    """
    CMAC_CTX *CMAC_CTX_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def CMAC_Final(CMAC_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int CMAC_Final(CMAC_CTX *, unsigned char *, size_t *);
    
    CFFI C function from _openssl.lib
    """
    pass

def CMAC_Init(CMAC_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int CMAC_Init(CMAC_CTX *, void *, size_t, EVP_CIPHER *, ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def CMAC_Update(CMAC_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int CMAC_Update(CMAC_CTX *, void *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def CMS_add1_signer(CMS_ContentInfo, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    CMS_SignerInfo *CMS_add1_signer(CMS_ContentInfo *, X509 *, EVP_PKEY *, EVP_MD *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def CMS_decrypt(CMS_ContentInfo, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int CMS_decrypt(CMS_ContentInfo *, EVP_PKEY *, X509 *, struct bio_st *, struct bio_st *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def CMS_encrypt(Cryptography_STACK_OF_X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    CMS_ContentInfo *CMS_encrypt(Cryptography_STACK_OF_X509 *, struct bio_st *, EVP_CIPHER *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def CMS_final(CMS_ContentInfo, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int CMS_final(CMS_ContentInfo *, struct bio_st *, struct bio_st *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def CMS_sign(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    CMS_ContentInfo *CMS_sign(X509 *, EVP_PKEY *, Cryptography_STACK_OF_X509 *, struct bio_st *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def CMS_verify(CMS_ContentInfo, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int CMS_verify(CMS_ContentInfo *, Cryptography_STACK_OF_X509 *, X509_STORE *, struct bio_st *, struct bio_st *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def Cryptography_add_osrandom_engine(): # real signature unknown; restored from __doc__
    """
    int Cryptography_add_osrandom_engine();
    
    CFFI C function from _openssl.lib
    """
    return 0

def Cryptography_EVP_MD_CTX_free(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void Cryptography_EVP_MD_CTX_free(EVP_MD_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def Cryptography_EVP_MD_CTX_new(): # real signature unknown; restored from __doc__
    """
    EVP_MD_CTX *Cryptography_EVP_MD_CTX_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def Cryptography_EVP_PKEY_id(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int Cryptography_EVP_PKEY_id(EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def Cryptography_HMAC_CTX_free(HMAC_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void Cryptography_HMAC_CTX_free(HMAC_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def Cryptography_HMAC_CTX_new(): # real signature unknown; restored from __doc__
    """
    HMAC_CTX *Cryptography_HMAC_CTX_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def Cryptography_X509_NAME_ENTRY_set(X509_NAME_ENTRY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int Cryptography_X509_NAME_ENTRY_set(X509_NAME_ENTRY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def Cryptography_X509_REVOKED_dup(X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_REVOKED *Cryptography_X509_REVOKED_dup(X509_REVOKED *);
    
    CFFI C function from _openssl.lib
    """
    pass

def CRYPTO_cleanup_all_ex_data(): # real signature unknown; restored from __doc__
    """
    void CRYPTO_cleanup_all_ex_data();
    
    CFFI C function from _openssl.lib
    """
    pass

def CRYPTO_get_locking_callback(): # real signature unknown; restored from __doc__
    """
    void(*CRYPTO_get_locking_callback())(int, int, char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def CRYPTO_lock(p_int, p_int_1, char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void CRYPTO_lock(int, int, char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def CRYPTO_mem_ctrl(p_int): # real signature unknown; restored from __doc__
    """
    int CRYPTO_mem_ctrl(int);
    
    CFFI C function from _openssl.lib
    """
    return 0

def CRYPTO_num_locks(): # real signature unknown; restored from __doc__
    """
    int CRYPTO_num_locks();
    
    CFFI C function from _openssl.lib
    """
    return 0

def CRYPTO_set_locking_callback(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void CRYPTO_set_locking_callback(void(*)(int, int, char *, int));
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_ASN1_OBJECT(ASN1_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_OBJECT *d2i_ASN1_OBJECT(ASN1_OBJECT * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_ASN1_TYPE(ASN1_TYPE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_TYPE *d2i_ASN1_TYPE(ASN1_TYPE * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_DHparams(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DH *d2i_DHparams(DH * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_DSAPrivateKey(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DSA *d2i_DSAPrivateKey(DSA * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_DSAPrivateKey_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DSA *d2i_DSAPrivateKey_bio(struct bio_st *, DSA * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_DSAPublicKey(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DSA *d2i_DSAPublicKey(DSA * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_DSA_PUBKEY(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DSA *d2i_DSA_PUBKEY(DSA * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_DSA_PUBKEY_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DSA *d2i_DSA_PUBKEY_bio(struct bio_st *, DSA * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_ECDSA_SIG(ECDSA_SIG, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ECDSA_SIG *d2i_ECDSA_SIG(ECDSA_SIG * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_ECPrivateKey(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_KEY *d2i_ECPrivateKey(EC_KEY * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_ECPrivateKey_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_KEY *d2i_ECPrivateKey_bio(struct bio_st *, EC_KEY * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_EC_PUBKEY(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_KEY *d2i_EC_PUBKEY(EC_KEY * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_EC_PUBKEY_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_KEY *d2i_EC_PUBKEY_bio(struct bio_st *, EC_KEY * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_GENERAL_NAMES(struct_stack_st_GENERAL_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct stack_st_GENERAL_NAME *d2i_GENERAL_NAMES(struct stack_st_GENERAL_NAME * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_OCSP_REQUEST_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    OCSP_REQUEST *d2i_OCSP_REQUEST_bio(struct bio_st *, OCSP_REQUEST * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_OCSP_RESPONSE_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    OCSP_RESPONSE *d2i_OCSP_RESPONSE_bio(struct bio_st *, OCSP_RESPONSE * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_PKCS12_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    PKCS12 *d2i_PKCS12_bio(struct bio_st *, PKCS12 * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_PKCS7_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    PKCS7 *d2i_PKCS7_bio(struct bio_st *, PKCS7 * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_PKCS8PrivateKey_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY *d2i_PKCS8PrivateKey_bio(struct bio_st *, EVP_PKEY * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_PKCS8_PRIV_KEY_INFO_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    PKCS8_PRIV_KEY_INFO *d2i_PKCS8_PRIV_KEY_INFO_bio(struct bio_st *, PKCS8_PRIV_KEY_INFO * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_PrivateKey_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY *d2i_PrivateKey_bio(struct bio_st *, EVP_PKEY * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_PUBKEY_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY *d2i_PUBKEY_bio(struct bio_st *, EVP_PKEY * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_RSAPrivateKey(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    RSA *d2i_RSAPrivateKey(RSA * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_RSAPrivateKey_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    RSA *d2i_RSAPrivateKey_bio(struct bio_st *, RSA * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_RSAPublicKey(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    RSA *d2i_RSAPublicKey(RSA * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_RSAPublicKey_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    RSA *d2i_RSAPublicKey_bio(struct bio_st *, RSA * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_RSA_PUBKEY(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    RSA *d2i_RSA_PUBKEY(RSA * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_RSA_PUBKEY_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    RSA *d2i_RSA_PUBKEY_bio(struct bio_st *, RSA * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_X509_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509 *d2i_X509_bio(struct bio_st *, X509 * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_X509_CRL_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_CRL *d2i_X509_CRL_bio(struct bio_st *, X509_CRL * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def d2i_X509_REQ_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_REQ *d2i_X509_REQ_bio(struct bio_st *, X509_REQ * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DHparams_dup(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DH *DHparams_dup(DH *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DHparams_print(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DHparams_print(struct bio_st *, DH *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DHparams_print_fp(FILE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DHparams_print_fp(FILE *, DH *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_check(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DH_check(DH *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_check_pub_key(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DH_check_pub_key(DH *, BIGNUM *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_compute_key(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DH_compute_key(unsigned char *, BIGNUM *, DH *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_free(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void DH_free(DH *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_generate_key(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DH_generate_key(DH *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_generate_parameters_ex(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DH_generate_parameters_ex(DH *, int, int, BN_GENCB *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_get0_key(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void DH_get0_key(DH *, BIGNUM * *, BIGNUM * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_get0_pqg(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void DH_get0_pqg(DH *, BIGNUM * *, BIGNUM * *, BIGNUM * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_get_ex_data(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void *DH_get_ex_data(DH *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_new(): # real signature unknown; restored from __doc__
    """
    DH *DH_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_set0_key(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DH_set0_key(DH *, BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_set0_pqg(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DH_set0_pqg(DH *, BIGNUM *, BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_set_ex_data(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DH_set_ex_data(DH *, int, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DH_size(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DH_size(DH *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DIST_POINT_free(DIST_POINT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void DIST_POINT_free(DIST_POINT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DIST_POINT_NAME_free(DIST_POINT_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void DIST_POINT_NAME_free(DIST_POINT_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DIST_POINT_NAME_new(): # real signature unknown; restored from __doc__
    """
    DIST_POINT_NAME *DIST_POINT_NAME_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def DIST_POINT_new(): # real signature unknown; restored from __doc__
    """
    DIST_POINT *DIST_POINT_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def DSAparams_dup(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DSA *DSAparams_dup(DSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DSA_free(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void DSA_free(DSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DSA_generate_key(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DSA_generate_key(DSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DSA_generate_parameters_ex(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DSA_generate_parameters_ex(DSA *, int, unsigned char *, int, int *, unsigned long *, BN_GENCB *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DSA_get0_key(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void DSA_get0_key(DSA *, BIGNUM * *, BIGNUM * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DSA_get0_pqg(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void DSA_get0_pqg(DSA *, BIGNUM * *, BIGNUM * *, BIGNUM * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DSA_new(): # real signature unknown; restored from __doc__
    """
    DSA *DSA_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def DSA_set0_key(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DSA_set0_key(DSA *, BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DSA_set0_pqg(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DSA_set0_pqg(DSA *, BIGNUM *, BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DSA_sign(p_int, unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DSA_sign(int, unsigned char *, int, unsigned char *, unsigned int *, DSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DSA_size(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DSA_size(DSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DSA_verify(p_int, unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int DSA_verify(int, unsigned char *, int, unsigned char *, int, DSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def DTLSv1_client_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *DTLSv1_client_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def DTLSv1_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *DTLSv1_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def DTLSv1_server_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *DTLSv1_server_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def ECDH_compute_key(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ECDH_compute_key(void *, size_t, EC_POINT *, EC_KEY *, void *(*)(void *, size_t, void *, size_t *));
    
    CFFI C function from _openssl.lib
    """
    pass

def ECDSA_do_sign(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ECDSA_SIG *ECDSA_do_sign(unsigned char *, int, EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ECDSA_do_sign_ex(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ECDSA_SIG *ECDSA_do_sign_ex(unsigned char *, int, BIGNUM *, BIGNUM *, EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ECDSA_do_verify(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ECDSA_do_verify(unsigned char *, int, ECDSA_SIG *, EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ECDSA_sign(p_int, unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ECDSA_sign(int, unsigned char *, int, unsigned char *, unsigned int *, EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ECDSA_sign_ex(p_int, unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ECDSA_sign_ex(int, unsigned char *, int, unsigned char *, unsigned int *, BIGNUM *, BIGNUM *, EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ECDSA_sign_setup(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ECDSA_sign_setup(EC_KEY *, BN_CTX *, BIGNUM * *, BIGNUM * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ECDSA_SIG_free(ECDSA_SIG, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ECDSA_SIG_free(ECDSA_SIG *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ECDSA_SIG_new(): # real signature unknown; restored from __doc__
    """
    ECDSA_SIG *ECDSA_SIG_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def ECDSA_size(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ECDSA_size(EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ECDSA_verify(p_int, unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ECDSA_verify(int, unsigned char *, int, unsigned char *, int, EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_curve_nid2nist(p_int): # real signature unknown; restored from __doc__
    """
    char *EC_curve_nid2nist(int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_get_builtin_curves(EC_builtin_curve, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    size_t EC_get_builtin_curves(EC_builtin_curve *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GF2m_simple_method(): # real signature unknown; restored from __doc__
    """
    EC_METHOD *EC_GF2m_simple_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GFp_mont_method(): # real signature unknown; restored from __doc__
    """
    EC_METHOD *EC_GFp_mont_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GFp_nist_method(): # real signature unknown; restored from __doc__
    """
    EC_METHOD *EC_GFp_nist_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GFp_simple_method(): # real signature unknown; restored from __doc__
    """
    EC_METHOD *EC_GFp_simple_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_clear_free(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EC_GROUP_clear_free(EC_GROUP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_free(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EC_GROUP_free(EC_GROUP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_get0_generator(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_POINT *EC_GROUP_get0_generator(EC_GROUP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_get_curve_GF2m(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_GROUP_get_curve_GF2m(EC_GROUP *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_get_curve_GFp(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_GROUP_get_curve_GFp(EC_GROUP *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_get_curve_name(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_GROUP_get_curve_name(EC_GROUP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_get_degree(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_GROUP_get_degree(EC_GROUP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_get_order(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_GROUP_get_order(EC_GROUP *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_have_precompute_mult(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_GROUP_have_precompute_mult(EC_GROUP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_method_of(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_METHOD *EC_GROUP_method_of(EC_GROUP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_new(EC_METHOD, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_GROUP *EC_GROUP_new(EC_METHOD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_new_by_curve_name(p_int): # real signature unknown; restored from __doc__
    """
    EC_GROUP *EC_GROUP_new_by_curve_name(int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_new_curve_GF2m(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_GROUP *EC_GROUP_new_curve_GF2m(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_new_curve_GFp(BIGNUM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_GROUP *EC_GROUP_new_curve_GFp(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_precompute_mult(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_GROUP_precompute_mult(EC_GROUP *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_set_asn1_flag(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EC_GROUP_set_asn1_flag(EC_GROUP *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_set_curve_GF2m(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_GROUP_set_curve_GF2m(EC_GROUP *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_set_curve_GFp(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_GROUP_set_curve_GFp(EC_GROUP *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_GROUP_set_point_conversion_form(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EC_GROUP_set_point_conversion_form(EC_GROUP *, point_conversion_form_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_check_key(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_KEY_check_key(EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_clear_flags(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EC_KEY_clear_flags(EC_KEY *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_copy(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_KEY *EC_KEY_copy(EC_KEY *, EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_dup(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_KEY *EC_KEY_dup(EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_free(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EC_KEY_free(EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_generate_key(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_KEY_generate_key(EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_get0_group(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_GROUP *EC_KEY_get0_group(EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_get0_private_key(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    BIGNUM *EC_KEY_get0_private_key(EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_get0_public_key(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_POINT *EC_KEY_get0_public_key(EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_get_conv_form(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    point_conversion_form_t EC_KEY_get_conv_form(EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_get_enc_flags(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned int EC_KEY_get_enc_flags(EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_get_flags(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_KEY_get_flags(EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_new(): # real signature unknown; restored from __doc__
    """
    EC_KEY *EC_KEY_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_new_by_curve_name(p_int): # real signature unknown; restored from __doc__
    """
    EC_KEY *EC_KEY_new_by_curve_name(int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_precompute_mult(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_KEY_precompute_mult(EC_KEY *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_set_asn1_flag(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EC_KEY_set_asn1_flag(EC_KEY *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_set_conv_form(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EC_KEY_set_conv_form(EC_KEY *, point_conversion_form_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_set_enc_flags(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EC_KEY_set_enc_flags(EC_KEY *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_set_flags(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EC_KEY_set_flags(EC_KEY *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_set_group(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_KEY_set_group(EC_KEY *, EC_GROUP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_set_private_key(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_KEY_set_private_key(EC_KEY *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_set_public_key(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_KEY_set_public_key(EC_KEY *, EC_POINT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_set_public_key_affine_coordinates(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_KEY_set_public_key_affine_coordinates(EC_KEY *, BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_KEY_up_ref(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_KEY_up_ref(EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_METHOD_get_field_type(EC_METHOD, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_METHOD_get_field_type(EC_METHOD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINTs_make_affine(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINTs_make_affine(EC_GROUP *, size_t, EC_POINT * *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINTs_mul(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINTs_mul(EC_GROUP *, EC_POINT *, BIGNUM *, size_t, EC_POINT * *, BIGNUM * *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_add(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_add(EC_GROUP *, EC_POINT *, EC_POINT *, EC_POINT *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_bn2point(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_POINT *EC_POINT_bn2point(EC_GROUP *, BIGNUM *, EC_POINT *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_clear_free(EC_POINT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EC_POINT_clear_free(EC_POINT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_cmp(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_cmp(EC_GROUP *, EC_POINT *, EC_POINT *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_copy(EC_POINT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_copy(EC_POINT *, EC_POINT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_dbl(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_dbl(EC_GROUP *, EC_POINT *, EC_POINT *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_dup(EC_POINT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_POINT *EC_POINT_dup(EC_POINT *, EC_GROUP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_free(EC_POINT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EC_POINT_free(EC_POINT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_get_affine_coordinates_GF2m(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_get_affine_coordinates_GF2m(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_get_affine_coordinates_GFp(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_get_affine_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_get_Jprojective_coordinates_GFp(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_get_Jprojective_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_hex2point(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_POINT *EC_POINT_hex2point(EC_GROUP *, char *, EC_POINT *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_invert(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_invert(EC_GROUP *, EC_POINT *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_is_at_infinity(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_is_at_infinity(EC_GROUP *, EC_POINT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_is_on_curve(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_is_on_curve(EC_GROUP *, EC_POINT *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_make_affine(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_make_affine(EC_GROUP *, EC_POINT *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_method_of(EC_POINT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_METHOD *EC_POINT_method_of(EC_POINT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_mul(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_mul(EC_GROUP *, EC_POINT *, BIGNUM *, EC_POINT *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_new(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_POINT *EC_POINT_new(EC_GROUP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_oct2point(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_oct2point(EC_GROUP *, EC_POINT *, unsigned char *, size_t, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_point2bn(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    BIGNUM *EC_POINT_point2bn(EC_GROUP *, EC_POINT *, point_conversion_form_t, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_point2hex(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *EC_POINT_point2hex(EC_GROUP *, EC_POINT *, point_conversion_form_t, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_point2oct(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    size_t EC_POINT_point2oct(EC_GROUP *, EC_POINT *, point_conversion_form_t, unsigned char *, size_t, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_set_affine_coordinates_GF2m(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_set_affine_coordinates_GF2m(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_set_affine_coordinates_GFp(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_set_affine_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_set_compressed_coordinates_GF2m(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_set_compressed_coordinates_GF2m(EC_GROUP *, EC_POINT *, BIGNUM *, int, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_set_compressed_coordinates_GFp(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_set_compressed_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, int, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_set_Jprojective_coordinates_GFp(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_set_Jprojective_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EC_POINT_set_to_infinity(EC_GROUP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EC_POINT_set_to_infinity(EC_GROUP *, EC_POINT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_add(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_add(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_add_conf_module(): # real signature unknown; restored from __doc__
    """
    void ENGINE_add_conf_module();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_by_id(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ENGINE *ENGINE_by_id(char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_cleanup(): # real signature unknown; restored from __doc__
    """
    void ENGINE_cleanup();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_cmd_is_executable(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_cmd_is_executable(ENGINE *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_ctrl(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_ctrl(ENGINE *, int, long, void *, void(*)());
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_ctrl_cmd(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_ctrl_cmd(ENGINE *, char *, long, void *, void(*)(), int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_ctrl_cmd_string(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_ctrl_cmd_string(ENGINE *, char *, char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_finish(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_finish(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_free(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_free(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_cipher(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_CIPHER *ENGINE_get_cipher(ENGINE *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_cipher_engine(p_int): # real signature unknown; restored from __doc__
    """
    ENGINE *ENGINE_get_cipher_engine(int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_cmd_defns(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ENGINE_CMD_DEFN *ENGINE_get_cmd_defns(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_default_DH(): # real signature unknown; restored from __doc__
    """
    ENGINE *ENGINE_get_default_DH();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_default_DSA(): # real signature unknown; restored from __doc__
    """
    ENGINE *ENGINE_get_default_DSA();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_default_RAND(): # real signature unknown; restored from __doc__
    """
    ENGINE *ENGINE_get_default_RAND();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_default_RSA(): # real signature unknown; restored from __doc__
    """
    ENGINE *ENGINE_get_default_RSA();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_DH(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DH_METHOD *ENGINE_get_DH(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_digest(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_MD *ENGINE_get_digest(ENGINE *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_digest_engine(p_int): # real signature unknown; restored from __doc__
    """
    ENGINE *ENGINE_get_digest_engine(int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_DSA(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DSA_METHOD *ENGINE_get_DSA(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_first(): # real signature unknown; restored from __doc__
    """
    ENGINE *ENGINE_get_first();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_flags(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_get_flags(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_id(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *ENGINE_get_id(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_last(): # real signature unknown; restored from __doc__
    """
    ENGINE *ENGINE_get_last();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_name(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *ENGINE_get_name(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_next(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ENGINE *ENGINE_get_next(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_prev(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ENGINE *ENGINE_get_prev(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_RAND(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    RAND_METHOD *ENGINE_get_RAND(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_RSA(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    RSA_METHOD *ENGINE_get_RSA(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_get_table_flags(): # real signature unknown; restored from __doc__
    """
    unsigned int ENGINE_get_table_flags();
    
    CFFI C function from _openssl.lib
    """
    return 0

def ENGINE_init(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_init(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_load_builtin_engines(): # real signature unknown; restored from __doc__
    """
    void ENGINE_load_builtin_engines();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_load_cryptodev(): # real signature unknown; restored from __doc__
    """
    void ENGINE_load_cryptodev();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_load_dynamic(): # real signature unknown; restored from __doc__
    """
    void ENGINE_load_dynamic();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_load_openssl(): # real signature unknown; restored from __doc__
    """
    void ENGINE_load_openssl();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_load_private_key(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY *ENGINE_load_private_key(ENGINE *, char *, UI_METHOD *, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_load_public_key(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY *ENGINE_load_public_key(ENGINE *, char *, UI_METHOD *, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_new(): # real signature unknown; restored from __doc__
    """
    ENGINE *ENGINE_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_all_ciphers(): # real signature unknown; restored from __doc__
    """
    void ENGINE_register_all_ciphers();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_all_complete(): # real signature unknown; restored from __doc__
    """
    int ENGINE_register_all_complete();
    
    CFFI C function from _openssl.lib
    """
    return 0

def ENGINE_register_all_DH(): # real signature unknown; restored from __doc__
    """
    void ENGINE_register_all_DH();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_all_digests(): # real signature unknown; restored from __doc__
    """
    void ENGINE_register_all_digests();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_all_DSA(): # real signature unknown; restored from __doc__
    """
    void ENGINE_register_all_DSA();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_all_RAND(): # real signature unknown; restored from __doc__
    """
    void ENGINE_register_all_RAND();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_all_RSA(): # real signature unknown; restored from __doc__
    """
    void ENGINE_register_all_RSA();
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_ciphers(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_register_ciphers(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_complete(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_register_complete(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_DH(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_register_DH(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_digests(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_register_digests(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_DSA(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_register_DSA(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_RAND(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_register_RAND(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_register_RSA(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_register_RSA(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_remove(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_remove(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_ciphers(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_ciphers(ENGINE *, struct $$ENGINE_CIPHERS_PTR *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_cmd_defns(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_cmd_defns(ENGINE *, ENGINE_CMD_DEFN *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_ctrl_function(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_ctrl_function(ENGINE *, struct $$ENGINE_CTRL_FUNC_PTR *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_default(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_default(ENGINE *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_default_ciphers(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_default_ciphers(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_default_DH(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_default_DH(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_default_digests(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_default_digests(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_default_DSA(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_default_DSA(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_default_RAND(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_default_RAND(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_default_RSA(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_default_RSA(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_default_string(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_default_string(ENGINE *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_destroy_function(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_destroy_function(ENGINE *, int(*)(ENGINE *));
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_DH(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_DH(ENGINE *, DH_METHOD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_digests(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_digests(ENGINE *, struct $$ENGINE_DIGESTS_PTR *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_DSA(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_DSA(ENGINE *, DSA_METHOD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_finish_function(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_finish_function(ENGINE *, int(*)(ENGINE *));
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_flags(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_flags(ENGINE *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_id(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_id(ENGINE *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_init_function(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_init_function(ENGINE *, int(*)(ENGINE *));
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_load_privkey_function(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_load_privkey_function(ENGINE *, struct $$ENGINE_LOAD_KEY_PTR *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_load_pubkey_function(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_load_pubkey_function(ENGINE *, struct $$ENGINE_LOAD_KEY_PTR *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_name(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_name(ENGINE *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_RAND(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_RAND(ENGINE *, RAND_METHOD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_RSA(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_set_RSA(ENGINE *, RSA_METHOD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_set_table_flags(unsigned_int): # real signature unknown; restored from __doc__
    """
    void ENGINE_set_table_flags(unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_unregister_ciphers(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ENGINE_unregister_ciphers(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_unregister_DH(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ENGINE_unregister_DH(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_unregister_digests(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ENGINE_unregister_digests(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_unregister_DSA(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ENGINE_unregister_DSA(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_unregister_RAND(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ENGINE_unregister_RAND(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_unregister_RSA(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ENGINE_unregister_RSA(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ENGINE_up_ref(ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ENGINE_up_ref(ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_clear_error(): # real signature unknown; restored from __doc__
    """
    void ERR_clear_error();
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_error_string(unsigned_long, char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *ERR_error_string(unsigned long, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_error_string_n(unsigned_long, char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ERR_error_string_n(unsigned long, char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_free_strings(): # real signature unknown; restored from __doc__
    """
    void ERR_free_strings();
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_func_error_string(unsigned_long): # real signature unknown; restored from __doc__
    """
    char *ERR_func_error_string(unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_get_error(): # real signature unknown; restored from __doc__
    """
    unsigned long ERR_get_error();
    
    CFFI C function from _openssl.lib
    """
    return 0

def ERR_get_error_line(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long ERR_get_error_line(char * *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_get_error_line_data(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long ERR_get_error_line_data(char * *, int *, char * *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_GET_FUNC(unsigned_long): # real signature unknown; restored from __doc__
    """
    int ERR_GET_FUNC(unsigned long);
    
    CFFI C function from _openssl.lib
    """
    return 0

def ERR_GET_LIB(unsigned_long): # real signature unknown; restored from __doc__
    """
    int ERR_GET_LIB(unsigned long);
    
    CFFI C function from _openssl.lib
    """
    return 0

def ERR_get_next_error_library(): # real signature unknown; restored from __doc__
    """
    int ERR_get_next_error_library();
    
    CFFI C function from _openssl.lib
    """
    return 0

def ERR_GET_REASON(unsigned_long): # real signature unknown; restored from __doc__
    """
    int ERR_GET_REASON(unsigned long);
    
    CFFI C function from _openssl.lib
    """
    return 0

def ERR_get_state(): # real signature unknown; restored from __doc__
    """
    ERR_STATE *ERR_get_state();
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_lib_error_string(unsigned_long): # real signature unknown; restored from __doc__
    """
    char *ERR_lib_error_string(unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_load_RAND_strings(): # real signature unknown; restored from __doc__
    """
    void ERR_load_RAND_strings();
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_PACK(p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
    """
    unsigned long ERR_PACK(int, int, int);
    
    CFFI C function from _openssl.lib
    """
    return 0

def ERR_peek_error(): # real signature unknown; restored from __doc__
    """
    unsigned long ERR_peek_error();
    
    CFFI C function from _openssl.lib
    """
    return 0

def ERR_peek_error_line(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long ERR_peek_error_line(char * *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_peek_error_line_data(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long ERR_peek_error_line_data(char * *, int *, char * *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_peek_last_error(): # real signature unknown; restored from __doc__
    """
    unsigned long ERR_peek_last_error();
    
    CFFI C function from _openssl.lib
    """
    return 0

def ERR_peek_last_error_line(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long ERR_peek_last_error_line(char * *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_peek_last_error_line_data(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long ERR_peek_last_error_line_data(char * *, int *, char * *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_print_errors(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ERR_print_errors(struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_print_errors_fp(FILE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ERR_print_errors_fp(FILE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_put_error(p_int, p_int_1, p_int_2, char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ERR_put_error(int, int, int, char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def ERR_reason_error_string(unsigned_long): # real signature unknown; restored from __doc__
    """
    char *ERR_reason_error_string(unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CipherFinal_ex(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_CipherFinal_ex(EVP_CIPHER_CTX *, unsigned char *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CipherInit_ex(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_CipherInit_ex(EVP_CIPHER_CTX *, EVP_CIPHER *, ENGINE *, unsigned char *, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CipherUpdate(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_CipherUpdate(EVP_CIPHER_CTX *, unsigned char *, int *, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CIPHER_block_size(EVP_CIPHER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_CIPHER_block_size(EVP_CIPHER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CIPHER_CTX_block_size(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_CIPHER_CTX_block_size(EVP_CIPHER_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CIPHER_CTX_cipher(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_CIPHER *EVP_CIPHER_CTX_cipher(EVP_CIPHER_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CIPHER_CTX_cleanup(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_CIPHER_CTX_cleanup(EVP_CIPHER_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CIPHER_CTX_ctrl(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_CIPHER_CTX_ctrl(EVP_CIPHER_CTX *, int, int, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CIPHER_CTX_free(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EVP_CIPHER_CTX_free(EVP_CIPHER_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CIPHER_CTX_init(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EVP_CIPHER_CTX_init(EVP_CIPHER_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CIPHER_CTX_new(): # real signature unknown; restored from __doc__
    """
    EVP_CIPHER_CTX *EVP_CIPHER_CTX_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CIPHER_CTX_set_key_length(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_CIPHER_CTX_set_key_length(EVP_CIPHER_CTX *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_CIPHER_CTX_set_padding(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_CIPHER_CTX_set_padding(EVP_CIPHER_CTX *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_DecryptFinal_ex(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_DecryptFinal_ex(EVP_CIPHER_CTX *, unsigned char *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_DecryptInit_ex(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_DecryptInit_ex(EVP_CIPHER_CTX *, EVP_CIPHER *, ENGINE *, unsigned char *, unsigned char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_DecryptUpdate(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_DecryptUpdate(EVP_CIPHER_CTX *, unsigned char *, int *, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_DigestFinal_ex(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_DigestFinal_ex(EVP_MD_CTX *, unsigned char *, unsigned int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_DigestInit_ex(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_DigestInit_ex(EVP_MD_CTX *, EVP_MD *, ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_DigestUpdate(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_DigestUpdate(EVP_MD_CTX *, void *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_EncryptFinal_ex(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_EncryptFinal_ex(EVP_CIPHER_CTX *, unsigned char *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_EncryptInit_ex(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_EncryptInit_ex(EVP_CIPHER_CTX *, EVP_CIPHER *, ENGINE *, unsigned char *, unsigned char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_EncryptUpdate(EVP_CIPHER_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_EncryptUpdate(EVP_CIPHER_CTX *, unsigned char *, int *, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_get_cipherbyname(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_CIPHER *EVP_get_cipherbyname(char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_get_digestbyname(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_MD *EVP_get_digestbyname(char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_md5(): # real signature unknown; restored from __doc__
    """
    EVP_MD *EVP_md5();
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_MD_CTX_block_size(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_MD_CTX_block_size(EVP_MD_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_MD_CTX_copy_ex(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_MD_CTX_copy_ex(EVP_MD_CTX *, EVP_MD_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_MD_CTX_md(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_MD *EVP_MD_CTX_md(EVP_MD_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_MD_size(EVP_MD, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_MD_size(EVP_MD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PBE_scrypt(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PBE_scrypt(char *, size_t, unsigned char *, size_t, uint64_t, uint64_t, uint64_t, uint64_t, unsigned char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKCS82PKEY(PKCS8_PRIV_KEY_INFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY *EVP_PKCS82PKEY(PKCS8_PRIV_KEY_INFO *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_add1_attr(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_add1_attr(EVP_PKEY *, X509_ATTRIBUTE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_add1_attr_by_NID(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_add1_attr_by_NID(EVP_PKEY *, int, int, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_add1_attr_by_OBJ(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_add1_attr_by_OBJ(EVP_PKEY *, ASN1_OBJECT *, int, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_add1_attr_by_txt(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_add1_attr_by_txt(EVP_PKEY *, char *, int, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_assign_DSA(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_assign_DSA(EVP_PKEY *, DSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_assign_EC_KEY(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_assign_EC_KEY(EVP_PKEY *, EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_assign_RSA(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_assign_RSA(EVP_PKEY *, RSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_bits(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_bits(EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_cmp(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_cmp(EVP_PKEY *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_CTX_dup(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY_CTX *EVP_PKEY_CTX_dup(EVP_PKEY_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_CTX_free(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EVP_PKEY_CTX_free(EVP_PKEY_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_CTX_new(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY_CTX *EVP_PKEY_CTX_new(EVP_PKEY *, ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_CTX_new_id(p_int, ENGINE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY_CTX *EVP_PKEY_CTX_new_id(int, ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_CTX_set_rsa_mgf1_md(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_CTX_set_rsa_mgf1_md(EVP_PKEY_CTX *, EVP_MD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_CTX_set_rsa_oaep_md(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_CTX_set_rsa_oaep_md(EVP_PKEY_CTX *, EVP_MD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_CTX_set_rsa_padding(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_CTX_set_rsa_padding(EVP_PKEY_CTX *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_CTX_set_rsa_pss_saltlen(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_CTX_set_rsa_pss_saltlen(EVP_PKEY_CTX *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_CTX_set_signature_md(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_CTX_set_signature_md(EVP_PKEY_CTX *, EVP_MD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_decrypt(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_decrypt(EVP_PKEY_CTX *, unsigned char *, size_t *, unsigned char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_decrypt_init(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_decrypt_init(EVP_PKEY_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_delete_attr(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_ATTRIBUTE *EVP_PKEY_delete_attr(EVP_PKEY *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_encrypt(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_encrypt(EVP_PKEY_CTX *, unsigned char *, size_t *, unsigned char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_encrypt_init(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_encrypt_init(EVP_PKEY_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_free(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void EVP_PKEY_free(EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_get1_DH(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DH *EVP_PKEY_get1_DH(EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_get1_DSA(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DSA *EVP_PKEY_get1_DSA(EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_get1_EC_KEY(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_KEY *EVP_PKEY_get1_EC_KEY(EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_get1_RSA(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    RSA *EVP_PKEY_get1_RSA(EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_get_attr(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_ATTRIBUTE *EVP_PKEY_get_attr(EVP_PKEY *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_get_attr_by_NID(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_get_attr_by_NID(EVP_PKEY *, int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_get_attr_count(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_get_attr_count(EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_id(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_id(EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_new(): # real signature unknown; restored from __doc__
    """
    EVP_PKEY *EVP_PKEY_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_set1_DH(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_set1_DH(EVP_PKEY *, DH *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_set1_DSA(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_set1_DSA(EVP_PKEY *, DSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_set1_EC_KEY(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_set1_EC_KEY(EVP_PKEY *, EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_set1_RSA(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_set1_RSA(EVP_PKEY *, RSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_sign(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_sign(EVP_PKEY_CTX *, unsigned char *, size_t *, unsigned char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_sign_init(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_sign_init(EVP_PKEY_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_size(EVP_PKEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_size(EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_type(p_int): # real signature unknown; restored from __doc__
    """
    int EVP_PKEY_type(int);
    
    CFFI C function from _openssl.lib
    """
    return 0

def EVP_PKEY_verify(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_verify(EVP_PKEY_CTX *, unsigned char *, size_t, unsigned char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_PKEY_verify_init(EVP_PKEY_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_PKEY_verify_init(EVP_PKEY_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_ripemd160(): # real signature unknown; restored from __doc__
    """
    EVP_MD *EVP_ripemd160();
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_sha1(): # real signature unknown; restored from __doc__
    """
    EVP_MD *EVP_sha1();
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_sha224(): # real signature unknown; restored from __doc__
    """
    EVP_MD *EVP_sha224();
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_sha256(): # real signature unknown; restored from __doc__
    """
    EVP_MD *EVP_sha256();
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_sha384(): # real signature unknown; restored from __doc__
    """
    EVP_MD *EVP_sha384();
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_sha512(): # real signature unknown; restored from __doc__
    """
    EVP_MD *EVP_sha512();
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_SignFinal(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_SignFinal(EVP_MD_CTX *, unsigned char *, unsigned int *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_SignInit(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_SignInit(EVP_MD_CTX *, EVP_MD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_SignUpdate(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_SignUpdate(EVP_MD_CTX *, void *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_VerifyFinal(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_VerifyFinal(EVP_MD_CTX *, unsigned char *, unsigned int, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_VerifyInit(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_VerifyInit(EVP_MD_CTX *, EVP_MD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def EVP_VerifyUpdate(EVP_MD_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int EVP_VerifyUpdate(EVP_MD_CTX *, void *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def GENERAL_NAMES_free(struct_stack_st_GENERAL_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void GENERAL_NAMES_free(struct stack_st_GENERAL_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def GENERAL_NAMES_new(): # real signature unknown; restored from __doc__
    """
    struct stack_st_GENERAL_NAME *GENERAL_NAMES_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def GENERAL_NAME_free(GENERAL_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void GENERAL_NAME_free(GENERAL_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def GENERAL_NAME_new(): # real signature unknown; restored from __doc__
    """
    GENERAL_NAME *GENERAL_NAME_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def GENERAL_NAME_print(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int GENERAL_NAME_print(struct bio_st *, GENERAL_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def GENERAL_SUBTREE_new(): # real signature unknown; restored from __doc__
    """
    GENERAL_SUBTREE *GENERAL_SUBTREE_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def HMAC_CTX_copy(HMAC_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int HMAC_CTX_copy(HMAC_CTX *, HMAC_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def HMAC_Final(HMAC_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int HMAC_Final(HMAC_CTX *, unsigned char *, unsigned int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def HMAC_Init_ex(HMAC_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int HMAC_Init_ex(HMAC_CTX *, void *, int, EVP_MD *, ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def HMAC_Update(HMAC_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int HMAC_Update(HMAC_CTX *, unsigned char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2a_ASN1_INTEGER(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2a_ASN1_INTEGER(struct bio_st *, ASN1_INTEGER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_ASN1_BIT_STRING(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_ASN1_BIT_STRING(struct asn1_string_st *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_ASN1_ENUMERATED(ASN1_ENUMERATED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_ASN1_ENUMERATED(ASN1_ENUMERATED *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_ASN1_GENERALIZEDTIME(ASN1_GENERALIZEDTIME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_ASN1_GENERALIZEDTIME(ASN1_GENERALIZEDTIME *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_ASN1_INTEGER(ASN1_INTEGER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_ASN1_INTEGER(ASN1_INTEGER *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_ASN1_OBJECT(ASN1_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_ASN1_OBJECT(ASN1_OBJECT *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_ASN1_OCTET_STRING(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_ASN1_OCTET_STRING(struct asn1_string_st *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_ASN1_TYPE(ASN1_TYPE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_ASN1_TYPE(ASN1_TYPE *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_CMS_bio_stream(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_CMS_bio_stream(struct bio_st *, CMS_ContentInfo *, struct bio_st *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_DHparams(DH, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_DHparams(DH *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_DSAPrivateKey(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_DSAPrivateKey(DSA *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_DSAPrivateKey_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_DSAPrivateKey_bio(struct bio_st *, DSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_DSAPublicKey(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_DSAPublicKey(DSA *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_DSA_PUBKEY(DSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_DSA_PUBKEY(DSA *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_DSA_PUBKEY_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_DSA_PUBKEY_bio(struct bio_st *, DSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_ECDSA_SIG(ECDSA_SIG, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_ECDSA_SIG(ECDSA_SIG *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_ECPrivateKey(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_ECPrivateKey(EC_KEY *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_ECPrivateKey_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_ECPrivateKey_bio(struct bio_st *, EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_EC_PUBKEY(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_EC_PUBKEY(EC_KEY *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_EC_PUBKEY_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_EC_PUBKEY_bio(struct bio_st *, EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_GENERAL_NAMES(struct_stack_st_GENERAL_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_GENERAL_NAMES(struct stack_st_GENERAL_NAME *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_OCSP_REQUEST_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_OCSP_REQUEST_bio(struct bio_st *, OCSP_REQUEST *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_OCSP_RESPONSE_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_OCSP_RESPONSE_bio(struct bio_st *, OCSP_RESPONSE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_PKCS12_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_PKCS12_bio(struct bio_st *, PKCS12 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_PKCS7_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_PKCS7_bio(struct bio_st *, PKCS7 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_PKCS8PrivateKey_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_PKCS8PrivateKey_bio(struct bio_st *, EVP_PKEY *, EVP_CIPHER *, char *, int, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_PKCS8PrivateKey_nid_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_PKCS8PrivateKey_nid_bio(struct bio_st *, EVP_PKEY *, int, char *, int, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_PrivateKey_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_PrivateKey_bio(struct bio_st *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_PUBKEY_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_PUBKEY_bio(struct bio_st *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_re_X509_CRL_tbs(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_re_X509_CRL_tbs(X509_CRL *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_re_X509_REQ_tbs(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_re_X509_REQ_tbs(X509_REQ *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_re_X509_tbs(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_re_X509_tbs(X509 *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_RSAPrivateKey(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_RSAPrivateKey(RSA *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_RSAPrivateKey_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_RSAPrivateKey_bio(struct bio_st *, RSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_RSAPublicKey(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_RSAPublicKey(RSA *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_RSAPublicKey_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_RSAPublicKey_bio(struct bio_st *, RSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_RSA_PUBKEY(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_RSA_PUBKEY(RSA *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_RSA_PUBKEY_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_RSA_PUBKEY_bio(struct bio_st *, RSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_X509(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_X509(X509 *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_X509_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_X509_bio(struct bio_st *, X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_X509_CINF(X509_CINF, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_X509_CINF(X509_CINF *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_X509_CRL_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_X509_CRL_bio(struct bio_st *, X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_X509_CRL_INFO(X509_CRL_INFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_X509_CRL_INFO(X509_CRL_INFO *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_X509_NAME(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_X509_NAME(X509_NAME *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_X509_REQ_bio(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_X509_REQ_bio(struct bio_st *, X509_REQ *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2d_X509_REQ_INFO(X509_REQ_INFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2d_X509_REQ_INFO(X509_REQ_INFO *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def i2o_ECPublicKey(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int i2o_ECPublicKey(EC_KEY *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def M_ASN1_TIME_dup(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct asn1_string_st *M_ASN1_TIME_dup(void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def NAME_CONSTRAINTS_free(NAME_CONSTRAINTS, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void NAME_CONSTRAINTS_free(NAME_CONSTRAINTS *);
    
    CFFI C function from _openssl.lib
    """
    pass

def NAME_CONSTRAINTS_new(): # real signature unknown; restored from __doc__
    """
    NAME_CONSTRAINTS *NAME_CONSTRAINTS_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def NETSCAPE_SPKI_b64_decode(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    NETSCAPE_SPKI *NETSCAPE_SPKI_b64_decode(char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def NETSCAPE_SPKI_b64_encode(NETSCAPE_SPKI, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *NETSCAPE_SPKI_b64_encode(NETSCAPE_SPKI *);
    
    CFFI C function from _openssl.lib
    """
    pass

def NETSCAPE_SPKI_free(NETSCAPE_SPKI, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void NETSCAPE_SPKI_free(NETSCAPE_SPKI *);
    
    CFFI C function from _openssl.lib
    """
    pass

def NETSCAPE_SPKI_get_pubkey(NETSCAPE_SPKI, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY *NETSCAPE_SPKI_get_pubkey(NETSCAPE_SPKI *);
    
    CFFI C function from _openssl.lib
    """
    pass

def NETSCAPE_SPKI_new(): # real signature unknown; restored from __doc__
    """
    NETSCAPE_SPKI *NETSCAPE_SPKI_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def NETSCAPE_SPKI_set_pubkey(NETSCAPE_SPKI, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int NETSCAPE_SPKI_set_pubkey(NETSCAPE_SPKI *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def NETSCAPE_SPKI_sign(NETSCAPE_SPKI, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int NETSCAPE_SPKI_sign(NETSCAPE_SPKI *, EVP_PKEY *, EVP_MD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def NETSCAPE_SPKI_verify(NETSCAPE_SPKI, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int NETSCAPE_SPKI_verify(NETSCAPE_SPKI *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def NOTICEREF_free(NOTICEREF, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void NOTICEREF_free(NOTICEREF *);
    
    CFFI C function from _openssl.lib
    """
    pass

def NOTICEREF_new(): # real signature unknown; restored from __doc__
    """
    NOTICEREF *NOTICEREF_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def o2i_ECPublicKey(EC_KEY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EC_KEY *o2i_ECPublicKey(EC_KEY * *, unsigned char * *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_cleanup(): # real signature unknown; restored from __doc__
    """
    void OBJ_cleanup();
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_cmp(ASN1_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OBJ_cmp(ASN1_OBJECT *, ASN1_OBJECT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_create(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OBJ_create(char *, char *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_dup(ASN1_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_OBJECT *OBJ_dup(ASN1_OBJECT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_ln2nid(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OBJ_ln2nid(char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_NAME_do_all(p_int, void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void OBJ_NAME_do_all(int, void(*)(OBJ_NAME *, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_nid2ln(p_int): # real signature unknown; restored from __doc__
    """
    char *OBJ_nid2ln(int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_nid2obj(p_int): # real signature unknown; restored from __doc__
    """
    ASN1_OBJECT *OBJ_nid2obj(int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_nid2sn(p_int): # real signature unknown; restored from __doc__
    """
    char *OBJ_nid2sn(int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_obj2nid(ASN1_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OBJ_obj2nid(ASN1_OBJECT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_obj2txt(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OBJ_obj2txt(char *, int, ASN1_OBJECT *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_sn2nid(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OBJ_sn2nid(char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_txt2nid(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OBJ_txt2nid(char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OBJ_txt2obj(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_OBJECT *OBJ_txt2obj(char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_BASICRESP_add1_ext_i2d(OCSP_BASICRESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_BASICRESP_add1_ext_i2d(OCSP_BASICRESP *, int, void *, int, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_BASICRESP_free(OCSP_BASICRESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void OCSP_BASICRESP_free(OCSP_BASICRESP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_BASICRESP_get_ext(OCSP_BASICRESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *OCSP_BASICRESP_get_ext(OCSP_BASICRESP *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_BASICRESP_get_ext_count(OCSP_BASICRESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_BASICRESP_get_ext_count(OCSP_BASICRESP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_BASICRESP_new(): # real signature unknown; restored from __doc__
    """
    OCSP_BASICRESP *OCSP_BASICRESP_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_basic_add1_cert(OCSP_BASICRESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_basic_add1_cert(OCSP_BASICRESP *, X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_basic_add1_nonce(OCSP_BASICRESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_basic_add1_nonce(OCSP_BASICRESP *, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_basic_add1_status(OCSP_BASICRESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    OCSP_SINGLERESP *OCSP_basic_add1_status(OCSP_BASICRESP *, OCSP_CERTID *, int, int, struct asn1_string_st *, struct asn1_string_st *, struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_basic_sign(OCSP_BASICRESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_basic_sign(OCSP_BASICRESP *, X509 *, EVP_PKEY *, EVP_MD *, Cryptography_STACK_OF_X509 *, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_onereq_get0_id(OCSP_ONEREQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    OCSP_CERTID *OCSP_onereq_get0_id(OCSP_ONEREQ *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_ONEREQ_get_ext(OCSP_ONEREQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *OCSP_ONEREQ_get_ext(OCSP_ONEREQ *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_ONEREQ_get_ext_count(OCSP_ONEREQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_ONEREQ_get_ext_count(OCSP_ONEREQ *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_REQUEST_add1_ext_i2d(OCSP_REQUEST, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_REQUEST_add1_ext_i2d(OCSP_REQUEST *, int, void *, int, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_request_add1_nonce(OCSP_REQUEST, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_request_add1_nonce(OCSP_REQUEST *, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_REQUEST_free(OCSP_REQUEST, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void OCSP_REQUEST_free(OCSP_REQUEST *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_REQUEST_new(): # real signature unknown; restored from __doc__
    """
    OCSP_REQUEST *OCSP_REQUEST_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_request_onereq_count(OCSP_REQUEST, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_request_onereq_count(OCSP_REQUEST *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_request_onereq_get0(OCSP_REQUEST, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    OCSP_ONEREQ *OCSP_request_onereq_get0(OCSP_REQUEST *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_response_create(p_int, OCSP_BASICRESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    OCSP_RESPONSE *OCSP_response_create(int, OCSP_BASICRESP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_response_get1_basic(OCSP_RESPONSE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    OCSP_BASICRESP *OCSP_response_get1_basic(OCSP_RESPONSE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_response_status(OCSP_RESPONSE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_response_status(OCSP_RESPONSE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_resp_count(OCSP_BASICRESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_resp_count(OCSP_BASICRESP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_resp_get0(OCSP_BASICRESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    OCSP_SINGLERESP *OCSP_resp_get0(OCSP_BASICRESP *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_SINGLERESP_get_ext(OCSP_SINGLERESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *OCSP_SINGLERESP_get_ext(OCSP_SINGLERESP *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_SINGLERESP_get_ext_count(OCSP_SINGLERESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_SINGLERESP_get_ext_count(OCSP_SINGLERESP *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OCSP_single_get0_status(OCSP_SINGLERESP, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int OCSP_single_get0_status(OCSP_SINGLERESP *, int *, ASN1_GENERALIZEDTIME * *, ASN1_GENERALIZEDTIME * *, ASN1_GENERALIZEDTIME * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OpenSSL_add_all_algorithms(): # real signature unknown; restored from __doc__
    """
    void OpenSSL_add_all_algorithms();
    
    CFFI C function from _openssl.lib
    """
    pass

def OPENSSL_config(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void OPENSSL_config(char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OPENSSL_free(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void OPENSSL_free(void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OPENSSL_malloc(size_t): # real signature unknown; restored from __doc__
    """
    void *OPENSSL_malloc(size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def OPENSSL_no_config(): # real signature unknown; restored from __doc__
    """
    void OPENSSL_no_config();
    
    CFFI C function from _openssl.lib
    """
    pass

def OpenSSL_version(p_int): # real signature unknown; restored from __doc__
    """
    char *OpenSSL_version(int);
    
    CFFI C function from _openssl.lib
    """
    pass

def OpenSSL_version_num(): # real signature unknown; restored from __doc__
    """
    unsigned long OpenSSL_version_num();
    
    CFFI C function from _openssl.lib
    """
    return 0

def OTHERNAME_free(OTHERNAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void OTHERNAME_free(OTHERNAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def OTHERNAME_new(): # real signature unknown; restored from __doc__
    """
    OTHERNAME *OTHERNAME_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_read_bio_DHparams(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DH *PEM_read_bio_DHparams(struct bio_st *, DH * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_read_bio_DSAPrivateKey(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DSA *PEM_read_bio_DSAPrivateKey(struct bio_st *, DSA * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_read_bio_DSA_PUBKEY(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DSA *PEM_read_bio_DSA_PUBKEY(struct bio_st *, DSA * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_read_bio_PKCS7(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    PKCS7 *PEM_read_bio_PKCS7(struct bio_st *, PKCS7 * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_read_bio_PrivateKey(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY *PEM_read_bio_PrivateKey(struct bio_st *, EVP_PKEY * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_read_bio_PUBKEY(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY *PEM_read_bio_PUBKEY(struct bio_st *, EVP_PKEY * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_read_bio_RSAPrivateKey(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    RSA *PEM_read_bio_RSAPrivateKey(struct bio_st *, RSA * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_read_bio_RSAPublicKey(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    RSA *PEM_read_bio_RSAPublicKey(struct bio_st *, RSA * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_read_bio_X509(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509 *PEM_read_bio_X509(struct bio_st *, X509 * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_read_bio_X509_AUX(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509 *PEM_read_bio_X509_AUX(struct bio_st *, X509 * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_read_bio_X509_CRL(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_CRL *PEM_read_bio_X509_CRL(struct bio_st *, X509_CRL * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_read_bio_X509_REQ(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_REQ *PEM_read_bio_X509_REQ(struct bio_st *, X509_REQ * *, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_CMS_stream(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_CMS_stream(struct bio_st *, CMS_ContentInfo *, struct bio_st *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_DHparams(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_DHparams(struct bio_st *, DH *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_DSAPrivateKey(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_DSAPrivateKey(struct bio_st *, DSA *, EVP_CIPHER *, unsigned char *, int, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_DSA_PUBKEY(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_DSA_PUBKEY(struct bio_st *, DSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_ECPrivateKey(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_ECPrivateKey(struct bio_st *, EC_KEY *, EVP_CIPHER *, unsigned char *, int, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_PKCS7(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_PKCS7(struct bio_st *, PKCS7 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_PKCS8PrivateKey(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_PKCS8PrivateKey(struct bio_st *, EVP_PKEY *, EVP_CIPHER *, char *, int, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_PKCS8PrivateKey_nid(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_PKCS8PrivateKey_nid(struct bio_st *, EVP_PKEY *, int, char *, int, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_PrivateKey(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_PrivateKey(struct bio_st *, EVP_PKEY *, EVP_CIPHER *, unsigned char *, int, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_PUBKEY(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_PUBKEY(struct bio_st *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_RSAPrivateKey(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_RSAPrivateKey(struct bio_st *, RSA *, EVP_CIPHER *, unsigned char *, int, int(*)(char *, int, int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_RSAPublicKey(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_RSAPublicKey(struct bio_st *, RSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_X509(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_X509(struct bio_st *, X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_X509_CRL(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_X509_CRL(struct bio_st *, X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PEM_write_bio_X509_REQ(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PEM_write_bio_X509_REQ(struct bio_st *, X509_REQ *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS12_create(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    PKCS12 *PKCS12_create(char *, char *, EVP_PKEY *, X509 *, Cryptography_STACK_OF_X509 *, int, int, int, int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS12_free(PKCS12, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void PKCS12_free(PKCS12 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS12_parse(PKCS12, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PKCS12_parse(PKCS12 *, char *, EVP_PKEY * *, X509 * *, Cryptography_STACK_OF_X509 * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS5_PBKDF2_HMAC(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PKCS5_PBKDF2_HMAC(char *, int, unsigned char *, int, int, EVP_MD *, int, unsigned char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS5_PBKDF2_HMAC_SHA1(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PKCS5_PBKDF2_HMAC_SHA1(char *, int, unsigned char *, int, int, int, unsigned char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_dataInit(PKCS7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct bio_st *PKCS7_dataInit(PKCS7 *, struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_decrypt(PKCS7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PKCS7_decrypt(PKCS7 *, EVP_PKEY *, X509 *, struct bio_st *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_encrypt(Cryptography_STACK_OF_X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    PKCS7 *PKCS7_encrypt(Cryptography_STACK_OF_X509 *, struct bio_st *, EVP_CIPHER *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_free(PKCS7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void PKCS7_free(PKCS7 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_get0_signers(PKCS7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Cryptography_STACK_OF_X509 *PKCS7_get0_signers(PKCS7 *, Cryptography_STACK_OF_X509 *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_sign(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    PKCS7 *PKCS7_sign(X509 *, EVP_PKEY *, Cryptography_STACK_OF_X509 *, struct bio_st *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_type_is_data(PKCS7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PKCS7_type_is_data(PKCS7 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_type_is_digest(PKCS7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PKCS7_type_is_digest(PKCS7 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_type_is_encrypted(PKCS7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PKCS7_type_is_encrypted(PKCS7 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_type_is_enveloped(PKCS7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PKCS7_type_is_enveloped(PKCS7 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_type_is_signed(PKCS7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PKCS7_type_is_signed(PKCS7 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_type_is_signedAndEnveloped(PKCS7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PKCS7_type_is_signedAndEnveloped(PKCS7 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS7_verify(PKCS7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int PKCS7_verify(PKCS7 *, Cryptography_STACK_OF_X509 *, X509_STORE *, struct bio_st *, struct bio_st *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def PKCS8_PRIV_KEY_INFO_free(PKCS8_PRIV_KEY_INFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void PKCS8_PRIV_KEY_INFO_free(PKCS8_PRIV_KEY_INFO *);
    
    CFFI C function from _openssl.lib
    """
    pass

def POLICYINFO_free(POLICYINFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void POLICYINFO_free(POLICYINFO *);
    
    CFFI C function from _openssl.lib
    """
    pass

def POLICYINFO_new(): # real signature unknown; restored from __doc__
    """
    POLICYINFO *POLICYINFO_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def POLICYQUALINFO_free(POLICYQUALINFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void POLICYQUALINFO_free(POLICYQUALINFO *);
    
    CFFI C function from _openssl.lib
    """
    pass

def POLICYQUALINFO_new(): # real signature unknown; restored from __doc__
    """
    POLICYQUALINFO *POLICYQUALINFO_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def POLICY_CONSTRAINTS_free(POLICY_CONSTRAINTS, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void POLICY_CONSTRAINTS_free(POLICY_CONSTRAINTS *);
    
    CFFI C function from _openssl.lib
    """
    pass

def POLICY_CONSTRAINTS_new(): # real signature unknown; restored from __doc__
    """
    POLICY_CONSTRAINTS *POLICY_CONSTRAINTS_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def RAND_add(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void RAND_add(void *, int, double);
    
    CFFI C function from _openssl.lib
    """
    pass

def RAND_bytes(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RAND_bytes(unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def RAND_cleanup(): # real signature unknown; restored from __doc__
    """
    void RAND_cleanup();
    
    CFFI C function from _openssl.lib
    """
    pass

def RAND_egd(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RAND_egd(char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RAND_egd_bytes(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RAND_egd_bytes(char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def RAND_file_name(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *RAND_file_name(char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def RAND_load_file(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RAND_load_file(char *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def RAND_query_egd_bytes(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RAND_query_egd_bytes(char *, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def RAND_seed(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void RAND_seed(void *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def RAND_status(): # real signature unknown; restored from __doc__
    """
    int RAND_status();
    
    CFFI C function from _openssl.lib
    """
    return 0

def RAND_write_file(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RAND_write_file(char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSAPublicKey_dup(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    RSA *RSAPublicKey_dup(RSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_blinding_off(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void RSA_blinding_off(RSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_blinding_on(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_blinding_on(RSA *, BN_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_check_key(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_check_key(RSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_free(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void RSA_free(RSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_generate_key_ex(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_generate_key_ex(RSA *, int, BIGNUM *, BN_GENCB *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_get0_crt_params(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void RSA_get0_crt_params(RSA *, BIGNUM * *, BIGNUM * *, BIGNUM * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_get0_factors(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void RSA_get0_factors(RSA *, BIGNUM * *, BIGNUM * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_get0_key(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void RSA_get0_key(RSA *, BIGNUM * *, BIGNUM * *, BIGNUM * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_new(): # real signature unknown; restored from __doc__
    """
    RSA *RSA_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_padding_add_PKCS1_OAEP(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_padding_add_PKCS1_OAEP(unsigned char *, int, unsigned char *, int, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_padding_add_PKCS1_PSS(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_padding_add_PKCS1_PSS(RSA *, unsigned char *, unsigned char *, EVP_MD *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_padding_check_PKCS1_OAEP(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_padding_check_PKCS1_OAEP(unsigned char *, int, unsigned char *, int, int, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_print(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_print(struct bio_st *, RSA *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_private_decrypt(p_int, unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_private_decrypt(int, unsigned char *, unsigned char *, RSA *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_private_encrypt(p_int, unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_private_encrypt(int, unsigned char *, unsigned char *, RSA *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_public_decrypt(p_int, unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_public_decrypt(int, unsigned char *, unsigned char *, RSA *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_public_encrypt(p_int, unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_public_encrypt(int, unsigned char *, unsigned char *, RSA *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_set0_crt_params(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_set0_crt_params(RSA *, BIGNUM *, BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_set0_factors(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_set0_factors(RSA *, BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_set0_key(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_set0_key(RSA *, BIGNUM *, BIGNUM *, BIGNUM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_size(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_size(RSA *);
    
    CFFI C function from _openssl.lib
    """
    pass

def RSA_verify_PKCS1_PSS(RSA, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int RSA_verify_PKCS1_PSS(RSA *, unsigned char *, EVP_MD *, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ACCESS_DESCRIPTION_free(Cryptography_STACK_OF_ACCESS_DESCRIPTION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void sk_ACCESS_DESCRIPTION_free(Cryptography_STACK_OF_ACCESS_DESCRIPTION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ACCESS_DESCRIPTION_new_null(): # real signature unknown; restored from __doc__
    """
    Cryptography_STACK_OF_ACCESS_DESCRIPTION *sk_ACCESS_DESCRIPTION_new_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ACCESS_DESCRIPTION_num(Cryptography_STACK_OF_ACCESS_DESCRIPTION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_ACCESS_DESCRIPTION_num(Cryptography_STACK_OF_ACCESS_DESCRIPTION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ACCESS_DESCRIPTION_push(Cryptography_STACK_OF_ACCESS_DESCRIPTION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_ACCESS_DESCRIPTION_push(Cryptography_STACK_OF_ACCESS_DESCRIPTION *, ACCESS_DESCRIPTION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ACCESS_DESCRIPTION_value(Cryptography_STACK_OF_ACCESS_DESCRIPTION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ACCESS_DESCRIPTION *sk_ACCESS_DESCRIPTION_value(Cryptography_STACK_OF_ACCESS_DESCRIPTION *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ASN1_INTEGER_free(Cryptography_STACK_OF_ASN1_INTEGER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void sk_ASN1_INTEGER_free(Cryptography_STACK_OF_ASN1_INTEGER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ASN1_INTEGER_new_null(): # real signature unknown; restored from __doc__
    """
    Cryptography_STACK_OF_ASN1_INTEGER *sk_ASN1_INTEGER_new_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ASN1_INTEGER_num(Cryptography_STACK_OF_ASN1_INTEGER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_ASN1_INTEGER_num(Cryptography_STACK_OF_ASN1_INTEGER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ASN1_INTEGER_push(Cryptography_STACK_OF_ASN1_INTEGER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_ASN1_INTEGER_push(Cryptography_STACK_OF_ASN1_INTEGER *, ASN1_INTEGER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ASN1_INTEGER_value(Cryptography_STACK_OF_ASN1_INTEGER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_INTEGER *sk_ASN1_INTEGER_value(Cryptography_STACK_OF_ASN1_INTEGER *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ASN1_OBJECT_free(Cryptography_STACK_OF_ASN1_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void sk_ASN1_OBJECT_free(Cryptography_STACK_OF_ASN1_OBJECT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ASN1_OBJECT_new_null(): # real signature unknown; restored from __doc__
    """
    Cryptography_STACK_OF_ASN1_OBJECT *sk_ASN1_OBJECT_new_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ASN1_OBJECT_num(Cryptography_STACK_OF_ASN1_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_ASN1_OBJECT_num(Cryptography_STACK_OF_ASN1_OBJECT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ASN1_OBJECT_push(Cryptography_STACK_OF_ASN1_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_ASN1_OBJECT_push(Cryptography_STACK_OF_ASN1_OBJECT *, ASN1_OBJECT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_ASN1_OBJECT_value(Cryptography_STACK_OF_ASN1_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_OBJECT *sk_ASN1_OBJECT_value(Cryptography_STACK_OF_ASN1_OBJECT *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_DIST_POINT_free(Cryptography_STACK_OF_DIST_POINT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void sk_DIST_POINT_free(Cryptography_STACK_OF_DIST_POINT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_DIST_POINT_new_null(): # real signature unknown; restored from __doc__
    """
    Cryptography_STACK_OF_DIST_POINT *sk_DIST_POINT_new_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_DIST_POINT_num(Cryptography_STACK_OF_DIST_POINT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_DIST_POINT_num(Cryptography_STACK_OF_DIST_POINT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_DIST_POINT_push(Cryptography_STACK_OF_DIST_POINT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_DIST_POINT_push(Cryptography_STACK_OF_DIST_POINT *, DIST_POINT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_DIST_POINT_value(Cryptography_STACK_OF_DIST_POINT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    DIST_POINT *sk_DIST_POINT_value(Cryptography_STACK_OF_DIST_POINT *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_GENERAL_NAME_num(struct_stack_st_GENERAL_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_GENERAL_NAME_num(struct stack_st_GENERAL_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_GENERAL_NAME_pop_free(struct_stack_st_GENERAL_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void sk_GENERAL_NAME_pop_free(struct stack_st_GENERAL_NAME *, void(*)(GENERAL_NAME *));
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_GENERAL_NAME_push(struct_stack_st_GENERAL_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_GENERAL_NAME_push(struct stack_st_GENERAL_NAME *, GENERAL_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_GENERAL_NAME_value(struct_stack_st_GENERAL_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    GENERAL_NAME *sk_GENERAL_NAME_value(struct stack_st_GENERAL_NAME *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_GENERAL_SUBTREE_free(Cryptography_STACK_OF_GENERAL_SUBTREE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void sk_GENERAL_SUBTREE_free(Cryptography_STACK_OF_GENERAL_SUBTREE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_GENERAL_SUBTREE_new_null(): # real signature unknown; restored from __doc__
    """
    Cryptography_STACK_OF_GENERAL_SUBTREE *sk_GENERAL_SUBTREE_new_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_GENERAL_SUBTREE_num(Cryptography_STACK_OF_GENERAL_SUBTREE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_GENERAL_SUBTREE_num(Cryptography_STACK_OF_GENERAL_SUBTREE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_GENERAL_SUBTREE_push(Cryptography_STACK_OF_GENERAL_SUBTREE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_GENERAL_SUBTREE_push(Cryptography_STACK_OF_GENERAL_SUBTREE *, GENERAL_SUBTREE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_GENERAL_SUBTREE_value(Cryptography_STACK_OF_GENERAL_SUBTREE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    GENERAL_SUBTREE *sk_GENERAL_SUBTREE_value(Cryptography_STACK_OF_GENERAL_SUBTREE *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_POLICYINFO_free(Cryptography_STACK_OF_POLICYINFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void sk_POLICYINFO_free(Cryptography_STACK_OF_POLICYINFO *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_POLICYINFO_new_null(): # real signature unknown; restored from __doc__
    """
    Cryptography_STACK_OF_POLICYINFO *sk_POLICYINFO_new_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_POLICYINFO_num(Cryptography_STACK_OF_POLICYINFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_POLICYINFO_num(Cryptography_STACK_OF_POLICYINFO *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_POLICYINFO_push(Cryptography_STACK_OF_POLICYINFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_POLICYINFO_push(Cryptography_STACK_OF_POLICYINFO *, POLICYINFO *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_POLICYINFO_value(Cryptography_STACK_OF_POLICYINFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    POLICYINFO *sk_POLICYINFO_value(Cryptography_STACK_OF_POLICYINFO *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_POLICYQUALINFO_free(Cryptography_STACK_OF_POLICYQUALINFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void sk_POLICYQUALINFO_free(Cryptography_STACK_OF_POLICYQUALINFO *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_POLICYQUALINFO_new_null(): # real signature unknown; restored from __doc__
    """
    Cryptography_STACK_OF_POLICYQUALINFO *sk_POLICYQUALINFO_new_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_POLICYQUALINFO_num(Cryptography_STACK_OF_POLICYQUALINFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_POLICYQUALINFO_num(Cryptography_STACK_OF_POLICYQUALINFO *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_POLICYQUALINFO_push(Cryptography_STACK_OF_POLICYQUALINFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_POLICYQUALINFO_push(Cryptography_STACK_OF_POLICYQUALINFO *, POLICYQUALINFO *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_POLICYQUALINFO_value(Cryptography_STACK_OF_POLICYQUALINFO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    POLICYQUALINFO *sk_POLICYQUALINFO_value(Cryptography_STACK_OF_POLICYQUALINFO *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_SSL_CIPHER_num(Cryptography_STACK_OF_SSL_CIPHER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_SSL_CIPHER_num(Cryptography_STACK_OF_SSL_CIPHER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_SSL_CIPHER_value(Cryptography_STACK_OF_SSL_CIPHER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    SSL_CIPHER *sk_SSL_CIPHER_value(Cryptography_STACK_OF_SSL_CIPHER *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_CRL_free(Cryptography_STACK_OF_X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void sk_X509_CRL_free(Cryptography_STACK_OF_X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_CRL_new_null(): # real signature unknown; restored from __doc__
    """
    Cryptography_STACK_OF_X509_CRL *sk_X509_CRL_new_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_CRL_num(Cryptography_STACK_OF_X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_CRL_num(Cryptography_STACK_OF_X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_CRL_push(Cryptography_STACK_OF_X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_CRL_push(Cryptography_STACK_OF_X509_CRL *, X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_CRL_value(Cryptography_STACK_OF_X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_CRL *sk_X509_CRL_value(Cryptography_STACK_OF_X509_CRL *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_EXTENSION_delete(X509_EXTENSIONS, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *sk_X509_EXTENSION_delete(X509_EXTENSIONS *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_EXTENSION_free(X509_EXTENSIONS, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void sk_X509_EXTENSION_free(X509_EXTENSIONS *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_EXTENSION_insert(X509_EXTENSIONS, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_EXTENSION_insert(X509_EXTENSIONS *, X509_EXTENSION *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_EXTENSION_new_null(): # real signature unknown; restored from __doc__
    """
    X509_EXTENSIONS *sk_X509_EXTENSION_new_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_EXTENSION_num(X509_EXTENSIONS, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_EXTENSION_num(X509_EXTENSIONS *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_EXTENSION_push(X509_EXTENSIONS, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_EXTENSION_push(X509_EXTENSIONS *, X509_EXTENSION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_EXTENSION_value(X509_EXTENSIONS, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *sk_X509_EXTENSION_value(X509_EXTENSIONS *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_free(Cryptography_STACK_OF_X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void sk_X509_free(Cryptography_STACK_OF_X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_NAME_ENTRY_dup(Cryptography_STACK_OF_X509_NAME_ENTRY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Cryptography_STACK_OF_X509_NAME_ENTRY *sk_X509_NAME_ENTRY_dup(Cryptography_STACK_OF_X509_NAME_ENTRY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_NAME_ENTRY_new_null(): # real signature unknown; restored from __doc__
    """
    Cryptography_STACK_OF_X509_NAME_ENTRY *sk_X509_NAME_ENTRY_new_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_NAME_ENTRY_num(Cryptography_STACK_OF_X509_NAME_ENTRY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_NAME_ENTRY_num(Cryptography_STACK_OF_X509_NAME_ENTRY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_NAME_ENTRY_push(Cryptography_STACK_OF_X509_NAME_ENTRY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_NAME_ENTRY_push(Cryptography_STACK_OF_X509_NAME_ENTRY *, X509_NAME_ENTRY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_NAME_ENTRY_value(Cryptography_STACK_OF_X509_NAME_ENTRY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_NAME_ENTRY *sk_X509_NAME_ENTRY_value(Cryptography_STACK_OF_X509_NAME_ENTRY *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_NAME_free(Cryptography_STACK_OF_X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void sk_X509_NAME_free(Cryptography_STACK_OF_X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_NAME_new_null(): # real signature unknown; restored from __doc__
    """
    Cryptography_STACK_OF_X509_NAME *sk_X509_NAME_new_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_NAME_num(Cryptography_STACK_OF_X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_NAME_num(Cryptography_STACK_OF_X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_NAME_push(Cryptography_STACK_OF_X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_NAME_push(Cryptography_STACK_OF_X509_NAME *, X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_NAME_value(Cryptography_STACK_OF_X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_NAME *sk_X509_NAME_value(Cryptography_STACK_OF_X509_NAME *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_new_null(): # real signature unknown; restored from __doc__
    """
    Cryptography_STACK_OF_X509 *sk_X509_new_null();
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_num(Cryptography_STACK_OF_X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_num(Cryptography_STACK_OF_X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_OBJECT_num(Cryptography_STACK_OF_X509_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_OBJECT_num(Cryptography_STACK_OF_X509_OBJECT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_OBJECT_value(Cryptography_STACK_OF_X509_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_OBJECT *sk_X509_OBJECT_value(Cryptography_STACK_OF_X509_OBJECT *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_push(Cryptography_STACK_OF_X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_push(Cryptography_STACK_OF_X509 *, X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_REVOKED_num(Cryptography_STACK_OF_X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int sk_X509_REVOKED_num(Cryptography_STACK_OF_X509_REVOKED *);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_REVOKED_value(Cryptography_STACK_OF_X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_REVOKED *sk_X509_REVOKED_value(Cryptography_STACK_OF_X509_REVOKED *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def sk_X509_value(Cryptography_STACK_OF_X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509 *sk_X509_value(Cryptography_STACK_OF_X509 *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SMIME_read_PKCS7(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    PKCS7 *SMIME_read_PKCS7(struct bio_st *, struct bio_st * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SMIME_write_PKCS7(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SMIME_write_PKCS7(struct bio_st *, PKCS7 *, struct bio_st *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSLeay(): # real signature unknown; restored from __doc__
    """
    unsigned long SSLeay();
    
    CFFI C function from _openssl.lib
    """
    return 0

def SSLeay_version(p_int): # real signature unknown; restored from __doc__
    """
    char *SSLeay_version(int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSLv23_client_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *SSLv23_client_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def SSLv23_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *SSLv23_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def SSLv23_server_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *SSLv23_server_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def SSLv3_client_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *SSLv3_client_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def SSLv3_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *SSLv3_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def SSLv3_server_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *SSLv3_server_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_check_private_key(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_check_private_key(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CIPHER_description(SSL_CIPHER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *SSL_CIPHER_description(SSL_CIPHER *, char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CIPHER_get_bits(SSL_CIPHER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CIPHER_get_bits(SSL_CIPHER *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CIPHER_get_name(SSL_CIPHER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *SSL_CIPHER_get_name(SSL_CIPHER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CIPHER_get_version(SSL_CIPHER, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *SSL_CIPHER_get_version(SSL_CIPHER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_COMP_get_name(COMP_METHOD, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *SSL_COMP_get_name(COMP_METHOD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_add_client_CA(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_add_client_CA(SSL_CTX *, X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_add_extra_chain_cert(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_CTX_add_extra_chain_cert(SSL_CTX *, X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_check_private_key(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_check_private_key(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_clear_options(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_CTX_clear_options(SSL_CTX *, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_free(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_free(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_get_cert_store(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_STORE *SSL_CTX_get_cert_store(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_get_ex_data(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void *SSL_CTX_get_ex_data(SSL_CTX *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_get_ex_new_index(long, void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_get_ex_new_index(long, void *, CRYPTO_EX_new *, CRYPTO_EX_dup *, CRYPTO_EX_free *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_get_info_callback(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void(*SSL_CTX_get_info_callback(SSL_CTX *))(SSL *, int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_get_mode(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_CTX_get_mode(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_get_options(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_CTX_get_options(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_get_session_cache_mode(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_CTX_get_session_cache_mode(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_get_ssl_method(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    SSL_METHOD *SSL_CTX_get_ssl_method(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_get_timeout(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_get_timeout(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_get_verify_callback(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int(*SSL_CTX_get_verify_callback(SSL_CTX *))(int, X509_STORE_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_get_verify_depth(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_get_verify_depth(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_get_verify_mode(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_get_verify_mode(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_load_verify_locations(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_load_verify_locations(SSL_CTX *, char *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_new(SSL_METHOD, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    SSL_CTX *SSL_CTX_new(SSL_METHOD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_sess_accept(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_sess_accept(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_sess_accept_good(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_sess_accept_good(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_sess_accept_renegotiate(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_sess_accept_renegotiate(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_sess_cache_full(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_sess_cache_full(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_sess_cb_hits(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_sess_cb_hits(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_sess_connect(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_sess_connect(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_sess_connect_good(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_sess_connect_good(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_sess_connect_renegotiate(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_sess_connect_renegotiate(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_sess_hits(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_sess_hits(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_sess_misses(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_sess_misses(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_sess_number(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_sess_number(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_sess_timeouts(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_sess_timeouts(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_alpn_protos(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_set_alpn_protos(SSL_CTX *, unsigned char *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_alpn_select_cb(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_alpn_select_cb(SSL_CTX *, int(*)(SSL *, unsigned char * *, unsigned char *, unsigned char *, unsigned int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_cert_cb(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_cert_cb(SSL_CTX *, int(*)(SSL *, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_cert_store(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_cert_store(SSL_CTX *, X509_STORE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_cert_verify_callback(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_cert_verify_callback(SSL_CTX *, int(*)(X509_STORE_CTX *, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_cipher_list(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_set_cipher_list(SSL_CTX *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_client_CA_list(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_client_CA_list(SSL_CTX *, Cryptography_STACK_OF_X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_client_cert_engine(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_set_client_cert_engine(SSL_CTX *, ENGINE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_default_passwd_cb(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_default_passwd_cb(SSL_CTX *, int(*)(char *, int, int, void *));
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_default_passwd_cb_userdata(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_default_passwd_cb_userdata(SSL_CTX *, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_default_verify_paths(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_set_default_verify_paths(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_ecdh_auto(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_set_ecdh_auto(SSL_CTX *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_ex_data(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_set_ex_data(SSL_CTX *, int, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_info_callback(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_info_callback(SSL_CTX *, void(*)(SSL *, int, int));
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_mode(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_CTX_set_mode(SSL_CTX *, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_next_protos_advertised_cb(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_next_protos_advertised_cb(SSL_CTX *, int(*)(SSL *, unsigned char * *, unsigned int *, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_next_proto_select_cb(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_next_proto_select_cb(SSL_CTX *, int(*)(SSL *, unsigned char * *, unsigned char *, unsigned char *, unsigned int, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_options(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_CTX_set_options(SSL_CTX *, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_session_cache_mode(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_CTX_set_session_cache_mode(SSL_CTX *, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_session_id_context(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_set_session_id_context(SSL_CTX *, unsigned char *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_timeout(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_set_timeout(SSL_CTX *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_tlsext_servername_arg(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_tlsext_servername_arg(SSL_CTX *, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_tlsext_servername_callback(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_tlsext_servername_callback(SSL_CTX *, int(*)(SSL *, int *, void *));
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_tlsext_status_arg(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_set_tlsext_status_arg(SSL_CTX *, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_tlsext_status_cb(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_CTX_set_tlsext_status_cb(SSL_CTX *, int(*)(SSL *, void *));
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_tmp_dh(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_CTX_set_tmp_dh(SSL_CTX *, DH *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_tmp_ecdh(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_CTX_set_tmp_ecdh(SSL_CTX *, EC_KEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_verify(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_verify(SSL_CTX *, int, int(*)(int, X509_STORE_CTX *));
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_set_verify_depth(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_CTX_set_verify_depth(SSL_CTX *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_use_certificate(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_use_certificate(SSL_CTX *, X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_use_certificate_ASN1(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_use_certificate_ASN1(SSL_CTX *, int, unsigned char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_use_certificate_chain_file(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_use_certificate_chain_file(SSL_CTX *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_use_certificate_file(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_use_certificate_file(SSL_CTX *, char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_use_PrivateKey(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_use_PrivateKey(SSL_CTX *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_use_PrivateKey_ASN1(p_int, SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_use_PrivateKey_ASN1(int, SSL_CTX *, unsigned char *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_CTX_use_PrivateKey_file(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_CTX_use_PrivateKey_file(SSL_CTX *, char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_do_handshake(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_do_handshake(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_free(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_free(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get0_alpn_selected(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_get0_alpn_selected(SSL *, unsigned char * *, unsigned int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get0_next_proto_negotiated(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_get0_next_proto_negotiated(SSL *, unsigned char * *, unsigned int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get1_session(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    SSL_SESSION *SSL_get1_session(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_app_data(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *SSL_get_app_data(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_ciphers(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Cryptography_STACK_OF_SSL_CIPHER *SSL_get_ciphers(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_cipher_list(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *SSL_get_cipher_list(SSL *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_client_CA_list(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Cryptography_STACK_OF_X509_NAME *SSL_get_client_CA_list(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_client_random(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    size_t SSL_get_client_random(SSL *, unsigned char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_current_cipher(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    SSL_CIPHER *SSL_get_current_cipher(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_current_compression(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    COMP_METHOD *SSL_get_current_compression(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_current_expansion(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    COMP_METHOD *SSL_get_current_expansion(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_error(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_get_error(SSL *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_ex_data(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void *SSL_get_ex_data(SSL *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_ex_data_X509_STORE_CTX_idx(): # real signature unknown; restored from __doc__
    """
    int SSL_get_ex_data_X509_STORE_CTX_idx();
    
    CFFI C function from _openssl.lib
    """
    return 0

def SSL_get_ex_new_index(long, void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_get_ex_new_index(long, void *, CRYPTO_EX_new *, CRYPTO_EX_dup *, CRYPTO_EX_free *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_finished(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    size_t SSL_get_finished(SSL *, void *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_info_callback(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void(*SSL_get_info_callback(SSL *))(SSL *, int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_mode(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_get_mode(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_options(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_get_options(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_peer_certificate(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509 *SSL_get_peer_certificate(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_peer_cert_chain(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Cryptography_STACK_OF_X509 *SSL_get_peer_cert_chain(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_peer_finished(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    size_t SSL_get_peer_finished(SSL *, void *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_rbio(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct bio_st *SSL_get_rbio(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_secure_renegotiation_support(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_get_secure_renegotiation_support(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_servername(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *SSL_get_servername(SSL *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_server_random(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    size_t SSL_get_server_random(SSL *, unsigned char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_server_tmp_key(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_get_server_tmp_key(SSL *, EVP_PKEY * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_session(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    SSL_SESSION *SSL_get_session(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_shutdown(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_get_shutdown(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_SSL_CTX(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    SSL_CTX *SSL_get_SSL_CTX(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_tlsext_status_ocsp_resp(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_get_tlsext_status_ocsp_resp(SSL *, unsigned char * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_verify_callback(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int(*SSL_get_verify_callback(SSL *))(int, X509_STORE_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_verify_depth(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_get_verify_depth(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_verify_mode(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_get_verify_mode(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_version(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *SSL_get_version(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_get_wbio(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct bio_st *SSL_get_wbio(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_library_init(): # real signature unknown; restored from __doc__
    """
    int SSL_library_init();
    
    CFFI C function from _openssl.lib
    """
    return 0

def SSL_load_client_CA_file(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Cryptography_STACK_OF_X509_NAME *SSL_load_client_CA_file(char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_load_error_strings(): # real signature unknown; restored from __doc__
    """
    void SSL_load_error_strings();
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_new(SSL_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    SSL *SSL_new(SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_peek(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_peek(SSL *, void *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_pending(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_pending(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_read(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_read(SSL *, void *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_renegotiate(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_renegotiate(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_renegotiate_pending(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_renegotiate_pending(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_select_next_proto(unsigned_char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_select_next_proto(unsigned char * *, unsigned char *, unsigned char *, unsigned int, unsigned char *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_SESSION_free(SSL_SESSION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_SESSION_free(SSL_SESSION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_SESSION_get_id(SSL_SESSION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned char *SSL_SESSION_get_id(SSL_SESSION *, unsigned int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_SESSION_get_master_key(SSL_SESSION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    size_t SSL_SESSION_get_master_key(SSL_SESSION *, unsigned char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_SESSION_print(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_SESSION_print(struct bio_st *, SSL_SESSION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_session_reused(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_session_reused(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_SESSION_set1_id_context(SSL_SESSION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_SESSION_set1_id_context(SSL_SESSION *, unsigned char *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_accept_state(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_set_accept_state(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_alpn_protos(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_set_alpn_protos(SSL *, unsigned char *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_app_data(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_set_app_data(SSL *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_bio(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_set_bio(SSL *, struct bio_st *, struct bio_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_cert_cb(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_set_cert_cb(SSL *, int(*)(SSL *, void *), void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_connect_state(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_set_connect_state(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_ex_data(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_set_ex_data(SSL *, int, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_fd(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_set_fd(SSL *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_info_callback(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_set_info_callback(SSL *, void(*)(SSL *, int, int));
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_mode(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_set_mode(SSL *, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_options(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long SSL_set_options(SSL *, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_read_ahead(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_set_read_ahead(SSL *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_session(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_set_session(SSL *, SSL_SESSION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_shutdown(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_set_shutdown(SSL *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_SSL_CTX(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    SSL_CTX *SSL_set_SSL_CTX(SSL *, SSL_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_tlsext_host_name(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_set_tlsext_host_name(SSL *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_tlsext_status_ocsp_resp(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_set_tlsext_status_ocsp_resp(SSL *, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_tlsext_status_type(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_set_tlsext_status_type(SSL *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_verify(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_set_verify(SSL *, int, int(*)(int, X509_STORE_CTX *));
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_set_verify_depth(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void SSL_set_verify_depth(SSL *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_shutdown(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_shutdown(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_state_string_long(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *SSL_state_string_long(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_total_renegotiations(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long SSL_total_renegotiations(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_use_certificate(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_use_certificate(SSL *, X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_use_certificate_ASN1(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_use_certificate_ASN1(SSL *, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_use_certificate_file(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_use_certificate_file(SSL *, char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_use_PrivateKey(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_use_PrivateKey(SSL *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_use_PrivateKey_ASN1(p_int, SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_use_PrivateKey_ASN1(int, SSL *, unsigned char *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_use_PrivateKey_file(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_use_PrivateKey_file(SSL *, char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_version(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_version(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_want_read(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_want_read(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_want_write(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_want_write(SSL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def SSL_write(SSL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int SSL_write(SSL *, void *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def TLSv1_1_client_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *TLSv1_1_client_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def TLSv1_1_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *TLSv1_1_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def TLSv1_1_server_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *TLSv1_1_server_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def TLSv1_2_client_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *TLSv1_2_client_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def TLSv1_2_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *TLSv1_2_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def TLSv1_2_server_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *TLSv1_2_server_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def TLSv1_client_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *TLSv1_client_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def TLSv1_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *TLSv1_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def TLSv1_server_method(): # real signature unknown; restored from __doc__
    """
    SSL_METHOD *TLSv1_server_method();
    
    CFFI C function from _openssl.lib
    """
    pass

def USERNOTICE_free(USERNOTICE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void USERNOTICE_free(USERNOTICE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def USERNOTICE_new(): # real signature unknown; restored from __doc__
    """
    USERNOTICE *USERNOTICE_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509V3_EXT_add_alias(p_int, p_int_1): # real signature unknown; restored from __doc__
    """
    int X509V3_EXT_add_alias(int, int);
    
    CFFI C function from _openssl.lib
    """
    return 0

def X509V3_EXT_conf_nid(Cryptography_LHASH_OF_CONF_VALUE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *X509V3_EXT_conf_nid(Cryptography_LHASH_OF_CONF_VALUE *, X509V3_CTX *, int, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509V3_EXT_d2i(X509_EXTENSION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void *X509V3_EXT_d2i(X509_EXTENSION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509V3_EXT_get(X509_EXTENSION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509V3_EXT_METHOD *X509V3_EXT_get(X509_EXTENSION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509V3_EXT_get_nid(p_int): # real signature unknown; restored from __doc__
    """
    X509V3_EXT_METHOD *X509V3_EXT_get_nid(int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509V3_EXT_i2d(p_int, p_int_1, void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *X509V3_EXT_i2d(int, int, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509V3_EXT_nconf(CONF, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *X509V3_EXT_nconf(CONF *, X509V3_CTX *, char *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509V3_EXT_print(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509V3_EXT_print(struct bio_st *, X509_EXTENSION *, unsigned long, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509V3_set_ctx(X509V3_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509V3_set_ctx(X509V3_CTX *, X509 *, X509 *, X509_REQ *, X509_CRL *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509V3_set_ctx_nodb(X509V3_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void *X509V3_set_ctx_nodb(X509V3_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_add_ext(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_add_ext(X509 *, X509_EXTENSION *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_alias_get0(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned char *X509_alias_get0(X509 *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_check_ca(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_check_ca(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_cmp(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_cmp(X509 *, X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_add0_revoked(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_add0_revoked(X509_CRL *, X509_REVOKED *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_add_ext(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_add_ext(X509_CRL *, X509_EXTENSION *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_cmp(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_cmp(X509_CRL *, X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_free(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_CRL_free(X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_get0_signature(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_CRL_get0_signature(X509_CRL *, struct asn1_string_st * *, X509_ALGOR * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_get_ext(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *X509_CRL_get_ext(X509_CRL *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_get_ext_count(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_get_ext_count(X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_get_issuer(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_NAME *X509_CRL_get_issuer(X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_get_lastUpdate(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct asn1_string_st *X509_CRL_get_lastUpdate(X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_get_nextUpdate(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct asn1_string_st *X509_CRL_get_nextUpdate(X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_get_REVOKED(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Cryptography_STACK_OF_X509_REVOKED *X509_CRL_get_REVOKED(X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_get_version(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_get_version(X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_new(): # real signature unknown; restored from __doc__
    """
    X509_CRL *X509_CRL_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_print(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_print(struct bio_st *, X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_set_issuer_name(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_set_issuer_name(X509_CRL *, X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_set_lastUpdate(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_set_lastUpdate(X509_CRL *, struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_set_nextUpdate(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_set_nextUpdate(X509_CRL *, struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_set_version(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_set_version(X509_CRL *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_sign(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_sign(X509_CRL *, EVP_PKEY *, EVP_MD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_sort(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_sort(X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_CRL_verify(X509_CRL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_CRL_verify(X509_CRL *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_delete_ext(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *X509_delete_ext(X509 *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_digest(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_digest(X509 *, EVP_MD *, unsigned char *, unsigned int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_dup(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509 *X509_dup(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_EXTENSION_create_by_OBJ(X509_EXTENSION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *X509_EXTENSION_create_by_OBJ(X509_EXTENSION * *, ASN1_OBJECT *, int, struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_EXTENSION_dup(X509_EXTENSION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *X509_EXTENSION_dup(X509_EXTENSION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_EXTENSION_free(X509_EXTENSION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_EXTENSION_free(X509_EXTENSION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_EXTENSION_get_critical(X509_EXTENSION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_EXTENSION_get_critical(X509_EXTENSION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_EXTENSION_get_data(X509_EXTENSION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct asn1_string_st *X509_EXTENSION_get_data(X509_EXTENSION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_EXTENSION_get_object(X509_EXTENSION, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_OBJECT *X509_EXTENSION_get_object(X509_EXTENSION *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_free(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_free(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get0_signature(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_get0_signature(struct asn1_string_st * *, X509_ALGOR * *, X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get0_tbs_sigalg(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_ALGOR *X509_get0_tbs_sigalg(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_default_cert_area(): # real signature unknown; restored from __doc__
    """
    char *X509_get_default_cert_area();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_default_cert_dir(): # real signature unknown; restored from __doc__
    """
    char *X509_get_default_cert_dir();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_default_cert_dir_env(): # real signature unknown; restored from __doc__
    """
    char *X509_get_default_cert_dir_env();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_default_cert_file(): # real signature unknown; restored from __doc__
    """
    char *X509_get_default_cert_file();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_default_cert_file_env(): # real signature unknown; restored from __doc__
    """
    char *X509_get_default_cert_file_env();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_default_private_dir(): # real signature unknown; restored from __doc__
    """
    char *X509_get_default_private_dir();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_ext(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *X509_get_ext(X509 *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_ext_by_NID(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_get_ext_by_NID(X509 *, int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_ext_count(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_get_ext_count(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_ext_d2i(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void *X509_get_ext_d2i(X509 *, int, int *, int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_ex_data(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void *X509_get_ex_data(X509 *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_ex_new_index(long, void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_get_ex_new_index(long, void *, CRYPTO_EX_new *, CRYPTO_EX_dup *, CRYPTO_EX_free *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_issuer_name(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_NAME *X509_get_issuer_name(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_notAfter(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct asn1_string_st *X509_get_notAfter(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_notBefore(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct asn1_string_st *X509_get_notBefore(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_pubkey(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY *X509_get_pubkey(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_serialNumber(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_INTEGER *X509_get_serialNumber(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_signature_nid(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_get_signature_nid(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_subject_name(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_NAME *X509_get_subject_name(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_get_version(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long X509_get_version(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_gmtime_adj(struct_asn1_string_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct asn1_string_st *X509_gmtime_adj(struct asn1_string_st *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_add_entry(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_NAME_add_entry(X509_NAME *, X509_NAME_ENTRY *, int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_add_entry_by_NID(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_NAME_add_entry_by_NID(X509_NAME *, int, int, unsigned char *, int, int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_add_entry_by_OBJ(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_NAME_add_entry_by_OBJ(X509_NAME *, ASN1_OBJECT *, int, unsigned char *, int, int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_add_entry_by_txt(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_NAME_add_entry_by_txt(X509_NAME *, char *, int, unsigned char *, int, int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_cmp(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_NAME_cmp(X509_NAME *, X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_delete_entry(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_NAME_ENTRY *X509_NAME_delete_entry(X509_NAME *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_dup(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_NAME *X509_NAME_dup(X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_entry_count(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_NAME_entry_count(X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_ENTRY_create_by_OBJ(X509_NAME_ENTRY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_NAME_ENTRY *X509_NAME_ENTRY_create_by_OBJ(X509_NAME_ENTRY * *, ASN1_OBJECT *, int, unsigned char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_ENTRY_free(X509_NAME_ENTRY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_NAME_ENTRY_free(X509_NAME_ENTRY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_ENTRY_get_data(X509_NAME_ENTRY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct asn1_string_st *X509_NAME_ENTRY_get_data(X509_NAME_ENTRY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_ENTRY_get_object(X509_NAME_ENTRY, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_OBJECT *X509_NAME_ENTRY_get_object(X509_NAME_ENTRY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_free(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_NAME_free(X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_get_entry(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_NAME_ENTRY *X509_NAME_get_entry(X509_NAME *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_get_index_by_NID(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_NAME_get_index_by_NID(X509_NAME *, int, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_hash(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long X509_NAME_hash(X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_new(): # real signature unknown; restored from __doc__
    """
    X509_NAME *X509_NAME_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_NAME_oneline(X509_NAME, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    char *X509_NAME_oneline(X509_NAME *, char *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_new(): # real signature unknown; restored from __doc__
    """
    X509 *X509_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_OBJECT_get0_X509(X509_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509 *X509_OBJECT_get0_X509(X509_OBJECT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_OBJECT_get_type(X509_OBJECT, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_OBJECT_get_type(X509_OBJECT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_print_ex(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_print_ex(struct bio_st *, X509 *, unsigned long, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_add_extensions(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REQ_add_extensions(X509_REQ *, X509_EXTENSIONS *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_digest(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REQ_digest(X509_REQ *, EVP_MD *, unsigned char *, unsigned int *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_free(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_REQ_free(X509_REQ *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_get0_signature(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_REQ_get0_signature(X509_REQ *, struct asn1_string_st * *, X509_ALGOR * *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_get_extensions(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSIONS *X509_REQ_get_extensions(X509_REQ *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_get_pubkey(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    EVP_PKEY *X509_REQ_get_pubkey(X509_REQ *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_get_subject_name(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_NAME *X509_REQ_get_subject_name(X509_REQ *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_get_version(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    long X509_REQ_get_version(X509_REQ *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_new(): # real signature unknown; restored from __doc__
    """
    X509_REQ *X509_REQ_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_print(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REQ_print(struct bio_st *, X509_REQ *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_print_ex(struct_bio_st, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REQ_print_ex(struct bio_st *, X509_REQ *, unsigned long, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_set_pubkey(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REQ_set_pubkey(X509_REQ *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_set_subject_name(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REQ_set_subject_name(X509_REQ *, X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_set_version(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REQ_set_version(X509_REQ *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_sign(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REQ_sign(X509_REQ *, EVP_PKEY *, EVP_MD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REQ_verify(X509_REQ, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REQ_verify(X509_REQ *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REVOKED_add1_ext_i2d(X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REVOKED_add1_ext_i2d(X509_REVOKED *, int, void *, int, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REVOKED_add_ext(X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REVOKED_add_ext(X509_REVOKED *, X509_EXTENSION *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REVOKED_delete_ext(X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *X509_REVOKED_delete_ext(X509_REVOKED *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REVOKED_free(X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_REVOKED_free(X509_REVOKED *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REVOKED_get0_revocationDate(X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    struct asn1_string_st *X509_REVOKED_get0_revocationDate(X509_REVOKED *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REVOKED_get0_serialNumber(X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ASN1_INTEGER *X509_REVOKED_get0_serialNumber(X509_REVOKED *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REVOKED_get_ext(X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_EXTENSION *X509_REVOKED_get_ext(X509_REVOKED *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REVOKED_get_ext_count(X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REVOKED_get_ext_count(X509_REVOKED *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REVOKED_new(): # real signature unknown; restored from __doc__
    """
    X509_REVOKED *X509_REVOKED_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REVOKED_set_revocationDate(X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REVOKED_set_revocationDate(X509_REVOKED *, struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_REVOKED_set_serialNumber(X509_REVOKED, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_REVOKED_set_serialNumber(X509_REVOKED *, ASN1_INTEGER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_set_ex_data(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_set_ex_data(X509 *, int, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_set_issuer_name(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_set_issuer_name(X509 *, X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_set_notAfter(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_set_notAfter(X509 *, struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_set_notBefore(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_set_notBefore(X509 *, struct asn1_string_st *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_set_pubkey(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_set_pubkey(X509 *, EVP_PKEY *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_set_serialNumber(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_set_serialNumber(X509 *, ASN1_INTEGER *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_set_subject_name(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_set_subject_name(X509 *, X509_NAME *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_set_version(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_set_version(X509 *, long);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_sign(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_sign(X509 *, EVP_PKEY *, EVP_MD *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_add_cert(X509_STORE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_STORE_add_cert(X509_STORE *, X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_add_crl(X509_STORE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_STORE_add_crl(X509_STORE *, X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_cleanup(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_STORE_CTX_cleanup(X509_STORE_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_free(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_STORE_CTX_free(X509_STORE_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_get0_param(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_VERIFY_PARAM *X509_STORE_CTX_get0_param(X509_STORE_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_get1_chain(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Cryptography_STACK_OF_X509 *X509_STORE_CTX_get1_chain(X509_STORE_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_get_chain(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Cryptography_STACK_OF_X509 *X509_STORE_CTX_get_chain(X509_STORE_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_get_current_cert(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509 *X509_STORE_CTX_get_current_cert(X509_STORE_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_get_error(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_STORE_CTX_get_error(X509_STORE_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_get_error_depth(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_STORE_CTX_get_error_depth(X509_STORE_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_get_ex_data(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void *X509_STORE_CTX_get_ex_data(X509_STORE_CTX *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_get_ex_new_index(long, void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_STORE_CTX_get_ex_new_index(long, void *, CRYPTO_EX_new *, CRYPTO_EX_dup *, CRYPTO_EX_free *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_init(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_STORE_CTX_init(X509_STORE_CTX *, X509_STORE *, X509 *, Cryptography_STACK_OF_X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_new(): # real signature unknown; restored from __doc__
    """
    X509_STORE_CTX *X509_STORE_CTX_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_set0_crls(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_STORE_CTX_set0_crls(X509_STORE_CTX *, Cryptography_STACK_OF_X509_CRL *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_set0_param(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_STORE_CTX_set0_param(X509_STORE_CTX *, X509_VERIFY_PARAM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_set_cert(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_STORE_CTX_set_cert(X509_STORE_CTX *, X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_set_chain(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_STORE_CTX_set_chain(X509_STORE_CTX *, Cryptography_STACK_OF_X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_set_default(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_STORE_CTX_set_default(X509_STORE_CTX *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_set_error(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_STORE_CTX_set_error(X509_STORE_CTX *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_set_ex_data(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_STORE_CTX_set_ex_data(X509_STORE_CTX *, int, void *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_set_verify_cb(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_STORE_CTX_set_verify_cb(X509_STORE_CTX *, int(*)(int, X509_STORE_CTX *));
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_CTX_trusted_stack(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_STORE_CTX_trusted_stack(X509_STORE_CTX *, Cryptography_STACK_OF_X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_free(X509_STORE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_STORE_free(X509_STORE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_get0_objects(X509_STORE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Cryptography_STACK_OF_X509_OBJECT *X509_STORE_get0_objects(X509_STORE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_get0_param(X509_STORE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    X509_VERIFY_PARAM *X509_STORE_get0_param(X509_STORE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_load_locations(X509_STORE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_STORE_load_locations(X509_STORE *, char *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_new(): # real signature unknown; restored from __doc__
    """
    X509_STORE *X509_STORE_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_set1_param(X509_STORE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_STORE_set1_param(X509_STORE *, X509_VERIFY_PARAM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_set_default_paths(X509_STORE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_STORE_set_default_paths(X509_STORE *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_STORE_set_flags(X509_STORE, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_STORE_set_flags(X509_STORE *, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_subject_name_hash(X509, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long X509_subject_name_hash(X509 *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_verify_cert(X509_STORE_CTX, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_verify_cert(X509_STORE_CTX *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_verify_cert_error_string(long): # real signature unknown; restored from __doc__
    """
    char *X509_verify_cert_error_string(long);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_add0_policy(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_VERIFY_PARAM_add0_policy(X509_VERIFY_PARAM *, ASN1_OBJECT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_clear_flags(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_VERIFY_PARAM_clear_flags(X509_VERIFY_PARAM *, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_free(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_VERIFY_PARAM_free(X509_VERIFY_PARAM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_get_depth(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_VERIFY_PARAM_get_depth(X509_VERIFY_PARAM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_get_flags(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned long X509_VERIFY_PARAM_get_flags(X509_VERIFY_PARAM *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_new(): # real signature unknown; restored from __doc__
    """
    X509_VERIFY_PARAM *X509_VERIFY_PARAM_new();
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_set1_email(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_VERIFY_PARAM_set1_email(X509_VERIFY_PARAM *, char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_set1_host(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_VERIFY_PARAM_set1_host(X509_VERIFY_PARAM *, char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_set1_ip(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_VERIFY_PARAM_set1_ip(X509_VERIFY_PARAM *, unsigned char *, size_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_set1_ip_asc(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_VERIFY_PARAM_set1_ip_asc(X509_VERIFY_PARAM *, char *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_set1_policies(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_VERIFY_PARAM_set1_policies(X509_VERIFY_PARAM *, Cryptography_STACK_OF_ASN1_OBJECT *);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_set_depth(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_VERIFY_PARAM_set_depth(X509_VERIFY_PARAM *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_set_flags(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_VERIFY_PARAM_set_flags(X509_VERIFY_PARAM *, unsigned long);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_set_hostflags(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_VERIFY_PARAM_set_hostflags(X509_VERIFY_PARAM *, unsigned int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_set_purpose(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_VERIFY_PARAM_set_purpose(X509_VERIFY_PARAM *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_set_time(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void X509_VERIFY_PARAM_set_time(X509_VERIFY_PARAM *, int64_t);
    
    CFFI C function from _openssl.lib
    """
    pass

def X509_VERIFY_PARAM_set_trust(X509_VERIFY_PARAM, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int X509_VERIFY_PARAM_set_trust(X509_VERIFY_PARAM *, int);
    
    CFFI C function from _openssl.lib
    """
    pass

def _setup_ssl_threads(): # real signature unknown; restored from __doc__
    """
    int _setup_ssl_threads();
    
    CFFI C function from _openssl.lib
    """
    return 0

# no classes
