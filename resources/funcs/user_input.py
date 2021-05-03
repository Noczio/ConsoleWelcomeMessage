from resources.funcs.is_data import is_int, is_in_range


def get_user_input(text: str, min_index: int, max_index: int) -> int:
    """Function that makes user loop until a valid input is given"""
    while True:
        user_input: str = input(f"\nSelecciona el {text} (entre {min_index} y {max_index}): ")
        if not is_int(user_input):
            print("Entrada incorrecta. Sólo se permiten enteros.")
        else:
            if is_in_range(int(user_input), min_index, max_index):
                return int(user_input)
            print(f"No es posible seleccionar enteros menores que {min_index} o mayores que {max_index}.")
