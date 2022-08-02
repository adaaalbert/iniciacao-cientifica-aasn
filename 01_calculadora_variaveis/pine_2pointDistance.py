# Calculates the distance between two 3D Cartesian
# coordinates
# formula -> delta_r = square_root((x2-x1)² + (y2-y1)² + (z2-z1)²)
import numpy as np

x1, y1, z1 = 23.7, -9.2, -7.8
x2, y2, z2 = -3.5, 4.8, 8.1

delta_r = np.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
