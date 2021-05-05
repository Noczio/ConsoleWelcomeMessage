from resources.concrete.welcome.welcome_message import WelcomeMessage
from resources.context.message import Message
from resources.context.menu import Menu


class AllMessageMenu(Menu):
    """Show all messages implementation as class"""

    def __init__(self) -> None:
        self._message: Message = WelcomeMessage()
        self.max_index: int = len(self._message)

    def __repr__(self) -> str:
        """Get author and quote from a WelcomeMessage instance in a for loop, then print those variables"""
        output: str = ""
        for counter, data in enumerate(self._message, start=0):
            author = data["Author"]
            quote = data["Quote"]
            if counter < self.max_index - 1:
                output += f"\n*{author}, dice: {quote}\n"
            else:
                output += f"\n*{author}, dice: {quote}"
        return output


def show_all_messages() -> None:
    """Function that shows all messages from a AllMessageMenu instance"""
    menu: Menu = AllMessageMenu()
    number_of_messages: int = menu.max_index
    if number_of_messages > 0:
        print(menu)
    else:
        print("\nNo se encontraron mensajes")
