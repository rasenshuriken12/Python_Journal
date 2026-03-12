# File Handling

import os
import json
import pickle

# Writing to a text file
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")
    file.write("Python file handling is easy!\n")
print("File written successfully")

# Reading from a text file
print("\nReading entire file:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
print("\nReading line by line:")
with open("sample.txt", "r") as file:
    for line in file:
        print(f"Line: {line.strip()}")

# Appending to a file
with open("sample.txt", "a") as file:
    file.write("This line is appended.\n")

# Using seek() and tell()
print("\nFile pointer operations:")
with open("sample.txt", "r") as file:
    print(f"Current position: {file.tell()}")
    content = file.read(10)
    print(f"Read 10 chars: {content}")
    print(f"New position: {file.tell()}")
    file.seek(0)  # Go back to start
    print(f"After seek(0): {file.tell()}")

# Working with binary files
binary_data = bytes([65, 66, 67, 68, 69])  # ASCII A,B,C,D,E
with open("binary.bin", "wb") as file:
    file.write(binary_data)

with open("binary.bin", "rb") as file:
    read_data = file.read()
    print(f"\nBinary file content: {read_data}")
    print(f"As string: {read_data.decode('ascii')}")

# JSON file handling
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"],
    "is_student": False
}

# Write JSON
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
print("\nJSON file written")

# Read JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(f"Loaded JSON: {loaded_data}")
    print(f"Name: {loaded_data['name']}")

# CSV file handling
import csv

# Write CSV
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "Boston"],
    ["Bob", 30, "Chicago"],
    ["Charlie", 35, "Denver"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

# Read CSV
print("\nCSV content:")
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"| {' | '.join(row)} |")

# Using pickle for Python object serialization
python_object = {
    "numbers": [1, 2, 3, 4, 5],
    "text": "Hello Pickle",
    "tuple": (10, 20, 30),
    "boolean": True
}

with open("data.pkl", "wb") as file:
    pickle.dump(python_object, file)

with open("data.pkl", "rb") as file:
    loaded_object = pickle.load(file)
    print(f"\nPickle loaded: {loaded_object}")

# File and directory operations
print(f"\nFile exists: {os.path.exists('sample.txt')}")
print(f"Is file: {os.path.isfile('sample.txt')}")
print(f"Is directory: {os.path.isdir('sample.txt')}")
print(f"File size: {os.path.getsize('sample.txt')} bytes")
print(f"Absolute path: {os.path.abspath('sample.txt')}")

# Create directory
os.makedirs("test_dir/subdir", exist_ok=True)
print("\nDirectory created")

# List directory contents
print("\nFiles in current directory:")
for item in os.listdir("."):
    if os.path.isfile(item):
        print(f"📄 {item}")
    elif os.path.isdir(item):
        print(f"📁 {item}")

# Cleanup (commented to keep files)
# os.remove("sample.txt")
# os.remove("binary.bin")
# os.remove("data.json")
# os.remove("data.csv")
# os.remove("data.pkl")
# os.rmdir("test_dir/subdir")
# os.rmdir("test_dir")
