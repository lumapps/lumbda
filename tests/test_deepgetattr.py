from lumbda.collection import deepgetattr


class MyClass(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)


def test_object_hasattr():
    """
    Test that the looked for attribute is found when present
    """
    my_object = MyClass(attribute=3, sub_object=MyClass(attribute=5))

    assert deepgetattr(my_object, 'attribute') == 3, 'It should return my_object.attribute'
    assert deepgetattr(my_object, 'sub_object.attribute') == 5, 'It should return my_object.sub_object.attribute'


def test_object_doesnt_haveattr():
    """
    Test that the return value is the default one when the looked for
    attribute is not present
    """
    my_object = MyClass(attribute=3, sub_object=MyClass(attribute=5))

    assert deepgetattr(my_object, 'hello') is None, 'It should return the default value'
    assert deepgetattr(my_object, 'hello', False) is False, 'It should return the given default value'
    assert deepgetattr(my_object, 'hello', 'world') == 'world', 'It should return the given default value'
    assert deepgetattr(my_object, 'hello.world') is None, 'It should return the default value'
    assert deepgetattr(my_object, 'attribute.hello') is None, 'It should return the default value'
    assert deepgetattr(my_object, 'sub_object.hello') is None, 'It should return the default value'
    assert deepgetattr(my_object, '') is None, 'It should return the default value'
