import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, vert=True, patch_artist=True, notch=True, labels=['A', 'B', 'C'], showmeans=True)
plt.title('Box Plot')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()
