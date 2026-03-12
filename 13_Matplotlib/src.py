# Matplotlib - Plotting Library

import matplotlib.pyplot as plt
import numpy as np

# Basic line plot
plt.figure(figsize=(10, 6))
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--')
plt.title('Sine and Cosine Functions')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Plot 1: Linear
axes[0, 0].plot(x, x, 'b-', label='y=x')
axes[0, 0].plot(x, x**2, 'r--', label='y=x²')
axes[0, 0].set_title('Linear and Quadratic')
axes[0, 0].legend()
axes[0, 0].grid(True)

# Plot 2: Exponential
axes[0, 1].plot(x, np.exp(x/2), 'g-')
axes[0, 1].set_title('Exponential')
axes[0, 1].set_yscale('log')
axes[0, 1].grid(True)

# Plot 3: Histogram
data = np.random.randn(1000)
axes[1, 0].hist(data, bins=30, alpha=0.7, color='orange', edgecolor='black')
axes[1, 0].set_title('Histogram')
axes[1, 0].set_xlabel('Value')
axes[1, 0].set_ylabel('Frequency')

# Plot 4: Scatter
x_scatter = np.random.randn(100)
y_scatter = np.random.randn(100)
colors = np.random.rand(100)
sizes = np.random.rand(100) * 100
scatter = axes[1, 1].scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.6)
axes[1, 1].set_title('Scatter Plot')
plt.colorbar(scatter, ax=axes[1, 1])

plt.tight_layout()
plt.show()

# Bar chart
plt.figure(figsize=(10, 6))
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
colors = ['red', 'green', 'blue', 'orange', 'purple']

bars = plt.bar(categories, values, color=colors, alpha=0.7)
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}', ha='center', va='bottom')

plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
sizes = [30, 20, 25, 15, 10]
labels = ['Python', 'JavaScript', 'Java', 'C++', 'Other']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
explode = (0.1, 0, 0, 0, 0)  # Explode the 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Programming Language Usage')
plt.axis('equal')
plt.show()

# 3D plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_title('3D Surface Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.colorbar(surf)
plt.show()

# Contour plot
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, 20, cmap='coolwarm')
plt.clabel(contour, inline=True, fontsize=8)
plt.title('Contour Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()
plt.show()

# Box plot
plt.figure(figsize=(10, 6))
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, labels=['Group 1', 'Group 2', 'Group 3'])
plt.title('Box Plot Example')
plt.xlabel('Groups')
plt.ylabel('Values')
plt.grid(True, alpha=0.3)
plt.show()

# Heatmap
plt.figure(figsize=(8, 6))
matrix = np.random.rand(10, 10)
im = plt.imshow(matrix, cmap='hot', interpolation='nearest')
plt.title('Heatmap')
plt.colorbar(im)
plt.show()

# Multiple styles in one figure
fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# Available styles
styles = ['default', 'ggplot', 'seaborn', 'classic', 'dark_background', 'bmh']
for i, ax in enumerate(axes.flat):
    if i < len(styles):
        with plt.style.context(styles[i]):
            ax.plot(x, np.sin(x + i))
            ax.set_title(f'Style: {styles[i]}')
            ax.grid(True)

plt.tight_layout()
plt.show()
