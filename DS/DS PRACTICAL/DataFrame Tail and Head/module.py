import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily','John'],
        'Age': [25, 30, 35, 40, 45, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix','CA']}

df = pd.DataFrame(data)

# Displaying the first few rows
print("First few rows of the DataFrame:")
print(df.head())

# Displaying the last few rows
print("\nLast few rows of the DataFrame:")
print(df.tail())
