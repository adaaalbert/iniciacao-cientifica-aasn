"""
Write a program to calculate the perimeter p of an n-gon inscribed inside a
sphere of diameter 1.

Find p for n = 3, 4, 5, 100, 10,000 and 1,000,000.
"""
from math import sin, pi


def perimeter(n_sides, radius):
    results = []
    for value in n_sides:
        results.append(2 * value * radius * sin(pi / value))
    return results


if __name__ == '__main__':
    values = (3, 4, 5, 100, 10_000, 1_000_000)
    print(perimeter(values, radius=0.5))
