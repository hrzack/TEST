import numpy as np
import matplotlib.pyplot as plt

# theta = np.linspace(0, np.pi*2, 1000)
# r1 = 5*np.cos(theta) + 1
# r2 = 7*np.sin(theta) - 2
# r2 = np.sin(theta)/2
# r2 = 20 / (6-4*np.cos(theta))


# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# fig, ax = plt.subplots()
# ax.plot(theta, r2)
# ax.plot(r2*np.cos(theta), r2*np.sin(theta))
# ax.set_rmax(2)
# ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
# ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
# ax.grid(True)
# plt.show()

x = np.arange(1, 100)
y = (3*x*x+2)/(2*x)
plt.plot(x, y)
plt.show()
