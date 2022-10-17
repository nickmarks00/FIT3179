import pandas as pd
import os
# import chardet

# with open(os.path.dirname(__file__) + '/../data/BACI_HS92_Y2020_V202201.csv', 'rb') as file:
#     print(chardet.detect(file.read()))

product_df = pd.read_csv(os.path.dirname(__file__) + "/../data/product_codes_HS92_V202201.csv", encoding='ascii')

trade_df = pd.read_csv(os.path.dirname(__file__) + "/../data/BACI_HS92_Y2020_V202201.csv", encoding='ascii')

country_df = pd.read_csv(os.path.dirname(__file__) + '/../data/country_codes_V202201.csv', encoding='ISO-8859-1')

product_filters = ['petroleum', 'coal', 'carbon' 'natural gas', 'ores', 'electrical']
country_list = ['Australia', 'Canada', 'Russian Federation', 'China', 'France', 'Germany', 'USA', 'United Kingdom', 'India', 'Indonesia', 'South Africa', 'United Arab Emirates', 'Saudi Arabia']

# Remove non numeric data
trade_df = trade_df[~trade_df['q'].str.contains('NA')]

# Filter product codes
mask = product_df.iloc[:, 1].str.contains(r'\b(?:{})\b'.format('|'.join(product_filters)))
product_df = product_df[mask]

product_codes = list(map(int, product_df['code'].tolist()))

# Filter country codes
country_cleaned = country_df[country_df['country_name_abbreviation'].isin(country_list)]
country_cleaned = country_cleaned.reset_index(drop=True)

# Filter trades
trade_df = trade_df[(trade_df['i'].isin(country_cleaned['country_code'])) & (trade_df['j'].isin(country_cleaned['country_code']))]

trade_df = trade_df[trade_df['k'].isin(product_codes)]

merged_trades = trade_df.groupby(['i', 'j'])['v'].sum().reset_index()

merged_trades.to_csv(os.path.dirname(__file__) + "/../data/2020_trades.csv")
country_cleaned.to_csv(os.path.dirname(__file__) + '/../data/country_nodes.csv')
