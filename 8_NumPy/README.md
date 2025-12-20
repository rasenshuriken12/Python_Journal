# NumPy

❇️ NumPy (Numerical Python) is the fundamental package for **scientific computing** in Python. It provides support for:

- **Multidimensional arrays** (faster than Python lists)
- **Mathematical functions** (linear algebra, statistics, etc.)
- **Tools for integrating C/C++ code**
- **Random number generation**

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

arr_range = np.arange(0, 1, 2) # start, stop, step
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
