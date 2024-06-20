import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = sns.load_dataset('penguins')
mean_flipper_length = df.groupby(['species', 'sex']).flipper_length_mm.mean().reset_index()
sns.lineplot(x='species', y='flipper_length_mm', hue='sex', data=mean_flipper_length, marker='o')
plt.title('Mean Flipper Length across Species and Sex')
plt.ylabel('Mean Flipper Length (mm)')
plt.xlabel('Species')
plt.show()
