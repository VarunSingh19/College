import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Gold%20Rates/annual_gold_rate.csv')
df1.plot(kind = "scatter",x = 'USD',y = 'INR')
print(plt.show())

df1.plot(kind = "bar",x = 'USD',y = 'INR')
print(plt.show())

df1.plot(kind = "area",x = 'USD',y = 'INR')
print(plt.show())

df1.plot(kind = "hist",x = 'USD',y = 'INR')
print(plt.show())