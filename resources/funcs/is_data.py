def is_in_range(value: int, low: int, high: int) -> bool:
    if low <= value <= high:
        return True
    return False


def is_int(value: str) -> bool:
    is_valid = True
    try:
        int(value)
    except ValueError:
        is_valid = False
    return is_valid
