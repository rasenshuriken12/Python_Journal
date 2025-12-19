<table>
<tr><td>

<br> ![1.](https://img.shields.io/badge/_1._-Numeric-007396?style=for-the-badge&logo=python&logoColor=white)

1.1 Integer

*Code:*
```python
x = int(1)
print(x)
print(type(x))
```

*Output:*
```html
1
<class 'int'>
```

1.2 Float 

*Code:*
```python
y = float(2)
print(y)
print(type(y))
```

*Output:*
```html
2.0
<class 'float'>
``` 

1.3 Complex

*Code:*
```python
z = complex(1, 2)
print(z)
print(type(z))
```

*Output:*
```html
1 + 2j
<class 'complex'>
```

 
<br> ![2.](https://img.shields.io/badge/_2._-Dictionary-007396?style=for-the-badge&logo=python&logoColor=white)

<br>

❇️ Stores key-value pairs.

❇️ Mutable (can be changed).

❇️ No duplicate keys allowed.

❇️ Maintains insertion order (Python 3.7+).

❇️ No indexing, access via keys.

❇️ Syntax: { "key" : "value" }

<br>

▶️ Creating a Dictionary 

*Code:*
```python
d1 = {1 : 'Hello', 2 : 'Good', 3 : 'Morning'}
print(d1)
```

*Output:*
```html
{1 : 'Hello', 2 : 'Good', 3 : 'Morning'}
```

🔸 Using dict()

*Code:*
```python
d2 = dict(a = "Hello", b = "Good", c = 'Morning')  # String keys only
print(d2)
```

*Output:*
```html
{'a' : "Hello", 'b' : "Good", 'c' : 'Morning'}
```

🔸 Using dict() & zip()

*Code:*
```python
keys = [1, 2, 3]
values = ['Geeks', 'For', 'Geeks']
d3 = dict(zip(keys, values))
print(d3)
d3 = dict(zip(values, keys))  # Dictionaries are mutable
print(d3)

```

*Output:*
```html
{1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}
{'Geeks' : 3, 'For' : 2}
```
> -  Initially, 1 is assigned to 'Geeks' then 1 is replaced and 3 is assigned to 'Geeks'.

*Code:*
```python
d4 = {'GEEKS' : 1, 'For' : 2, 'Geeks' : 3}  # Case sensitive 
print(d4)
```

*Output:*
```html
{'GEEKS' : 1, 'For' : 2, 'Geeks' : 3}
```

🔸 Storing different values

*Code:*
```python
d5 = {'name' : 'Tanmay', 'age' : 18}
print(d5)
```

*Output:*
```html
{'name' : 'Tanmay', 'age' : 18}
```

🔸 Storing different keys

*Code:*
```python
d6 = {"name" : 'Dhanesh', 2025 : "year"}
print(d6)
```

*Output:*
```html
{"name" : 'Dhanesh', 2025 : "year"}
```

▶️ Accessing Dictionary items

*Code:*
```python
keys = ['name', '1', (1,2)]
values = ['Ritesh', 'Python', (1,2,4)]

d1 = dict(zip(keys, values))
print(d1)
print(d1['name'])  # Only Keys(LHS) can be used to access items.

d2 = dict(zip(values, keys))
print(d2)
print(d2['1'])
```

*Output:*
```html
{'name' : 'Ritesh', '1' : 'Python', (1,2) : (1,2,4)}
Deva
{'Ritesh' : 'name', 'Python' : '1', (1,2,4) : (1,2)}

```

🔸 Using get()

*Code:*
```python
d = {'name' : 'Deva', 1 : 'Python', (1,2) : [1,2,4]}
print(d.get("name"))  # Only keys can be used to access items.
print(d.get(1))
print(d.get((1,2)))
```

*Output:*
```html
Deva
Python
[1,2,4]
``` 

▶️ Adding & Updating Dictionary items

🔸 Adding 

*Code:*
```python
d = {1 : 'Hello', '2' : 'Good', 3 : 'Morning'}
d[4] = "Sampada"   # New Key-Value pair
print(d)
```

*Output:*
```html
{1 : 'Hello', '2' : 'Good', 3 : 'Morning', 4 : 'Sampada'}
```

🔸 Updating 

*Code:*
```python
d = {1 : 'Hello', '2' : 'Good', 3 : 'Morning', 4 : 'Astha'}
d[3] = "Evening"   # Updating an existing value
print(d)
```

*Output:*
```html
{1 : 'Hello', '2' : 'Good', 3 : 'Evening', 4 : 'Astha'}
```

▶️ Deleting Dictionary items

🔸 Using del

*Code:*
```python
d = {1 : 'Hello', '2' : 'Good', 3 : 'Morning', 4 : 'Shrutika'}
del d[3]   # Deletes only Keys(LHS).
print(d)
```

*Output:*
```html
{1 : 'Hello', '2' : 'Good', 4 : 'Shrutika'}
```

🔸 Using pop()

*Code:*
```python
d = {1 : 'Hello', '2' : 'Good', 4 : 'Shrutika'}
print(d.pop('2'))  # Deletes Keys & returns its Values.
print(d)
```

*Output:*
```html
Good
{1 : 'Hello', 4 : 'Shrutika'}
```

🔸 Using popitem()

*Code:*
```python
d = {1 : 'Hello', 4 : 'Shrutika'}
K, V = d.popitem()
print(f"Key : {K}, Value : {V}")  # Deletes & returns Last Key-Value pair.
print(d)
```

*Output:*
```html
Key : 4, Value : Shrutika 
{1 : 'Hello'}
``` 

▶️ Iterating through Dictionary items
  
*Code:*
```python
d = {1 : 'Hello', '2' : 'Good', 'Morning' : 3}

for K in d.keys():
    print(f"Key : {K}")

print("\n")

for V in d.values():
    print(f"Value : {V}")
```

*Output:*
```html
Key : 1
Key : 2
Key : Morning

Value : Hello
Value : Good
Value : 3

```

*Code:*
```python
d = {1 : 'Hello', '2' : 'Good', 'Morning' : 3}

for K, V in d.items():
    print(f"Key, Value : {K}, {V}")
```

*Output:*
```html
Key, Value : 1, Hello
Key, Value : 2, Good
Key, Value : Morning, 3
``` 

▶️ Nested Dictionaries

*Code:*
```python
d = {1 : 'Welcome', 2 : 'To', 3 : {'A' : 'Harry', 'B' : 'Potter', 'C' : 'And The', 'D' : "Philosopher's", 'E' : 'Stone'}}
print(d)
```

*Output:*
```html
{1 : 'Welcome', 2 : 'To', 3 : {'A' : 'Harry', 'B' : 'Potter', 'C' : 'And The', 'D' : "Philosopher's", 'E' : 'Stone'}}
```
 
<br> ![3.](https://img.shields.io/badge/_3._-Boolean-007396?style=for-the-badge&logo=python&logoColor=white)

▶️ Boolean Examples 

*Code:*
```python
x = {}   # empty mapping 
print(bool(x))
y = ()   # empty sequence
print(bool(y))
```

*Output:*
```html
False
False
```

*Code:*
```python
x = None
print(bool(x))
y = 0.0
print(bool(y))
```

*Output:*
```html
False
False
```

*Code:*
```python
x = 1
print(bool(x))
y = - 1.5
print(bool(y))
```

*Output:*
```html
True
True
```

*Code:*
```python
x = 'Hello'   # non empty string
print(bool(x))
```

*Output:*
```html
True
```
 
▶️ Boolean Operators 

🔸 OR & AND operator 

*Code:*
```python
A, B = True, False
print(A or B)   # True - If any one variable is True.
print(A and B)  # True - Iff both variables are True.
```

*Output:*
```html
True
False
```

*Logic:*
|   A   |   B   |  OR   |  AND  |
|-------|-------|-------|-------|
| True  | True  | True  | True  |
| True  | False | True  | False |
| False | True  | True  | False |
| False | False | False | False |

🔸 NOT Operator

*Code:*
```python
A, B = True, False
print(not A)   # True - If variable is False.
print(not B)
```

*Output:*
```html
False
True
```

🔸 Equivalent & Not equivalent Operator

*Code:*
```python
A, B = True, False
print(A == B)   # True - Iff both variables have same value.
print(A != B)   # True - Iff both variables don't have same value.
```

*Output:*
```html
False
True
```
🔸 is Operator

*Code:*
```python
A, B = 5, 5
print(A is B)   # True - if both variables refer to the same value in memory. 
```

*Output:*
```html
True
```

> - `==` & `is` operator work differently. `==` focuses on same values while `is` focuses on values at same Memory location.

🔸 in Operator

*Code:*
```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  
print("orange" in fruits)
```

*Output:*
```html
True
False
```
> - It checks if a value exists within a sequence (like a list, tuple, string, or range).

<br> ![4.](https://img.shields.io/badge/_4._-Sequence-007396?style=for-the-badge&logo=python&logoColor=white)

🔵 String

▶️ Creating a string 

*Code:*
```python
string1  = "Hello Good Morning"
print(string1)

string2  = "How are you?"
print(string2))

print(type(string1))
```

*Output:*
```html
Hello Good Morning
How are you?
<class 'str'>
```

🔸 Multi Line Strings

*Code:*
```python
s1 = """ Hi guys, 
I am Learning Python String."""
print(s)

s2 = '''Hello Good Morning,
I live in Mumbai, India.'''
print(s)
```

*Output:*
```html
Hi guys, 
I am Learning Python String.
Hello Good Morning,
I live in Mumbai, India.
``` 


🔵 List

🔵 Tuple


<br> ![5.](https://img.shields.io/badge/_5._-Set-007396?style=for-the-badge&logo=python&logoColor=white)

<br> ⊡⁠ Stores unordered unique elements.
<br> ⊡⁠ Mutable (can add/remove items).
<br> ⊡⁠ No duplicates allowed.
<br> ⊡⁠ Unordered, so no indexing.
<br> ⊡⁠ Syntax: { item1, item2, item3 }

▶️ Creating a set

*Code:*
```python
set1  = set(" Hello Good Morning")
print(set1)
print(type(set1))
```

*Output:*
```html
{'n', 'r', ' ', 'o', 'g', 'i', 'l', 'd', 'G', 'M', 'H', 'e'}
<class 'set'>
```

🔸 Heterogeneous Elements

*Code:*
```python
set2 = {"Hello", 10, 52.7, True}
print(set2)
```

*Output:*
```html
{'Hello', True, 10, 52.7}
```

> - Output varies as Sets display Unordered elements with No Duplicates. 

▶️ Accessing a Set 

*Code:*
```python
set1  = set(["Hello", "Good", "Morning"])

for i in set1:
    print(i, end=" ")
```

*Output:*
```html
Morning Hello Good
```

> - Output varies

▶️ Adding items to set

🔸 Using add()

*Code:*
```python
set1 = {1,2,3,4}
set1.add(5)
print(set1)
```

*Output:*
```html
{1, 2, 3, 4, 5,}
```

> - Here, add() is used to add only a single item.

🔸 Using update()

*Code:*
```python
set2 = {1,2,3,4}
set2.update([5,6])
pint(set2)
```

*Output:*
```html
{1, 2, 3, 4, 5, 6}
```

> - Here, update() is used to add multiple items.
> - Only 6 is added, bcoz 5 is already present and Set doesn't allow Duplicates.

▶️ Removing items from a set

🔸 Using remove()

*Code:*
```python
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)

set1.remove(7)
print(set1)
```

*Output:*
```html
{1, 2, 4, 5}
Traceback (most recent call last):
  File "/home/main.py", line 5, in <module>
    set1.remove(7)
    ~~~~~~~~~~~^^^
KeyError: 7
```

> - Here, remove() is used to remove only a single item.
> - It raises an error when an element is removed that does not exist.

🔸 Using discard()

*Code:*
```python
set1 = {1, 2, 3, 4, 5}
set1.discard(3)
print(set1)

set1.discard(7)
print(set1)    # No Errors raised
```

*Output:*
```html
{1, 2, 4, 5}
{1, 2, 4, 5}
```

> - Here, discard() is used to discard only a single item.
> - It doesn't raise an error when an element is discarded that does not exist.

🔸 Using pop()

*Code:*
```python
set1 = {1, 2, 3, 4, 5}
val = set1.pop()
print(val)
print(set1)
```

*Output:*
```html
{2, 3, 4, 5}
```

> - Here, pop() is used to pop & return any random item.

🔸 Using clear()

*Code:*
```python
set1 = {1, 2, 3, 4, 5}
set1.clear()
print(set1)
```

*Output:*
```html
set()
```

> - Here, pop() is used to pop all items from a set.

🔵 Frozenset

<br> ❇️ Same as a set(), but frozenset() are Immutable i.e its elements cannot be modified.
<br> ❇️⁠ It accepts iterable objects as input parameter.
<br> ❇️ Syntax : frozenset(iterable_obj_name)

▶️ Converting a Dictionary to Frozenset

*Code:*
```python
d = {"name" : "Devaratha", "age" : 19}
print(frozenset(d))
```

*Output:*
```html
frozenset({'age', 'name'})
```

▶️ Converting a List to Frozenset

*Code:*
```python
l = ["Hello", "Good", "Morning"]
print(frozenset(l))
```

*Output:*
```html
frozenset({'Good', 'Hello', 'Morning'})
```

▶️ Converting a Tuple to Frozenset

*Code:*
```python
t = ()   # Empty Tuple
print(frozenset(t))
```

*Output:*
```html
frozenset()
```

▶️ Frozenset / Set Operations 

🔸 Copy

*Code:*
```python
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])
c = a.copy()
print(c)
```

*Output:*
```html
frozenset({1, 2, 3, 4})
```

🔸 Union

*Code:*
```python
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])
u = a.union(b)
print(u)
```

*Output:*
```html
frozenset({1, 2, 3, 4, 5, 6})
```

🔸 Intersection 

*Code:*
```python
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])
i = a.intersection(b)
print(i)
```

*Output:*
```html
frozenset({3, 4})
```

🔸 Difference 

*Code:*
```python
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])
d = a.difference(b)
print(d)
```

*Output:*
```html
frozenset({1, 2})
```

🔸 Symmetric Difference 

*Code:*
```python
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])
u = a.symmetric_difference(b)
print(u)
```

*Output:*
```html
frozenset({1, 2, 5, 6})
```

</td></tr>
</table>



