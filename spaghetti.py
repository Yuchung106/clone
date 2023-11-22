import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
np.random.seed(0)
data = np.random.randn(100, 2)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Descriptive Statistics: Mean and Median
a = data[:, 0]
b = data[:, 1]
axes[0, 0].bar(['Mean', 'Median'], [np.mean(a), np.median(a)], color='blue', alpha=0.7, label='Variable A')
axes[0, 0].bar(['Mean', 'Median'], [np.mean(b), np.median(b)], color='green', alpha=0.7, label='Variable B')
axes[0, 0].legend()
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')

# Correlation Analysis
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1])
axes[0, 1].set_title('Correlation Analysis')

# Histogram of Variables
axes[1, 0].hist(a, bins=15, color='blue', alpha=0.7, label='Variable A')
axes[1, 0].hist(b, bins=15, color='green', alpha=0.7, label='Variable B')
axes[1, 0].legend()
axes[1, 0].set_title('Histogram of Variables')

# Scatter Plot of Variable 1 vs Variable 2
axes[1, 1].scatter(a, b, alpha=0.7)
axes[1, 1].set_xlabel('Variable 1')
axes[1, 1].set_ylabel('Variable 2')
axes[1, 1].set_title('Scatter Plot of Variable 1 vs Variable 2')

# Adjust layout and display
plt.tight_layout()
plt.show()

