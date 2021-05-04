from resources.concrete.welcome.welcome_message import WelcomeMessage
from resources.context.menu import Menu
from resources.funcs.user_input import get_user_input


class OneMessageMenu(Menu):
    """Show only one message implementation as class"""

    def __init__(self) -> None:
        self._message = WelcomeMessage()
        # min_index is 0 if there are not messages, else set it to 1
        self.min_index = 1 if len(self._message) > 0 else 0
        self.max_index = len(self._message)

    def __repr__(self) -> str:
        """Get author and quote from a WelcomeMessage instance like a python list, then print those variables"""
        author, quote = self._message[self.current_index]
        output = f"\n*{author}, dice: {quote}"
        return output

    def get_user_input(self, *args, **kwargs) -> int:
        self.current_index = get_user_input("mensaje", self.min_index, self.max_index) - 1
        return self.current_index


def show_one_message() -> None:
    """Function that shows only one message from a OneMessageMenu instance. User must provide a valid index"""
    menu = OneMessageMenu()
    number_of_messages = menu.max_index
    if number_of_messages > 0:
        menu.get_user_input()
        print(menu)
    else:
        print("\nNo se encontraron mensajes")
