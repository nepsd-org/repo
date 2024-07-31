import pytest

from ..src.main import add, multiply

def test_add_ND_T1():
    assert add(3, 4) == 7

def test_add_ND_T2():
    assert add(0.3, -1) == -0.7

def test_add_ND_T3():
    with pytest.raises(TypeError) as _e_info:
        assert 5 + '0' != 5

def test_multiply_ND_T5():
    assert multiply(3, 4) == 12
