from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class, Iterable
from java.lang.reflect import Method, Constructor, Type
from java.util import Map, HashMap, List
from se.krka.kahlua.converter import KahluaConverterManager
from se.krka.kahlua.integration.expose.caller import Caller
from se.krka.kahlua.integration.processor import ClassParameterInformation
from se.krka.kahlua.vm import KahluaTable, Platform, LuaCallFrame

T = TypeVar('T', default=Any)

class AnnotationUtil:

  @staticmethod
  def getAnnotation(arg0: Method, arg1: Class[T]) -> T: ...

  def __init__(self): ...


class ClassDebugInformation:

  def getMethods(self) -> Map[str, MethodDebugInformation]: ...

  def __init__(self, arg0: Class[Any], arg1: ClassParameterInformation): ...


class IterableExposer:

  # @LuaMethod
  def (self, arg0: Iterable[Any]) -> object: ...

  def __init__(self): ...


class LuaJavaClassExposer:

  # @LuaMethod
  def definition(self, arg0: object) -> str: ...

  def destroy(self) -> None: ...

  @overload
  def exposeGlobalClassFunction(self, arg0: KahluaTable, arg1: Class[Any], arg2: Constructor[Any], arg3: str) -> None: ...

  @overload
  def exposeGlobalClassFunction(self, arg0: KahluaTable, arg1: Class[Any], arg2: Method, arg3: str) -> None: ...

  def exposeGlobalFunctions(self, arg0: object) -> None: ...

  @overload
  def exposeGlobalObjectFunction(self, arg0: KahluaTable, arg1: object, arg2: Method) -> None: ...

  @overload
  def exposeGlobalObjectFunction(self, arg0: KahluaTable, arg1: object, arg2: Method, arg3: str) -> None: ...

  @overload
  def exposeLikeJava(self, arg0: Class) -> None: ...

  @overload
  def exposeLikeJava(self, arg0: Class, arg1: KahluaTable) -> None: ...

  @overload
  def exposeLikeJavaRecursively(self, arg0: Type) -> None: ...

  @overload
  def exposeLikeJavaRecursively(self, arg0: Type, arg1: KahluaTable) -> None: ...

  @overload
  def exposeMethod(self, arg0: Class[Any], arg1: Method, arg2: KahluaTable) -> None: ...

  @overload
  def exposeMethod(self, arg0: Class[Any], arg1: Method, arg2: str, arg3: KahluaTable) -> None: ...

  def getClassDebugInformation(self) -> Map[Class[Any], ClassDebugInformation]: ...

  def isExposed(self, arg0: Class[Any]) -> bool: ...

  def shouldExpose(self, arg0: Class[Any]) -> bool: ...

  @overload
  def __init__(self, arg0: KahluaConverterManager, arg1: Platform, arg2: KahluaTable):
    self.typemap: HashMap[str, Class[Any]]

  @overload
  def __init__(self, arg0: KahluaConverterManager, arg1: Platform, arg2: KahluaTable, arg3: KahluaTable): ...


class LuaJavaInvoker:

  @overload
  def call(self, arg0: MethodArguments) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  def equals(self, arg0: object) -> bool: ...

  def getMethodDebugData(self) -> MethodDebugInformation: ...

  def getNumMethodParams(self) -> int: ...

  def hashCode(self) -> int: ...

  def isAllInt(self) -> bool: ...

  def matchesArgumentTypes(self, arg0: LuaCallFrame, arg1: int) -> bool: ...

  def matchesArgumentTypesOrPrimitives(self, arg0: LuaCallFrame, arg1: int) -> bool: ...

  def prepareCall(self, arg0: LuaCallFrame, arg1: int) -> MethodArguments: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: LuaJavaClassExposer, arg1: KahluaConverterManager, arg2: Class[Any], arg3: str, arg4: Caller): ...


class MethodArguments:

  def assertValid(self) -> None: ...

  def fail(self, arg0: str) -> None: ...

  def getFailure(self) -> str: ...

  def getParams(self) -> list[object]: ...

  def getReturnValues(self) -> ReturnValues: ...

  def getSelf(self) -> object: ...

  def isValid(self) -> bool: ...

  def setReturnValues(self, arg0: ReturnValues) -> None: ...

  def setSelf(self, arg0: object) -> None: ...

  @staticmethod
  def get(arg0: int) -> MethodArguments: ...

  @staticmethod
  def put(arg0: MethodArguments) -> None: ...

  def __init__(self, arg0: int): ...


class MethodDebugInformation:

  def getLuaDescription(self) -> str: ...

  def getLuaName(self) -> str: ...

  def getParameters(self) -> List[MethodParameter]: ...

  def getReturnDescription(self) -> str: ...

  def getReturnType(self) -> str: ...

  def isMethod(self) -> bool: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: str, arg1: bool, arg2: List[MethodParameter], arg3: str, arg4: str): ...


class MethodParameter:

  def getDescription(self) -> str: ...

  def getName(self) -> str: ...

  def getType(self) -> str: ...

  def __init__(self, arg0: str, arg1: str, arg2: str): ...


class MultiLuaJavaInvoker:

  def addInvoker(self, arg0: LuaJavaInvoker) -> None: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  def equals(self, arg0: object) -> bool: ...

  def getInvokers(self) -> List[LuaJavaInvoker]: ...

  def hashCode(self) -> int: ...

  def __init__(self): ...


class ReturnValues:

  @overload
  def push(self, arg0: list[object]) -> ReturnValues: ...

  @overload
  def push(self, arg0: object) -> ReturnValues: ...

  @staticmethod
  def get(arg0: KahluaConverterManager, arg1: LuaCallFrame) -> ReturnValues: ...

  @staticmethod
  def put(arg0: ReturnValues) -> None: ...


class TypeUtil:

  @staticmethod
  def getClassName(arg0: Type) -> str: ...

  @staticmethod
  def removePackages(arg0: str) -> str: ...

  def __init__(self): ...

