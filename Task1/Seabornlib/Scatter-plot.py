import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset('tips')
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex', size='size', sizes=(20, 200), palette='viridis', alpha=0.7)
plt.title('Scatter Plot of Total Bill vs Tip')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.legend(title='Gender')
plt.tight_layout()
plt.show()


