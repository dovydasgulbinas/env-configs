# encoding: utf-8
# module PyQt4.QtTest
# from /usr/lib/python2.7/dist-packages/PyQt4/QtTest.so
# by generator 1.143
# no doc
# no imports

# no functions
# classes

class QTest(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def keyClick(self, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTest.keyClick(QWidget, Qt.Key, Qt.KeyboardModifiers modifier=Qt.NoModifier, int delay=-1)
        QTest.keyClick(QWidget, str, Qt.KeyboardModifiers modifier=Qt.NoModifier, int delay=-1)
        """
        pass

    def keyClicks(self, QWidget, QString, Qt_KeyboardModifiers_modifier=None, int_delay=-1): # real signature unknown; restored from __doc__
        """ QTest.keyClicks(QWidget, QString, Qt.KeyboardModifiers modifier=Qt.NoModifier, int delay=-1) """
        pass

    def keyEvent(self, QTest_KeyAction, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTest.keyEvent(QTest.KeyAction, QWidget, Qt.Key, Qt.KeyboardModifiers modifier=Qt.NoModifier, int delay=-1)
        QTest.keyEvent(QTest.KeyAction, QWidget, str, Qt.KeyboardModifiers modifier=Qt.NoModifier, int delay=-1)
        """
        pass

    def keyPress(self, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTest.keyPress(QWidget, Qt.Key, Qt.KeyboardModifiers modifier=Qt.NoModifier, int delay=-1)
        QTest.keyPress(QWidget, str, Qt.KeyboardModifiers modifier=Qt.NoModifier, int delay=-1)
        """
        pass

    def keyRelease(self, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTest.keyRelease(QWidget, Qt.Key, Qt.KeyboardModifiers modifier=Qt.NoModifier, int delay=-1)
        QTest.keyRelease(QWidget, str, Qt.KeyboardModifiers modifier=Qt.NoModifier, int delay=-1)
        """
        pass

    def mouseClick(self, QWidget, Qt_MouseButton, Qt_KeyboardModifiers_modifier=0, QPoint_pos=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QTest.mouseClick(QWidget, Qt.MouseButton, Qt.KeyboardModifiers modifier=0, QPoint pos=QPoint(), int delay=-1) """
        pass

    def mouseDClick(self, QWidget, Qt_MouseButton, Qt_KeyboardModifiers_modifier=0, QPoint_pos=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QTest.mouseDClick(QWidget, Qt.MouseButton, Qt.KeyboardModifiers modifier=0, QPoint pos=QPoint(), int delay=-1) """
        pass

    def mouseEvent(self, QTest_MouseAction, QWidget, Qt_MouseButton, Qt_KeyboardModifiers, QPoint, int_delay=-1): # real signature unknown; restored from __doc__
        """ QTest.mouseEvent(QTest.MouseAction, QWidget, Qt.MouseButton, Qt.KeyboardModifiers, QPoint, int delay=-1) """
        pass

    def mouseMove(self, QWidget, QPoint_pos=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QTest.mouseMove(QWidget, QPoint pos=QPoint(), int delay=-1) """
        pass

    def mousePress(self, QWidget, Qt_MouseButton, Qt_KeyboardModifiers_modifier=0, QPoint_pos=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QTest.mousePress(QWidget, Qt.MouseButton, Qt.KeyboardModifiers modifier=0, QPoint pos=QPoint(), int delay=-1) """
        pass

    def mouseRelease(self, QWidget, Qt_MouseButton, Qt_KeyboardModifiers_modifier=0, QPoint_pos=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QTest.mouseRelease(QWidget, Qt.MouseButton, Qt.KeyboardModifiers modifier=0, QPoint pos=QPoint(), int delay=-1) """
        pass

    def qSleep(self, p_int): # real signature unknown; restored from __doc__
        """ QTest.qSleep(int) """
        pass

    def qWait(self, p_int): # real signature unknown; restored from __doc__
        """ QTest.qWait(int) """
        pass

    def qWaitForWindowShown(self, QWidget): # real signature unknown; restored from __doc__
        """ QTest.qWaitForWindowShown(QWidget) -> bool """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Click = 2
    MouseClick = 2
    MouseDClick = 3
    MouseMove = 4
    MousePress = 0
    MouseRelease = 1
    Press = 0
    Release = 1


