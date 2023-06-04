import pandas as pd
import csv

df_jan_mar = pd.read_csv('../../data/January-March-CLEAN.csv')
df_apr_jun = pd.read_csv('../../data/April-June-CLEAN.csv')
df_jul_sep = pd.read_csv('../../data/July-September-CLEAN.csv')
df_oct_dec = pd.read_csv('../../data/October-December-CLEAN.csv')

concatenated_df = pd.concat([df_jan_mar, df_apr_jun, df_jul_sep, df_oct_dec])
developers = concatenated_df["Developer(s)"]

game_counts = developers.value_counts()
most_releases = game_counts.idxmax()
count = game_counts[most_releases]

print(f"Most releases: {most_releases}, released {count} times.")
