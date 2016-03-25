import uuid


def to_uuid(value):
    """
    Convert the value to uuid if it's not already a uuid

    Args:
        value (string): the value to convert

    Returns:
        the converted value

    Raises:
        TypeError: when the value cannot be converted to a uuid
        ValueError: when the string is badly formed
    """
    if isinstance(value, uuid.UUID):
        return value
    return uuid.UUID(value)


def uuid_or_none(value):
    """
    Convert the value to uuid or return None if it cannot be converted

    Args:
        value: the value to convert

    Returns:
        the converted value or None
    """
    try:
        return to_uuid(value)
    except TypeError:
        return None
