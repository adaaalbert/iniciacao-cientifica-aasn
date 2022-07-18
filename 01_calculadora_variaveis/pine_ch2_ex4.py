# A quadratic equation with the general form:
# ax² + bx + c = 0
# has two solutions given by the quadratic formula
# x = ((-b +- (b² - 4ac)^1/2)/2a)
import numpy as np

# Input the constant values
a = float(input("Digit the 'a' value."))
b = float(input("Digit the 'b' value."))
c = float(input("Digit the 'c' value."))

# Fixing to work with complex numbers
a = a + 0j
b = b + 0j
c = c + 0j

# Calculate the 2 solutions
x1 = (-b + (np.sqrt(b**2 - 4*a*c))) / 2*a
x2 = (-b - (np.sqrt(b**2 - 4*a*c))) / 2*a

print(x1)
print(x2)
