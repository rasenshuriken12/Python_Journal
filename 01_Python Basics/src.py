# Hello World
print("Hello, Python! 👋")

# Variables and basic operations
name = "Alice"
age = 25
height = 5.6
is_student = True

print(f"{name} is {age} years old, {height}ft tall, Student: {is_student}")

# Basic input and conditionals
user_input = input("Enter your name: ")
if len(user_input) > 0:
    print(f"Welcome, {user_input}!")
else:
    print("No name entered")

# Loops
for i in range(5):
    print(f"Count: {i}")

count = 0
while count < 3:
    print(f"While loop: {count}")
    count += 1

# Functions
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Python"))
print(greet("World", "Hi"))

# List comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")
