from abc import ABC, abstractmethod


class Menu(ABC):
    """Abstract menu. repr must be implemented, but get_user_input is optional"""
    info_dictionary: dict = {}
    min_index: int = 0
    max_index: int = 0

    @abstractmethod
    def __repr__(self) -> str:
        pass

    def get_user_input(self, *args, **kwargs) -> int:
        pass
