import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json

# Load data from JSON files
with open('data1.json', 'r') as f:
    data1 = json.load(f)


# Assuming 'similarities' and 'num_matrices' are keys in the loaded JSON data
similarities = data1['similarities']
num_matrices = 399

# Generate years range
years = range(2008, 2025)

# Generate ticks for x and y axes
ticks = np.linspace(0, num_matrices - 1, len(years))

# Plotting
plt.figure(figsize=(10, 8))

# Plot heatmap
heatmap = sns.heatmap(similarities, cmap='viridis', annot=False)
plt.xticks(ticks, years, color='white')  # Set tick labels color to white
plt.yticks(ticks, years, color='white')  # Set tick labels color to white
plt.xlabel('Year', color='white')  # Set x-axis label color to white
plt.ylabel('Year', color='white')  # Set y-axis label color to white
plt.title('Similarity Between Consecutive Correlation Matrices', color='white')  # Set title color to white

# Set color bar text color to white
cbar = heatmap.collections[0].colorbar
cbar.set_label('Similarity', color='white')  # Set colorbar label color to white
cbar.ax.tick_params(colors='white')  # Set colorbar tick colors to white

plt.tight_layout()

# Save the plot as a file
plt.savefig('heatmap.png', transparent=True)

# Display the plot
plt.show()