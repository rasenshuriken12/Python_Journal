# 🚧 NumPy - Numerical Computing

import numpy as np

# Creating arrays
print("=== Creating Arrays ===")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.zeros((3, 4))
arr4 = np.ones((2, 3))
arr5 = np.full((3, 3), 7)
arr6 = np.eye(4)  # Identity matrix
arr7 = np.random.rand(3, 3)  # Random numbers
arr8 = np.arange(0, 10, 2)  # Step range
arr9 = np.linspace(0, 10, 5)  # Linear space

print(f"1D Array: {arr1}")
print(f"2D Array:\n{arr2}")
print(f"Zeros:\n{arr3}")
print(f"Identity:\n{arr6}")
print(f"Random:\n{arr7}")
print(f"Range: {arr8}")
print(f"Linspace: {arr9}")

# Array attributes
print(f"\n=== Array Attributes ===")
print(f"Shape: {arr2.shape}")
print(f"Dimensions: {arr2.ndim}")
print(f"Size: {arr2.size}")
print(f"Data type: {arr2.dtype}")
print(f"Item size: {arr2.itemsize} bytes")

# Reshaping
print(f"\n=== Reshaping ===")
arr = np.arange(1, 13)
print(f"Original: {arr}")
reshaped = arr.reshape(3, 4)
print(f"Reshaped (3x4):\n{reshaped}")
flattened = reshaped.flatten()
print(f"Flattened: {flattened}")

# Indexing and slicing
print(f"\n=== Indexing and Slicing ===")
matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(f"Matrix:\n{matrix}")
print(f"Element [1,1]: {matrix[1,1]}")
print(f"Row 0: {matrix[0]}")
print(f"Column 1: {matrix[:,1]}")
print(f"Slice [0:2, 1:3]:\n{matrix[0:2, 1:3]}")
print(f"Boolean indexing: {matrix[matrix > 50]}")

# Mathematical operations
print(f"\n=== Mathematical Operations ===")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f"a + b: {a + b}")
print(f"a * b: {a * b}")
print(f"a ** 2: {a ** 2}")
print(f"np.sqrt(a): {np.sqrt(a)}")
print(f"np.sin(a): {np.sin(a)}")
print(f"np.exp(a): {np.exp(a)}")
print(f"np.log(a): {np.log(a)}")

# Linear algebra
print(f"\n=== Linear Algebra ===")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"Matrix A:\n{A}")
print(f"Matrix B:\n{B}")
print(f"Dot product:\n{np.dot(A, B)}")
print(f"Transpose of A:\n{A.T}")
print(f"Determinant of A: {np.linalg.det(A)}")
print(f"Inverse of A:\n{np.linalg.inv(A)}")
print(f"Eigenvalues of A: {np.linalg.eigvals(A)}")

# Aggregations
print(f"\n=== Aggregations ===")
data = np.random.randn(5, 5)  # 5x5 random normal distribution
print(f"Data:\n{data}")
print(f"Sum: {np.sum(data)}")
print(f"Mean: {np.mean(data)}")
print(f"Median: {np.median(data)}")
print(f"Standard deviation: {np.std(data)}")
print(f"Variance: {np.var(data)}")
print(f"Min: {np.min(data)}")
print(f"Max: {np.max(data)}")
print(f"Sum by axis=0 (columns): {np.sum(data, axis=0)}")
print(f"Sum by axis=1 (rows): {np.sum(data, axis=1)}")

# Broadcasting
print(f"\n=== Broadcasting ===")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Original:\n{arr}")
print(f"Add 10 to all:\n{arr + 10}")
print(f"Multiply by 2:\n{arr * 2}")
print(f"Add row [1,1,1]:\n{arr + [1, 1, 1]}")

# Stacking
print(f"\n=== Stacking ===")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"vstack:\n{np.vstack([a, b])}")
print(f"hstack: {np.hstack([a, b])}")

# Saving and loading
print(f"\n=== Saving/Loading ===")
np.save('array.npy', arr)
loaded = np.load('array.npy')
print(f"Loaded array:\n{loaded}")

# Advanced indexing
print(f"\n=== Advanced Indexing ===")
indices = np.array([[0, 1], [1, 2]])
print(f"Fancy indexing:\n{arr[indices]}")
