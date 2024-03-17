import pandas as pd

# Read the excel file into data frame
excell_file_location = '/Users/dd/Desktop/3Y.xlsx'
df = pd.read_excel(excell_file_location)

# # Check for missing values
# missing_values = df.isnull().sum()
# print("Missing values in the DataFrame:")
# print(missing_values)

df = df.rename(columns={'Feet amount': 'Feet_amount'})

# Create a pivot table with grand totals
pivot_table = pd.pivot_table(df, index=['Region',], columns='Month',
                             values='Feet_amount', aggfunc='sum', margins=True)

pivot_table = pivot_table.round()


print(pivot_table)

# Export pivot table to Excel
pivot_table.to_excel('/Users/dd/Desktop/pivot_table.xlsx')