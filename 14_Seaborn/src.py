# Seaborn - Statistical Data Visualization

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load built-in datasets
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
titanic = sns.load_dataset('titanic')

print("Tips dataset:")
print(tips.head())
print(f"\nColumns: {tips.columns.tolist()}")

# Set style
sns.set_style('whitegrid')
sns.set_palette('husl')

# 1. Distribution plots
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(data=tips, x='total_bill', bins=30, kde=True)
plt.title('Distribution of Total Bill')

plt.subplot(1, 2, 2)
sns.kdeplot(data=tips, x='total_bill', hue='time', fill=True)
plt.title('KDE by Time')

plt.tight_layout()
plt.show()

# 2. Count plots
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
sns.countplot(data=tips, x='day')
plt.title('Number of meals by day')

plt.subplot(1, 3, 2)
sns.countplot(data=tips, x='sex', hue='smoker')
plt.title('Smokers by gender')

plt.subplot(1, 3, 3)
sns.countplot(data=tips, x='time')
plt.title('Lunch vs Dinner')

plt.tight_layout()
plt.show()

# 3. Relationship plots
plt.figure(figsize=(14, 5))

plt.subplot(1, 3, 1)
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', size='size')
plt.title('Tip vs Total Bill')

plt.subplot(1, 3, 2)
sns.lineplot(data=tips, x='size', y='total_bill', hue='day', marker='o')
plt.title('Total Bill by Party Size')

plt.subplot(1, 3, 3)
sns.barplot(data=tips, x='day', y='total_bill', hue='sex')
plt.title('Average Bill by Day and Gender')

plt.tight_layout()
plt.show()

# 4. Box plots and violin plots
plt.figure(figsize=(14, 5))

plt.subplot(1, 3, 1)
sns.boxplot(data=tips, x='day', y='total_bill', hue='smoker')
plt.title('Box Plot - Total Bill by Day')

plt.subplot(1, 3, 2)
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True)
plt.title('Violin Plot - Distribution by Day')

plt.subplot(1, 3, 3)
sns.boxenplot(data=tips, x='time', y='tip')
plt.title('Boxen Plot - Tip by Time')

plt.tight_layout()
plt.show()

# 5. Pair plots (multiple variables)
sns.pairplot(iris, hue='species', diag_kind='hist')
plt.suptitle('Iris Dataset - Pair Plot', y=1.02)
plt.show()

# 6. Heatmap (correlation)
plt.figure(figsize=(10, 8))
correlation = tips.select_dtypes(include=[np.number]).corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={'shrink': 0.8})
plt.title('Correlation Heatmap - Tips Dataset')
plt.show()

# 7. Joint plots
g = sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg', height=8)
g.fig.suptitle('Joint Plot with Regression', y=1.02)
plt.show()

# 8. Facet grids (multi-panel plots)
g = sns.FacetGrid(tips, col='time', row='smoker', hue='sex', height=4)
g.map(sns.scatterplot, 'total_bill', 'tip')
g.add_legend()
plt.show()

# 9. Cat plots (categorical)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.catplot(data=tips, x='day', y='total_bill', kind='boxen', height=4, aspect=1.5)
plt.title('Catplot - Boxen')

plt.subplot(1, 2, 2)
sns.catplot(data=tips, x='day', y='tip', kind='violin', height=4, aspect=1.5)
plt.title('Catplot - Violin')

plt.tight_layout()
plt.show()

# 10. Regression plots
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'alpha':0.5})
plt.title('Linear Regression')

plt.subplot(1, 2, 2)
sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex', col='time', height=4)
plt.title('Regression by Category')

plt.tight_layout()
plt.show()

# 11. Residual plots
plt.figure(figsize=(10, 4))
sns.residplot(data=tips, x='total_bill', y='tip', lowess=True)
plt.title('Residual Plot')
plt.show()

# 12. Styling options
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Different styles
styles = ['darkgrid', 'whitegrid', 'dark', 'white']
titles = ['Dark Grid', 'White Grid', 'Dark', 'White']

for ax, style, title in zip(axes.flat, styles, titles):
    with sns.axes_style(style):
        sns.histplot(data=tips, x='total_bill', kde=True, ax=ax)
        ax.set_title(title)

plt.tight_layout()
plt.show()

# 13. Custom palette examples
palettes = ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind']
fig, axes = plt.subplots(2, 3, figsize=(15, 8))

for ax, palette in zip(axes.flat, palettes):
    with sns.color_palette(palette):
        sns.boxplot(data=tips, x='day', y='total_bill', ax=ax)
        ax.set_title(f'Palette: {palette}')

plt.tight_layout()
plt.show()
