▶️ Matplotlib is an open-source visualization library for the Python programming language, widely used for creating static, animated and interactive plots.

<br> ![1.](https://img.shields.io/badge/_1._-Data_Visualisation-007396?style=for-the-badge&logo=python&logoColor=white)   

*Code:*
```python
import matplotlib.pyplot as plt

# Sample data 
x = [0, 2, 4, 6, 8]
y = [0, 4, 16, 36, 64]

# Creating the line chart
fig, ax = plt.subplots()     # fig = Figure object (the canvas/window) , ax = Axes object (the actual plot area)
ax.plot(x, y, marker='o')

# Adding labels and title
ax.set_title("Basic Components of Matplotlib Figure")
ax.set_xlabel("X-Axis") 
ax.set_ylabel("Y-Axis")  

plt.show()
```

*Output:*

<img src="https://github.com/rasenshuriken12/Python_Journal/blob/c7f5272304f0b71e33ee0c7f0a592e125c47d23d/10_Matplotlib/assets/LineChart.png" alt="Line Chart" width="500">

❇️ Line Chart

- Line chart is used to represent a relationship between two data X and Y on a different axis.
- It displays data points connected by a line, often used to visualize trends over time, especially with time series data.
- It is ideal for analyzing continuous data, such as Stock prices, Temperature changes, or Website Traffic over days, months, or years.

*Code:*
```python
import matplotlib.pyplot as plt

# Sample data for the line chart
weeks = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']
temp = [55, 75, 78, 85, 80, 71, 69, 65]

# Create figure and axes object (Object-Oriented approach)
fig, ax = plt.subplots(figsize=(10, 8))  # fig = figure, ax = axes
ax.plot(weeks, temp, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)  # linestyle = '-' OR 'solid'

# Add labels and title
ax.set_xlabel('Weeks', fontsize=12)
ax.set_ylabel('Temperature', fontsize=12)
ax.set_title('Temperature in Mumbai', fontsize=14, fontweight='bold')

# Add value annotations above each point
for i, value in enumerate(temp):
    ax.text(weeks[i], value + 1.5, f'{value}', ha='center', fontsize=10, fontweight='bold')

# Add explanatory annotations
ax.text(2.5, 8, 'Line connects data points over time', ha='center', va='bottom', fontsize=10, color='blue', bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))

ax.text(-0.3, temp[0], '← Starting Point', ha='left', va='center', fontsize=10, color='red', fontweight='bold')
ax.text(5.3, temp[-1], 'Ending Point →', ha='right', va='center', fontsize=10, color='red', fontweight='bold')

# Add grid
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Customize ticks
ax.tick_params(axis='both', which='major', labelsize=10)

# Add a legend (though we only have one line)
ax.legend(['Weekly Temperature'], loc='upper left')

plt.tight_layout()
plt.show()
```

*Output:*

<img src="https://github.com/rasenshuriken12/Python_Journal/blob/c7f5272304f0b71e33ee0c7f0a592e125c47d23d/10_Matplotlib/assets/LineChart.png" alt="Line Chart" width="500">


'-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

