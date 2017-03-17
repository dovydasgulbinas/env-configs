# encoding: utf-8
# module gio._gio
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gio/_gio.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
import gio as __gio
import glib as __glib
import gobject as __gobject
import gobject._gobject as __gobject__gobject


class AppInfo(__gobject.GInterface):
    # no doc
    def add_supports_type(self, *args, **kwargs): # real signature unknown
        pass

    def can_delete(self, *args, **kwargs): # real signature unknown
        pass

    def can_remove_supports_type(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self, *args, **kwargs): # real signature unknown
        pass

    def equal(self, *args, **kwargs): # real signature unknown
        pass

    def get_commandline(self, *args, **kwargs): # real signature unknown
        pass

    def get_description(self, *args, **kwargs): # real signature unknown
        pass

    def get_executable(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def launch(self, files=None, launch_context=None): # real signature unknown; restored from __doc__
        """
        launch (files=None, launch_context=None) -> gboolean
        
        Launches the application. Passes files to the launched application
        as arguments, using the optional launch_context to get information
        about the details of the launcher (like what screen it is on).
        On error, error will be set accordingly.
        
        Note that even if the launch is successful the application launched
        can fail to start if it runs into problems during startup.
        There is no way to detect this.
        
        Some URIs can be changed when passed through a gio.File
        (for instance unsupported uris with strange formats like mailto:),
        so if you have a textual uri you want to pass in as argument,
        consider using gio.AppInfo.launch_uris() instead.
        """
        pass

    def launch_uris(self, files=None, launch_context=None): # real signature unknown; restored from __doc__
        """
        launch_uris (files=None, launch_context=None) -> gboolean
        
        Launches the application. Passes files to the launched application
        as arguments, using the optional launch_context to get information
        about the details of the launcher (like what screen it is on).
        On error, error will be set accordingly.
        
        Note that even if the launch is successful the application launched
        can fail to start if it runs into problems during startup.
        There is no way to detect this.
        """
        pass

    def remove_supports_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_as_default_for_extension(self, *args, **kwargs): # real signature unknown
        pass

    def set_as_default_for_type(self, *args, **kwargs): # real signature unknown
        pass

    def should_show(self, *args, **kwargs): # real signature unknown
        pass

    def supports_files(self, *args, **kwargs): # real signature unknown
        pass

    def supports_uris(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __gtype__ = None # (!) real value is ''


