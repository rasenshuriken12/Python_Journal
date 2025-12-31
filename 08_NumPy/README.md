# NumPy

❇️ NumPy (Numerical Python) is the fundamental package for **scientific computing** in Python. It provides support for:

- **Multidimensional arrays** (faster than Python lists)
- **Mathematical functions** (linear algebra, statistics, etc.)
- **Tools for integrating C/C++ code**
- **Random number generation**

❇️ NumPy arrays are similar to Python lists in some ways but uses Less Memory and is 50x Faster than Python lists for numerical operations and scientific computing.

🆚 Python Lists vs NumPy Arrays

| Feature	| Python List	| NumPy Array
|---|---|---|
| Type	| Built-in Python data structure	| Object from NumPy library |
| Homogeneity |	Can store mixed data types |	Stores elements of the single data type |
| Performance	| Slower for numerical computations	| Much faster for numerical operations |
| Preferred | Shorter sequence of data items | Longer sequence of data items |
| Memory Usage	| Uses more memory (stores Python objects)	| Memory efficient (stores raw data) |
| Creation | list() or [ ] | np.array() or specialized functions |
| Element Access | Slower (object references) | Faster (direct memory access) |
| Size Flexibility | Dynamic (easy to append/remove) | Fixed size (costly to resize) |
| Broadcasting	| Not supported	| Fully Supported |
| Multi-dimensional | Nested lists (inefficient) | Native support (efficient) |
| Indexing & Slicing	| Basic	| Advanced slicing & masking |
| Use in Data Science /	ML | Rarely used	| Industry standard |
| Mathematical Operations | Requires loops to handle arithmetic items	| Directly handles arithmetic items by Vectorized operations (no loops) |
| Example Operation |	[1,2,3] + [4,5,6] → concatenation	| array([1,2,3]) + array([4,5,6]) → element-wise addition |

<br>

### ▶️ Creating a Numpy Array 

🔸 Creating a 1D array (Vector)

*Code:*
```python
# Import the NumPy library to use its functions and features.
import numpy as np    # By using the alias np, you can reference Numpy functions and classes more conveniently in your code.

# Create a NumPy array containing the values 1, 2 
x = np.array([1, 2])
print(x)

print("Shape:", x.shape)   # shape returns tuple with 1 element (col,). (2,) is a TUPLE! & (2) is just an integer 2
print(x.ndim, "D Array with ", x.shape[0], "elements")   # Dimension

print("Array type: ", type(x))  
print("Shape returns: ", type(x.shape))
```

*Output:* 
```html
 [1 2]
Shape: (2,)
1D Array with 2 elements
Array type: <class 'numpy.ndarray'>
Shape returns: <class 'tuple'>
```

🔸 Creating a 2D array (Matrix)

*Code:*
```python
import numpy as np

y = np.array([[1, 2, 3], [4, 5, 6]])
print(y)

print("Shape:", y.shape)   # shape returns tuple with 2 elements (row, col).
print(y.ndim, "D Array with ", y.shape[0], "rows &", y.shape[1], "columns")   # Dimension
print(f"Total elements: {y.size}") 
```

*Output:*
```html
 [[1 2 3]
 [4 5 6]]
Shape: (2, 3)
2D Array with 2 rows & 3 columns
Total elements: 6
```

🔸 Creating a 3D array (Tensors)

*Code:*
```python
import numpy as np

z = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 6, 9]]])
print(z)

print("Shape:", z.shape)    # shape returns tuple with 3 elements (depth, row, col).
print(z.ndim, "D Array with ", z.shape[0], "planes", z.shape[1], "rows and", z.shape[2], "columns")   # Dimension
print(f"Total elements: {z.size}") 
```

*Output:*
```html
3D Array
 [[[1 2 3]
   [4 5 6]]

  [[7 8 9]
   [3 6 9]]]
Shape: (2, 2, 3)
3 D Array with  2 planes 2 rows and 3 columns
Total elements: 12
```

*Analogy:*

3D Array = A BOOK
- Depth = Page number (0, 1, 2, ...)
- Row = Line on the page
- Column = Character position in line

Example: Book with 100 pages, 50 lines per page, 80 characters per line

