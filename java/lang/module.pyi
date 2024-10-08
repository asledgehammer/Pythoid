from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import InputStream
from java.lang import Enum
from java.net import URI
from java.nio import ByteBuffer
from java.nio.file import Path
from java.util import Optional, Set, List, Collection
from java.util.function import Supplier
from java.util.stream import Stream

class Configuration:

  def findModule(self, arg0: str) -> Optional[ResolvedModule]: ...

  def modules(self) -> Set[ResolvedModule]: ...

  def parents(self) -> List[Configuration]: ...

  def resolve(self, arg0: ModuleFinder, arg1: ModuleFinder, arg2: Collection[str]) -> Configuration: ...

  def resolveAndBind(self, arg0: ModuleFinder, arg1: ModuleFinder, arg2: Collection[str]) -> Configuration: ...

  def toString(self) -> str: ...

  @staticmethod
  def empty() -> Configuration: ...


class ModuleDescriptor:

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: ModuleDescriptor) -> int: ...

  def equals(self, arg0: object) -> bool: ...

  def exports(self) -> Set[ModuleDescriptor.Exports]: ...

  def hashCode(self) -> int: ...

  def isAutomatic(self) -> bool: ...

  def isOpen(self) -> bool: ...

  def mainClass(self) -> Optional[str]: ...

  def modifiers(self) -> Set[ModuleDescriptor.Modifier]: ...

  def name(self) -> str: ...

  def opens(self) -> Set[ModuleDescriptor.Opens]: ...

  def packages(self) -> Set[str]: ...

  def provides(self) -> Set[ModuleDescriptor.Provides]: ...

  def rawVersion(self) -> Optional[str]: ...

  def requires(self) -> Set[ModuleDescriptor.Requires]: ...

  def toNameAndVersion(self) -> str: ...

  def toString(self) -> str: ...

  def uses(self) -> Set[str]: ...

  def version(self) -> Optional[ModuleDescriptor.Version]: ...

  @staticmethod
  def newAutomaticModule(arg0: str) -> ModuleDescriptor.Builder: ...

  @staticmethod
  @overload
  def newModule(arg0: str) -> ModuleDescriptor.Builder: ...

  @staticmethod
  @overload
  def newModule(arg0: str, arg1: Set[ModuleDescriptor.Modifier]) -> ModuleDescriptor.Builder: ...

  @staticmethod
  def newOpenModule(arg0: str) -> ModuleDescriptor.Builder: ...

  @staticmethod
  @overload
  def read(arg0: InputStream) -> ModuleDescriptor: ...

  @staticmethod
  @overload
  def read(arg0: ByteBuffer) -> ModuleDescriptor: ...

  @staticmethod
  @overload
  def read(arg0: InputStream, arg1: Supplier[Set[str]]) -> ModuleDescriptor: ...

  @staticmethod
  @overload
  def read(arg0: ByteBuffer, arg1: Supplier[Set[str]]) -> ModuleDescriptor: ...

  class Version:

    @overload
    def compareTo(self, arg0: object) -> int: ...

    @overload
    def compareTo(self, arg0: object) -> int: ...

    @overload
    def compareTo(self, arg0: ModuleDescriptor.Version) -> int: ...

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def toString(self) -> str: ...

    @staticmethod
    def parse(arg0: str) -> ModuleDescriptor.Version: ...

  class Modifier(Enum):

    AUTOMATIC: ModuleDescriptor.Modifier

    MANDATED: ModuleDescriptor.Modifier

    OPEN: ModuleDescriptor.Modifier

    SYNTHETIC: ModuleDescriptor.Modifier

    @staticmethod
    def valueOf(arg0: str) -> ModuleDescriptor.Modifier: ...

    @staticmethod
    def values() -> list[ModuleDescriptor.Modifier]: ...

  class Builder:

    def build(self) -> ModuleDescriptor: ...

    @overload
    def exports(self, arg0: str) -> ModuleDescriptor.Builder: ...

    @overload
    def exports(self, arg0: ModuleDescriptor.Exports) -> ModuleDescriptor.Builder: ...

    @overload
    def exports(self, arg0: str, arg1: Set[str]) -> ModuleDescriptor.Builder: ...

    @overload
    def exports(self, arg0: Set[ModuleDescriptor.Exports.Modifier], arg1: str) -> ModuleDescriptor.Builder: ...

    @overload
    def exports(self, arg0: Set[ModuleDescriptor.Exports.Modifier], arg1: str, arg2: Set[str]) -> ModuleDescriptor.Builder: ...

    def mainClass(self, arg0: str) -> ModuleDescriptor.Builder: ...

    @overload
    def opens(self, arg0: str) -> ModuleDescriptor.Builder: ...

    @overload
    def opens(self, arg0: ModuleDescriptor.Opens) -> ModuleDescriptor.Builder: ...

    @overload
    def opens(self, arg0: str, arg1: Set[str]) -> ModuleDescriptor.Builder: ...

    @overload
    def opens(self, arg0: Set[ModuleDescriptor.Opens.Modifier], arg1: str) -> ModuleDescriptor.Builder: ...

    @overload
    def opens(self, arg0: Set[ModuleDescriptor.Opens.Modifier], arg1: str, arg2: Set[str]) -> ModuleDescriptor.Builder: ...

    def packages(self, arg0: Set[str]) -> ModuleDescriptor.Builder: ...

    @overload
    def provides(self, arg0: ModuleDescriptor.Provides) -> ModuleDescriptor.Builder: ...

    @overload
    def provides(self, arg0: str, arg1: List[str]) -> ModuleDescriptor.Builder: ...

    @overload
    def requires(self, arg0: str) -> ModuleDescriptor.Builder: ...

    @overload
    def requires(self, arg0: ModuleDescriptor.Requires) -> ModuleDescriptor.Builder: ...

    @overload
    def requires(self, arg0: Set[ModuleDescriptor.Requires.Modifier], arg1: str) -> ModuleDescriptor.Builder: ...

    @overload
    def requires(self, arg0: Set[ModuleDescriptor.Requires.Modifier], arg1: str, arg2: ModuleDescriptor.Version) -> ModuleDescriptor.Builder: ...

    def uses(self, arg0: str) -> ModuleDescriptor.Builder: ...

    @overload
    def version(self, arg0: str) -> ModuleDescriptor.Builder: ...

    @overload
    def version(self, arg0: ModuleDescriptor.Version) -> ModuleDescriptor.Builder: ...

  class Provides:

    @overload
    def compareTo(self, arg0: object) -> int: ...

    @overload
    def compareTo(self, arg0: object) -> int: ...

    @overload
    def compareTo(self, arg0: ModuleDescriptor.Provides) -> int: ...

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def providers(self) -> List[str]: ...

    def service(self) -> str: ...

    def toString(self) -> str: ...

  class Opens:

    @overload
    def compareTo(self, arg0: object) -> int: ...

    @overload
    def compareTo(self, arg0: object) -> int: ...

    @overload
    def compareTo(self, arg0: ModuleDescriptor.Opens) -> int: ...

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def isQualified(self) -> bool: ...

    def modifiers(self) -> Set[ModuleDescriptor.Opens.Modifier]: ...

    def source(self) -> str: ...

    def targets(self) -> Set[str]: ...

    def toString(self) -> str: ...

    class Modifier(Enum):

      MANDATED: ModuleDescriptor.Opens.Modifier

      SYNTHETIC: ModuleDescriptor.Opens.Modifier

      @staticmethod
      def valueOf(arg0: str) -> ModuleDescriptor.Opens.Modifier: ...

      @staticmethod
      def values() -> list[ModuleDescriptor.Opens.Modifier]: ...

  class Exports:

    @overload
    def compareTo(self, arg0: object) -> int: ...

    @overload
    def compareTo(self, arg0: object) -> int: ...

    @overload
    def compareTo(self, arg0: ModuleDescriptor.Exports) -> int: ...

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def isQualified(self) -> bool: ...

    def modifiers(self) -> Set[ModuleDescriptor.Exports.Modifier]: ...

    def source(self) -> str: ...

    def targets(self) -> Set[str]: ...

    def toString(self) -> str: ...

    class Modifier(Enum):

      MANDATED: ModuleDescriptor.Exports.Modifier

      SYNTHETIC: ModuleDescriptor.Exports.Modifier

      @staticmethod
      def valueOf(arg0: str) -> ModuleDescriptor.Exports.Modifier: ...

      @staticmethod
      def values() -> list[ModuleDescriptor.Exports.Modifier]: ...

  class Requires:

    @overload
    def compareTo(self, arg0: object) -> int: ...

    @overload
    def compareTo(self, arg0: object) -> int: ...

    @overload
    def compareTo(self, arg0: ModuleDescriptor.Requires) -> int: ...

    def compiledVersion(self) -> Optional[ModuleDescriptor.Version]: ...

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def modifiers(self) -> Set[ModuleDescriptor.Requires.Modifier]: ...

    def name(self) -> str: ...

    def rawCompiledVersion(self) -> Optional[str]: ...

    def toString(self) -> str: ...

    class Modifier(Enum):

      MANDATED: ModuleDescriptor.Requires.Modifier

      STATIC: ModuleDescriptor.Requires.Modifier

      SYNTHETIC: ModuleDescriptor.Requires.Modifier

      TRANSITIVE: ModuleDescriptor.Requires.Modifier

      @staticmethod
      def valueOf(arg0: str) -> ModuleDescriptor.Requires.Modifier: ...

      @staticmethod
      def values() -> list[ModuleDescriptor.Requires.Modifier]: ...


