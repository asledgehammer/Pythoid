from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt.datatransfer import DataFlavor
from java.io import OutputStream, InputStream
from java.lang import ClassLoader
from java.net import URL

class CommandInfo:

  def getCommandClass(self) -> str: ...

  def getCommandName(self) -> str: ...

  def getCommandObject(self, arg0: DataHandler, arg1: ClassLoader) -> object: ...

  def __init__(self, arg0: str, arg1: str): ...

  class Beans: ...


class CommandMap:

  @overload
  def createDataContentHandler(self, arg0: str) -> DataContentHandler: ...

  @overload
  def createDataContentHandler(self, arg0: str, arg1: DataSource) -> DataContentHandler: ...

  @overload
  def getAllCommands(self, arg0: str) -> list[CommandInfo]: ...

  @overload
  def getAllCommands(self, arg0: str, arg1: DataSource) -> list[CommandInfo]: ...

  @overload
  def getCommand(self, arg0: str, arg1: str) -> CommandInfo: ...

  @overload
  def getCommand(self, arg0: str, arg1: str, arg2: DataSource) -> CommandInfo: ...

  def getMimeTypes(self) -> list[str]: ...

  @overload
  def getPreferredCommands(self, arg0: str) -> list[CommandInfo]: ...

  @overload
  def getPreferredCommands(self, arg0: str, arg1: DataSource) -> list[CommandInfo]: ...

  @staticmethod
  def getDefaultCommandMap() -> CommandMap: ...

  @staticmethod
  def setDefaultCommandMap(arg0: CommandMap) -> None: ...

  def __init__(self): ...


class DataContentHandler:

  def getContent(self, arg0: DataSource) -> object: ...

  def getTransferData(self, arg0: DataFlavor, arg1: DataSource) -> object: ...

  def getTransferDataFlavors(self) -> list[DataFlavor]: ...

  def writeTo(self, arg0: object, arg1: str, arg2: OutputStream) -> None: ...


class DataContentHandlerFactory:

  def createDataContentHandler(self, arg0: str) -> DataContentHandler: ...


class DataHandler:

  def getAllCommands(self) -> list[CommandInfo]: ...

  def getBean(self, arg0: CommandInfo) -> object: ...

  def getCommand(self, arg0: str) -> CommandInfo: ...

  def getContent(self) -> object: ...

  def getContentType(self) -> str: ...

  def getDataSource(self) -> DataSource: ...

  def getInputStream(self) -> InputStream: ...

  def getName(self) -> str: ...

  def getOutputStream(self) -> OutputStream: ...

  def getPreferredCommands(self) -> list[CommandInfo]: ...

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

  def setCommandMap(self, arg0: CommandMap) -> None: ...

  def writeTo(self, arg0: OutputStream) -> None: ...

  @staticmethod
  def setDataContentHandlerFactory(arg0: DataContentHandlerFactory) -> None: ...

  @overload
  def __init__(self, arg0: URL): ...
  @overload
  def __init__(self, arg0: DataSource): ...
  @overload
  def __init__(self, arg0: object, arg1: str): ...


class DataSource:

  def getContentType(self) -> str: ...

  def getInputStream(self) -> InputStream: ...

  def getName(self) -> str: ...

  def getOutputStream(self) -> OutputStream: ...

