from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from java.nio import ByteBuffer, FloatBuffer, IntBuffer
from java.util import List, Set, Map

V3 = TypeVar('V3', default=Any)
M4 = TypeVar('M4', default=Any)
C = TypeVar('C', default=Any)
N = TypeVar('N', default=Any)
Q = TypeVar('Q', default=Any)

class AiBuiltInWrapperProvider:

  @overload
  def wrapColor(self, arg0: ByteBuffer, arg1: int) -> AiColor: ...

  @overload
  def wrapColor(self, arg0: ByteBuffer, arg1: int) -> object: ...

  @overload
  def wrapColor(self, arg0: ByteBuffer, arg1: int) -> object: ...

  @overload
  def wrapMatrix4f(self, arg0: list[float]) -> object: ...

  @overload
  def wrapMatrix4f(self, arg0: list[float]) -> AiMatrix4f: ...

  @overload
  def wrapMatrix4f(self, arg0: list[float]) -> object: ...

  @overload
  def wrapQuaternion(self, arg0: ByteBuffer, arg1: int) -> AiQuaternion: ...

  @overload
  def wrapQuaternion(self, arg0: ByteBuffer, arg1: int) -> object: ...

  @overload
  def wrapQuaternion(self, arg0: ByteBuffer, arg1: int) -> object: ...

  @overload
  def wrapSceneNode(self, arg0: object, arg1: object, arg2: list[int], arg3: str) -> AiNode: ...

  @overload
  def wrapSceneNode(self, arg0: object, arg1: object, arg2: list[int], arg3: str) -> object: ...

  @overload
  def wrapSceneNode(self, arg0: object, arg1: object, arg2: list[int], arg3: str) -> object: ...

  @overload
  def wrapVector3f(self, arg0: ByteBuffer, arg1: int, arg2: int) -> object: ...

  @overload
  def wrapVector3f(self, arg0: ByteBuffer, arg1: int, arg2: int) -> AiVector: ...

  @overload
  def wrapVector3f(self, arg0: ByteBuffer, arg1: int, arg2: int) -> object: ...

  def __init__(self): ...


class AiColor:

  def getAlpha(self) -> float: ...

  def getBlue(self) -> float: ...

  def getGreen(self) -> float: ...

  def getRed(self) -> float: ...

  def setAlpha(self, arg0: float) -> None: ...

  def setBlue(self, arg0: float) -> None: ...

  def setGreen(self, arg0: float) -> None: ...

  def setRed(self, arg0: float) -> None: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: ByteBuffer, arg1: int): ...


class AiMatrix4f:

  def get(self, arg0: int, arg1: int) -> float: ...

  def toByteBuffer(self) -> FloatBuffer: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: list[float]): ...


class AiMesh:

  def getBitangentBuffer(self) -> FloatBuffer: ...

  def getBitangentX(self, arg0: int) -> float: ...

  def getBitangentY(self, arg0: int) -> float: ...

  def getBitangentZ(self, arg0: int) -> float: ...

  def getBones(self) -> List[AiBone]: ...

  def getColorA(self, arg0: int, arg1: int) -> float: ...

  def getColorB(self, arg0: int, arg1: int) -> float: ...

  def getColorBuffer(self, arg0: int) -> FloatBuffer: ...

  def getColorG(self, arg0: int, arg1: int) -> float: ...

  def getColorR(self, arg0: int, arg1: int) -> float: ...

  def getFaceBuffer(self) -> IntBuffer: ...

  def getFaceNumIndices(self, arg0: int) -> int: ...

  def getFaceOffsets(self) -> IntBuffer: ...

  def getFaceVertex(self, arg0: int, arg1: int) -> int: ...

  def getIndexBuffer(self) -> IntBuffer: ...

  def getMaterialIndex(self) -> int: ...

  def getName(self) -> str: ...

  def getNormalBuffer(self) -> FloatBuffer: ...

  def getNormalX(self, arg0: int) -> float: ...

  def getNormalY(self, arg0: int) -> float: ...

  def getNormalZ(self, arg0: int) -> float: ...

  def getNumFaces(self) -> int: ...

  def getNumUVComponents(self, arg0: int) -> int: ...

  def getNumVertices(self) -> int: ...

  def getPositionBuffer(self) -> FloatBuffer: ...

  def getPositionX(self, arg0: int) -> float: ...

  def getPositionY(self, arg0: int) -> float: ...

  def getPositionZ(self, arg0: int) -> float: ...

  def getPrimitiveTypes(self) -> Set[AiPrimitiveType]: ...

  def getTangentBuffer(self) -> FloatBuffer: ...

  def getTangentX(self, arg0: int) -> float: ...

  def getTangentY(self, arg0: int) -> float: ...

  def getTangentZ(self, arg0: int) -> float: ...

  def getTexCoordBuffer(self, arg0: int) -> FloatBuffer: ...

  def getTexCoordU(self, arg0: int, arg1: int) -> float: ...

  def getTexCoordV(self, arg0: int, arg1: int) -> float: ...

  def getTexCoordW(self, arg0: int, arg1: int) -> float: ...

  def getWrappedBitangent(self, arg0: int, arg1: AiWrapperProvider[V3, M4, C, N, Q]) -> object: ...

  def getWrappedColor(self, arg0: int, arg1: int, arg2: AiWrapperProvider[V3, M4, C, N, Q]) -> object: ...

  def getWrappedNormal(self, arg0: int, arg1: AiWrapperProvider[V3, M4, C, N, Q]) -> object: ...

  def getWrappedPosition(self, arg0: int, arg1: AiWrapperProvider[V3, M4, C, N, Q]) -> object: ...

  def getWrappedTangent(self, arg0: int, arg1: AiWrapperProvider[V3, M4, C, N, Q]) -> object: ...

  def getWrappedTexCoords(self, arg0: int, arg1: int, arg2: AiWrapperProvider[V3, M4, C, N, Q]) -> object: ...

  def hasBones(self) -> bool: ...

  def hasColors(self, arg0: int) -> bool: ...

  def hasFaces(self) -> bool: ...

  def hasNormals(self) -> bool: ...

  def hasPositions(self) -> bool: ...

  def hasTangentsAndBitangents(self) -> bool: ...

  @overload
  def hasTexCoords(self) -> bool: ...

  @overload
  def hasTexCoords(self, arg0: int) -> bool: ...

  def hasVertexColors(self) -> bool: ...

  def isPureTriangle(self) -> bool: ...

  def toString(self) -> str: ...


