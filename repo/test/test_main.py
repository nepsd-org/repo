import pytest

from ..src.main import add

def test_add_1():
    assert add(3, 4) == 7

def test_add_2():
    assert add(0.3, -1) == -0.7

def test_add_3():
    with pytest.raises(TypeError) as e_info:
        assert 5 + '0' != 5
