from resources.concrete.welcome.welcome_message import WelcomeMessage


def show_output(message: WelcomeMessage) -> None:
    """Get author and quote from a WelcomeMessage instance in a for loop, then print those variables"""
    for data in message:
        author = data["Author"]
        quote = data["Quote"]
        print(f"\n*{author}, dice: {quote}")


def show_all_messages() -> None:
    """Function that creates an instance of WelcomeMessage and then shows all messages"""
    message = WelcomeMessage()
    if len(message) > 0:
        show_output(message)
    else:
        print("\nNo se encontraron mensajes")
