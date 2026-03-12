# Packages and Modules

# Creating and using modules
# First, create a file called 'mymath.py':

"""
# mymath.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

PI = 3.14159

class Calculator:
    def __init__(self, name):
        self.name = name
    
    def power(self, base, exp):
        return base ** exp
"""

# Import entire module
import mymath
print(f"Add: {mymath.add(10, 5)}")
print(f"PI: {mymath.PI}")

# Import specific items
from mymath import multiply, divide, Calculator
print(f"Multiply: {multiply(4, 3)}")
print(f"Divide: {divide(15, 3)}")

calc = Calculator("MyCalc")
print(f"Power: {calc.power(2, 10)}")

# Import with alias
import mymath as mm
print(f"Subtract: {mm.subtract(20, 7)}")

# Import all (not recommended)
from mymath import *
print(f"Add from * import: {add(100, 200)}")

# Package structure
"""
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        submodule.py
"""

# Create a package
# In __init__.py you can define what's exported
# __all__ = ['module1', 'module2']

# Using built-in modules
import math
import random
import datetime
import os
import sys

# Math module
print(f"Math: sqrt(16) = {math.sqrt(16)}")
print(f"Math: sin(90°) = {math.sin(math.pi/2):.2f}")

# Random module
print(f"\nRandom integer (1-10): {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'orange'])}")
print(f"Random sample: {random.sample(range(100), 5)}")

# Datetime module
now = datetime.datetime.now()
print(f"\nCurrent date/time: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Date only: {now.date()}")
print(f"Time only: {now.time()}")

# OS module
print(f"\nCurrent directory: {os.getcwd()}")
print(f"Environment PATH: {os.environ.get('PATH', 'Not set')[:50]}...")

# Sys module
print(f"\nPython version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Command line args: {sys.argv}")

# Creating a package with __init__.py
"""
# mypackage/__init__.py
print("Initializing mypackage")
__version__ = "1.0.0"

# mypackage/module1.py
def function1():
    return "Function 1 from module1"

# mypackage/module2.py
def function2():
    return "Function 2 from module2"
"""

# Third-party packages (need to be installed)
# pip install requests numpy pandas

try:
    import requests
    response = requests.get("https://api.github.com")
    print(f"\nRequests status: {response.status_code}")
except ImportError:
    print("\nRequests not installed")

# Module search path
print(f"\nModule search path:")
for i, path in enumerate(sys.path[:3]):  # Show first 3
    print(f"  {i+1}. {path}")

# Reloading modules
import importlib
import mymath
importlib.reload(mymath)  # Reload if module changed

# Conditional imports
try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False
    np = None

print(f"\nNumPy available: {NUMPY_AVAILABLE}")
