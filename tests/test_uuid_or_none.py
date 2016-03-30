import uuid

from lumbda.collection import uuid_or_none


def test_value_is_uuid():
    """
    Test that the function returns an uuid when the parameter is a valid uuid
    """
    sample_uuid = uuid.uuid4()

    assert uuid_or_none(str(sample_uuid)) == sample_uuid, 'It should return the given uuid string as uuid'


def test_value_is_not_uuid():
    """
    Test that the function returns None when the parameter is not valid
    """
    assert uuid_or_none('random') is None, 'It should return None when the parameter is a invalid string'
    assert uuid_or_none(None) is None, 'It should return None when the parameter is not a string'
