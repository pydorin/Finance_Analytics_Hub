import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from Excel file - please update abc
file_path = ''
df = pd.read_excel(file_path)

# Convert 'Month' column to datetime
df['Month'] = pd.to_datetime(df['Month'])

# Convert 'Region' column to numerical format
df['Region'] = pd.factorize(df['Region'])[0]

# Calculate correlation matrix
corr_matrix = df.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
