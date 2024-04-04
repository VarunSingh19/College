import pandas as pd

# URL of the CSV dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Load the CSV dataset into a DataFrame
df = pd.read_csv(url)

# Displaying the first few rows
print("First few rows of the DataFrame:")
print(df.head())

# Displaying the last few rows
print("\nLast few rows of the DataFrame:")
print(df.tail())
