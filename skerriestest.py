import matplotlib.pyplot as plt
import numpy as np

# Create a range of numbers from 0 to 2 * Pi (100 steps)
x = np.linspace(1, 12 * np.pi, 180)

# Calculate the sine of these numbers
y = np.sin(x)

# Plot the sine wave
plt.plot(x, y)

# Add a title
plt.title('Simple Slabovich Sine Wave')

# Display the plot
plt.show()