import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_jan_mar = pd.read_csv('../../data/January-March-CLEAN.csv')
df_apr_jun = pd.read_csv('../../data/April-June-CLEAN.csv')
df_jul_sep = pd.read_csv('../../data/July-September-CLEAN.csv')
df_oct_dec = pd.read_csv('../../data/October-December-CLEAN.csv')

# Concat all dataframes into one and extract the "Month" and "Title" columns:
df = pd.concat([df_jan_mar[['Platform(s)', 'Genre(s)']],
                df_apr_jun[['Platform(s)', 'Genre(s)']],
                df_jul_sep[['Platform(s)', 'Genre(s)']],
                df_oct_dec[['Platform(s)', 'Genre(s)']]])

# Handle missing values in the genre column
df['Genre(s)'].fillna('Unknown', inplace=True)

# Specify the 5 genres you want to focus on
genres_of_interest = ['Puzzle', 'Adventure', 'First-person shooter', 'Role-playing', 'Simulation']

# Filter the DataFrame to include only the specified genres
filtered_df = df[df['Genre(s)'].isin(genres_of_interest)]

# Plot the bar chart
plt.figure(figsize=(12, 6))
sns.countplot(data=filtered_df, x='Genre(s)', hue='Platform(s)')
plt.xticks(rotation=45)
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Distribution of Platforms for Selected Genres')
plt.legend(title='Platform')
plt.tight_layout()
plt.show()
