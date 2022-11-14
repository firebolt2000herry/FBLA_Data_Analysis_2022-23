import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import numpy as np

df = pd.read_csv("./Datasets/GDP (current US$).xls - Data (1).csv")
print(df['Country Name'])