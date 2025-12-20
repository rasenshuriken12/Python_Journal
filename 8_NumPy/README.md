# NumPy

❇️ NumPy (Numerical Python) is the fundamental package for **scientific computing** in Python. It provides support for:

- **Multidimensional arrays** (faster than Python lists)
- **Mathematical functions** (linear algebra, statistics, etc.)
- **Tools for integrating C/C++ code**
- **Random number generation**

❇️ NumPy arrays are similar to Python lists in some ways but are distinct and optimized for numerical and scientific computing.

▶️ Creating a Numpy Array 

🔸 Creating a 1D array

*Code:*
```python
import numpy as np

x = np.array([1, 2])
print(x)
```

*Output:*
```html
[1 2]
```

🔸 Creating a 2D array

*Code:*
```python
import numpy as np

y = np.array([[1, 2], [3, 4]])
print(y)
```

*Output:*
```html
[[1 2]
 [3 4]]
```

🔸 Creating a 3D array

*Code:*
```python
import numpy as np

z = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(z)
```

*Output:*
```html
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
```

🔸 Creating an array of zeros(Zero / Null Matrix)

*Code:*
```python
import numpy as np

arr_0 = np.zeros((3, 3))  # row, column
print(arr_0)

```

*Output:*
```html
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
```

🔸 Creating an array of ones

*Code:*
```python
import numpy as np

arr_1 = np.ones((2, 2))  # row, column
print(arr_1)
```

*Output:*
```html
[[1. 1.]
 [1. 1.]]
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
> NOTE : name of the function is `arange()`, its not `arrange`.
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


▶️ Numpy Array Indexing

🔸 Using 1d Array

*Code:*
```python
import numpy as np

arr1d = np.array([10, 20, 30, 40, 50])
print("Single element access:", arr1d[3])  
print("Negative indexing:", arr1d[-4])    # Negative indexing
```

*Output:*
```html
Single element access: 40
Negative indexing: 20
```

🔸 Using 2d Array

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


▶️ Numpy Array Slicing 

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
arr[1:3] = 5
print(arr)
```

*Output:*
```python
[ 1 5 5 4 5]
```


▶️ Reshaping Numpy array

🔸 Conversion of 1-D array to 2-D array

*Code:*
```python
import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
print(f"Array : {array}")

# converting 1-D array to 2-D array
reshaped = array.reshape((4, 4))  # rows, columns

print("Reshaped 2D Array : ")
print(reshaped)
```

*Output:*
```html
Array : [ 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16]
Reshaped 2D Array :
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
```

🔸 Conversion of 1-D array to 3-D array
*Code:*
```python
import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
print(f"Array : {array}")

reshaped = array.reshape((2, 2, 4))  # Ensure 2*2*4 = 16

print("Reshaped 3D Array : ")
print(reshaped)
```

*Output:*
```html
Array : [ 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16]
Reshaped 3D Array :
[[[ 1  2  3  4]
  [ 5  6  7  8]]

 [[ 9 10 11 12]
  [13 14 15 16]]]
```

🔸 Conversion of 2-D array to 1-D array
*Code:*
```python
import numpy as np

array = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print("2D Array : ")
print(array)

reshaped = array.reshape((9))

print("Reshaped 1D Array : ")
print(reshaped)
```

*Output:*
```html
2D Array : 
[[1 2 3]
 [4 5 6]
 [7 8 9]]
Reshaped 1D Array : 
[[1 2 3 4 5 6 7 8 9]]
```


▶️ Resizing Numpy array

*Code:*
```python
import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(f"Array : {array}")

array.resize(2, 4)  # Permanently reshaped
print(f"Resized Array : {array}")
```

*Output:*
```html
Array : [ 1 2 3 4 5 6 7 8]
Resized 2D Array :
[[ 1  2  3  4]
 [ 5  6  7  8]]
```

*Code:*
```python
import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(f"Array : {array}")

array.resize(3, 2, 3)  # Required values 18, existing values 8
print(f"Resized 3D Array : {array}")
```

*Output:*
```html
Array : [ 1 2 3 4 5 6 7 8]
Resized 3D Array :
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  0]
  [ 0  0  0]]

 [[ 0  0  0]
  [ 0  0  0]]]
```

