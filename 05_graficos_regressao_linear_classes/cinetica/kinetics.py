"""
Simple script to plot data of an example of kinetics data from chemical
reaction.
"""
import numpy as np
import matplotlib.pyplot as plt

time_data, conc_data = np.loadtxt('dados.csv', skiprows=1, unpack=True,
                                  delimiter=',')
fig = plt.figure(figsize=(9, 3))

# subplot: concentration vs time
ax1 = fig.add_subplot(1, 3, 1)
ax1.plot(time_data, conc_data, 'bo')
ax1.set_xlabel('Time (min)')
ax1.set_ylabel('Conc. (mol/l)')
ax1.set_title('Conc vs. Time')

# subplot: log(Conc) vs Time
ax2 = fig.add_subplot(1, 3, 2)
ax2.semilogy(time_data, conc_data, 'ro')
ax2.set_xlabel('Time (min)')
ax2.set_ylabel('log (Conc)')
ax2.set_title('log (Conc) vs. Time')

# subplot: 1 / Conc vs Time
ax3 = fig.add_subplot(1, 3, 3)
ax3.plot(time_data, (1 / conc_data), 'ro')
ax3.set_xlabel('Time (min)')
ax3.set_ylabel('1/Conc')
ax3.set_title('1/Conc vs. Time')

fig.tight_layout()
fig.show()
