import matplotlib.pyplot as plt  
import numpy as np

x = np.array([1, 10])
y = np.array([1, 10])

plt.plot(x, y)
plt.title("Line Chart")
plt.xlabel("x")  # Corrected xlabel
plt.ylabel("y")  # Corrected ylabel
plt.show()
