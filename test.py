import pandas as pd
import glob
import os

# Define the path to the CSV files
path = r'data'

# Identify all CSV files with the specific pattern
all_files = glob.glob(os.path.join(path, "*CLEAN.csv"))

# Merge all CSV files into one DataFrame
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
print(df)
# The genre with the most releases:
# import pandas as pd
# data = pd.read_csv('./data/January-March.csv')
#
# genre_counts = data.groupby('Genre(s)').size().reset_index(name='count')
# genre_counts = genre_counts.sort_values(by='count', ascending=False)
#
# print('The genre with the most releases is', genre_counts.iloc[0]['Genre(s)'])


# The title that is mentioned the most:
# import pandas as pd
#
# df = pd.read_csv("./data/Critically_acclaimed_games.csv")
#
# title_count = df["Title"].value_counts()
#
# most_mentioned_title = title_count.index[0]
#
# print("The title that is mentioned the most is:", most_mentioned_title)


# Which csv file out of January-March.csv, April-June.csv, July-September.csv, October-December.csv has the most titles:
# import pandas as pd
#
# df_jan_mar = pd.read_csv('./data/January-March.csv')
# df_apr_jun = pd.read_csv('./data/April-June.csv')
# df_jul_sep = pd.read_csv('./data/July-September.csv')
# df_oct_dec = pd.read_csv('./data/October-December.csv')
#
# num_titles_jan_mar = df_jan_mar.shape[0]
# num_titles_apr_jun = df_apr_jun.shape[0]
# num_titles_jul_sep = df_jul_sep.shape[0]
# num_titles_oct_dec = df_oct_dec.shape[0]
#
# title_counts = {
#     'January-March.csv': num_titles_jan_mar,
#     'April-June.csv': num_titles_apr_jun,
#     'July-September.csv': num_titles_jul_sep,
#     'October-December.csv': num_titles_oct_dec
# }
#
# max_file = max(title_counts, key=lambda k: title_counts[k])
#
# print(max_file)
#
#
# # Which Month has the most titles.
# # import pandas as pd
#
# df_jul_sep = pd.read_csv('./data/July-September.csv')
#
# month_titles = df_jul_sep[['Month', 'Title']]
# month_counts = month_titles.groupby('Month').count()
# max_month = month_counts['Title'].idxmax()
#
# print(max_month)
