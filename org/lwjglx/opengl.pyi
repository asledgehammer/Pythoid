from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import Canvas
from java.lang import RuntimeException, Throwable
from org.lwjgl.glfw import GLFWImage
from org.lwjgl.opengl import GLCapabilities

class Display:

  capabilities: GLCapabilities

  @staticmethod
  @overload
  def create() -> None: ...

  @staticmethod
  @overload
  def create(arg0: PixelFormat) -> None: ...

  @staticmethod
  def destroy() -> None: ...

  @staticmethod
  def getAdapter() -> str: ...

  @staticmethod
  def getAvailableDisplayModes() -> list[DisplayMode]: ...

  @staticmethod
  def getDesktopDisplayMode() -> DisplayMode: ...

  @staticmethod
  def getDisplayMode() -> DisplayMode: ...

  @staticmethod
  def getFramebufferHeight() -> int: ...

  @staticmethod
  def getFramebufferWidth() -> int: ...

  @staticmethod
  def getHeight() -> int: ...

  @staticmethod
  def getVersion() -> str: ...

  @staticmethod
  def getWidth() -> int: ...

  @staticmethod
  def getWindow() -> int: ...

  @staticmethod
  def getX() -> int: ...

  @staticmethod
  def getY() -> int: ...

  @staticmethod
  def isActive() -> bool: ...

  @staticmethod
  def isBorderlessWindow() -> bool: ...

  @staticmethod
  def isCloseRequested() -> bool: ...

  @staticmethod
  def isCreated() -> bool: ...

  @staticmethod
  def isCurrent() -> bool: ...

  @staticmethod
  def isDirty() -> bool: ...

  @staticmethod
  def isFullscreen() -> bool: ...

  @staticmethod
  def isResizable() -> bool: ...

  @staticmethod
  def isVisible() -> bool: ...

  @staticmethod
  def makeCurrent() -> None: ...

  @staticmethod
  def processMessages() -> None: ...

  @staticmethod
  def releaseContext() -> None: ...

  @staticmethod
  def setBorderlessWindow(arg0: bool) -> None: ...

  @staticmethod
  def setDisplayMode(arg0: DisplayMode) -> None: ...

  @staticmethod
  def setDisplayModeAndFullscreen(arg0: DisplayMode) -> None: ...

  @staticmethod
  def setFullscreen(arg0: bool) -> None: ...

  @staticmethod
  def setIcon(arg0: GLFWImage.Buffer) -> None: ...

  @staticmethod
  def setInitialBackground(arg0: float, arg1: float, arg2: float) -> None: ...

  @staticmethod
  def setLocation(arg0: int, arg1: int) -> None: ...

  @staticmethod
  def setParent(arg0: Canvas) -> None: ...

  @staticmethod
  def setResizable(arg0: bool) -> None: ...

  @staticmethod
  def setTitle(arg0: str) -> None: ...

  @staticmethod
  def setVSyncEnabled(arg0: bool) -> None: ...

  @staticmethod
  def swapBuffers() -> None: ...

  @staticmethod
  def sync(arg0: int) -> None: ...

  @staticmethod
  @overload
  def update() -> None: ...

  @staticmethod
  @overload
  def update(arg0: bool) -> None: ...

  @staticmethod
  def wasResized() -> bool: ...

  def __init__(self): ...

  class Window: ...

  class Callbacks: ...


class DisplayMode:

  def equals(self, arg0: object) -> bool: ...

  def getBitsPerPixel(self) -> int: ...

  def getFrequency(self) -> int: ...

  def getHeight(self) -> int: ...

  def getWidth(self) -> int: ...

  def hashCode(self) -> int: ...

  def isFullscreenCapable(self) -> bool: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: int, arg1: int): ...


class OpenGLException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class PixelFormat:

  def getAccumulationAlpha(self) -> int: ...

  def getAccumulationBitsPerPixel(self) -> int: ...

  def getAlphaBits(self) -> int: ...

  def getAuxBuffers(self) -> int: ...

  def getBitsPerPixel(self) -> int: ...

  def getDepthBits(self) -> int: ...

  def getSamples(self) -> int: ...

  def getStencilBits(self) -> int: ...

  def isFloatingPoint(self) -> bool: ...

  def isSRGB(self) -> bool: ...

  def isStereo(self) -> bool: ...

  def withAccumulationAlpha(self, arg0: int) -> PixelFormat: ...

  def withAccumulationBitsPerPixel(self, arg0: int) -> PixelFormat: ...

  def withAlphaBits(self, arg0: int) -> PixelFormat: ...

  def withAuxBuffers(self, arg0: int) -> PixelFormat: ...

  def withBitsPerPixel(self, arg0: int) -> PixelFormat: ...

  @overload
  def withCoverageSamples(self, arg0: int) -> PixelFormat: ...

  @overload
  def withCoverageSamples(self, arg0: int, arg1: int) -> PixelFormat: ...

  def withDepthBits(self, arg0: int) -> PixelFormat: ...

  def withFloatingPoint(self, arg0: bool) -> PixelFormat: ...

  def withFloatingPointPacked(self, arg0: bool) -> PixelFormat: ...

  def withSRGB(self, arg0: bool) -> PixelFormat: ...

  def withSamples(self, arg0: int) -> PixelFormat: ...

  def withStencilBits(self, arg0: int) -> PixelFormat: ...

  def withStereo(self, arg0: bool) -> PixelFormat: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: int, arg1: int, arg2: int): ...
  @overload
  def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int): ...
  @overload
  def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int): ...
  @overload
  def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: bool): ...
  @overload
  def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: bool, arg9: bool): ...


class PixelFormatLWJGL: ...


class Util:

  @staticmethod
  def checkGLError() -> None: ...

  @staticmethod
  def translateGLErrorString(arg0: int) -> str: ...

