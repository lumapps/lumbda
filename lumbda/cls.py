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
