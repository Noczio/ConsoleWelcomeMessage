from resources.concrete.welcome.welcome_message import WelcomeMessage
from resources.funcs.user_input import get_user_input
from resources.context.menu import Menu


class OneMessageMenu(Menu):
    """Show only one message implementation as class"""
    def __init__(self):
        self.message = WelcomeMessage()
        # min_index is 0 if there are not messages, else set it to 1
        self.min_index = 1 if len(self.message) > 0 else 0
        self.max_index = len(self.message)
        self.user_index = 0

    def __repr__(self) -> str:
        """Get author and quote from a WelcomeMessage instance like a python list, then print those variables"""
        author, quote = self.message[self.user_index]
        output = f"\n*{author}, dice: {quote}"
        return output

    def get_user_input(self, *args, **kwargs) -> int:
        self.user_index = get_user_input("mensaje", self.min_index, self.max_index) - 1
        return self.user_index


def show_one_message() -> None:
    """Function that shows only one message from a WelcomeMessage instance. User must provide a valid index"""
    menu = OneMessageMenu()
    number_of_messages = menu.max_index
    if number_of_messages > 0:
        menu.get_user_input()
        print(menu)
    else:
        print("\nNo se encontraron mensajes")
