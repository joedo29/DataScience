import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')

# BARPLOT
# barplot is a general plot that allows you to aggregate the categorical data
# based off some function, by default the mean:
sns.barplot(x='sex', y='total_bill', data=tips)




plt.show()
