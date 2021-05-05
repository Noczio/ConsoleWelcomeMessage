from abc import ABC, abstractmethod
from resources.context.limits import IndexLimits


class Menu(ABC, IndexLimits):
    """Abstract menu. repr must be implemented, but get_user_input is optional"""

    @abstractmethod
    def __repr__(self) -> str:
        pass

    def get_user_input(self, *args, **kwargs) -> int:
        pass
