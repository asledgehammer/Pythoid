from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import CharSequence, Class
from java.nio import ByteBuffer, DoubleBuffer, FloatBuffer, IntBuffer, LongBuffer, ShortBuffer, Buffer
from java.util import Iterator, Spliterator, Comparator
from java.util.function import Consumer
from java.util.stream import Stream
from org.lwjgl import CLongBuffer, PointerBuffer

T = TypeVar('T', default=Any)
SELF = TypeVar('SELF', default=Any)
StructSpliterator_T = TypeVar('StructSpliterator_T', default=Any)
StructSpliterator_SELF = TypeVar('StructSpliterator_SELF', default=Any)
StructIterator_T = TypeVar('StructIterator_T', default=Any)
StructIterator_SELF = TypeVar('StructIterator_SELF', default=Any)

class Callback:

  BITS32: bool

  BITS64: bool

  CLONG_SHIFT: int

  CLONG_SIZE: int

  POINTER_SHIFT: int

  POINTER_SIZE: int

  @overload
  def address(self) -> int: ...

  @overload
  def address(self) -> int: ...

  def close(self) -> None: ...

  def equals(self, arg0: object) -> bool: ...

  @overload
  def free(self) -> None: ...

  @overload
  def free(self) -> None: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def __stdcall(arg0: str) -> str: ...

  @staticmethod
  def get(arg0: int) -> T: ...

  @staticmethod
  def getSafe(arg0: int) -> T: ...


class CallbackI:

  BITS32: bool

  BITS64: bool

  CLONG_SHIFT: int

  CLONG_SIZE: int

  POINTER_SHIFT: int

  POINTER_SIZE: int

  @overload
  def address(self) -> int: ...

  @overload
  def address(self) -> int: ...

  def getSignature(self) -> str: ...

  class P:

    def address(self) -> int: ...

    def callback(self, arg0: int) -> int: ...

    def getSignature(self) -> str: ...

  class D:

    def address(self) -> int: ...

    def callback(self, arg0: int) -> float: ...

    def getSignature(self) -> str: ...

  class F:

    def address(self) -> int: ...

    def callback(self, arg0: int) -> float: ...

    def getSignature(self) -> str: ...

  class N:

    def address(self) -> int: ...

    def callback(self, arg0: int) -> int: ...

    def getSignature(self) -> str: ...

  class J:

    def address(self) -> int: ...

    def callback(self, arg0: int) -> int: ...

    def getSignature(self) -> str: ...

  class I:

    def address(self) -> int: ...

    def callback(self, arg0: int) -> int: ...

    def getSignature(self) -> str: ...

  class S:

    def address(self) -> int: ...

    def callback(self, arg0: int) -> int: ...

    def getSignature(self) -> str: ...

  class B:

    def address(self) -> int: ...

    def callback(self, arg0: int) -> int: ...

    def getSignature(self) -> str: ...

  class Z:

    def address(self) -> int: ...

    def callback(self, arg0: int) -> bool: ...

    def getSignature(self) -> str: ...

  class V:

    def address(self) -> int: ...

    def callback(self, arg0: int) -> None: ...

    def getSignature(self) -> str: ...


class CustomBuffer[SELF](Pointer.Default):

  @overload
  def address(self) -> int: ...

  @overload
  def address(self, arg0: int) -> int: ...

  def address0(self) -> int: ...

  def capacity(self) -> int: ...

  def clear(self) -> SELF: ...

  def compact(self) -> SELF: ...

  def duplicate(self) -> SELF: ...

  def flip(self) -> SELF: ...

  def free(self) -> None: ...

  def hasRemaining(self) -> bool: ...

  @overload
  def limit(self) -> int: ...

  @overload
  def limit(self, arg0: int) -> SELF: ...

  def mark(self) -> SELF: ...

  @overload
  def position(self) -> int: ...

  @overload
  def position(self, arg0: int) -> SELF: ...

  def put(self, arg0: SELF) -> SELF: ...

  def remaining(self) -> int: ...

  def reset(self) -> SELF: ...

  def rewind(self) -> SELF: ...

  def sizeof(self) -> int: ...

  @overload
  def slice(self) -> SELF: ...

  @overload
  def slice(self, arg0: int, arg1: int) -> SELF: ...

  def toString(self) -> str: ...


