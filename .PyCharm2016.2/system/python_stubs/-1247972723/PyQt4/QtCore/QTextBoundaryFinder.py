# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QTextBoundaryFinder(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QTextBoundaryFinder()
    QTextBoundaryFinder(QTextBoundaryFinder)
    QTextBoundaryFinder(QTextBoundaryFinder.BoundaryType, QString)
    """
    def boundaryReasons(self): # real signature unknown; restored from __doc__
        """ QTextBoundaryFinder.boundaryReasons() -> QTextBoundaryFinder.BoundaryReasons """
        pass

    def isAtBoundary(self): # real signature unknown; restored from __doc__
        """ QTextBoundaryFinder.isAtBoundary() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QTextBoundaryFinder.isValid() -> bool """
        return False

    def position(self): # real signature unknown; restored from __doc__
        """ QTextBoundaryFinder.position() -> int """
        return 0

    def setPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QTextBoundaryFinder.setPosition(int) """
        pass

    def string(self): # real signature unknown; restored from __doc__
        """ QTextBoundaryFinder.string() -> QString """
        return QString

    def toEnd(self): # real signature unknown; restored from __doc__
        """ QTextBoundaryFinder.toEnd() """
        pass

    def toNextBoundary(self): # real signature unknown; restored from __doc__
        """ QTextBoundaryFinder.toNextBoundary() -> int """
        return 0

    def toPreviousBoundary(self): # real signature unknown; restored from __doc__
        """ QTextBoundaryFinder.toPreviousBoundary() -> int """
        return 0

    def toStart(self): # real signature unknown; restored from __doc__
        """ QTextBoundaryFinder.toStart() """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QTextBoundaryFinder.type() -> QTextBoundaryFinder.BoundaryType """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    EndWord = 2
    Grapheme = 0
    Line = 2
    NotAtBoundary = 0
    Sentence = 3
    StartWord = 1
    Word = 1


