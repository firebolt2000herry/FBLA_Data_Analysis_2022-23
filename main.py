import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np


files = {
    'Datasets/GDP (current US$).xls - Data (1).csv' : ['Canada', 'China', 'France', 'United States'],
    'Datasets/GDP growth (annual %).xls - Data.csv' : ['Canada', 'China', 'France', 'United States'],
    'Datasets/GDP per capita (current US$).xls - Data.csv' : ['Canada', 'China', 'France', 'United States'],
    'Datasets/Inflation, consumer prices (annual %).xls - Data.csv' : ['Canada', 'China', 'France', 'United States'],
    'Datasets/Life expectancy at birth, total (years).xls - Data.csv' : ['Canada', 'China', 'France', 'United States'],
    'Datasets/Net migration.xls - Data.csv' : ['Canada', 'China', 'France', 'United States'],
    'Datasets/Personal remittances, received (% of GDP).xls - Data.csv' : ['Canada', 'China', 'France', 'United States'],
    'Datasets/Population growth (annual %).xls - Data.csv' : ['Canada', 'China', 'France', 'United States'],
    'Datasets/Population, total.xls - Data.csv' : ['Canada', 'China', 'France', 'United States'],
    'Datasets/Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population).xls - Data.csv' : ['Canada', 'China', 'France', 'United States'],
    'Datasets/Unemployment, total (% of total labor force) (modeled ILO estimate).xls - Data.csv' :  ['Canada', 'China', 'France', 'United States']
}
files2 = {
    'Datasets/Human Capital Index (HCI) (scale 0-1).xls - Data.csv' : ['Canada', 'China', 'France', 'United States']
}

for filename, l in files.items():
    df = pd.read_csv(filename, skiprows=3)
    df = df.fillna(0)
    df = df[df['Country Name'].isin(l)]
    df = df.reset_index(drop=True)
    for year in range(1960, 2021):
        df[str(year)] = df[str(year)].astype('int64') 
    print(filename)
    print(df)
    print('\n')


for filename, l in files2.items():
    df = pd.read_csv(filename, skiprows=3)
    df = df.fillna(0)
    df = df[df['Country Name'].isin(l)]
    df = df.reset_index(drop=True)
    for year in range(2010, 202):
        df[str(year)] = df[str(year)].astype('int64') 
    print(filename)
    print(df)
    print('\n')








