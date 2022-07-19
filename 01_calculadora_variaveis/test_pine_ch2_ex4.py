from cmath import sqrt
from pine_ch2_ex4 import roots

# TODO nomes das funções em inglês


def test_duas_raizes_1_1_0():
    assert roots(1, 1, 0) == (0, -1)


def test_duas_raizes_1_2_1():
    assert roots(1, 2, 1) == (-1, -1)


def test_raiz_complexa():
    expected = complex(-0.5, -sqrt(3)/2), complex(-0.5, sqrt(3)/2)
    x1, x2 = roots(1, 1, 1)
    assert (x1 in expected) and (x2 in expected)


def test_raiz_coeficiente_a_diferente_de_1():
    assert roots(2, -16, 50) == (4+3j, 4-3j)
