from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import GregorianCalendar
from zombie.iso.sprite import IsoSpriteManager, IsoSprite

class ErosionIceQueen:

  instance: ErosionIceQueen

  def addSprite(self, _sprite: str, _winterSprite: str) -> None: ...

  def setSnow(self, _isSnow: bool) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  def __init__(self, _sprMngr: IsoSpriteManager): ...

  class Sprite:

    def __init__(self, arg0: IsoSprite, arg1: str, arg2: str):
      self.normal: str
      self.sprite: IsoSprite
      self.winter: str


class ErosionSeason:

  NUM_SEASONS: int

  SEASON_AUTUMN: int

  SEASON_DEFAULT: int

  SEASON_SPRING: int

  SEASON_SUMMER: int

  SEASON_SUMMER2: int

  SEASON_WINTER: int

  @overload
  def clone(self) -> object: ...

  @overload
  def clone(self) -> ErosionSeason: ...

  def getCurDayPercent(self) -> float: ...

  def getDawn(self) -> float: ...

  def getDayHighNoon(self) -> float: ...

  def getDayMeanTemperature(self) -> float: ...

  def getDayNoiseVal(self) -> float: ...

  def getDayTemperature(self) -> float: ...

  def getDaylight(self) -> float: ...

  def getDusk(self) -> float: ...

  def getHighNoon(self) -> float: ...

  def getLat(self) -> int: ...

  def getMaxDaylightSummer(self) -> float: ...

  def getMaxDaylightWinter(self) -> float: ...

  def getRainDayStrength(self) -> float: ...

  def getRainYearAverage(self) -> float: ...

  def getSeason(self) -> int: ...

  def getSeasonDay(self) -> float: ...

  def getSeasonDays(self) -> float: ...

  def getSeasonLag(self) -> int: ...

  def getSeasonName(self) -> str: ...

  def getSeasonProgression(self) -> float: ...

  def getSeasonStrength(self) -> float: ...

  def getSeedA(self) -> int: ...

  def getSeedB(self) -> int: ...

  def getSeedC(self) -> int: ...

  def getTempDiff(self) -> int: ...

  def getTempMax(self) -> int: ...

  def getTempMin(self) -> int: ...

  def getWinterStartDay(self, day: int, month: int, year: int) -> GregorianCalendar: ...

  def init(self, _lat: int, _tempMax: int, _tempMin: int, _tempDiff: int, _seasonLag: int, _noon: float, _seedA: int, _seedB: int, _seedC: int) -> None: ...

  def isRainDay(self) -> bool: ...

  def isSeason(self, _season: int) -> bool: ...

  def isSunnyDay(self) -> bool: ...

  def isThunderDay(self) -> bool: ...

  def setCurSeason(self, season: int) -> None: ...

  def setDay(self, _day: int, _month: int, _year: int) -> None: ...

  def setRain(self, _jan: float, _feb: float, _mar: float, _apr: float, _may: float, _jun: float, _jul: float, _aug: float, _sep: float, _oct: float, _nov: float, _dec: float) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  def __init__(self): ...

  class YearData: ...