Shape: (100, 50, 80)

<br>

🔸 Creating an array of zeros(Zero / Null Matrix)

*Code:*
```python
import numpy as np

arr_0 = np.zeros((2, 2))  # 2 rows, 2 columns
print(arr_0)

```

*Output:*
```html
[[0. 0.]
 [0. 0.]]
```

🔸 Creating an array of ones

*Code:*
```python
import numpy as np

arr_1 = np.ones((3, 3))  # 3 rows, 3 columns
print(arr_1)
```

*Output:*
```html
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
```

🔸 Creating an array of constant 

*Code:*
```python
import numpy as np

arr_const = np.full((2, 4), 5) # row, column, constant 
print(arr_const)
```

*Output:*
```html
[[5. 5. 5. 5.]
 [5. 5. 5. 5.]]
```

🔸 Creating an Identity (square) matrix 

*Code:*
```python
import numpy as np

arr_iden = np.eye(4) # row / column 
print(arr_iden)
```

*Output:*
```html
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

🔸 Creating a Diagonal (square) matrix 

*Code:*
```python
import numpy as np

arr_diag = np.diag([2, 4, 5]) # diagonal elements 
print(arr_diag)
```

*Output:*
```html
[[2. 0. 0.]
 [0. 4. 0.]
 [0. 0. 5.]]
```

🔸 Creating an array of range

*Code:*
```python
import numpy as np

arr_range = np.arange(0, 10, 2) # start, stop, step
print(arr_range)
```

*Output:*
```html
[0 2 4 6 8]
```
> NOTE : name of the function is `arange()`(short for "array range"), its not `arrange`.
> - Starts at `start`, **increments by `step`**, and stops before reaching `stop`.
> - **Excludes the `stop` value**.


🔸 Creating an array of linspace

*Code:*
```python
import numpy as np

arr_linspace = np.linspace(0, 15, 2) # start, stop, step
print(arr_range)
```

*Output:*
```html
[0 2 4 6 8 10]
```

> - Divides the interval `[start, stop]` into `num` **equally spaced** values.
> - **Includes the `stop` value** by default.


### ▶️ Numpy Array Indexing

🔸 In 1d Array

*Code:*
```python
import numpy as np

arr1d = np.array([10, 20, 30, 40, 50])
print("Single element access:", arr1d[0])  
print("Negative indexing:", arr1d[-4])    # Negative indexing for arr1d[1]
```

*Output:*
```html
Single element access: 10
Negative indexing: 20
```

🔸 In 2d Array

*Code:*
```python
import numpy as np

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Multidimensional array access:", arr2d[2, 0])
```

*Output:*
```html
Multidimensional array access: 7
```


### ▶️ Numpy Array Slicing 

*Code:*
```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
print("Range1 : ", arr[1:2])
print("Range2 : ", arr[0:1])
print("Range3 : ", arr[1:1])
print("Column slicing : ", arr[:, 1]) # Column
print("Row slicing : ", arr[2]) # Row

print("\nInteger array indexing : ", arr[[0, 2]])

print("\nElements greater than 5 : ", arr[arr > 5])
```

*Output:*
```html
[[1 2 3]
 [4 5 6]
 [7 8 9]]
Range1 :  [[4 5 6]]
Range2 :  [[1 2 3]]
Range3 :  []
Column slicing :  [2 5 8]
Row slicing :  [7 8 9]

Integer array indexing :  [[1 2 3]
 [7 8 9]]

Elements greater than 5 :  [6 7 8 9]
```

🔸 Modifying Array Elements

*Code:*
```python
import numpy as np 

arr = np.array([1, 2, 3, 4, 5])
arr[1:3] = 5   # array indexing starts from 0
print(arr)
```

*Output:*
```python
[ 1 5 5 4 5]
```

### 🆚 Difference between Reshaping, Resizing, Stacking, Splitting

| Operation	| Purpose	| Changes Memory?	| Changes Data?	| Returns |
|--|--|--|--|--|
| Reshape	| Change shape only	| No (view) |	No |	New view of same data |
| Resize |	Change shape and size	| Yes (new array)	| Can add/remove data |	New array |
| Stack	| Combine arrays	| Yes	| No |	New combined array |
| Split |	Divide arrays	| No (views) |	No	| List of sub-arrays |

### ▶️ Reshaping Numpy array

*Code:*
```python
import numpy as np

