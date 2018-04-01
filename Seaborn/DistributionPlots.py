import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips') # load dataset from online repository
# for all available dataset, go here: https://github.com/mwaskom/seaborn-data

# how to load and use your own data and deal with missing data
df = pd.DataFrame(pd.read_csv('SmallSalaries.csv'))
df['BasePay'].fillna(value=df['BasePay'].mean()) # fill NaN value with mean()
sns.distplot(df['BasePay']) # draw a distplot on your own dataset

tips = sns.load_dataset('tips')

# DISTPLOT
# The distplot shows the distribution of a univariate set of observations.
sns.distplot(tips['total_bill'])
# KDE: Kernel Density Estimation
# to remove KDE line, use sns.distplot(tips['total_bill'], kde=False)

# JOINTPLOT
# jointplot() allows you to basically match up two distplots for bivariate data
# With your choice of what kind parameter to compare with:
# “scatter”     “reg”       “resid”     “kde”       “hex”
sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg') # or kind='scatter',.etc

# PAIRPLOT
# pairplot will plot pairwise relationships across an entire dataframe (for the numerical columns)
# and supports a color hue argument (for categorical columns)
sns.pairplot(tips, hue='sex', palette='coolwarm')

# RUGPLOT
# draw a dash mark for every point on a univariate distribution
# They are the building block of a KDE plot
sns.rugplot(tips['total_bill'])

plt.show()
