from resources.funcs.user_input import get_user_input
from resources.context.menu import Menu


class StartMessageMenu(Menu):
    def __init__(self) -> None:
        # variables that can be accessed by functions and other modules
        self.info_dictionary = {1: "Ver todos los mensajes",
                                2: "Ver un mensaje específico",
                                3: "Salir"}
        # All possible inputs as a list
        valid_values = list(self.info_dictionary.keys())
        # Save into min_index and max_index the smallest and biggest value from valid_values list
        self.min_index = min(valid_values)
        self.max_index = max(valid_values)

    def __repr__(self) -> str:
        """Function than prints main_menu_dictionary index and value in a for loop"""
        print("")  # Line jump for aesthetic purposes
        output = ""
        for index, value in self.info_dictionary.items():
            if index < self.max_index:
                output += f"{index}. {value}\n"
            else:
                output += f"{index}. {value}"
        return output

    def get_user_input(self, *args, **kwargs) -> int:
        selected_menu_int = get_user_input("menú", self.min_index, self.max_index)
        return selected_menu_int


def get_selected_menu() -> str:
    """Info shown when app starts. This returns a string after user's input validation"""
    # First, show available options
    menu = StartMessageMenu()
    number_of_menus = menu.max_index
    if number_of_menus > 0:
        print(menu)
        # Next, call get_user_input with min and max indexes
        selected_menu_int = menu.get_user_input()
        # Finally, return a menu name. "menu_" + "1", "2" or "3"
        menu_name = "menu_" + str(selected_menu_int)
        return menu_name
    else:
        print("No se encontró el menú principal")
        menu_name = "menu_" + str(3)
        return menu_name
