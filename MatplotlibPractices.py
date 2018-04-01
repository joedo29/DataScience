import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x*2
z = x**2

# Exercise 1: Create a single plot
fig1 = plt.figure()
ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('Outer Plot')
ax1.plot(x,y)

# Exercise 2: plot inside a plot
ax2 = fig1.add_axes([0.25, 0.55, 0.2, 0.2]) # left - bottom - width - height
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Inner Plot')
ax2.plot(x, z, color='red')

# Exercise 3: create subplot 2 row by 2 columns
fig3, ax3 = plt.subplots(nrows=2, ncols=2, figsize=(12, 6))
ax3[0, 0].plot(x, y, linestyle='--', color='blue', linewidth=5)
ax3[1, 1].plot(x, z, color='red', linewidth=10)


# plt.tight_layout()
plt.show()
