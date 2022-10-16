import pandas as pd
import os
# import chardet
# import copy

product_df = pd.read_csv(os.path.dirname(__file__) + "/../data/product_codes_HS92_V202201.csv", encoding='ascii')

country_df = pd.read_csv(os.path.dirname(__file__) + '/../data/country_codes_V202201.csv', encoding='ISO-8859-1')

product_filters = ['petroleum', 'coal', 'carbon' 'natural gas', 'ores', 'electrical energy']


mask = product_df.iloc[:, 1].str.contains(r'\b(?:{})\b'.format('|'.join(product_filters)))
product_df = product_df[mask]

# with open(os.path.dirname(__file__) + '/../data/exports-imports/product_codes_HS92_V202201.csv', 'rb') as file:
#     print(chardet.detect(file.read()))


print(product_df)