import pandas as pd

# Load the dataset
df = pd.read_csv('metadata.csv')

# Basic info
print("Shape:", df.shape)
print(df.info())

# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())
