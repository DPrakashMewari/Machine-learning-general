import pickle
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("mushrooms.csv")
df.head()
print(df.columns)

#
print(df['class'].value_counts())
# Value count of edible 4208 , poison is 3916

#
print(df['cap-shape'].value_counts())
