import matplotlib.pyplot as plt
import seaborn as sns

# Load the tips dataset from seaborn
tips = sns.load_dataset('tips')

# Plotting the histogram
plt.figure(figsize=(8, 6))
sns.histplot(tips['total_bill'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Total Bill Amounts')
plt.xlabel('Total Bill ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
