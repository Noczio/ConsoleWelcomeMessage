from resources.code.context.message import Message
from resources.code.funcs.load import load_json_file


class WelcomeMessage(Message):

    def __init__(self, file_path: str = ".\\resources\\info\\welcome_message.json"):
        self.data = load_json_file(file_path)
        self._current_index = 0
        self._min_index = 0
        self._max_index = len(data)-1 if len(data) > 0 else 0

    def __next__(self):
        self._current_index += 1
        if self._current_index > self._max_index:
            self._current_index = 0
            raise StopIteration
        return self.data[self._current_index]

    def __getitem__(self, index: Any) -> Any:
        if (index <= self._max_index) and (index >= -self._max_index):
            actual_data = self.data[index]
            author = actual_data["author"]
            quote = actual_data["quote"]
            return author, quote
            # key does not exist. Raise KeyError
        raise KeyError("Key does not exist")
        # key is not string. Raise TypeError
    raise TypeError("Key is not string")

