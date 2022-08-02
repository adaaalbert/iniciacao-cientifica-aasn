"""Introduction to Python Science & Eng. - Pine -
Chapter 2 - Exercise 1

An object is thrown vertically up in the air from a height initial_height above
the ground at an initial velocity initial_speed. Its subsequent height and speed
are given by the equations:

height = initial_height + initial_speed * time - (1/2) * GRAVITY * time**2
speed = initial_speed - GRAVITY * time

where GRAVITY = 9.8 m/s², the acceleration due to gravity

This script calculates the height and speed at a time after the object is
thrown.
"""

GRAVITY = 9.8               # m/s²

initial_height = 1.6        # meter
initial_speed = 14.2        # m/s, meters/second
time = 2.0                  # s

height = initial_height + initial_speed * time - (GRAVITY * time ** 2) / 2
speed = initial_speed - GRAVITY * time

print(f'After {time} s, the height is {height:.2f} m and the speed is '
      f'{speed:.2f} m/s.')
