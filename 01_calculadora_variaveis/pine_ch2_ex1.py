# Introduction to Python Science & Eng. - Pine
# Chapter 2 - Exercise 1
# A ball is thrown vertically up in the air from a height h0 above
# the ground at an initial velocity v0 . Its subsequent height h and
# velocity v are given by the equations
# h = h0 + v0t - 1/2gt²
# v = v0 - gt
# where g = 9.8 m/s², the acceleration due to gravity
# This script calculates the height h and velocity v at a time t
# after the ball is thrown.
h0 = 1.6        # meter
v0 = 14.2       # m/s, meters/second
t = 2.0         # time in s
g = 9.8         # m/s²

h = h0 + v0*t - (g*t**2)/2
v = v0 - g*t

print(h)
print(v)
