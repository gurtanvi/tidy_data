import pandas as pd
import numpy as np

df = pd.read_csv("manuf_data.csv",header=0, index_col=0, quotechar='"',sep='[,;]', engine='python', na_values = ['na', '-', '.', '', ';'] )
print(df)

cols_to_drop = ['prodid', 'station_id.1']
df_pruned = df.drop(cols_to_drop, inplace=True, axis=1)


final_dataset = df.pivot_table(index=['prod_id','station_id','part_id'], columns=['sensor'], values='value', aggfunc='first')
print(final_dataset)
