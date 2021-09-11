import pandas as pd
import numpy as np

df = pd.read_csv("manuf_data.csv",header=0, index_col=0, quotechar='"',sep='[,;]', engine='python', na_values = ['na', '-', '.', '', ';'] )
print(df)

df.head()