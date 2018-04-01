import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')
sns.set(style='whitegrid') # this is to show horizontal lines in plots

# BARPLOT
# barplot is a general plot that allows you to aggregate the categorical data
# based off some function, by default the mean:
sns.barplot(x='sex', y='tip', data=tips, estimator=np.std)

# COUNTPLOT
# This is essentially the same as barplot except the estimator is explicitly
# counting the number of occurrences. Which is why we only pass the x value:
sns.countplot(x='sex', data=tips).set_title('Count PLot Example')

# BOXPLOT
#  The box plot (a.k.a. box and whisker diagram) is a standardized way of
# displaying the distribution of data based on the five number summary:
# minimum, first quartile, median, third quartile, and maximum.
sns.boxplot(x='day', y='total_bill', hue='smoker', data=tips, orient='v')

# VIOLINPLOT
# Violin plots have many of the same summary statistics as box plots:
# a. the white dot represents the median
# b. the thick gray bar in the center represents the interquartile range
# c. the thin gray line represents the 95% confidence interval
# On each side of the gray line is a kernel density estimation to show the
# distribution shape of the data. Wider sections of the violin plot represent
# a higher probability that members of the population will take on the given value;
# the skinnier sections represent a lower probability.
sns.violinplot(x='day', y='total_bill', data=tips, palette='rainbow')

# STRIPPLOT
# The stripplot will draw a scatterplot where one variable is categorical.
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', palette='Set1')

# SWARMPLOT
# The swarmplot is similar to stripplot(), but the points are adjusted
# (only along the categorical axis) so that they don’t overlap.
sns.swarmplot(x="day", y="total_bill", data=tips)

# FACTOR PLot
# factorplot is the most general form of a categorical plot.
# It can take in a kind parameter to adjust the plot type:
# kind parameter includes: bar, violin, box, swarm, strip,. etc
sns.factorplot(x='sex',y='total_bill',data=tips,kind='strip')
plt.show()
