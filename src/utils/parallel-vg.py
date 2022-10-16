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
    # df = df[df[key] != 0]

df['key'] = 'GDP per capita'
res = pd.DataFrame()

for key in keys:
    tmp = copy.deepcopy(df)
    tmp['key'] = key
    tmp['value'] = tmp[key]
    res = pd.concat([res, tmp], axis=0)

# Duplicate each row four times
# df['value'] = df['GDP per capita']
# df1 = copy.deepcopy(df)
# df2 = copy.deepcopy(df)
# df3 = copy.deepcopy(df)


# df1['key'] = 'Fossil fuel electricity per capita (kWh)'
# df1['value'] = df1['Fossil fuel electricity per capita (kWh)']
# df2['key'] = 'Nuclear electricity per capita (kWh)'
# df2['value'] = df2['Nuclear electricity per capita (kWh)']
# df3['key'] = 'Renewable electricity per capita (kWh)'
# df3['value'] = df3['Renewable electricity per capita (kWh)']

# df = pd.concat([df,df1,df2,df3], axis=0)

res.to_csv(os.path.dirname(__file__) + '/../data/parallel.csv')
