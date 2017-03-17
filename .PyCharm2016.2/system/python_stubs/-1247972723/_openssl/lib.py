# encoding: utf-8
# module _openssl.lib calls itself <Lib object for '_openssl'>
# from /usr/lib/python2.7/dist-packages/cryptography/hazmat/bindings/_openssl.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
from _cffi_backend import (Cryptography_locking_cb, 
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

ASN1_F_ASN1_ENUMERATED_TO_BN = 113

ASN1_F_ASN1_EX_C2I = 204

ASN1_F_ASN1_FIND_END = 190

ASN1_F_ASN1_GENERALIZEDTIME_SET = 185

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

ASN1_F_ASN1_TIME_SET = 175

ASN1_F_ASN1_TYPE_GET_INT_OCTETSTRING = 134

ASN1_F_ASN1_TYPE_GET_OCTETSTRING = 135

ASN1_F_ASN1_UNPACK_STRING = 136

ASN1_F_ASN1_UTCTIME_SET = 187

ASN1_F_ASN1_VERIFY = 137

ASN1_F_B64_READ_ASN1 = 209

ASN1_F_B64_WRITE_ASN1 = 210

ASN1_F_BITSTR_CB = 180

ASN1_F_BN_TO_ASN1_ENUMERATED = 138
ASN1_F_BN_TO_ASN1_INTEGER = 139

ASN1_F_D2I_ASN1_TYPE_BYTES = 149

ASN1_F_D2I_ASN1_UINTEGER = 150
ASN1_F_D2I_ASN1_UTCTIME = 151

ASN1_F_D2I_NETSCAPE_RSA = 152

ASN1_F_D2I_NETSCAPE_RSA_2 = 153

ASN1_F_D2I_PRIVATEKEY = 154
ASN1_F_D2I_X509 = 156

ASN1_F_D2I_X509_CINF = 157
ASN1_F_D2I_X509_PKEY = 159

ASN1_F_I2D_ASN1_SET = 188
ASN1_F_I2D_ASN1_TIME = 160

ASN1_F_I2D_DSA_PUBKEY = 161

ASN1_F_LONG_C2I = 166

ASN1_F_OID_MODULE_INIT = 174

ASN1_F_PARSE_TAGGING = 182

ASN1_F_PKCS5_PBE_SET = 202

ASN1_F_SMIME_READ_ASN1 = 212

ASN1_F_SMIME_TEXT = 213

ASN1_F_X509_CINF_NEW = 168

ASN1_R_BOOLEAN_IS_WRONG_LENGTH = 106

ASN1_R_BUFFER_TOO_SMALL = 107

ASN1_R_CIPHER_HAS_NO_OBJECT_IDENTIFIER = 108

ASN1_R_DATA_IS_WRONG = 109

ASN1_R_DECODE_ERROR = 110

ASN1_R_DECODING_ERROR = 111

ASN1_R_DEPTH_EXCEEDED = 174

ASN1_R_ENCODE_ERROR = 112

ASN1_R_ERROR_GETTING_TIME = 173

ASN1_R_ERROR_LOADING_SECTION = 172

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

ASN1_R_UNKOWN_FORMAT = 195

ASN1_R_UNSUPPORTED_ANY_DEFINED_BY_TYPE = 164

ASN1_R_UNSUPPORTED_ENCRYPTION_ALGORITHM = 166

ASN1_R_UNSUPPORTED_PUBLIC_KEY_TYPE = 167

ASN1_R_UNSUPPORTED_TYPE = 196

ASN1_R_WRONG_TAG = 168
ASN1_R_WRONG_TYPE = 169

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
BIO_TYPE_BER = 530
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

BIO_TYPE_PROXY_CLIENT = 526
BIO_TYPE_PROXY_SERVER = 527

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

Cryptography_HAS_098C_CAMELLIA_CODES = 1

Cryptography_HAS_098H_ERROR_CODES = 1

Cryptography_HAS_100_VERIFICATION_ERROR_CODES = 1

Cryptography_HAS_100_VERIFICATION_PARAMS = 1

Cryptography_HAS_102_VERIFICATION_ERROR_CODES = 1

Cryptography_HAS_102_VERIFICATION_PARAMS = 1

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

Cryptography_HAS_ECDSA_SHA2_NIDS = 1

Cryptography_HAS_EC_1_0_1 = 1
Cryptography_HAS_EC_1_0_2 = 1

Cryptography_HAS_EC_CODES = 1

Cryptography_HAS_EGD = 1

Cryptography_HAS_ENGINE_CRYPTODEV = 1

Cryptography_HAS_GCM = 1

Cryptography_HAS_GET_SERVER_TMP_KEY = 1

Cryptography_HAS_MGF1_MD = 1

Cryptography_HAS_NETBSD_D1_METH = 1

Cryptography_HAS_NEXTPROTONEG = 1

Cryptography_HAS_OP_NO_COMPRESSION = 1

Cryptography_HAS_PBKDF2_HMAC = 1

Cryptography_HAS_PKEY_CTX = 1

Cryptography_HAS_PSS_PADDING = 1

Cryptography_HAS_RELEASE_BUFFERS = 1

Cryptography_HAS_REMOVE_THREAD_STATE = 1

Cryptography_HAS_RSA_R_PKCS_DECODING_ERROR = 1

Cryptography_HAS_SECURE_RENEGOTIATION = 1

Cryptography_HAS_SET_CERT_CB = 1

Cryptography_HAS_SSL2 = 0

Cryptography_HAS_SSL3_METHOD = 1

Cryptography_HAS_SSL_CTX_SET_CLIENT_CERT_ENGINE = 1

Cryptography_HAS_SSL_OP_MSIE_SSLV2_RSA_PADDING = 1

Cryptography_HAS_SSL_OP_NO_TICKET = 1

Cryptography_HAS_SSL_SET_SSL_CTX = 1

Cryptography_HAS_STATUS_REQ_OCSP_RESP = 1

Cryptography_HAS_TLSEXT_HOSTNAME = 1

Cryptography_HAS_TLSEXT_STATUS_REQ_CB = 1
Cryptography_HAS_TLSEXT_STATUS_REQ_TYPE = 1

Cryptography_HAS_TLSv1_1 = 1
Cryptography_HAS_TLSv1_2 = 1

Cryptography_HAS_X509_V_FLAG_CHECK_SS_SIGNATURE = 1

Cryptography_HAS_X509_V_FLAG_PARTIAL_CHAIN = 1

Cryptography_HAS_X509_V_FLAG_TRUSTED_FIRST = 1

Cryptography_STATIC_CALLBACKS = 1

CRYPTO_LOCK = 1

CRYPTO_LOCK_SSL = 16

CRYPTO_MEM_CHECK_DISABLE = 3
CRYPTO_MEM_CHECK_ENABLE = 2
CRYPTO_MEM_CHECK_OFF = 0
CRYPTO_MEM_CHECK_ON = 1

CRYPTO_READ = 4
CRYPTO_UNLOCK = 2
CRYPTO_WRITE = 8

DH_F_COMPUTE_KEY = 102

DH_R_INVALID_PUBKEY = 102

EC_F_EC_GROUP_NEW_BY_CURVE_NAME = 174

EC_R_UNKNOWN_GROUP = 129

ENGINE_METHOD_ALL = 65535
ENGINE_METHOD_CIPHERS = 64
ENGINE_METHOD_DIGESTS = 128
ENGINE_METHOD_DSA = 2
ENGINE_METHOD_ECDH = 16
ENGINE_METHOD_ECDSA = 32
ENGINE_METHOD_NONE = 0
ENGINE_METHOD_RAND = 8
ENGINE_METHOD_RSA = 1
ENGINE_METHOD_STORE = 256

ENGINE_R_CONFLICTING_ENGINE_ID = 103

ERR_LIB_ASN1 = 13
ERR_LIB_DH = 5
ERR_LIB_EC = 16
ERR_LIB_EVP = 6
ERR_LIB_PEM = 9
ERR_LIB_PKCS12 = 35
ERR_LIB_RSA = 4

EVP_CTRL_GCM_GET_TAG = 16

EVP_CTRL_GCM_SET_IVLEN = 9
EVP_CTRL_GCM_SET_TAG = 17

EVP_F_AES_INIT_KEY = 133

EVP_F_CAMELLIA_INIT_KEY = 159

EVP_F_D2I_PKEY = 100

EVP_F_DSAPKEY2PKCS8 = 134

EVP_F_DSA_PKEY2PKCS8 = 135

EVP_F_ECDSA_PKEY2PKCS8 = 129

EVP_F_ECKEY_PKEY2PKCS8 = 132

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

EVP_F_EVP_PKEY2PKCS8_BROKEN = 113

EVP_F_EVP_PKEY_COPY_PARAMETERS = 103

EVP_F_EVP_PKEY_DECRYPT = 104
EVP_F_EVP_PKEY_ENCRYPT = 105

EVP_F_EVP_PKEY_GET1_DH = 119
EVP_F_EVP_PKEY_GET1_DSA = 120
EVP_F_EVP_PKEY_GET1_ECDSA = 130

EVP_F_EVP_PKEY_GET1_EC_KEY = 131

EVP_F_EVP_PKEY_GET1_RSA = 121

EVP_F_EVP_PKEY_NEW = 106

EVP_F_EVP_RIJNDAEL = 126
EVP_F_EVP_SIGNFINAL = 107
EVP_F_EVP_VERIFYFINAL = 108

EVP_F_PKCS5_PBE_KEYIVGEN = 117

EVP_F_PKCS5_V2_PBE_KEYIVGEN = 118

EVP_F_PKCS8_SET_BROKEN = 112

EVP_F_RC2_MAGIC_TO_METH = 109

EVP_F_RC5_CTRL = 125

EVP_MAX_MD_SIZE = 64

EVP_PKEY_DH = 28
EVP_PKEY_DSA = 116
EVP_PKEY_EC = 408
EVP_PKEY_RSA = 6

EVP_R_AES_KEY_SETUP_FAILED = 143

EVP_R_ASN1_LIB = 140

EVP_R_BAD_BLOCK_LENGTH = 136

EVP_R_BAD_DECRYPT = 100

EVP_R_BAD_KEY_LENGTH = 137

EVP_R_BN_DECODE_ERROR = 112

EVP_R_BN_PUBKEY_ERROR = 113

EVP_R_CAMELLIA_KEY_SETUP_FAILED = 157

EVP_R_CIPHER_PARAMETER_ERROR = 122

EVP_R_CTRL_NOT_IMPLEMENTED = 132

EVP_R_CTRL_OPERATION_NOT_IMPLEMENTED = 133

EVP_R_DATA_NOT_MULTIPLE_OF_BLOCK_LENGTH = 138

EVP_R_DECODE_ERROR = 114

EVP_R_DIFFERENT_KEY_TYPES = 101

EVP_R_ENCODE_ERROR = 115

EVP_R_INITIALIZATION_ERROR = 134

EVP_R_INPUT_NOT_INITIALIZED = 111

EVP_R_INVALID_KEY_LENGTH = 130

EVP_R_IV_TOO_LARGE = 102

EVP_R_KEYGEN_FAILURE = 120

EVP_R_MISSING_PARAMETERS = 103

EVP_R_NO_CIPHER_SET = 131

EVP_R_NO_DIGEST_SET = 139

EVP_R_NO_DSA_PARAMETERS = 116

EVP_R_NO_SIGN_FUNCTION_CONFIGURED = 104

EVP_R_NO_VERIFY_FUNCTION_CONFIGURED = 105

EVP_R_PKCS8_UNKNOWN_BROKEN_TYPE = 117

EVP_R_PUBLIC_KEY_NOT_RSA = 106

EVP_R_UNKNOWN_PBE_ALGORITHM = 121

EVP_R_UNSUPORTED_NUMBER_OF_ROUNDS = 135

EVP_R_UNSUPPORTED_CIPHER = 107
EVP_R_UNSUPPORTED_KEYLENGTH = 123

EVP_R_UNSUPPORTED_KEY_DERIVATION_FUNCTION = 124

EVP_R_UNSUPPORTED_PRIVATE_KEY_ALGORITHM = 118

EVP_R_UNSUPPORTED_SALT_TYPE = 126

EVP_R_WRONG_FINAL_BLOCK_LENGTH = 109

EVP_R_WRONG_PUBLIC_KEY_TYPE = 110

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

OPENSSL_EC_NAMED_CURVE = 1

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

PEM_F_PEM_F_PEM_WRITE_PKCS8PRIVATEKEY = 118

PEM_F_PEM_GET_EVP_CIPHER_INFO = 107

PEM_F_PEM_PK8PKEY = 119
PEM_F_PEM_READ = 108

PEM_F_PEM_READ_BIO = 109

PEM_F_PEM_READ_BIO_PRIVATEKEY = 123

PEM_F_PEM_READ_PRIVATEKEY = 124

PEM_F_PEM_SEALFINAL = 110
PEM_F_PEM_SEALINIT = 111
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

PEM_R_PUBLIC_KEY_NO_RSA = 110

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

SSL_VERIFY_CLIENT_ONCE = 4

SSL_VERIFY_FAIL_IF_NO_PEER_CERT = 2

SSL_VERIFY_NONE = 0
SSL_VERIFY_PEER = 1

TLSEXT_NAMETYPE_host_name = 0

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

def ACCESS_DESCRIPTION_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ACCESS_DESCRIPTION_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def AES_ctr128_encrypt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def AES_set_decrypt_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def AES_set_encrypt_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def AES_unwrap_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def AES_wrap_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_BIT_STRING_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_BIT_STRING_get_bit(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_BIT_STRING_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_BIT_STRING_set_bit(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_ENUMERATED_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_ENUMERATED_get(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_ENUMERATED_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_ENUMERATED_set(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_GENERALIZEDTIME_check(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_GENERALIZEDTIME_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_GENERALIZEDTIME_set(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_GENERALIZEDTIME_set_string(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_IA5STRING_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_INTEGER_cmp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_INTEGER_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_INTEGER_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_INTEGER_get(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_INTEGER_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_INTEGER_set(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_INTEGER_to_BN(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_item_d2i(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_ITEM_ptr(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_OBJECT_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_OBJECT_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_OCTET_STRING_cmp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_OCTET_STRING_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_OCTET_STRING_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_OCTET_STRING_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_OCTET_STRING_set(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_STRING_cmp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_STRING_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_STRING_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_STRING_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_STRING_length(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_STRING_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_STRING_set(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_STRING_set_default_mask_asc(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_STRING_to_UTF8(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_STRING_type(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_STRING_type_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_TIME_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_TIME_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_TIME_print(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_TIME_set(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_TIME_to_generalizedtime(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_UTCTIME_check(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_UTCTIME_cmp_time_t(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_UTCTIME_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_UTCTIME_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_UTCTIME_print(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_UTCTIME_set(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_UTF8STRING_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ASN1_UTF8STRING_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def AUTHORITY_KEYID_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def AUTHORITY_KEYID_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BASIC_CONSTRAINTS_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BASIC_CONSTRAINTS_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_append_filename(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_callback_ctrl(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_ctrl(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_ctrl_pending(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_ctrl_wpending(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_eof(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_find_type(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_flush(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_free_all(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_f_buffer(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_f_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_gets(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_get_buffer_num_lines(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_get_close(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_get_fd(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_get_fp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_get_info_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_get_mem_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_get_mem_ptr(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_int_ctrl(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_method_type(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_new_CMS(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_new_fd(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_new_file(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_new_fp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_new_mem_buf(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_new_socket(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_next(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_pending(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_pop(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_ptr_ctrl(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_puts(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_read(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_read_filename(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_reset(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_retry_type(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_rw_filename(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_seek(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_set(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_set_buffer_read_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_set_buffer_size(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_set_close(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_set_fd(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_set_fp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_set_info_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_set_mem_buf(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_set_mem_eof_return(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_set_read_buffer_size(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_set_write_buffer_size(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_should_io_special(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_should_read(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_should_retry(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_should_write(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_s_fd(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_s_file(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_s_mem(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_s_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_s_socket(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_tell(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_vfree(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_wpending(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_write(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BIO_write_filename(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_add(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_bin2bn(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_bn2bin(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_bn2hex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_clear_bit(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_cmp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_copy(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_CTX_end(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_CTX_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_CTX_get(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_CTX_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_CTX_start(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_dec2bn(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_div(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_exp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_gcd(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_get_word(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_hex2bn(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_is_bit_set(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_lshift(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_lshift1(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_mask_bits(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_mod(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_mod_add(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_mod_exp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_mod_inverse(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_mod_mul(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_mod_sqr(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_mod_sub(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_mul(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_nnmod(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_num_bits(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_num_bytes(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_one(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_rshift(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_rshift1(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_set_bit(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_set_word(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_sqr(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_sub(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_to_ASN1_INTEGER(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_value_one(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def BN_zero(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CMAC_CTX_copy(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CMAC_CTX_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CMAC_CTX_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CMAC_Final(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CMAC_Init(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CMAC_Update(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CMS_add1_signer(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CMS_decrypt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CMS_encrypt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CMS_final(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CMS_sign(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CMS_verify(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def Cryptography_EVP_PKEY_decrypt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def Cryptography_EVP_PKEY_encrypt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def Cryptography_EVP_PKEY_id(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def Cryptography_HMAC_CTX_copy(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def Cryptography_HMAC_Final(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def Cryptography_HMAC_Init_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def Cryptography_HMAC_Update(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def Cryptography_i2d_NAME_CONSTRAINTS(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def Cryptography_SSL_CTX_get_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def Cryptography_X509_REVOKED_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_add(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_cleanup_all_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_get_id_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_get_locking_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_is_mem_check_on(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_lock(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_malloc_init(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_mem_ctrl(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_mem_leaks(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_num_locks(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_set_id_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def CRYPTO_set_locking_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_ASN1_OBJECT(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_ASN1_TYPE(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_DHparams(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_DSAPrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_DSAPrivateKey_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_DSAPublicKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_DSA_PUBKEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_DSA_PUBKEY_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_DSA_SIG(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_ECDSA_SIG(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_ECPrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_ECPrivateKey_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_EC_PUBKEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_EC_PUBKEY_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_GENERAL_NAMES(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_PKCS12_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_PKCS7_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_PKCS8PrivateKey_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_PKCS8_PRIV_KEY_INFO_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_PrivateKey_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_PUBKEY_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_RSAPrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_RSAPrivateKey_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_RSAPublicKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_RSAPublicKey_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_RSA_PUBKEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_RSA_PUBKEY_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_X509_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_X509_CRL_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def d2i_X509_REQ_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DHparams_print(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DHparams_print_fp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DH_check(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DH_check_pub_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DH_compute_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DH_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DH_generate_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DH_generate_parameters(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DH_generate_parameters_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DH_get_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DH_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DH_set_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DH_size(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DIST_POINT_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DIST_POINT_NAME_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DIST_POINT_NAME_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DIST_POINT_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DSA_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DSA_generate_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DSA_generate_parameters(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DSA_generate_parameters_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DSA_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DSA_sign(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DSA_SIG_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DSA_SIG_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DSA_size(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DSA_verify(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DTLSv1_client_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DTLSv1_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def DTLSv1_server_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDH_compute_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDH_get_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDH_get_ex_new_index(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDH_set_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_do_sign(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_do_sign_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_do_verify(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_get_default_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_get_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_get_ex_new_index(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_OpenSSL(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_set_default_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_set_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_set_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_sign(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_sign_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_sign_setup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_SIG_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_SIG_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_size(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ECDSA_verify(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_curve_nid2nist(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_get_builtin_curves(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GF2m_simple_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GFp_mont_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GFp_nist_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GFp_simple_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_clear_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_get0_generator(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_get_curve_GF2m(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_get_curve_GFp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_get_curve_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_get_degree(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_get_order(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_have_precompute_mult(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_method_of(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_new_by_curve_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_new_curve_GF2m(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_new_curve_GFp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_precompute_mult(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_set_asn1_flag(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_set_curve_GF2m(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_set_curve_GFp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_GROUP_set_point_conversion_form(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_check_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_clear_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_copy(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_generate_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_get0_group(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_get0_private_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_get0_public_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_get_conv_form(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_get_enc_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_get_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_get_key_method_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_insert_key_method_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_new_by_curve_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_precompute_mult(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_set_asn1_flag(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_set_conv_form(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_set_enc_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_set_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_set_group(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_set_private_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_set_public_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_set_public_key_affine_coordinates(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_KEY_up_ref(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_METHOD_get_field_type(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINTs_make_affine(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINTs_mul(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_add(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_bn2point(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_clear_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_cmp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_copy(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_dbl(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_get_affine_coordinates_GF2m(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_get_affine_coordinates_GFp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_get_Jprojective_coordinates_GFp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_hex2point(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_invert(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_is_at_infinity(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_is_on_curve(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_make_affine(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_method_of(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_mul(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_oct2point(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_point2bn(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_point2hex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_point2oct(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_set_affine_coordinates_GF2m(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_set_affine_coordinates_GFp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_set_compressed_coordinates_GF2m(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_set_compressed_coordinates_GFp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_set_Jprojective_coordinates_GFp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EC_POINT_set_to_infinity(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_add(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_add_conf_module(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_by_id(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_cleanup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_cmd_is_executable(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_ctrl(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_ctrl_cmd(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_ctrl_cmd_string(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_finish(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_cipher(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_cipher_engine(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_cmd_defns(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_default_DH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_default_DSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_default_ECDH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_default_ECDSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_default_RAND(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_default_RSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_DH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_digest(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_digest_engine(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_DSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_ECDH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_ECDSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_first(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_id(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_last(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_next(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_prev(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_RAND(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_RSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_STORE(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_get_table_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_init(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_load_builtin_engines(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_load_cryptodev(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_load_dynamic(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_load_openssl(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_load_private_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_load_public_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_all_ciphers(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_all_complete(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_all_DH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_all_digests(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_all_DSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_all_ECDH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_all_ECDSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_all_RAND(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_all_RSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_all_STORE(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_ciphers(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_complete(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_DH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_digests(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_DSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_ECDH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_ECDSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_RAND(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_RSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_register_STORE(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_remove(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_ciphers(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_cmd_defns(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_ctrl_function(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_default(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_default_ciphers(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_default_DH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_default_digests(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_default_DSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_default_ECDH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_default_ECDSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_default_RAND(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_default_RSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_default_string(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_destroy_function(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_DH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_digests(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_DSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_ECDH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_ECDSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_finish_function(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_id(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_init_function(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_load_privkey_function(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_load_pubkey_function(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_RAND(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_RSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_STORE(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_set_table_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_unregister_ciphers(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_unregister_DH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_unregister_digests(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_unregister_DSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_unregister_ECDH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_unregister_ECDSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_unregister_RAND(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_unregister_RSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_unregister_STORE(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ENGINE_up_ref(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_clear_error(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_error_string(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_error_string_n(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_FATAL_ERROR(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_free_strings(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_func_error_string(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_get_error(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_get_error_line(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_get_error_line_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_GET_FUNC(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_GET_LIB(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_get_next_error_library(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_GET_REASON(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_lib_error_string(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_load_crypto_strings(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_load_RAND_strings(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_load_SSL_strings(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_PACK(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_peek_error(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_peek_error_line(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_peek_error_line_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_peek_last_error(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_peek_last_error_line(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_peek_last_error_line_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_print_errors(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_print_errors_fp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_put_error(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_reason_error_string(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def ERR_remove_thread_state(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CipherFinal_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CipherInit_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CipherUpdate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CIPHER_block_size(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CIPHER_CTX_block_size(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CIPHER_CTX_cipher(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CIPHER_CTX_cleanup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CIPHER_CTX_ctrl(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CIPHER_CTX_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CIPHER_CTX_init(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CIPHER_CTX_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CIPHER_CTX_set_key_length(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_CIPHER_CTX_set_padding(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_DecryptFinal_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_DecryptInit_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_DecryptUpdate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_DigestFinal_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_DigestInit_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_DigestUpdate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_EncryptFinal_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_EncryptInit_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_EncryptUpdate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_get_cipherbyname(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_get_digestbyname(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_md5(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_MD_CTX_cleanup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_MD_CTX_copy_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_MD_CTX_create(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_MD_CTX_destroy(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_MD_CTX_md(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_MD_size(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKCS82PKEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_add1_attr(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_add1_attr_by_NID(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_add1_attr_by_OBJ(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_add1_attr_by_txt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_assign_DSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_assign_EC_KEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_assign_RSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_bits(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_cmp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_CTX_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_CTX_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_CTX_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_CTX_new_id(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_CTX_set_rsa_mgf1_md(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_CTX_set_rsa_padding(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_CTX_set_rsa_pss_saltlen(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_CTX_set_signature_md(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_decrypt_init(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_delete_attr(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_encrypt_init(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_get1_DH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_get1_DSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_get1_EC_KEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_get1_RSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_get_attr(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_get_attr_by_NID(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_get_attr_by_OBJ(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_get_attr_count(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_id(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_set1_DH(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_set1_DSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_set1_EC_KEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_set1_RSA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_sign(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_sign_init(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_size(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_type(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_verify(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_PKEY_verify_init(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_ripemd160(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_sha1(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_sha224(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_sha256(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_sha384(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_sha512(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_SignFinal(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_SignInit(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_SignUpdate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_VerifyFinal(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_VerifyInit(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def EVP_VerifyUpdate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def GENERAL_NAMES_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def GENERAL_NAMES_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def GENERAL_NAME_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def GENERAL_NAME_print(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def GENERAL_SUBTREE_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def HMAC_CTX_cleanup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def HMAC_CTX_init(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2a_ASN1_INTEGER(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_ASN1_BIT_STRING(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_ASN1_ENUMERATED(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_ASN1_GENERALIZEDTIME(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_ASN1_INTEGER(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_ASN1_OBJECT(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_ASN1_OCTET_STRING(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_ASN1_TYPE(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_AUTHORITY_INFO_ACCESS(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_AUTHORITY_KEYID(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_BASIC_CONSTRAINTS(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_CERTIFICATEPOLICIES(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_CMS_bio_stream(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_CRL_DIST_POINTS(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_DHparams(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_DSAPrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_DSAPrivateKey_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_DSAPublicKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_DSA_PUBKEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_DSA_PUBKEY_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_DSA_SIG(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_ECDSA_SIG(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_ECPrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_ECPrivateKey_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_EC_PUBKEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_EC_PUBKEY_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_EXTENDED_KEY_USAGE(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_GENERAL_NAMES(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_PKCS12_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_PKCS7_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_PKCS8PrivateKey_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_PKCS8PrivateKey_nid_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_PrivateKey_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_PUBKEY_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_RSAPrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_RSAPrivateKey_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_RSAPublicKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_RSAPublicKey_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_RSA_PUBKEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_RSA_PUBKEY_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_X509(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_X509_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_X509_CINF(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_X509_CRL_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_X509_CRL_INFO(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_X509_NAME(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_X509_REQ_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2d_X509_REQ_INFO(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def i2o_ECPublicKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def M_ASN1_TIME_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def NAME_CONSTRAINTS_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def NAME_CONSTRAINTS_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def NETSCAPE_SPKI_b64_decode(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def NETSCAPE_SPKI_b64_encode(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def NETSCAPE_SPKI_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def NETSCAPE_SPKI_get_pubkey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def NETSCAPE_SPKI_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def NETSCAPE_SPKI_set_pubkey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def NETSCAPE_SPKI_sign(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def NETSCAPE_SPKI_verify(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def NOTICEREF_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def NOTICEREF_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def o2i_ECPublicKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_cleanup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_cmp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_create(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_ln2nid(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_nid2ln(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_nid2obj(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_nid2sn(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_obj2nid(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_obj2txt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_sn2nid(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_txt2nid(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OBJ_txt2obj(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OpenSSL_add_all_algorithms(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OPENSSL_config(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OPENSSL_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OPENSSL_no_config(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OTHERNAME_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def OTHERNAME_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_read_bio_DHparams(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_read_bio_DSAPrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_read_bio_DSA_PUBKEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_read_bio_PKCS7(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_read_bio_PrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_read_bio_PUBKEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_read_bio_RSAPrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_read_bio_RSAPublicKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_read_bio_X509(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_read_bio_X509_CRL(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_read_bio_X509_REQ(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_CMS_stream(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_DHparams(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_DSAPrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_DSA_PUBKEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_ECPrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_PKCS7(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_PKCS8PrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_PKCS8PrivateKey_nid(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_PrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_PUBKEY(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_RSAPrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_RSAPublicKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_X509(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_X509_CRL(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PEM_write_bio_X509_REQ(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS12_create(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS12_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS12_parse(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS5_PBKDF2_HMAC(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS5_PBKDF2_HMAC_SHA1(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_dataInit(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_decrypt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_encrypt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_get0_signers(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_sign(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_type_is_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_type_is_digest(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_type_is_encrypted(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_type_is_enveloped(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_type_is_signed(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_type_is_signedAndEnveloped(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS7_verify(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def PKCS8_PRIV_KEY_INFO_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def POLICYINFO_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def POLICYINFO_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def POLICYQUALINFO_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def POLICYQUALINFO_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RAND_add(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RAND_bytes(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RAND_cleanup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RAND_egd(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RAND_egd_bytes(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RAND_file_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RAND_load_file(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RAND_pseudo_bytes(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RAND_query_egd_bytes(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RAND_seed(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RAND_status(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RAND_write_file(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSAPublicKey_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_blinding_off(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_blinding_on(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_check_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_generate_key_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_padding_add_PKCS1_OAEP(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_padding_add_PKCS1_PSS(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_padding_check_PKCS1_OAEP(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_print(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_private_decrypt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_private_encrypt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_public_decrypt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_public_encrypt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_size(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def RSA_verify_PKCS1_PSS(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ACCESS_DESCRIPTION_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ACCESS_DESCRIPTION_new_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ACCESS_DESCRIPTION_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ACCESS_DESCRIPTION_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ACCESS_DESCRIPTION_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ASN1_INTEGER_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ASN1_INTEGER_new_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ASN1_INTEGER_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ASN1_INTEGER_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ASN1_INTEGER_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ASN1_OBJECT_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ASN1_OBJECT_new_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ASN1_OBJECT_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ASN1_OBJECT_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_ASN1_OBJECT_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_DIST_POINT_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_DIST_POINT_new_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_DIST_POINT_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_DIST_POINT_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_DIST_POINT_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_GENERAL_NAME_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_GENERAL_NAME_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_GENERAL_NAME_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_GENERAL_SUBTREE_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_GENERAL_SUBTREE_new_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_GENERAL_SUBTREE_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_GENERAL_SUBTREE_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_GENERAL_SUBTREE_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_POLICYINFO_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_POLICYINFO_new_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_POLICYINFO_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_POLICYINFO_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_POLICYINFO_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_POLICYQUALINFO_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_POLICYQUALINFO_new_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_POLICYQUALINFO_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_POLICYQUALINFO_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_POLICYQUALINFO_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_SSL_CIPHER_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_SSL_CIPHER_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_CRL_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_CRL_new_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_CRL_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_CRL_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_CRL_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_EXTENSION_delete(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_EXTENSION_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_EXTENSION_insert(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_EXTENSION_new_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_EXTENSION_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_EXTENSION_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_EXTENSION_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_NAME_ENTRY_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_NAME_ENTRY_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_NAME_ENTRY_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_NAME_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_NAME_new_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_NAME_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_NAME_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_NAME_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_new_null(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_push(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_REVOKED_num(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_REVOKED_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def sk_X509_value(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SMIME_read_PKCS7(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SMIME_write_PKCS7(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSLeay(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSLeay_version(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSLv23_client_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSLv23_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSLv23_server_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSLv3_client_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSLv3_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSLv3_server_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_check_private_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CIPHER_description(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CIPHER_get_bits(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CIPHER_get_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CIPHER_get_version(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_COMP_get_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_add_client_CA(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_add_extra_chain_cert(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_check_private_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_get_cert_store(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_get_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_get_ex_new_index(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_get_info_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_get_mode(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_get_options(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_get_session_cache_mode(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_get_timeout(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_get_verify_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_get_verify_depth(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_get_verify_mode(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_load_verify_locations(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_alpn_protos(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_alpn_select_cb(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_cert_cb(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_cert_store(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_cert_verify_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_cipher_list(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_client_CA_list(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_client_cert_engine(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_default_passwd_cb(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_default_passwd_cb_userdata(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_default_verify_paths(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_info_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_mode(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_next_protos_advertised_cb(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_next_proto_select_cb(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_options(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_session_cache_mode(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_timeout(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_tlsext_servername_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_tlsext_status_arg(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_tlsext_status_cb(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_tmp_dh(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_tmp_ecdh(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_verify(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_set_verify_depth(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_use_certificate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_use_certificate_ASN1(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_use_certificate_chain_file(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_use_certificate_file(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_use_PrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_use_PrivateKey_ASN1(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_CTX_use_PrivateKey_file(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_do_handshake(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get0_alpn_selected(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get0_next_proto_negotiated(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get1_session(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_ciphers(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_cipher_list(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_client_CA_list(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_current_cipher(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_current_compression(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_current_expansion(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_error(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_ex_data_X509_STORE_CTX_idx(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_ex_new_index(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_finished(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_info_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_mode(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_options(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_peer_certificate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_peer_cert_chain(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_peer_finished(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_secure_renegotiation_support(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_servername(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_server_tmp_key(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_shutdown(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_tlsext_status_ocsp_resp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_verify_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_verify_depth(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_verify_mode(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_get_version(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_library_init(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_load_error_strings(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_peek(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_pending(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_read(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_renegotiate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_renegotiate_pending(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_select_next_proto(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_SESSION_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_SESSION_print(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_session_reused(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_accept_state(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_alpn_protos(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_bio(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_cert_cb(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_connect_state(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_fd(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_info_callback(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_mode(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_options(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_session(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_shutdown(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_SSL_CTX(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_tlsext_host_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_tlsext_status_ocsp_resp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_tlsext_status_type(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_verify(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_set_verify_depth(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_shutdown(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_state_string_long(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_total_renegotiations(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_use_certificate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_use_certificate_ASN1(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_use_certificate_file(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_use_PrivateKey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_use_PrivateKey_ASN1(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_use_PrivateKey_file(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_version(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_want_read(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_want_write(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def SSL_write(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def TLSv1_1_client_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def TLSv1_1_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def TLSv1_1_server_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def TLSv1_2_client_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def TLSv1_2_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def TLSv1_2_server_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def TLSv1_client_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def TLSv1_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def TLSv1_server_method(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def USERNOTICE_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def USERNOTICE_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509V3_EXT_add_alias(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509V3_EXT_conf_nid(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509V3_EXT_d2i(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509V3_EXT_get(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509V3_EXT_get_nid(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509V3_EXT_i2d(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509V3_EXT_nconf(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509V3_EXT_print(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509V3_set_ctx(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509V3_set_ctx_nodb(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_add_ext(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_alias_get0(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_cmp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_add0_revoked(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_add_ext(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_cmp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_get_ext(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_get_ext_count(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_get_issuer(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_get_lastUpdate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_get_nextUpdate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_get_REVOKED(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_get_version(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_print(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_set_issuer_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_set_lastUpdate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_set_nextUpdate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_set_version(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_sign(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_sort(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_CRL_verify(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_delete_ext(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_digest(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_EXTENSION_create_by_OBJ(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_EXTENSION_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_EXTENSION_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_EXTENSION_get_critical(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_EXTENSION_get_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_EXTENSION_get_object(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_default_cert_area(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_default_cert_dir(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_default_cert_dir_env(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_default_cert_file(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_default_cert_file_env(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_default_private_dir(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_ext(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_ext_by_NID(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_ext_count(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_ex_new_index(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_issuer_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_notAfter(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_notBefore(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_pubkey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_serialNumber(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_subject_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_get_version(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_gmtime_adj(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_add_entry_by_NID(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_add_entry_by_OBJ(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_add_entry_by_txt(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_cmp(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_delete_entry(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_dup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_entry_count(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_ENTRY_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_ENTRY_get_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_ENTRY_get_object(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_get_entry(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_get_index_by_NID(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_hash(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_NAME_oneline(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_print_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_add_extensions(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_digest(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_get_extensions(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_get_pubkey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_get_subject_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_get_version(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_print(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_print_ex(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_set_pubkey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_set_subject_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_set_version(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_sign(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REQ_verify(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REVOKED_add1_ext_i2d(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REVOKED_add_ext(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REVOKED_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REVOKED_get_ext(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REVOKED_get_ext_count(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REVOKED_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REVOKED_set_revocationDate(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_REVOKED_set_serialNumber(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_set_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_set_issuer_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_set_notAfter(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_set_notBefore(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_set_pubkey(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_set_serialNumber(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_set_subject_name(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_set_version(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_sign(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_add_cert(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_add_crl(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_cleanup(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_get0_param(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_get1_chain(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_get_chain(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_get_current_cert(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_get_error(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_get_error_depth(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_get_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_get_ex_new_index(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_init(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_set0_crls(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_set0_param(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_set_cert(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_set_chain(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_set_default(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_set_error(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_set_ex_data(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_set_verify_cb(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_CTX_trusted_stack(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_free(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_load_locations(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_set1_param(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_set_default_paths(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_STORE_set_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_subject_name_hash(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_verify_cert(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_verify_cert_error_string(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_add0_policy(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_clear_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_get_depth(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_get_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_new(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_set1_email(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_set1_host(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_set1_ip(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_set1_ip_asc(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_set1_policies(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_set_depth(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_set_flags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_set_hostflags(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_set_purpose(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_set_time(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

def X509_VERIFY_PARAM_set_trust(*args, **kwargs): # real signature unknown
    """ direct call to the C function of the same name """
    pass

# no classes
