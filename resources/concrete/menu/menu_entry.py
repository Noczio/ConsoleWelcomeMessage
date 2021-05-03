from resources.funcs.is_data import is_int, is_in_range

main_menu_dictionary = {1: "Ver todos los mensajes",
                        2: "Ver un mensaje específico",
                        3: "Salir"}


def get_selected_menu() -> str:
    """Info shown when app starts. This returns a string after user's input validation"""
    # First, show available options
    show_options()
    # Second, get all possible inputs as a list
    valid_values = list(main_menu_dictionary.keys())
    # Next, save into min_index and max_index the smallest and biggest value from valid_values list
    min_index = min(valid_values)
    max_index = max(valid_values)
    # Next, call get_user_input with min and max indexes
    selected_menu_int = get_user_input(min_index, max_index)
    # Finally, return a menu name. "menu_" + "1", "2" or "3"
    menu_name = "menu_" + str(selected_menu_int)
    return menu_name


def show_options() -> None:
    """Function than prints main_menu_dictionary index and value in a for loop"""
    print("")
    for menu_index, menu_value in main_menu_dictionary.items():
        print(f"{menu_index}. {menu_value}")


def get_user_input(min_index: int, max_index: int) -> int:
    """Function that makes user loop until a valid input is given"""
    while True:
        user_input: str = input(f"\nSelecciona el menú (entre {min_index} y {max_index}): ")
        if not is_int(user_input):
            print("Entrada incorrecta. Sólo se permiten enteros.")
        else:
            if is_in_range(int(user_input), min_index, max_index):
                return int(user_input)
            print(f"No es posible seleccionar enteros menores que {min_index} o mayores que {max_index}.")