arr = np.arange(12)  # [0, 1, 2, ..., 11]
print("Original array:", arr)
print("Original shape:", arr.shape)  # (12,)

# Reshape to 2D
reshaped_2d = arr.reshape(3, 4)
print("\nReshaped 1D Array to 2D Array")
print(reshaped_2d)
print("Reshaped shape:", reshaped_2d.shape)  # (3, 4)

# Reshape to 3D
reshaped_3d = arr.reshape(2, 3, 2)
print("\nReshaped 1D Array to 3D Array:")
print(reshaped_3d)
print("Reshaped shape:", reshaped_3d.shape)  # (2, 3, 2)
```

*Output:*
```html
Original array: [ 0  1  2  3  4  5  6  7  8  9 10 11]
Original shape: (12,)

Reshaped 1D Array to 2D Array:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
Reshaped shape: (3, 4)

Reshaped 1D Array to 3D Array:
[[[ 0  1]
  [ 2  3]
  [ 4  5]]

 [[ 6  7]
  [ 8  9]
  [10 11]]]
Reshaped shape: (2, 3, 2)
```

### ▶️ Resizing Numpy array

*Code:*
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(f"Array : {arr}")

arr.resize(2, 4)   # Permanently reshaped. Make a copy to preserve original by arr.copy()
print(f"\nResized Array : \n{arr}")

new_arr = np.resize(arr, (4, 2))   # returns new array
print(f"\nNew Resized Array : \n{new_arr}")
```

*Output:
```html
Array : [ 1 2 3 4 5 6 7 8]

Resized 2D Array :
[[ 1  2  3  4]
 [ 5  6  7  8]]

New Resized Array :
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
```

*Code:*
```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
print(f"Array : {arr}")

arr_copy = arr.copy()   # Make a copy to preserve original
arr_copy.resize(3, 3)   # Required values 9, existing values 4
print(f"\nResized 2D Array : {arr_copy}")   # fills with zeros!
```

*Output:*
```html
Array : [ 1 2 3 4 5 6 7 8]

Resized 3D Array :
[[ 1  2  3]
 [ 4  0  0]
 [ 0  0  0]]
```

*Code:*
```python
# Resize to smaller (truncates)
arr_small = np.resize(arr, (3,))
print("\nResized to (3,):", arr_small)

# Resize to larger (repeats data)
arr_large = np.resize(arr, (12,))
print("Resized to (12,):", arr_large)  
```

*Output:*
```html
Resized to (3,): [1 2 3]
Resized to (12,): [1 2 3 4 5 6 1 2 3 4 5 6]
```

### ▶️ Stacking Numpy array

🔸 Stacking 1D arrays 

*Code:*
```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("1D array as Rows: ")
print(np.stack((x, y), axis=0))   # x & y become rows

print("\n1D array as Columns: ")
print(np.stack((x, y), axis=1))   # x & y become columns. Same for axis = -1
```

*Output:*
```html
1D array as Rows: 
[[1 2 3]
 [4 5 6]]

1D array as Columns: 
[[1 4]
 [2 5]
 [3 6]]
```

🔸 Stacking 2D arrays 

*Code:*
```python
import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])

print("2D array as Planes: ")
print(np.stack((x, y), axis=0))

print("\n2D array as Rows: ")
print(np.stack((x, y), axis=1))

print("\n2D array as Columns: ")
print(np.stack((x, y), axis=2))
```

*Output:*
```html
2D array as Planes: 
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]

2D array as Rows: 
[[[ 1  2  3]
  [ 7  8  9]]

 [[ 4  5  6]
  [10 11 12]]]

2D array as Columns: 
[[[ 1  7]
  [ 2  8]
  [ 3  9]]

 [[ 4 10]
  [ 5 11]
  [ 6 12]]]
```

🔸 Stacking 3D arrays 

