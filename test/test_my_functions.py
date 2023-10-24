import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(number_one=1, number_two=4)
    assert result == 5

def test_add_string():
    result = my_functions.add(number_one="I like ",number_two="burgers")
    assert  result == "I like burgers"
def test_divide():
    result = my_functions.divide(number_one=10, number_two=5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(number_one=10, number_two=0)
