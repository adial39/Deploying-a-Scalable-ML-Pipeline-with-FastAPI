import pandas as pd

# Load the dataset
df = pd.read_csv('data/census.csv')

# Display the first 5 rows
print("First 5 rows:")
print(df.head())

# Show data info
print("\nData Info:")
print(df.info())

# Show summary statistics for numerical and categorical columns
print("\nSummary Statistics:")
print(df.describe(include='all'))
