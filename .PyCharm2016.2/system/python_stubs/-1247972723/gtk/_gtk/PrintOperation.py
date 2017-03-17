# encoding: utf-8
# module gtk._gtk
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gtk/_gtk.so
# by generator 1.143
# no doc

# imports
import atk as __atk
import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject


from PrintOperationPreview import PrintOperationPreview

class PrintOperation(__gobject__gobject.GObject, PrintOperationPreview):
    """
    Object GtkPrintOperation
    
    Signals from GtkPrintOperation:
      done (GtkPrintOperationResult)
      begin-print (GtkPrintContext)
      paginate (GtkPrintContext) -> gboolean
      request-page-setup (GtkPrintContext, gint, GtkPageSetup)
      draw-page (GtkPrintContext, gint)
      end-print (GtkPrintContext)
      status-changed ()
      create-custom-widget () -> GObject
      update-custom-widget (GtkWidget, GtkPageSetup, GtkPrintSettings)
      custom-widget-apply (GtkWidget)
      preview (GtkPrintOperationPreview, GtkPrintContext, GtkWindow) -> gboolean
    
    Properties from GtkPrintOperation:
      default-page-setup -> GtkPageSetup: Default Page Setup
        The GtkPageSetup used by default
      print-settings -> GtkPrintSettings: Print Settings
        The GtkPrintSettings used for initializing the dialog
      job-name -> gchararray: Job Name
        A string used for identifying the print job.
      n-pages -> gint: Number of Pages
        The number of pages in the document.
      current-page -> gint: Current Page
        The current page in the document
      use-full-page -> gboolean: Use full page
        TRUE if the origin of the context should be at the corner of the page and not the corner of the imageable area
      track-print-status -> gboolean: Track Print Status
        TRUE if the print operation will continue to report on the print job status after the print data has been sent to the printer or print server.
      unit -> GtkUnit: Unit
        The unit in which distances can be measured in the context
      show-progress -> gboolean: Show Dialog
        TRUE if a progress dialog is shown while printing.
      allow-async -> gboolean: Allow Async
        TRUE if print process may run asynchronous.
      export-filename -> gchararray: Export filename
        Export filename
      status -> GtkPrintStatus: Status
        The status of the print operation
      status-string -> gchararray: Status String
        A human-readable description of the status
      custom-tab-label -> gchararray: Custom tab label
        Label for the tab containing custom widgets.
      embed-page-setup -> gboolean: Embed Page Setup
        TRUE if page setup combos are embedded in GtkPrintDialog
      has-selection -> gboolean: Has Selection
        TRUE if a selection exists.
      support-selection -> gboolean: Support Selection
        TRUE if the print operation will support print of selection.
      n-pages-to-print -> gint: Number of Pages To Print
        The number of pages that will be printed.
    
    Signals from GtkPrintOperationPreview:
      ready (GtkPrintContext)
      got-page-size (GtkPrintContext, GtkPageSetup)
    
    Signals from GObject:
      notify (GParam)
    """
    def cancel(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_begin_print(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_create_custom_widget(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_custom_widget_apply(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_done(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_page(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_end_print(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_paginate(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_preview(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_request_page_setup(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_status_changed(cls, *args, **kwargs): # real signature unknown
        pass

    def draw_page_finish(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_page_setup(self, *args, **kwargs): # real signature unknown
        pass

    def get_embed_page_setup(self, *args, **kwargs): # real signature unknown
        pass

    def get_error(self, *args, **kwargs): # real signature unknown
        pass

    def get_has_selection(self, *args, **kwargs): # real signature unknown
        pass

    def get_n_pages_to_print(self, *args, **kwargs): # real signature unknown
        pass

    def get_print_settings(self, *args, **kwargs): # real signature unknown
        pass

    def get_status(self, *args, **kwargs): # real signature unknown
        pass

    def get_status_string(self, *args, **kwargs): # real signature unknown
        pass

    def get_support_selection(self, *args, **kwargs): # real signature unknown
        pass

    def is_finished(self, *args, **kwargs): # real signature unknown
        pass

    def run(self, *args, **kwargs): # real signature unknown
        pass

    def set_allow_async(self, *args, **kwargs): # real signature unknown
        pass

    def set_current_page(self, *args, **kwargs): # real signature unknown
        pass

    def set_custom_tab_label(self, *args, **kwargs): # real signature unknown
        pass

    def set_default_page_setup(self, *args, **kwargs): # real signature unknown
        pass

    def set_defer_drawing(self, *args, **kwargs): # real signature unknown
        pass

    def set_embed_page_setup(self, *args, **kwargs): # real signature unknown
        pass

    def set_export_filename(self, *args, **kwargs): # real signature unknown
        pass

    def set_has_selection(self, *args, **kwargs): # real signature unknown
        pass

    def set_job_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_n_pages(self, *args, **kwargs): # real signature unknown
        pass

    def set_print_settings(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_progress(self, *args, **kwargs): # real signature unknown
        pass

    def set_support_selection(self, *args, **kwargs): # real signature unknown
        pass

    def set_track_print_status(self, *args, **kwargs): # real signature unknown
        pass

    def set_unit(self, *args, **kwargs): # real signature unknown
        pass

    def set_use_full_page(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


