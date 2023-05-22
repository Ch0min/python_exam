import pandas as pd

# Load hver csv file til et Pandas DataFrame:
df_jan_mar = pd.read_csv('../data/January-March.csv')
df_apr_jun = pd.read_csv('../data/April-June.csv')
df_jul_sep = pd.read_csv('../data/July-September.csv')
df_oct_dec = pd.read_csv('../data/October-December.csv')


# Tager fat i titles i hver DataFrame, samt bruger vi shape attributten til, at vælge rows.
num_titles_jan_mar = df_jan_mar.shape[0]
num_titles_apr_jun = df_apr_jun.shape[0]
num_titles_jul_sep = df_jul_sep.shape[0]
num_titles_oct_dec = df_oct_dec.shape[0]

# Opretter vi et Dictionary med antallet af titles/games for hver DataFrame.
title_counts = {
    'January-March.csv': num_titles_jan_mar,
    'April-June.csv': num_titles_apr_jun,
    'July-September.csv': num_titles_jul_sep,
    'October-December.csv': num_titles_oct_dec
}

# Tager fat i title_counts Dict og returnere the key (CSV filnavn) med den mindste value.
# key=lambda k: title_counts[k] tager fat i alle keys i title_counts Dict, og sammenligner, hvem der har mindst titler.
min_file = min(title_counts, key=lambda k: title_counts[k])

print(f"The month period with the least games is {min_file}")


# Find kun den ene måned med mindst titler.

# Concat alle DataFrames til et, og tag fat i "Month" og "Title" kolonnerne.
all_months = pd.concat([df_jan_mar[['Month', 'Title']],
                        df_apr_jun[['Month', 'Title']],
                        df_jul_sep[['Month', 'Title']],
                        df_oct_dec[['Month', 'Title']]])


# Groups titler af "Month" og optæller antallet af titler i hver måned.
month_counts = all_months.groupby('Month').count()
min_month = month_counts['Title'].idxmin()

print(f"The month with the least games released is {min_month}")



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