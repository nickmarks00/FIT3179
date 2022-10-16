import pandas as pd
import os

cols = [i for i in range(0, 58)]

df = pd.read_csv(os.path.dirname(__file__) + '/../data/bp-stats-review-2022-all-data.csv', header=2, usecols=cols, comment="#")

year_list = list(df.columns)

df_long = pd.melt(df, id_vars="Country", value_vars=year_list)

df_long = df_long.rename(columns={"variable": "Year", "value": "Energy"})

df_long.to_csv(os.path.dirname(__file__) + '/../data/bp-data-cleaned.csv')