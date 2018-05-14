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

# Can create an array with np.array(x), where x is a python list or tuple.
b = np.array([6, 7, 8])
print(b)
print(type(b))

# Can specify type:
c = np.array([[1,2] ,[3,4]], dtype=complex)
print(c)

# Can do an all zeros array by specifying shape:
d = np.zeros( (3,4))
print(d)

# Same thing with ones:
e = np.ones( [4,3] )
print(e)

# Two ways to automatically create a range of elements:
# 1: arange(first, last, spacing). Note not inclusive.
f = np.arange(10, 30, 5)
print(f)
# 2: linspace(first, last, num_elements). Inclusive.
g = np.linspace(0, 5, 4)
print(g)

# ALL arithmetic operators apply elementwise:
print(e + e)
print(f < 20)
print((e + e) * e)

# Need to use the dot function to dot two matrices:
h = np.arange(6).reshape(2,3)
i = np.arange(6).reshape(3,2)
print(h)
print(i)
print(i.dot(h))
print(np.dot(i, h))

# Sum all elements of array:
print(h.sum())
print(h.sum(axis=0)) # 0 axis = columns. So sum all columns.
print(h.sum(axis=1)) # 1 axis = rows. So sum all rows.

# Find min/max:
print(h.max())
print(h.min())

# Universal functions operate elementwise:
j = np.arange(5)
print(j)
print(np.exp(j))
print(np.cos(j))

# Indexing is as in MATLAB
k = np.arange(5)**2

