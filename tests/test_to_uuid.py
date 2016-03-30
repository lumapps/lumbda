import pytest
import uuid

from lumbda.collection import to_uuid


def test_with_uuid():
    """
    Test that it returns the parameter when it's already an uuid
    """
    sample_uuid = uuid.uuid4()

    assert to_uuid(sample_uuid) is sample_uuid, 'It should return the parameter'


def test_with_string():
    """
    Test that it returns an uuid or raise when the parameter is a string
    """
    sample_uuid = uuid.uuid4()

    assert to_uuid(str(sample_uuid)) == sample_uuid, 'It should return the given uuid string as an uuid'
    assert to_uuid(unicode(sample_uuid)) == sample_uuid, 'It should return the given uuid unicode as an uuid'

    # It should raise ValueError when the parameter is not a valid UUID
    with pytest.raises(ValueError):
        to_uuid('random')

    # It should raise TypeError when the parameter is not a string
    with pytest.raises(TypeError):
        to_uuid(None)
