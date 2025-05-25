import pytest
from src.fib import fibonacci

@pytest.mark.parametrize("n, expected", [
    (7, 13),
    (9, 34),
    (5, 5),
    (2, 1)
])
def test_positive(n: int, expected: int):
    assert fibonacci(n) == expected


def test_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_edge_0():
    assert fibonacci(0) == 0


def test_edge_1():
    assert fibonacci(1) == 1


def test_edge_a_lot():
    result = fibonacci(100000)
    with pytest.raises(ValueError, match=r"Exceeds the limit \(4300 digits\).*"):
        print(result)