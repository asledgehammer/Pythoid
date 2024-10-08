from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import AWTEvent, Component, Rectangle
from java.awt.font import TextAttribute, TextHitInfo
from java.lang import Character
from java.text import AttributedCharacterIterator
from java.util import Locale, Map

class InputContext:

  def dispatchEvent(self, arg0: AWTEvent) -> None: ...

  def dispose(self) -> None: ...

  def endComposition(self) -> None: ...

  def getInputMethodControlObject(self) -> object: ...

  def getLocale(self) -> Locale: ...

  def isCompositionEnabled(self) -> bool: ...

  def reconvert(self) -> None: ...

  def removeNotify(self, arg0: Component) -> None: ...

  def selectInputMethod(self, arg0: Locale) -> bool: ...

  def setCharacterSubsets(self, arg0: list[Character.Subset]) -> None: ...

  def setCompositionEnabled(self, arg0: bool) -> None: ...

  @staticmethod
  def getInstance() -> InputContext: ...


class InputMethodHighlight:

  CONVERTED_TEXT: int

  RAW_TEXT: int

  SELECTED_CONVERTED_TEXT_HIGHLIGHT: InputMethodHighlight

  SELECTED_RAW_TEXT_HIGHLIGHT: InputMethodHighlight

  UNSELECTED_CONVERTED_TEXT_HIGHLIGHT: InputMethodHighlight

  UNSELECTED_RAW_TEXT_HIGHLIGHT: InputMethodHighlight

  def getState(self) -> int: ...

  def getStyle(self) -> Map[TextAttribute, Any]: ...

  def getVariation(self) -> int: ...

  def isSelected(self) -> bool: ...

  @overload
  def __init__(self, arg0: bool, arg1: int): ...
  @overload
  def __init__(self, arg0: bool, arg1: int, arg2: int): ...
  @overload
  def __init__(self, arg0: bool, arg1: int, arg2: int, arg3: Map[TextAttribute, Any]): ...


class InputMethodRequests:

  def cancelLatestCommittedText(self, arg0: list[AttributedCharacterIterator.Attribute]) -> AttributedCharacterIterator: ...

  def getCommittedText(self, arg0: int, arg1: int, arg2: list[AttributedCharacterIterator.Attribute]) -> AttributedCharacterIterator: ...

  def getCommittedTextLength(self) -> int: ...

  def getInsertPositionOffset(self) -> int: ...

  def getLocationOffset(self, arg0: int, arg1: int) -> TextHitInfo: ...

  def getSelectedText(self, arg0: list[AttributedCharacterIterator.Attribute]) -> AttributedCharacterIterator: ...

  def getTextLocation(self, arg0: TextHitInfo) -> Rectangle: ...

