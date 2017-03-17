# encoding: utf-8
# module webkit.webkit
# from /usr/lib/python2.7/dist-packages/webkit/webkit.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gtk as __gtk


# Variables with simple values

DOWNLOAD_ERROR_CANCELLED_BY_USER = 0

DOWNLOAD_ERROR_DESTINATION = 1
DOWNLOAD_ERROR_NETWORK = 2

DOWNLOAD_STATUS_CANCELLED = 2
DOWNLOAD_STATUS_CREATED = 0
DOWNLOAD_STATUS_ERROR = -1
DOWNLOAD_STATUS_FINISHED = 3
DOWNLOAD_STATUS_STARTED = 1

EDITING_BEHAVIOR_MAC = 0
EDITING_BEHAVIOR_UNIX = 2
EDITING_BEHAVIOR_WINDOWS = 1

LOAD_COMMITTED = 1
LOAD_FAILED = 4
LOAD_FINISHED = 2

LOAD_FIRST_VISUALLY_NON_EMPTY_LAYOUT = 3

LOAD_PROVISIONAL = 0

NAVIGATION_RESPONSE_ACCEPT = 0
NAVIGATION_RESPONSE_DOWNLOAD = 2
NAVIGATION_RESPONSE_IGNORE = 1

NETWORK_ERROR_CANCELLED = 302
NETWORK_ERROR_FAILED = 399

NETWORK_ERROR_FILE_DOES_NOT_EXIST = 303

NETWORK_ERROR_TRANSPORT = 300

NETWORK_ERROR_UNKNOWN_PROTOCOL = 301

PLUGIN_ERROR_CANNOT_FIND_PLUGIN = 200

PLUGIN_ERROR_CANNOT_LOAD_PLUGIN = 201

PLUGIN_ERROR_CONNECTION_CANCELLED = 203

PLUGIN_ERROR_FAILED = 299

PLUGIN_ERROR_JAVA_UNAVAILABLE = 202

PLUGIN_ERROR_WILL_HANDLE_LOAD = 204

POLICY_ERROR_CANNOT_SHOW_MIME_TYPE = 100

POLICY_ERROR_CANNOT_SHOW_URL = 101

POLICY_ERROR_CANNOT_USE_RESTRICTED_PORT = 103

POLICY_ERROR_FAILED = 199

POLICY_ERROR_FRAME_LOAD_INTERRUPTED_BY_POLICY_CHANGE = 102

WEB_NAVIGATION_REASON_BACK_FORWARD = 2

WEB_NAVIGATION_REASON_FORM_RESUBMITTED = 4
WEB_NAVIGATION_REASON_FORM_SUBMITTED = 1

WEB_NAVIGATION_REASON_LINK_CLICKED = 0

WEB_NAVIGATION_REASON_OTHER = 5
WEB_NAVIGATION_REASON_RELOAD = 3

WEB_VIEW_TARGET_INFO_HTML = 0
WEB_VIEW_TARGET_INFO_IMAGE = 2

WEB_VIEW_TARGET_INFO_NETSCAPE_URL = 4

WEB_VIEW_TARGET_INFO_TEXT = 1

WEB_VIEW_TARGET_INFO_URI_LIST = 3

# functions

def get_default_web_database_quota(*args, **kwargs): # real signature unknown
    pass

def get_web_database_directory_path(*args, **kwargs): # real signature unknown
    pass

def remove_all_web_databases(*args, **kwargs): # real signature unknown
    pass

def set_default_web_database_quota(*args, **kwargs): # real signature unknown
    pass

def set_web_database_directory_path(*args, **kwargs): # real signature unknown
    pass

# classes

