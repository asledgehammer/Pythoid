from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Integer
from java.util import HashMap, ArrayList, Collection, LinkedHashMap, List
from zombie.characters.skills import PerkFactory
from zombie.core.textures import Texture

class ObservationFactory:

  ObservationMap: HashMap[str, ObservationFactory.Observation]

  @staticmethod
  def addObservation(type: str, name: str, desc: str) -> None: ...

  @staticmethod
  def getObservation(name: str) -> ObservationFactory.Observation: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def setMutualExclusive(a: str, b: str) -> None: ...

  def __init__(self): ...

  class Observation:

    def getDescription(self) -> str: ...

    @overload
    def getLabel(self) -> str: ...

    @overload
    def getLabel(self) -> str: ...

    @overload
    def getLeftLabel(self) -> str: ...

    @overload
    def getLeftLabel(self) -> str: ...

    def getName(self) -> str: ...

    @overload
    def getRightLabel(self) -> str: ...

    @overload
    def getRightLabel(self) -> str: ...

    def getTraitID(self) -> str: ...

    def setDescription(self, description: str) -> None: ...

    def setName(self, name: str) -> None: ...

    def setTraitID(self, traitID: str) -> None: ...

    def __init__(self, tr: str, name: str, desc: str):
      self.mutuallyexclusive: ArrayList[str]


class TraitCollection:

  def add(self, trait: str) -> None: ...

  def addAll(self, c: Collection[str]) -> None: ...

  def clear(self) -> None: ...

  @overload
  def contains(self, o: object) -> bool: ...

  @overload
  def contains(self, trait: str) -> bool: ...

  def get(self, n: int) -> str: ...

  def getTraitSlot(self, name: str) -> TraitCollection.TraitSlot: ...

  def isEmpty(self) -> bool: ...

  @overload
  def remove(self, o: object) -> bool: ...

  @overload
  def remove(self, name: str) -> bool: ...

  def removeAll(self, c: Collection[Any]) -> None: ...

  def set(self, name: str, val: bool) -> None: ...

  def size(self) -> int: ...

  def toString(self) -> str: ...

  def __init__(self): ...

  class TraitSlot:

    def isName(self, arg0: str) -> bool: ...

    def isSet(self) -> bool: ...

    def set(self, arg0: bool) -> None: ...

    def toString(self) -> str: ...


class TraitFactory:

  TraitMap: LinkedHashMap[str, TraitFactory.Trait]

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  @overload
  def addTrait(type: str, name: str, cost: int, desc: str, profession: bool) -> TraitFactory.Trait: ...

  @staticmethod
  @overload
  def addTrait(type: str, name: str, cost: int, desc: str, profession: bool, removeInMP: bool) -> TraitFactory.Trait: ...

  @staticmethod
  def getTrait(name: str) -> TraitFactory.Trait: ...

  @staticmethod
  def getTraits() -> ArrayList[TraitFactory.Trait]: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def setMutualExclusive(a: str, b: str) -> None: ...

  @staticmethod
  def sortList() -> None: ...

  def __init__(self): ...

  class Trait:

    def addXPBoost(self, perk: PerkFactory.Perk, level: int) -> None: ...

    def getCost(self) -> int: ...

    def getDescription(self) -> str: ...

    def getFreeRecipes(self) -> List[str]: ...

    @overload
    def getLabel(self) -> str: ...

    @overload
    def getLabel(self) -> str: ...

    @overload
    def getLeftLabel(self) -> str: ...

    @overload
    def getLeftLabel(self) -> str: ...

    def getMutuallyExclusiveTraits(self) -> ArrayList[str]: ...

    @overload
    def getRightLabel(self) -> str: ...

    @overload
    def getRightLabel(self) -> str: ...

    def getTexture(self) -> Texture: ...

    def getType(self) -> str: ...

    def getXPBoostMap(self) -> HashMap[PerkFactory.Perk, Integer]: ...

    def isFree(self) -> bool: ...

    def isRemoveInMP(self) -> bool: ...

    def setDescription(self, desc: str) -> None: ...

    def setFreeRecipes(self, freeRecipes: List[str]) -> None: ...

    def setRemoveInMP(self, removeInMP: bool) -> None: ...

    def __init__(self, tr: str, name: str, cost: int, desc: str, prof: bool, removeInMP: bool):
      self.cost: int
      self.description: str
      self.mutuallyexclusive: ArrayList[str]
      self.name: str
      self.prof: bool
      self.texture: Texture
      self.traitid: str
      self.xpboostmap: HashMap[PerkFactory.Perk, Integer]

