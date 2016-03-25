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
