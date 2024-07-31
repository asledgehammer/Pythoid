from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from gnu.trove.list.array import TIntArrayList
from java.lang import Boolean, Integer, Enum
from java.nio import ByteBuffer
from java.nio.file import FileSystem
from java.util import ArrayList, HashMap
from org.joml import Vector2d, Matrix4f, Vector3f
from se.krka.kahlua.vm import KahluaTable
from zombie.Lua import LuaManager
from zombie.asset import Asset, AssetType, AssetPath, AssetManager
from zombie.characters import IsoPlayer
from zombie.config import ConfigOption, BooleanConfigOption, DoubleConfigOption
from zombie.core.skinnedmodel import ModelCamera
from zombie.core.textures import Texture, TextureID, TextureDraw
from zombie.fileSystem import FileTask, FileSystem, IFileTaskCallback
from zombie.inventory.types import MapItem
from zombie.ui import UIElement
from zombie.worldMap.markers import WorldMapMarkers, WorldMapMarkersV1
from zombie.worldMap.styles import WorldMapStyle, WorldMapStyleV1, WorldMapStyleLayer
from zombie.worldMap.symbols import WorldMapSymbolsV1

class FileTask_LoadWorldMapBinary(FileTask):

  def call(self) -> object: ...

  def done(self) -> None: ...

  def getErrorMessage(self) -> str: ...

  def __init__(self, worldMapData: WorldMapData, filename: str, fileSystem: FileSystem, cb: IFileTaskCallback): ...


class FileTask_LoadWorldMapXML(FileTask):

  def call(self) -> object: ...

  def done(self) -> None: ...

  def getErrorMessage(self) -> str: ...

  def __init__(self, worldMapData: WorldMapData, filename: str, fileSystem: FileSystem, cb: IFileTaskCallback): ...


class ImagePyramid:

  def destroy(self) -> None: ...

  def generateFiles(self, imageFile: str, outputDirectory: str) -> None: ...

  def generateZip(self, imageFile: str, zipFile: str) -> None: ...

  def getImage(self, x: int, y: int, z: int) -> Texture: ...

  def getTexture(self, x: int, y: int, z: int) -> TextureID: ...

  def openZipFile(self) -> FileSystem: ...

  def setDirectory(self, directory: str) -> None: ...

  def setZipFile(self, zipFile: str) -> None: ...

  def __init__(self): ...

  class PyramidTexture:

    def __init__(self): ...


class MapDefinitions:

  def pickRandom(self) -> str: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getInstance() -> MapDefinitions: ...

  def __init__(self): ...


class MapProjection:

  EARTH_CIRCUMFERENCE_METERS: float

  EARTH_HALF_CIRCUMFERENCE_METERS: float

  EARTH_RADIUS_METERS: float

  MAX_LATITUDE_DEGREES: float

  @staticmethod
  def exp2(N: float) -> float: ...

  @staticmethod
  def log2(N: float) -> float: ...

  def __init__(self): ...

  class ProjectedMeters(Vector2d):

    def __init__(self): ...

  class LngLat:

    def __init__(self, lng: float, lat: float): ...

  class BoundingBox:

    def __init__(self, min: Vector2d, max: Vector2d): ...


class Rasterize:

  def __init__(self): ...

  class Edge: ...


class StrokeGeometry:

  def __init__(self): ...

  class Point: ...

  class Attrs: ...


class UIWorldMap(UIElement):

  def getAPI(self) -> UIWorldMapV1: ...

  def getAPIv1(self) -> UIWorldMapV1: ...

  def onMouseDown(self, x: float, y: float) -> Boolean: ...

  def onMouseMove(self, dx: float, dy: float) -> Boolean: ...

  def onMouseUp(self, x: float, y: float) -> Boolean: ...

  def onMouseUpOutside(self, x: float, y: float) -> None: ...

  def onMouseWheel(self, delta: float) -> Boolean: ...

  def render(self) -> None: ...

  def update(self) -> None: ...

  @staticmethod
  def setExposed(exposer: LuaManager.Exposer) -> None: ...

  def __init__(self, table: KahluaTable): ...


