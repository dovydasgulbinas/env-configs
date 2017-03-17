# encoding: utf-8
# module xapian._xapian calls itself _xapian
# from /usr/lib/python2.7/dist-packages/xapian/_xapian.so
# by generator 1.143
# no doc

# imports
from _xapian import (AssertionError_swiginit, AssertionError_swigregister, 
    BM25Weight_swiginit, BM25Weight_swigregister, BoolWeight_swiginit, 
    BoolWeight_swigregister, Compactor_add_source, Compactor_compact, 
    Compactor_resolve_duplicate_metadata, Compactor_set_block_size, 
    Compactor_set_compaction_level, Compactor_set_destdir, 
    Compactor_set_multipass, Compactor_set_renumber, Compactor_set_status, 
    Compactor_swiginit, Compactor_swigregister, DatabaseCorruptError_swiginit, 
    DatabaseCorruptError_swigregister, DatabaseCreateError_swiginit, 
    DatabaseCreateError_swigregister, DatabaseError_swiginit, 
    DatabaseError_swigregister, DatabaseLockError_swiginit, 
    DatabaseLockError_swigregister, DatabaseModifiedError_swiginit, 
    DatabaseModifiedError_swigregister, DatabaseOpeningError_swiginit, 
    DatabaseOpeningError_swigregister, DatabaseVersionError_swiginit, 
    DatabaseVersionError_swigregister, Database___str__, 
    Database__metadata_keys_begin, Database__metadata_keys_end, 
    Database_add_database, Database_allterms_begin, Database_allterms_end, 
    Database_close, Database_get_avlength, Database_get_collection_freq, 
    Database_get_doccount, Database_get_doclength, 
    Database_get_doclength_lower_bound, Database_get_doclength_upper_bound, 
    Database_get_document, Database_get_lastdocid, Database_get_metadata, 
    Database_get_spelling_suggestion, Database_get_termfreq, 
    Database_get_uuid, Database_get_value_freq, 
    Database_get_value_lower_bound, Database_get_value_upper_bound, 
    Database_get_wdf_upper_bound, Database_has_positions, Database_keep_alive, 
    Database_positionlist_begin, Database_positionlist_end, 
    Database_postlist_begin, Database_postlist_end, Database_reopen, 
    Database_spellings_begin, Database_spellings_end, Database_swiginit, 
    Database_swigregister, Database_synonym_keys_begin, 
    Database_synonym_keys_end, Database_synonyms_begin, Database_synonyms_end, 
    Database_term_exists, Database_termlist_begin, Database_termlist_end, 
    Database_valuestream_begin, Database_valuestream_end, 
    DateValueRangeProcessor_swiginit, DateValueRangeProcessor_swigregister, 
    DecreasingValueWeightPostingSource_swiginit, 
    DecreasingValueWeightPostingSource_swigregister, 
    DocNotFoundError_swiginit, DocNotFoundError_swigregister, 
    Document___str__, Document_add_boolean_term, Document_add_posting, 
    Document_add_term, Document_add_value, Document_clear_terms, 
    Document_clear_values, Document_get_data, Document_get_docid, 
    Document_get_value, Document_remove_posting, Document_remove_term, 
    Document_remove_value, Document_serialise, Document_set_data, 
    Document_swiginit, Document_swigregister, Document_termlist_begin, 
    Document_termlist_count, Document_termlist_end, Document_unserialise, 
    Document_values_begin, Document_values_count, Document_values_end, 
    ESetIterator___eq__, ESetIterator___ne__, ESetIterator___str__, 
    ESetIterator_equals, ESetIterator_get_term, ESetIterator_get_weight, 
    ESetIterator_next, ESetIterator_prev, ESetIterator_swiginit, 
    ESetIterator_swigregister, ESet___str__, ESet_back, ESet_begin, 
    ESet_empty, ESet_end, ESet_get_ebound, ESet_items_get, ESet_size, 
    ESet_swiginit, ESet_swigregister, Enquire___str__, Enquire_add_matchspy, 
    Enquire_clear_matchspies, Enquire_get_eset, 
    Enquire_get_matching_terms_begin, Enquire_get_matching_terms_end, 
    Enquire_get_mset, Enquire_get_query, Enquire_set_collapse_key, 
    Enquire_set_cutoff, Enquire_set_docid_order, Enquire_set_query, 
    Enquire_set_sort_by_key, Enquire_set_sort_by_key_then_relevance, 
    Enquire_set_sort_by_relevance, Enquire_set_sort_by_relevance_then_key, 
    Enquire_set_sort_by_relevance_then_value, Enquire_set_sort_by_value, 
    Enquire_set_sort_by_value_then_relevance, Enquire_set_weighting_scheme, 
    Enquire_swiginit, Enquire_swigregister, Error___str__, Error_get_context, 
    Error_get_error_string, Error_get_msg, Error_get_type, Error_swigregister, 
    ExpandDecider___call__, ExpandDecider_swiginit, 
    ExpandDecider_swigregister, FeatureUnavailableError_swiginit, 
    FeatureUnavailableError_swigregister, FixedWeightPostingSource_swiginit, 
    FixedWeightPostingSource_swigregister, InternalError_swiginit, 
    InternalError_swigregister, InvalidArgumentError_swiginit, 
    InvalidArgumentError_swigregister, InvalidOperationError_swiginit, 
    InvalidOperationError_swigregister, KeyMaker___call__, KeyMaker_swiginit, 
    KeyMaker_swigregister, LogicError_swigregister, MSetIterator___eq__, 
    MSetIterator___ne__, MSetIterator___str__, MSetIterator_equals, 
    MSetIterator_get_collapse_count, MSetIterator_get_collapse_key, 
    MSetIterator_get_docid, MSetIterator_get_document, 
    MSetIterator_get_percent, MSetIterator_get_rank, MSetIterator_get_weight, 
    MSetIterator_next, MSetIterator_prev, MSetIterator_swiginit, 
    MSetIterator_swigregister, MSet___cmp__, MSet___str__, 
    MSet__get_hit_internal, MSet_back, MSet_begin, MSet_convert_to_percent, 
    MSet_empty, MSet_end, MSet_fetch, MSet_get_docid, MSet_get_document, 
    MSet_get_document_percentage, MSet_get_firstitem, 
    MSet_get_matches_estimated, MSet_get_matches_lower_bound, 
    MSet_get_matches_upper_bound, MSet_get_max_attained, 
    MSet_get_max_possible, MSet_get_termfreq, MSet_get_termweight, 
    MSet_get_uncollapsed_matches_estimated, 
    MSet_get_uncollapsed_matches_lower_bound, 
    MSet_get_uncollapsed_matches_upper_bound, MSet_items_get, MSet_size, 
    MSet_swiginit, MSet_swigregister, MatchDecider___call__, 
    MatchDecider_swiginit, MatchDecider_swigregister, MatchSpy___call__, 
    MatchSpy___str__, MatchSpy_merge_results, MatchSpy_name, 
    MatchSpy_swiginit, MatchSpy_swigregister, MultiValueKeyMaker_add_value, 
    MultiValueKeyMaker_swiginit, MultiValueKeyMaker_swigregister, 
    MultiValueSorter_add, MultiValueSorter_swiginit, 
    MultiValueSorter_swigregister, NetworkError_swiginit, 
    NetworkError_swigregister, NetworkTimeoutError_swiginit, 
    NetworkTimeoutError_swigregister, NumberValueRangeProcessor_swiginit, 
    NumberValueRangeProcessor_swigregister, PositionIterator___eq__, 
    PositionIterator___ne__, PositionIterator___str__, 
    PositionIterator_equals, PositionIterator_get_termpos, 
    PositionIterator_next, PositionIterator_skip_to, 
    PositionIterator_swiginit, PositionIterator_swigregister, 
    PostingIterator___eq__, PostingIterator___ne__, PostingIterator___str__, 
    PostingIterator_equals, PostingIterator_get_docid, 
    PostingIterator_get_doclength, PostingIterator_get_wdf, 
    PostingIterator_next, PostingIterator_positionlist_begin, 
    PostingIterator_positionlist_end, PostingIterator_skip_to, 
    PostingIterator_swiginit, PostingIterator_swigregister, 
    PostingSource___str__, PostingSource_at_end, PostingSource_check, 
    PostingSource_get_docid, PostingSource_get_maxweight, 
    PostingSource_get_termfreq_est, PostingSource_get_termfreq_max, 
    PostingSource_get_termfreq_min, PostingSource_get_weight, 
    PostingSource_init, PostingSource_name, PostingSource_next, 
    PostingSource_skip_to, PostingSource_swiginit, PostingSource_swigregister, 
    QueryParserError_swiginit, QueryParserError_swigregister, 
    QueryParser___str__, QueryParser_add_boolean_prefix, 
    QueryParser_add_prefix, QueryParser_add_valuerangeprocessor, 
    QueryParser_get_corrected_query_string, QueryParser_get_default_op, 
    QueryParser_parse_query, QueryParser_set_database, 
    QueryParser_set_default_op, QueryParser_set_max_wildcard_expansion, 
    QueryParser_set_stemmer, QueryParser_set_stemming_strategy, 
    QueryParser_set_stopper, QueryParser_stoplist_begin, 
    QueryParser_stoplist_end, QueryParser_swiginit, QueryParser_swigregister, 
    QueryParser_unstem_begin, QueryParser_unstem_end, Query___str__, 
    Query_empty, Query_get_length, Query_get_terms_begin, Query_get_terms_end, 
    Query_serialise, Query_swiginit, Query_swigregister, Query_unserialise, 
    RSet___str__, RSet_add_document, RSet_contains, RSet_empty, 
    RSet_remove_document, RSet_size, RSet_swiginit, RSet_swigregister, 
    RangeError_swiginit, RangeError_swigregister, Registry_get_match_spy, 
    Registry_get_posting_source, Registry_get_weighting_scheme, 
    Registry_register_match_spy, Registry_register_posting_source, 
    Registry_register_weighting_scheme, Registry_swiginit, 
    Registry_swigregister, RuntimeError_swigregister, 
    SWIG_PyInstanceMethod_New, SerialisationError_swiginit, 
    SerialisationError_swigregister, SimpleStopper_add, 
    SimpleStopper_swiginit, SimpleStopper_swigregister, Sorter_swigregister, 
    StemImplementation___call__, StemImplementation___str__, 
    StemImplementation_swiginit, StemImplementation_swigregister, 
    Stem___call__, Stem___str__, Stem_get_available_languages, Stem_swiginit, 
    Stem_swigregister, Stopper___call__, Stopper___str__, Stopper_swiginit, 
    Stopper_swigregister, StringValueRangeProcessor_swiginit, 
    StringValueRangeProcessor_swigregister, SwigPyIterator___add__, 
    SwigPyIterator___eq__, SwigPyIterator___iadd__, SwigPyIterator___isub__, 
    SwigPyIterator___ne__, SwigPyIterator___next__, SwigPyIterator___sub__, 
    SwigPyIterator_advance, SwigPyIterator_copy, SwigPyIterator_decr, 
    SwigPyIterator_distance, SwigPyIterator_equal, SwigPyIterator_incr, 
    SwigPyIterator_next, SwigPyIterator_previous, SwigPyIterator_swigregister, 
    SwigPyIterator_value, TermGenerator___str__, TermGenerator_get_document, 
    TermGenerator_get_termpos, TermGenerator_increase_termpos, 
    TermGenerator_index_text, TermGenerator_index_text_without_positions, 
    TermGenerator_set_database, TermGenerator_set_document, 
    TermGenerator_set_flags, TermGenerator_set_max_word_length, 
    TermGenerator_set_stemmer, TermGenerator_set_stemming_strategy, 
    TermGenerator_set_stopper, TermGenerator_set_termpos, 
    TermGenerator_swiginit, TermGenerator_swigregister, TermIterator___eq__, 
    TermIterator___ne__, TermIterator___str__, TermIterator_equals, 
    TermIterator_get_term, TermIterator_get_termfreq, TermIterator_get_wdf, 
    TermIterator_next, TermIterator_positionlist_begin, 
    TermIterator_positionlist_count, TermIterator_positionlist_end, 
    TermIterator_skip_to, TermIterator_swiginit, TermIterator_swigregister, 
    TradWeight_swiginit, TradWeight_swigregister, UnimplementedError_swiginit, 
    UnimplementedError_swigregister, ValueCountMatchSpy_get_total, 
    ValueCountMatchSpy_swiginit, ValueCountMatchSpy_swigregister, 
    ValueCountMatchSpy_top_values_begin, ValueCountMatchSpy_top_values_end, 
    ValueCountMatchSpy_values_begin, ValueCountMatchSpy_values_end, 
    ValueIterator___eq__, ValueIterator___ne__, ValueIterator___str__, 
    ValueIterator_check, ValueIterator_equals, ValueIterator_get_docid, 
    ValueIterator_get_value, ValueIterator_get_valueno, ValueIterator_next, 
    ValueIterator_skip_to, ValueIterator_swiginit, ValueIterator_swigregister, 
    ValueMapPostingSource_add_mapping, ValueMapPostingSource_clear_mappings, 
    ValueMapPostingSource_set_default_weight, ValueMapPostingSource_swiginit, 
    ValueMapPostingSource_swigregister, ValuePostingSource_swiginit, 
    ValuePostingSource_swigregister, ValueRangeProcessor___call__, 
    ValueRangeProcessor_swiginit, ValueRangeProcessor_swigregister, 
    ValueSetMatchDecider_add_value, ValueSetMatchDecider_remove_value, 
    ValueSetMatchDecider_swiginit, ValueSetMatchDecider_swigregister, 
    ValueWeightPostingSource_swiginit, ValueWeightPostingSource_swigregister, 
    Weight_get_maxextra, Weight_get_maxpart, Weight_get_sumextra, 
    Weight_get_sumpart, Weight_name, Weight_swigregister, 
    WritableDatabase___str__, WritableDatabase_add_document, 
    WritableDatabase_add_spelling, WritableDatabase_add_synonym, 
    WritableDatabase_begin_transaction, WritableDatabase_cancel_transaction, 
    WritableDatabase_clear_synonyms, WritableDatabase_commit, 
    WritableDatabase_commit_transaction, WritableDatabase_delete_document, 
    WritableDatabase_flush, WritableDatabase_remove_spelling, 
    WritableDatabase_remove_synonym, WritableDatabase_replace_document, 
    WritableDatabase_set_metadata, WritableDatabase_swiginit, 
    WritableDatabase_swigregister, __eq__, __ne__, brass_open, chert_open, 
    delete_AssertionError, delete_BM25Weight, delete_BoolWeight, 
    delete_Compactor, delete_Database, delete_DatabaseCorruptError, 
    delete_DatabaseCreateError, delete_DatabaseError, 
    delete_DatabaseLockError, delete_DatabaseModifiedError, 
    delete_DatabaseOpeningError, delete_DatabaseVersionError, 
    delete_DateValueRangeProcessor, delete_DecreasingValueWeightPostingSource, 
    delete_DocNotFoundError, delete_Document, delete_ESet, 
    delete_ESetIterator, delete_Enquire, delete_Error, delete_ExpandDecider, 
    delete_FeatureUnavailableError, delete_FixedWeightPostingSource, 
    delete_InternalError, delete_InvalidArgumentError, 
    delete_InvalidOperationError, delete_KeyMaker, delete_LogicError, 
    delete_MSet, delete_MSetIterator, delete_MatchDecider, delete_MatchSpy, 
    delete_MultiValueKeyMaker, delete_MultiValueSorter, delete_NetworkError, 
    delete_NetworkTimeoutError, delete_NumberValueRangeProcessor, 
    delete_PositionIterator, delete_PostingIterator, delete_PostingSource, 
    delete_Query, delete_QueryParser, delete_QueryParserError, delete_RSet, 
    delete_RangeError, delete_Registry, delete_RuntimeError, 
    delete_SerialisationError, delete_SimpleStopper, delete_Sorter, 
    delete_Stem, delete_StemImplementation, delete_Stopper, 
    delete_StringValueRangeProcessor, delete_SwigPyIterator, 
    delete_TermGenerator, delete_TermIterator, delete_TradWeight, 
    delete_UnimplementedError, delete_ValueCountMatchSpy, 
    delete_ValueIterator, delete_ValueMapPostingSource, 
    delete_ValuePostingSource, delete_ValueRangeProcessor, 
    delete_ValueSetMatchDecider, delete_ValueWeightPostingSource, 
    delete_Weight, delete_WritableDatabase, disown_Compactor, 
    disown_ExpandDecider, disown_KeyMaker, disown_MatchDecider, 
    disown_MatchSpy, disown_PostingSource, disown_StemImplementation, 
    disown_Stopper, disown_ValueRangeProcessor, flint_open, inmemory_open, 
    major_version, minor_version, new_AssertionError, new_BM25Weight, 
    new_BoolWeight, new_Compactor, new_Database, new_DatabaseCorruptError, 
    new_DatabaseCreateError, new_DatabaseError, new_DatabaseLockError, 
    new_DatabaseModifiedError, new_DatabaseOpeningError, 
    new_DatabaseVersionError, new_DateValueRangeProcessor, 
    new_DecreasingValueWeightPostingSource, new_DocNotFoundError, 
    new_Document, new_ESet, new_ESetIterator, new_Enquire, new_ExpandDecider, 
    new_FeatureUnavailableError, new_FixedWeightPostingSource, 
    new_InternalError, new_InvalidArgumentError, new_InvalidOperationError, 
    new_KeyMaker, new_MSet, new_MSetIterator, new_MatchDecider, new_MatchSpy, 
    new_MultiValueKeyMaker, new_MultiValueSorter, new_NetworkError, 
    new_NetworkTimeoutError, new_NumberValueRangeProcessor, 
    new_PositionIterator, new_PostingIterator, new_PostingSource, new_Query, 
    new_QueryParser, new_QueryParserError, new_RSet, new_RangeError, 
    new_Registry, new_SerialisationError, new_SimpleStopper, new_Stem, 
    new_StemImplementation, new_Stopper, new_StringValueRangeProcessor, 
    new_TermGenerator, new_TermIterator, new_TradWeight, 
    new_UnimplementedError, new_ValueCountMatchSpy, new_ValueIterator, 
    new_ValueMapPostingSource, new_ValuePostingSource, 
    new_ValueRangeProcessor, new_ValueSetMatchDecider, 
    new_ValueWeightPostingSource, new_WritableDatabase, open_stub, 
    remote_open, remote_open_writable, revision, sortable_serialise, 
    sortable_unserialise, version_string)


