from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation

class Cylinder(Quadric):

  def draw(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int) -> None: ...

  def __init__(self): ...


class Quadric:

  def getDrawStyle(self) -> int: ...

  def getNormals(self) -> int: ...

  def getOrientation(self) -> int: ...

  def getTextureFlag(self) -> bool: ...

  def setDrawStyle(self, arg0: int) -> None: ...

  def setNormals(self, arg0: int) -> None: ...

  def setOrientation(self, arg0: int) -> None: ...

  def setTextureFlag(self, arg0: bool) -> None: ...

  def __init__(self): ...
