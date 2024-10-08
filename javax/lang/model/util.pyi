from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import Writer
from java.lang import CharSequence, Enum
from java.util import List, Set, Map
from javax.lang.model import AnnotatedConstruct
from javax.lang.model.element import Element, TypeElement, Name, AnnotationMirror, ModuleElement, PackageElement, ExecutableElement, RecordComponentElement
from javax.lang.model.type import TypeMirror, DeclaredType, PrimitiveType, ArrayType, TypeKind, NoType, NullType, WildcardType, ExecutableType
from javax.tools import JavaFileObject

class Elements:

  def getAllAnnotationMirrors(self, arg0: Element) -> List[AnnotationMirror]: ...

  def getAllMembers(self, arg0: TypeElement) -> List[Element]: ...

  def getAllModuleElements(self) -> Set[ModuleElement]: ...

  def getAllPackageElements(self, arg0: CharSequence) -> Set[PackageElement]: ...

  def getAllTypeElements(self, arg0: CharSequence) -> Set[TypeElement]: ...

  def getBinaryName(self, arg0: TypeElement) -> Name: ...

  def getConstantExpression(self, arg0: object) -> str: ...

  def getDocComment(self, arg0: Element) -> str: ...

  def getElementValuesWithDefaults(self, arg0: AnnotationMirror) -> Map[ExecutableElement, AnnotationValue]: ...

  def getFileObjectOf(self, arg0: Element) -> JavaFileObject: ...

  def getModuleElement(self, arg0: CharSequence) -> ModuleElement: ...

  def getModuleOf(self, arg0: Element) -> ModuleElement: ...

  def getName(self, arg0: CharSequence) -> Name: ...

  @overload
  def getOrigin(self, arg0: Element) -> Elements.Origin: ...

  @overload
  def getOrigin(self, arg0: AnnotatedConstruct, arg1: AnnotationMirror) -> Elements.Origin: ...

  @overload
  def getOrigin(self, arg0: ModuleElement, arg1: ModuleElement.Directive) -> Elements.Origin: ...

  def getOutermostTypeElement(self, arg0: Element) -> TypeElement: ...

  @overload
  def getPackageElement(self, arg0: CharSequence) -> PackageElement: ...

  @overload
  def getPackageElement(self, arg0: ModuleElement, arg1: CharSequence) -> PackageElement: ...

  def getPackageOf(self, arg0: Element) -> PackageElement: ...

  @overload
  def getTypeElement(self, arg0: CharSequence) -> TypeElement: ...

  @overload
  def getTypeElement(self, arg0: ModuleElement, arg1: CharSequence) -> TypeElement: ...

  def hides(self, arg0: Element, arg1: Element) -> bool: ...

  def isAutomaticModule(self, arg0: ModuleElement) -> bool: ...

  def isBridge(self, arg0: ExecutableElement) -> bool: ...

  def isDeprecated(self, arg0: Element) -> bool: ...

  def isFunctionalInterface(self, arg0: TypeElement) -> bool: ...

  def overrides(self, arg0: ExecutableElement, arg1: ExecutableElement, arg2: TypeElement) -> bool: ...

  def printElements(self, arg0: Writer, arg1: list[Element]) -> None: ...

  def recordComponentFor(self, arg0: ExecutableElement) -> RecordComponentElement: ...

  class Origin(Enum):

    EXPLICIT: Elements.Origin

    MANDATED: Elements.Origin

    SYNTHETIC: Elements.Origin

    def isDeclared(self) -> bool: ...

    @staticmethod
    def valueOf(arg0: str) -> Elements.Origin: ...

    @staticmethod
    def values() -> list[Elements.Origin]: ...


class Types:

  def asElement(self, arg0: TypeMirror) -> Element: ...

  def asMemberOf(self, arg0: DeclaredType, arg1: Element) -> TypeMirror: ...

  def boxedClass(self, arg0: PrimitiveType) -> TypeElement: ...

  def capture(self, arg0: TypeMirror) -> TypeMirror: ...

  def contains(self, arg0: TypeMirror, arg1: TypeMirror) -> bool: ...

  def directSupertypes(self, arg0: TypeMirror) -> List[TypeMirror]: ...

  def erasure(self, arg0: TypeMirror) -> TypeMirror: ...

  def getArrayType(self, arg0: TypeMirror) -> ArrayType: ...

  @overload
  def getDeclaredType(self, arg0: TypeElement, arg1: list[TypeMirror]) -> DeclaredType: ...

  @overload
  def getDeclaredType(self, arg0: DeclaredType, arg1: TypeElement, arg2: list[TypeMirror]) -> DeclaredType: ...

  def getNoType(self, arg0: TypeKind) -> NoType: ...

  def getNullType(self) -> NullType: ...

  def getPrimitiveType(self, arg0: TypeKind) -> PrimitiveType: ...

  def getWildcardType(self, arg0: TypeMirror, arg1: TypeMirror) -> WildcardType: ...

  def isAssignable(self, arg0: TypeMirror, arg1: TypeMirror) -> bool: ...

  def isSameType(self, arg0: TypeMirror, arg1: TypeMirror) -> bool: ...

  def isSubsignature(self, arg0: ExecutableType, arg1: ExecutableType) -> bool: ...

  def isSubtype(self, arg0: TypeMirror, arg1: TypeMirror) -> bool: ...

  def unboxedType(self, arg0: TypeMirror) -> PrimitiveType: ...

