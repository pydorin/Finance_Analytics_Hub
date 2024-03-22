import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
df = pd.read_excel("data.xlsx")

# Create box plot
plt.figure(figsize=(10, 6))
boxplot = df.boxplot(column='Feet amount', by=['Region'], grid=False)

# Add labels and title
plt.xlabel('Region')
plt.ylabel('Feet Amount')
plt.title('Box Plot of Feet Amount by Region')

# Show the plot - need to check why 2 plots are generated
plt.tight_layout()
plt.show()
