import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import numpy as np

df = pd.read_csv("./Datasets/GDP (current US$).xls - Data (1).csv")
df = df.drop([0, 1])
print(df)




#df = df.loc[3:, :].reset
#print(df)