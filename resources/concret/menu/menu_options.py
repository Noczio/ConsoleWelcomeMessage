from resources.concret.menu.menu_all_messages import show_all_messages
from resources.concret.menu.menu_one_message import show_one_message
from resources.concret.menu.menu_exit import close_app
from resources.context.switch import Switch


def wait(word: str) -> None:
    """Makes user press any input to continue. A "word" string must be provided"""
    input(f"\nPresione cualquier tecla para {word} ... ")


class MenuOptions(Switch):
    """Calls a menu with method "case" inherited from class Switch"""
    @staticmethod
    def menu_1() -> None:
        show_all_messages()
        wait("volver al menú principal")

    @staticmethod
    def menu_2() -> None:
        show_one_message()
        wait("volver al menú principal")

    @staticmethod
    def menu_3() -> None:
        wait("terminar")
        close_app()
