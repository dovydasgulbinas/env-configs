# encoding: utf-8
# module twisted.python._sendmsg
# from /usr/lib/python2.7/dist-packages/twisted/python/_sendmsg.x86_64-linux-gnu.so
# by generator 1.143
"""
Bindings for sendmsg(2), recvmsg(2), and a minimal helper for inspecting
address family of a socket.
"""
# no imports

# Variables with simple values

SCM_CREDENTIALS = 2
SCM_RIGHTS = 1
SCM_TIMESTAMP = 29

# functions

def getsockfam(*args, **kwargs): # real signature unknown
    """
    Retrieve the address family of a given socket.
    
    @param fd: The file descriptor of the socket the address family of which
        to retrieve.
    @type fd: C{int}
    
    @raise socket.error: Raised if the underlying getsockname call indicates
        an error.
    
    @return: A C{int} representing the address family of the socket.  For
        example, L{socket.AF_INET}, L{socket.AF_INET6}, or L{socket.AF_UNIX}.
    """
    pass

def recv1msg(*args, **kwargs): # real signature unknown
    """
    Wrap the C recvmsg(2) function for receiving "messages" on a socket.
    
    @param fd: The file descriptor of the socket over which to receive a message.
    @type fd: C{int}
    
    @param flags: Flags to affect how the message is sent.  See the C{MSG_}
        constants in the sendmsg(2) manual page.  By default no flags are set.
    @type flags: C{int}
    
    @param maxsize: The maximum number of bytes to receive from the socket
        using the datagram or stream mechanism.  The default maximum is 8192.
    @type maxsize: C{int}
    
    @param cmsg_size: The maximum number of bytes to receive from the socket
        outside of the normal datagram or stream mechanism.  The default maximum is 4096.
    
    @raise OverflowError: Raised if too much ancillary data is given.
    @raise socket.error: Raised if the underlying syscall indicates an error.
    
    @return: A C{tuple} of three elements: the bytes received using the
        datagram/stream mechanism, flags as an C{int} describing the data
        received, and a C{list} of C{tuples} giving ancillary received data.
    """
    pass

def send1msg(*args, **kwargs): # real signature unknown
    """
    Wrap the C sendmsg(2) function for sending "messages" on a socket.
    
    @param fd: The file descriptor of the socket over which to send a message.
    @type fd: C{int}
    
    @param data: Bytes to write to the socket.
    @type data: C{str}
    
    @param flags: Flags to affect how the message is sent.  See the C{MSG_}
        constants in the sendmsg(2) manual page.  By default no flags are set.
    @type flags: C{int}
    
    @param ancillary: Extra data to send over the socket outside of the normal
        datagram or stream mechanism.  By default no ancillary data is sent.
    @type ancillary: C{list} of C{tuple} of C{int}, C{int}, and C{str}.
    
    @raise OverflowError: Raised if too much ancillary data is given.
    @raise socket.error: Raised if the underlying syscall indicates an error.
    
    @return: The return value of the underlying syscall, if it succeeds.
    """
    pass

# no classes
