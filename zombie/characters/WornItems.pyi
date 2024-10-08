from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import ArrayList
from java.util.function import Consumer
from zombie.core.skinnedmodel.visual import ItemVisuals
from zombie.inventory import InventoryItem, ItemContainer

class BodyLocation:

  def addAlias(self, alias: str) -> BodyLocation: ...

  def getId(self) -> str: ...

  def isExclusive(self, id: str) -> bool: ...

  def isHideModel(self, otherId: str) -> bool: ...

  def isID(self, id: str) -> bool: ...

  def isMultiItem(self) -> bool: ...

  def setExclusive(self, otherId: str) -> BodyLocation: ...

  def setHideModel(self, otherId: str) -> BodyLocation: ...

  def setMultiItem(self, bMultiItem: bool) -> BodyLocation: ...

  def __init__(self, group: BodyLocationGroup, id: str): ...


class BodyLocationGroup:

  def checkValid(self, locationId: str) -> None: ...

  def getAllLocations(self) -> ArrayList[BodyLocation]: ...

  def getLocation(self, locationId: str) -> BodyLocation: ...

  def getLocationByIndex(self, index: int) -> BodyLocation: ...

  def getLocationNotNull(self, locationId: str) -> BodyLocation: ...

  def getOrCreateLocation(self, locationId: str) -> BodyLocation: ...

  def indexOf(self, locationId: str) -> int: ...

  def isExclusive(self, firstId: str, secondId: str) -> bool: ...

  def isHideModel(self, firstId: str, secondId: str) -> bool: ...

  def isMultiItem(self, locationId: str) -> bool: ...

  def setExclusive(self, firstId: str, secondId: str) -> None: ...

  def setHideModel(self, firstId: str, secondId: str) -> None: ...

  def setMultiItem(self, locationId: str, bMultiItem: bool) -> None: ...

  def size(self) -> int: ...

  def __init__(self, id: str): ...


class BodyLocations:

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getGroup(id: str) -> BodyLocationGroup: ...

  def __init__(self): ...


class WornItem:

  def getItem(self) -> InventoryItem: ...

  def getLocation(self) -> str: ...

  def __init__(self, location: str, item: InventoryItem): ...


class WornItems:

  def addItemsToItemContainer(self, container: ItemContainer) -> None: ...

  def clear(self) -> None: ...

  def contains(self, item: InventoryItem) -> bool: ...

  def copyFrom(self, other: WornItems) -> None: ...

  def forEach(self, c: Consumer[WornItem]) -> None: ...

  def get(self, index: int) -> WornItem: ...

  def getBodyLocationGroup(self) -> BodyLocationGroup: ...

  def getItem(self, location: str) -> InventoryItem: ...

  def getItemByIndex(self, index: int) -> InventoryItem: ...

  def getItemVisuals(self, itemVisuals: ItemVisuals) -> None: ...

  def getLocation(self, item: InventoryItem) -> str: ...

  def isEmpty(self) -> bool: ...

  def remove(self, item: InventoryItem) -> None: ...

  def setFromItemVisuals(self, itemVisuals: ItemVisuals) -> None: ...

  def setItem(self, location: str, item: InventoryItem) -> None: ...

  def size(self) -> int: ...

  @overload
  def __init__(self, group: BodyLocationGroup): ...
  @overload
  def __init__(self, other: WornItems): ...

