"""Simple script for vertical throw calculation

Example: A ball is thrown vertically up in the air from an initial height above
the ground at an initial speed. Its subsequent height and speed are given by the
following equations:
height = initial_height + initial_speed * time - (1/2) * GRAVITY * time**2
speed = initial_speed - GRAVITY * time
where GRAVITY = 9.8 m/s², the acceleration due to gravity

This script calculates the height and speed at a time after the ball is thrown.
"""

from vertical_throw import height

initial_height = float(input("Enter the initial height / m: "))
initial_speed = float(input("Enter the initial speed / m/s: "))
time = float(input("Enter the time / s: "))

new_height = height(initial_height, initial_speed, time)

print(f"Height: {new_height:.2f} m")
