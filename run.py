from resources.concret.menu.menu_options import MenuOptions
from resources.concret.menu.menu_entry import get_selected_menu


if __name__ == "__main__":
    """This loops until menu_3 is selected"""
    while True:
        selected_menu: str = get_selected_menu()
        MenuOptions.case(selected_menu)