class Download(__gobject__gobject.GObject):
    """
    Object WebKitDownload
    
    Signals from WebKitDownload:
      error (gint, gint, gchararray) -> gboolean
    
    Properties from WebKitDownload:
      network-request -> WebKitNetworkRequest: Network Request
        The network request for the URI that should be downloaded
      destination-uri -> gchararray: Destination URI
        The destination URI where to save the file
      suggested-filename -> gchararray: Suggested Filename
        The filename suggested as default when saving
      progress -> gdouble: Progress
        Determines the current progress of the download
      status -> WebKitDownloadStatus: Status
        Determines the current status of the download
      current-size -> guint64: Current Size
        The length of the data already downloaded
      total-size -> guint64: Total Size
        The total size of the file
      network-response -> WebKitNetworkResponse: Network Response
        The network response for the URI that should be downloaded
    
    Signals from GObject:
      notify (GParam)
    """
    def cancel(self, *args, **kwargs): # real signature unknown
        pass

    def get_current_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_destination_uri(self, *args, **kwargs): # real signature unknown
        pass

    def get_elapsed_time(self, *args, **kwargs): # real signature unknown
        pass

    def get_network_request(self, *args, **kwargs): # real signature unknown
        pass

    def get_progress(self, *args, **kwargs): # real signature unknown
        pass

    def get_status(self, *args, **kwargs): # real signature unknown
        pass

    def get_suggested_filename(self, *args, **kwargs): # real signature unknown
        pass

    def get_total_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_uri(self, *args, **kwargs): # real signature unknown
        pass

    def set_destination_uri(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class DownloadError(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is ''


class DownloadStatus(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        -1: -1,
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }
    __gtype__ = None # (!) real value is ''


class EditingBehavior(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is ''


class LoadStatus(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }
    __gtype__ = None # (!) real value is ''


class NavigationResponse(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is ''


class NetworkError(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        300: 300,
        301: 301,
        302: 302,
        303: 303,
        399: 399,
    }
    __gtype__ = None # (!) real value is ''


class NetworkRequest(__gobject__gobject.GObject):
    """
    Object WebKitNetworkRequest
    
    Properties from WebKitNetworkRequest:
      uri -> gchararray: URI
        The URI to which the request will be made.
      message -> SoupMessage: Message
        The SoupMessage that backs the request.
    
    Signals from GObject:
      notify (GParam)
    """
    def get_uri(self, *args, **kwargs): # real signature unknown
        pass

    def set_uri(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class NetworkResponse(__gobject__gobject.GObject):
    """
    Object WebKitNetworkResponse
    
    Properties from WebKitNetworkResponse:
      uri -> gchararray: URI
        The URI to which the response will be made.
      message -> SoupMessage: Message
        The SoupMessage that backs the response.
      suggested-filename -> gchararray: Suggested filename
        The suggested filename for the response.
    
    Signals from GObject:
      notify (GParam)
    """
    def get_uri(self, *args, **kwargs): # real signature unknown
        pass

    def set_uri(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class PluginError(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        200: 200,
        201: 201,
        202: 202,
        203: 203,
        204: 204,
        299: 299,
    }
    __gtype__ = None # (!) real value is ''


class PolicyError(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        100: 100,
        101: 101,
        102: 102,
        103: 103,
        199: 199,
    }
    __gtype__ = None # (!) real value is ''


class SecurityOrigin(__gobject__gobject.GObject):
    """
    Object WebKitSecurityOrigin
    
    Properties from WebKitSecurityOrigin:
      protocol -> gchararray: Protocol
        The protocol of the security origin
      host -> gchararray: Host
        The host of the security origin
      port -> guint: Port
        The port of the security origin
      web-database-usage -> guint64: Web Database Usage
        The cumulative size of all web databases in the security origin
      web-database-quota -> guint64: Web Database Quota
        The web database quota of the security origin in bytes
    
    Signals from GObject:
      notify (GParam)
    """
    def get_all_web_databases(self, *args, **kwargs): # real signature unknown
        pass

    def get_host(self, *args, **kwargs): # real signature unknown
        pass

    def get_port(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol(self, *args, **kwargs): # real signature unknown
        pass

    def get_web_database_quota(self, *args, **kwargs): # real signature unknown
        pass

    def get_web_database_usage(self, *args, **kwargs): # real signature unknown
        pass

    def set_web_database_quota(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class WebBackForwardList(__gobject__gobject.GObject):
    """
    Object WebKitWebBackForwardList
    
    Signals from GObject:
      notify (GParam)
    """
    def add_item(self, *args, **kwargs): # real signature unknown
        pass

    def contains_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_back_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_back_length(self, *args, **kwargs): # real signature unknown
        pass

    def get_back_list_with_limit(self, *args, **kwargs): # real signature unknown
        pass

    def get_current_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_forward_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_forward_length(self, *args, **kwargs): # real signature unknown
        pass

    def get_forward_list_with_limit(self, *args, **kwargs): # real signature unknown
        pass

    def get_limit(self, *args, **kwargs): # real signature unknown
        pass

    def get_nth_item(self, *args, **kwargs): # real signature unknown
        pass

    def go_back(self, *args, **kwargs): # real signature unknown
        pass

    def go_forward(self, *args, **kwargs): # real signature unknown
        pass

    def go_to_item(self, *args, **kwargs): # real signature unknown
        pass

    def set_limit(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class WebDatabase(__gobject__gobject.GObject):
    """
    Object WebKitWebDatabase
    
    Properties from WebKitWebDatabase:
      security-origin -> WebKitSecurityOrigin: Security Origin
        The security origin of the database
      name -> gchararray: Name
        The name of the Web Database database
      display-name -> gchararray: Display Name
        The display name of the Web Storage database
      expected-size -> guint64: Expected Size
        The expected size of the Web Database database
      size -> guint64: Size
        The current size of the Web Database database
      filename -> gchararray: Filename
        The absolute filename of the Web Storage database
    
    Signals from GObject:
      notify (GParam)
    """
    def get_display_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_expected_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_filename(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_security_origin(self, *args, **kwargs): # real signature unknown
        pass

    def get_size(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class WebDataSource(__gobject__gobject.GObject):
    """
    Object WebKitWebDataSource
    
    Signals from GObject:
      notify (GParam)
    """
    def get_data(self, *args, **kwargs): # real signature unknown
        pass

    def get_encoding(self, *args, **kwargs): # real signature unknown
        pass

    def get_initial_request(self, *args, **kwargs): # real signature unknown
        pass

    def get_main_resource(self, *args, **kwargs): # real signature unknown
        pass

    def get_request(self, *args, **kwargs): # real signature unknown
        pass

    def get_unreachable_uri(self, *args, **kwargs): # real signature unknown
        pass

    def get_web_frame(self, *args, **kwargs): # real signature unknown
        pass

    def is_loading(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class WebFrame(__gobject__gobject.GObject):
    """
    Object WebKitWebFrame
    
    Signals from WebKitWebFrame:
      cleared ()
      load-committed ()
      title-changed (gchararray)
      hovering-over-link (gchararray, gchararray)
      scrollbars-policy-changed () -> gboolean
      resource-request-starting (WebKitWebResource, WebKitNetworkRequest, WebKitNetworkResponse)
      resource-response-received (WebKitWebResource, WebKitNetworkResponse)
      resource-load-finished (WebKitWebResource)
      resource-content-length-received (WebKitWebResource, gint)
      resource-load-failed (WebKitWebResource, gpointer)
      insecure-content-run (WebKitSecurityOrigin, gchararray)
    
    Properties from WebKitWebFrame:
      name -> gchararray: Name
        The name of the frame
      title -> gchararray: Title
        The document title of the frame
      uri -> gchararray: URI
        The current URI of the contents displayed by the frame
      load-status -> WebKitLoadStatus: Load Status
        Determines the current status of the load
      horizontal-scrollbar-policy -> GtkPolicyType: Horizontal Scrollbar Policy
        Determines the current policy for the horizontal scrollbar of the frame.
      vertical-scrollbar-policy -> GtkPolicyType: Vertical Scrollbar Policy
        Determines the current policy for the vertical scrollbar of the frame.
    
    Signals from GObject:
      notify (GParam)
    """
    def find_frame(self, *args, **kwargs): # real signature unknown
        pass

    def get_data_source(self, *args, **kwargs): # real signature unknown
        pass

    def get_global_context(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_network_response(self, *args, **kwargs): # real signature unknown
        pass

    def get_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_provisional_data_source(self, *args, **kwargs): # real signature unknown
        pass

    def get_security_origin(self, *args, **kwargs): # real signature unknown
        pass

    def get_title(self, *args, **kwargs): # real signature unknown
        pass

    def get_uri(self, *args, **kwargs): # real signature unknown
        pass

    def get_web_view(self, *args, **kwargs): # real signature unknown
        pass

    def load_request(self, *args, **kwargs): # real signature unknown
        pass

    def load_string(self, *args, **kwargs): # real signature unknown
        pass

    def load_uri(self, *args, **kwargs): # real signature unknown
        pass

    def print_(self, *args, **kwargs): # real signature unknown
        pass

    def print_full(self, *args, **kwargs): # real signature unknown
        pass

    def reload(self, *args, **kwargs): # real signature unknown
        pass

    def stop_loading(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class WebHistoryItem(__gobject__gobject.GObject):
    """
    Object WebKitWebHistoryItem
    
    Properties from WebKitWebHistoryItem:
      title -> gchararray: Title
        The title of the history item
      alternate-title -> gchararray: Alternate Title
        The alternate title of the history item
      uri -> gchararray: URI
        The URI of the history item
      original-uri -> gchararray: Original URI
        The original URI of the history item
      last-visited-time -> gdouble: Last visited Time
        The time at which the history item was last visited
    
    Signals from GObject:
      notify (GParam)
    """
    def get_alternate_title(self, *args, **kwargs): # real signature unknown
        pass

    def get_last_visited_time(self, *args, **kwargs): # real signature unknown
        pass

    def get_original_uri(self, *args, **kwargs): # real signature unknown
        pass

    def get_title(self, *args, **kwargs): # real signature unknown
        pass

    def get_uri(self, *args, **kwargs): # real signature unknown
        pass

    def set_alternate_title(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class WebInspector(__gobject__gobject.GObject):
    """
    Object WebKitWebInspector
    
    Signals from WebKitWebInspector:
      inspect-web-view (WebKitWebView) -> WebKitWebView
      show-window () -> gboolean
      attach-window () -> gboolean
      detach-window () -> gboolean
      close-window () -> gboolean
      finished ()
    
    Properties from WebKitWebInspector:
      web-view -> WebKitWebView: Web View
        The Web View that renders the Web Inspector itself
      inspected-uri -> gchararray: Inspected URI
        The URI that is currently being inspected
      javascript-profiling-enabled -> gboolean: Enable JavaScript profiling
        Profile the executed JavaScript.
      timeline-profiling-enabled -> gboolean: Enable Timeline profiling
        Profile the WebCore instrumentation.
    
    Signals from GObject:
      notify (GParam)
    """
    def get_inspected_uri(self, *args, **kwargs): # real signature unknown
        pass

    def get_web_view(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class WebNavigationAction(__gobject__gobject.GObject):
    """
    Object WebKitWebNavigationAction
    
    Properties from WebKitWebNavigationAction:
      reason -> WebKitWebNavigationReason: Reason
        The reason why this navigation is occurring
      original-uri -> gchararray: Original URI
        The URI that was requested as the target for the navigation
      button -> gint: Button
        The button used to click
      modifier-state -> gint: Modifier state
        A bitmask representing the state of the modifier keys
      target-frame -> gchararray: Target frame
        The target frame for the navigation
    
    Signals from GObject:
      notify (GParam)
    """
    def get_button(self, *args, **kwargs): # real signature unknown
        pass

    def get_modifier_state(self, *args, **kwargs): # real signature unknown
        pass

    def get_original_uri(self, *args, **kwargs): # real signature unknown
        pass

    def get_reason(self, *args, **kwargs): # real signature unknown
        pass

    def set_original_uri(self, *args, **kwargs): # real signature unknown
        pass

    def set_reason(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class WebNavigationReason(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
    }
    __gtype__ = None # (!) real value is ''


class WebPolicyDecision(__gobject__gobject.GObject):
    """
    Object WebKitWebPolicyDecision
    
    Signals from GObject:
      notify (GParam)
    """
    def download(self, *args, **kwargs): # real signature unknown
        pass

    def ignore(self, *args, **kwargs): # real signature unknown
        pass

    def use(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class WebResource(__gobject__gobject.GObject):
    """
    Object WebKitWebResource
    
    Signals from WebKitWebResource:
      response-received (WebKitNetworkResponse)
      load-failed (gpointer)
      load-finished ()
      content-length-received (gint)
    
    Properties from WebKitWebResource:
      uri -> gchararray: URI
        The URI of the resource
      mime-type -> gchararray: MIME Type
        The MIME type of the resource
      encoding -> gchararray: Encoding
        The text encoding name of the resource
      frame-name -> gchararray: Frame Name
        The frame name of the resource
    
    Signals from GObject:
      notify (GParam)
    """
    def get_data(self, *args, **kwargs): # real signature unknown
        pass

    def get_encoding(self, *args, **kwargs): # real signature unknown
        pass

    def get_frame_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_mime_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_uri(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class WebSettings(__gobject__gobject.GObject):
    """
    Object WebKitWebSettings
    
    Properties from WebKitWebSettings:
      default-encoding -> gchararray: Default Encoding
        The default encoding used to display text.
      cursive-font-family -> gchararray: Cursive Font Family
        The default Cursive font family used to display text.
      default-font-family -> gchararray: Default Font Family
        The default font family used to display text.
      fantasy-font-family -> gchararray: Fantasy Font Family
        The default Fantasy font family used to display text.
      monospace-font-family -> gchararray: Monospace Font Family
        The default font family used to display monospace text.
      sans-serif-font-family -> gchararray: Sans Serif Font Family
        The default Sans Serif font family used to display text.
      serif-font-family -> gchararray: Serif Font Family
        The default Serif font family used to display text.
      default-font-size -> gint: Default Font Size
        The default font size used to display text.
      default-monospace-font-size -> gint: Default Monospace Font Size
        The default font size used to display monospace text.
      minimum-font-size -> gint: Minimum Font Size
        The minimum font size used to display text.
      minimum-logical-font-size -> gint: Minimum Logical Font Size
        The minimum logical font size used to display text.
      enforce-96-dpi -> gboolean: Enforce 96 DPI
        Enforce a resolution of 96 DPI
      auto-load-images -> gboolean: Auto Load Images
        Load images automatically.
      auto-shrink-images -> gboolean: Auto Shrink Images
        Automatically shrink standalone images to fit.
      respect-image-orientation -> gboolean: Respect Image Orientation
        Whether WebKit should respect image orientation.
      print-backgrounds -> gboolean: Print Backgrounds
        Whether background images should be printed.
      enable-scripts -> gboolean: Enable Scripts
        Enable embedded scripting languages.
      enable-plugins -> gboolean: Enable Plugins
        Enable embedded plugin objects.
      resizable-text-areas -> gboolean: Resizable Text Areas
        Whether text areas are resizable.
      user-stylesheet-uri -> gchararray: User Stylesheet URI
        The URI of a stylesheet that is applied to every page.
      zoom-step -> gfloat: Zoom Stepping Value
        The value by which the zoom level is changed when zooming in or out.
      enable-developer-extras -> gboolean: Enable Developer Extras
        Enables special extensions that help developers
      enable-private-browsing -> gboolean: Enable Private Browsing
        Enables private browsing mode
      enable-spell-checking -> gboolean: Enable Spell Checking
        Enables spell checking while typing
      spell-checking-languages -> gchararray: Languages to use for spell checking
        Comma separated list of languages to use for spell checking
      enable-caret-browsing -> gboolean: Enable Caret Browsing
        Whether to enable accessibility enhanced keyboard navigation
      enable-html5-database -> gboolean: Enable HTML5 Database
        Whether to enable HTML5 database support
      enable-html5-local-storage -> gboolean: Enable HTML5 Local Storage
        Whether to enable HTML5 Local Storage support
      html5-local-storage-database-path -> gchararray: Local Storage Database Path
        The path to where HTML5 Local Storage databases are stored.
      enable-xss-auditor -> gboolean: Enable XSS Auditor
        Whether to enable the XSS auditor
      enable-spatial-navigation -> gboolean: Enable Spatial Navigation
        Whether to enable Spatial Navigation
      enable-frame-flattening -> gboolean: Enable Frame Flattening
        Whether to enable Frame Flattening
      user-agent -> gchararray: User Agent
        The User-Agent string used by WebKitGtk
      javascript-can-open-windows-automatically -> gboolean: JavaScript can open windows automatically
        Whether JavaScript can open windows automatically
      javascript-can-access-clipboard -> gboolean: JavaScript can access Clipboard
        Whether JavaScript can access Clipboard
      enable-offline-web-application-cache -> gboolean: Enable offline web application cache
        Whether to enable offline web application cache
      editing-behavior -> WebKitEditingBehavior: Editing behavior
        The behavior mode to use in editing mode
      enable-universal-access-from-file-uris -> gboolean: Enable universal access from file URIs
        Whether to allow universal access from file URIs
      enable-file-access-from-file-uris -> gboolean: Enable file access from file URIs
        Controls file access for file:// URIs.
      enable-dom-paste -> gboolean: Enable DOM paste
        Whether to enable DOM paste
      tab-key-cycles-through-elements -> gboolean: Tab key cycles through elements
        Whether the tab key cycles through elements on the page.
      enable-default-context-menu -> gboolean: Enable Default Context Menu
        Enables the handling of right-clicks for the creation of the default context menu
      enable-site-specific-quirks -> gboolean: Enable Site Specific Quirks
        Enables the site-specific compatibility workarounds
      enable-page-cache -> gboolean: Enable page cache
        Whether the page cache should be used
      auto-resize-window -> gboolean: Auto Resize Window
        Automatically resize the toplevel window when a page requests it
      enable-java-applet -> gboolean: Enable Java Applet
        Whether Java Applet support through <applet> should be enabled
      enable-hyperlink-auditing -> gboolean: Enable Hyperlink Auditing
        Whether <a ping> should be able to send pings
      enable-fullscreen -> gboolean: Enable Fullscreen
        Whether to enable the Javascript Fullscreen API
      enable-dns-prefetching -> gboolean: WebKit prefetches domain names
        Whether WebKit prefetches domain names
      enable-webgl -> gboolean: Enable WebGL
        Whether WebGL content should be rendered
      enable-media-stream -> gboolean: Enable Media Stream
        Whether Media Stream should be enabled
      enable-webaudio -> gboolean: Enable WebAudio
        Whether WebAudio content should be handled
      enable-accelerated-compositing -> gboolean: Enable accelerated compositing
        Whether accelerated compositing should be enabled
      enable-smooth-scrolling -> gboolean: Enable smooth scrolling
        Whether to enable smooth scrolling
      media-playback-requires-user-gesture -> gboolean: Media playback requires user gesture
        Whether media playback requires user gesture
      media-playback-allows-inline -> gboolean: Media playback allows inline
        Whether media playback allows inline
      enable-running-of-insecure-content -> gboolean: Enable running of insecure content
        Whether non-HTTPS resources can run on HTTPS pages.
      enable-display-of-insecure-content -> gboolean: Enable display of insecure content
        Whether non-HTTPS resources can display on HTTPS pages.
      enable-mediasource -> gboolean: Enable MediaSource
        Whether MediaSource should be enabled.
    
    Signals from GObject:
      notify (GParam)
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class WebView(__gtk.Container):
    """
    Object WebKitWebView
    
    Signals from WebKitWebView:
      icon-loaded (gchararray)
      load-committed (WebKitWebFrame)
      title-changed (WebKitWebFrame, gchararray)
      hovering-over-link (gchararray, gchararray)
      resource-request-starting (WebKitWebFrame, WebKitWebResource, WebKitNetworkRequest, WebKitNetworkResponse)
      resource-response-received (WebKitWebFrame, WebKitWebResource, WebKitNetworkResponse)
      resource-load-finished (WebKitWebFrame, WebKitWebResource)
      resource-content-length-received (WebKitWebFrame, WebKitWebResource, gint)
      resource-load-failed (WebKitWebFrame, WebKitWebResource, GError)
      load-finished (WebKitWebFrame)
      create-web-view (WebKitWebFrame) -> WebKitWebView
      web-view-ready () -> gboolean
      close-web-view () -> gboolean
      navigation-requested (WebKitWebFrame, WebKitNetworkRequest) -> WebKitNavigationResponse
      new-window-policy-decision-requested (WebKitWebFrame, WebKitNetworkRequest, WebKitWebNavigationAction, WebKitWebPolicyDecision) -> gboolean
      navigation-policy-decision-requested (WebKitWebFrame, WebKitNetworkRequest, WebKitWebNavigationAction, WebKitWebPolicyDecision) -> gboolean
      mime-type-policy-decision-requested (WebKitWebFrame, WebKitNetworkRequest, gchararray, WebKitWebPolicyDecision) -> gboolean
      window-object-cleared (WebKitWebFrame, gpointer, gpointer)
      download-requested (WebKitDownload) -> gboolean
      load-started (WebKitWebFrame)
      load-progress-changed (gint)
      load-error (WebKitWebFrame, gchararray, GError) -> gboolean
      onload-event (WebKitWebFrame)
      populate-popup (GtkMenu)
      print-requested (WebKitWebFrame) -> gboolean
      status-bar-text-changed (gchararray)
      console-message (gchararray, gint, gchararray) -> gboolean
      script-alert (WebKitWebFrame, gchararray) -> gboolean
      script-confirm (WebKitWebFrame, gchararray, gpointer) -> gboolean
      script-prompt (WebKitWebFrame, gchararray, gchararray, gpointer) -> gboolean
      select-all ()
      cut-clipboard ()
      copy-clipboard ()
      paste-clipboard ()
      undo ()
      redo ()
      move-cursor (GtkMovementStep, gint) -> gboolean
      create-plugin-widget (gchararray, gchararray, GHashTable) -> GtkWidget
      database-quota-exceeded (GObject, GObject)
      geolocation-policy-decision-requested (WebKitWebFrame, WebKitGeolocationPolicyDecision) -> gboolean
      geolocation-policy-decision-cancelled (WebKitWebFrame)
      document-load-finished (WebKitWebFrame)
      frame-created (WebKitWebFrame)
      run-file-chooser (WebKitFileChooserRequest) -> gboolean
      should-begin-editing (WebKitDOMRange) -> gboolean
      should-end-editing (WebKitDOMRange) -> gboolean
      should-insert-node (WebKitDOMNode, WebKitDOMRange, WebKitInsertAction) -> gboolean
      should-insert-text (gchararray, WebKitDOMRange, WebKitInsertAction) -> gboolean
      should-delete-range (WebKitDOMRange) -> gboolean
      should-show-delete-interface-for-element (WebKitDOMHTMLElement) -> gboolean
      should-change-selected-range (WebKitDOMRange, WebKitDOMRange, WebKitSelectionAffinity, gboolean) -> gboolean
      should-apply-style (WebKitDOMCSSStyleDeclaration, WebKitDOMRange) -> gboolean
      editing-began ()
      user-changed-contents ()
      editing-ended ()
      selection-changed ()
      viewport-attributes-recompute-requested (WebKitViewportAttributes)
      viewport-attributes-changed (WebKitViewportAttributes)
      entering-fullscreen (WebKitDOMHTMLElement) -> gboolean
      leaving-fullscreen (WebKitDOMHTMLElement) -> gboolean
      context-menu (GtkWidget, WebKitHitTestResult, gboolean) -> gboolean
      set-scroll-adjustments (GtkAdjustment, GtkAdjustment)
    
    Properties from WebKitWebView:
      title -> gchararray: Title
        Returns the @web_view's document title
      uri -> gchararray: URI
        Returns the current URI of the contents displayed by the @web_view
      copy-target-list -> GtkTargetList: Copy target list
        The list of targets this web view supports for clipboard copying
      paste-target-list -> GtkTargetList: Paste target list
        The list of targets this web view supports for clipboard pasting
      editable -> gboolean: Editable
        Whether content can be modified by the user
      settings -> WebKitWebSettings: Settings
        An associated WebKitWebSettings instance
      web-inspector -> WebKitWebInspector: Web Inspector
        The associated WebKitWebInspector instance
      viewport-attributes -> WebKitViewportAttributes: Viewport Attributes
        The associated WebKitViewportAttributes instance
      window-features -> WebKitWebWindowFeatures: Window Features
        An associated WebKitWebWindowFeatures instance
      transparent -> gboolean: Transparent
        Whether content has a transparent background
      zoom-level -> gfloat: Zoom level
        The level of zoom of the content
      full-content-zoom -> gboolean: Full content zoom
        Whether the full content is scaled when zooming
      load-status -> WebKitLoadStatus: Load Status
        Determines the current status of the load
      progress -> gdouble: Progress
        Determines the current progress of the load
      encoding -> gchararray: Encoding
        The default encoding of the web view
      custom-encoding -> gchararray: Custom Encoding
        The custom encoding of the web view
      icon-uri -> gchararray: Icon URI
        The URI for the favicon for the #WebKitWebView.
      im-context -> GtkIMContext: IM Context
        The GtkIMMultiContext for the #WebKitWebView.
      view-mode -> WebKitWebViewViewMode: View Mode
        The view-mode media feature for the #WebKitWebView.
      self-scrolling -> gboolean: Self-scrolling
        Whether or not this WebView draws its own scrollbars.
    
    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)
    
    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container
    
    Signals from GtkWidget:
      composited-changed ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-request (GtkRequisition)
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      event (GdkEvent) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      keynav-failed (GtkDirectionType) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      expose-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      client-event (GdkEvent) -> gboolean
      no-expose-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      extension-events -> GdkExtensionMode: Extension events
        The mask that decides what kind of extension events this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      double-buffered -> gboolean: Double Buffered
        Whether or not the widget is double buffered
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def can_copy_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def can_cut_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def can_go_back(self, *args, **kwargs): # real signature unknown
        pass

    def can_go_forward(self, *args, **kwargs): # real signature unknown
        pass

    def can_paste_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def can_redo(self, *args, **kwargs): # real signature unknown
        pass

    def can_show_mime_type(self, *args, **kwargs): # real signature unknown
        pass

    def can_undo(self, *args, **kwargs): # real signature unknown
        pass

    def copy_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def cut_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def delete_selection(self, *args, **kwargs): # real signature unknown
        pass

    def execute_script(self, *args, **kwargs): # real signature unknown
        pass

    def get_back_forward_list(self, *args, **kwargs): # real signature unknown
        pass

    def get_copy_target_list(self, *args, **kwargs): # real signature unknown
        pass

    def get_custom_encoding(self, *args, **kwargs): # real signature unknown
        pass

    def get_editable(self, *args, **kwargs): # real signature unknown
        pass

    def get_encoding(self, *args, **kwargs): # real signature unknown
        pass

    def get_focused_frame(self, *args, **kwargs): # real signature unknown
        pass

    def get_full_content_zoom(self, *args, **kwargs): # real signature unknown
        pass

    def get_load_status(self, *args, **kwargs): # real signature unknown
        pass

    def get_main_frame(self, *args, **kwargs): # real signature unknown
        pass

    def get_paste_target_list(self, *args, **kwargs): # real signature unknown
        pass

    def get_progress(self, *args, **kwargs): # real signature unknown
        pass

    def get_settings(self, *args, **kwargs): # real signature unknown
        pass

    def get_title(self, *args, **kwargs): # real signature unknown
        pass

    def get_transparent(self, *args, **kwargs): # real signature unknown
        pass

    def get_view_source_mode(self, *args, **kwargs): # real signature unknown
        pass

    def get_web_inspector(self, *args, **kwargs): # real signature unknown
        pass

    def get_window_features(self, *args, **kwargs): # real signature unknown
        pass

    def get_zoom_level(self, *args, **kwargs): # real signature unknown
        pass

    def go_back(self, *args, **kwargs): # real signature unknown
        pass

    def go_back_or_forward(self, *args, **kwargs): # real signature unknown
        pass

    def go_forward(self, *args, **kwargs): # real signature unknown
        pass

    def go_to_back_forward_item(self, *args, **kwargs): # real signature unknown
        pass

    def has_selection(self, *args, **kwargs): # real signature unknown
        pass

    def load_html_string(self, *args, **kwargs): # real signature unknown
        pass

    def load_string(self, *args, **kwargs): # real signature unknown
        pass

    def load_uri(self, *args, **kwargs): # real signature unknown
        pass

    def mark_text_matches(self, *args, **kwargs): # real signature unknown
        pass

    def move_cursor(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def paste_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self, *args, **kwargs): # real signature unknown
        pass

    def reload(self, *args, **kwargs): # real signature unknown
        pass

    def reload_bypass_cache(self, *args, **kwargs): # real signature unknown
        pass

    def search_text(self, *args, **kwargs): # real signature unknown
        pass

    def select_all(self, *args, **kwargs): # real signature unknown
        pass

    def set_custom_encoding(self, *args, **kwargs): # real signature unknown
        pass

    def set_editable(self, *args, **kwargs): # real signature unknown
        pass

    def set_full_content_zoom(self, *args, **kwargs): # real signature unknown
        pass

    def set_highlight_text_matches(self, *args, **kwargs): # real signature unknown
        pass

    def set_maintains_back_forward_list(self, *args, **kwargs): # real signature unknown
        pass

    def set_settings(self, *args, **kwargs): # real signature unknown
        pass

    def set_transparent(self, *args, **kwargs): # real signature unknown
        pass

    def set_view_source_mode(self, *args, **kwargs): # real signature unknown
        pass

    def set_zoom_level(self, *args, **kwargs): # real signature unknown
        pass

    def stop_loading(self, *args, **kwargs): # real signature unknown
        pass

    def undo(self, *args, **kwargs): # real signature unknown
        pass

    def unmark_text_matches(self, *args, **kwargs): # real signature unknown
        pass

    def zoom_in(self, *args, **kwargs): # real signature unknown
        pass

    def zoom_out(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


class WebViewTargetInfo(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }
    __gtype__ = None # (!) real value is ''


class WindowFeatures(__gobject__gobject.GObject):
    """
    Object WebKitWebWindowFeatures
    
    Properties from WebKitWebWindowFeatures:
      x -> gint: x
        The starting x position of the window on the screen.
      y -> gint: y
        The starting y position of the window on the screen.
      width -> gint: Width
        The width of the window on the screen.
      height -> gint: Height
        The height of the window on the screen.
      toolbar-visible -> gboolean: Toolbar Visible
        Controls whether the toolbar should be visible for the window.
      statusbar-visible -> gboolean: Statusbar Visible
        Controls whether the statusbar should be visible for the window.
      scrollbar-visible -> gboolean: Scrollbar Visible
        Controls whether the scrollbars should be visible for the window.
      menubar-visible -> gboolean: Menubar Visible
        Controls whether the menubar should be visible for the window.
      locationbar-visible -> gboolean: Locationbar Visible
        Controls whether the locationbar should be visible for the window.
      fullscreen -> gboolean: Fullscreen
        Controls whether window will be displayed fullscreen.
    
    Signals from GObject:
      notify (GParam)
    """
    def equal(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


