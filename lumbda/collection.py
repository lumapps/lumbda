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


def find_first(fn, iterable, kv_lambda=lambda it: enumerate(it)):
    """
    Find the first key, value of iterable for which fn(value) returns true
    iterable may be any container which support iteration or an iterator

    It is possible to pass a custom function that returns a (key, value)
    iterator of iterable

    Args:
        fn: the function that will match the iterator element
        iterable: the iterable
        kv_lambda (optional): a lambda returning a (key, value) iterator of iterable

    Returns:
        a (key, value) tuple of the first matching element or None

    """
    for key, value in kv_lambda(iterable):
        if fn(value):
            return key, value


def chunk(iterator, size=1):
    """
    Split a list in `n` items long chunks

    Args:
        iterator (iterable): the list to split
        size (int): the size of the chunks

    Returns:
        generator, a generator yielding each chunk
    """
    for idx in range(0, len(iterator), size):
        yield iterator[idx:idx + size]


def dict_update(source, update):
    """
    Functional dict.update that will return the results instead of
    updating the original dict.

    Args:
        source (dict): The dictionary to be updated
        update (dict): The dictionary that updates source

    Returns:
        the merge of the two dicts
    """
    source_copy = source.copy()
    source_copy.update(update)

    return source_copy


def deepgetattr(obj, attr, default=None):
    """
    Recurse through a deep attribute list and return the value or default

    Args:
        obj: the object
        attr (string): the attributes separated by dots
        default (optional): the default value

    Returns:
        the final value or default
    """
    try:
        return reduce(getattr, attr.split('.'), obj)
    except AttributeError:
        return default
