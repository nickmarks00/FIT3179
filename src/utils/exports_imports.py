import pandas as pd
import os
import chardet
import copy

product_df = pd.read_csv(os.path.dirname(__file__) + "/../../data/exports-imports/product_codes_HS92_V202201.csv", encoding='ascii')

country_df = pd.read_csv(os.path.dirname(__file__) + '/../../data/exports-imports/country_codes_V202201.csv', encoding='ISO-8859-1')

product_filters = ['petroleum', ('coal', 'carbon'), 'natural gas', 'ores', 'electrical energy']


for filter in product_filters:

    if type(filter) == str:
        product_df_filter = product_df['description'].str.contains(filter).to_frame()

        pf = product_df[product_df_filter['description']]
    else:
        pf1 = product_df['description'].str.contains(filter[0])
        pf2 = product_df['description'].str.contains(filter[1])

        pf = product_df[pf1['description'] or pf2['description']]


# with open(os.path.dirname(__file__) + '/../data/exports-imports/product_codes_HS92_V202201.csv', 'rb') as file:
#     print(chardet.detect(file.read()))


print(len(product_df))