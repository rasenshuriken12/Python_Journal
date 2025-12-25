# Exception Handling 

<table>
<tr><td>

<br> 

❇️ Exception Handling handles errors that occur during the execution of a program. 

❇️⁠ It helps in preventing crashes due to errors.

<br>

▶️ Difference Between Errors and Exceptions

🔵 Errors 

<br> 

❇️ Errors are serious issues (compile time events) in your code, typically due to bad syntax or logic, that often can't be handled programmatically. They need to be fixed in the code.

<br>

Examples:
<br> 1. SyntaxError: Missed a colon or parentheses
<br> 2. IndentationError: Improper indentation
<br> 3. NameError: Referencing a variable that doesn't exist

---

🚧 🔵 Exceptions 

<br> 

❇️ Exceptions are runtime events that occur during execution and can be anticipated and handled. It can be fixed by using try, except blocks to catch and respond to exceptions gracefully.

<br>

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
