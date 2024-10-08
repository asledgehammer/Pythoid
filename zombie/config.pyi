from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import ArrayList

class BooleanConfigOption(ConfigOption):

  def getDefaultValue(self) -> bool: ...

  def getTooltip(self) -> str: ...

  def getType(self) -> str: ...

  def getValue(self) -> bool: ...

  def getValueAsObject(self) -> object: ...

  def getValueAsString(self) -> str: ...

  def isValidString(self, s: str) -> bool: ...

  def parse(self, s: str) -> None: ...

  def resetToDefault(self) -> None: ...

  def setDefaultToCurrentValue(self) -> None: ...

  def setValue(self, value: bool) -> None: ...

  def setValueFromObject(self, o: object) -> None: ...

  def __init__(self, name: str, defaultValue: bool): ...


class ConfigFile:

  def getOptions(self) -> ArrayList[ConfigOption]: ...

  def getVersion(self) -> int: ...

  def read(self, fileName: str) -> bool: ...

  def write(self, fileName: str, version: int, options: ArrayList[ConfigOption]) -> bool: ...

  def __init__(self): ...


class ConfigOption:

  def getName(self) -> str: ...

  def getTooltip(self) -> str: ...

  def getType(self) -> str: ...

  def getValueAsLuaString(self) -> str: ...

  def getValueAsObject(self) -> object: ...

  def getValueAsString(self) -> str: ...

  def isValidString(self, s: str) -> bool: ...

  def parse(self, s: str) -> None: ...

  def resetToDefault(self) -> None: ...

  def setDefaultToCurrentValue(self) -> None: ...

  def setValueFromObject(self, o: object) -> None: ...

  def __init__(self, name: str): ...


class DoubleConfigOption(ConfigOption):

  def getDefaultValue(self) -> float: ...

  def getMax(self) -> float: ...

  def getMin(self) -> float: ...

  def getTooltip(self) -> str: ...

  def getType(self) -> str: ...

  def getValue(self) -> float: ...

  def getValueAsObject(self) -> object: ...

  def getValueAsString(self) -> str: ...

  def isValidString(self, s: str) -> bool: ...

  def parse(self, s: str) -> None: ...

  def resetToDefault(self) -> None: ...

  def setDefaultToCurrentValue(self) -> None: ...

  def setValue(self, value: float) -> None: ...

  def setValueFromObject(self, o: object) -> None: ...

  def __init__(self, name: str, min: float, max: float, defaultValue: float): ...


class EnumConfigOption(IntegerConfigOption):

  def getNumValues(self) -> int: ...

  def getType(self) -> str: ...

  def __init__(self, name: str, numValues: int, defaultValue: int): ...


class IntegerConfigOption(ConfigOption):

  def getDefaultValue(self) -> int: ...

  def getMax(self) -> float: ...

  def getMin(self) -> float: ...

  def getTooltip(self) -> str: ...

  def getType(self) -> str: ...

  def getValue(self) -> int: ...

  def getValueAsObject(self) -> object: ...

  def getValueAsString(self) -> str: ...

  def isValidString(self, s: str) -> bool: ...

  def parse(self, s: str) -> None: ...

  def resetToDefault(self) -> None: ...

  def setDefaultToCurrentValue(self) -> None: ...

  def setValue(self, value: int) -> None: ...

  def setValueFromObject(self, o: object) -> None: ...

  def __init__(self, name: str, min: int, max: int, defaultValue: int): ...


class StringConfigOption(ConfigOption):

  def getDefaultValue(self) -> str: ...

  def getTooltip(self) -> str: ...

  def getType(self) -> str: ...

  def getValue(self) -> str: ...

  def getValueAsLuaString(self) -> str: ...

  def getValueAsObject(self) -> object: ...

  def getValueAsString(self) -> str: ...

  def isValidString(self, s: str) -> bool: ...

  def parse(self, s: str) -> None: ...

  def resetToDefault(self) -> None: ...

  def setDefaultToCurrentValue(self) -> None: ...

  def setValue(self, value: str) -> None: ...

  def setValueFromObject(self, o: object) -> None: ...

  def __init__(self, name: str, defaultValue: str, maxLength: int): ...

