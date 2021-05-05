from resources.context.message import Message
from resources.funcs.load import load_json_file


class WelcomeMessage(Message):

    def __init__(self, file_path: str = ".\\resources\\info\\welcome_message.json") -> None:
        """__init__ constructor. file_path doesnt need to be provided by default"""
        # Load json file and the set _current_index, _min_index and _max_index
        self._data: list = load_json_file(file_path)
        # If there is not data after loading the json file the set _max_index to 0
        self.max_index: int = len(self._data) - 1 if len(self._data) > 0 else 0

    def __next__(self) -> dict:
        """__next__ implementation for class WelcomeMessage"""
        if self.current_index > self.max_index:
            self.current_index = 0
            raise StopIteration
        actual_data: dict = self._data[self.current_index]
        self.current_index += 1
        return actual_data

    def __getitem__(self, index: int) -> tuple:
        """__getitem__ implementation for class WelcomeMessage"""
        # If index is inside boundaries then return a tuple that contains an author and quote
        if (index <= self.max_index) and (index >= -self.max_index):
            actual_data: dict = self._data[index]
            author: str = actual_data["Author"]
            quote: str = actual_data["Quote"]
            return author, quote
        # Index out of boundaries. Raise IndexError
        raise IndexError("Index out of boundaries")
