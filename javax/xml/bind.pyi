from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import PrintStream, PrintWriter, File, OutputStream, Writer, InputStream, Reader
from java.lang import Class, Exception, Throwable
from java.net import URL
from javax.xml.bind.annotation.adapters import XmlAdapter
from javax.xml.bind.attachment import AttachmentMarshaller, AttachmentUnmarshaller
from javax.xml.namespace import QName
from javax.xml.stream import XMLEventWriter, XMLStreamWriter, XMLEventReader, XMLStreamReader
from javax.xml.transform import Result, Source
from javax.xml.validation import Schema
from org.w3c.dom import Node
from org.xml.sax import ContentHandler, InputSource, Locator, Attributes

T = TypeVar('T', default=Any)
A = TypeVar('A', default=Any)

class JAXBElement[T]:

  def getDeclaredType(self) -> Class[T]: ...

  def getName(self) -> QName: ...

  def getScope(self) -> Class: ...

  def getValue(self) -> object: ...

  def isGlobalScope(self) -> bool: ...

  def isNil(self) -> bool: ...

  def isTypeSubstituted(self) -> bool: ...

  def setNil(self, arg0: bool) -> None: ...

  def setValue(self, arg0: object) -> None: ...

  @overload
  def __init__(self, arg0: QName, arg1: Class[T], arg2: object): ...
  @overload
  def __init__(self, arg0: QName, arg1: Class[T], arg2: Class, arg3: object): ...

  class GlobalScope:

    def __init__(self): ...


class JAXBException(Exception):

  def getCause(self) -> Throwable: ...

  def getErrorCode(self) -> str: ...

  def getLinkedException(self) -> Throwable: ...

  @overload
  def printStackTrace(self) -> None: ...

  @overload
  def printStackTrace(self, arg0: PrintStream) -> None: ...

  @overload
  def printStackTrace(self, arg0: PrintWriter) -> None: ...

  def setLinkedException(self, arg0: Throwable) -> None: ...

  def toString(self) -> str: ...

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: str): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: str, arg2: Throwable): ...


class Marshaller:

  JAXB_ENCODING: str

  JAXB_FORMATTED_OUTPUT: str

  JAXB_FRAGMENT: str

  JAXB_NO_NAMESPACE_SCHEMA_LOCATION: str

  JAXB_SCHEMA_LOCATION: str

  def getAdapter(self, arg0: Class[A]) -> A: ...

  def getAttachmentMarshaller(self) -> AttachmentMarshaller: ...

  def getEventHandler(self) -> ValidationEventHandler: ...

  def getListener(self) -> Marshaller.Listener: ...

  def getNode(self, arg0: object) -> Node: ...

  def getProperty(self, arg0: str) -> object: ...

  def getSchema(self) -> Schema: ...

  @overload
  def marshal(self, arg0: object, arg1: File) -> None: ...

  @overload
  def marshal(self, arg0: object, arg1: OutputStream) -> None: ...

  @overload
  def marshal(self, arg0: object, arg1: Writer) -> None: ...

  @overload
  def marshal(self, arg0: object, arg1: XMLEventWriter) -> None: ...

  @overload
  def marshal(self, arg0: object, arg1: XMLStreamWriter) -> None: ...

  @overload
  def marshal(self, arg0: object, arg1: Result) -> None: ...

  @overload
  def marshal(self, arg0: object, arg1: Node) -> None: ...

  @overload
  def marshal(self, arg0: object, arg1: ContentHandler) -> None: ...

  @overload
  def setAdapter(self, arg0: XmlAdapter) -> None: ...

  @overload
  def setAdapter(self, arg0: Class[A], arg1: A) -> None: ...

  def setAttachmentMarshaller(self, arg0: AttachmentMarshaller) -> None: ...

  def setEventHandler(self, arg0: ValidationEventHandler) -> None: ...

  def setListener(self, arg0: Marshaller.Listener) -> None: ...

  def setProperty(self, arg0: str, arg1: object) -> None: ...

  def setSchema(self, arg0: Schema) -> None: ...

  class Listener:

    def afterMarshal(self, arg0: object) -> None: ...

    def beforeMarshal(self, arg0: object) -> None: ...

    def __init__(self): ...


