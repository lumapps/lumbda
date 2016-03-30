from lumbda.collection import chunk


def test_chunk():
    """
    Test that the chunk function splits the iterator
    """
    numbers = range(1, 100)

    assert len(list(chunk(numbers, size=20))) == 5, 'It should be cut in 5 lists'

    flat_chunks = [elem for sublist in chunk(numbers, size=20) for elem in sublist]
    assert flat_chunks == numbers, 'It should reflatten to the original list'

    assert list(chunk(numbers, size=20))[0] == range(1, 21), 'The first chunk should be the 20 first elements'
    assert list(chunk(numbers, size=20))[-1] == range(81, 100), 'The first chunk should be the 20 last elements'


def test_bigger_size():
    """
    Test that the function returns the whole list when the size is bigger than the iterator
    """
    numbers = range(10)

    assert len(list(chunk(numbers, size=10))) == 1, 'It should be cut in a single list'
    assert len(list(chunk(numbers, size=100))) == 1, 'It should be cut in a single list'
