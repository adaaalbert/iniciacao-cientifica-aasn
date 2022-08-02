"""
This script defines a function height and returns a calculated height given the
time and initial speed of an object based on vertical throw equation.
"""
GRAVITY = 9.8  # m/s**2


def height(initial_height, initial_speed, time):
    """Returns the height of a vertical throw after given time and speed.-"""

    return initial_height + initial_speed * time - (1/2) * GRAVITY * time**2