*Code:*
```python
import numpy as np

x = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

y = np.array([[[10, 20], [30, 40]],
              [[50, 60], [70, 80]]])

print("3D array as Batches: ")
print(np.stack((x, y), axis=0))

print("\3D array as Planes: ")
print(np.stack((x, y), axis=1))

print("\n3D array as Rows: ")
print(np.stack((x, y), axis=2))

print("\n3D array as Columns: ")
print(np.stack((x, y), axis=3))
```

*Output:*
```html
3D array as Batches:
[[[[ 1  2]
   [ 3  4]]

  [[ 5  6]
   [ 7  8]]]

 [[[10 20]
   [30 40]]

  [[50 60]
   [70 80]]]]

3D array as Planes:
[[[[ 1  2]
   [ 3  4]]

  [[10 20]
   [30 40]]]

 [[[ 5  6]
   [ 7  8]]

  [[50 60]
   [70 80]]]]

3D array as Rows:
[[[[ 1  2]
   [10 20]]

  [[ 3  4]
   [30 40]]]

 [[[ 5  6]
   [50 60]]

  [[ 7  8]
   [70 80]]]]

3D array as Columns: 
[[[[ 1 10]
   [ 2 20]]

  [[ 3 30]
   [ 4 40]]]

 [[[ 5 50]
   [ 6 60]]

  [[ 7 70]
   [ 8 80]]]]
```


### ▶️ Splitting Numpy arrays

*Code:*
```python
import numpy as np

arr = np.arange(6)       # Creates an array of values 0 - 5
res = np.split(arr, 2)   # Splits into equal-sized subarrays
print(res)
```

*Output:*
```html
[array([0, 1, 2]), array([3, 4, 5])]
```

*Code:*
```python
import numpy as np

arr = np.arange(10)   
res = np.array_split(arr, 3)   # Allows uneven splitting
print(res)
```

*Output:*
```html
[array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])
```

### ▶️ Boadcasting 



# ❇️ Real Life Example

*Code:*
```python
import numpy as np

# List of Electricity consumption values and Building areas
Elec = [4456.67, 31298, 23567.9, 12563.5]
Area = [456.67, 1298, 3567.9, 2563.5]

# Convert the lists into NumPy arrays
np_Elec = np.array(Elec)
np_Area = np.array(Area)

# Print the NumPy arrays
print("Electricity consumption:", np_Elec)
print("Building areas:", np_Area)
```

*Output:*
```html
Electricity consumption: [ 4456.67 31298.   23567.9  12563.5 ]
Building areas: [ 456.67 1298.   3567.9  2563.5 ]
```

*Code:*
```python
# Calculate the Energy Efficiency Index (EEI) by element-wise division
EEI = np_Elec / np_Area

# Print the EEI value for the 3rd building (index 2)
print("EEI for building 3:", EEI[2])
```

*Output:*
```html
EEI for building 3: 6.605538271812551
```

*Code:*
```python
# Print buildings with EEI greater than 8
print("Buildings with EEI > 8:", np_Elec[EEI > 8], "\n")

# Print buildings with EEI smaller or equal to 10
print("Buildings with EEI <= 10:", np_Elec[EEI <= 10], "\n")

# Print buildings with EEI between 5 and 15
print("Buildings with EEI between 5 and 15:", np_Elec[(EEI > 5) & (EEI < 15)], "\n")
```

*Output:*
```html
Buildings with EEI > 8: [ 4456.67 31298.  ] 

Buildings with EEI <= 10: [ 4456.67 23567.9  12563.5 ] 

Buildings with EEI between 5 and 15: [ 4456.67 23567.9 ]
```

*Code:*
```python
# Stack np_Elec and np_Area arrays as columns to create a 2-D array
array_2D = np.column_stack((np_Elec, np_Area))

# The numpy.column_stack() function stacks the 1-D arrays as columns into a 2-D array.
# The parameter(list/tuple) represents a sequence of 1-D or 2-D arrays where all of them must have the same first dimension.

# Print the resulting 2-D array   
print(array_2D)
```

*Output:*
```html
[[ 4456.67   456.67]
 [31298.    1298.  ]
 [23567.9   3567.9 ]
 [12563.5   2563.5 ]]
```
