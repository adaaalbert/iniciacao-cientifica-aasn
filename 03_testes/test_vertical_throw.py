from vertical_throw import height
from pytest import approx


def test_time_0_initial_speed_0():
    assert height(5, 0, 0) == 5


def test_time_0_initial_speed_1():
    assert height(5, 1, 0) == 5


def test_initial_speed_0_initial_height_0_time_1():
    assert height(0, 0, 1) == -4.9


def test_initial_speed_0_initial_height_0_time_2():
    assert height(0, 0, 2) == -19.6


def test_initial_speed_0_initial_height_1_time_2():
    assert height(1, 0, 2) == -18.6


def test_initial_speed_1_initial_height_0_time_1():
    assert height(0, 1, 1) == approx(-3.9, rel=0, abs=0.001)
