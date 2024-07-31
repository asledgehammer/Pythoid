from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from java.lang.invoke import TypeDescriptor, MethodHandles
from java.util import Optional, List

T = TypeVar('T', default=Any)
AnonymousDynamicConstantDesc_T = TypeVar('AnonymousDynamicConstantDesc_T', default=Any)

class ClassDesc:

  @overload
  def arrayType(self) -> TypeDescriptor.OfField: ...

  @overload
  def arrayType(self) -> ClassDesc: ...

  @overload
  def arrayType(self) -> TypeDescriptor.OfField: ...

  @overload
  def arrayType(self, arg0: int) -> ClassDesc: ...

  @overload
  def componentType(self) -> TypeDescriptor.OfField: ...

  @overload
  def componentType(self) -> ClassDesc: ...

  @overload
  def componentType(self) -> TypeDescriptor.OfField: ...

  def descriptorString(self) -> str: ...

  def displayName(self) -> str: ...

  def equals(self, arg0: object) -> bool: ...

  @overload
  def isArray(self) -> bool: ...

  @overload
  def isArray(self) -> bool: ...

  def isClassOrInterface(self) -> bool: ...

  @overload
  def isPrimitive(self) -> bool: ...

  @overload
  def isPrimitive(self) -> bool: ...

  @overload
  def nested(self, arg0: str) -> ClassDesc: ...

  @overload
  def nested(self, arg0: str, arg1: list[str]) -> ClassDesc: ...

  def packageName(self) -> str: ...

  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  @staticmethod
  @overload
  def of(arg0: str) -> ClassDesc: ...

  @staticmethod
  @overload
  def of(arg0: str, arg1: str) -> ClassDesc: ...

  @staticmethod
  def ofDescriptor(arg0: str) -> ClassDesc: ...


class Constable:

  def describeConstable(self) -> Optional[ConstantDesc]: ...


class ConstantDesc:

  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...


class DirectMethodHandleDesc:

  def asType(self, arg0: MethodTypeDesc) -> MethodHandleDesc: ...

  def equals(self, arg0: object) -> bool: ...

  def invocationType(self) -> MethodTypeDesc: ...

  def isOwnerInterface(self) -> bool: ...

  def kind(self) -> DirectMethodHandleDesc.Kind: ...

  def lookupDescriptor(self) -> str: ...

  def methodName(self) -> str: ...

  def owner(self) -> ClassDesc: ...

  def refKind(self) -> int: ...

  @staticmethod
  def of(arg0: DirectMethodHandleDesc.Kind, arg1: ClassDesc, arg2: str, arg3: str) -> DirectMethodHandleDesc: ...

  @staticmethod
  def ofConstructor(arg0: ClassDesc, arg1: list[ClassDesc]) -> DirectMethodHandleDesc: ...

  @staticmethod
  def ofField(arg0: DirectMethodHandleDesc.Kind, arg1: ClassDesc, arg2: str, arg3: ClassDesc) -> DirectMethodHandleDesc: ...

  @staticmethod
  def ofMethod(arg0: DirectMethodHandleDesc.Kind, arg1: ClassDesc, arg2: str, arg3: MethodTypeDesc) -> DirectMethodHandleDesc: ...

  class Kind(Enum):

    CONSTRUCTOR: DirectMethodHandleDesc.Kind

    GETTER: DirectMethodHandleDesc.Kind

    INTERFACE_SPECIAL: DirectMethodHandleDesc.Kind

    INTERFACE_STATIC: DirectMethodHandleDesc.Kind

    INTERFACE_VIRTUAL: DirectMethodHandleDesc.Kind

    SETTER: DirectMethodHandleDesc.Kind

    SPECIAL: DirectMethodHandleDesc.Kind

    STATIC: DirectMethodHandleDesc.Kind

    STATIC_GETTER: DirectMethodHandleDesc.Kind

    STATIC_SETTER: DirectMethodHandleDesc.Kind

    VIRTUAL: DirectMethodHandleDesc.Kind

    @staticmethod
    @overload
    def valueOf(arg0: int) -> DirectMethodHandleDesc.Kind: ...

    @staticmethod
    @overload
    def valueOf(arg0: str) -> DirectMethodHandleDesc.Kind: ...

    @staticmethod
    @overload
    def valueOf(arg0: int, arg1: bool) -> DirectMethodHandleDesc.Kind: ...

    @staticmethod
    def values() -> list[DirectMethodHandleDesc.Kind]: ...


