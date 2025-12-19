# Python Basics

<table>
<tr><td>
  
<br> ![1.](https://img.shields.io/badge/_1._-Print%20a%20string%20using%20print()-007396?style=for-the-badge&logo=python&logoColor=white)   

*Code:*
```python 
print("Hello World!")
```

*Output:*
```html
Hello World!
```

> - Here, print() displays the string 'Hello World!' on the console.

*Code:*
```python 
name = "Arya"
age = 18
branch, div = "IT", "D"
print(name, age)
print(branch)
print (div)
```

*Output:*
```html
Arya 18
IT
D
```

> - Here, name stores the value 'Arya'.
> - branch and div is stored as 'IT' & 'D' at a time.
> - 2nd & 3rd print() automatically inserts '\n' and  displays 'IT' & 'D' on the next line.


<br> ![2.](https://img.shields.io/badge/_2._-Input%20a%20string%20using%20input()-007396?style=for-the-badge&logo=python&logoColor=white)   

*Code:*
```python 
name = input("Enter your name: ")
print("Hello, ", name, "! Welcome!")
```

*Output:*
```html
Enter your name: Vidisha
Hello, Vidisha! Welcome!
```

> - Here, input() prompts the user with "Enter your name:" and stores the input 'Vidisha' of datatype string.
> - print() displays "Hello, Vidisha! Welcome!" using the value of name.

 
*Code:*
```python 
x, y, z = input("Enter name, age, city: ").split()
print("Name : ", x)
print("Age : ", y)
print("City : ", z)
```

*Output:*
```html 
Enter name, age, city: Vimla 18 Mumbai
Name: Vimla
Age : 18
City : Mumbai
```

> - Here, 3 inputs are taken at a time.
> - Age is taken as a string.
 

<br> ![3.](https://img.shields.io/badge/_3._-Typecasting-007396?style=for-the-badge&logo=python&logoColor=white)   
  
*Code:*
```python 
n = int(input("No. of Students: "))
print(n)
```

*Output:*
```html 
No. of Students: 10
10
```

> - Here, the variable n is converted to datatype int.


*Code:*
```python 
m = float(input("Average Marks of Students: "))
print(m)
```

*Output:*
```html 
No. of Students: 75.5
75.5
```

> - Here, the variable m is converted to datatype float.
 

<br> ![4.](https://img.shields.io/badge/_4._-Comments-007396?style=for-the-badge&logo=python&logoColor=white)   
  
*Code:*
```python
# This is a single-line comment.

""" This is a multi-line comment. """

''' This is a multi-line comment. '''
```
*Output:*
```html

```

> - Python ignores comments when running the code, but they help people understand what the code is doing.
 

<br> ![5.](https://img.shields.io/badge/_5._-Indentation-007396?style=for-the-badge&logo=python&logoColor=white)

<br> 

❇️ Indentation is used to define blocks of code.

❇️ All statements with the same level of indentation are considered part of the same block.

❇️ Indentation is achieved using whitespace (spaces or tabs) at the beginning of each line.

<br>

*Code:*
```python
if 10 > 5:
    print("I have indentation.")

print("I have no indentation.")
```

*Output:*
```html
I have indentation.
```

> - The 1st print statement is indented by 4 spaces, so they belong to the if block.
> - The 2nd print statement is not indented, so it is outside the if block.
 

<br> ![6.](https://img.shields.io/badge/_6._-Operators-007396?style=for-the-badge&logo=python&logoColor=white)   

❇️ UNARY Operators

❇️ BINARY Operators 

▶️ Arithmetic Operators

- Used for mathematical calculations.

| Operator | Description |
|---|---|
| + | Adds 2 no.s |
| - | Subtracts 2 no.s |
| * | Multiplies 2 no.s |
| ** | Exponential of 2 no.s |
| / | Quotient - Divides 2 no.s |
| % | Remainder - Divides 2 no.s(Modulo) |
| // | Floor Division - Rounds to whole no. |

*Code:*
```python
a = 10
b = 3

print("Addition:", a + b)        
print("Subtraction:", a - b)     
print("Multiplication:", a * b)  
print("Division:", a / b)        
print("Floor Division:", a // b)   # rounds down
print("Modulus:", a % b)           # remainder
print("Exponentiation:", a ** b)   # 10³
```

*Output:*
```html
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333333335
Floor Division: 3
Modulus: 1
Exponentiation: 1000
```

▶️ Comparison (Relational) Operators

- Used to compare values → result is True / False.

| Operator | Description |
|---|---| 
| == | Equal to	| 
| != | Not equal |
| > | Greater than |
| < | Less than | 
| >= | Greater or equal | 
| <= | Less or equal | 

*Code:*
```python
x = 10
y = 5

print("Equal:", x == y)           
print("Not equal:", x != y)       
print("Greater than:", x > y)     
print("Less than:", x < y)        
print("Greater or equal:", x >= y)
print("Less or equal:", x <= y)   
```

*Output:*
```html
Equal: False
Not equal: True
Greater than: True
Less than: False
Greater or equal: True
Less or equal: False
String comparison: True
```

- Can compare strings too

*Code:*
```python
print("String comparison:", "apple" < "banana") 
```

*Output:*
```html
String comparison: True 
```


▶️ Logocal Operators

- Used to combine conditional statements.

|   a   |   b   | a AND b | a OR b | NOT a | NOT b | 
|---|---|---|---|---|---|
| True  | True  |   True  |  True  | False | False |
| True  | False |  False  |  True  | False | True  |
| False | True  |  False  |  True  | True  | False |
| False | False |  False  | False  | True  | True  |

*Code:*
```python
age = 25
has_license = True

# AND - Both must be True
can_drive = age >= 18 and has_license
print("Can drive?", can_drive)

# OR - At least one must be True
has_discount = age < 12 or age >= 60
print("Has discount?", has_discount)  

# NOT - Inverts the boolean
is_adult = not (age < 18)
print("Is adult?", is_adult)  
```

*Output:*
```html
Can drive? True
Has discount? False
Is adult? True
```

▶️ Assignment Operators

- Used to assign and update values.

| Operator | Description | 
|---|---|
| =	| Assign | 
| += | Add & assign | 
| -= | Subtract & assign | 
| *= | Multiply & assign |
| /= | Divide & assign |
| //= | Floor divide & assign	|
| %= | Modulus & assign | 
| **= | Power & assign | 

*Code:*

x = 10  # Basic assignment
```python
# Compound assignment operators
x += 5       # x = x + 5 (now 15)
x -= 3       # x = x - 3 (now 12)
x *= 2       # x = x * 2 (now 24)
x /= 4       # x = x / 4 (now 6.0)
x //= 2      # x = x // 2 (now 3.0)
x %= 2       # x = x % 2 (now 1.0)
x **= 3      # x = x ** 3 (now 1.0)

# Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)      # 1 2 3
```

*Output:*
```html

```


▶️ Bitwise Operators



❇️ TERNARY Operators

▶️ Boolean Operators

| Operator | Description |
|---|---|

▶️ Boolean Operators

▶️ Boolean Operators

▶️ Boolean Operators

</td></tr>
</table>
