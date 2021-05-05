def wait_for_any_input(word: str) -> None:
    """Makes user press any input to continue. A "word" string must be provided"""
    input(f"\nPresione cualquier tecla para {word} ... ")
