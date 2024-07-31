from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import TimeZone, Locale

class AbstractCalendar(CalendarSystem):

  @overload
  def getCalendarDate(self) -> CalendarDate: ...

  @overload
  def getCalendarDate(self, arg0: int) -> CalendarDate: ...

  @overload
  def getCalendarDate(self, arg0: int, arg1: TimeZone) -> CalendarDate: ...

  @overload
  def getCalendarDate(self, arg0: int, arg1: CalendarDate) -> CalendarDate: ...

  def getEra(self, arg0: str) -> Era: ...

  def getEras(self) -> list[Era]: ...

  def getNthDayOfWeek(self, arg0: int, arg1: int, arg2: CalendarDate) -> CalendarDate: ...

  def getTime(self, arg0: CalendarDate) -> int: ...

  def getTimeOfDayValue(self, arg0: CalendarDate) -> int: ...

  def getWeekLength(self) -> int: ...

  def setEra(self, arg0: CalendarDate, arg1: str) -> None: ...

  def setTimeOfDay(self, arg0: CalendarDate, arg1: int) -> CalendarDate: ...

  def validateTime(self, arg0: CalendarDate) -> bool: ...

  @staticmethod
  def getDayOfWeekDateOnOrBefore(arg0: int, arg1: int) -> int: ...


class BaseCalendar(AbstractCalendar):

  APRIL: int

  AUGUST: int

  DECEMBER: int

  FEBRUARY: int

  FRIDAY: int

  JANUARY: int

  JULY: int

  JUNE: int

  MARCH: int

  MAY: int

  MONDAY: int

  NOVEMBER: int

  OCTOBER: int

  SATURDAY: int

  SEPTEMBER: int

  SUNDAY: int

  THURSDAY: int

  TUESDAY: int

  WEDNESDAY: int

  def getCalendarDateFromFixedDate(self, arg0: CalendarDate, arg1: int) -> None: ...

  def getDayOfWeek(self, arg0: CalendarDate) -> int: ...

  def getDayOfYear(self, arg0: CalendarDate) -> int: ...

  @overload
  def getFixedDate(self, arg0: CalendarDate) -> int: ...

  @overload
  def getFixedDate(self, arg0: int, arg1: int, arg2: int, arg3: BaseCalendar.Date) -> int: ...

  def getMonthLength(self, arg0: CalendarDate) -> int: ...

  def getYearFromFixedDate(self, arg0: int) -> int: ...

  def getYearLength(self, arg0: CalendarDate) -> int: ...

  def getYearLengthInMonths(self, arg0: CalendarDate) -> int: ...

  def normalize(self, arg0: CalendarDate) -> bool: ...

  def validate(self, arg0: CalendarDate) -> bool: ...

  @staticmethod
  def getDayOfWeekFromFixedDate(arg0: int) -> int: ...

  def __init__(self): ...

  class Date(CalendarDate):

    def getNormalizedYear(self) -> int: ...

    def setNormalizedDate(self, arg0: int, arg1: int, arg2: int) -> BaseCalendar.Date: ...

    def setNormalizedYear(self, arg0: int) -> None: ...


class CalendarDate:

  FIELD_UNDEFINED: int

  TIME_UNDEFINED: int

  def addDate(self, arg0: int, arg1: int, arg2: int) -> CalendarDate: ...

  def addDayOfMonth(self, arg0: int) -> CalendarDate: ...

  def addHours(self, arg0: int) -> CalendarDate: ...

  def addMillis(self, arg0: int) -> CalendarDate: ...

  def addMinutes(self, arg0: int) -> CalendarDate: ...

  def addMonth(self, arg0: int) -> CalendarDate: ...

  def addSeconds(self, arg0: int) -> CalendarDate: ...

  def addTimeOfDay(self, arg0: int, arg1: int, arg2: int, arg3: int) -> CalendarDate: ...

  def addYear(self, arg0: int) -> CalendarDate: ...

  def clone(self) -> object: ...

  def equals(self, arg0: object) -> bool: ...

  def getDayOfMonth(self) -> int: ...

  def getDayOfWeek(self) -> int: ...

  def getDaylightSaving(self) -> int: ...

  def getEra(self) -> Era: ...

  def getHours(self) -> int: ...

  def getMillis(self) -> int: ...

  def getMinutes(self) -> int: ...

  def getMonth(self) -> int: ...

  def getSeconds(self) -> int: ...

  def getTimeOfDay(self) -> int: ...

  def getYear(self) -> int: ...

  def getZone(self) -> TimeZone: ...

  def getZoneOffset(self) -> int: ...

  def hashCode(self) -> int: ...

  def isDaylightTime(self) -> bool: ...

  def isLeapYear(self) -> bool: ...

  def isNormalized(self) -> bool: ...

  def isSameDate(self, arg0: CalendarDate) -> bool: ...

  def isStandardTime(self) -> bool: ...

  def setDate(self, arg0: int, arg1: int, arg2: int) -> CalendarDate: ...

  def setDayOfMonth(self, arg0: int) -> CalendarDate: ...

  def setEra(self, arg0: Era) -> CalendarDate: ...

  def setHours(self, arg0: int) -> CalendarDate: ...

  def setMillis(self, arg0: int) -> CalendarDate: ...

  def setMinutes(self, arg0: int) -> CalendarDate: ...

  def setMonth(self, arg0: int) -> CalendarDate: ...

  def setSeconds(self, arg0: int) -> CalendarDate: ...

  def setStandardTime(self, arg0: bool) -> None: ...

  def setTimeOfDay(self, arg0: int, arg1: int, arg2: int, arg3: int) -> CalendarDate: ...

  def setYear(self, arg0: int) -> CalendarDate: ...

  def setZone(self, arg0: TimeZone) -> CalendarDate: ...

  def toString(self) -> str: ...


