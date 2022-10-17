import pandas as pd
import os

df = pd.read_csv(os.path.dirname(__file__) + "/../data/global-energy-substitution.csv")

df = df.drop(['Biofuels (TWh, substituted energy)', 'Other renewables (TWh, substituted energy)', 'Traditional biomass (TWh, substituted energy)'], axis=1)

col_list = list(df.columns)

df_long = pd.melt(df, id_vars=["Entity","Code","Year"], value_vars=col_list)

df_long = df_long.rename(columns={"value": "Energy", "variable": "Type"})

df_long.to_csv(os.path.dirname(__file__) + "/../data/global-data-cleaned.csv")