# Python Basics


<br> ![1.](https://img.shields.io/badge/_1._-Print%20a%20string%20using%20print()-007396?style=for-the-badge&logo=python&logoColor=white)   

<details>
  <summary>Click to expand 🔻</summary>

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

</details>


<br> ![2.](https://img.shields.io/badge/_2._-Input%20a%20string%20using%20input()-007396?style=for-the-badge&logo=python&logoColor=white)   

<details>
  <summary>Click to expand 🔻</summary>

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

</details> 

<br> ![3.](https://img.shields.io/badge/_3._-Typecasting-007396?style=for-the-badge&logo=python&logoColor=white)   

<details>
  <summary>Click to expand 🔻</summary>
  
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


</details> 
