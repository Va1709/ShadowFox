import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)
sizes = 1000 * np.random.rand(50) 
colors = np.random.rand(50) 
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='viridis')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.colorbar()  
plt.show()
