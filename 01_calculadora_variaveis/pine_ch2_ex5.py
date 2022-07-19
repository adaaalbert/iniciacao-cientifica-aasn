# Write a program to calculate the perimeter p of an n-gon inscribed
# inside a sphere of diameter 1.
# Find p for n = 3, 4, 5, 100, 10,000 and 1,000,000.

from math import sin, pi

values = (3, 4, 5, 100, 10_000, 1_000_000)

radius = 0.5

# Calculate perimeters to given 'n' values
for value in values:
    print(2 * value * radius * sin(pi / value))
