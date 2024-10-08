from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from com.google.common.util.concurrent import FutureCallback
from de.btobastian.javacord.entities import Server, Region, User, Channel, VoiceChannel, Invite
from de.btobastian.javacord.entities.message import Message
from de.btobastian.javacord.entities.permissions import PermissionsBuilder, Permissions
from de.btobastian.javacord.listener import Listener
from de.btobastian.javacord.utils import ThreadPool
from de.btobastian.javacord.utils.ratelimits import RateLimitManager
from java.awt.image import BufferedImage
from java.lang import Void
from java.util import Collection
from java.util.concurrent import Future

class DiscordAPI:

  @overload
  def acceptInvite(self, arg0: str) -> Future[Server]: ...

  @overload
  def acceptInvite(self, arg0: str, arg1: FutureCallback[Server]) -> Future[Server]: ...

  def checkTokenBlocking(self, arg0: str) -> bool: ...

  def connect(self, arg0: FutureCallback[DiscordAPI]) -> None: ...

  def connectBlocking(self) -> None: ...

  @overload
  def createServer(self, arg0: str) -> Future[Server]: ...

  @overload
  def createServer(self, arg0: str, arg1: FutureCallback[Server]) -> Future[Server]: ...

  @overload
  def createServer(self, arg0: str, arg1: Region) -> Future[Server]: ...

  @overload
  def createServer(self, arg0: str, arg1: BufferedImage) -> Future[Server]: ...

  @overload
  def createServer(self, arg0: str, arg1: Region, arg2: FutureCallback[Server]) -> Future[Server]: ...

  @overload
  def createServer(self, arg0: str, arg1: Region, arg2: BufferedImage) -> Future[Server]: ...

  @overload
  def createServer(self, arg0: str, arg1: BufferedImage, arg2: FutureCallback[Server]) -> Future[Server]: ...

  @overload
  def createServer(self, arg0: str, arg1: Region, arg2: BufferedImage, arg3: FutureCallback[Server]) -> Future[Server]: ...

  def deleteInvite(self, arg0: str) -> Future[Void]: ...

  def disconnect(self) -> None: ...

  def getCachedUserById(self, arg0: str) -> User: ...

  def getChannelById(self, arg0: str) -> Channel: ...

  def getChannels(self) -> Collection[Channel]: ...

  def getGame(self) -> str: ...

  def getMessageById(self, arg0: str) -> Message: ...

  def getMessageCacheSize(self) -> int: ...

  @overload
  def getPermissionsBuilder(self) -> PermissionsBuilder: ...

  @overload
  def getPermissionsBuilder(self, arg0: Permissions) -> PermissionsBuilder: ...

  def getRateLimitManager(self) -> RateLimitManager: ...

  def getServerById(self, arg0: str) -> Server: ...

  def getServers(self) -> Collection[Server]: ...

  def getStreamingUrl(self) -> str: ...

  def getThreadPool(self) -> ThreadPool: ...

  def getToken(self) -> str: ...

  def getUserById(self, arg0: str) -> Future[User]: ...

  def getUsers(self) -> Collection[User]: ...

  def getVoiceChannelById(self, arg0: str) -> VoiceChannel: ...

  def getVoiceChannels(self) -> Collection[VoiceChannel]: ...

  def getYourself(self) -> User: ...

  def isAutoReconnectEnabled(self) -> bool: ...

  def isIdle(self) -> bool: ...

  def isLazyLoading(self) -> bool: ...

  def isWaitingForServersOnStartup(self) -> bool: ...

  @overload
  def parseInvite(self, arg0: str) -> Future[Invite]: ...

  @overload
  def parseInvite(self, arg0: str, arg1: FutureCallback[Invite]) -> Future[Invite]: ...

  def registerListener(self, arg0: Listener) -> None: ...

  def setAutoReconnect(self, arg0: bool) -> None: ...

  def setEmail(self, arg0: str) -> None: ...

  @overload
  def setGame(self, arg0: str) -> None: ...

  @overload
  def setGame(self, arg0: str, arg1: str) -> None: ...

  def setIdle(self, arg0: bool) -> None: ...

  def setLazyLoading(self, arg0: bool) -> None: ...

  def setMessageCacheSize(self, arg0: int) -> None: ...

  def setPassword(self, arg0: str) -> None: ...

  def setReconnectRatelimit(self, arg0: int, arg1: int) -> None: ...

  def setToken(self, arg0: str, arg1: bool) -> None: ...

  def setWaitForServersOnStartup(self, arg0: bool) -> None: ...

  def updateAvatar(self, arg0: BufferedImage) -> Future[Void]: ...

  def updateEmail(self, arg0: str) -> Future[Void]: ...

  def updatePassword(self, arg0: str) -> Future[Void]: ...

  def updateProfile(self, arg0: str, arg1: str, arg2: str, arg3: BufferedImage) -> Future[Void]: ...

  def updateUsername(self, arg0: str) -> Future[Void]: ...

