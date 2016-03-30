from lumbda.collection import dict_update


def test_empty_source():
    """
    The returned dict should be the update when the source is empty
    """
    update = {'hello': 'world'}

    assert dict_update({}, update) == update, 'It should return an update copy'
    assert dict_update({}, update) is not update, 'It should not return a reference to update'
    assert dict_update({}, {}) == {}, 'It should return update'


def test_empty_update():
    """
    The returned dict should be the source when the update is empty
    """
    source = {'hello': 'world'}

    assert dict_update(source, {}) == source, 'It should return a source copy'
    assert dict_update(source, {}) is not source, 'It should not return a reference to source'
    assert dict_update({}, {}) == {}, 'It should return source'


def test_dict_update():
    """
    The returned dict should be a merge of update in source
    """
    source = {0: 'hello', 1: 'world'}

    assert dict_update(source, {0: 'random'}) == {0: 'random', 1: 'world'}
    assert dict_update(source, {0: 'random', 2: 'dream'}) == {0: 'random', 1: 'world', 2: 'dream'}
