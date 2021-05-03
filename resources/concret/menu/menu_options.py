from resources.context.switch import Switch
from resources.concret.menu.menu_all_messages import show_all_messages
from resources.concret.menu.menu_one_message import show_one_message
from resources.concret.menu.menu_exit import close_app


def wait(word: str) -> None:
    input(f"\nPresione cualquier tecla para {word} ... ")


class MenuOptions(Switch):
    """Switch implementation from other languages to Python. This calls each menu."""
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
