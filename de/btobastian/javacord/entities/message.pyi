from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from com.google.common.util.concurrent import FutureCallback
from de.btobastian.javacord.entities import CustomEmoji, User, Channel
from de.btobastian.javacord.entities.message.embed import Embed, EmbedBuilder
from de.btobastian.javacord.entities.permissions import Role
from java.io import File, InputStream
from java.lang import Void
from java.util import Collection, Calendar, List, Iterator
from java.util.concurrent import Future

class Message:

  def addCustomEmojiReaction(self, arg0: CustomEmoji) -> Future[Void]: ...

  def addUnicodeReaction(self, arg0: str) -> Future[Void]: ...

  def compareTo(self, arg0: object) -> int: ...

  def delete(self) -> Future[Void]: ...

  def edit(self, arg0: str) -> Future[Void]: ...

  def getAttachments(self) -> Collection[MessageAttachment]: ...

  def getAuthor(self) -> User: ...

  def getChannelReceiver(self) -> Channel: ...

  def getContent(self) -> str: ...

  def getCreationDate(self) -> Calendar: ...

  def getEmbeds(self) -> Collection[Embed]: ...

  def getId(self) -> str: ...

  def getMentionedRoles(self) -> List[Role]: ...

  def getMentions(self) -> List[User]: ...

  def getNonce(self) -> str: ...

  def getReactions(self) -> List[Reaction]: ...

  def getReceiver(self) -> MessageReceiver: ...

  def getUserReceiver(self) -> User: ...

  def isDeleted(self) -> bool: ...

  def isMentioningEveryone(self) -> bool: ...

  def isPinned(self) -> bool: ...

  def isPrivateMessage(self) -> bool: ...

  def isTts(self) -> bool: ...

  def pin(self) -> Future[Void]: ...

  def removeAllReactions(self) -> Future[Void]: ...

  @overload
  def reply(self, arg0: str) -> Future[Message]: ...

  @overload
  def reply(self, arg0: str, arg1: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def reply(self, arg0: str, arg1: EmbedBuilder) -> Future[Message]: ...

  @overload
  def reply(self, arg0: str, arg1: EmbedBuilder, arg2: FutureCallback[Message]) -> Future[Message]: ...


class MessageHistory:

  def getMessageById(self, arg0: str) -> Message: ...

  def getMessages(self) -> Collection[Message]: ...

  def getMessagesSorted(self) -> List[Message]: ...

  def getNewestMessage(self) -> Message: ...

  def getOldestMessage(self) -> Message: ...

  def iterator(self) -> Iterator[Message]: ...


class MessageReceiver:

  def getId(self) -> str: ...

  @overload
  def getMessageHistory(self, arg0: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistory(self, arg0: int, arg1: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryAfter(self, arg0: Message, arg1: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryAfter(self, arg0: str, arg1: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryAfter(self, arg0: Message, arg1: int, arg2: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryAfter(self, arg0: str, arg1: int, arg2: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryBefore(self, arg0: Message, arg1: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryBefore(self, arg0: str, arg1: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryBefore(self, arg0: Message, arg1: int, arg2: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryBefore(self, arg0: str, arg1: int, arg2: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def sendFile(self, arg0: File) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: File, arg1: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: File, arg1: str) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: InputStream, arg1: str) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: File, arg1: str, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: InputStream, arg1: str, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: InputStream, arg1: str, arg2: str) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: InputStream, arg1: str, arg2: str, arg3: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: bool) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: bool, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: bool, arg2: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: bool) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: str, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: bool, arg2: str, arg3: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: bool, arg3: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: bool, arg3: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: str, arg3: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: bool, arg3: str, arg4: FutureCallback[Message]) -> Future[Message]: ...

  def type(self) -> None: ...

