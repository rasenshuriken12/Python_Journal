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

