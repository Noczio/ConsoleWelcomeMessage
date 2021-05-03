from resources.concrete.welcome.welcome_message import WelcomeMessage
from resources.context.menu import Menu


class AllMessageMenu(Menu):

    def __init__(self):
        self.message = WelcomeMessage()
        self.max_index = len(self.message )

    def __repr__(self) -> str:
        """Get author and quote from a WelcomeMessage instance in a for loop, then print those variables"""
        output = ""
        for data in self.message:
            author = data["Author"]
            quote = data["Quote"]
            output += f"\n*{author}, dice: {quote}"
        return output

    def get_user_input(self, *args, **kwargs) -> int:
        pass


def show_all_messages():
    menu = AllMessageMenu()
    number_of_messages = menu.max_index
    if number_of_messages > 0:
        print(menu)
    else:
        print("\nNo se encontraron mensajes")
