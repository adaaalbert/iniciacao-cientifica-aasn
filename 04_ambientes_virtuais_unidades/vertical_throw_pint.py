"""
This script defines a function height and returns a calculated height given the
time and initial speed of an object based on vertical throw equation.
"""
import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

GRAVITY = Q_(9.8, 'm/s**2')


@ureg.wraps('m', ('m', 'm/s', 's'))
def height(initial_height, initial_speed, time):
    """
    Calculates the current height of an object after vertical throw, given the
    intial height & speed and a given time.

    Parameters
    ----------
    initial_height
    initial_speed
    time

    Returns
    -------
    returns the height of the object

    """
    return initial_height + initial_speed * time - (1 / 2) * GRAVITY.magnitude * time ** 2


if __name__ == '__main__':
    print(height('5 m', '1 m/s', '0 s'))
    print(height('500 cm', '1 m/s', '0 s'))
    print(height('50 ft', '10 in/s', '1000 ms'))
