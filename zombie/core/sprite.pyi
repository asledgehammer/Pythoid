from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from java.util import List
from java.util.function import Consumer
from zombie.core import SpriteRenderer
from zombie.core.opengl import Shader
from zombie.core.skinnedmodel import ModelManager
from zombie.core.textures import TextureDraw, Texture, TextureFBO
from zombie.iso import PlayerCamera

class GenericSpriteRenderState:

  UVCA_CIRCLE: int

  UVCA_NOCIRCLE: int

  UVCA_NONE: int

  def CheckSpriteSlots(self) -> None: ...

  def EndShader(self) -> None: ...

  def ShaderUpdate1f(self, shaderID: int, uniform: int, uniformValue: float) -> None: ...

  def ShaderUpdate1i(self, shaderID: int, uniform: int, uniformValue: int) -> None: ...

  def ShaderUpdate2f(self, shaderID: int, uniform: int, value1: float, value2: float) -> None: ...

  def ShaderUpdate3f(self, shaderID: int, uniform: int, value1: float, value2: float, value3: float) -> None: ...

  def ShaderUpdate4f(self, shaderID: int, uniform: int, value1: float, value2: float, value3: float, value4: float) -> None: ...

  def StartShader(self, iD: int, playerIndex: int) -> None: ...

  def clear(self) -> None: ...

  def clearCutawayTexture(self) -> None: ...

  def clearUseVertColorsArray(self) -> None: ...

  def doCoreIntParam(self, id: int, val: float) -> None: ...

  def drawGeneric(self, gd: TextureDraw.GenericDrawer) -> None: ...

  def drawModel(self, model: ModelManager.ModelSlot) -> None: ...

  def drawParticles(self, playerIndex: int, var1: int, var2: int) -> None: ...

  def drawPuddles(self, shader: Shader, playerIndex: int, apiId: int, z: int) -> None: ...

  def drawSkyBox(self, shader: Shader, playerIndex: int, apiId: int, bufferId: int) -> None: ...

  def drawWater(self, shader: Shader, playerIndex: int, apiId: int, bShore: bool) -> None: ...

  def glAlphaFunc(self, a: int, b: float) -> None: ...

  def glBind(self, a: int) -> None: ...

  def glBlendEquation(self, a: int) -> None: ...

  def glBlendFunc(self, a: int, b: int) -> None: ...

  def glBlendFuncSeparate(self, a: int, b: int, c: int, d: int) -> None: ...

  def glBuffer(self, i: int, p: int) -> None: ...

  def glClear(self, a: int) -> None: ...

  def glClearColor(self, r: int, g: int, b: int, a: int) -> None: ...

  def glColorMask(self, a: int, b: int, c: int, d: int) -> None: ...

  def glDepthMask(self, b: bool) -> None: ...

  def glDisable(self, a: int) -> None: ...

  def glDoEndFrame(self) -> None: ...

  def glDoEndFrameFx(self, player: int) -> None: ...

  @overload
  def glDoStartFrame(self, w: int, h: int, zoom: float, player: int) -> None: ...

  @overload
  def glDoStartFrame(self, w: int, h: int, zoom: float, player: int, isTextFrame: bool) -> None: ...

  def glDoStartFrameFx(self, w: int, h: int, player: int) -> None: ...

  def glEnable(self, a: int) -> None: ...

  def glGenerateMipMaps(self, a: int) -> None: ...

  def glIgnoreStyles(self, b: bool) -> None: ...

  def glLoadIdentity(self) -> None: ...

  def glStencilFunc(self, a: int, b: int, c: int) -> None: ...

  def glStencilMask(self, a: int) -> None: ...

  def glStencilOp(self, a: int, b: int, c: int) -> None: ...

  def glTexParameteri(self, a: int, b: int, c: int) -> None: ...

  def glViewport(self, x: int, y: int, width: int, height: int) -> None: ...

  def isReady(self) -> bool: ...

  def isRendered(self) -> bool: ...

  def isRendering(self) -> bool: ...

  def onReady(self) -> None: ...

  def onRenderAcquired(self) -> None: ...

  def onRendered(self) -> None: ...

  @overload
  def render(self, tex: Texture, x: float, y: float, width: float, height: float, r: float, g: float, b: float, a: float, texdModifier: Consumer[TextureDraw]) -> None: ...

  @overload
  def render(self, tex: Texture, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, c1: int, c2: int, c3: int, c4: int) -> None: ...

  @overload
  def render(self, tex: Texture, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, r: float, g: float, b: float, a: float, texdModifier: Consumer[TextureDraw]) -> None: ...

  @overload
  def render(self, tex: Texture, x: float, y: float, width: float, height: float, r: float, g: float, b: float, a: float, u1: float, v1: float, u2: float, v2: float, u3: float, v3: float, u4: float, v4: float, texdModifier: Consumer[TextureDraw]) -> None: ...

  @overload
  def render(self, tex: Texture, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, r1: float, g1: float, b1: float, a1: float, r2: float, g2: float, b2: float, a2: float, r3: float, g3: float, b3: float, a3: float, r4: float, g4: float, b4: float, a4: float, texdModifier: Consumer[TextureDraw]) -> None: ...

  @overload
  def renderPoly(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def renderPoly(self, tex: Texture, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def renderPoly(self, tex: Texture, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, r: float, g: float, b: float, a: float, u1: float, v1: float, u2: float, v2: float, u3: float, v3: float, u4: float, v4: float) -> None: ...

  def renderRect(self, x: int, y: int, width: int, height: int, r: float, g: float, b: float, a: float) -> None: ...

  def renderdebug(self, tex: Texture, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, r1: float, g1: float, b1: float, a1: float, r2: float, g2: float, b2: float, a2: float, r3: float, g3: float, b3: float, a3: float, r4: float, g4: float, b4: float, a4: float, texdModifier: Consumer[TextureDraw]) -> None: ...

  def renderflipped(self, tex: Texture, x: float, y: float, width: float, height: float, r: float, g: float, b: float, a: float, texdModifier: Consumer[TextureDraw]) -> None: ...

  @overload
  def renderline(self, tex: Texture, x1: int, y1: int, x2: int, y2: int, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def renderline(self, tex: Texture, x1: float, y1: float, x2: float, y2: float, r: float, g: float, b: float, a: float, thickness: int) -> None: ...

  def setCutawayTexture(self, tex: Texture, x: int, y: int, w: int, h: int) -> None: ...

  def setExtraWallShaderParams(self, wallTexRender: SpriteRenderer.WallShaderTexRender) -> None: ...

  def setUseVertColorsArray(self, whichShader: int, c0: int, c1: int, c2: int, c3: int) -> None: ...

  @staticmethod
  def clearSprites(postRender: List[TextureDraw]) -> None: ...


class RenderStateSlot(Enum):

  Populating: RenderStateSlot

  Ready: RenderStateSlot

  Rendering: RenderStateSlot

  def count(self) -> int: ...

  def index(self) -> int: ...

  @staticmethod
  def valueOf(arg0: str) -> RenderStateSlot: ...

  @staticmethod
  def values() -> list[RenderStateSlot]: ...


class SpriteRenderState(GenericSpriteRenderState):

  def CheckSpriteSlots(self) -> None: ...

  def clear(self) -> None: ...

  def getActiveState(self) -> GenericSpriteRenderState: ...

  def onReady(self) -> None: ...

  def onRendered(self) -> None: ...

  def prePopulating(self) -> None: ...

  def __init__(self, index: int):
    self.fbo: TextureFBO
    self.maxzoomlevel: float
    self.minzoomlevel: float
    self.playerambient: list[float]
    self.playercamera: list[PlayerCamera]
    self.playerindex: int
    self.stateui: SpriteRenderStateUI
    self.time: int
    self.zoomlevel: list[float]


class SpriteRenderStateUI(GenericSpriteRenderState):

  def clear(self) -> None: ...

  def __init__(self, index: int):
    self.bactive: bool


class SpriteRendererStates:

  def getPopulating(self) -> SpriteRenderState: ...

  def getPopulatingActiveState(self) -> GenericSpriteRenderState: ...

  def getReady(self) -> SpriteRenderState: ...

  def getRendered(self) -> SpriteRenderState: ...

  def getRendering(self) -> SpriteRenderState: ...

  def getRenderingActiveState(self) -> GenericSpriteRenderState: ...

  def movePopulatingToReady(self) -> None: ...

  def moveReadyToRendering(self) -> None: ...

  def setPopulating(self, populating: SpriteRenderState) -> None: ...

  def setReady(self, ready: SpriteRenderState) -> None: ...

  def setRendered(self, rendered: SpriteRenderState) -> None: ...

  def setRendering(self, rendering: SpriteRenderState) -> None: ...

  def __init__(self): ...

