from resources.context.message import Message
from resources.funcs.load import load_json_file
from typing import Any


class WelcomeMessage(Message):

    def __init__(self, file_path: str = ".\\resources\\info\\welcome_message.json"):
        self.data = load_json_file(file_path)
        self._current_index = 0
        self._min_index = 0
        self._max_index = len(self.data)-1 if len(self.data) > 0 else 0

    def __next__(self) -> tuple:
        self._current_index += 1
        if self._current_index > self._max_index:
            self._current_index = 0
            raise StopIteration
        return self.data[self._current_index]

    def __getitem__(self, index: int) -> tuple:
        if (index <= self._max_index) and (index >= -self._max_index):
            actual_data = self.data[index]
            author = actual_data["Author"]
            quote = actual_data["Quote"]
            return author, quote
            # key does not exist. Raise KeyError
        raise KeyError("Key does not exist")