class CalendarSystem:

  @overload
  def getCalendarDate(self) -> CalendarDate: ...

  @overload
  def getCalendarDate(self, arg0: int) -> CalendarDate: ...

  @overload
  def getCalendarDate(self, arg0: int, arg1: TimeZone) -> CalendarDate: ...

  @overload
  def getCalendarDate(self, arg0: int, arg1: CalendarDate) -> CalendarDate: ...

  def getEra(self, arg0: str) -> Era: ...

  def getEras(self) -> list[Era]: ...

  def getMonthLength(self, arg0: CalendarDate) -> int: ...

  def getName(self) -> str: ...

  def getNthDayOfWeek(self, arg0: int, arg1: int, arg2: CalendarDate) -> CalendarDate: ...

  def getTime(self, arg0: CalendarDate) -> int: ...

  def getWeekLength(self) -> int: ...

  def getYearLength(self, arg0: CalendarDate) -> int: ...

  def getYearLengthInMonths(self, arg0: CalendarDate) -> int: ...

  @overload
  def newCalendarDate(self) -> CalendarDate: ...

  @overload
  def newCalendarDate(self, arg0: TimeZone) -> CalendarDate: ...

  def normalize(self, arg0: CalendarDate) -> bool: ...

  def setEra(self, arg0: CalendarDate, arg1: str) -> None: ...

  def setTimeOfDay(self, arg0: CalendarDate, arg1: int) -> CalendarDate: ...

  def validate(self, arg0: CalendarDate) -> bool: ...

  @staticmethod
  def forName(arg0: str) -> CalendarSystem: ...

  @staticmethod
  def getGregorianCalendar() -> Gregorian: ...

  def __init__(self): ...

  class GregorianHolder: ...


class Era:

  def equals(self, arg0: object) -> bool: ...

  def getAbbreviation(self) -> str: ...

  def getDiaplayAbbreviation(self, arg0: Locale) -> str: ...

  def getDisplayName(self, arg0: Locale) -> str: ...

  def getName(self) -> str: ...

  def getSince(self, arg0: TimeZone) -> int: ...

  def getSinceDate(self) -> CalendarDate: ...

  def hashCode(self) -> int: ...

  def isLocalTime(self) -> bool: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: str, arg1: str, arg2: int, arg3: bool): ...


class Gregorian(BaseCalendar):

  @overload
  def getCalendarDate(self) -> CalendarDate: ...

  @overload
  def getCalendarDate(self) -> Gregorian.Date: ...

  @overload
  def getCalendarDate(self, arg0: int) -> CalendarDate: ...

  @overload
  def getCalendarDate(self, arg0: int) -> Gregorian.Date: ...

  @overload
  def getCalendarDate(self, arg0: int, arg1: TimeZone) -> Gregorian.Date: ...

  @overload
  def getCalendarDate(self, arg0: int, arg1: TimeZone) -> CalendarDate: ...

  @overload
  def getCalendarDate(self, arg0: int, arg1: CalendarDate) -> Gregorian.Date: ...

  @overload
  def getCalendarDate(self, arg0: int, arg1: CalendarDate) -> CalendarDate: ...

  def getName(self) -> str: ...

  @overload
  def newCalendarDate(self) -> Gregorian.Date: ...

  @overload
  def newCalendarDate(self) -> CalendarDate: ...

  @overload
  def newCalendarDate(self, arg0: TimeZone) -> Gregorian.Date: ...

  @overload
  def newCalendarDate(self, arg0: TimeZone) -> CalendarDate: ...

  class Date(BaseCalendar.Date):

    def getNormalizedYear(self) -> int: ...

    def setNormalizedYear(self, arg0: int) -> None: ...


class JulianCalendar(BaseCalendar):

  @overload
  def getCalendarDate(self) -> CalendarDate: ...

  @overload
  def getCalendarDate(self) -> JulianCalendar.Date: ...

  @overload
  def getCalendarDate(self, arg0: int) -> CalendarDate: ...

  @overload
  def getCalendarDate(self, arg0: int) -> JulianCalendar.Date: ...

  @overload
  def getCalendarDate(self, arg0: int, arg1: TimeZone) -> CalendarDate: ...

  @overload
  def getCalendarDate(self, arg0: int, arg1: TimeZone) -> JulianCalendar.Date: ...

  @overload
  def getCalendarDate(self, arg0: int, arg1: CalendarDate) -> CalendarDate: ...

  @overload
  def getCalendarDate(self, arg0: int, arg1: CalendarDate) -> JulianCalendar.Date: ...

  def getCalendarDateFromFixedDate(self, arg0: CalendarDate, arg1: int) -> None: ...

  def getDayOfWeek(self, arg0: CalendarDate) -> int: ...

  def getFixedDate(self, arg0: int, arg1: int, arg2: int, arg3: BaseCalendar.Date) -> int: ...

  def getName(self) -> str: ...

  def getYearFromFixedDate(self, arg0: int) -> int: ...

  @overload
  def newCalendarDate(self) -> CalendarDate: ...

  @overload
  def newCalendarDate(self) -> JulianCalendar.Date: ...

  @overload
  def newCalendarDate(self, arg0: TimeZone) -> JulianCalendar.Date: ...

  @overload
  def newCalendarDate(self, arg0: TimeZone) -> CalendarDate: ...

  class Date(BaseCalendar.Date):

    def getNormalizedYear(self) -> int: ...

    @overload
    def setEra(self, arg0: Era) -> JulianCalendar.Date: ...

    @overload
    def setEra(self, arg0: Era) -> CalendarDate: ...

    def setNormalizedYear(self, arg0: int) -> None: ...

    def toString(self) -> str: ...
