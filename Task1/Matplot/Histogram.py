import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
data = np.random.randn(1000) 
plt.hist(data, bins=30, alpha=0.7, color='purple', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
