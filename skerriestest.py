import matplotlib.pyplot as plt
import numpy as np

# Create a range of numbers from 0 to 2 * Pi (100 steps)
x = np.linspace(0, 2 * np.pi, 100)

# Calculate the sine of these numbers
y = np.sin(x)

# Plot the sine wave
plt.plot(x, y)

# Add a title
plt.title('Simple Sine Wave')

# Display the plot
plt.show()