class ModuleFinder:

  def find(self, arg0: str) -> Optional[ModuleReference]: ...

  def findAll(self) -> Set[ModuleReference]: ...

  @staticmethod
  def compose(arg0: list[ModuleFinder]) -> ModuleFinder: ...

  @staticmethod
  def of(arg0: list[Path]) -> ModuleFinder: ...

  @staticmethod
  def ofSystem() -> ModuleFinder: ...


class ModuleReader:

  @overload
  def close(self) -> None: ...

  @overload
  def close(self) -> None: ...

  def find(self, arg0: str) -> Optional[URI]: ...

  def list(self) -> Stream[str]: ...

  def open(self, arg0: str) -> Optional[InputStream]: ...

  def read(self, arg0: str) -> Optional[ByteBuffer]: ...

  def release(self, arg0: ByteBuffer) -> None: ...


class ModuleReference:

  def descriptor(self) -> ModuleDescriptor: ...

  def location(self) -> Optional[URI]: ...

  def open(self) -> ModuleReader: ...


class ResolvedModule:

  def configuration(self) -> Configuration: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def name(self) -> str: ...

  def reads(self) -> Set[ResolvedModule]: ...

  def reference(self) -> ModuleReference: ...

  def toString(self) -> str: ...


class Resolver: ...

