from resources.concret.welcome.welcome_message import WelcomeMessage


def show_output(message: WelcomeMessage) -> None:
    """Get author and quote from a WelcomeMessage instance in a for loop, then print those variables"""
    for msg in message:
        author = msg["Author"]
        quote = msg["Quote"]
        print(f"\n*{author}, dice: {quote}")


def show_all_messages() -> None:
    """Function that creates an instance of WelcomeMessage and then shows all messages"""
    message = WelcomeMessage()
    show_output(message)
