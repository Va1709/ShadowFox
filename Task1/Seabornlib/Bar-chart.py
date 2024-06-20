import matplotlib.pyplot as plt
import seaborn as sns

# Load the tips dataset from seaborn
tips = sns.load_dataset('tips')

# Calculate average total bill amount for each day of the week
avg_total_bill = tips.groupby('day')['total_bill'].mean().reset_index()

# Plotting the bar chart
plt.figure(figsize=(8, 6))
sns.barplot(x='day', y='total_bill', data=avg_total_bill, palette='rocket')
plt.title('Average Total Bill Amount by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Average Total Bill ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

