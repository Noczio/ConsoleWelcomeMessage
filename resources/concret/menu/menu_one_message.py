from resources.concret.welcome.welcome_message import WelcomeMessage
from resources.funcs.is_data import is_int, is_in_range


def get_user_input(min_index: int, max_index: int) -> int:
    while True:
        user_input: str = input(f"\nSelecciona el mensaje (entre {min_index} y {max_index}): ")
        if not is_int(user_input):
            print("Entrada incorrecta. Sólo se permiten enteros.")
        else:
            if is_in_range(int(user_input), min_index, max_index):
                return int(user_input)
            print(f"No es posible seleccionar enteros menores que {min_index} o mayores que {max_index}")


def show_menu(message: WelcomeMessage, index: int) -> None:
    author, quote = message[index]
    print(f"\n*{author}, dice: {quote}")


def show_one_message() -> None:
    message = WelcomeMessage()
    user_message_index = get_user_input(0, len(message)-1)
    show_menu(message, user_message_index)


