from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import StringBuffer, StringBuilder, CharSequence, Enum, IllegalArgumentException
from java.util.function import Function, Predicate
from java.util.stream import Stream

class ASCII: ...


class CharPredicates:

  @staticmethod
  def forPOSIXName(arg0: str, arg1: bool) -> Pattern.CharPredicate: ...

  @staticmethod
  def forUnicodeProperty(arg0: str, arg1: bool) -> Pattern.CharPredicate: ...


class IntHashSet:

  def add(self, arg0: int) -> None: ...

  def clear(self) -> None: ...

  def contains(self, arg0: int) -> bool: ...

  def __init__(self): ...


class MatchResult:

  @overload
  def end(self) -> int: ...

  @overload
  def end(self, arg0: int) -> int: ...

  @overload
  def group(self) -> str: ...

  @overload
  def group(self, arg0: int) -> str: ...

  def groupCount(self) -> int: ...

  @overload
  def start(self) -> int: ...

  @overload
  def start(self, arg0: int) -> int: ...


class Matcher:

  @overload
  def appendReplacement(self, arg0: StringBuffer, arg1: str) -> Matcher: ...

  @overload
  def appendReplacement(self, arg0: StringBuilder, arg1: str) -> Matcher: ...

  @overload
  def appendTail(self, arg0: StringBuffer) -> StringBuffer: ...

  @overload
  def appendTail(self, arg0: StringBuilder) -> StringBuilder: ...

  @overload
  def end(self) -> int: ...

  @overload
  def end(self) -> int: ...

  @overload
  def end(self, arg0: int) -> int: ...

  @overload
  def end(self, arg0: int) -> int: ...

  @overload
  def end(self, arg0: str) -> int: ...

  @overload
  def find(self) -> bool: ...

  @overload
  def find(self, arg0: int) -> bool: ...

  @overload
  def group(self) -> str: ...

  @overload
  def group(self) -> str: ...

  @overload
  def group(self, arg0: int) -> str: ...

  @overload
  def group(self, arg0: int) -> str: ...

  @overload
  def group(self, arg0: str) -> str: ...

  @overload
  def groupCount(self) -> int: ...

  @overload
  def groupCount(self) -> int: ...

  def hasAnchoringBounds(self) -> bool: ...

  def hasTransparentBounds(self) -> bool: ...

  def hitEnd(self) -> bool: ...

  def lookingAt(self) -> bool: ...

  def matches(self) -> bool: ...

  def pattern(self) -> Pattern: ...

  def region(self, arg0: int, arg1: int) -> Matcher: ...

  def regionEnd(self) -> int: ...

  def regionStart(self) -> int: ...

  @overload
  def replaceAll(self, arg0: str) -> str: ...

  @overload
  def replaceAll(self, arg0: Function[MatchResult, str]) -> str: ...

  @overload
  def replaceFirst(self, arg0: str) -> str: ...

  @overload
  def replaceFirst(self, arg0: Function[MatchResult, str]) -> str: ...

  def requireEnd(self) -> bool: ...

  @overload
  def reset(self) -> Matcher: ...

  @overload
  def reset(self, arg0: CharSequence) -> Matcher: ...

  def results(self) -> Stream[MatchResult]: ...

  @overload
  def start(self) -> int: ...

  @overload
  def start(self) -> int: ...

  @overload
  def start(self, arg0: int) -> int: ...

  @overload
  def start(self, arg0: int) -> int: ...

  @overload
  def start(self, arg0: str) -> int: ...

  def toMatchResult(self) -> MatchResult: ...

  def toString(self) -> str: ...

  def useAnchoringBounds(self, arg0: bool) -> Matcher: ...

  def usePattern(self, arg0: Pattern) -> Matcher: ...

  def useTransparentBounds(self, arg0: bool) -> Matcher: ...

  @staticmethod
  def quoteReplacement(arg0: str) -> str: ...

  class ImmutableMatchResult:

    @overload
    def end(self) -> int: ...

    @overload
    def end(self) -> int: ...

    @overload
    def end(self, arg0: int) -> int: ...

    @overload
    def end(self, arg0: int) -> int: ...

    @overload
    def group(self) -> str: ...

    @overload
    def group(self) -> str: ...

    @overload
    def group(self, arg0: int) -> str: ...

    @overload
    def group(self, arg0: int) -> str: ...

    @overload
    def groupCount(self) -> int: ...

    @overload
    def groupCount(self) -> int: ...

    @overload
    def start(self) -> int: ...

    @overload
    def start(self) -> int: ...

    @overload
    def start(self, arg0: int) -> int: ...

    @overload
    def start(self, arg0: int) -> int: ...


