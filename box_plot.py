import pandas as pd
import matplotlib.pyplot as plt

# Sample data - to be ipdated
data = {
    'Year': [2023]*24 + [2024]*24 + [2023]*24,
    'Month': [f'{year}-{month:02}' for year in [2023, 2024] for month in range(1, 13)]*2,
    'Region': ['PNW']*24 + ['PSW']*24 + ['MW']*24,
    'Feet amount': [100, 105, 110, 116, 122, 128, 134, 141, 148, 155, 163, 171,
                    180, 189, 198, 208, 218, 229, 241, 253, 265, 279, 293, 307,
                    60, 78, 82, 86, 90, 95, 100, 105, 110, 115, 121, 127,
                    133, 140, 147, 154, 162, 170, 179, 188, 197, 207, 217, 228,
                    100, 130, 137, 143, 150, 158, 166, 174, 183, 192, 202, 212,
                    222, 233, 245, 257, 270, 284, 298, 313, 329, 345, 362, 380]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

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
