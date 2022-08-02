from cmath import sqrt
from pine_ch2_ex4 import roots


def test_two_roots_1_1_0():
    assert roots(1, 1, 0) == (0, -1)


def test_two_roots_1_2_1():
    assert roots(1, 2, 1) == (-1, -1)


def test_complex_root():
    expected = complex(-0.5, -sqrt(3)/2), complex(-0.5, sqrt(3)/2)
    x1, x2 = roots(1, 1, 1)
    assert (x1 in expected) and (x2 in expected)


def test_root_coeff_x2_not_equal_1():
    assert roots(2, -16, 50) == (4+3j, 4-3j)
