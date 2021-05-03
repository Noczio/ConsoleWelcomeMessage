from abc import ABC, abstractmethod
from typing import Any


class Message(ABC):

    _data: Any

    @abstractmethod
    def __getitem__(self, key: Any) -> Any:
        pass

    @abstractmethod
    def __next__(self) -> Any:
        pass

    def __iter__(self) -> "Message":
        return self

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        self._data = value

    def __len__(self) -> int:
        return len(self.data)
