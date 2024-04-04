import numpy as np

# to create a numpy array

l = [1,2,5,9,8]
npf1 = np.array(l)
print(npf1)

a = np.array([1,2,5,9,8])
print(a)

# Mathematical operation in Numpy array
print(a+10)
print(a*10)
print(a/10)

# Shape of Array
a1 = np.array([1,2,5,9,8])
print(a1)
print(a1.shape)
print(a1.dtype)


a2 = np.array([[1,2,3],[4,5,6]])
print(a2.shape)

a3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a3.shape)


# Zeros
c = np.zeros((2,2))
print(c)

# Ones
k = np.ones((2,2))
print(k)

# Reshape
r = np.array([[1,2,3],[4,5,6]])
print(r.shape)
print(r.reshape(3,2))


# Generate Random Number using Numpy

numpy_array = np.random.normal(5,0.5,10)
print(numpy_array)

# Slicing
print(numpy_array[0])
print(numpy_array[1])


# Build in Functions
print("Minimum :",numpy_array.min())
print("Maximum :",numpy_array.max())
print("Mean :",numpy_array.mean())
print("Standard Deviation :",numpy_array.std())
print("Median :",np.median(numpy_array))







