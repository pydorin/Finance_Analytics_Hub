import pandas as pd
import matplotlib.pyplot as plt

# Read the excell file (please update) - to check the path!
data = pd.read_excel('https://github.com/pydorin/Finance_Analytics_Hub/blob/main/3Y.xlsx')

# Group data by Year and Region
grouped_data = data.groupby(['Month', 'Region'])['Feet amount'].sum().unstack()

# Create bar chart
ax = grouped_data.plot(kind='bar', figsize=(11, 7))

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Total Feet Amount')
plt.title('Total Feet Amount by Month and Region')

# Add legend
plt.legend(title='Region')

# Rotate x-axis labels
plt.xticks(rotation=60)

# Add labels on top of the bars
for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.tight_layout()
plt.show()
