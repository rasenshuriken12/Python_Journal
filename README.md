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



#  💛 Oops Concept 

<table>
<tr><td>

<br> ![1.](https://img.shields.io/badge/_1._-Classes_&_Objects-007396?style=for-the-badge&logo=python&logoColor=white) 
<br> ![2.](https://img.shields.io/badge/_2._-Polymorphism-007396?style=for-the-badge&logo=python&logoColor=white) 
<br> ![3.](https://img.shields.io/badge/_3._-Inheritance-007396?style=for-the-badge&logo=python&logoColor=white) 
<br> ![4.](https://img.shields.io/badge/_4._-Abstraction-007396?style=for-the-badge&logo=python&logoColor=white) 
<br> ![5.](https://img.shields.io/badge/_5._-Encapsulation-007396?style=for-the-badge&logo=python&logoColor=white) 

</td></tr>
</table>

# Exception Handling 

<table>
<tr><td>

<br> ⊡⁠ Exception Handling handles errors that occur during the execution of a program. 
<br> ⊡⁠ Exception Handling helps in preventing crashes due to errors.

▶️ Difference Between Errors and Exceptions

🔵 Errors 
<br> ⊡⁠ Errors are serious issues (compile time events) in your code, typically due to bad syntax or logic, that often can't be handled programmatically. They need to be fixed in the code.

Examples:
<br> 1. SyntaxError: Missed a colon or parentheses
<br> 2. IndentationError: Improper indentation
<br> 3. NameError: Referencing a variable that doesn't exist

---

💛🔵 Exceptions 
<br> ⊡⁠ Exceptions are runtime events that occur during execution and can be anticipated and handled. It can be fixed by using try, except blocks to catch and respond to exceptions gracefully.

Examples:
<br> 1. ZeroDivisionError: Dividing by zero
<br> 2.⁠ FileNotFoundError: File doesn’t exist
<br> 3. ValueError: Invalid value passed to a function

*Code:*
```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Oops! Can't divide by zero.")
```

*Output:*
```html
Oops! Can't divide by zero.
```

*Syntax:*
```python
try:
      # Code that might raise an exception

except SomeException:
      # Code to handle the exception

else:
      # Code to run if no exception occurs

finally:
      # Code to run regardless of whether an exception occurs
```

*Code:*
```python
try:
    a,b = int(input("\nEnter two numbers : ")).split()
    res = a / b
    
except ZeroDivisionError:
    print("\n You can't divide by zero!")
    
except ValueError:
    print("\n Enter a valid number!")
    
else:
    print("\n Result is : ", res)
    
finally:
    print("\nExecution complete.")
```

*Output:*
```html
Enter two numbers : 10 5
 Result is : 2
Execution complete.
```

</td></tr>
</table>

# File Handling 

# RegEx

<table>
<tr><td>

💛 ⊡⁠ Regular Expressions (RegEx) are a powerful tool for **pattern matching** and **text manipulation** that allows you to search, extract, replace, or validate strings based on specific patterns.

**(A) `re.search()`**
- Checks if a pattern exists in a string.
- Returns the **first match** (or `None`).

*Code:*
```python
text = "Python is fun"
match = re.search(r"fun", text)
if match:
    print("Found:", match.group())  
```

*Output:*
```html
Found: fun
```

*Code:*
```python
import re
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 2")
if match != None:
    print ("Match at index %s, %s" % (match.start(), match.end()))
    print ("Full match: %s" % (match.group(0)))
    print ("Month: %s" % (match.group(1)))
    print ("Day: %s" % (match.group(2)))

else:
    print ("The regex pattern does not match.")
```

*Output:*
```html
Match at index 14, 20
Full match: June 2
Month: June
Day: 2
```

*Explanation:*
- r"..." : Raw string to avoid escaping backslashes (i.e., \n stays as \n).
- ([a-zA-Z]+) : Match one or more letters (uppercase or lowercase). i.e., the month name.
- (\d+) : Match one or more digits i.e., the day number.
- The space '  ' between them : Expect a space between the two parts.
- match.start(), match.end() : Starting & Ending index of match in the string.
- match.group(0) : entire matched string.
- match.group(1) : 1st group of matched string.
- match.group(2) : 2nd group of matched string.

 **(B) `re.findall()`**
- Returns **all matches** as a list.

*Code:*
```python
text = "cats and dogs"
matches = re.findall(r"[a-z]+", text)
print(matches)  # Output: ['cats', 'and', 'dogs']
```

 **(C) `re.sub()`**
- Replaces matches with new text.

*Code:*
```python
text = "Python is awesome"
new_text = re.sub(r"awesome", "great", text)
print(new_text)  # Output: "Python is great"
```

 **(D) `re.split()`**
- Splits a string by a pattern.

*Code:*
```python
text = "apple,banana,cherry"
items = re.split(r",", text)
print(items)  # Output: ['apple', 'banana', 'cherry']
```

</td></tr>
</table>

# Tkinter

# 💛 Numpy

NumPy (Numerical Python) is the fundamental package for **scientific computing** in Python. It provides support for:

- **Multidimensional arrays** (faster than Python lists)
- **Mathematical functions** (linear algebra, statistics, etc.)
- **Tools for integrating C/C++ code**
- **Random number generation**

▶️ Creating a Numpy Array 

<details>
  <summary>Click to expand 🔻</summary>

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

</details>


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
