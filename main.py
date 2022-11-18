import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

%matplotlib inline
countries = ['Canada', 'China', 'France', 'United States']
special_filename = 'Human Capital Index (HCI) (scale 0-1)'
files = [
    'GDP (current US$)',
    'GDP growth (annual %)',
    'GDP per capita (current US$)',
    'Inflation, consumer prices (annual %)',
    'Life expectancy at birth, total (years)',
    'Net migration',
    'Personal remittances, received (% of GDP)',
    'Population growth (annual %)',
    'Population, total',
    'Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population)',
    'Unemployment, total (% of total labor force) (modeled ILO estimate)',
    special_filename,
]
dfs = []

for filename in files:
    df = pd.read_csv(f'Datasets/{filename}.xls - Data.csv', skiprows=3).fillna(0)
    df = df[df['Country Name'].isin(countries)]
    df = df.reset_index(drop=True)
    year_range = [2010, 2020] if filename == special_filename else [1960, 2021]
    for year in range(year_range[0], year_range[1]+1):
        df[str(year)] = df[str(year)].astype('int64') 
    print(f'{filename}\n{df}\n')
    dfs.append([filename, df])

# print(dfs)
q