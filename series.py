import pandas as pd
import numpy as np

labels  = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr     = np.array(my_data)
d       = {'a': 10, 'b': 20, 'c': 30}

# Create a series
print(pd.Series(data = my_data, index = labels))

# panda with dictionay
print(pd.Series(d))

ser1 = pd.Series([1,2,3,4],['USA', 'Germany','USSR', 'Japan'])
print(ser1)
print(ser1['USA']) # 1
