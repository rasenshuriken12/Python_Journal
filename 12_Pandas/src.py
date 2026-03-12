# Pandas - Data Analysis Library

import pandas as pd
import numpy as np

# Creating Series
print("=== Series ===")
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s3 = pd.Series({'a': 100, 'b': 200, 'c': 300})

print(f"Series 1:\n{s1}")
print(f"Series 2:\n{s2}")
print(f"Series 3:\n{s3}")
print(f"Value at index 'b': {s2['b']}")
print(f"Values > 2: {s1[s1 > 2]}")

# Creating DataFrames
print("\n=== DataFrames ===")
# From dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Tokyo', 'Paris', 'Berlin'],
    'Salary': [50000, 60000, 75000, 55000, 65000],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing']
}
df = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df)

# From list of lists
data2 = [
    [1, 'Product A', 10.99, 100],
    [2, 'Product B', 20.50, 200],
    [3, 'Product C', 15.75, 150]
]
df2 = pd.DataFrame(data2, columns=['ID', 'Product', 'Price', 'Quantity'])
print("\nDataFrame from list:")
print(df2)

# From NumPy array
arr = np.random.randn(5, 4)
df3 = pd.DataFrame(arr, columns=['A', 'B', 'C', 'D'])
print("\nDataFrame from NumPy:")
print(df3)

# DataFrame operations
print("\n=== DataFrame Operations ===")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Index: {df.index.tolist()}")
print(f"Data types:\n{df.dtypes}")
print(f"Info:")
df.info()
print(f"\nHead (first 3 rows):\n{df.head(3)}")
print(f"Tail (last 2 rows):\n{df.tail(2)}")
print(f"Describe:\n{df.describe()}")

# Selecting data
print("\n=== Selecting Data ===")
print(f"Single column 'Name':\n{df['Name']}")
print(f"Multiple columns:\n{df[['Name', 'Age']]}")
print(f"Row by index (iloc):\n{df.iloc[1]}")
print(f"Rows 1-3, cols 0-2 (iloc):\n{df.iloc[1:4, 0:3]}")
print(f"Row by label (loc):\n{df.loc[2]}")
print(f"Conditional selection (Age > 30):\n{df[df['Age'] > 30]}")
print(f"Multiple conditions (Age > 25 and Salary > 60000):\n{df[(df['Age'] > 25) & (df['Salary'] > 60000)]}")

# Adding/removing columns
print("\n=== Adding/Removing Columns ===")
df['Bonus'] = df['Salary'] * 0.1
print(f"With Bonus column:\n{df}")
df['Age Group'] = pd.cut(df['Age'], bins=[20, 30, 40], labels=['20-30', '30-40'])
print(f"With Age Group:\n{df}")
df.drop('Bonus', axis=1, inplace=True)
print(f"After dropping Bonus:\n{df}")

# Aggregation and grouping
print("\n=== Aggregation ===")
print(f"Mean salary by department:\n{df.groupby('Department')['Salary'].mean()}")
print(f"Stats by department:\n{df.groupby('Department').agg({'Salary': ['mean', 'min', 'max'], 'Age': 'mean'})}")

# Handling missing data
print("\n=== Missing Data ===")
df_with_nan = df.copy()
df_with_nan.loc[1, 'Salary'] = np.nan
df_with_nan.loc[3, 'City'] = None
print(f"DataFrame with NaN:\n{df_with_nan}")
print(f"Is null:\n{df_with_nan.isnull()}")
print(f"Drop rows with NaN:\n{df_with_nan.dropna()}")
print(f"Fill NaN with value:\n{df_with_nan.fillna({'Salary': df['Salary'].mean(), 'City': 'Unknown'})}")

# Sorting
print("\n=== Sorting ===")
print(f"Sort by Age:\n{df.sort_values('Age')}")
print(f"Sort by multiple columns:\n{df.sort_values(['Department', 'Salary'], ascending=[True, False])}")

# Merging and joining
print("\n=== Merging ===")
df_left = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df_right = pd.DataFrame({'ID': [2, 3, 4], 'Score': [85, 90, 75]})
print(f"Left:\n{df_left}")
print(f"Right:\n{df_right}")
print(f"Inner merge:\n{pd.merge(df_left, df_right, on='ID')}")
print(f"Left merge:\n{pd.merge(df_left, df_right, on='ID', how='left')}")
print(f"Right merge:\n{pd.merge(df_left, df_right, on='ID', how='right')}")
print(f"Outer merge:\n{pd.merge(df_left, df_right, on='ID', how='outer')}")

# Pivot tables
print("\n=== Pivot Tables ===")
pivot = pd.pivot_table(df, values='Salary', index='Department', aggfunc=['mean', 'sum'])
print(pivot)

# Reading and writing files
print("\n=== File I/O ===")
# Save to CSV
df.to_csv('data.csv', index=False)
print("DataFrame saved to 'data.csv'")

# Read from CSV
df_loaded = pd.read_csv('data.csv')
print("Loaded from CSV:")
print(df_loaded.head())

# Excel (requires openpyxl)
# df.to_excel('data.xlsx', index=False)
# df_excel = pd.read_excel('data.xlsx')

# JSON
df.to_json('data.json', orient='records')
with open('data.json', 'r') as f:
    print(f"JSON content:\n{f.read()[:200]}...")
df_json = pd.read_json('data.json')
