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

▶️ Logocal Operators

▶️ Bitwise Operators

❇️ BINARY Operators 

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

▶️ Relational Operators

- Used to compare values → result is True / False.

| Operator | Description |
|---|---| 
| == | Equal to	| 
| != | Not equal |
| > | Greater than |
| < | Less than | 
| >= | Greater or equal | 
| <= | Less or equal | 

❇️ TERNARY Operators

▶️ Boolean Operators

| Operator | Description |
|---|---|

▶️ Boolean Operators

▶️ Boolean Operators

▶️ Boolean Operators

</td></tr>
</table>
