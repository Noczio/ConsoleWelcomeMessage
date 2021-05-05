def is_in_range(value: int, low: int, high: int) -> bool:
    """Function that Returns True if a integer value is inside a domain"""
    if low <= value <= high:
        return True
    return False


def is_int(value: str) -> bool:
    """Function that returns True if parameter can be parsed into a integer"""
    is_valid: bool = True
    try:
        int(value)
    except ValueError:
        is_valid = False
    return is_valid
