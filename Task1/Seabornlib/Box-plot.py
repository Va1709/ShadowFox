import matplotlib.pyplot as plt
import seaborn as sns

# Load the tips dataset from seaborn
tips = sns.load_dataset('tips')

# Plotting the box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='total_bill', data=tips, palette='pastel')
plt.title('Distribution of Total Bill Amounts by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill ($)')
plt.tight_layout()
plt.show()
