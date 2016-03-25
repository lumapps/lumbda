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
