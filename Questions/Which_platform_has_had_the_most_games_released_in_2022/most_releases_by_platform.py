import pandas as pd

df_jan_mar = pd.read_csv('../../data/January-March-CLEAN.csv')
df_apr_jun = pd.read_csv('../../data/April-June-CLEAN.csv')
df_jul_sep = pd.read_csv('../../data/July-September-CLEAN.csv')
df_oct_dec = pd.read_csv('../../data/October-December-CLEAN.csv')

df = pd.concat([df_jan_mar[['Platform(s)', 'Genre(s)']],
                df_apr_jun[['Platform(s)', 'Genre(s)']],
                df_jul_sep[['Platform(s)', 'Genre(s)']],
                df_oct_dec[['Platform(s)', 'Genre(s)']]])

df['Genre(s)'].fillna('Unknown', inplace=True)

platform_counts = {}

for platforms in df.loc[pd.notnull(df['Platform(s)']), 'Platform(s)'].str.split(", "):
    for platform in platforms:
        if platform in platform_counts:
            platform_counts[platform] += 1
        else:
            platform_counts[platform] = 1

most_releases = max(platform_counts, key=platform_counts.get)
print(most_releases)