class Unmarshaller:

  def getAdapter(self, arg0: Class[A]) -> A: ...

  def getAttachmentUnmarshaller(self) -> AttachmentUnmarshaller: ...

  def getEventHandler(self) -> ValidationEventHandler: ...

  def getListener(self) -> Unmarshaller.Listener: ...

  def getProperty(self, arg0: str) -> object: ...

  def getSchema(self) -> Schema: ...

  def getUnmarshallerHandler(self) -> UnmarshallerHandler: ...

  def isValidating(self) -> bool: ...

  @overload
  def setAdapter(self, arg0: XmlAdapter) -> None: ...

  @overload
  def setAdapter(self, arg0: Class[A], arg1: A) -> None: ...

  def setAttachmentUnmarshaller(self, arg0: AttachmentUnmarshaller) -> None: ...

  def setEventHandler(self, arg0: ValidationEventHandler) -> None: ...

  def setListener(self, arg0: Unmarshaller.Listener) -> None: ...

  def setProperty(self, arg0: str, arg1: object) -> None: ...

  def setSchema(self, arg0: Schema) -> None: ...

  def setValidating(self, arg0: bool) -> None: ...

  @overload
  def unmarshal(self, arg0: File) -> object: ...

  @overload
  def unmarshal(self, arg0: InputStream) -> object: ...

  @overload
  def unmarshal(self, arg0: Reader) -> object: ...

  @overload
  def unmarshal(self, arg0: URL) -> object: ...

  @overload
  def unmarshal(self, arg0: XMLEventReader) -> object: ...

  @overload
  def unmarshal(self, arg0: XMLStreamReader) -> object: ...

  @overload
  def unmarshal(self, arg0: Source) -> object: ...

  @overload
  def unmarshal(self, arg0: Node) -> object: ...

  @overload
  def unmarshal(self, arg0: InputSource) -> object: ...

  @overload
  def unmarshal(self, arg0: XMLEventReader, arg1: Class[T]) -> JAXBElement[T]: ...

  @overload
  def unmarshal(self, arg0: XMLStreamReader, arg1: Class[T]) -> JAXBElement[T]: ...

  @overload
  def unmarshal(self, arg0: Source, arg1: Class[T]) -> JAXBElement[T]: ...

  @overload
  def unmarshal(self, arg0: Node, arg1: Class[T]) -> JAXBElement[T]: ...

  class Listener:

    def afterUnmarshal(self, arg0: object, arg1: object) -> None: ...

    def beforeUnmarshal(self, arg0: object, arg1: object) -> None: ...

    def __init__(self): ...


class UnmarshallerHandler:

  def characters(self, arg0: list[str], arg1: int, arg2: int) -> None: ...

  def declaration(self, arg0: str, arg1: str, arg2: str) -> None: ...

  def endDocument(self) -> None: ...

  def endElement(self, arg0: str, arg1: str, arg2: str) -> None: ...

  def endPrefixMapping(self, arg0: str) -> None: ...

  def getResult(self) -> object: ...

  def ignorableWhitespace(self, arg0: list[str], arg1: int, arg2: int) -> None: ...

  def processingInstruction(self, arg0: str, arg1: str) -> None: ...

  def setDocumentLocator(self, arg0: Locator) -> None: ...

  def skippedEntity(self, arg0: str) -> None: ...

  def startDocument(self) -> None: ...

  def startElement(self, arg0: str, arg1: str, arg2: str, arg3: Attributes) -> None: ...

  def startPrefixMapping(self, arg0: str, arg1: str) -> None: ...


class ValidationEvent:

  ERROR: int

  FATAL_ERROR: int

  WARNING: int

  def getLinkedException(self) -> Throwable: ...

  def getLocator(self) -> ValidationEventLocator: ...

  def getMessage(self) -> str: ...

  def getSeverity(self) -> int: ...


class ValidationEventHandler:

  def handleEvent(self, arg0: ValidationEvent) -> bool: ...


class ValidationEventLocator:

  def getColumnNumber(self) -> int: ...

  def getLineNumber(self) -> int: ...

  def getNode(self) -> Node: ...

  def getObject(self) -> object: ...

  def getOffset(self) -> int: ...

  def getURL(self) -> URL: ...