class DynamicConstantDesc[T]:

  def bootstrapArgs(self) -> list[ConstantDesc]: ...

  def bootstrapArgsList(self) -> List[ConstantDesc]: ...

  def bootstrapMethod(self) -> DirectMethodHandleDesc: ...

  def constantName(self) -> str: ...

  def constantType(self) -> ClassDesc: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  def toString(self) -> str: ...

  @staticmethod
  @overload
  def of(arg0: DirectMethodHandleDesc) -> DynamicConstantDesc[T]: ...

  @staticmethod
  @overload
  def of(arg0: DirectMethodHandleDesc, arg1: list[ConstantDesc]) -> DynamicConstantDesc[T]: ...

  @staticmethod
  def ofCanonical(arg0: DirectMethodHandleDesc, arg1: str, arg2: ClassDesc, arg3: list[ConstantDesc]) -> ConstantDesc: ...

  @staticmethod
  def ofNamed(arg0: DirectMethodHandleDesc, arg1: str, arg2: ClassDesc, arg3: list[ConstantDesc]) -> DynamicConstantDesc[T]: ...

  class AnonymousDynamicConstantDesc[AnonymousDynamicConstantDesc_T](DynamicConstantDesc): ...

  class CanonicalMapHolder: ...


class MethodHandleDesc:

  def asType(self, arg0: MethodTypeDesc) -> MethodHandleDesc: ...

  def equals(self, arg0: object) -> bool: ...

  def invocationType(self) -> MethodTypeDesc: ...

  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  @staticmethod
  def of(arg0: DirectMethodHandleDesc.Kind, arg1: ClassDesc, arg2: str, arg3: str) -> DirectMethodHandleDesc: ...

  @staticmethod
  def ofConstructor(arg0: ClassDesc, arg1: list[ClassDesc]) -> DirectMethodHandleDesc: ...

  @staticmethod
  def ofField(arg0: DirectMethodHandleDesc.Kind, arg1: ClassDesc, arg2: str, arg3: ClassDesc) -> DirectMethodHandleDesc: ...

  @staticmethod
  def ofMethod(arg0: DirectMethodHandleDesc.Kind, arg1: ClassDesc, arg2: str, arg3: MethodTypeDesc) -> DirectMethodHandleDesc: ...


class MethodTypeDesc:

  @overload
  def changeParameterType(self, arg0: int, arg1: ClassDesc) -> MethodTypeDesc: ...

  @overload
  def changeParameterType(self, arg0: int, arg1: TypeDescriptor.OfField) -> TypeDescriptor.OfMethod: ...

  @overload
  def changeParameterType(self, arg0: int, arg1: TypeDescriptor.OfField) -> TypeDescriptor.OfMethod: ...

  @overload
  def changeReturnType(self, arg0: ClassDesc) -> MethodTypeDesc: ...

  @overload
  def changeReturnType(self, arg0: TypeDescriptor.OfField) -> TypeDescriptor.OfMethod: ...

  @overload
  def changeReturnType(self, arg0: TypeDescriptor.OfField) -> TypeDescriptor.OfMethod: ...

  def descriptorString(self) -> str: ...

  def displayDescriptor(self) -> str: ...

  @overload
  def dropParameterTypes(self, arg0: int, arg1: int) -> TypeDescriptor.OfMethod: ...

  @overload
  def dropParameterTypes(self, arg0: int, arg1: int) -> MethodTypeDesc: ...

  @overload
  def dropParameterTypes(self, arg0: int, arg1: int) -> TypeDescriptor.OfMethod: ...

  def equals(self, arg0: object) -> bool: ...

  @overload
  def insertParameterTypes(self, arg0: int, arg1: list[ClassDesc]) -> MethodTypeDesc: ...

  @overload
  def insertParameterTypes(self, arg0: int, arg1: list[TypeDescriptor.OfField]) -> TypeDescriptor.OfMethod: ...

  @overload
  def insertParameterTypes(self, arg0: int, arg1: list[TypeDescriptor.OfField]) -> TypeDescriptor.OfMethod: ...

  @overload
  def parameterArray(self) -> list[ClassDesc]: ...

  @overload
  def parameterArray(self) -> list[TypeDescriptor.OfField]: ...

  @overload
  def parameterArray(self) -> list[TypeDescriptor.OfField]: ...

  @overload
  def parameterCount(self) -> int: ...

  @overload
  def parameterCount(self) -> int: ...

  @overload
  def parameterList(self) -> List[ClassDesc]: ...

  @overload
  def parameterList(self) -> List[F]: ...

  @overload
  def parameterType(self, arg0: int) -> TypeDescriptor.OfField: ...

  @overload
  def parameterType(self, arg0: int) -> ClassDesc: ...

  @overload
  def parameterType(self, arg0: int) -> TypeDescriptor.OfField: ...

  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  @overload
  def returnType(self) -> ClassDesc: ...

  @overload
  def returnType(self) -> TypeDescriptor.OfField: ...

  @overload
  def returnType(self) -> TypeDescriptor.OfField: ...

  @staticmethod
  def of(arg0: ClassDesc, arg1: list[ClassDesc]) -> MethodTypeDesc: ...

  @staticmethod
  def ofDescriptor(arg0: str) -> MethodTypeDesc: ...
