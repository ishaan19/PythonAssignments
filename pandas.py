#1
import numpy as np
import pandas as pd

context = {
           'Name':pd.Series(['bharti','ishaan']),
           'Age':pd.Series([21,22]),
           'Email':pd.Series(['bhartigupta63@gmail.com','ishaankapoor1906@gmail.com']),
           'Phone number':pd.Series(['9999999119','9999999910'])
           }
df = pd.DataFrame(context)
print(df)

#2

import pandas as pd
import numpy as np

file = pd.read_csv("weather.csv")

print("The first five rows of trhe dataframe are:",file.head())

print("The first ten rows are:",file.head(10))

print("Basic statistics are:",file.describe(include='all'))

print("The last five rows are:",file.tail())

print("Basic statistics of 2nd column is:", file.describe(include='all').Location)
