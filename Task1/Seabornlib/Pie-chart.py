import matplotlib.pyplot as plt
import seaborn as sns

# Load the tips dataset from seaborn
tips = sns.load_dataset('tips')

# Calculate the total tips given by gender
tips_by_gender = tips.groupby('sex')['tip'].sum().reset_index()

# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(tips_by_gender['tip'], labels=tips_by_gender['sex'], autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'], startangle=140)
plt.title('Distribution of Tips Given by Gender')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()
