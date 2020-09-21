from abc import ABC, abstractmethod
import datetime
from typing import List

class Attachment(ABC):
    # use this when target platform does not support this type of attachment
    @abstractmethod
    def get_human_readable_explaination(self) -> str: ...


class Author(ABC):
    @abstractmethod
    @property
    def username(self) -> str: ...

    @username.setter
    @abstractmethod
    def username(self, value: str): ...

    # TODO: create class for profile pictures, maybe cache them?

    @abstractmethod
    @property
    def profile_picture(self): ...

    @profile_picture.setter
    @abstractmethod
    def profile_picture(self, value): ...


class Message(ABC):
    @abstractmethod
    @property
    def text(self) -> str: ...

    @text.setter
    @abstractmethod
    def text(self, value: str) -> None: ...
    
    @abstractmethod
    @property
    def date(self) -> datetime.datetime: ...

    @date.setter
    @abstractmethod
    def date(self, value: datetime.datetime) -> None: ...

    @abstractmethod
    @property
    def author(self) -> Author: ...

    @author.setter
    @abstractmethod
    def author(self, value: Author) -> None: ...

    @abstractmethod
    @property
    def attachments(self) -> List[Attachment]: ...

    @attachments.setter
    @abstractmethod
    def attachments(self, value: List[Attachment]) -> None: ...
