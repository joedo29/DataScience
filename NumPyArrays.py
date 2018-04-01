import numpy as np

# Create a one dimension array and cast it to numpy array
my_list = [1, 2, 3]
numPyArray = np.array(my_list)
print(numPyArray)

# Create a multy dimension array and cast it to numpy array
multyArray = [[1,2,3], [4,5,6], [7,8,9]]
numPyMultyArray = np.array(multyArray)
print(numPyMultyArray)

# np.arange automatically generates multy dimensional array using numpy
x = np.arange(0, 10, 2) # a list of evenly numbers from 0 to 10
print(x)

# zeroes and ones module in numpy
zero = np.zeros((4,5)) # 4 rows and 5 columns
one  = np.ones((3,5))
print(zero)
print(one)

# np.linspace returns evenly spaced numbers over a specified interval
lin = np.linspace(0, 10, 10)
print(lin)

# np.eye creates an indentity matrix
indentity = np.eye(3) # a 3 by 3 indentity matrix
print(indentity)

# np.random.rand
rand = np.random.rand(5) # returns 5 random numbers
randint = np.random.randint(1, 100, 10) # returns a random number from 1 to 99
print(rand)
print(randint)

# perform ARITHMETIC on array
arr = np.arange(1, 11)
print(arr)
print(arr + 10)
print(arr + arr)
print(arr * arr)
print(np.sin(arr))
print(np.log(arr))
