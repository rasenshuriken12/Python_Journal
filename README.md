# Python Journal

| ![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5?style=for-the-badge&logo=LinkedIn&logoColor=white) | [![My_Portfolio](https://img.shields.io/badge/My_Portfolio-indigo?style=for-the-badge&logo=firefox&logoColor=white)](https://yourwebsite.com/) | [![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/rasenshuriken12/) | 
|---|---|---|

---

# Python 

❇️ Python is a high-level, interpreted, general-purpose programming language.

❇️ Key Features:
- Easy to learn( No Curly braces, uses Indentation )
- Interpreted Language ( Code executes line-by-line at runtime, Slow execution).  
- Python requires fewer lines of code compared to other programming languages.

# 1) [Python Basics](https://github.com/rasenshuriken12/Python_Journal/tree/869cbd7b9547227a7ae2b87a8dfffc03e7faa530/1_Python%20Basics)

# 2) [Data Types](https://github.com/rasenshuriken12/Python_Journal/blob/b61e1fa3ea09c4b5ab00bbbbb1c515365e0c57fb/2_Data%20Types)

# 🚧 3) Oops Concept 

# 4) [Exception Handling](https://github.com/rasenshuriken12/Python_Journal/tree/901b752445cdbf79a72ef63d8b745c556b192906/4_Exception%20Handling)

# 5) File Handling 

# 🚧 6) [RegEx](https://github.com/rasenshuriken12/Python_Journal/tree/95e78f250d237b2e341ccd95cc5db0de8ecb2cce/6_RegEx)

# 7) Tkinter

# 🚧 8) Numpy




▶️ Numpy Array Indexing

<details>
  <summary>Click to expand 🔻</summary>
  
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

</details>

▶️ Numpy Array Slicing 

<details>
  <summary>Click to expand 🔻</summary>

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

</details>

▶️ Reshaping Numpy array

<details>
  <summary>Click to expand 🔻</summary>

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

</details>

▶️ Resizing Numpy array

<details>
  <summary>Click to expand 🔻</summary>

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

</details>

# Pandas

# Matplotlib


---


 ![status](https://img.shields.io/badge/status-upcoming-yellow)

---

| [![TOP](https://img.shields.io/badge/_🔺_-Navigate_to_TOP_↑_-blue?style=for-the-badge&labelColor=white)](#Python_Basics) | [![Resources](https://img.shields.io/badge/📚_Back_to-Resources-A52A2A?style=for-the-badge&logo=book&logoColor=white)](https://github.com/rasenshuriken12/Resources) | [![GitHub](https://img.shields.io/badge/Back_to-GitHub-000?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/rasenshuriken12/) |
|---|---|---|
