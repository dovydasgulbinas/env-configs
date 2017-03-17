# encoding: utf-8
# module PyQt4.QtScript
# from /usr/lib/python2.7/dist-packages/PyQt4/QtScript.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


# functions

def qScriptConnect(QObject, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qScriptConnect(QObject, SIGNAL(), QScriptValue, QScriptValue) -> bool """
    pass

def qScriptDisconnect(QObject, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qScriptDisconnect(QObject, SIGNAL(), QScriptValue, QScriptValue) -> bool """
    pass

# classes

class QScriptClass(): # skipped bases: <type 'sip.simplewrapper'>
    """ QScriptClass(QScriptEngine) """
    def engine(self): # real signature unknown; restored from __doc__
        """ QScriptClass.engine() -> QScriptEngine """
        return QScriptEngine

    def extension(self, QScriptClass_Extension, QVariant_argument=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QScriptClass.extension(QScriptClass.Extension, QVariant argument=QVariant()) -> QVariant """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ QScriptClass.name() -> QString """
        pass

    def newIterator(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptClass.newIterator(QScriptValue) -> QScriptClassPropertyIterator """
        return QScriptClassPropertyIterator

    def property(self, QScriptValue, QScriptString, p_int): # real signature unknown; restored from __doc__
        """ QScriptClass.property(QScriptValue, QScriptString, int) -> QScriptValue """
        return QScriptValue

    def propertyFlags(self, QScriptValue, QScriptString, p_int): # real signature unknown; restored from __doc__
        """ QScriptClass.propertyFlags(QScriptValue, QScriptString, int) -> QScriptValue.PropertyFlags """
        pass

    def prototype(self): # real signature unknown; restored from __doc__
        """ QScriptClass.prototype() -> QScriptValue """
        return QScriptValue

    def queryProperty(self, QScriptValue, QScriptString, QScriptClass_QueryFlags): # real signature unknown; restored from __doc__
        """ QScriptClass.queryProperty(QScriptValue, QScriptString, QScriptClass.QueryFlags) -> (QScriptClass.QueryFlags, int) """
        pass

    def setProperty(self, QScriptValue, QScriptString, p_int, QScriptValue_1): # real signature unknown; restored from __doc__
        """ QScriptClass.setProperty(QScriptValue, QScriptString, int, QScriptValue) """
        pass

    def supportsExtension(self, QScriptClass_Extension): # real signature unknown; restored from __doc__
        """ QScriptClass.supportsExtension(QScriptClass.Extension) -> bool """
        return False

    def __init__(self, QScriptEngine): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Callable = 0
    HandlesReadAccess = 1
    HandlesWriteAccess = 2
    HasInstance = 1


class QScriptClassPropertyIterator(): # skipped bases: <type 'sip.simplewrapper'>
    """ QScriptClassPropertyIterator(QScriptValue) """
    def flags(self): # real signature unknown; restored from __doc__
        """ QScriptClassPropertyIterator.flags() -> QScriptValue.PropertyFlags """
        pass

    def hasNext(self): # real signature unknown; restored from __doc__
        """ QScriptClassPropertyIterator.hasNext() -> bool """
        return False

    def hasPrevious(self): # real signature unknown; restored from __doc__
        """ QScriptClassPropertyIterator.hasPrevious() -> bool """
        return False

    def id(self): # real signature unknown; restored from __doc__
        """ QScriptClassPropertyIterator.id() -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ QScriptClassPropertyIterator.name() -> QScriptString """
        return QScriptString

    def next(self): # real signature unknown; restored from __doc__
        """ QScriptClassPropertyIterator.next() """
        pass

    def object(self): # real signature unknown; restored from __doc__
        """ QScriptClassPropertyIterator.object() -> QScriptValue """
        return QScriptValue

    def previous(self): # real signature unknown; restored from __doc__
        """ QScriptClassPropertyIterator.previous() """
        pass

    def toBack(self): # real signature unknown; restored from __doc__
        """ QScriptClassPropertyIterator.toBack() """
        pass

    def toFront(self): # real signature unknown; restored from __doc__
        """ QScriptClassPropertyIterator.toFront() """
        pass

    def __init__(self, QScriptValue): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QScriptContext(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def activationObject(self): # real signature unknown; restored from __doc__
        """ QScriptContext.activationObject() -> QScriptValue """
        return QScriptValue

    def argument(self, p_int): # real signature unknown; restored from __doc__
        """ QScriptContext.argument(int) -> QScriptValue """
        return QScriptValue

    def argumentCount(self): # real signature unknown; restored from __doc__
        """ QScriptContext.argumentCount() -> int """
        return 0

    def argumentsObject(self): # real signature unknown; restored from __doc__
        """ QScriptContext.argumentsObject() -> QScriptValue """
        return QScriptValue

    def backtrace(self): # real signature unknown; restored from __doc__
        """ QScriptContext.backtrace() -> QStringList """
        pass

    def callee(self): # real signature unknown; restored from __doc__
        """ QScriptContext.callee() -> QScriptValue """
        return QScriptValue

    def engine(self): # real signature unknown; restored from __doc__
        """ QScriptContext.engine() -> QScriptEngine """
        return QScriptEngine

    def isCalledAsConstructor(self): # real signature unknown; restored from __doc__
        """ QScriptContext.isCalledAsConstructor() -> bool """
        return False

    def parentContext(self): # real signature unknown; restored from __doc__
        """ QScriptContext.parentContext() -> QScriptContext """
        return QScriptContext

    def setActivationObject(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptContext.setActivationObject(QScriptValue) """
        pass

    def setThisObject(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptContext.setThisObject(QScriptValue) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QScriptContext.state() -> QScriptContext.ExecutionState """
        pass

    def thisObject(self): # real signature unknown; restored from __doc__
        """ QScriptContext.thisObject() -> QScriptValue """
        return QScriptValue

    def throwError(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QScriptContext.throwError(QScriptContext.Error, QString) -> QScriptValue
        QScriptContext.throwError(QString) -> QScriptValue
        """
        return QScriptValue

    def throwValue(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptContext.throwValue(QScriptValue) -> QScriptValue """
        return QScriptValue

    def toString(self): # real signature unknown; restored from __doc__
        """ QScriptContext.toString() -> QString """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ExceptionState = 1
    NormalState = 0
    RangeError = 4
    ReferenceError = 1
    SyntaxError = 2
    TypeError = 3
    UnknownError = 0
    URIError = 5


class QScriptContextInfo(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QScriptContextInfo(QScriptContext)
    QScriptContextInfo(QScriptContextInfo)
    QScriptContextInfo()
    """
    def columnNumber(self): # real signature unknown; restored from __doc__
        """ QScriptContextInfo.columnNumber() -> int """
        return 0

    def fileName(self): # real signature unknown; restored from __doc__
        """ QScriptContextInfo.fileName() -> QString """
        pass

    def functionEndLineNumber(self): # real signature unknown; restored from __doc__
        """ QScriptContextInfo.functionEndLineNumber() -> int """
        return 0

    def functionMetaIndex(self): # real signature unknown; restored from __doc__
        """ QScriptContextInfo.functionMetaIndex() -> int """
        return 0

    def functionName(self): # real signature unknown; restored from __doc__
        """ QScriptContextInfo.functionName() -> QString """
        pass

    def functionParameterNames(self): # real signature unknown; restored from __doc__
        """ QScriptContextInfo.functionParameterNames() -> QStringList """
        pass

    def functionStartLineNumber(self): # real signature unknown; restored from __doc__
        """ QScriptContextInfo.functionStartLineNumber() -> int """
        return 0

    def functionType(self): # real signature unknown; restored from __doc__
        """ QScriptContextInfo.functionType() -> QScriptContextInfo.FunctionType """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ QScriptContextInfo.isNull() -> bool """
        return False

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ QScriptContextInfo.lineNumber() -> int """
        return 0

    def scriptId(self): # real signature unknown; restored from __doc__
        """ QScriptContextInfo.scriptId() -> int """
        return 0

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NativeFunction = 3
    QtFunction = 1
    QtPropertyFunction = 2
    ScriptFunction = 0


class QScriptEngine(__PyQt4_QtCore.QObject):
    """
    QScriptEngine()
    QScriptEngine(QObject)
    """
    def abortEvaluation(self, QScriptValue_result=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QScriptEngine.abortEvaluation(QScriptValue result=QScriptValue()) """
        pass

    def agent(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.agent() -> QScriptEngineAgent """
        return QScriptEngineAgent

    def availableExtensions(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.availableExtensions() -> QStringList """
        pass

    def canEvaluate(self, QString): # real signature unknown; restored from __doc__
        """ QScriptEngine.canEvaluate(QString) -> bool """
        return False

    def checkSyntax(self, QString): # real signature unknown; restored from __doc__
        """ QScriptEngine.checkSyntax(QString) -> QScriptSyntaxCheckResult """
        return QScriptSyntaxCheckResult

    def clearExceptions(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.clearExceptions() """
        pass

    def collectGarbage(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.collectGarbage() """
        pass

    def currentContext(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.currentContext() -> QScriptContext """
        return QScriptContext

    def defaultPrototype(self, p_int): # real signature unknown; restored from __doc__
        """ QScriptEngine.defaultPrototype(int) -> QScriptValue """
        return QScriptValue

    def evaluate(self, QString, QString_fileName=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QScriptEngine.evaluate(QString, QString fileName=QString(), int lineNumber=1) -> QScriptValue """
        pass

    def globalObject(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.globalObject() -> QScriptValue """
        return QScriptValue

    def hasUncaughtException(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.hasUncaughtException() -> bool """
        return False

    def importedExtensions(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.importedExtensions() -> QStringList """
        pass

    def importExtension(self, QString): # real signature unknown; restored from __doc__
        """ QScriptEngine.importExtension(QString) -> QScriptValue """
        return QScriptValue

    def installTranslatorFunctions(self, QScriptValue_object=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QScriptEngine.installTranslatorFunctions(QScriptValue object=QScriptValue()) """
        pass

    def isEvaluating(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.isEvaluating() -> bool """
        return False

    def newArray(self, int_length=0): # real signature unknown; restored from __doc__
        """ QScriptEngine.newArray(int length=0) -> QScriptValue """
        return QScriptValue

    def newDate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QScriptEngine.newDate(float) -> QScriptValue
        QScriptEngine.newDate(QDateTime) -> QScriptValue
        """
        return QScriptValue

    def newFunction(self, callable, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QScriptEngine.newFunction(callable, int length=0) -> QScriptValue
        QScriptEngine.newFunction(callable, QScriptValue, int length=0) -> QScriptValue
        """
        return QScriptValue

    def newObject(self, QScriptClass=None, QScriptValue_data=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QScriptEngine.newObject() -> QScriptValue
        QScriptEngine.newObject(QScriptClass, QScriptValue data=QScriptValue()) -> QScriptValue
        """
        return QScriptValue

    def newQMetaObject(self, QMetaObject, QScriptValue_ctor=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QScriptEngine.newQMetaObject(QMetaObject, QScriptValue ctor=QScriptValue()) -> QScriptValue """
        pass

    def newQObject(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QScriptEngine.newQObject(QObject, QScriptEngine.ValueOwnership ownership=QScriptEngine.QtOwnership, QScriptEngine.QObjectWrapOptions options=0) -> QScriptValue
        QScriptEngine.newQObject(QScriptValue, QObject, QScriptEngine.ValueOwnership ownership=QScriptEngine.QtOwnership, QScriptEngine.QObjectWrapOptions options=0) -> QScriptValue
        """
        return QScriptValue

    def newRegExp(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QScriptEngine.newRegExp(QRegExp) -> QScriptValue
        QScriptEngine.newRegExp(QString, QString) -> QScriptValue
        """
        return QScriptValue

    def newVariant(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QScriptEngine.newVariant(QVariant) -> QScriptValue
        QScriptEngine.newVariant(QScriptValue, QVariant) -> QScriptValue
        """
        return QScriptValue

    def nullValue(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.nullValue() -> QScriptValue """
        return QScriptValue

    def popContext(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.popContext() """
        pass

    def processEventsInterval(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.processEventsInterval() -> int """
        return 0

    def pushContext(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.pushContext() -> QScriptContext """
        return QScriptContext

    def reportAdditionalMemoryCost(self, p_int): # real signature unknown; restored from __doc__
        """ QScriptEngine.reportAdditionalMemoryCost(int) """
        pass

    def setAgent(self, QScriptEngineAgent): # real signature unknown; restored from __doc__
        """ QScriptEngine.setAgent(QScriptEngineAgent) """
        pass

    def setDefaultPrototype(self, p_int, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptEngine.setDefaultPrototype(int, QScriptValue) """
        pass

    def setGlobalObject(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptEngine.setGlobalObject(QScriptValue) """
        pass

    def setProcessEventsInterval(self, p_int): # real signature unknown; restored from __doc__
        """ QScriptEngine.setProcessEventsInterval(int) """
        pass

    def signalHandlerException(self, *args, **kwargs): # real signature unknown
        """ QScriptEngine.signalHandlerException[QScriptValue] [signal] """
        pass

    def toObject(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptEngine.toObject(QScriptValue) -> QScriptValue """
        return QScriptValue

    def toStringHandle(self, QString): # real signature unknown; restored from __doc__
        """ QScriptEngine.toStringHandle(QString) -> QScriptString """
        return QScriptString

    def uncaughtException(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.uncaughtException() -> QScriptValue """
        return QScriptValue

    def uncaughtExceptionBacktrace(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.uncaughtExceptionBacktrace() -> QStringList """
        pass

    def uncaughtExceptionLineNumber(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.uncaughtExceptionLineNumber() -> int """
        return 0

    def undefinedValue(self): # real signature unknown; restored from __doc__
        """ QScriptEngine.undefinedValue() -> QScriptValue """
        return QScriptValue

    def __init__(self, QObject=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AutoCreateDynamicProperties = 256
    AutoOwnership = 2
    ExcludeChildObjects = 1
    ExcludeDeleteLater = 16
    ExcludeSlots = 32
    ExcludeSuperClassContents = 6
    ExcludeSuperClassMethods = 2
    ExcludeSuperClassProperties = 4
    PreferExistingWrapperObject = 512
    QtOwnership = 0
    ScriptOwnership = 1
    SkipMethodsInEnumeration = 8


class QScriptEngineAgent(): # skipped bases: <type 'sip.wrapper'>
    """ QScriptEngineAgent(QScriptEngine) """
    def contextPop(self): # real signature unknown; restored from __doc__
        """ QScriptEngineAgent.contextPop() """
        pass

    def contextPush(self): # real signature unknown; restored from __doc__
        """ QScriptEngineAgent.contextPush() """
        pass

    def engine(self): # real signature unknown; restored from __doc__
        """ QScriptEngineAgent.engine() -> QScriptEngine """
        return QScriptEngine

    def exceptionCatch(self, p_int, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptEngineAgent.exceptionCatch(int, QScriptValue) """
        pass

    def exceptionThrow(self, p_int, QScriptValue, bool): # real signature unknown; restored from __doc__
        """ QScriptEngineAgent.exceptionThrow(int, QScriptValue, bool) """
        pass

    def extension(self, QScriptEngineAgent_Extension, QVariant_argument=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QScriptEngineAgent.extension(QScriptEngineAgent.Extension, QVariant argument=QVariant()) -> QVariant """
        pass

    def functionEntry(self, p_int): # real signature unknown; restored from __doc__
        """ QScriptEngineAgent.functionEntry(int) """
        pass

    def functionExit(self, p_int, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptEngineAgent.functionExit(int, QScriptValue) """
        pass

    def positionChange(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ QScriptEngineAgent.positionChange(int, int, int) """
        pass

    def scriptLoad(self, p_int, QString, QString_1, p_int_1): # real signature unknown; restored from __doc__
        """ QScriptEngineAgent.scriptLoad(int, QString, QString, int) """
        pass

    def scriptUnload(self, p_int): # real signature unknown; restored from __doc__
        """ QScriptEngineAgent.scriptUnload(int) """
        pass

    def supportsExtension(self, QScriptEngineAgent_Extension): # real signature unknown; restored from __doc__
        """ QScriptEngineAgent.supportsExtension(QScriptEngineAgent.Extension) -> bool """
        return False

    def __init__(self, QScriptEngine): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DebuggerInvocationRequest = 0


class QScriptString(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QScriptString()
    QScriptString(QScriptString)
    """
    def isValid(self): # real signature unknown; restored from __doc__
        """ QScriptString.isValid() -> bool """
        return False

    def toArrayIndex(self): # real signature unknown; restored from __doc__
        """ QScriptString.toArrayIndex() -> (int, bool) """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ QScriptString.toString() -> QString """
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

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, QScriptString=None): # real signature unknown; restored from __doc__ with multiple overloads
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QScriptSyntaxCheckResult(): # skipped bases: <type 'sip.simplewrapper'>
    """ QScriptSyntaxCheckResult(QScriptSyntaxCheckResult) """
    def errorColumnNumber(self): # real signature unknown; restored from __doc__
        """ QScriptSyntaxCheckResult.errorColumnNumber() -> int """
        return 0

    def errorLineNumber(self): # real signature unknown; restored from __doc__
        """ QScriptSyntaxCheckResult.errorLineNumber() -> int """
        return 0

    def errorMessage(self): # real signature unknown; restored from __doc__
        """ QScriptSyntaxCheckResult.errorMessage() -> QString """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QScriptSyntaxCheckResult.state() -> QScriptSyntaxCheckResult.State """
        pass

    def __init__(self, QScriptSyntaxCheckResult): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Error = 0
    Intermediate = 1
    Valid = 2


class QScriptValue(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QScriptValue()
    QScriptValue(QScriptValue)
    QScriptValue(QScriptValue.SpecialValue)
    QScriptValue(QScriptEngine, QScriptValue.SpecialValue)
    QScriptValue(bool)
    QScriptValue(QScriptEngine, bool)
    QScriptValue(int)
    QScriptValue(QScriptEngine, int)
    QScriptValue(float)
    QScriptValue(QScriptEngine, float)
    QScriptValue(QString)
    QScriptValue(QScriptEngine, QString)
    """
    def call(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QScriptValue.call(QScriptValue thisObject=QScriptValue(), list-of-QScriptValue args=QScriptValueList()) -> QScriptValue
        QScriptValue.call(QScriptValue, QScriptValue) -> QScriptValue
        """
        return QScriptValue

    def construct(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QScriptValue.construct(list-of-QScriptValue args=QScriptValueList()) -> QScriptValue
        QScriptValue.construct(QScriptValue) -> QScriptValue
        """
        return QScriptValue

    def data(self): # real signature unknown; restored from __doc__
        """ QScriptValue.data() -> QScriptValue """
        return QScriptValue

    def engine(self): # real signature unknown; restored from __doc__
        """ QScriptValue.engine() -> QScriptEngine """
        return QScriptEngine

    def equals(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptValue.equals(QScriptValue) -> bool """
        return False

    def instanceOf(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptValue.instanceOf(QScriptValue) -> bool """
        return False

    def isArray(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isArray() -> bool """
        return False

    def isBool(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isBool() -> bool """
        return False

    def isBoolean(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isBoolean() -> bool """
        return False

    def isDate(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isDate() -> bool """
        return False

    def isError(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isError() -> bool """
        return False

    def isFunction(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isFunction() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isNull() -> bool """
        return False

    def isNumber(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isNumber() -> bool """
        return False

    def isObject(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isObject() -> bool """
        return False

    def isQMetaObject(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isQMetaObject() -> bool """
        return False

    def isQObject(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isQObject() -> bool """
        return False

    def isRegExp(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isRegExp() -> bool """
        return False

    def isString(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isString() -> bool """
        return False

    def isUndefined(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isUndefined() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isValid() -> bool """
        return False

    def isVariant(self): # real signature unknown; restored from __doc__
        """ QScriptValue.isVariant() -> bool """
        return False

    def lessThan(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptValue.lessThan(QScriptValue) -> bool """
        return False

    def property(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QScriptValue.property(QString, QScriptValue.ResolveFlags mode=QScriptValue.ResolvePrototype) -> QScriptValue
        QScriptValue.property(QScriptString, QScriptValue.ResolveFlags mode=QScriptValue.ResolvePrototype) -> QScriptValue
        QScriptValue.property(int, QScriptValue.ResolveFlags mode=QScriptValue.ResolvePrototype) -> QScriptValue
        """
        return QScriptValue

    def propertyFlags(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QScriptValue.propertyFlags(QString, QScriptValue.ResolveFlags mode=QScriptValue.ResolvePrototype) -> QScriptValue.PropertyFlags
        QScriptValue.propertyFlags(QScriptString, QScriptValue.ResolveFlags mode=QScriptValue.ResolvePrototype) -> QScriptValue.PropertyFlags
        """
        pass

    def prototype(self): # real signature unknown; restored from __doc__
        """ QScriptValue.prototype() -> QScriptValue """
        return QScriptValue

    def scriptClass(self): # real signature unknown; restored from __doc__
        """ QScriptValue.scriptClass() -> QScriptClass """
        return QScriptClass

    def setData(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptValue.setData(QScriptValue) """
        pass

    def setProperty(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QScriptValue.setProperty(QString, QScriptValue, QScriptValue.PropertyFlags flags=QScriptValue.KeepExistingFlags)
        QScriptValue.setProperty(QScriptString, QScriptValue, QScriptValue.PropertyFlags flags=QScriptValue.KeepExistingFlags)
        QScriptValue.setProperty(int, QScriptValue, QScriptValue.PropertyFlags flags=QScriptValue.KeepExistingFlags)
        """
        pass

    def setPrototype(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptValue.setPrototype(QScriptValue) """
        pass

    def setScriptClass(self, QScriptClass): # real signature unknown; restored from __doc__
        """ QScriptValue.setScriptClass(QScriptClass) """
        pass

    def strictlyEquals(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptValue.strictlyEquals(QScriptValue) -> bool """
        return False

    def toBool(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toBool() -> bool """
        return False

    def toBoolean(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toBoolean() -> bool """
        return False

    def toDateTime(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toDateTime() -> QDateTime """
        pass

    def toInt32(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toInt32() -> int """
        return 0

    def toInteger(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toInteger() -> float """
        return 0.0

    def toNumber(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toNumber() -> float """
        return 0.0

    def toObject(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toObject() -> QScriptValue """
        return QScriptValue

    def toQMetaObject(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toQMetaObject() -> QMetaObject """
        pass

    def toQObject(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toQObject() -> QObject """
        pass

    def toRegExp(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toRegExp() -> QRegExp """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toString() -> QString """
        pass

    def toUInt16(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toUInt16() -> int """
        return 0

    def toUInt32(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toUInt32() -> int """
        return 0

    def toVariant(self): # real signature unknown; restored from __doc__
        """ QScriptValue.toVariant() -> QVariant """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    KeepExistingFlags = 2048
    NullValue = 0
    PropertyGetter = 8
    PropertySetter = 16
    QObjectMember = 32
    ReadOnly = 1
    ResolveFull = 3
    ResolveLocal = 0
    ResolvePrototype = 1
    ResolveScope = 2
    SkipInEnumeration = 4
    UndefinedValue = 1
    Undeletable = 2
    UserRange = -16777216


class QScriptValueIterator(): # skipped bases: <type 'sip.simplewrapper'>
    """ QScriptValueIterator(QScriptValue) """
    def flags(self): # real signature unknown; restored from __doc__
        """ QScriptValueIterator.flags() -> QScriptValue.PropertyFlags """
        pass

    def hasNext(self): # real signature unknown; restored from __doc__
        """ QScriptValueIterator.hasNext() -> bool """
        return False

    def hasPrevious(self): # real signature unknown; restored from __doc__
        """ QScriptValueIterator.hasPrevious() -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ QScriptValueIterator.name() -> QString """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ QScriptValueIterator.next() """
        pass

    def previous(self): # real signature unknown; restored from __doc__
        """ QScriptValueIterator.previous() """
        pass

    def remove(self): # real signature unknown; restored from __doc__
        """ QScriptValueIterator.remove() """
        pass

    def scriptName(self): # real signature unknown; restored from __doc__
        """ QScriptValueIterator.scriptName() -> QScriptString """
        return QScriptString

    def setValue(self, QScriptValue): # real signature unknown; restored from __doc__
        """ QScriptValueIterator.setValue(QScriptValue) """
        pass

    def toBack(self): # real signature unknown; restored from __doc__
        """ QScriptValueIterator.toBack() """
        pass

    def toFront(self): # real signature unknown; restored from __doc__
        """ QScriptValueIterator.toFront() """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ QScriptValueIterator.value() -> QScriptValue """
        return QScriptValue

    def __init__(self, QScriptValue): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



