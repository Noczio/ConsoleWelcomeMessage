from resources.funcs.is_data import is_int, is_in_range


def get_selected_menu() -> str:
    """Info shown when app starts. This returns a string with either  \"menu_\" + 1, 2 or 3"""
    show_options()
    selected_menu_int = get_user_input()
    menu_name = "menu_" + str(selected_menu_int)
    return menu_name


def show_options() -> None:
    main_info = {1: "Ver todos los mensajes",
                 2: "Ver un mensaje específico",
                 3: "Salir"}
    print("")  # line jump for aesthetic purposes
    for key, value in main_info.items():
        print(f"{key}. {value}")


def get_user_input() -> int:
    while True:
        user_input: str = input("\nSelecciona el menú (1, 2 o 3): ")
        if not is_int(user_input):
            print("Entrada incorrecta. Sólo se permiten enteros.")
        else:
            if is_in_range(int(user_input), 1, 4):
                return int(user_input)
            print("No es posible seleccionar enteros diferentes a 1, 2 o 3.")
