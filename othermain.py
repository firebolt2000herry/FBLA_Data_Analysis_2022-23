import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split


countries = ['Canada', 'China', 'France', 'United States']
df = pd.read_csv('Datasets/GDP (current US$).xls - Data.csv', skiprows=3).fillna(0)
df = df[df['Country Name'].isin(countries)]
df = df.reset_index(drop=True)

df.plot(kind='scatter', x='1999', y='')