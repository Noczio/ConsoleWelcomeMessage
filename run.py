from resources.concrete.menu.options import MenuOptions
from resources.concrete.menu.start_menu import get_selected_menu


if __name__ == "__main__":
    """Main logic. This loops until menu_3 is selected"""
    try:
        while True:
            # First get a menu. menu_1, menu_2 or menu_3
            selected_menu = get_selected_menu()
            # Next, call switch MenuOptions with selected_menu
            MenuOptions.case(selected_menu)
    except Exception as e:
        raise e
