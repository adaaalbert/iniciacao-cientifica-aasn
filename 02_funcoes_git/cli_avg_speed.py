"""
Simple script for average speed calculation
"""

from average_speed import avg_speed

distance = float(input("Enter the distance / m: "))
time = float(input("Enter the time /s: "))

avg_speed = avg_speed(distance, time)

print(f'The average speed is {avg_speed:.2f} m/s.')
