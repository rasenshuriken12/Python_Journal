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

- Operators that work on a single operand.

▶️ Arithmetic unary

*Code:*
```python
x = 3.14

print(+x)      # 3.14 (positive)
print(-x)      # -3.14 (negation)

print(+-5)     # -5
print(--5)     # 5 (double negative)
```

▶️ Logical unary (not)

▶️ Bitwise unary (~)


❇️ BINARY Operators 

- Operators that work on two operands.

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

*Code:*
```python
print("-" * 10)
```

*Output:*
```html
----------
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


▶️ Logical Operators

- Used to combine conditional statements.

|   A   |   B   | A and B | A or B | not A | not B | 
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

# NOT - Inverts the boolean (Unary Operator)
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
```python
x = 10  # Basic assignment

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

▶️ Identity Operators

- Check if two objects are the same object in memory.

*Code:*
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is b:", a is b)          # False (different objects)
print("a is c:", a is c)          # True (same object)
print("a is not b:", a is not b)  # True

# Better to use == for value comparison
print("a == b:", a == b)          # True (same values)
```

▶️ Membership Operators

- Test if a value exists in a sequence.

*Code:*
```python
fruits = ["apple", "banana", "cherry"]

print("'banana' in fruits:", "banana" in fruits)          # True
print("'orange' not in fruits:", "orange" not in fruits)  # True

# Works with strings
text = "Hello World"
print("'World' in text:", "World" in text)      # True

# Works with dictionaries (checks keys)
person = {"name": "Alice", "age": 30}
print("'name' in person:", "name" in person)    # True
print("'Alice' in person:", "Alice" in person)  # False (checks keys, not values)
```

▶️ Bitwise Operators

- Work on numbers at the binary level.

> Truth Table for Bitwise Operators (0 - False, 1 - True)

| a | b | AND | OR | XOR |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 0 | 
| 1 | 0 | 0 | 1 | 1 |  
| 0 | 1 | 0 | 1 | 1 |
| 0 | 0 | 0 | 0 | 0 |

Refer [Logic Gates](https://github.com/rasenshuriken12/DLCOA/blob/main/Logic%20Gates)

*Code:*
```python
a = 10    # Binary: 1010
b = 4     # Binary: 0100

print("AND:", a & b)             # 0 (1010 & 0100 = 0000) - Both must be True
print("OR:", a | b)              # 14 (1010 | 0100 = 1110) - Atleast one must be True
print("XOR:", a ^ b)             # 14 (1010 ^ 0100 = 1110) - Anyone must be True
print("NOT:", ~a)                # -11 in 2's Complement (inverts bits) - 0 → 1, 1 → 0  (Unary Operator)
print("Left shift:", a << 1)     # 20 (1010 → 10100) - Add 0 from RHS
print("Right shift:", a >> 1)    # 5 (1010 → 0101) - Add 0 from LHS
```

*Code:*
```python
# Check if number is even/odd
num = 15
print(f"{num} is even?", (num & 1) == 0) 
```

*Output:*
```html
15 is even? False
```

▶️ Operator Precedence
- Determines order of operations.

*Code:*
```python
# PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
result = 2 + 3 * 4      # 14, not 20
print("2 + 3 * 4 =", result)

# Use parentheses to control order
result = (2 + 3) * 4    # 20
print("(2 + 3) * 4 =", result)

''' Full precedence (highest to lowest):
1. Parentheses: ()
2. Exponentiation: **
3. Unary: +x, -x, ~x
4. Multiplication/Division/Modulo: *, /, //, %
5. Addition/Subtraction: +, -
6. Bitwise shifts: <<, >>
7. Bitwise AND: &
8. Bitwise XOR: ^
9. Bitwise OR: |
10. Comparisons: ==, !=, >, <, >=, <=
11. Identity: is, is not
12. Membership: in, not in
13. Logical NOT: not
14. Logical AND: and
15. Logical OR: or
'''

# Complex example
result = 5 + 2 * 3 ** 2 - 4 / 2
print("5 + 2 * 3 ** 2 - 4 / 2 =", result)
# Steps:
1) 5 + 2 * 9 - 4 / 2
2) 5 + 18 - 4 / 2
3) 5 + 18 - 2 = 21
```

*Output:*
```html
2 + 3 * 4 = 14
(2 + 3) * 4 = 20
5 + 2 * 3 ** 2 - 4 / 2 = 21
```


❇️ TERNARY Operators

- Operators that work on three operands.

▶️ Conditional Operator

*Code:*
```python
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}") 

# Equivalent to:
if age >= 18:
    status = "adult"
else:
    status = "minor"
```

*Output:*
```html
Age 20: adult
```

</td></tr>
</table>
