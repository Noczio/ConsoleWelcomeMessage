from resources.concret.welcome.welcome_message import WelcomeMessage


def show_menu(message: WelcomeMessage) -> None:
    for msg in message:
        author = msg["author"]
        quote = msg["quote"]
        print(author, "dice:", quote)


def show_all_messages() -> None:
    message = WelcomeMessage()
    show_menu(message)


