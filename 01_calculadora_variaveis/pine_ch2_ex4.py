"""
A quadratic equation with the general form:
ax² + bx + c = 0
has two solutions given by the quadratic formula
x = ((-b +- (b² - 4ac)^1/2)/2a)
"""
from cmath import sqrt


def roots(coef_x2, coef_x, const):
    """Calculate the 2 solutions"""
    root1 = (-coef_x + sqrt(coef_x ** 2 - 4 * coef_x2 * const)) / (2 * coef_x2)
    root2 = (-coef_x - sqrt(coef_x ** 2 - 4 * coef_x2 * const)) / (2 * coef_x2)
    return root1, root2


if __name__ == '__main__':
    # Input coefficients and constant values
    a = complex(input("Digit the 'a' value."))
    b = complex(input("Digit the 'b' value."))
    c = complex(input("Digit the 'c' value."))
    print(roots(a, b, c))
