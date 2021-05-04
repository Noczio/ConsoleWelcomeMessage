from resources.context.limits import IndexLimits
from abc import ABC, abstractmethod
from typing import Any


class Message(ABC, IndexLimits):
    """Abstract Message. data property must be loaded. Also, __getitem__ and __next__ must be implemented."""
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
