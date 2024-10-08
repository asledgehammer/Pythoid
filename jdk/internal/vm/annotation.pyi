from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class

class DontInline:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...


class ForceInline:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...


class Hidden:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...


class IntrinsicCandidate:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...


class ReservedStackAccess:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...

