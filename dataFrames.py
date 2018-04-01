import pandas as pd
import numpy as np
from numpy.random import randn

# Create a DataFrame
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)
print(df['W']) # print single column
print(df[['W', 'Z']]) # print multiple columns

ARITHMETIC between columns
df['New'] = df['W'] + df['Z']
print(df)

# drop a column
print(df.drop('Y', axis=1)) # hide 'Y' column from this call without remove
df.drop('Y', axis=1, inplace = True) #actually delete the column
print(df)

#drop a row
df.drop('E', inplace = True)
print(df)
