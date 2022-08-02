"""
Write a program to calculate the perimeter p of an n-gon inscribed inside a
sphere of diameter 1.

Find p for n = 3, 4, 5, 100, 10,000 and 1,000,000.
"""
from itertools import islice
from math import sin, pi


def perimeter(n_sides, radius):

    for value in n_sides:
        yield 2 * value * radius * sin(pi / value)


if __name__ == '__main__':
    values = [100] * 100_000
    g = perimeter(values, radius=0.5)
    print(g)
    print(next(g))
    print(tuple(islice(g, 10)))
    print(len(tuple(g)))