from resources.concrete.menu.all_messages_menu import show_all_messages
from resources.concrete.menu.one_message_menu import show_one_message
from resources.concrete.menu.exit_menu import close_app
from resources.funcs.wait import wait_for_any_input
from resources.context.switch import Switch


class MenuOptions(Switch):
    """Calls a menu with method "case" inherited from class Switch"""
    @staticmethod
    def menu_1() -> None:
        show_all_messages()
        wait_for_any_input("volver al menú principal")

    @staticmethod
    def menu_2() -> None:
        show_one_message()
        wait_for_any_input("volver al menú principal")

    @staticmethod
    def menu_3() -> None:
        wait_for_any_input("terminar")
        close_app()