class Pattern:

  CANON_EQ: int

  CASE_INSENSITIVE: int

  COMMENTS: int

  DOTALL: int

  LITERAL: int

  MULTILINE: int

  UNICODE_CASE: int

  UNICODE_CHARACTER_CLASS: int

  UNIX_LINES: int

  def asMatchPredicate(self) -> Predicate[str]: ...

  def asPredicate(self) -> Predicate[str]: ...

  def flags(self) -> int: ...

  def matcher(self, arg0: CharSequence) -> Matcher: ...

  def pattern(self) -> str: ...

  @overload
  def split(self, arg0: CharSequence) -> list[str]: ...

  @overload
  def split(self, arg0: CharSequence, arg1: int) -> list[str]: ...

  def splitAsStream(self, arg0: CharSequence) -> Stream[str]: ...

  def toString(self) -> str: ...

  @staticmethod
  @overload
  def compile(arg0: str) -> Pattern: ...

  @staticmethod
  @overload
  def compile(arg0: str, arg1: int) -> Pattern: ...

  @staticmethod
  def matches(arg0: str, arg1: CharSequence) -> bool: ...

  @staticmethod
  def quote(arg0: str) -> str: ...

  class Start(Pattern.Node): ...

  class Node: ...

  class GroupHead(Pattern.Node): ...

  class Slice(Pattern.SliceNode): ...

  class BnM(Pattern.Node): ...

  class StartS(Pattern.Start): ...

  class Begin(Pattern.Node): ...

  class First(Pattern.Node): ...

  class Loop(Pattern.Node): ...

  class BranchConn(Pattern.Node): ...

  class Branch(Pattern.Node): ...

  class NFCCharProperty(Pattern.Node): ...

  class CharPredicate:

    def negate(self) -> Pattern.CharPredicate: ...

    @overload
    def union(self, arg0: Pattern.CharPredicate) -> Pattern.CharPredicate: ...

    @overload
    def union(self, arg0: Pattern.CharPredicate, arg1: Pattern.CharPredicate) -> Pattern.CharPredicate: ...

  class CharProperty(Pattern.Node): ...

  class UnixCaret(Pattern.Node): ...

  class Caret(Pattern.Node): ...

  class UnixDollar(Pattern.Node): ...

  class Dollar(Pattern.Node): ...

  class CIBackRef(Pattern.Node): ...

  class BackRef(Pattern.Node): ...

  class Bound(Pattern.Node): ...

  class BmpCharPredicate:

    def negate(self) -> Pattern.CharPredicate: ...

    @overload
    def union(self, arg0: Pattern.CharPredicate) -> Pattern.CharPredicate: ...

    @overload
    def union(self, arg0: Pattern.CharPredicate) -> Pattern.CharPredicate: ...

    @overload
    def union(self, arg0: Pattern.CharPredicate, arg1: Pattern.CharPredicate) -> Pattern.CharPredicate: ...

    @overload
    def union(self, arg0: Pattern.CharPredicate, arg1: Pattern.CharPredicate) -> Pattern.CharPredicate: ...

  class LastMatch(Pattern.Node): ...

  class LineEnding(Pattern.Node): ...

  class XGrapheme(Pattern.Node): ...

  class GraphemeBound(Pattern.Node): ...

  class End(Pattern.Node): ...

  class BitClass:

    @overload
    def union(self, arg0: Pattern.CharPredicate) -> Pattern.CharPredicate: ...

    @overload
    def union(self, arg0: Pattern.CharPredicate, arg1: Pattern.CharPredicate) -> Pattern.CharPredicate: ...

  class BmpCharProperty(Pattern.CharProperty): ...

  class Pos(Pattern.Node): ...

  class Neg(Pattern.Node): ...

  class Ques(Pattern.Node): ...

  class Qtype(Enum):

    GREEDY: Pattern.Qtype

    INDEPENDENT: Pattern.Qtype

    LAZY: Pattern.Qtype

    POSSESSIVE: Pattern.Qtype

    @staticmethod
    def valueOf(arg0: str) -> Pattern.Qtype: ...

    @staticmethod
    def values() -> list[Pattern.Qtype]: ...

  class LookBehindEndNode(Pattern.Node): ...

  class TreeInfo: ...

  class BehindS(Pattern.Behind): ...

  class Behind(Pattern.Node): ...

  class NotBehindS(Pattern.NotBehind): ...

  class NotBehind(Pattern.Node): ...

  class Curly(Pattern.Node): ...

  class GroupTail(Pattern.Node): ...

  class GroupCurly(Pattern.Node): ...

  class LazyLoop(Pattern.Loop): ...

  class Prolog(Pattern.Node): ...

  class BmpCharPropertyGreedy(Pattern.CharPropertyGreedy): ...

  class CharPropertyGreedy(Pattern.Node): ...

  class SliceUS(Pattern.SliceIS): ...

  class SliceU(Pattern.SliceNode): ...

  class SliceIS(Pattern.SliceNode): ...

  class SliceI(Pattern.SliceNode): ...

  class SliceS(Pattern.Slice): ...

  class LastNode(Pattern.Node): ...

  class BnMS(Pattern.BnM): ...

  class SliceNode(Pattern.Node): ...


class PatternSyntaxException(IllegalArgumentException):

  def getDescription(self) -> str: ...

  def getIndex(self) -> int: ...

  def getMessage(self) -> str: ...

  def getPattern(self) -> str: ...

  def __init__(self, arg0: str, arg1: str, arg2: int): ...

