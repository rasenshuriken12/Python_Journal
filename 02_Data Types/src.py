# Numbers
integer_num = 42
float_num = 3.14159
complex_num = 3 + 4j

print(f"Integer: {integer_num}, Float: {float_num}, Complex: {complex_num}")

# Strings
text = "Python Programming"
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Split: {text.split()}")
print(f"Slice [0:6]: {text[0:6]}")

# Lists (mutable)
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
fruits.insert(1, "mango")
print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Tuples (immutable)
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# Dictionaries (key-value pairs)
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Java", "SQL"]
}
print(f"Person: {person}")
print(f"Name: {person['name']}")
print(f"Skills: {', '.join(person['skills'])}")

# Sets (unique elements)
unique_numbers = {1, 2, 3, 3, 4, 4, 5}
print(f"Set (no duplicates): {unique_numbers}")

# Boolean
is_python_fun = True
is_hard = False
print(f"Is Python fun? {is_python_fun}")
print(f"Is it hard? {is_hard}")

# Type checking
print(f"Type of 42: {type(42)}")
print(f"Type of 'hello': {type('hello')}")
print(f"Type of [1,2,3]: {type([1,2,3])}")
