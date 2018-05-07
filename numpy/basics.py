import numpy as np

a = np.arange(15).reshape(3,5)
print(a)

# Print a's shape in form (rows, columns):
print(a.shape)

# Print a's dimension. In this case, a is a 2D matrix. Output 2.
print(a.ndim)

# Print a's elements' type. In this case, int64
print(a.dtype.name)

# Print the number of bytes that each elememt occupies
print(a.itemsize)

# Print the total number of elements in a
print(a.size)

# Print a's type. In this case, it is numpy.ndarray
print(type(a))

b = np.array([6, 7, 8])
print(b)
print(type(b))
