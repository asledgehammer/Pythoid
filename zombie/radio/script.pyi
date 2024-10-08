from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from zombie.radio.globals import RadioGlobal, CompareMethod, CompareResult

class ConditionContainer:

  @overload
  def Add(self, container: ConditionContainer) -> None: ...

  @overload
  def Add(self, A: RadioGlobal, B: RadioGlobal, compareMethod: CompareMethod, nextOperator: OperatorType) -> None: ...

  @overload
  def Evaluate(self) -> CompareResult: ...

  @overload
  def Evaluate(self) -> CompareResult: ...

  @overload
  def getNextOperator(self) -> OperatorType: ...

  @overload
  def getNextOperator(self) -> OperatorType: ...

  @overload
  def setNextOperator(self, operatorType: OperatorType) -> None: ...

  @overload
  def setNextOperator(self, operatorType: OperatorType) -> None: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, operator: OperatorType): ...

  class Condition:

    @overload
    def Evaluate(self) -> CompareResult: ...

    @overload
    def Evaluate(self) -> CompareResult: ...

    @overload
    def getNextOperator(self) -> OperatorType: ...

    @overload
    def getNextOperator(self) -> OperatorType: ...

    @overload
    def setNextOperator(self, arg0: OperatorType) -> None: ...

    @overload
    def setNextOperator(self, arg0: OperatorType) -> None: ...

    @overload
    def __init__(self, arg0: RadioGlobal, arg1: RadioGlobal, arg2: CompareMethod): ...
    @overload
    def __init__(self, arg0: RadioGlobal, arg1: RadioGlobal, arg2: CompareMethod, arg3: OperatorType): ...


class ConditionIter:

  def Evaluate(self) -> CompareResult: ...

  def getNextOperator(self) -> OperatorType: ...

  def setNextOperator(self, operatorType: OperatorType) -> None: ...


class ExitOptionOld:

  def addScriptEntry(self, entry: RadioScriptEntry) -> None: ...

  def evaluate(self) -> RadioScriptEntry: ...

  def setCondition(self, conditionContainer: ConditionContainer) -> None: ...

  def __init__(self, parentName: str, name: str): ...


class OperatorType(Enum):

  NONE: OperatorType

  @staticmethod
  def valueOf(arg0: str) -> OperatorType: ...

  @staticmethod
  def values() -> list[OperatorType]: ...


class RadioScriptEntry:

  def getChanceMax(self) -> int: ...

  def getChanceMin(self) -> int: ...

  def getDelay(self) -> int: ...

  def getScriptName(self) -> str: ...

  def setChanceMax(self, max: int) -> None: ...

  def setChanceMin(self, min: int) -> None: ...

  def setDelay(self, delay: int) -> None: ...

  def setScriptName(self, name: str) -> None: ...

  @overload
  def __init__(self, name: str, delay: int): ...
  @overload
  def __init__(self, name: str, delay: int, min: int, max: int): ...


class RadioScriptInfo:

  def addExitOption(self, exitOption: ExitOptionOld) -> None: ...

  def getNextScript(self) -> RadioScriptEntry: ...

  def __init__(self): ...

