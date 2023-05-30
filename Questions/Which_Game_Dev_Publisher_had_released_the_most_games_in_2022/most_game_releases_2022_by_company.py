import pandas as pd
import csv

df_jan_mar = pd.read_csv('../../data/January-March-CLEAN.csv')
df_apr_jun = pd.read_csv('../../data/April-June-CLEAN.csv')
df_jul_sep = pd.read_csv('../../data/July-September-CLEAN.csv')
df_oct_dec = pd.read_csv('../../data/October-December-CLEAN.csv')

df = pd.concat([df_jan_mar[['Platform(s)', 'Genre(s)']],
                df_apr_jun[['Platform(s)', 'Genre(s)']],
                df_jul_sep[['Platform(s)', 'Genre(s)']],
                df_oct_dec[['Platform(s)', 'Genre(s)']]])

df['Genre(s)'].fillna('Unknown', inplace=True)

game_counts = {}

for df_chunk in [df_jan_mar, df_apr_jun, df_jul_sep, df_oct_dec]:
    developers = df_chunk["Developer(s)"].str.split("; ")
    for dev_list in developers:
        if pd.notnull(dev_list) and dev_list:
            for dev in dev_list:
                if dev in game_counts:
                    game_counts[dev] += 1
                else:
                    game_counts[dev] = 1

most_releases = max(game_counts, key=game_counts.get)
count = game_counts[most_releases]
print("Most releases: " + str(most_releases) + ", released " + str(count) + " times.")