class AiNode:

  def findNode(self, arg0: str) -> AiNode: ...

  def getChildren(self) -> List[AiNode]: ...

  def getMeshes(self) -> list[int]: ...

  def getMetadata(self) -> Map[str, AiMetadataEntry]: ...

  def getName(self) -> str: ...

  def getNumChildren(self) -> int: ...

  def getNumMeshes(self) -> int: ...

  def getParent(self) -> AiNode: ...

  def getTransform(self, arg0: AiWrapperProvider[V3, M4, C, N, Q]) -> object: ...


class AiPostProcessSteps(Enum):

  CALC_TANGENT_SPACE: AiPostProcessSteps

  DEBONE: AiPostProcessSteps

  FIND_DEGENERATES: AiPostProcessSteps

  FIND_INSTANCES: AiPostProcessSteps

  FIND_INVALID_DATA: AiPostProcessSteps

  FIX_INFACING_NORMALS: AiPostProcessSteps

  FLIP_UVS: AiPostProcessSteps

  FLIP_WINDING_ORDER: AiPostProcessSteps

  GEN_NORMALS: AiPostProcessSteps

  GEN_SMOOTH_NORMALS: AiPostProcessSteps

  GEN_UV_COORDS: AiPostProcessSteps

  IMPROVE_CACHE_LOCALITY: AiPostProcessSteps

  JOIN_IDENTICAL_VERTICES: AiPostProcessSteps

  LIMIT_BONE_WEIGHTS: AiPostProcessSteps

  MAKE_LEFT_HANDED: AiPostProcessSteps

  OPTIMIZE_GRAPH: AiPostProcessSteps

  OPTIMIZE_MESHES: AiPostProcessSteps

  PRE_TRANSFORM_VERTICES: AiPostProcessSteps

  REMOVE_COMPONENT: AiPostProcessSteps

  REMOVE_REDUNDANT_MATERIALS: AiPostProcessSteps

  SORT_BY_PTYPE: AiPostProcessSteps

  SPLIT_BY_BONE_COUNT: AiPostProcessSteps

  SPLIT_LARGE_MESHES: AiPostProcessSteps

  TRANSFORM_UV_COORDS: AiPostProcessSteps

  TRIANGULATE: AiPostProcessSteps

  VALIDATE_DATA_STRUCTURE: AiPostProcessSteps

  @staticmethod
  def valueOf(arg0: str) -> AiPostProcessSteps: ...

  @staticmethod
  def values() -> list[AiPostProcessSteps]: ...


class AiQuaternion:

  def getW(self) -> float: ...

  def getX(self) -> float: ...

  def getY(self) -> float: ...

  def getZ(self) -> float: ...

  def setW(self, arg0: float) -> None: ...

  def setX(self, arg0: float) -> None: ...

  def setY(self, arg0: float) -> None: ...

  def setZ(self, arg0: float) -> None: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: ByteBuffer, arg1: int): ...


class AiScene:

  def getAnimations(self) -> List[AiAnimation]: ...

  def getCameras(self) -> List[AiCamera]: ...

  def getLights(self) -> List[AiLight]: ...

  def getMaterials(self) -> List[AiMaterial]: ...

  def getMeshes(self) -> List[AiMesh]: ...

  def getNumAnimations(self) -> int: ...

  def getNumCameras(self) -> int: ...

  def getNumLights(self) -> int: ...

  def getNumMaterials(self) -> int: ...

  def getNumMeshes(self) -> int: ...

  def getSceneRoot(self, arg0: AiWrapperProvider[V3, M4, C, N, Q]) -> object: ...

  def toString(self) -> str: ...


class AiVector:

  def getNumComponents(self) -> int: ...

  def getX(self) -> float: ...

  def getY(self) -> float: ...

  def getZ(self) -> float: ...

  def setX(self, arg0: float) -> None: ...

  def setY(self, arg0: float) -> None: ...

  def setZ(self, arg0: float) -> None: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: ByteBuffer, arg1: int, arg2: int): ...


class AiWrapperProvider[V3, M4, C, N, Q]:

  def wrapColor(self, arg0: ByteBuffer, arg1: int) -> object: ...

  def wrapMatrix4f(self, arg0: list[float]) -> object: ...

  def wrapQuaternion(self, arg0: ByteBuffer, arg1: int) -> object: ...

  def wrapSceneNode(self, arg0: object, arg1: object, arg2: list[int], arg3: str) -> object: ...

  def wrapVector3f(self, arg0: ByteBuffer, arg1: int, arg2: int) -> object: ...


class JassimpLibraryLoader:

  def loadLibrary(self) -> None: ...

  def __init__(self): ...

