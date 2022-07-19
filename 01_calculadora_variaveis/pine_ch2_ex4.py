# A quadratic equation with the general form:
# ax² + bx + c = 0
# has two solutions given by the quadratic formula
# x = ((-b +- (b² - 4ac)^1/2)/2a)
from cmath import sqrt


def roots(a, b, c):
    """Calculate the 2 solutions"""
    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2


if __name__ == '__main__':
    # Input the constant values
    a = complex(input("Digit the 'a' value."))
    b = complex(input("Digit the 'b' value."))
    c = complex(input("Digit the 'c' value."))

    print(roots(a, b, c))
