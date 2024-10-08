from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt.datatransfer import DataFlavor, Transferable, FlavorTable, FlavorMap
from java.io import InputStream
from java.lang import Long
from java.util import Map, Set, SortedMap, LinkedHashSet

class DataTransferer:

  javaTextEncodingFlavor: DataFlavor

  def convertData(self, arg0: object, arg1: Transferable, arg2: int, arg3: Map[Long, DataFlavor], arg4: bool) -> list[int]: ...

  def getDefaultUnicodeEncoding(self) -> str: ...

  def getFlavorsForFormats(self, arg0: list[int], arg1: FlavorTable) -> Map[DataFlavor, Long]: ...

  def getFlavorsForFormatsAsArray(self, arg0: list[int], arg1: FlavorTable) -> list[DataFlavor]: ...

  def getFlavorsForFormatsAsSet(self, arg0: list[int], arg1: FlavorTable) -> Set[DataFlavor]: ...

  def getFormatsForFlavors(self, arg0: list[DataFlavor], arg1: FlavorTable) -> SortedMap[Long, DataFlavor]: ...

  def getFormatsForTransferable(self, arg0: Transferable, arg1: FlavorTable) -> SortedMap[Long, DataFlavor]: ...

  def getFormatsForTransferableAsArray(self, arg0: Transferable, arg1: FlavorTable) -> list[int]: ...

  def getPlatformMappingsForFlavor(self, arg0: DataFlavor) -> LinkedHashSet[str]: ...

  def getPlatformMappingsForNative(self, arg0: str) -> LinkedHashSet[DataFlavor]: ...

  def getToolkitThreadBlockedHandler(self) -> ToolkitThreadBlockedHandler: ...

  def isFileFormat(self, arg0: int) -> bool: ...

  def isImageFormat(self, arg0: int) -> bool: ...

  def isLocaleDependentTextFormat(self, arg0: int) -> bool: ...

  def processDataConversionRequests(self) -> None: ...

  def registerTextFlavorProperties(self, arg0: str, arg1: str, arg2: str, arg3: str) -> None: ...

  def translateBytes(self, arg0: list[int], arg1: DataFlavor, arg2: int, arg3: Transferable) -> object: ...

  def translateStream(self, arg0: InputStream, arg1: DataFlavor, arg2: int, arg3: Transferable) -> object: ...

  def translateTransferable(self, arg0: Transferable, arg1: DataFlavor, arg2: int) -> list[int]: ...

  @staticmethod
  def adaptFlavorMap(arg0: FlavorMap) -> FlavorTable: ...

  @staticmethod
  def getInstance() -> DataTransferer: ...

  @staticmethod
  def keysToLongArray(arg0: SortedMap[Long, Any]) -> list[int]: ...

  @staticmethod
  def setToSortedDataFlavorArray(arg0: Set[DataFlavor]) -> list[DataFlavor]: ...

  def __init__(self): ...

  class ReencodingInputStream(InputStream):

    def available(self) -> int: ...

    def close(self) -> None: ...

    def read(self) -> int: ...

    def __init__(self, arg0: DataTransferer, arg1: InputStream, arg2: int, arg3: str, arg4: Transferable): ...


class ToolkitThreadBlockedHandler:

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def lock(self) -> None: ...

  def unlock(self) -> None: ...


class TransferableProxy:

  @overload
  def getTransferData(self, arg0: DataFlavor) -> object: ...

  @overload
  def getTransferData(self, arg0: DataFlavor) -> object: ...

  @overload
  def getTransferDataFlavors(self) -> list[DataFlavor]: ...

  @overload
  def getTransferDataFlavors(self) -> list[DataFlavor]: ...

  @overload
  def isDataFlavorSupported(self, arg0: DataFlavor) -> bool: ...

  @overload
  def isDataFlavorSupported(self, arg0: DataFlavor) -> bool: ...

  def __init__(self, arg0: Transferable, arg1: bool): ...

