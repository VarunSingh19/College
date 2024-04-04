import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris_data = load_iris()
iris_data
print(iris_data.keys())
df = pd.DataFrame(iris_data.data, columns = iris_data.feature_names)
print(df)
training_data, testing_data = train_test_split(df, test_size=0.2)
print(training_data)
print(testing_data)
print(f"No. of training examples :{training_data.shape[0]}")
print(f"No. of testing examples :{testing_data.shape[0]}")
training_data.head()