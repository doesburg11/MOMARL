import pandas as pd
import matplotlib.pyplot as plt

file = "/home/doesburg/Dropbox/03_marl_code/MOMARL/MOMALand/beach/results/nds/BPD_50_individual.csv"

# Read the first row to get the axis titles
axis_titles = pd.read_csv(file, header=None, nrows=1).iloc[0]

# Read the rest of the CSV file, skipping the first row
data = pd.read_csv(file, header=None, skiprows=1)

# Assign columns to x and y
x = data[0]
y = data[1]

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the data with enhancements
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Pareto front')

# Fill the area beneath the line graph with grey color
plt.fill_between(x, y, color='grey', alpha=0.3)

# Add titles and labels
plt.title('Estimated Pareto coverage set Beach Problem Domain', fontsize=16, fontweight='bold')
plt.xlabel(axis_titles[0], fontsize=14)
plt.ylabel(axis_titles[1], fontsize=14)

# Add grid lines
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add a legend
plt.legend(loc='best')

# Scale the y-axis so that the minimum value is close to the x-axis
plt.ylim(bottom=min(y) - (max(y) - min(y)) * 0.1)

# Show the plot
plt.show()