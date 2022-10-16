import pandas as pd
import numpy as np
import os
import copy

gdp_df = pd.read_csv(os.path.dirname(__file__) + "/../data/consumption-co2-per-capita-vs-gdppc.csv")

fuel_type_df = pd.read_csv(os.path.dirname(__file__) + "/../data/per-capita-electricity-fossil-nuclear-renewables.csv")

country_cont_df = pd.read_csv(os.path.dirname(__file__) + '/../data/country-continent.csv')

df = pd.merge(gdp_df, fuel_type_df, how='left', on=['Entity','Year'])
df = pd.merge(df,country_cont_df, how='left', on=['Entity'])

# Clean empty rows
keys = ['GDP per capita', 'Fossil fuel electricity per capita (kWh)', 'Nuclear electricity per capita (kWh)', 'Renewable electricity per capita (kWh)']
for key in keys:
    df = df[~df[key].isnull()]

# df['key'] = 'GDP per capita'
# res = pd.DataFrame()

# for key in keys:
#     tmp = copy.deepcopy(df)
#     tmp['key'] = key
#     tmp['value'] = tmp[key]
#     min_val, max_val = tmp[key].min(), tmp[key].max()
#     tmp['min'], tmp['max'] = min_val, max_val
#     tmp['mid'] = (max_val + min_val) / 2
#     tmp['norm_val'] = (tmp['value'] - tmp['min']) / (max_val - min_val)
#     res = pd.concat([res, tmp], axis=0)


df = df.rename(columns = {'GDP per capita': '4 - GDP', 'Fossil fuel electricity per capita (kWh)': '1 - Fossil Fuels', 'Nuclear electricity per capita (kWh)': '3 - Nuclear', 'Renewable electricity per capita (kWh)': '2 - Renewable', 'Continent_y': 'Continent/region'})

df.to_csv(os.path.dirname(__file__) + '/../data/parallel.csv')