# Variables with simple values

BAD_VALUENO = 4294967295L

Compactor_FULL = 1
Compactor_FULLER = 2
Compactor_STANDARD = 0

DB_CREATE = 2

DB_CREATE_OR_OPEN = 1
DB_CREATE_OR_OVERWRITE = 3

DB_OPEN = 4

Enquire_ASCENDING = 1
Enquire_DESCENDING = 0

Enquire_DONT_CARE = 2

Enquire_INCLUDE_QUERY_TERMS = 1

Enquire_USE_EXACT_TERMFREQ = 2

ESET_TNAME = 0
ESET_WT = 1

MSET_DID = 0
MSET_DOCUMENT = 4
MSET_PERCENT = 3
MSET_RANK = 2
MSET_WT = 1

QueryParser_FLAG_AUTO_MULTIWORD_SYNONYMS = 1536

QueryParser_FLAG_AUTO_SYNONYMS = 512

QueryParser_FLAG_BOOLEAN = 1

QueryParser_FLAG_BOOLEAN_ANY_CASE = 8

QueryParser_FLAG_CJK_NGRAM = 2048

QueryParser_FLAG_DEFAULT = 7
QueryParser_FLAG_LOVEHATE = 4
QueryParser_FLAG_PARTIAL = 64
QueryParser_FLAG_PHRASE = 2

