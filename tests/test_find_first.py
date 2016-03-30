import string
from lumbda.collection import find_first


def test_list():
    """
    Test find_first with a list as the iterable
    """
    numbers = range(1, 10)

    assert find_first(lambda x: not x % 3, numbers) == (2, 3), 'It should return the first number divisible by 3'
    assert find_first(lambda x: x == 5, numbers) == (4, 5), 'It should return 5'
    assert find_first(lambda _: True, numbers) == (0, 1), 'It should return the first element'
    assert find_first(lambda _: False, numbers) == (None, None), 'It should not find any element'


def test_dict():
    """
    Test find_first with a dict as the iterable
    """
    def kv_lambda(it):
        return it.iteritems()
    alphabet_map = {letter: idx for idx, letter in enumerate(string.ascii_lowercase)}

    assert find_first(lambda x: x == 4, alphabet_map, kv_lambda) == ('e', 4), 'It should return the fifth letter'
    assert find_first(lambda _: True, alphabet_map, kv_lambda) != (None, None), 'It should return the first element'
    assert find_first(lambda _: False, alphabet_map, kv_lambda) == (None, None), 'It should not find any element'


def test_set():
    """
    Test find_first with a set as the iterable
    """
    numbers = set(range(1, 10))

    assert find_first(lambda x: not x % 3, numbers) == (2, 3), 'It should return the first number divisible by 3'
    assert find_first(lambda x: x == 5, numbers) == (4, 5), 'It should return 5'
    assert find_first(lambda _: True, numbers) == (0, 1), 'It should return the first element'
    assert find_first(lambda _: False, numbers) == (None, None), 'It should not find any element'
