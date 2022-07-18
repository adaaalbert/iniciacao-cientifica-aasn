"""Introduction to Python Science & Eng. - Pine
Chapter 2 - Exercise 1
A ball is thrown vertically up in the air from a height initial_height above
the ground at an initial velocity initial_speed. Its subsequent height height
and velocity speed are given by the equations
height = initial_height + v0t - 1/2gt²
speed = initial_speed - gt
where GRAVITY = 9.8 m/s², the acceleration due to gravity
This script calculates the height height and velocity speed at a time time
after the ball is thrown.
"""

GRAVITY = 9.8               # m/s²

initial_height = 1.6        # meter
initial_speed = 14.2        # m/s, meters/second
time = 2.0                  # s

height = initial_height + initial_speed * time - (GRAVITY * time ** 2) / 2
speed = initial_speed - GRAVITY * time

print(f'Height: {height:.3f} m')
print(f'Speed: {speed:.3f} m/s')
