# Write a program to calculate the perimeter p of an n-gon inscribed
# inside a sphere of diameter 1.
# Find p for n = 3, 4, 5, 100, 10,000 and 1,000,000.
import numpy as np

n1 = 3
n2 = 4
n3 = 5
n4 = 100
n5 = 10.000
n6 = 1000000
r = 0.5

# Calculate perimeters to given 'n' values
p1 = 2*n1*r*np.sin(np.pi/n1)
p2 = 2*n2*r*np.sin(np.pi/n2)
p3 = 2*n3*r*np.sin(np.pi/n3)
p4 = 2*n4*r*np.sin(np.pi/n4)
p5 = 2*n5*r*np.sin(np.pi/n5)
p6 = 2*n6*r*np.sin(np.pi/n6)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
