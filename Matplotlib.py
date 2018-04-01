# import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

# FUNCTIONAL METHOD
plt.plot(x, y,'r-')
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')
# plt.show()

# Multiple plots on on the same canvas
plt.subplot(1, 2, 1) #row, column, # of plots
plt.plot(x, y, 'r-')

plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')
# plt.show()

# OOP METHOD
fig1 = plt.figure()
axes1 = fig1.add_axes([0.1, 0.1,0.8,0.8]) # list take in 4 arguments left - bottom - width - height
axes2 = fig1.add_axes([0.2,0.5,0.4,0.3]) # value range from 0 to 1
axes1.plot(x, y)
axes2.plot(y, x)
axes1.set_title('Larger PLot')
axes2.set_title('Smaller PLot')
axes1.set_xlabel('X Label')
axes2.set_ylabel('Y Label')

# subplot using OOP method
fig2, axes = plt.subplots(nrows=2, ncols=2) # two dimensional array. This creates 4 plots

# providing axes values for plot at index [0,0]
axes[0,0].plot(x, y)
axes[0,0].set_title('First plot')

# providing axes values for plot at index [1,1]
axes[1,1].plot(y, x)
axes[1,1].set_title('Second plot')

# How to use legend() to add label to many lines in the same plot
fig3 = plt.figure()
ax = fig3.add_axes([0,0,1,1])
ax.plot(x, x**2, label='X squared', color='purple')
ax.plot(x, x**3, label='X cubed', color='red')

ax.legend(loc='best')

# How to save figures
fig3.savefig('data/myfig.pdf', dpi=200)

# ADDING STYLES TO plots
fig4 = plt.figure()
ax4  = fig4.add_axes([0.1,0.1,0.8,0.8])
ax4.set_xlabel('X values')
ax4.set_ylabel('Y values')
ax4.set_title('Title')

# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax4.plot(x, y, color = 'purple', linewidth = 2, linestyle='-', marker='o',
    markersize=5, markerfacecolor='red'
    )
# plt.tight_layout() # take care of overlapping plots
plt.show()


# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# plt.show()
