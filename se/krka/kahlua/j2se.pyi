from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import DataInputStream, DataOutputStream
from java.nio import ByteBuffer
from java.util import Map
from se.krka.kahlua.vm import KahluaTable, KahluaTableIterator, LuaCallFrame, Platform

class J2SEPlatform:

  @overload
  def newEnvironment(self) -> KahluaTable: ...

  @overload
  def newEnvironment(self) -> KahluaTable: ...

  @overload
  def newTable(self) -> KahluaTable: ...

  @overload
  def newTable(self) -> KahluaTable: ...

  @overload
  def pow(self, arg0: float, arg1: float) -> float: ...

  @overload
  def pow(self, arg0: float, arg1: float) -> float: ...

  @overload
  def setupEnvironment(self, arg0: KahluaTable) -> None: ...

  @overload
  def setupEnvironment(self, arg0: KahluaTable) -> None: ...

  @staticmethod
  def getInstance() -> J2SEPlatform: ...

  def __init__(self): ...


class KahluaTableImpl:

  @overload
  def getMetatable(self) -> KahluaTable: ...

  @overload
  def getMetatable(self) -> KahluaTable: ...

  def getRewriteTable(self) -> KahluaTableImpl: ...

  @overload
  def getString(self, arg0: str) -> str: ...

  @overload
  def getString(self, arg0: str) -> str: ...

  @overload
  def isEmpty(self) -> bool: ...

  @overload
  def isEmpty(self) -> bool: ...

  @overload
  def iterator(self) -> KahluaTableIterator: ...

  @overload
  def iterator(self) -> KahluaTableIterator: ...

  @overload
  def len(self) -> int: ...

  @overload
  def len(self) -> int: ...

  @overload
  def load(self, arg0: DataInputStream, arg1: int) -> None: ...

  @overload
  def load(self, arg0: DataInputStream, arg1: int) -> None: ...

  @overload
  def load(self, arg0: ByteBuffer, arg1: int) -> None: ...

  @overload
  def load(self, arg0: ByteBuffer, arg1: int) -> None: ...

  @overload
  def load(self, arg0: DataInputStream, arg1: int, arg2: int) -> object: ...

  @overload
  def load(self, arg0: ByteBuffer, arg1: int, arg2: int) -> object: ...

  @overload
  def rawget(self, arg0: int) -> object: ...

  @overload
  def rawget(self, arg0: int) -> object: ...

  @overload
  def rawget(self, arg0: object) -> object: ...

  @overload
  def rawget(self, arg0: object) -> object: ...

  def rawgetBool(self, arg0: object) -> bool: ...

  def rawgetFloat(self, arg0: object) -> float: ...

  def rawgetInt(self, arg0: object) -> int: ...

  def rawgetStr(self, arg0: object) -> str: ...

  @overload
  def rawset(self, arg0: int, arg1: object) -> None: ...

  @overload
  def rawset(self, arg0: int, arg1: object) -> None: ...

  @overload
  def rawset(self, arg0: object, arg1: object) -> None: ...

  @overload
  def rawset(self, arg0: object, arg1: object) -> None: ...

  @overload
  def save(self, arg0: DataOutputStream) -> None: ...

  @overload
  def save(self, arg0: DataOutputStream) -> None: ...

  @overload
  def save(self, arg0: ByteBuffer) -> None: ...

  @overload
  def save(self, arg0: ByteBuffer) -> None: ...

  @overload
  def setMetatable(self, arg0: KahluaTable) -> None: ...

  @overload
  def setMetatable(self, arg0: KahluaTable) -> None: ...

  def setRewriteTable(self, arg0: object) -> None: ...

  @overload
  def size(self) -> int: ...

  @overload
  def size(self) -> int: ...

  def toString(self) -> str: ...

  @overload
  def wipe(self) -> None: ...

  @overload
  def wipe(self) -> None: ...

  @staticmethod
  def canSave(arg0: object, arg1: object) -> bool: ...

  def __init__(self, arg0: Map[object, object]):
    self.delegate: Map[object, object]


class MathLib:

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def isNegative(arg0: float) -> bool: ...

  @staticmethod
  def register(arg0: Platform, arg1: KahluaTable) -> None: ...

  @staticmethod
  def round(arg0: float) -> float: ...

  def __init__(self, arg0: int): ...