QueryParser_FLAG_PURE_NOT = 32

QueryParser_FLAG_SPELLING_CORRECTION = 128

QueryParser_FLAG_SYNONYM = 256
QueryParser_FLAG_WILDCARD = 16

QueryParser_STEM_ALL = 2

QueryParser_STEM_ALL_Z = 3

QueryParser_STEM_NONE = 0
QueryParser_STEM_SOME = 1

Query_OP_AND = 0

Query_OP_AND_MAYBE = 4
Query_OP_AND_NOT = 2

Query_OP_ELITE_SET = 10

Query_OP_FILTER = 5
Query_OP_NEAR = 6
Query_OP_OR = 1
Query_OP_PHRASE = 7

Query_OP_SCALE_WEIGHT = 9

Query_OP_SYNONYM = 13

Query_OP_VALUE_GE = 11
Query_OP_VALUE_LE = 12
Query_OP_VALUE_RANGE = 8

Query_OP_XOR = 3

TermGenerator_FLAG_CJK_NGRAM = 2048

TermGenerator_FLAG_SPELLING = 128

TermGenerator_STEM_ALL = 2

TermGenerator_STEM_ALL_Z = 3

TermGenerator_STEM_NONE = 0
TermGenerator_STEM_SOME = 1

# no functions
# no classes
