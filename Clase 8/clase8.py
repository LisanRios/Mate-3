import pandas as pd
cols = ['Date', 'Time', 'Latitude', 'Longitude', 'Depth', 'Magnitude Type']
df_e = pd.read_csv(f'archs/earthquakes_1965_2016_database.csv.zip', dtype=str)[cols]
print(df_e)