# Which Month had the most released games in 2022?

import pandas as pd

# Load each csv file into a pandas DataFrame:
df_jan_mar = pd.read_csv('../data/January-March.csv')
df_apr_jun = pd.read_csv('../data/April-June.csv')
df_jul_sep = pd.read_csv('../data/July-September.csv')
df_oct_dec = pd.read_csv('../data/October-December.csv')

# Get the number of titles in each DataFrame using the shape attribute and selecting the number of rows:
# Ex: rdf_jan_mar.shape[0] returns the number of rows in the dataframe df_jan_mar,
#   which is equivalent to the number of titles in the January-March period.
num_titles_jan_mar = df_jan_mar.shape[0]
num_titles_apr_jun = df_apr_jun.shape[0]
num_titles_jul_sep = df_jul_sep.shape[0]
num_titles_oct_dec = df_oct_dec.shape[0]

# Create a dictionary with the number of titles for each DataFrame:
title_counts = {
    'January-March.csv': num_titles_jan_mar,
    'April-June.csv': num_titles_apr_jun,
    'July-September.csv': num_titles_jul_sep,
    'October-December.csv': num_titles_oct_dec
}

# Find the key (i.e., the filename) with the maximum value
#   (i.e., the highest number of titles) using the max function and a lambda function:
# Finally, max(title_counts, key=lambda k: title_counts[k]) returns the key (i.e., the CSV filename)
#   with the maximum value (i.e., the file with the most titles).
#   This key is then assigned to the variable max_file.
max_file = max(title_counts, key=lambda k: title_counts[k])

print(f"The month period with the most games is {max_file}")


# Find the month with the most titles across all files

# Concat all dataframes into one and extract the "Month" and "Title" columns:
all_months = pd.concat([df_jan_mar[['Month', 'Title']],
                        df_apr_jun[['Month', 'Title']],
                        df_jul_sep[['Month', 'Title']],
                        df_oct_dec[['Month', 'Title']]])

# It groups the titles by month and counts the number of titles in each month:
month_counts = all_months.groupby('Month').count()
max_month = month_counts['Title'].idxmax()

print(f"The month with the most games released is {max_month}")



# jan: 57
# feb: 74
# mar: 72
# apr: 65
# maj: 84
# jun: 128
# jul: 117
# aug: 100
# sep: 120
# okt: 82
# nov: 81
# dec: 56