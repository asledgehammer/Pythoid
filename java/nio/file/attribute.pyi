from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from java.time import Instant
from java.util.concurrent import TimeUnit
from javax.security.auth import Subject

T = TypeVar('T', default=Any)

class AttributeView:

  def name(self) -> str: ...


class BasicFileAttributeView:

  def name(self) -> str: ...

  def readAttributes(self) -> BasicFileAttributes: ...

  def setTimes(self, arg0: FileTime, arg1: FileTime, arg2: FileTime) -> None: ...


class BasicFileAttributes:

  def creationTime(self) -> FileTime: ...

  def fileKey(self) -> object: ...

  def isDirectory(self) -> bool: ...

  def isOther(self) -> bool: ...

  def isRegularFile(self) -> bool: ...

  def isSymbolicLink(self) -> bool: ...

  def lastAccessTime(self) -> FileTime: ...

  def lastModifiedTime(self) -> FileTime: ...

  def size(self) -> int: ...


class DosFileAttributeView:

  @overload
  def name(self) -> str: ...

  @overload
  def name(self) -> str: ...

  @overload
  def readAttributes(self) -> BasicFileAttributes: ...

  @overload
  def readAttributes(self) -> DosFileAttributes: ...

  @overload
  def readAttributes(self) -> BasicFileAttributes: ...

  def setArchive(self, arg0: bool) -> None: ...

  def setHidden(self, arg0: bool) -> None: ...

  def setReadOnly(self, arg0: bool) -> None: ...

  def setSystem(self, arg0: bool) -> None: ...

  def setTimes(self, arg0: FileTime, arg1: FileTime, arg2: FileTime) -> None: ...


class DosFileAttributes:

  def creationTime(self) -> FileTime: ...

  def fileKey(self) -> object: ...

  def isArchive(self) -> bool: ...

  def isDirectory(self) -> bool: ...

  def isHidden(self) -> bool: ...

  def isOther(self) -> bool: ...

  def isReadOnly(self) -> bool: ...

  def isRegularFile(self) -> bool: ...

  def isSymbolicLink(self) -> bool: ...

  def isSystem(self) -> bool: ...

  def lastAccessTime(self) -> FileTime: ...

  def lastModifiedTime(self) -> FileTime: ...

  def size(self) -> int: ...


class FileAttribute[T]:

  def name(self) -> str: ...

  def value(self) -> object: ...


class FileAttributeView:

  def name(self) -> str: ...


class FileStoreAttributeView:

  def name(self) -> str: ...


class FileTime:

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: FileTime) -> int: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def to(self, arg0: TimeUnit) -> int: ...

  def toInstant(self) -> Instant: ...

  def toMillis(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def fromMillis(arg0: int) -> FileTime: ...


class GroupPrincipal: ...


class PosixFilePermission(Enum):

  GROUP_EXECUTE: PosixFilePermission

  GROUP_READ: PosixFilePermission

  GROUP_WRITE: PosixFilePermission

  OTHERS_EXECUTE: PosixFilePermission

  OTHERS_READ: PosixFilePermission

  OTHERS_WRITE: PosixFilePermission

  OWNER_EXECUTE: PosixFilePermission

  OWNER_READ: PosixFilePermission

  OWNER_WRITE: PosixFilePermission

  @staticmethod
  def valueOf(arg0: str) -> PosixFilePermission: ...

  @staticmethod
  def values() -> list[PosixFilePermission]: ...


class UserPrincipal:

  def equals(self, arg0: object) -> bool: ...

  def getName(self) -> str: ...

  def hashCode(self) -> int: ...

  def implies(self, arg0: Subject) -> bool: ...

  def toString(self) -> str: ...


class UserPrincipalLookupService:

  def lookupPrincipalByGroupName(self, arg0: str) -> GroupPrincipal: ...

  def lookupPrincipalByName(self, arg0: str) -> UserPrincipal: ...

