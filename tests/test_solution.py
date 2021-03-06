import pytest
from src.solution import *


@pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),
        (2, 2, 4),
        (1, 5, 6),
])
def test_add(a, b, expected):
    actual = add(a, b)
    assert actual == expected
