from math_series.series import __version__
from math_series.series import fibonacci , lucas


def test_version():
    assert __version__ == "0.1.0"


def test_fibonacci():
    input = [0, 1, 2, 3, 4, 5, 6, 7, -2]
    expected = [0, 1, 1, 2, 3, 5, 8, 13, "wrong input"]
    actual = [fibonacci(i) for i in input]
    assert expected == actual

def test_lucas():
    input = [0, 1, 2, 3, 4, 5, 6, 7, -2]
    expected = [2, 1, 3, 4, 7, 11, 18, 29, "wrong input"]
    actual = [lucas(i) for i in input]
    assert expected == actual