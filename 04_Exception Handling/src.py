# Exception Handling

# Basic try-except
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")

# try-except-else-finally
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid types for division!")
        return None
    else:
        # Executes if no exception occurred
        print(f"Division successful!")
        return result
    finally:
        # Always executes
        print("Cleanup: Division operation attempted")

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "2"))

# Raising custom exceptions
class AgeError(Exception):
    """Custom exception for age validation"""
    pass

def validate_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative!")
    if age > 150:
        raise AgeError("Age seems unrealistic!")
    return f"Age {age} is valid"

try:
    print(validate_age(25))
    print(validate_age(-5))
except AgeError as e:
    print(f"Age validation failed: {e}")

# Multiple exceptions in one line
try:
    data = [1, 2, 3]
    value = data[5]
    result = value / 0
except (IndexError, ZeroDivisionError) as e:
    print(f"Caught an error: {e}")

# Nested try-except
try:
    file = open("nonexistent.txt", "r")
    try:
        content = file.read()
        print(content)
    finally:
        file.close()
        print("File closed")
except FileNotFoundError:
    print("File not found!")

# Assertions for debugging
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    return sum(numbers) / len(numbers)

try:
    print(calculate_average([1, 2, 3]))
    print(calculate_average([]))
except AssertionError as e:
    print(f"Assertion failed: {e}")
