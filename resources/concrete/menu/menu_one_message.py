from resources.concrete.welcome.welcome_message import WelcomeMessage
from resources.funcs.is_data import is_int, is_in_range


def get_user_input(min_index: int, max_index: int) -> int:
    """Function that makes user loop until a valid input is given"""
    while True:
        user_input: str = input(f"\nSelecciona el mensaje (entre {min_index} y {max_index}): ")
        if not is_int(user_input):
            print("Entrada incorrecta. Sólo se permiten enteros.")
        else:
            if is_in_range(int(user_input), min_index, max_index):
                return int(user_input)
            print(f"No es posible seleccionar enteros menores que {min_index} o mayores que {max_index}.")


def show_output(message: WelcomeMessage, index: int) -> None:
    """Get author and quote from WelcomeMessage instance like a python list, then print those variables"""
    author, quote = message[index]
    print(f"\n*{author}, dice: {quote}")


def show_one_message() -> None:
    """Function that shows only one message from a WelcomeMessage instance. User must provide a valid index"""
    # Create a WelcomeMessage instance and then get user input
    message = WelcomeMessage()
    if len(message) > 0:
        min_index = 1
        max_index = len(message)
        # Call get_user_input with min_index and max_index. Answer minus 1 because python positions start from 0
        user_message_index = get_user_input(min_index, max_index)-1
        # Finally, show a message with the provided user_message_index
        show_output(message, user_message_index)
    else:
        print("\nNo se encontraron mensajes")