class UIWorldMapV1:

  def addData(self, fileName: str) -> None: ...

  def addImages(self, directory: str) -> None: ...

  def centerOn(self, worldX: float, worldY: float) -> None: ...

  def clearData(self) -> None: ...

  def endDirectoryData(self) -> None: ...

  def getBaseZoom(self) -> float: ...

  def getBoolean(self, name: str) -> bool: ...

  def getCenterWorldX(self) -> float: ...

  def getCenterWorldY(self) -> float: ...

  def getDataCount(self) -> int: ...

  def getDataFileByIndex(self, index: int) -> str: ...

  def getDouble(self, name: str, defaultValue: float) -> float: ...

  def getHeightInCells(self) -> int: ...

  def getHeightInSquares(self) -> int: ...

  def getImagesCount(self) -> int: ...

  def getMarkers(self) -> WorldMapMarkers: ...

  def getMarkersAPI(self) -> WorldMapMarkersV1: ...

  def getMaxXInCells(self) -> int: ...

  def getMaxXInSquares(self) -> int: ...

  def getMaxYInCells(self) -> int: ...

  def getMaxYInSquares(self) -> int: ...

  def getMinXInCells(self) -> int: ...

  def getMinXInSquares(self) -> int: ...

  def getMinYInCells(self) -> int: ...

  def getMinYInSquares(self) -> int: ...

  def getOptionByIndex(self, index: int) -> ConfigOption: ...

  def getOptionCount(self) -> int: ...

  def getRenderer(self) -> WorldMapRenderer: ...

  def getStyle(self) -> WorldMapStyle: ...

  def getStyleAPI(self) -> WorldMapStyleV1: ...

  def getSymbolsAPI(self) -> WorldMapSymbolsV1: ...

  def getWidthInCells(self) -> int: ...

  def getWidthInSquares(self) -> int: ...

  def getWorldScale(self) -> float: ...

  def getZoomF(self) -> float: ...

  def mouseToWorldX(self) -> float: ...

  def mouseToWorldY(self) -> float: ...

  def moveView(self, dx: float, dy: float) -> None: ...

  def resetView(self) -> None: ...

  def setBackgroundRGBA(self, r: float, g: float, b: float, a: float) -> None: ...

  def setBoolean(self, name: str, value: bool) -> None: ...

  def setBoundsFromData(self) -> None: ...

  def setBoundsFromWorld(self) -> None: ...

  def setBoundsInCells(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  def setBoundsInSquares(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  def setDouble(self, name: str, value: float) -> None: ...

  def setDropShadowWidth(self, width: int) -> None: ...

  def setMapItem(self, mapItem: MapItem) -> None: ...

  def setUnvisitedGridRGBA(self, r: float, g: float, b: float, a: float) -> None: ...

  def setUnvisitedRGBA(self, r: float, g: float, b: float, a: float) -> None: ...

  def setZoom(self, zoom: float) -> None: ...

  @overload
  def uiToWorldX(self, uiX: float, uiY: float) -> float: ...

  @overload
  def uiToWorldX(self, uiX: float, uiY: float, zoomF: float, centerWorldX: float, centerWorldY: float) -> float: ...

  @overload
  def uiToWorldY(self, uiX: float, uiY: float) -> float: ...

  @overload
  def uiToWorldY(self, uiX: float, uiY: float, zoomF: float, centerWorldX: float, centerWorldY: float) -> float: ...

  def worldOriginX(self) -> float: ...

  def worldOriginY(self) -> float: ...

  def worldToUIX(self, worldX: float, worldY: float) -> float: ...

  def worldToUIY(self, worldX: float, worldY: float) -> float: ...

  def zoomAt(self, uiX: float, uiY: float, delta: float) -> None: ...

  def __init__(self, ui: UIWorldMap): ...


class VASErenderer:

  @staticmethod
  def n_drawLineString(points: list[float], npoints: int, lineWidth: float, r: float, g: float, b: float, a: float) -> None: ...

  def __init__(self): ...


class VBOLinesUV:

  @overload
  def addElement(self, x: float, y: float, z: float, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def addElement(self, x: float, y: float, z: float, u: float, v: float, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def addLine(self, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def addLine(self, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, r0: float, g0: float, b0: float, a0: float, r1: float, g1: float, b1: float, a1: float) -> None: ...

  @overload
  def addQuad(self, x0: float, y0: float, u0: float, v0: float, x1: float, y1: float, u1: float, v1: float, z: float, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def addQuad(self, x0: float, y0: float, u0: float, v0: float, x1: float, y1: float, u1: float, v1: float, x2: float, y2: float, u2: float, v2: float, x3: float, y3: float, u3: float, v3: float, z: float, r: float, g: float, b: float, a: float) -> None: ...

  def addTriangle(self, x0: float, y0: float, z0: float, u0: float, v0: float, x1: float, y1: float, z1: float, u1: float, v1: float, x2: float, y2: float, z2: float, u2: float, v2: float, r: float, g: float, b: float, a: float) -> None: ...

  def flush(self) -> None: ...

  def reserve(self, numElements: int) -> None: ...

  def setLineWidth(self, width: float) -> None: ...

  def setMode(self, mode: int) -> None: ...

  def setOffset(self, dx: float, dy: float, dz: float) -> None: ...

  def startRun(self, textureID: TextureID) -> None: ...

  def __init__(self): ...

  class Run: ...


class WorldMap:

  def addData(self, fileName: str) -> None: ...

  def addImages(self, directory: str) -> None: ...

  def clearData(self) -> None: ...

  def endDirectoryData(self) -> None: ...

  def getCell(self, x: int, y: int) -> WorldMapCell: ...

  def getDataByIndex(self, index: int) -> WorldMapData: ...

  def getDataCount(self) -> int: ...

  def getDataHeightInCells(self) -> int: ...

  def getDataHeightInSquares(self) -> int: ...

  def getDataWidthInCells(self) -> int: ...

  def getDataWidthInSquares(self) -> int: ...

  def getHeightInCells(self) -> int: ...

  def getHeightInSquares(self) -> int: ...

  def getImagesByIndex(self, index: int) -> WorldMapImages: ...

  def getImagesCount(self) -> int: ...

  def getMaxXInCells(self) -> int: ...

  def getMaxXInSquares(self) -> int: ...

  def getMaxYInCells(self) -> int: ...

  def getMaxYInSquares(self) -> int: ...

  def getMinXInCells(self) -> int: ...

  def getMinXInSquares(self) -> int: ...

  def getMinYInCells(self) -> int: ...

  def getMinYInSquares(self) -> int: ...

  def getWidthInCells(self) -> int: ...

  def getWidthInSquares(self) -> int: ...

  def hasData(self) -> bool: ...

  def hasImages(self) -> bool: ...

  def isLastDataInDirectory(self, data: WorldMapData) -> bool: ...

  @overload
  def onStateChanged(self, oldState: Asset.State, newState: Asset.State, asset: Asset) -> None: ...

  @overload
  def onStateChanged(self, oldState: Asset.State, newState: Asset.State, asset: Asset) -> None: ...

  def setBoundsFromData(self) -> None: ...

  def setBoundsFromWorld(self) -> None: ...

  def setBoundsInCells(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  def setBoundsInSquares(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  def __init__(self):
    self.m_data: ArrayList[WorldMapData]
    self.m_images: ArrayList[WorldMapImages]
    self.m_lastdataindirectory: ArrayList[WorldMapData]
    self.m_maxdatax: int
    self.m_maxdatay: int
    self.m_maxx: int
    self.m_maxy: int
    self.m_mindatax: int
    self.m_mindatay: int
    self.m_minx: int
    self.m_miny: int


class WorldMapBinary:

  def read(self, filePath: str, data: WorldMapData) -> bool: ...

  def __init__(self): ...


class WorldMapCell:

  def dispose(self) -> None: ...

  def hitTest(self, x: float, y: float, features: ArrayList[WorldMapFeature]) -> None: ...

  def __init__(self):
    self.m_features: ArrayList[WorldMapFeature]
    self.m_x: int
    self.m_y: int


class WorldMapData(Asset):

  ASSET_TYPE: AssetType

  s_fileNameToData: HashMap[str, WorldMapData]

  def clear(self) -> None: ...

  def getCell(self, x: int, y: int) -> WorldMapCell: ...

  def getHeightInCells(self) -> int: ...

  def getHeightInSquares(self) -> int: ...

  def getType(self) -> AssetType: ...

  def getWidthInCells(self) -> int: ...

  def getWidthInSquares(self) -> int: ...

  def hitTest(self, x: float, y: float, features: ArrayList[WorldMapFeature]) -> None: ...

  def onLoaded(self) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getOrCreateData(fileName: str) -> WorldMapData: ...

  @overload
  def __init__(self, path: AssetPath, manager: AssetManager):
    self.m_celllookup: HashMap[Integer, WorldMapCell]

    self.m_cells: ArrayList[WorldMapCell]

    self.m_maxx: int

    self.m_maxy: int

    self.m_minx: int

    self.m_miny: int

    self.m_relativefilename: str

  @overload
  def __init__(self, path: AssetPath, manager: AssetManager, params: AssetManager.AssetParams): ...


class WorldMapDataAssetManager(AssetManager):

  instance: WorldMapDataAssetManager

  def __init__(self): ...


class WorldMapFeature:

  def containsPoint(self, x: float, y: float) -> bool: ...

  def dispose(self) -> None: ...

  def hasLineString(self) -> bool: ...

  def hasPoint(self) -> bool: ...

  def hasPolygon(self) -> bool: ...


class WorldMapGeometry:

  def calculateBounds(self) -> None: ...

  def containsPoint(self, x: float, y: float) -> bool: ...

  def dispose(self) -> None: ...

  def triangulate(self, delta: list[float]) -> None: ...

  def __init__(self):
    self.m_maxx: int
    self.m_maxy: int
    self.m_minx: int
    self.m_miny: int
    self.m_points: ArrayList[WorldMapPoints]
    self.m_triangles: list[float]
    self.m_trianglesperzoom: ArrayList[WorldMapGeometry.TrianglesPerZoom]
    self.m_type: WorldMapGeometry.Type
    self.m_vboindex1: int
    self.m_vboindex2: int
    self.m_vboindex3: int
    self.m_vboindex4: int

  class Type(Enum):

    LineString: WorldMapGeometry.Type

    Point: WorldMapGeometry.Type

    Polygon: WorldMapGeometry.Type

    @staticmethod
    def valueOf(arg0: str) -> WorldMapGeometry.Type: ...

    @staticmethod
    def values() -> list[WorldMapGeometry.Type]: ...

  class PolygonHit(Enum):

    Inside: WorldMapGeometry.PolygonHit

    OnEdge: WorldMapGeometry.PolygonHit

    Outside: WorldMapGeometry.PolygonHit

    @staticmethod
    def valueOf(arg0: str) -> WorldMapGeometry.PolygonHit: ...

    @staticmethod
    def values() -> list[WorldMapGeometry.PolygonHit]: ...

  class TrianglesPerZoom:

    def __init__(self):
      self.m_triangles: list[float]


class WorldMapImages:

  def getMaxX(self) -> int: ...

  def getMaxY(self) -> int: ...

  def getMinX(self) -> int: ...

  def getMinY(self) -> int: ...

  def getPyramid(self) -> ImagePyramid: ...

  def getResolution(self) -> float: ...

  def getZoom(self, zoomF: float) -> int: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getOrCreate(directory: str) -> WorldMapImages: ...

  def __init__(self): ...


class WorldMapJNI:

  @staticmethod
  def init() -> None: ...

  def __init__(self): ...


class WorldMapPoint:

  def __init__(self):
    self.x: int
    self.y: int


class WorldMapPoints(TIntArrayList):

  def calculateBounds(self) -> None: ...

  def getX(self, index: int) -> int: ...

  def getY(self, index: int) -> int: ...

  def isClockwise(self) -> bool: ...

  def numPoints(self) -> int: ...

  def __init__(self): ...


class WorldMapProperties(HashMap):

  def __init__(self): ...


class WorldMapRemotePlayer:

  def getAccessLevel(self) -> str: ...

  def getChangeCount(self) -> int: ...

  def getForename(self) -> str: ...

  def getOnlineID(self) -> int: ...

  def getSurname(self) -> str: ...

  @overload
  def getUsername(self) -> str: ...

  @overload
  def getUsername(self, arg0: Boolean) -> str: ...

  def getX(self) -> float: ...

  def getY(self) -> float: ...

  def hasFullData(self) -> bool: ...

  def isAccessLevel(self, arg0: str) -> bool: ...

  def isInvisible(self) -> bool: ...

  def setFullData(self, arg0: int, arg1: str, arg2: str, arg3: str, arg4: str, arg5: float, arg6: float, arg7: bool) -> None: ...

  def setPlayer(self, arg0: IsoPlayer) -> None: ...

  def setPosition(self, arg0: float, arg1: float) -> None: ...

  def __init__(self, arg0: int): ...


class WorldMapRemotePlayers:

  instance: WorldMapRemotePlayers

  def Reset(self) -> None: ...

  def getOrCreatePlayer(self, arg0: IsoPlayer) -> WorldMapRemotePlayer: ...

  def getOrCreatePlayerByID(self, arg0: int) -> WorldMapRemotePlayer: ...

  def getPlayerByID(self, arg0: int) -> WorldMapRemotePlayer: ...

  def getPlayers(self) -> ArrayList[WorldMapRemotePlayer]: ...

  def removePlayerByID(self, arg0: int) -> None: ...

  def __init__(self): ...


class WorldMapRenderLayer:

  def __init__(self): ...


class WorldMapRenderer:

  def centerOn(self, worldX: float, worldY: float) -> None: ...

  def getAbsoluteX(self) -> int: ...

  def getAbsoluteY(self) -> int: ...

  def getBaseZoom(self) -> float: ...

  def getBoolean(self, name: str) -> bool: ...

  def getCenterWorldX(self) -> float: ...

  def getCenterWorldY(self) -> float: ...

  def getDisplayZoomF(self) -> float: ...

  def getDouble(self, name: str, defaultValue: float) -> float: ...

  def getHeight(self) -> int: ...

  def getModelViewMatrix(self) -> Matrix4f: ...

  def getOptionByIndex(self, index: int) -> ConfigOption: ...

  def getOptionByName(self, name: str) -> ConfigOption: ...

  def getOptionCount(self) -> int: ...

  def getProjectionMatrix(self) -> Matrix4f: ...

  def getWidth(self) -> int: ...

  def getWorldMap(self) -> WorldMap: ...

  def getWorldScale(self, zoomF: float) -> float: ...

  def getZoom(self) -> int: ...

  def getZoomF(self) -> float: ...

  def log2(self, x: float) -> float: ...

  def moveView(self, dx: int, dy: int) -> None: ...

  def render(self, ui: UIWorldMap) -> None: ...

  def resetView(self) -> None: ...

  def sceneToUI(self, sceneX: float, sceneY: float, sceneZ: float, projection: Matrix4f, modelView: Matrix4f, out: Vector3f) -> Vector3f: ...

  def setBoolean(self, name: str, value: bool) -> None: ...

  def setDouble(self, name: str, value: float) -> None: ...

  def setDropShadowWidth(self, width: int) -> None: ...

  def setMap(self, worldMap: WorldMap, x: int, y: int, width: int, height: int) -> None: ...

  def setVisited(self, visited: WorldMapVisited) -> None: ...

  def setZoom(self, zoom: float) -> None: ...

  def uiToScene(self, uiX: float, uiY: float, projection: Matrix4f, modelView: Matrix4f, out: Vector3f) -> Vector3f: ...

  @overload
  def uiToWorldX(self, uiX: float, uiY: float, zoomF: float, centerWorldX: float, centerWorldY: float) -> float: ...

  @overload
  def uiToWorldX(self, uiX: float, uiY: float, zoomF: float, centerWorldX: float, centerWorldY: float, projection: Matrix4f, modelView: Matrix4f) -> float: ...

  @overload
  def uiToWorldY(self, uiX: float, uiY: float, zoomF: float, centerWorldX: float, centerWorldY: float) -> float: ...

  @overload
  def uiToWorldY(self, uiX: float, uiY: float, zoomF: float, centerWorldX: float, centerWorldY: float, projection: Matrix4f, modelView: Matrix4f) -> float: ...

  def updateView(self) -> None: ...

  def worldOriginUIX(self, zoomF: float, centerWorldX: float) -> float: ...

  def worldOriginUIY(self, zoomF: float, centerWorldY: float) -> float: ...

  def worldToUIX(self, worldX: float, worldY: float, zoomF: float, centerWorldX: float, centerWorldY: float, projection: Matrix4f, modelView: Matrix4f) -> float: ...

  def worldToUIY(self, worldX: float, worldY: float, zoomF: float, centerWorldX: float, centerWorldY: float, projection: Matrix4f, modelView: Matrix4f) -> float: ...

  def zoomAt(self, mouseX: int, mouseY: int, delta: int) -> None: ...

  @overload
  def zoomMult(self) -> float: ...

  @overload
  def zoomMult(self, zoomF: float) -> float: ...

  def __init__(self):
    self.m_style: WorldMapStyle

  class Drawer(TextureDraw.GenericDrawer):

    def drawLineString(self, args: WorldMapStyleLayer.RenderArgs, feature: WorldMapFeature, color: WorldMapStyleLayer.RGBAf, lineWidth: float) -> None: ...

    def drawLineStringTexture(self, args: WorldMapStyleLayer.RenderArgs, feature: WorldMapFeature, color: WorldMapStyleLayer.RGBAf, lineWidth: float, texture: Texture) -> None: ...

    def drawLineStringXXX(self, args: WorldMapStyleLayer.RenderArgs, feature: WorldMapFeature, color: WorldMapStyleLayer.RGBAf, lineWidth: float) -> None: ...

    def drawLineStringYYY(self, args: WorldMapStyleLayer.RenderArgs, feature: WorldMapFeature, color: WorldMapStyleLayer.RGBAf, lineWidth: float) -> None: ...

    def drawTexture(self, texture: Texture, fill: WorldMapStyleLayer.RGBAf, worldX1: int, worldY1: int, worldX2: int, worldY2: int) -> None: ...

    @overload
    def drawTextureTiled(self, texture: Texture, fill: WorldMapStyleLayer.RGBAf, worldX1: int, worldY1: int, worldX2: int, worldY2: int, cellX: int, cellY: int) -> None: ...

    @overload
    def drawTextureTiled(self, texture: Texture, fill: WorldMapStyleLayer.RGBAf, worldX1: int, worldY1: int, worldX2: int, worldY2: int, tileW: int, tileH: int, cellX: int, cellY: int) -> None: ...

    @overload
    def fillPolygon(self, args: WorldMapStyleLayer.RenderArgs, feature: WorldMapFeature, color: WorldMapStyleLayer.RGBAf) -> None: ...

    @overload
    def fillPolygon(self, args: WorldMapStyleLayer.RenderArgs, feature: WorldMapFeature, color: WorldMapStyleLayer.RGBAf, texture: Texture, textureScale: float) -> None: ...

    def getAbsoluteX(self) -> int: ...

    def getAbsoluteY(self) -> int: ...

    def getHeight(self) -> int: ...

    def getWidth(self) -> int: ...

    def getWorldScale(self) -> float: ...

    def postRender(self) -> None: ...

    def render(self) -> None: ...

    def uiToWorldX(self, uiX: float, uiY: float) -> float: ...

    def uiToWorldY(self, uiX: float, uiY: float) -> float: ...

    def worldOriginUIX(self, centerWorldX: float) -> float: ...

    def worldOriginUIY(self, centerWorldY: float) -> float: ...

  class CharacterModelCamera(ModelCamera):

    def Begin(self) -> None: ...

    def End(self) -> None: ...

  class WorldMapBooleanOption(BooleanConfigOption):

    def __init__(self, arg0: WorldMapRenderer, arg1: str, arg2: bool): ...

  class WorldMapDoubleOption(DoubleConfigOption):

    def __init__(self, arg0: WorldMapRenderer, arg1: str, arg2: float, arg3: float, arg4: float): ...

  class PlayerRenderData: ...


class WorldMapSettings:

  VERSION: int

  VERSION1: int

  def getBoolean(self, name: str) -> bool: ...

  def getDouble(self, name: str, defaultValue: float) -> float: ...

  def getFileVersion(self) -> int: ...

  def getOptionByIndex(self, index: int) -> ConfigOption: ...

  def getOptionByName(self, name: str) -> ConfigOption: ...

  def getOptionCount(self) -> int: ...

  def load(self) -> None: ...

  def save(self) -> None: ...

  def setBoolean(self, name: str, value: bool) -> None: ...

  def setDouble(self, name: str, value: float) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getInstance() -> WorldMapSettings: ...

  def __init__(self): ...

  class WorldMap:

    def __init__(self, arg0: WorldMapSettings):
      self.centerx: DoubleConfigOption
      self.centery: DoubleConfigOption
      self.isometric: BooleanConfigOption
      self.showsymbolsui: BooleanConfigOption
      self.zoom: DoubleConfigOption

  class MiniMap:

    def __init__(self, arg0: WorldMapSettings):
      self.isometric: BooleanConfigOption
      self.showsymbols: BooleanConfigOption
      self.startvisible: BooleanConfigOption
      self.zoom: DoubleConfigOption


class WorldMapVBOs:

  NUM_ELEMENTS: int

  def addElement(self, x: float, y: float, z: float, r: float, g: float, b: float, a: float) -> None: ...

  def create(self) -> None: ...

  def drawElements(self, mode: int, index1: int, index2: int, count: int) -> None: ...

  def reserveVertices(self, numVertices: int, indices: list[int]) -> None: ...

  def reset(self) -> None: ...

  @staticmethod
  def getInstance() -> WorldMapVBOs: ...

  def __init__(self): ...

  class WorldMapVBO: ...


class WorldMapVisited:

  def clearKnownInCells(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  def clearKnownInSquares(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  def clearVisitedInCells(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  def clearVisitedInSquares(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  def forget(self) -> None: ...

  def getMinX(self) -> int: ...

  def getMinY(self) -> int: ...

  @overload
  def load(self) -> None: ...

  @overload
  def load(self, input: ByteBuffer, WorldVersion: int) -> None: ...

  def render(self, renderX: float, renderY: float, minX: int, minY: int, maxX: int, maxY: int, worldScale: float, blur: bool) -> None: ...

  def renderGrid(self, renderX: float, renderY: float, minX: int, minY: int, maxX: int, maxY: int, worldScale: float, zoomF: float) -> None: ...

  def renderMain(self) -> None: ...

  @overload
  def save(self) -> None: ...

  @overload
  def save(self, output: ByteBuffer) -> None: ...

  def setBounds(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  def setKnownInCells(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  def setKnownInSquares(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  def setVisitedInCells(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  def setVisitedInSquares(self, minX: int, minY: int, maxX: int, maxY: int) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def SaveAll() -> None: ...

  @staticmethod
  def getInstance() -> WorldMapVisited: ...

  @staticmethod
  def update() -> None: ...

  def __init__(self): ...


class WorldMapXML:

  def read(self, filePath: str, data: WorldMapData) -> bool: ...

  def __init__(self): ...