class FunctionProvider:

  @overload
  def getFunctionAddress(self, arg0: CharSequence) -> int: ...

  @overload
  def getFunctionAddress(self, arg0: ByteBuffer) -> int: ...


class MemoryStack(Pointer.Default):

  @overload
  def ASCII(self, arg0: CharSequence) -> ByteBuffer: ...

  @overload
  def ASCII(self, arg0: CharSequence, arg1: bool) -> ByteBuffer: ...

  @overload
  def ASCIISafe(self, arg0: CharSequence) -> ByteBuffer: ...

  @overload
  def ASCIISafe(self, arg0: CharSequence, arg1: bool) -> ByteBuffer: ...

  @overload
  def UTF16(self, arg0: CharSequence) -> ByteBuffer: ...

  @overload
  def UTF16(self, arg0: CharSequence, arg1: bool) -> ByteBuffer: ...

  @overload
  def UTF16Safe(self, arg0: CharSequence) -> ByteBuffer: ...

  @overload
  def UTF16Safe(self, arg0: CharSequence, arg1: bool) -> ByteBuffer: ...

  @overload
  def UTF8(self, arg0: CharSequence) -> ByteBuffer: ...

  @overload
  def UTF8(self, arg0: CharSequence, arg1: bool) -> ByteBuffer: ...

  @overload
  def UTF8Safe(self, arg0: CharSequence) -> ByteBuffer: ...

  @overload
  def UTF8Safe(self, arg0: CharSequence, arg1: bool) -> ByteBuffer: ...

  @overload
  def bytes(self, arg0: list[int]) -> ByteBuffer: ...

  @overload
  def bytes(self, arg0: int) -> ByteBuffer: ...

  @overload
  def bytes(self, arg0: int, arg1: int) -> ByteBuffer: ...

  @overload
  def bytes(self, arg0: int, arg1: int, arg2: int) -> ByteBuffer: ...

  @overload
  def bytes(self, arg0: int, arg1: int, arg2: int, arg3: int) -> ByteBuffer: ...

  @overload
  def calloc(self, arg0: int) -> ByteBuffer: ...

  @overload
  def calloc(self, arg0: int, arg1: int) -> ByteBuffer: ...

  def callocCLong(self, arg0: int) -> CLongBuffer: ...

  def callocDouble(self, arg0: int) -> DoubleBuffer: ...

  def callocFloat(self, arg0: int) -> FloatBuffer: ...

  def callocInt(self, arg0: int) -> IntBuffer: ...

  def callocLong(self, arg0: int) -> LongBuffer: ...

  def callocPointer(self, arg0: int) -> PointerBuffer: ...

  def callocShort(self, arg0: int) -> ShortBuffer: ...

  @overload
  def clongs(self, arg0: list[int]) -> CLongBuffer: ...

  @overload
  def clongs(self, arg0: int) -> CLongBuffer: ...

  @overload
  def clongs(self, arg0: int, arg1: int) -> CLongBuffer: ...

  @overload
  def clongs(self, arg0: int, arg1: int, arg2: int) -> CLongBuffer: ...

  @overload
  def clongs(self, arg0: int, arg1: int, arg2: int, arg3: int) -> CLongBuffer: ...

  @overload
  def close(self) -> None: ...

  @overload
  def close(self) -> None: ...

  @overload
  def doubles(self, arg0: list[float]) -> DoubleBuffer: ...

  @overload
  def doubles(self, arg0: float) -> DoubleBuffer: ...

  @overload
  def doubles(self, arg0: float, arg1: float) -> DoubleBuffer: ...

  @overload
  def doubles(self, arg0: float, arg1: float, arg2: float) -> DoubleBuffer: ...

  @overload
  def doubles(self, arg0: float, arg1: float, arg2: float, arg3: float) -> DoubleBuffer: ...

  @overload
  def floats(self, arg0: list[float]) -> FloatBuffer: ...

  @overload
  def floats(self, arg0: float) -> FloatBuffer: ...

  @overload
  def floats(self, arg0: float, arg1: float) -> FloatBuffer: ...

  @overload
  def floats(self, arg0: float, arg1: float, arg2: float) -> FloatBuffer: ...

  @overload
  def floats(self, arg0: float, arg1: float, arg2: float, arg3: float) -> FloatBuffer: ...

  def getAddress(self) -> int: ...

  def getFrameIndex(self) -> int: ...

  def getPointer(self) -> int: ...

  def getPointerAddress(self) -> int: ...

  def getSize(self) -> int: ...

  @overload
  def ints(self, arg0: list[int]) -> IntBuffer: ...

  @overload
  def ints(self, arg0: int) -> IntBuffer: ...

  @overload
  def ints(self, arg0: int, arg1: int) -> IntBuffer: ...

  @overload
  def ints(self, arg0: int, arg1: int, arg2: int) -> IntBuffer: ...

  @overload
  def ints(self, arg0: int, arg1: int, arg2: int, arg3: int) -> IntBuffer: ...

  @overload
  def longs(self, arg0: list[int]) -> LongBuffer: ...

  @overload
  def longs(self, arg0: int) -> LongBuffer: ...

  @overload
  def longs(self, arg0: int, arg1: int) -> LongBuffer: ...

  @overload
  def longs(self, arg0: int, arg1: int, arg2: int) -> LongBuffer: ...

  @overload
  def longs(self, arg0: int, arg1: int, arg2: int, arg3: int) -> LongBuffer: ...

  @overload
  def malloc(self, arg0: int) -> ByteBuffer: ...

  @overload
  def malloc(self, arg0: int, arg1: int) -> ByteBuffer: ...

  def mallocCLong(self, arg0: int) -> CLongBuffer: ...

  def mallocDouble(self, arg0: int) -> DoubleBuffer: ...

  def mallocFloat(self, arg0: int) -> FloatBuffer: ...

  def mallocInt(self, arg0: int) -> IntBuffer: ...

  def mallocLong(self, arg0: int) -> LongBuffer: ...

  def mallocPointer(self, arg0: int) -> PointerBuffer: ...

  def mallocShort(self, arg0: int) -> ShortBuffer: ...

  def nASCII(self, arg0: CharSequence, arg1: bool) -> int: ...

  def nASCIISafe(self, arg0: CharSequence, arg1: bool) -> int: ...

  def nUTF16(self, arg0: CharSequence, arg1: bool) -> int: ...

  def nUTF16Safe(self, arg0: CharSequence, arg1: bool) -> int: ...

  def nUTF8(self, arg0: CharSequence, arg1: bool) -> int: ...

  def nUTF8Safe(self, arg0: CharSequence, arg1: bool) -> int: ...

  def ncalloc(self, arg0: int, arg1: int, arg2: int) -> int: ...

  @overload
  def nmalloc(self, arg0: int) -> int: ...

  @overload
  def nmalloc(self, arg0: int, arg1: int) -> int: ...

  @overload
  def pointers(self, arg0: list[int]) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: list[Buffer]) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: list[Pointer]) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: Buffer) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: int) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: Pointer) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: Buffer, arg1: Buffer) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: int, arg1: int) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: Pointer, arg1: Pointer) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: Buffer, arg1: Buffer, arg2: Buffer) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: int, arg1: int, arg2: int) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: Pointer, arg1: Pointer, arg2: Pointer) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: Buffer, arg1: Buffer, arg2: Buffer, arg3: Buffer) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: int, arg1: int, arg2: int, arg3: int) -> PointerBuffer: ...

  @overload
  def pointers(self, arg0: Pointer, arg1: Pointer, arg2: Pointer, arg3: Pointer) -> PointerBuffer: ...

  def pop(self) -> MemoryStack: ...

  def push(self) -> MemoryStack: ...

  def setPointer(self, arg0: int) -> None: ...

  @overload
  def shorts(self, arg0: list[int]) -> ShortBuffer: ...

  @overload
  def shorts(self, arg0: int) -> ShortBuffer: ...

  @overload
  def shorts(self, arg0: int, arg1: int) -> ShortBuffer: ...

  @overload
  def shorts(self, arg0: int, arg1: int, arg2: int) -> ShortBuffer: ...

  @overload
  def shorts(self, arg0: int, arg1: int, arg2: int, arg3: int) -> ShortBuffer: ...

  @staticmethod
  @overload
  def create() -> MemoryStack: ...

  @staticmethod
  @overload
  def create(arg0: int) -> MemoryStack: ...

  @staticmethod
  @overload
  def create(arg0: ByteBuffer) -> MemoryStack: ...

  @staticmethod
  def ncreate(arg0: int, arg1: int) -> MemoryStack: ...

  @staticmethod
  def nstackCalloc(arg0: int, arg1: int, arg2: int) -> int: ...

  @staticmethod
  @overload
  def nstackMalloc(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nstackMalloc(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def stackASCII(arg0: CharSequence) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackASCII(arg0: CharSequence, arg1: bool) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackASCIISafe(arg0: CharSequence) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackASCIISafe(arg0: CharSequence, arg1: bool) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackBytes(arg0: list[int]) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackBytes(arg0: int) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackBytes(arg0: int, arg1: int) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackBytes(arg0: int, arg1: int, arg2: int) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackBytes(arg0: int, arg1: int, arg2: int, arg3: int) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackCLongs(arg0: list[int]) -> CLongBuffer: ...

  @staticmethod
  @overload
  def stackCLongs(arg0: int) -> CLongBuffer: ...

  @staticmethod
  @overload
  def stackCLongs(arg0: int, arg1: int) -> CLongBuffer: ...

  @staticmethod
  @overload
  def stackCLongs(arg0: int, arg1: int, arg2: int) -> CLongBuffer: ...

  @staticmethod
  @overload
  def stackCLongs(arg0: int, arg1: int, arg2: int, arg3: int) -> CLongBuffer: ...

  @staticmethod
  def stackCalloc(arg0: int) -> ByteBuffer: ...

  @staticmethod
  def stackCallocCLong(arg0: int) -> CLongBuffer: ...

  @staticmethod
  def stackCallocDouble(arg0: int) -> DoubleBuffer: ...

  @staticmethod
  def stackCallocFloat(arg0: int) -> FloatBuffer: ...

  @staticmethod
  def stackCallocInt(arg0: int) -> IntBuffer: ...

  @staticmethod
  def stackCallocLong(arg0: int) -> LongBuffer: ...

  @staticmethod
  def stackCallocPointer(arg0: int) -> PointerBuffer: ...

  @staticmethod
  def stackCallocShort(arg0: int) -> ShortBuffer: ...

  @staticmethod
  @overload
  def stackDoubles(arg0: list[float]) -> DoubleBuffer: ...

  @staticmethod
  @overload
  def stackDoubles(arg0: float) -> DoubleBuffer: ...

  @staticmethod
  @overload
  def stackDoubles(arg0: float, arg1: float) -> DoubleBuffer: ...

  @staticmethod
  @overload
  def stackDoubles(arg0: float, arg1: float, arg2: float) -> DoubleBuffer: ...

  @staticmethod
  @overload
  def stackDoubles(arg0: float, arg1: float, arg2: float, arg3: float) -> DoubleBuffer: ...

  @staticmethod
  @overload
  def stackFloats(arg0: list[float]) -> FloatBuffer: ...

  @staticmethod
  @overload
  def stackFloats(arg0: float) -> FloatBuffer: ...

  @staticmethod
  @overload
  def stackFloats(arg0: float, arg1: float) -> FloatBuffer: ...

  @staticmethod
  @overload
  def stackFloats(arg0: float, arg1: float, arg2: float) -> FloatBuffer: ...

  @staticmethod
  @overload
  def stackFloats(arg0: float, arg1: float, arg2: float, arg3: float) -> FloatBuffer: ...

  @staticmethod
  def stackGet() -> MemoryStack: ...

  @staticmethod
  @overload
  def stackInts(arg0: list[int]) -> IntBuffer: ...

  @staticmethod
  @overload
  def stackInts(arg0: int) -> IntBuffer: ...

  @staticmethod
  @overload
  def stackInts(arg0: int, arg1: int) -> IntBuffer: ...

  @staticmethod
  @overload
  def stackInts(arg0: int, arg1: int, arg2: int) -> IntBuffer: ...

  @staticmethod
  @overload
  def stackInts(arg0: int, arg1: int, arg2: int, arg3: int) -> IntBuffer: ...

  @staticmethod
  @overload
  def stackLongs(arg0: list[int]) -> LongBuffer: ...

  @staticmethod
  @overload
  def stackLongs(arg0: int) -> LongBuffer: ...

  @staticmethod
  @overload
  def stackLongs(arg0: int, arg1: int) -> LongBuffer: ...

  @staticmethod
  @overload
  def stackLongs(arg0: int, arg1: int, arg2: int) -> LongBuffer: ...

  @staticmethod
  @overload
  def stackLongs(arg0: int, arg1: int, arg2: int, arg3: int) -> LongBuffer: ...

  @staticmethod
  def stackMalloc(arg0: int) -> ByteBuffer: ...

  @staticmethod
  def stackMallocCLong(arg0: int) -> CLongBuffer: ...

  @staticmethod
  def stackMallocDouble(arg0: int) -> DoubleBuffer: ...

  @staticmethod
  def stackMallocFloat(arg0: int) -> FloatBuffer: ...

  @staticmethod
  def stackMallocInt(arg0: int) -> IntBuffer: ...

  @staticmethod
  def stackMallocLong(arg0: int) -> LongBuffer: ...

  @staticmethod
  def stackMallocPointer(arg0: int) -> PointerBuffer: ...

  @staticmethod
  def stackMallocShort(arg0: int) -> ShortBuffer: ...

  @staticmethod
  @overload
  def stackPointers(arg0: list[int]) -> PointerBuffer: ...

  @staticmethod
  @overload
  def stackPointers(arg0: list[Pointer]) -> PointerBuffer: ...

  @staticmethod
  @overload
  def stackPointers(arg0: int) -> PointerBuffer: ...

  @staticmethod
  @overload
  def stackPointers(arg0: Pointer) -> PointerBuffer: ...

  @staticmethod
  @overload
  def stackPointers(arg0: int, arg1: int) -> PointerBuffer: ...

  @staticmethod
  @overload
  def stackPointers(arg0: Pointer, arg1: Pointer) -> PointerBuffer: ...

  @staticmethod
  @overload
  def stackPointers(arg0: int, arg1: int, arg2: int) -> PointerBuffer: ...

  @staticmethod
  @overload
  def stackPointers(arg0: Pointer, arg1: Pointer, arg2: Pointer) -> PointerBuffer: ...

  @staticmethod
  @overload
  def stackPointers(arg0: int, arg1: int, arg2: int, arg3: int) -> PointerBuffer: ...

  @staticmethod
  @overload
  def stackPointers(arg0: Pointer, arg1: Pointer, arg2: Pointer, arg3: Pointer) -> PointerBuffer: ...

  @staticmethod
  def stackPop() -> MemoryStack: ...

  @staticmethod
  def stackPush() -> MemoryStack: ...

  @staticmethod
  @overload
  def stackShorts(arg0: list[int]) -> ShortBuffer: ...

  @staticmethod
  @overload
  def stackShorts(arg0: int) -> ShortBuffer: ...

  @staticmethod
  @overload
  def stackShorts(arg0: int, arg1: int) -> ShortBuffer: ...

  @staticmethod
  @overload
  def stackShorts(arg0: int, arg1: int, arg2: int) -> ShortBuffer: ...

  @staticmethod
  @overload
  def stackShorts(arg0: int, arg1: int, arg2: int, arg3: int) -> ShortBuffer: ...

  @staticmethod
  @overload
  def stackUTF16(arg0: CharSequence) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackUTF16(arg0: CharSequence, arg1: bool) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackUTF16Safe(arg0: CharSequence) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackUTF16Safe(arg0: CharSequence, arg1: bool) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackUTF8(arg0: CharSequence) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackUTF8(arg0: CharSequence, arg1: bool) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackUTF8Safe(arg0: CharSequence) -> ByteBuffer: ...

  @staticmethod
  @overload
  def stackUTF8Safe(arg0: CharSequence, arg1: bool) -> ByteBuffer: ...

  class DebugMemoryStack(MemoryStack):

    def pop(self) -> MemoryStack: ...

    def push(self) -> MemoryStack: ...


class NativeResource:

  @overload
  def close(self) -> None: ...

  @overload
  def close(self) -> None: ...

  def free(self) -> None: ...


class NativeType:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...

  def value(self) -> str: ...


class Pointer:

  BITS32: bool

  BITS64: bool

  CLONG_SHIFT: int

  CLONG_SIZE: int

  POINTER_SHIFT: int

  POINTER_SIZE: int

  def address(self) -> int: ...

  class Default:

    BITS32: bool

    BITS64: bool

    CLONG_SHIFT: int

    CLONG_SIZE: int

    POINTER_SHIFT: int

    POINTER_SIZE: int

    @overload
    def address(self) -> int: ...

    @overload
    def address(self) -> int: ...

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def toString(self) -> str: ...


class SharedLibrary:

  BITS32: bool

  BITS64: bool

  CLONG_SHIFT: int

  CLONG_SIZE: int

  POINTER_SHIFT: int

  POINTER_SIZE: int

  def address(self) -> int: ...

  def close(self) -> None: ...

  def free(self) -> None: ...

  @overload
  def getFunctionAddress(self, arg0: CharSequence) -> int: ...

  @overload
  def getFunctionAddress(self, arg0: ByteBuffer) -> int: ...

  def getName(self) -> str: ...

  def getPath(self) -> str: ...

  class Delegate:

    def address(self) -> int: ...

    def free(self) -> None: ...

    @overload
    def getName(self) -> str: ...

    @overload
    def getName(self) -> str: ...

    @overload
    def getPath(self) -> str: ...

    @overload
    def getPath(self) -> str: ...

  class Default(Pointer.Default):

    @overload
    def getName(self) -> str: ...

    @overload
    def getName(self) -> str: ...

    @overload
    def getPath(self) -> str: ...

    @overload
    def getPath(self) -> str: ...


class Struct(Pointer.Default):

  def clear(self) -> None: ...

  def free(self) -> None: ...

  def isNull(self, arg0: int) -> bool: ...

  def sizeof(self) -> int: ...

  class Layout(Struct.Member):

    def offsetof(self, arg0: int) -> int: ...

  class Member:

    @overload
    def getAlignment(self) -> int: ...

    @overload
    def getAlignment(self, arg0: int) -> int: ...

    def getSize(self) -> int: ...


class StructBuffer[T, SELF](CustomBuffer):

  @overload
  def apply(self, arg0: Consumer[T]) -> SELF: ...

  @overload
  def apply(self, arg0: int, arg1: Consumer[T]) -> SELF: ...

  @overload
  def forEach(self, arg0: Consumer[T]) -> None: ...

  @overload
  def forEach(self, arg0: Consumer[T]) -> None: ...

  @overload
  def get(self) -> T: ...

  @overload
  def get(self, arg0: int) -> T: ...

  @overload
  def get(self, arg0: T) -> SELF: ...

  @overload
  def get(self, arg0: int, arg1: T) -> SELF: ...

  @overload
  def iterator(self) -> Iterator[T]: ...

  @overload
  def iterator(self) -> Iterator[T]: ...

  def parallelStream(self) -> Stream[T]: ...

  @overload
  def put(self, arg0: T) -> SELF: ...

  @overload
  def put(self, arg0: int, arg1: T) -> SELF: ...

  def sizeof(self) -> int: ...

  @overload
  def spliterator(self) -> Spliterator[T]: ...

  @overload
  def spliterator(self) -> Spliterator[T]: ...

  def stream(self) -> Stream[T]: ...

  class StructSpliterator[StructSpliterator_T, StructSpliterator_SELF]:

    CONCURRENT: int

    DISTINCT: int

    IMMUTABLE: int

    NONNULL: int

    ORDERED: int

    SIZED: int

    SORTED: int

    SUBSIZED: int

    @overload
    def characteristics(self) -> int: ...

    @overload
    def characteristics(self) -> int: ...

    @overload
    def estimateSize(self) -> int: ...

    @overload
    def estimateSize(self) -> int: ...

    @overload
    def forEachRemaining(self, arg0: Consumer[T]) -> None: ...

    @overload
    def forEachRemaining(self, arg0: Consumer[T]) -> None: ...

    @overload
    def getComparator(self) -> Comparator[T]: ...

    @overload
    def getComparator(self) -> Comparator[T]: ...

    def getExactSizeIfKnown(self) -> int: ...

    def hasCharacteristics(self, arg0: int) -> bool: ...

    @overload
    def tryAdvance(self, arg0: Consumer[T]) -> bool: ...

    @overload
    def tryAdvance(self, arg0: Consumer[T]) -> bool: ...

    @overload
    def trySplit(self) -> Spliterator[T]: ...

    @overload
    def trySplit(self) -> Spliterator[T]: ...

  class StructIterator[StructIterator_T, StructIterator_SELF]:

    @overload
    def forEachRemaining(self, arg0: Consumer[T]) -> None: ...

    @overload
    def forEachRemaining(self, arg0: Consumer[E]) -> None: ...

    @overload
    def hasNext(self) -> bool: ...

    @overload
    def hasNext(self) -> bool: ...

    @overload
    def next(self) -> object: ...

    @overload
    def next(self) -> T: ...

    @overload
    def next(self) -> object: ...

    def remove(self) -> None: ...

