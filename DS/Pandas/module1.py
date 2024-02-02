import pandas as pd
print(pd.__version__)


# Pandas Series
# Description : In pandas, a series  is a one-dimensional labeled array capable of holding 
# any data types. it can be thought of as a column in a spreadsheet or a single column of a 
# DataFrame. A Series object has two main components: the index and the data.


a = [1,5,8]
myvar = pd.Series(a)
# print(myvar)
# print(myvar[2])

myvar = pd.Series(a,index = ["X","Y","Z"])
# print(myvar)



# Pandas DataFrame
# Description : In pandas, a Dataframe is a two-dimensional labeled data structure capable of holding
# data of different types. it is similar to a spreadsheet or a SQL table, where data is arranged in rows 
# and columns. A Dataframe consists of three main components:  the index, columns, and data.
# ab = pd.DataFrame()
# print(ab)

mydataset = {
    'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(mydataset)
# print(df)


data = {
    "Calories": [420,380,678],
    "Passings": [39,56,23]
}
df1 = pd.DataFrame(data)
# print(df1)


# Load file into a DataFrame
# 1. using JSON

df = pd.read_json('https://raw.githubusercontent.com/jdorfman/awesome-json-datasets/master/package.json')
# print(df)

print(df.isnull())

#  the isnull() function is a method in pandas used to detect missing or NaN
# (Not a Number) values in a DataFrame or Series. 


# print(df.isnull().sum())

# The isnull().sum() method is commonly used in pandas to count the number of 
# missing values (NaN) in each column of a DataFrame. 

# 2. using CSV
df1 = pd.read_csv('https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Gold%20Rates/annual_gold_rate.csv')
# print(df1)
# print(df1.head())
# print(df1.tail())
# print(df1.isnull())
# print(df1.isnull().sum())

# print(df1.info())

# The .info() method in pandas is used to display a concise summary of a DataFrame, 
# including information about the data types, non-null values, and memory usage. 
# It provides a quick overview of the structure and characteristics of the DataFrame.

# new_df = df1.dropna()
# print(new_df)
# new_df1 = df1.fillna(145)
# print(new_df1)