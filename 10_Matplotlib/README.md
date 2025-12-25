▶️ Matplotlib is an open-source visualization library for the Python programming language, widely used for creating static, animated and interactive plots.

<br> ![1.](https://img.shields.io/badge/_1._-Data_Visualisation-007396?style=for-the-badge&logo=python&logoColor=white)   

❇️ Line Chart

- Line chart is used to represent a relationship between two data X and Y on a different axis.
- It displays data points connected by a line, often used to visualize trends over time, especially with time series data.
- It is ideal for analyzing continuous data, such as Stock prices, Temperature changes, or Website Traffic over days, months, or years.

*Code:*
```python

import matplotlib.pyplot as plt

# Sample data for the line chart
x = [0, 2, 4, 6, 8]
y = [0, 4, 16, 36, 64]

# Creating the line chart
fig, ax = plt.subplots()     # fig = Figure object (the canvas/window) , ax = Axes object (the actual plot area)
ax.plot(x, y, marker='o')

# Adding labels and explanation annotations
ax.set_title("Basic Components of Matplotlib Figure")
ax.set_xlabel("X-Axis") 
ax.set_ylabel("Y-Axis")  

plt.show()
```

*Output:*

<img src="https://github.com/rasenshuriken12/Python_Journal/blob/c7f5272304f0b71e33ee0c7f0a592e125c47d23d/10_Matplotlib/assets/LineChart.png" alt="Line Chart" width="500">
